# Generated by Django 3.0.8 on 2020-07-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
