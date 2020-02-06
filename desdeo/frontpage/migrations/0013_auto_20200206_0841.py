# Generated by Django 2.2 on 2020-02-06 06:41

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0012_auto_20191216_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimages',
            name='image',
            field=stdimage.models.StdImageField(help_text='Image should be 1200x600 pixels, or bigger.', upload_to='images/'),
        ),
    ]
