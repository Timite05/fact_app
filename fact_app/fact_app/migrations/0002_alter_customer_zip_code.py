# Generated by Django 4.2.16 on 2024-11-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fact_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
