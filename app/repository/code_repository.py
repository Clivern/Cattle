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

from app.models import Code


class CodeRepository():
    """Code Repository"""

    def insert_one(self, code):
        """
        Insert a New Code

        Args:
            code: a dict of code data

        Returns:
            An instance of the created code
        """
        code = Code(
            uuid=code["uuid"],
            slug=code["slug"],
            token=code["token"],
            language=code["language"],
            version=code["version"],
            content=code["content"]
        )

        code.save()
        return False if code.pk is None else code

    def get_one_by_id(self, id):
        """
        Get Code By ID

        Args:
            id: the code id

        Returns:
            An instance of the code or False if it doesn't exist
        """
        try:
            code = Code.objects.get(pk=id)
            return False if code.pk is None else code
        except Exception:
            return False

    def get_one_by_uuid(self, uuid):
        """
        Get Code By UUID

        Args:
            uuid: the code uuid

        Returns:
            An instance of the code or False if it doesn't exist
        """
        try:
            code = Code.objects.get(uuid=uuid)
            return False if code.pk is None else code
        except Exception:
            return False

    def get_one_by_slug(self, slug):
        """
        Get Code By Slug

        Args:
            slug: the code slug

        Returns:
            An instance of the code or False if it doesn't exist
        """
        try:
            code = Code.objects.get(slug=slug)
            return False if code.pk is None else code
        except Exception:
            return False

    def update_one_by_uuid(self, uuid, new_data):
        """
        Update Code by UUID

        Args:
            uuid: the code uuid.
            new_data: a dict of code new data.

        Returns:
            A boolean representing the success of the operation
        """
        code = self.get_one_by_uuid(uuid)

        if code is not False:
            if "slug" in new_data:
                code.slug = new_data["slug"]
            if "token" in new_data:
                code.token = new_data["token"]
            if "language" in new_data:
                code.language = new_data["language"]
            if "version" in new_data:
                code.version = new_data["version"]
            if "content" in new_data:
                code.content = new_data["content"]

            code.save()
            return True

        return False

    def delete_one_by_id(self, id):
        """
        Delete Code By ID

        Args:
            id: the code id

        Returns:
            Whether the operation succeeded or not
        """
        code = self.get_one_by_id(id)

        if code is not False:
            count, deleted = code.delete()
            return True if count > 0 else False

        return False

    def delete_one_by_uuid(self, uuid):
        """
        Delete Code By UUID

        Args:
            uuid: the code uuid

        Returns:
            Whether the operation succeeded or not
        """
        code = self.get_one_by_uuid(uuid)

        if code is not False:
            count, deleted = code.delete()
            return True if count > 0 else False

        return False

    def delete_one_by_slug(self, slug):
        """
        Delete Code By Slug

        Args:
            slug: the code slug

        Returns:
            Whether the operation succeeded or not
        """
        code = self.get_one_by_slug(slug)

        if code is not False:
            count, deleted = code.delete()
            return True if count > 0 else False

        return False
