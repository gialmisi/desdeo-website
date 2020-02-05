# Generated by Django 2.2.6 on 2019-12-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20191204_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloadable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Short description about the file.', max_length=1000)),
                ('file', models.FileField(help_text='The file to be made available', upload_to='')),
            ],
        ),
    ]