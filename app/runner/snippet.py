# Copyright 2021 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import json
from multiprocessing import Process, Manager

from pindo.runner import Runner

from app.shortcuts import Logger


def execute_code(engine, output):
    """
    Execute the code

    Args:
        engine: the engine instance
        output: the var to store the result
    """
    logger = Logger().get_logger(__name__)

    try:
        engine.setup()
        r = engine.run()
    except Exception as e:
        output['result'] = {
            "output": "Failed to run the code",
            "build_time": None,
            "execution_time": None,
        }
        logger.error("Failed to run the code {}".format(str(e)))
        return

    output['result'] = r


class Snippet():
    """Snippet Class"""

    def __init__(self, id, content, language, version, timeout=60):
        self._id = id
        self._content = content
        self._language = language
        self._version = version
        self._timeout = timeout
        self.logger = Logger().get_logger(__name__)

    def run(self):
        """
        Run The Code

        Returns:
            The result as dict
        """
        self.logger.info("Run the {} code version {} with uuid {}".format(
            self._language,
            self._version,
            self._id
        ))

        self.logger.debug("Code has a content {}".format(self._content))

        if self._language == "go":
            code = Runner.go(self._content, self._version, self._id)

        elif self._language == "java":
            try:
                main_class = re.search("public class(.*?){", self._content).group(1).strip()
                code = Runner.java(self._content, self._version, self._id, {"main_class": main_class})
            except Exception:
                self.logger.error("Invalid Java Code: Main class in missing")
                self.logger.debug("Code has a content {}".format(self._content))
                raise Exception("Invalid Java Code: Main class in missing")

        elif self._language == "php":
            code = Runner.php(self._content, self._version, self._id)

        elif self._language == "ruby":
            code = Runner.ruby(self._content, self._version, self._id)

        elif self._language == "python":
            code = Runner.python(self._content, self._version, self._id)

        elif self._language == "rust":
            code = Runner.rust(self._content, self._version, self._id)

        else:
            self.logger.error("Invalid programming language {}".format(self._language))
            raise Exception("Invalid programming language {}".format(self._language))

        engine = Runner.docker(code)

        manager = Manager()
        out = manager.dict()

        p = Process(target=execute_code, args=(engine, out))
        p.start()
        p.join(timeout=self._timeout)
        p.terminate()

        try:
            engine.cleanup()
        except Exception as e:
            self.logger.warning("Error while doing cleanup: {}".format(str(e)));

        # Code is damn slow
        if p.exitcode is None:
            # $_timeout exceeded
            return {
                "output": "Maximum execution time ({} seconds) reached".format(self._timeout),
                "build_time": None,
                "execution_time": None,
            }

        return out['result']

    @classmethod
    def from_string(cls, data):
        """
        Get Code from JSON string

        Args:
            data: the JSON string

        Returns:
            An instance of this class
        """
        data = json.loads(data)

        return cls(
            data['id'],
            data['content'],
            data['language'],
            data['version'],
            data['timeout']
        )

    def __str__(self):
        """
        Convert the Object to string

        Returns:
            A JSON representation of this instance
        """
        return json.dumps({
            'id': self._id,
            'content': self._content,
            'language': self._language,
            'version': self._version,
            'timeout': self._timeout,
        })

    @property
    def id(self):
        """
        Gets the ID
        """
        return self._id

    @property
    def content(self):
        """
        Gets the Content
        """
        return self._content

    @property
    def timeout(self):
        """
        Gets the Timeout
        """
        return self._timeout

    @property
    def language(self):
        """
        Gets the Language
        """
        return self._language

    @property
    def version(self):
        """
        Gets the Version
        """
        return self._version
