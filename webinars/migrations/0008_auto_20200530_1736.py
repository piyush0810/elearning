# Generated by Django 2.2 on 2020-05-30 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0007_auto_20200530_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webinar',
            old_name='image',
            new_name='image_webinar',
        ),
        migrations.RenameField(
            model_name='webinar',
            old_name='link',
            new_name='link_webinar',
        ),
        migrations.RenameField(
            model_name='webinar',
            old_name='text',
            new_name='text_webinar',
        ),
    ]
