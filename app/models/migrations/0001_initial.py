# Generated by Django 4.1.2 on 2022-10-20 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('quantity_members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('family_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.familygroup')),
                ('items', models.ManyToManyField(to='models.item')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('FA', 'father'), ('MO', 'mother'), ('SI', 'sister'), ('BR', 'brother'), ('CH', 'child'), ('WI', 'wife'), ('HU', 'husband')], max_length=30)),
                ('user_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.user')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField()),
                ('points', models.IntegerField()),
                ('priority_level', models.CharField(blank=True, choices=[('NO', 'noUrgent'), ('UR', 'urgent'), ('EM', 'emergency')], max_length=30)),
                ('state', models.CharField(blank=True, choices=[('WH', 'whithoutStart'), ('PE', 'pending'), ('FA', 'failed'), ('CO', 'completed')], max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('FA', 'family'), ('SI', 'single')], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.user')),
            ],
        ),
    ]
