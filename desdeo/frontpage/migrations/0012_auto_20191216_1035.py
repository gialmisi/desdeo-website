# Generated by Django 2.2.6 on 2019-12-16 08:35

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0011_auto_20191204_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimages',
            name='order',
            field=models.IntegerField(default=1, help_text='Order of the displayed image in the carousel in ascending order. Smaller is first.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carouselimages',
            name='description',
            field=models.TextField(blank=True, help_text='Caption text to be shown on the image.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='carouselimages',
            name='image',
            field=stdimage.models.StdImageField(help_text='Image should be 800x400 pixels, or bigger.', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='featurette',
            name='link',
            field=models.CharField(help_text='The link the button on the featurettes redirects to.', max_length=100),
        ),
        migrations.AlterField(
            model_name='featurette',
            name='order',
            field=models.IntegerField(help_text='Order of the displayed featurette in ascending order. Smaller is first.'),
        ),
        migrations.AlterField(
            model_name='featurette',
            name='text_content',
            field=models.TextField(help_text='The text to be shown next to the featurette.', max_length=1000),
        ),
    ]
