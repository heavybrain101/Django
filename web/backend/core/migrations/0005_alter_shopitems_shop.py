# Generated by Django 5.0b1 on 2023-11-20 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_wallet_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitems',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.shopcategory'),
        ),
    ]
