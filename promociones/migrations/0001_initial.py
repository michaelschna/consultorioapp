# Generated by Django 3.1 on 2020-08-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=4, max_digits=10)),
                ('estado', models.IntegerField()),
                ('user', models.CharField(max_length=15)),
                ('usermod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'producto',
                'db_table': 'producto',
                'ordering': ['created'],
            },
        ),
    ]
