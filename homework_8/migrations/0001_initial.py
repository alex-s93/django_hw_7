# Generated by Django 5.0.6 on 2024-06-03 13:38

import django.db.models.deletion
import homework_8.models.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'task_manager_category',
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, unique_for_date='created_at')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'In progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], default='New', max_length=20)),
                ('deadline', models.DateTimeField(validators=[homework_8.models.validators.validate_future_date])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='homework_8.category')),
            ],
            options={
                'verbose_name': 'Task',
                'db_table': 'task_manager_task',
                'ordering': ('-created_at',),
                'unique_together': {('title',)},
            },
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'In progress'), ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')], default='New', max_length=20)),
                ('deadline', models.DateTimeField(validators=[homework_8.models.validators.validate_future_date])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='homework_8.task')),
            ],
            options={
                'verbose_name': 'SubTask',
                'db_table': 'task_manager_subtask',
                'ordering': ('-created_at',),
                'unique_together': {('title',)},
            },
        ),
    ]
