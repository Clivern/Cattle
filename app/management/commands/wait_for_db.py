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

import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command that waits for database to be available"""

    help = "Wait untill the database is up and running"

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')

        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
