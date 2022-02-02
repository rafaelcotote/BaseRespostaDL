# Generated by Django 4.0.1 on 2022-01-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_oficios_temaofi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficios',
            name='conteudo',
            field=models.TextField(verbose_name='Resposta do Ofício'),
        ),
        migrations.AlterField(
            model_name='oficios',
            name='temaofi',
            field=models.CharField(choices=[('Emissões Atmosféricas', 'Emissões Atmosféricas'), ('Resíduos Solidos', 'Resíduos Sólidos'), ('Efluentes Líquidos', 'Efluentes Líquidos'), ('Fertilizantes', 'Fertilizantes'), ('Programa de Gerenciamento de Riscos - PGR', 'Programa de Gerenciamento de Riscos - PGR')], max_length=50, verbose_name='Tema do Ofício'),
        ),
    ]
