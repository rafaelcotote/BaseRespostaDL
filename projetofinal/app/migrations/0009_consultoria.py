# Generated by Django 4.0.1 on 2022-01-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_oficios_questionamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_consulta', models.CharField(max_length=50)),
            ],
        ),
    ]