# Generated by Django 5.1 on 2024-11-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_alter_do_user_alter_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='do',
            name='user',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
