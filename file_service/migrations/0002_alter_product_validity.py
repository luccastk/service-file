# Generated by Django 5.1.7 on 2025-03-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='validity',
            field=models.DateField(null=True),
        ),
    ]
