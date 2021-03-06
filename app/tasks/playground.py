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

import json
import time

import newrelic.agent
from django_rq import job

from app.shortcuts import Logger
from app.runner.snippet import Snippet
from app.shortcuts import record_metric
from app.repository.task_repository import TaskRepository
from app.repository.code_repository import CodeRepository


@job
@newrelic.agent.background_task()
def run(task_id):
    """
    Run Code in Background

    Args:
        task_id: The Async Task ID
    """
    start_time = time.time()
    logger = Logger().get_logger(__name__)

    logger.info("Run task with id {} in background".format(task_id))

    task_repository = TaskRepository()
    code_repository = CodeRepository()

    task = task_repository.get_one_by_id(task_id)

    if not task:
        logger.info("task with id {} not found".format(task_id))
        return None

    logger.info("Task has this uuid {}".format(task.uuid))

    data = json.loads(task.payload)

    if 'code_id' in data.keys():
        code = code_repository.get_one_by_id(data['code_id'])

        if not code:
            logger.info("Code with id {} not found".format(data['code_id']))
            return None

        snippet = Snippet(task.uuid, code.content, code.language, code.version)
    else:
        snippet = Snippet(task.uuid, data['content'], data['language'], data['version'])

    status = TaskRepository.SUCCEEDED

    try:
        result = snippet.run()
        logger.info("Task with uuid {} succeeded".format(task.uuid))
    except Exception as e:
        result = {
            "output": "Failed to run the code",
            "build_time": None,
            "execution_time": None,
        }
        status = TaskRepository.FAILED
        logger.error("Task with uuid {} failed: {}".format(task.uuid, str(e)))

    duration = (time.time() - start_time) * 1000

    # Send Metrics to NR
    record_metric("Task/Playground/TotalCount", 1)
    record_metric("Task/Playground/{}".format("SuccessCount" if status == TaskRepository.SUCCEEDED else "FailCount"), 1)
    record_metric("Task/Playground/DurationMillisec", duration)

    logger.info("Task with uuid {} spent {} millisec".format(task.uuid, duration))

    task_repository.update_one_by_id(task.id, {
        "result": json.dumps(result) if result is not None else "{}",
        "status": status
    })
