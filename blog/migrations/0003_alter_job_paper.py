# Generated by Django 4.1.1 on 2022-10-19 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_paper_paper_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.paper'),
        ),
    ]