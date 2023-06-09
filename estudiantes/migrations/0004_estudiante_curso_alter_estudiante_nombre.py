# Generated by Django 4.2.1 on 2023-05-18 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('estudiantes', '0003_remove_estudiante_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.curso'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
