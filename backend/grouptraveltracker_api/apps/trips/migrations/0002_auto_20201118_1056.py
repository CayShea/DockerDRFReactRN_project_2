# Generated by Django 3.1 on 2020-11-18 18:56

import apps.trips.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.CharField(db_index=True, default=shortuuid.main.ShortUUID.uuid, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='owner',
            field=models.ForeignKey(default=apps.trips.models.get_user_id, on_delete=django.db.models.deletion.CASCADE, related_name='user_trips', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tripmember',
            name='id',
            field=models.CharField(db_index=True, default=shortuuid.main.ShortUUID.uuid, max_length=255, primary_key=True, serialize=False),
        ),
    ]
