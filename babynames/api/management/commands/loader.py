import csv

from django.core.management.base import BaseCommand, CommandError

from ...models import Name

class Command(BaseCommand):
    help = 'Load open data into name database'

    def handle(self, *args, **options):
        # From the perspective of the path for manage.py
        f = open('../data/united-states-1000-1880.csv', 'r')

        reader = csv.reader(f)

        next(reader, None) # Skip first row.

        for row in reader:
            year, name, popularity, gender = row

            # Check if name exists.
            name = Name.objects.filter(name=name)

            # Insert a new name.
            if not name:
                Name.objects.create(
                    name=name,
                    gender=gender,
                )
                continue

            # We have a name already. Eventually populate popularity in this
            # scenario.
            continue

        f.close()
