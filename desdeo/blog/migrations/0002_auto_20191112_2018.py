# Generated by Django 2.2.6 on 2019-11-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcontent',
            name='contents',
            field=models.TextField(),
        ),
    ]
