# Generated by Django 4.2.2 on 2023-06-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorpage', '0002_authorpage_name'),
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriespage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='series', to='authorpage.authorpage'),
        ),
    ]
