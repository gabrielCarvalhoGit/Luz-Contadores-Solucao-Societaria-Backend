# Generated by Django 5.1.1 on 2024-09-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_custom_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
