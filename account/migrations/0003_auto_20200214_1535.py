# Generated by Django 2.2.1 on 2020-02-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200214_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='county',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='시/군/구'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='statue',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='도/특별/광역시'),
        ),
    ]
