# Generated by Django 3.1.7 on 2021-06-17 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mlab', '0003_user_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_result',
            name='username',
        ),
        migrations.AddField(
            model_name='user_result',
            name='userid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_result',
            name='testid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mlab.tests'),
        ),
    ]
