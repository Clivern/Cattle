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

import random
import string


class Random():
    """Random Class"""

    @classmethod
    def token(cls, length):
        """
        Generate a Token

        Args:
            cls: class instance
            length: the length

        Returns:
            The random string
        """
        characters = string.ascii_letters + string.digits

        return ''.join(random.choice(characters) for i in range(length)).lower()

    @classmethod
    def rand_int(cls, min, max):
        """
        Generate a Random Int

        Args:
            cls: class instance
            min: the min int
            max: the max int

        Returns:
            The random int
        """
        return random.randint(min, max)
