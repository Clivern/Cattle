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

from django.core.management.base import BaseCommand

from app.util.file_system import FileSystem


class Command(BaseCommand):
    """Build UI Index Page"""

    help = "Build UI Index Page"

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Start Building Index Page')

        try:
            self.file_system = FileSystem()

            path = self.file_system.app_path("themes/default/templates/index.html")
            content = self.file_system.read_file(path)

            urls = re.findall(r'href=[\'"]?([^\'" >]+)', content)
            urls = list(dict.fromkeys(urls))

            for url in urls:
                if url.startswith("/static"):
                    url = url.replace("/static/", "")
                    content = content.replace("/static/" + url, "{% " + "static '{}'".format(url) + " %}")

            self.file_system.write_file(path, content)
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error: {}'.format(str(e))))
            return

        self.stdout.write(self.style.SUCCESS('Done!'))
