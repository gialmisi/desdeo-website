# Generated by Django 2.2.6 on 2019-10-25 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('contents', models.FileField(upload_to='blogposts/')),
            ],
        ),
    ]
