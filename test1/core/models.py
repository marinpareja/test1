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
    CP = models.IntegerField(primary_key = True)
    def __unicode__(self):
        return self.Municipio

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
        
class Persona_Empresa(models.Model):
    Id = models.AutoField(primary_key = True)
    NIF_CIF = models.CharField(max_length=15)
    IsEmpresa = models.BinaryField()
    Nombre_Emp = models.CharField(max_length=50)
    Nombre_Per = models.ForeignKey(Nombre)
    Apellido1 = models.ForeignKey(Apellido, related_name="Persona_Apellido1")
    Apellido2 = models.ForeignKey(Apellido, related_name="Persona_Apellido2")
    Domicilio = models.CharField(max_length=50)
    Municipio = models.ForeignKey(Ciudad)
    Telefono = models.IntegerField(max_length=15)
    Contacto = models.ManyToManyField("self")
    
    Pago_Pay = models.ManyToManyField(PayPal)
    Transferencia = models.ManyToManyField(Transferencia)
    SMS = models.ManyToManyField(SMS)

    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre, self.Apellido1, self.Apellido2)

class Lugar(models.Model):
    Lugar = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Lugar
    
class Tipo_Servicio(models.Model):
    Id = models.AutoField(primary_key = True) #El precio de un servicio puede variar
    Nombre = models.CharField(max_length=25)
    Tiempo = models.IntegerField()
    Multip = models.FloatField()
    def __unicode__(self):
        return self.Nombre  
        
class Cliente(models.Model):
    Id = models.AutoField(primary_key = True)
    Nombre = models.ForeignKey(Nombre)
    Apellido1 = models.ForeignKey(Apellido, related_name="Cliente_Apellido1")
    Apellido2 = models.ForeignKey(Apellido, related_name="Cliente_Apellido2")
    FechaNaci = models.DateField()
    FechaServicio = models.DateField()
    Domicilio =models.CharField(max_length=250)
    Lugar = models.ForeignKey(Lugar)
    Municipio = models.ForeignKey(Ciudad)
    Tipo_Servicio = models.ForeignKey(Tipo_Servicio)
    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre, self.Apellido1, self.Apellido2)
        
class Empleado(models.Model):
    Empleado = models.ForeignKey(Persona_Empresa)
    SS = models.IntegerField()
    Transferencia = models.ForeignKey(Transferencia)
    def __unicode__(self):
        return self.Empleado 
        
class Pago_Empleado(models.Model):
    Empleado = models.ForeignKey(Persona_Empresa)
    Fecha = models.DateField()
    Servicios = models.FloatField()
    Bonificacion = models.FloatField()
    Cantidad = models.FloatField()
    def __unicode__(self):
        return self.Empleado 
           
class Servicio(models.Model):
    Id = models.AutoField(primary_key = True)
    Persona_Empresa = models.ForeignKey(Persona_Empresa, related_name="Persona_Empresa")
    Cliente = models.ForeignKey(Cliente)
    Empleado = models.ForeignKey(Empleado)
    FechaSolicitud = models.DateField()
    FechaServicio = models.DateTimeField()
    FotoAntes = models.FilePathField()
    FotoDespues = models.FilePathField()
    Tipo_Servicio = models.ForeignKey(Tipo_Servicio)
    def __unicode__(self):
        return u'%s %s %s' % (self.Empleado, self.Cliente, self.FechaServicio)
    