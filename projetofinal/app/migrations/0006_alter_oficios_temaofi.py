# Generated by Django 4.0.1 on 2022-01-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_oficios_recebimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='temaofi',
            field=models.CharField(choices=[('Emissões Atmosféricas', 'Emissões Atmosféricas'), ('Resíduos Solidos', 'Resíduos Sólidos'), ('Efluentes Líquidos', 'Efluentes Líquidos'), ('Fertilizantes', 'Fertilizantes'), ('Programa de Gerenciamento de Riscos - PGR', 'Programa de Gerenciamento de Riscos')], max_length=50, verbose_name='Tema do Ofício'),
        ),
    ]
