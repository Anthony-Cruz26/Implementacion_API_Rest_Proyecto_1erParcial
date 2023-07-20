# Generated by Django 4.2.2 on 2023-07-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_cliente_producto_factura_cliente_factura_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suministrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.IntegerField(null=True)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('sucursal', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='suministrador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura.suministrador'),
        ),
    ]
