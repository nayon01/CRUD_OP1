# Generated by Django 4.1.5 on 2023-01-14 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userprofile_email_alter_userprofile_mobile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='img',
            new_name='photo',
        ),
    ]