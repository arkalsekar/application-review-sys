# Generated by Django 3.1.1 on 2021-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_application_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='application_id',
            field=models.UUIDField(null=True),
        ),
    ]
