# Generated by Django 3.2.9 on 2021-11-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_article_last_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, help_text='An image to be displayed at the end of the news article.', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.URLField(blank=True, help_text='An URL of a video to be embedded.'),
        ),
        migrations.AlterField(
            model_name='article',
            name='contents',
            field=models.TextField(help_text='The textual content of the news article.'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(help_text='The publication date.'),
        ),
    ]
