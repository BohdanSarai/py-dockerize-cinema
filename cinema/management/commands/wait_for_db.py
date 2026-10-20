import time

from django.core.management.base import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Maximum time to wait for database in seconds",
        )

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connection.ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
