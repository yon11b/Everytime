# Generated by Django 3.2.7 on 2021-11-05 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_regist_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='member',
        ),
    ]
