# Generated by Django 4.1.7 on 2023-03-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
