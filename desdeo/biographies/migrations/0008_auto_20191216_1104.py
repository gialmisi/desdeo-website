# Generated by Django 2.2.6 on 2019-12-16 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biographies', '0007_auto_20191216_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='othercontributor',
            old_name='name',
            new_name='first_name',
        ),
    ]
