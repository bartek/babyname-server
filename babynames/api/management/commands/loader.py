import csv

from django.core.management.base import BaseCommand, CommandError

from ...models import Name


class Command(BaseCommand):
    help = 'Load open data into name database'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str)

    def handle(self, *args, **options):
        file_path = options['file'][0]

        try:
            csvfile = open(file_path, 'r')
        except IOError:
            raise CommandError("Unable to open file, {}".format(file_path))

        reader = csv.reader(csvfile)

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
                    popularity=[popularity],
                )

            # Update existing names popularity.
            name = names[0]
            name.popularity.append(popularity)
            name.save()

        csvfile.close()
