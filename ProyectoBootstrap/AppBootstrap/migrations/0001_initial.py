# Generated by Django 4.0.6 on 2022-07-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=70)),
                ('fecha_publicacion', models.DateField(null=True)),
            ],
        ),
    ]