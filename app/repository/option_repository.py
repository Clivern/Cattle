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
        """
        Insert a New Option

        Args:
            option: a dict of option data

        Returns:
            An instance of the created option
        """
        option = Option(
            key=option["key"],
            value=option["value"],
            autoload=option["autoload"] if "autoload" in option else False
        )

        option.save()
        return False if option.pk is None else option

    def insert_many(self, options):
        """
        Insert Many Options

        Args:
            options: array of options

        Returns:
            Whether the operation succeeded or not
        """
        status = True

        for option in options:
            status &= True if self.insert_one(option) is not False else False

        return status

    def get_one_by_id(self, id):
        """
        Get Option By ID

        Args:
            id: the option id

        Returns:
            An instance of the option or False if it doesn't exist
        """
        try:
            option = Option.objects.get(pk=id)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_one_by_key(self, key):
        """
        Get Option By Key

        Args:
            key: the option key

        Returns:
            An instance of the option or False if it doesn't exist
        """
        try:
            option = Option.objects.get(key=key)
            return False if option.pk is None else option
        except Exception:
            return False

    def get_value_by_key(self, key, default=""):
        """
        Get Option Value By Key

        Args:
            key: the option key
            default: a default value

        Returns:
            Option value or the default one
        """
        try:
            option = Option.objects.get(key=key)
            return default if option.pk is None else option.value
        except Exception:
            return default

    def get_many_by_autoload(self, autoload):
        """
        Get Many Options By Autoload

        Args:
            autoload: the autoload value

        Returns:
            array of options
        """
        options = Option.objects.filter(autoload=autoload)
        return options

    def get_many_by_keys(self, keys):
        """
        Get Many Options By Keys

        Args:
            keys: array of keys

        Returns:
            array of options
        """
        options = Option.objects.filter(key__in=keys)
        return options

    def update_value_by_id(self, id, value):
        """
        Update Option Value By ID

        Args:
            id: the option id
            value: the option value

        Returns:
            Whether the operation succeeded or not
        """
        option = self.get_one_by_id(id)

        if option is not False:
            option.value = value
            option.save()
            return True

        return False

    def update_value_by_key(self, key, value):
        """
        Update Option Value By Key

        Args:
            key: the option key
            value: the new value

        Returns:
            Whether the operation succeeded or not
        """
        option = self.get_one_by_key(key)

        if option is not False:
            option.value = value
            option.save()
            return True

        return False

    def count(self):
        """
        Count all options

        Returns:
            options count
        """
        return Option.objects.count()

    def delete_one_by_id(self, id):
        """
        Delete Option By ID

        Args:
            id: the option id

        Returns:
            Whether the operation succeeded or not
        """
        option = self.get_one_by_id(id)

        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False

        return False

    def delete_one_by_key(self, key):
        """
        Delete Option By Key

        Args:
            key: the option key

        Returns:
            Whether the operation succeeded or not
        """
        option = self.get_one_by_key(key)

        if option is not False:
            count, deleted = option.delete()
            return True if count > 0 else False

        return False

    def truncate(self):
        """
        Truncate all options

        Returns:
            deleted options count
        """
        return Option.objects.all().delete()
