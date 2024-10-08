# Generated by Django 5.0.6 on 2024-09-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
