# Generated by Django 4.2.2 on 2023-06-16 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='page_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='home_homepage_ptr', serialize=False, to='wagtailcore.page'),
        ),
    ]
