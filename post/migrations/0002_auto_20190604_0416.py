# Generated by Django 2.2.2 on 2019-06-04 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='catergory',
            new_name='category',
        ),
    ]