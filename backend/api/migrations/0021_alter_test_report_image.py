# Generated by Django 4.1.7 on 2023-03-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_room_emergency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='report_image',
            field=models.ImageField(blank=True, default='images/default.webp', null=True, upload_to='images/'),
        ),
    ]
