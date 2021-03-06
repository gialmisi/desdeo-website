# Generated by Django 2.2.6 on 2019-12-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biographies', '0006_bio_keywords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='bio',
            name='surname',
            field=models.CharField(default='Surname', help_text='Used to order the profiles shown.', max_length=100),
            preserve_default=False,
        ),
    ]
