# Generated by Django 4.2.2 on 2023-07-12 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_remove_commentmodel_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='BlogApp.commentmodel'),
        ),
    ]
