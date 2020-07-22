from __future__ import unicode_literals

from django.db import migrations, models, transaction
import csv
from datetime import datetime
from datetime import date

def load_initial_data(apps, schema_editor):
    # get the correct versions of models using the app registry
    ffacility = apps.get_model("facilities", "Facility")
    faddress = apps.get_model("facilities", "Address")
    fdescription = apps.get_model("facilities","Description")

    # This is where your migration logic will go.
    # For my use case i needed to get unique id and
    # transform data from the csv file into the schema i wanted
    with open('data/Health_Facility_General_Information.csv') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        for row in reader:
            address,acreated = faddress.objects.get_or_create(facility_address_one= row[5],
                             facility_address_two=row[6],
                             facility_city=row[7],
                             facility_state=row[8],
                             facility_zip_code=row[9],
                             facility_latitude=row[33],
                             facility_longitude=row[34],
                             facility_location = row[35],
                             facility_country_code=row[13],
                             facility_country = row[14])



            description,dcreated = fdescription.objects.get_or_create(short_description=row[2],description=row[3])
            if acreated and dcreated:
                facility = ffacility.objects.get_or_create(id= int(row[0]),facility_id=int(row[0]), facility_name=row[1],facility_phone_number=row[10],
                facility_open= datetime.strptime(row[4],"%m/%d/%Y").date(),facility_fax_number=row[11], address_id=address.id,description_id =description.id)

def reverse_func(apps, schema_editor):
    ffacility = apps.get_model("facilities", "Facility")
    faddress = apps.get_model("facilities", "Address")
    fdescription = apps.get_model("facilities","Description")

    fdescription.objects.all().delete()
    faddress.objects.all().delete()
    ffacility.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data,reverse_func),
    ]
