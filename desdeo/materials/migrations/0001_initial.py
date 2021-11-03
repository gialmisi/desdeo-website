# Generated by Django 3.2.9 on 2021-11-03 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Short description about the file.', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='File to be made available', upload_to='')),
                ('material_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='materials.materialentry')),
            ],
        ),
    ]
