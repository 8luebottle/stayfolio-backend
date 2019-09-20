# Generated by Django 2.2.4 on 2019-09-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0019_auto_20190921_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazines',
            name='place',
        ),
        migrations.AddField(
            model_name='magazines',
            name='details',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='magazines',
            name='identifier_kr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]