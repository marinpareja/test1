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
    
    class Meta:
        verbose_name_plural = "Ciudades"
        
class PayPal(models.Model):
    Email = models.CharField(max_length=75)
    def __unicode__(self):
        return self.Email
    
    class Meta:
        verbose_name_plural = "PayPal"
            
class Transferencia(models.Model):
    Nombre = models.ForeignKey(Nombre, blank = True)
    Apellido1 = models.ForeignKey(Apellido, related_name="Transf_Apellido1", blank = True)
    Apellido2 = models.ForeignKey(Apellido, related_name="Transf_Apellido2", blank = True)    
    IBAN = models.CharField(max_length=4)
    Entidad = models.IntegerField(max_length=4)
    Sucursal = models.IntegerField(max_length=4)
    Control = models.IntegerField(max_length=2)
    Numero = models.IntegerField(max_length=10)


class SMS(models.Model):
    Tipo = models.CharField(max_length=25)
    Cantidad = models.FloatField()
    def __unicode__(self):
        return self.Tipo      
    
    class Meta:
        verbose_name_plural = "SMS"
                
class Persona_Empresa(models.Model):
    Id = models.AutoField(primary_key = True)
    NIF_CIF = models.CharField(max_length=15, blank = True)
    IsEmpresa = models.BinaryField()
    Nombre_Emp = models.CharField(max_length=50, blank = True)
    Nombre_Per = models.ForeignKey(Nombre, blank = True)
    Apellido1 = models.ForeignKey(Apellido, related_name="Persona_Apellido1", blank = True)
    Apellido2 = models.ForeignKey(Apellido, related_name="Persona_Apellido2", blank = True)
    Domicilio = models.CharField(max_length=50, blank = True)
    Municipio = models.ForeignKey(Ciudad, blank = True)
    Telefono = models.IntegerField(max_length=15, blank = True)
    Contacto = models.ManyToManyField("self", blank = True)
    
    Pago_Pay = models.ManyToManyField(PayPal, blank = True)
    Transferencia = models.ManyToManyField(Transferencia, blank = True)
    SMS = models.ManyToManyField(SMS, blank = True)

    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre_Per, self.Apellido1, self.Apellido2)

    class Meta:
        verbose_name = "Persona o Empresa"
        verbose_name_plural = "Personas o Empresas"
        
class Lugar(models.Model):
    Lugar = models.CharField(max_length=50)
    def __unicode__(self):
        return self.Lugar
    
class Tipo_Servicio(models.Model):
    Id = models.AutoField(primary_key = True) #El precio de un servicio puede variar
    Nombre = models.CharField(max_length=25)
    Precio = models.FloatField()
    def __unicode__(self):
        return self.Nombre  

    class Meta:
        verbose_name_plural = "Lugares"
                
class Cliente(models.Model):
    Id = models.AutoField(primary_key = True)
    Nombre = models.ForeignKey(Nombre)
    Apellido1 = models.ForeignKey(Apellido, related_name="Cliente_Apellido1", blank = True)
    Apellido2 = models.ForeignKey(Apellido, related_name="Cliente_Apellido2", blank = True)
    FechaNaci = models.DateField(blank = True)
    FechaServicio = models.DateField(blank = True)
    Domicilio = models.CharField(max_length=250)
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
    FechaSolicitud = models.DateTimeField()
    FechaServicio = models.DateTimeField(blank = True)
    FotoAntes = models.ImageField(upload_to='before/', blank = True)
    FotoDespues = models.ImageField(upload_to='after/',blank = True)
    Tipo_Servicio = models.ForeignKey(Tipo_Servicio)
    def __unicode__(self):
        return u'%s %s %s' % (self.Empleado, self.Cliente, self.FechaServicio)
    