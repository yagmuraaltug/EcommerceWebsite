# Generated by Django 2.1.15 on 2022-03-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
