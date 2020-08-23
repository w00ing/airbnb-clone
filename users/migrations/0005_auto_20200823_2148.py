# Generated by Django 2.2.5 on 2020-08-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_email_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmed',
            new_name='email_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
    ]
