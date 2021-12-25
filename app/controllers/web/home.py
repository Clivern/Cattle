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
from django.shortcuts import render

from app.shortcuts import get_config
from app.controllers.controller import Controller


class Home(View, Controller):
    """Home Page Controller"""

    template_name = 'templates/index.html'

    def get(self, request):
        return render(request, self.template_name, {
            "title": get_config("app_name", "Bulldog"),
            "description": get_config("app_description", ""),
            "base_url": get_config("app_url", ""),
        })
