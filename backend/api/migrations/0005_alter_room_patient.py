# Generated by Django 4.1.7 on 2023-03-02 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_room_available_room_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='patient',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient'),
        ),
    ]
