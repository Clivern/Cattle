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

import os

from app.repository.option_repository import OptionRepository


def get_config(key, default=""):
    # Load from env vars
    value = os.getenv(key.upper(), "_not_set_")

    if value != "_not_set_":
        return os.getenv(key.upper(), default)

    # Load from database
    option_repository = OptionRepository()
    option = option_repository.get_one_by_key(key.lower())

    if option:
        return option.value

    return default
