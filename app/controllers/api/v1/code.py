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
import uuid
from http import HTTPStatus

from django.views import View
from django.http import JsonResponse
from django.utils.translation import gettext as _

from app.shortcuts import Logger
from app.util.random import Random
from app.tasks.playground import run
from app.util.validator import Validator
from app.controllers.controller import Controller
from app.repository.task_repository import TaskRepository
from app.repository.code_repository import CodeRepository
from app.exceptions.invalid_request import InvalidRequest
from app.exceptions.resource_not_found import ResourceNotFound
from app.exceptions.internal_server_error import InternalServerError


class CreateCode(View, Controller):
    """CreateCode Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.code_repository = CodeRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Create Code

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode('utf-8'),
            self.validator.get_schema_path("/schemas/api/v1/code/create.json")
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        slug = Random.token(Random.rand_int(5, 10))
        data = json.loads(request.body.decode('utf-8'))

        while self.code_repository.get_one_by_slug(slug):
            slug = Random.token(Random.rand_int(5, 10))

        self.logger.info("New slug {} will be used for the code item".format(slug))

        code = self.code_repository.insert_one({
            "uuid": str(uuid.uuid4()),
            "slug": slug,
            "token": Random.token(Random.rand_int(20, 35)),
            "language": data["language"],
            "version": data["version"],
            "content": data["content"],
        })

        self.logger.info("New code item with uuid {} got created".format(code.id))

        return JsonResponse({
            "id": code.id,
            "uuid": code.uuid,
            "slug": code.slug,
            "token": code.token,
            "language": code.language,
            "version": code.version,
            "content": code.content,
            "createdAt": code.created_at,
            "updatedAt":  code.updated_at
        }, status=HTTPStatus.CREATED)


class CodeAction(View, Controller):
    """CodeAction Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.code_repository = CodeRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, id):
        """
        Get Request

        Args:
            request: the request
            id: the code uuid

        Returns:
            The JSON Response
        """

        # Workaround to allow fetching code item by slug for web ui
        if "-" in id:
            id_type = "uuid"
        else:
            id_type = "slug"

        self.logger.info("Attempt to get code resource with {} {}".format(id_type, id))

        if id_type == "uuid":
            code = self.code_repository.get_one_by_uuid(id)
        else:
            code = self.code_repository.get_one_by_slug(id)

        if not code:
            self.logger.info("Code with {} {} not found".format(id_type, id))
            raise ResourceNotFound("Code with {} {} not found".format(id_type, id))

        self.logger.info("Found a code item with {} {}".format(id_type, code.id))

        return JsonResponse({
            "id": code.id,
            "uuid": code.uuid,
            "slug": code.slug,
            "language": code.language,
            "version": code.version,
            "content": code.content,
            "createdAt": code.created_at,
            "updatedAt":  code.updated_at
        }, status=HTTPStatus.OK)

    def put(self, request, id):
        """
        Update Request

        Args:
            request: the request
            id: the code uuid

        Returns:
            The JSON Response
        """
        self.logger.info("Attempt to update code resource with uuid {}".format(id))
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode('utf-8'),
            self.validator.get_schema_path("/schemas/api/v1/code/update.json")
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        code = self.code_repository.get_one_by_uuid(id)

        if not code:
            self.logger.info("Code with uuid {} not found".format(id))
            raise ResourceNotFound("Code with uuid {} not found".format(id))

        data = json.loads(request.body.decode('utf-8'))

        self.logger.info("Found a code item with uuid {}".format(code.id))

        if code.token != data["token"]:
            self.logger.info("Unable to update code item with uuid {}: Token doesn't match".format(id))
            raise InvalidRequest(_("Token doesn't match"))

        result = self.code_repository.update_one_by_uuid(code.uuid, {
            "language": data["language"],
            "version": data["version"],
            "content": data["content"],
        })

        if not result:
            self.logger.error("Error while updating code item with uuid {}".format(id))
            raise InternalServerError(_("Internal Server Error."))

        self.logger.error("Code item with uuid {} got updated".format(id))

        return JsonResponse({
            "id": code.id,
            "uuid": code.uuid,
            "slug": code.slug,
            "token": code.token,
            "language": data["language"],
            "version": data["version"],
            "content": data["content"],
            "createdAt": code.created_at,
            "updatedAt":  code.updated_at
        }, status=HTTPStatus.OK)

    def delete(self, request, id):
        """
        Delete Request

        Args:
            request: the request
            id: the code uuid

        Returns:
            The JSON Response
        """
        self.logger.info("Attempt to delete code resource with uuid {}".format(id))

        result = self.code_repository.delete_one_by_uuid(id)

        if not result:
            self.logger.info("Code with uuid {} not found".format(id))
            raise ResourceNotFound("Code with uuid {} not found".format(id))

        self.logger.error("Code item with uuid {} got deleted".format(id))

        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)


