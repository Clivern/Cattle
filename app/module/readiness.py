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

from django.db import connection
from django.db.utils import OperationalError
from django.utils import timezone

from app.shortcuts import Logger
from app.repository.task_repository import TaskRepository


class Readiness():
    """Readiness Class"""

    def __init__(self):
        self.task_repository = TaskRepository()
        self.logger = Logger().get_logger(__name__)

    def check_db_connection(self):
        """
        Check Database Connection

        Returns:
            Whether the DB connection is working or not
        """
        self.logger.info("Connect to database")

        try:
            connection.ensure_connection()
        except OperationalError as e:
            self.logger.error("Unable to connect to database: {}".format(str(e)))
            return False

        self.logger.info("Database connection established successfully")

        return True

    def check_workers(self, delay_benchmark_in_seconds=30):
        """
        Check the delay and make sure the delay is accepted

        Returns:
            Whether workers are fast or slow
        """
        self.logger.info("Check async workers health")

        # Check the latest task
        self.logger.info("Get latest task")

        latest_task = self.task_repository.get_latest_task()

        if latest_task is None:
            # No Tasks Yet
            self.logger.info("There is no tasks right now so skip the check")
            return True

        self.logger.info("Found a task with id {} and created_at {}".format(latest_task.id, latest_task.created_at))

        delta = timezone.now() - latest_task.created_at

        if delta.seconds > delay_benchmark_in_seconds and TaskRepository.SUCCEEDED != latest_task.status:
            # Workers are slow
            self.logger.info("Task with id {} and status {} reached {} seconds".format(
                latest_task.id,
                latest_task.status,
                delta.seconds
            ))

            return False

        # Workers are pretty fast
        self.logger.info("Task with id {} and status {} finished in {} seconds".format(
            latest_task.id,
            latest_task.status,
            delta.seconds
        ))

        return True
