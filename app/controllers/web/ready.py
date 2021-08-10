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

from django.views import View
from django.http import JsonResponse

from app.module.readiness import Readiness
from app.controllers.controller import Controller


class Ready(View, Controller):
    """Ready Page Controller"""

    def get(self, request):
        readiness = Readiness()

        if not readiness.check_db_connection():
            return JsonResponse({
                "status": "down",
                "errorMessage": "Error while connecting to the database"
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        # Check workers speed
        if not readiness.check_workers(30):
            return JsonResponse({
                "status": "down",
                "errorMessage": "Workers are damn slow"
            }, status=HTTPStatus.INTERNAL_SERVER_ERROR)

        return JsonResponse({
            "status": "up"
        })
