# Generated by Django 4.2.2 on 2023-06-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpage',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
