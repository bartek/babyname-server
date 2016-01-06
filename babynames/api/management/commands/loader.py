import csv

from django.core.management.base import BaseCommand

from ...models import Name


class Command(BaseCommand):
    help = 'Load open data into name database'

    def handle(self, *args, **options):
        # From the perspective of the path for manage.py
        f = open('../data/united-states-1000-1880.csv', 'r')

        reader = csv.reader(f)

        next(reader, None)  # Skip first row.

        for row in reader:
            year, name, popularity, gender = row

            # Check if name exists.
            names = Name.objects.filter(name=name)

            # Insert a new name.
            if names.count() == 0:
                Name.objects.create(
                    name=name,
                    gender=gender,
                )
                continue

            # FIXME: We have a name already. Eventually populate popularity in this scenario.
            pass

        f.close()
