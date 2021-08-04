import os
import csv

from db_handler.models import ShopsDB
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = ('Import csv into `Model` database. When you invoce'
            'function you should pass the path to the csv file')

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        if options.get('csv_path') is None:
            raise CommandError("Invalid Invocation. See help.")

        csvPath = options.get('csv_path')
        if not os.path.exists(csvPath):
            raise CommandError(f"{csvPath} doesnt exist.")

        model_fields = [f.name for f in ShopsDB._meta.fields]
        fields_name = []

        with open(csvPath, 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar="\"")
            fields_name = next(reader)
            for i, _ in enumerate(fields_name):
                fields_name[i] = fields_name[i].lower().replace(' ', '_')
                if not fields_name[i] in model_fields:
                    raise CommandError(
                        f'{fields_name[i]} field does not exists in {ShopsDB}.'
                        )

            for row in reader:
                try:
                    dict_data = {}
                    for i, field in enumerate(row):
                        dict_data[fields_name[i]] = field

                    _, created = ShopsDB.objects.get_or_create(**dict_data)
                    print(created)
                except Exception as e:
                    raise CommandError(e)
