# Generated by Django 2.1.5 on 2019-02-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('processing', 'processing'), ('finished', 'finished'), ('cancel', 'cancel')], default='new', max_length=255),
        ),
    ]
