from django.db import models

# Create your models here.
class Cuenta(models.Model):
    nombre_usuario = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    contrasena = models.CharField( max_length=50)
    nombre = models.CharField( max_length=50)
    apellido= models.CharField( max_length=50)
    fecha_nacimiento= models.DateField( auto_now=False, auto_now_add=False)
    sexo_choices= [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('N/A', 'No aplica'),
    ]   
    sexo = models.CharField(
        max_length=3,
        choices=sexo_choices,
        default='M',
    )
    telefono = models.IntegerField()
    fecha_creacion = models.DateTimeField( auto_now=False, auto_now_add=False)

class Membresia(models.Model):
   nombre_membresia= models.CharField(max_length=50)
   precio = models.IntegerField()
   cuentas = models.ManyToManyField(Cuenta, through='Subscripcion_cuenta')

class Subscripcion_cuenta(models.Model):
    fecha_inicio= models.DateField(auto_now=True, primary_key=True)
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    id_membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False,null=True)

class Tarjeta(models.Model):
   numero_tarjeta= models.IntegerField()
   tipo= models.CharField( max_length=50)
   ccv=models.IntegerField()
   id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
   vencimiento=models.DateField( auto_now=False, auto_now_add=False)
        
class Subscripcion(models.Model):
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    id_membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fecha_pago= models.DateTimeField(auto_now=False, auto_now_add=False)
    fin_servicio= models.DateTimeField( auto_now=False, auto_now_add=False)
    total = models.IntegerField()