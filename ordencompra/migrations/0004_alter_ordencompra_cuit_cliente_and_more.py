# Generated by Django 4.1.3 on 2022-11-18 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cliente", "0003_alter_cliente_telefono"),
        ("empresa", "0003_alter_empresa_direccion_alter_empresa_email_and_more"),
        ("ordencompra", "0003_rename_fechafin_ordencompra_fecha_fin_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordencompra",
            name="cuit_cliente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="cliente.cliente",
                verbose_name="CUIT Cliente",
            ),
        ),
        migrations.AlterField(
            model_name="ordencompra",
            name="cuit_empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="empresa.empresa",
                verbose_name="CUIT Empresa",
            ),
        ),
        migrations.AlterField(
            model_name="ordencompra",
            name="numero_oc",
            field=models.CharField(max_length=30, verbose_name="Nº de Orden de Compra"),
        ),
    ]