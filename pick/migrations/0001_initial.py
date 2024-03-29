# Generated by Django 2.2.4 on 2019-09-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('pick_id', models.AutoField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('main_image_url', models.URLField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('place_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
            ],
            options={
                'db_table': 'picks',
            },
        ),
        migrations.CreateModel(
            name='PickImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.URLField(max_length=2500)),
                ('pick_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pick.Pick')),
            ],
            options={
                'db_table': 'pick_images',
            },
        ),
    ]
