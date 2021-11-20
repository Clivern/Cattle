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

import os
import newrelic.agent

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
os.environ.setdefault('NEW_RELIC_STATUS', 'disabled')

application = get_wsgi_application()

from app import APP_ROOT                                    # noqa: E402
from app.shortcuts import get_config                        # noqa: E402
from app.shortcuts import Logger                            # noqa: E402

if get_config("new_relic_config_file", "") == "":
    file = "{}/{}".format(
        APP_ROOT,
        get_config("new_relic_config_file_path", "newrelic.ini")
    )

    logger = Logger().get_logger(__name__)

    if os.path.isfile(file):
        # Enable New Relic
        os.environ["NEW_RELIC_STATUS"] = "enabled"
        logger.info("Load newrelic config file {}".format(file))
        newrelic.agent.initialize(file)
    else:
        logger.warning("Newrelic will be disabled since newrelic.ini config is missing")
