# Generated by Django 3.1.3 on 2020-11-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nit', models.CharField(blank=True, max_length=15, verbose_name='Nit')),
                ('favorito', models.BooleanField(verbose_name=False)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=50, verbose_name='Apellido')),
                ('genero', models.CharField(blank=True, max_length=1, verbose_name='Genero')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo')),
                ('edad', models.CharField(blank=True, max_length=3, verbose_name='Edad')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TelefonoCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.PositiveIntegerField()),
                ('predeterminado', models.BooleanField(verbose_name=False)),
            ],
            options={
                'verbose_name': 'Telefono de Cliente',
                'verbose_name_plural': 'Telefonos de Clientes',
            },
        ),
        migrations.CreateModel(
            name='TipoTelefono',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=20, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Tipo de Telefono',
                'verbose_name_plural': 'Tipos de Telefonos',
            },
        ),
    ]
