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

from pindo.runner import Runner

from app.util.file_system import FileSystem


class Snippet():
    """Snippet Class"""

    def __init__(self, id, content, language, version):
        self._fs = FileSystem()
        self._id = id
        self._content = content
        self._language = language
        self._version = version

    def run(self):
        """
        Run The Code

        Returns:
            The result as dict
        """
        if self._language == "go":
            code = Runner.go(self._content, self._version, self._id)

        elif self._language == "java":
            try:
                main_class = re.search("public class(.*?){", code).group(1).strip()
                code = Runner.java(self._content, self._version, self._id, {"main_class": main_class})
            except Exception:
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
            raise Exception("Invalid programming language {}".format(self._language))

        engine = Runner.docker(self._fs.storage_path("mount"), code)

        engine.setup()
        result = engine.run()
        engine.cleanup()

        return result

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
            data['version']
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
            'version': self._version
        })

    @property
    def id(self):
        return self._id

    @property
    def content(self):
        return self._content

    @property
    def language(self):
        return self._language

    @property
    def version(self):
        return self._version
