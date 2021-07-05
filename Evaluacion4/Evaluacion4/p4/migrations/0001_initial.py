# Generated by Django 3.2.4 on 2021-07-04 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('idmoneda', models.IntegerField(primary_key=True, serialize=False, verbose_name='id moneda')),
                ('moneda', models.CharField(max_length=6, verbose_name='moneda')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('numeroID', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('nombre', models.CharField(max_length=40, verbose_name='nombre')),
                ('telefono', models.IntegerField(max_length=10, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('email', models.CharField(max_length=40, verbose_name='correo electronico')),
                ('pais', models.CharField(max_length=20, verbose_name='pais')),
                ('contraseña', models.CharField(max_length=8, verbose_name='contraseña')),
                ('tipomoneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p4.moneda')),
            ],
        ),
    ]