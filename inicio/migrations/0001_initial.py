# Generated by Django 5.0.6 on 2024-06-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Famosos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('profesion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('temporadas', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]