# Generated by Django 4.2.2 on 2023-06-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotton',
            name='local',
            field=models.BooleanField(default=True, verbose_name='Mahalliy'),
        ),
    ]
