# Generated by Django 4.1.4 on 2022-12-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photos',
            field=models.FileField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
