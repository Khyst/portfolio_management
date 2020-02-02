# Generated by Django 2.2.1 on 2020-01-30 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0003_auto_20200130_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='refpost',
            name='o_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='refpost',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject'),
        ),
    ]
