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

import base64


class Encoder():
    """Encoder Class"""

    def b64encode(self, text):
        """Encode text"""
        return str(base64.b64encode(bytes(text, 'utf-8')), "utf-8")

    def b64decode(self, encoded):
        """Decode encoded text"""
        return base64.b64decode(encoded).decode("utf-8")
