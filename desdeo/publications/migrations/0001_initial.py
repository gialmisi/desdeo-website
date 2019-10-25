# Generated by Django 2.2.6 on 2019-10-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BibEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('journal_title', models.CharField(max_length=200)),
                ('issue', models.CharField(max_length=100)),
                ('pages', models.CharField(max_length=100)),
                ('doi_url', models.URLField()),
            ],
        ),
    ]