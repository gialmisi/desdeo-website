# Generated by Django 2.2.6 on 2019-11-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_auto_20191025_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.TextField(help_text='List of authors', max_length=200)),
                ('title', models.TextField(help_text='Title of the publication', max_length=200)),
                ('year', models.IntegerField(default=2000, help_text='Publication year. Used for sorting.')),
                ('info', models.TextField(help_text='Example: journal name, issue, pages, publication year')),
                ('doi_url', models.CharField(help_text="Link to publisher's webpage.", max_length=100)),
                ('open_access_url', models.CharField(help_text='Link to open access source.', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BibEntry',
        ),
    ]
