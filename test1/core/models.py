from django.db import models

# Create your models here.

class Nombre(models.Model):
    Nombre = models.CharField(max_length=45)
    def __unicode__(self):
        return self.Nombre

class Apellido(models.Model):
    Apellido = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Apellido

class Provincia(models.Model):    
    Provincia = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Provincia
    
class Ciudad(models.Model):
    Municipio = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    Provincia = models.ForeignKey(Provincia)
    CP = models.IntegerField()
    def __unicode__(self):
        return self.Municipio
    
class Persona(models.Model):
    Nombre = models.ForeignKey(Nombre)
    Apellido1 = models.ForeignKey(Apellido)
    #Apellido2 = models.ForeignKey(Apellido)
    Municipio = models.ForeignKey(Ciudad)
    Telefono = models.IntegerField()
    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre, self.Apellido1, self.Apellido2)

class Forma_Pago(models.Model):
    Tipo = models.CharField(max_length=25)
    def __unicode__(self):
        return self.Tipo
        
class PayPal(models.Model):
    Email = models.CharField(max_length=75)
    def __unicode__(self):
        return self.Email
    
class Transferencia(models.Model):
    Nombre = models.CharField(max_length=50)
    Concepto = models.CharField(max_length=100)
    def __unicode__(self):
        return self.Nombre

class SMS(models.Model):
    Tipo = models.CharField(max_length=25)
    Cantidad = models.FloatField()
    def __unicode__(self):
        return self.Tipo      
          
class Efectivo(models.Model):
    Efectivo = models.BinaryField()
    def __unicode__(self):
        return self.Efectivo 
    
class Empleado(models.Model):
    Empleado = models.ForeignKey(Persona)
    SS = models.IntegerField()
    Transferencia = models.ForeignKey(Transferencia)
    def __unicode__(self):
        return self.Empleado 
        
class Pago_Empleado(models.Model):
    Empleado = models.ForeignKey(Persona)
    Fecha = models.DateField()
    Servicios = models.FloatField()
    Bonificacion = models.FloatField()
    Cantidad = models.FloatField()
    def __unicode__(self):
        return self.Empleado 
        
class Empresa(models.Model):
    Nombre = models.CharField(max_length=50)
    CIF = models.CharField(max_length=25)
    Contacto = models.ForeignKey(Persona)
    def __unicode__(self):
        return self.Nombre
    
class Cliente(models.Model):
    Empresa = models.ForeignKey(Empresa)
    Persona = models.ForeignKey(Persona)
    #Cliente = models.ForeignKey(Persona)
    Transferencia = models.ForeignKey(Transferencia)

class Tipo(models.Model):
    Nombre = models.CharField(max_length=25)
    Tiempo = models.IntegerField()
    Multip = models.FloatField()
    def __unicode__(self):
        return self.Nombre    
    
class Servicio(models.Model):
    Cliente = models.ForeignKey(Cliente)
    Empleado = models.ForeignKey(Empleado)
    FechaSolicitud = models.DateField()
    FechaServicio = models.DateField()
    FotoAntes = models.FilePathField()
    FotoDespues = models.FilePathField()
    Tipo = models.ForeignKey(Tipo)
    Transferencia = models.ForeignKey(Transferencia)

    