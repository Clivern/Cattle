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

import json

from jsonschema import validate
from jsonschema import ValidationError

from django.utils.translation import gettext as _

from app import APP_ROOT
from app.util.logger import Logger


class Validator():
    """Validator Class"""

    def __init__(self):
        """Inits Validator"""
        self.logger = Logger().get_logger(__name__)

    def validate(self, data, schema_path):
        """
        Validate data against JSON schema

        Args:
            data: A JSON or dict to validate
            schema_path: absolute path to schema file

        Returns:
            True if data is valid and False otherwise
        """
        self.error = ""
        f = open(schema_path, "r")
        schema = json.loads(f.read())

        # Convert to dict if data is string
        if not isinstance(data, dict):
            try:
                data = json.loads(data)
            except Exception:
                self.error = _("Invalid request data")
                return False

        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            error_field = ""
            if "id" in e.schema.keys():
                error_field = _("Invalid field {}: ").format(e.schema["id"])

            self.error = error_field + str(e.message)

            return False

        return True

    def get_schema_path(self, rel_path):
        """
        Get absolute path to JSON schema file

        Args:
            rel_path: a relative path to JSON schema file from app root

        Returns:
            Absolute path to JSON schema file
        """
        return "{root}{rel_path}".format(root=APP_ROOT, rel_path=rel_path)

    def get_error(self):
        """
        Get validation error message

        Returns:
            An error or empty string
        """
        return self.error

    def is_positive_integer(self, value, min=0):
        """
        Validate if a value is integer and more than a certain value

        Args:
            value: the value to validate
            min: a minimum value

        Returns:
            True if value is valid and False otherwise
        """
        if not value.isdigit():
            return False

        try:
            value = int(value)
        except Exception:
            return False

        if value < min:
            return False

        return True
