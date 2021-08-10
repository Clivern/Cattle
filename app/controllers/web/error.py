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

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import gettext as _

from app.shortcuts import get_config
from app.shortcuts import Logger


def handler404(request, exception=None, template_name="templates/index.html"):
    """404 Error Page"""

    logger = Logger().get_logger(__name__)

    if exception is not None:
        # Log exceptions only on debug mode
        logger.debug("Route Not Found: {exception}".format(
            exception=exception
        ))

    context = {
        "title": _("404 | {}").format(get_config("app_name", "Bulldog")),
        "description": get_config("app_description", ""),
        "base_url": get_config("app_url", ""),
    }

    return render(request, template_name, context, status=404)


def handler500(request, exception=None, template_name="templates/index.html"):
    """500 Error Page"""

    logger = Logger().get_logger(__name__)

    if exception is not None:
        logger.error("Internal Server Error: {exception}".format(
            exception=exception
        ))

    context = {
        "title": _("500 | {}").format(get_config("app_name", "Bulldog")),
        "description": get_config("app_description", ""),
        "base_url": get_config("app_url", ""),
    }

    return render(request, template_name, context, status=500)


def csrf_failure(request, reason=""):
    return JsonResponse({
        "error": _("Error! Access forbidden due to invalid CSRF token.")
    })
