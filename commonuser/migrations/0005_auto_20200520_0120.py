# Generated by Django 2.2.2 on 2020-05-19 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commonuser', '0004_auto_20200519_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonusermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='commonusermodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='commonusers', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
