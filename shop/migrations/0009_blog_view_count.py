# Generated by Django 4.0.3 on 2022-07-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_blog_thumbnail_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
