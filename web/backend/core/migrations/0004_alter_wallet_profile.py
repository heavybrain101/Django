# Generated by Django 5.0b1 on 2023-11-20 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_wallet_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
