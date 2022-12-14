# Generated by Django 4.1.3 on 2022-11-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ordencompra", "0004_alter_ordencompra_cuit_cliente_and_more"),
        ("cliente", "0003_alter_cliente_telefono"),
        ("empresa", "0003_alter_empresa_direccion_alter_empresa_email_and_more"),
        ("facturacion", "0003_rename_numerofac_facturacion_numero_factura_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facturacion",
            name="cuit_cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cliente.cliente",
                verbose_name="CUIT Cliente",
            ),
        ),
        migrations.AlterField(
            model_name="facturacion",
            name="cuit_empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="empresa.empresa",
                verbose_name="CUIT Empresa",
            ),
        ),
        migrations.AlterField(
            model_name="facturacion",
            name="numero_factura",
            field=models.CharField(max_length=30, verbose_name="Nº de Factura"),
        ),
        migrations.AlterField(
            model_name="facturacion",
            name="numero_oc",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ordencompra.ordencompra",
                verbose_name="Nº de Orden de Compra",
            ),
        ),
    ]
