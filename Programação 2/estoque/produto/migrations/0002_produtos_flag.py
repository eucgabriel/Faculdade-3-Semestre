# Generated by Django 4.0.2 on 2022-05-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='flag',
            field=models.BooleanField(default=True),
        ),
    ]
