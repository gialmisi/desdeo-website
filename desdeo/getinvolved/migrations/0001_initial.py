# Generated by Django 2.2.6 on 2019-11-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(help_text='The main contents of the Get involved page. Markdown is supported.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
