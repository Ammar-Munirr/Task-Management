# Generated by Django 4.2.6 on 2023-10-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateField(),
        ),
    ]