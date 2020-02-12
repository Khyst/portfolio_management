# Generated by Django 2.2.1 on 2020-02-04 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procedure', '0013_auto_20200202_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(default=0)),
                ('post_title', models.CharField(default='', max_length=200)),
                ('reference', models.TextField()),
                ('description', models.TextField()),
                ('intro_image', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.Subject')),
            ],
        ),
        migrations.DeleteModel(
            name='refPost',
        ),
    ]
