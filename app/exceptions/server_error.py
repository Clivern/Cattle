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

from http import HTTPStatus

from app.exceptions.error_codes import ErrorCodes


class ServerError(Exception):
    """ServerError Custom Exception

    Attributes:
        http_status_code: HTTP status code to respond with
        error_code: a dict of error info
    """

    def __init__(self, message, http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR, error_code=ErrorCodes.SERVER_ERROR):
        """Inits ServerError"""
        Exception.__init__(self, message)
        self.http_status_code = http_status_code
        self.error_code = error_code

    def get_http_status_code(self):
        """Get error HTTP status code to respond with

        Returns:
            HTTP status code
        """
        return self.http_status_code

    def get_error_code(self):
        """Get error code and reference

        Returns:
            A dict containing error code and reference
        """
        return self.error_code
