# Generated by Django 2.2.1 on 2019-06-28 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncionVentricular',
            fields=[
                ('id_func_vent', models.AutoField(primary_key=True, serialize=False)),
                ('vol_relat_rest', models.IntegerField(null=True, verbose_name='vol relat rest')),
                ('vfdvi_rest', models.IntegerField(null=True, verbose_name='vfdvi rest')),
                ('fvsvi_rest', models.IntegerField(null=True, verbose_name='fvsvi rest')),
                ('vfdvi_m2_rest', models.IntegerField(null=True, verbose_name='vfdvi m2 rest')),
                ('fvsvi_m2_rest', models.IntegerField(null=True, verbose_name='fvsvi m2 rest')),
                ('frac_eyeccion_rest', models.IntegerField(null=True, verbose_name='frac eyeccion rest')),
                ('vol_relat_stress', models.IntegerField(null=True, verbose_name='vol relat stress')),
                ('vfdvi_stress', models.IntegerField(null=True, verbose_name='vfdvi stress')),
                ('fvsvi_stress', models.IntegerField(null=True, verbose_name='fvsvi stress')),
                ('vfdvi_m2_stress', models.IntegerField(null=True, verbose_name='vfdvi m2 stress')),
                ('fvsvi_m2_stress', models.IntegerField(null=True, verbose_name='fvsvi m2 stress')),
                ('frac_eyeccion_stress', models.IntegerField(null=True, verbose_name='frac eyeccion stress')),
                ('tid', models.IntegerField(null=True, verbose_name='Tid')),
                ('paciente_fv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pacientes')),
            ],
        ),
    ]
