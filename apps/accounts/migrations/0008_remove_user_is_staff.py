# Generated by Django 5.1.1 on 2024-10-29 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_groups_remove_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
