# Generated by Django 4.1.2 on 2022-10-13 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_worker_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='current_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='project.task'),
        ),
        migrations.AddField(
            model_name='worker',
            name='current_todo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='project.todo'),
        ),
    ]
