# Generated by Django 3.1.3 on 2020-11-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contactos', '0007_auto_20201109_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefonocliente',
            name='Cliente',
            field=models.ManyToManyField(to='Contactos.Cliente'),
        ),
    ]
