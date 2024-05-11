# Generated by Django 4.2.11 on 2024-03-27 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now=True)),
                ('data_updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_created', models.DateTimeField(auto_now=True)),
                ('data_updated', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes_app.folder')),
            ],
        ),
    ]
