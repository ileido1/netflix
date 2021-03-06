# Generated by Django 3.2.5 on 2021-07-07 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N/A', 'No aplica')], default='M', max_length=3)),
                ('telefono', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_membresia', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('ccv', models.IntegerField()),
                ('vencimiento', models.DateField()),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Subscripcion_cuenta',
            fields=[
                ('fecha_inicio', models.DateField(auto_now=True, primary_key=True, serialize=False)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.cuenta')),
                ('id_membresia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.membresia')),
            ],
        ),
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField()),
                ('fin_servicio', models.DateTimeField()),
                ('total', models.IntegerField()),
                ('id_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.cuenta')),
                ('id_membresia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.membresia')),
                ('id_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscripcion.tarjeta')),
            ],
        ),
        migrations.AddField(
            model_name='membresia',
            name='cuentas',
            field=models.ManyToManyField(through='subscripcion.Subscripcion_cuenta', to='subscripcion.Cuenta'),
        ),
    ]
