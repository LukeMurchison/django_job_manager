# Generated by Django 4.1.1 on 2022-10-21 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_job_finishing_alter_job_mark_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]