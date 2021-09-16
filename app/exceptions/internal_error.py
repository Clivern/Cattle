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
from app.exceptions.server_error import ServerError


class InternalError(ServerError):
    """Client Error Custom Exception"""

    def __init__(self, message, http_status_code=HTTPStatus.INTERNAL_SERVER_ERROR, error_code=ErrorCodes.SERVER_ERROR):
        """Inits InternalError"""
        ServerError.__init__(self, message, http_status_code, error_code)
