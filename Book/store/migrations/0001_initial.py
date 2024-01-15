# Generated by Django 4.2.6 on 2024-01-15 14:54

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Science',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', tinymce.models.HTMLField()),
                ('Author', models.CharField(max_length=100)),
            ],
        ),
    ]
