# Generated by Django 3.2.5 on 2021-07-23 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_shippingaddress_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
    ]