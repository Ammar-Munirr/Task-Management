# Generated by Django 4.2.6 on 2023-10-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('TO-DO', 'TO-DO'), ('IN-PROGRESS', 'IN-PROGRESS'), ('DONE', 'DONE')], default='TO-DO', max_length=13),
        ),
    ]
