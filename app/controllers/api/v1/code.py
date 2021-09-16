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

from django.views import View

from app.controllers.controller import Controller


class CreateCode(View, Controller):
    """CreateCode Endpoint Controller"""

    def __init__(self):
        pass

    def post(self, request):
        pass


class UpdateCode(View, Controller):
    """UpdateCode Endpoint Controller"""

    def __init__(self):
        pass

    def put(self, request):
        pass


class DeleteCode(View, Controller):
    """DeleteCode Endpoint Controller"""

    def __init__(self):
        pass

    def delete(self, request):
        pass


class GetCode(View, Controller):
    """GetCode Endpoint Controller"""

    def __init__(self):
        pass

    def get(self, request):
        pass


class GetJob(View, Controller):
    """GetJob Endpoint Controller"""

    def __init__(self):
        pass

    def get(self, request):
        pass


class RunCode(View, Controller):
    """RunCode Endpoint Controller"""

    def __init__(self):
        pass

    def post(self, request):
        pass


class ExecuteCode(View, Controller):
    """ExecuteCode Endpoint Controller"""

    def __init__(self):
        pass

    def post(self, request):
        pass
