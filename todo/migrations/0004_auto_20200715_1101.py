# Generated by Django 3.0.8 on 2020-07-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200715_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='completed_on',
            new_name='datecompleted',
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
