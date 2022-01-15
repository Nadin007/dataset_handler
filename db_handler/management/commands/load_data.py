import csv
import os

from django.core.management.base import BaseCommand, CommandError

from db_handler.models import ShopsDB


class Command(BaseCommand):
    help = ('Import csv into `Model` database. When you invoce'
            'function you should pass the path to the csv file')

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **options):
        if options.get('csv_path') is None:
            raise CommandError("Invalid Invocation. See help.")

        csvpath = options.get('csv_path')
        if not os.path.exists(csvpath):
            raise CommandError(f"{csvpath} doesnt exist.")

        model_fields = [f.name for f in ShopsDB._meta.fields]
        fields_name = []

        with open(csvpath, 'r') as csvFile:
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
                    try:
                        ShopsDB.objects.get(**dict_data)
                    except ShopsDB.DoesNotExist:
                        ShopsDB.objects.create(**dict_data)
                except Exception as e:
                    raise CommandError(e)
