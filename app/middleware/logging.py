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

import time

from django.http import JsonResponse
from django.utils.translation import gettext as _

from app.shortcuts import Logger


class Logging():
    """
    Logging Middleware

    Logs incoming requests and outgoing response with latency in millisec

    Attributes:
        get_response: a callable function
        logger: An instance of Logger class
    """

    def __init__(self, get_response):
        """Inits Logging"""
        self.get_response = get_response
        self.logger = Logger().get_logger(__name__)

    def __call__(self, request):
        """Execute Middleware

        Args:
            request: request instance
        """
        start_time = time.time()

        self.logger.info(_("Incoming {method} Request to {path} with {body} and headers {headers}").format(
            method=request.method,
            path=request.path,
            body=request.body,
            headers=request.headers
        ))

        response = self.get_response(request)

        resp_time = (time.time() - start_time) * 1000

        if isinstance(response, JsonResponse):
            self.logger.info(_("Outgoing {status} Response to {path} with {body} and latency {latency_millisec} millisec").format(
                status=response.status_code,
                path=request.path,
                body=response.content,
                latency_millisec=resp_time
            ))
        else:
            self.logger.info(_("Outgoing {status} Response to {path}: <html>.. and latency {latency_millisec} millisec").format(
                status=response.status_code,
                path=request.path,
                latency_millisec=resp_time
            ))

        return response
