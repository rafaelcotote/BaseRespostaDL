# Generated by Django 4.0.1 on 2022-01-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_oficios_status_oficio_alter_oficios_anexs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='recebimento',
            field=models.DateField(blank=True, verbose_name='Data do Recebimento'),
        ),
    ]
