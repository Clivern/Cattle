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

from app import APP_ROOT                                    # noqa: E402
from app.shortcuts import Logger                            # noqa: E402
from app.shortcuts import get_config                        # noqa: E402


def setup_new_relic():
    """
    Setup New Relic Agent
    """
    logger = Logger().get_logger(__name__)

    logger.info("Setup newrelic agent")

    if get_config("new_relic_config_file", "") != "":
        logger.info("Application is running through newrelic admin so abort!")
        logger.info("Newrelic agent setup finished")
        return

    if "NEW_RELIC_STATUS" not in os.environ.keys():
        os.environ["NEW_RELIC_STATUS"] = "disabled"

    file = "{}/{}".format(
        APP_ROOT,
        get_config("new_relic_config_file_path", "newrelic.ini")
    )

    if os.path.isfile(file) and os.environ["NEW_RELIC_STATUS"] == "disabled":
        # Enable New Relic
        os.environ["NEW_RELIC_STATUS"] = "enabled"
        newrelic.agent.initialize(file)
        logger.info("Load newrelic config file {}".format(file))

    elif os.environ["NEW_RELIC_STATUS"] == "enabled":
        logger.info("Newrelic agent is already enabled")

    else:
        logger.warning("Newrelic will be disabled since newrelic.ini config is missing")

    logger.info("Newrelic agent setup finished")
