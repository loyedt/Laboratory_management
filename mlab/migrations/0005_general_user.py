# Generated by Django 3.1.7 on 2021-06-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlab', '0004_auto_20210617_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='general_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tstno', models.IntegerField()),
                ('phno', models.IntegerField()),
                ('tstrst', models.FileField(upload_to='generalresult')),
            ],
        ),
    ]