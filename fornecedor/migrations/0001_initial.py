# Generated by Django 4.0.4 on 2022-06-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
            ],
        ),
    ]
