# Generated by Django 4.1.2 on 2022-11-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userauthmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='userauthmodel',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userauthmodel',
            name='user_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