class GetTask(View, Controller):
    """GetTask Endpoint Controller"""

    def __init__(self):
        self.task_repository = TaskRepository()
        self.logger = Logger().get_logger(__name__)

    def get(self, request, id):
        """
        Fetch Task Data

        Args:
            request: the request
            id: the code uuid

        Returns:
            The JSON Response
        """
        self.logger.info("Fetch task with uuid {}".format(id))

        task = self.task_repository.get_one_by_uuid(id)

        if not task:
            self.logger.info("Task with uuid {} not found".format(id))
            raise ResourceNotFound("Task with uuid {} not found".format(id))

        self.logger.info("Found a task with uuid {}".format(id))

        return JsonResponse({
            "id": id,
            "status": task.status.upper(),
            "result": json.loads(task.result),
            "createdAt": task.created_at,
            "updatedAt":  task.updated_at
        }, status=HTTPStatus.OK)


class ExecuteCode(View, Controller):
    """ExecuteCode Endpoint Controller"""

    def __init__(self):
        self.validator = Validator()
        self.task_repository = TaskRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request):
        """
        Execute Code

        Args:
            request: the request

        Returns:
            The JSON Response
        """
        self.logger.info("Validate incoming request")

        result = self.validator.validate(
            request.body.decode('utf-8'),
            self.validator.get_schema_path("/schemas/api/v1/code/execute.json")
        )

        if not result:
            self.logger.info("Request is invalid")
            raise InvalidRequest(self.validator.get_error())

        data = json.loads(request.body.decode('utf-8'))

        payload = {
            "language": data["language"],
            "version": data["version"],
            "content": data["content"]
        }

        self.logger.info("Create a new task to run the code")

        task = self.task_repository.insert_one({
            "uuid": str(uuid.uuid4()),
            "status": TaskRepository.PENDING,
            "payload": json.dumps(payload),
            "result": "{}"
        })

        self.logger.info("A new task with uuid {} got created".format(task.id))

        run.delay(task.id)

        self.logger.info("A new task with uuid {} sent to workers".format(task.id))

        return JsonResponse({
            "id": task.uuid,
            "status": task.status.upper(),
            "createdAt": task.created_at,
            "updatedAt":  task.updated_at
        }, status=HTTPStatus.ACCEPTED)


class RunCode(View, Controller):
    """RunCode Endpoint Controller"""

    def __init__(self):
        self.code_repository = CodeRepository()
        self.task_repository = TaskRepository()
        self.logger = Logger().get_logger(__name__)

    def post(self, request, id):
        """
        Run Code

        Args:
            request: the request
            id: the code uuid

        Returns:
            The JSON Response
        """
        self.logger.info("Fetch code with uuid {}".format(id))

        code = self.code_repository.get_one_by_uuid(id)

        if not code:
            self.logger.info("Code with uuid {} not found".format(id))
            raise ResourceNotFound("Code with uuid {} not found".format(id))

        self.logger.info("Create a new task to run code item with uuid {}".format(code.id))

        task = self.task_repository.insert_one({
            "uuid": str(uuid.uuid4()),
            "status": TaskRepository.PENDING,
            "payload": json.dumps({"code_id": code.id}),
            "result": "{}"
        })

        if not task:
            self.logger.error("Error while creating a new task")
            raise InternalServerError("Internal Server Error.")

        self.logger.info("A new task with uuid {} got created".format(task.uuid))

        run.delay(task.id)

        self.logger.info("A new task with uuid {} sent to workers".format(task.uuid))

        return JsonResponse({
            "id": task.uuid,
            "status": task.status.upper(),
            "createdAt": task.created_at,
            "updatedAt":  task.updated_at
        }, status=HTTPStatus.ACCEPTED)
