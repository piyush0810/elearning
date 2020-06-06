# Generated by Django 2.2 on 2020-05-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='cost',
            field=models.IntegerField(default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='webinar',
            name='image',
            field=models.CharField(blank=True, default='course-1.jpg', max_length=20, null=True),
        ),
    ]