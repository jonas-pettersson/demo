# Generated by Django 3.1.1 on 2020-09-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
