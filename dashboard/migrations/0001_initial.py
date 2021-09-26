# Generated by Django 3.2.6 on 2021-09-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30, verbose_name='Nome do projeto')),
                ('project_description', models.TextField()),
                ('project_link', models.CharField(max_length=200)),
                ('project_image', models.ImageField(upload_to='projects/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
