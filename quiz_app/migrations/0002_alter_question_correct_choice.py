# Generated by Django 5.0 on 2023-12-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_choice',
            field=models.CharField(max_length=255),
        ),
    ]
