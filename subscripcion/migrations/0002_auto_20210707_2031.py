# Generated by Django 3.2.5 on 2021-07-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscripcion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscripcion_cuenta',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='subscripcion_cuenta',
            name='invite_reason',
        ),
        migrations.AddField(
            model_name='subscripcion_cuenta',
            name='fecha_fin',
            field=models.DateField(null=True),
        ),
    ]
