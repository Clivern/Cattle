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

import logging
from threading import local

import uuid


_locals = local()


class Correlation():
    """
    Correlation Middleware

    Add a unique correlation ID to all incoming requests

    Attributes:
        get_response: a callable function
    """

    def __init__(self, get_response):
        """Inits Correlation"""
        self.get_response = get_response

    def __call__(self, request):
        """Execute Middleware

        Args:
            request: request instance
        """
        request.META["X-Correlation-ID"] = str(uuid.uuid4())

        _locals.correlation_id = request.META["X-Correlation-ID"]

        response = self.get_response(request)

        response['X-Correlation-ID'] = request.META["X-Correlation-ID"]

        return response


class CorrelationFilter(logging.Filter):
    """
    Correlation Filter

    Append the correlation ID to all log records
    """

    def filter(self, record):
        if not hasattr(record, 'correlation_id'):
            record.correlation_id = ""

        if hasattr(_locals, 'correlation_id'):
            record.correlation_id = _locals.correlation_id

        return True
