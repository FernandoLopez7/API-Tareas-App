# Generated by Django 4.2.2 on 2023-07-16 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0004_gruposusuariotareas_usuariotareas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.usuariotareas'),
        ),
    ]
