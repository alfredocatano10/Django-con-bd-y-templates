# Generated by Django 3.1.7 on 2021-06-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210624_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, null=True)),
                ('desc', models.CharField(default='', max_length=100, null=True)),
                ('date', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Puesto',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
