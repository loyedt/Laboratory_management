# Generated by Django 3.1.7 on 2021-07-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlab', '0010_urinalysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urinalysis',
            name='ph',
            field=models.FloatField(),
        ),
    ]
