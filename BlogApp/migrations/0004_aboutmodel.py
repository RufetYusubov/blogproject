# Generated by Django 4.2.2 on 2023-07-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=150)),
                ('streetadres', models.CharField(max_length=150)),
            ],
        ),
    ]
