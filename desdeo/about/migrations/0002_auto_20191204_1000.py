# Generated by Django 2.2.6 on 2019-12-04 08:00

import about.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contents',
            new_name='Content',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(storage=about.models.OverwriteStorage(), upload_to='images/about')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about.Content')),
            ],
        ),
    ]
