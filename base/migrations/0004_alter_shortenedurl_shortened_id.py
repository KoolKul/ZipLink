# Generated by Django 5.1.3 on 2024-12-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='shortened_id',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
