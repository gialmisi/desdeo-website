# Generated by Django 3.2.9 on 2021-11-03 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
    ]