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

from django.http import JsonResponse
from django.utils.translation import gettext as _

from app.shortcuts import Logger
from app.exceptions.client_error import ClientError
from app.exceptions.server_error import ServerError
from app.exceptions.error_codes import ErrorCodes


class Errors():
    """
    Errors Middleware

    Logs stacktrace incase of client or server errors raised. also to send a custom response

    Attributes:
        get_response: a callable function
        logger: An instance of Logger class
    """

    def __init__(self, get_response):
        """Inits Errors"""
        self.get_response = get_response
        self.logger = Logger().get_logger(__name__)

    def __call__(self, request):
        """Execute Middleware

        Args:
            request: request instance
        """
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """Proccess Exceptions

        Args:
            request: request instance
            exception: thrown exception instance

        Returns:
            an instance of JsonResponse
        """
        if isinstance(exception, ClientError):
            # Log client errors for debugging purposes
            # client errros like unauthorized access or invalid request data
            self.logger.debug(
                _("Client error thrown {method}:{path}  - {name} - {exception}").format(
                    method=request.method,
                    path=request.path,
                    name=exception.__class__.__name__,
                    exception=exception
                )
            )
        else:
            self.logger.error(
                _("The server encountered something unexpected! {method}:{path}  - {name} - {exception}").format(
                    method=request.method,
                    path=request.path,
                    name=exception.__class__.__name__,
                    exception=exception
                )
            )
            self.logger.exception(exception)

        if isinstance(exception, ClientError):
            if "Accept" in request.headers.keys() and "text/html" in request.headers['Accept']:
                return

            # Incase of client error, send json response with the error message, error code and reference
            return JsonResponse({
                'errorCode': exception.get_error_code()["code"],
                'errorMessage': str(exception),
                'correlationId': request.META["X-Correlation-ID"],
                'reference': exception.get_error_code()["reference"]
            }, status=exception.get_http_status_code())

        elif isinstance(exception, ServerError):
            if "Accept" in request.headers.keys() and "text/html" in request.headers['Accept']:
                return

            # Incase of server error, send json response with a generic message, error code and reference
            return JsonResponse({
                'errorCode': exception.get_error_code()["code"],
                'errorMessage': _("Internal Server Error!"),
                'correlationId': request.META["X-Correlation-ID"],
                'reference': exception.get_error_code()["reference"]
            }, status=exception.get_http_status_code())

        else:
            if "Accept" in request.headers.keys() and "text/html" in request.headers['Accept']:
                return

            # Incase of other unexpected errors, send json response with a generic message, default error code and reference
            return JsonResponse({
                'errorCode': ErrorCodes.SERVER_ERROR["code"],
                'errorMessage': _("Something goes wrong! Please contact a system administrator."),
                'correlationId': request.META["X-Correlation-ID"],
                'reference': ErrorCodes.SERVER_ERROR["reference"]
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)
