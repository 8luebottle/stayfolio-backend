# Generated by Django 2.2.4 on 2019-09-21 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20190920_1551'),
        ('magazines', '0013_remove_magazines_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazines',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='place.Place'),
        ),
    ]
