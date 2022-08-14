# Generated by Django 4.0.3 on 2022-07-12 02:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_hot_deal_product_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
