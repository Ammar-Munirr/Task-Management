# Generated by Django 4.2.6 on 2023-10-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_tasks_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('IN-PROGRESS', 'IN-PROGRESS'), ('DONE', 'DONE')], default=1, max_length=13),
            preserve_default=False,
        ),
    ]
