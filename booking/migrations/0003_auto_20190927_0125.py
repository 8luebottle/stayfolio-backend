# Generated by Django 2.2.4 on 2019-09-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190926_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment',
        ),
        migrations.AddField(
            model_name='booking',
            name='bill_total',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=9),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]