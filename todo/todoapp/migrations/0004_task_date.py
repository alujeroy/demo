# Generated by Django 4.1.5 on 2023-02-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_prior_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1234-12-01'),
            preserve_default=False,
        ),
    ]
