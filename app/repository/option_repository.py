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

from app.models import Option


class OptionRepository():
    """Option Repository"""

    def insert_one(self, option):
        """Insert a New Option"""
        if self.get_one_by_key(option["key"]) is not False:
            return True

        option = Option(
            key=option["key"],
            value=option["value"],
            autoload=option["autoload"] if "autoload" in option else False
        )

        option.save()
        return False if option.pk is None else option

    def insert_many(self, options):
        """Insert Many Options"""
        status = True
        for option in options:
            status &= True if self.insert_one(option) is not False else False
        return status

    def get_one_by_id(self, id):
        """Get Option By ID"""
        try:
            option = Option.objects.get(pk=id)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_one_by_key(self, key):
        """Get Option By Key"""
        try:
            option = Option.objects.get(key=key)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_value_by_key(self, key, default=""):
        """Get Option Value By Key"""
        try:
            option = Option.objects.get(key=key)
            return default if option.pk is None else option.value
        except Exception:
            return default

    def get_many_by_autoload(self, autoload):
        """Get Many Options By Autoload"""
        options = Option.objects.filter(autoload=autoload)
        return options

    def get_many_by_keys(self, keys):
        """Get Many Options By Keys"""
        options = Option.objects.filter(key__in=keys)
        return options

    def update_value_by_id(self, id, value):
        """Update Option Value By ID"""
        option = self.get_one_by_id(id)
        if option is not False:
            option.value = value
            option.save()
            return True
        return False

    def update_value_by_key(self, key, value):
        """Update Option Value By Key"""
        option = self.get_one_by_key(key)
        if option is not False:
            option.value = value
            option.save()
            return True
        else:
            return self.insert_one({
                "key": key,
                "value": value
            }) is not False

        return False

    def count(self):
        return Option.objects.count()

    def delete_one_by_id(self, id):
        """Delete Option By ID"""
        option = self.get_one_by_id(id)
        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False
        return False

    def delete_one_by_key(self, key):
        """Delete Option By Key"""
        option = self.get_one_by_key(key)
        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False
        return False

    def truncate(self):
        return Option.objects.all().delete()
