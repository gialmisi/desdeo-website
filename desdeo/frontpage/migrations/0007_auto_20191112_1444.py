# Generated by Django 2.2.6 on 2019-11-12 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0006_auto_20191112_0922'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublicationsDescription',
            new_name='Featurette',
        ),
        migrations.DeleteModel(
            name='AboutDescription',
        ),
        migrations.DeleteModel(
            name='TeamDescription',
        ),
    ]
