# encoding: utf-8

from django.db import models

# Create your models here.

class Nombre(models.Model):
    Nombre = models.CharField(max_length=45, unique = True)
    def __unicode__(self):
        return unicode(self.Nombre)
    
    class Meta:
        ordering = ['Nombre']

class Apellido(models.Model):
    Apellido = models.CharField(max_length=50, unique = True)
    def __unicode__(self):
        return unicode(self.Apellido)

    class Meta:
        ordering = ['Apellido']
            
class Provincia(models.Model):
    id=models.IntegerField(primary_key=True)    
    Provincia = models.CharField(max_length=50, unique = True)
    def __unicode__(self):
        return unicode(self.Provincia)
    
class Ciudad(models.Model):
    Municipio = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    Provincia = models.ForeignKey(Provincia)
    CP = models.IntegerField(max_length=5)
    def __unicode__(self):
        return unicode(self.Municipio)
    
    class Meta:
        verbose_name_plural = "Ciudades"
        ordering = ['Municipio']
        
class PayPal(models.Model):
    Email = models.EmailField(unique = True)
    def __unicode__(self):
        return unicode(self.Email)
    
    class Meta:
        verbose_name_plural = "PayPal"
            
class Transferencia(models.Model):
    Nombre = models.ForeignKey(Nombre, blank = True)
    Apellido1 = models.ForeignKey(Apellido, related_name="Transf_Apellido1", blank = True, verbose_name='Primer Apellido')
    Apellido2 = models.ForeignKey(Apellido, related_name="Transf_Apellido2", blank = True, verbose_name='Segundo Apellido')    
    IBAN = models.CharField(max_length=4)
    Entidad = models.IntegerField(max_length=4)
    Sucursal = models.IntegerField(max_length=4)
    Control = models.IntegerField(max_length=2)
    Numero = models.IntegerField(max_length=10)
    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre, self.Apellido1, self.Apellido2)

class SMS(models.Model):
    Tipo = models.CharField(max_length=25)
    Cantidad = models.FloatField()
    def __unicode__(self):
        return unicode(self.Tipo)
    
    class Meta:
        verbose_name_plural = "SMS"
                
class Persona_Empresa(models.Model):
    Id = models.AutoField(primary_key = True)
    NIF_CIF = models.CharField(max_length=15, blank = True, verbose_name='NIF/CIF')
    IsEmpresa = models.BinaryField(verbose_name='¿Es empresa?')
    Nombre_Emp = models.CharField(max_length=50, blank = True, verbose_name='Nombre de la Empresa')
    Nombre_Per = models.ForeignKey(Nombre, blank = True, verbose_name='Nombre')
    Apellido1 = models.ForeignKey(Apellido, related_name="Persona_Apellido1", blank = True, verbose_name='Primer Apellido')
    Apellido2 = models.ForeignKey(Apellido, related_name="Persona_Apellido2", blank = True, verbose_name='Segundo Apellido')
    Domicilio = models.CharField(max_length=50, blank = True)
    Municipio = models.ForeignKey(Ciudad, blank = True)
    Telefono = models.IntegerField(max_length=15, blank = True, verbose_name='Teléfono')
    Contacto = models.ManyToManyField("self", blank = True, verbose_name='Persona de Contacto')
    Email = models.EmailField(blank = True)
        
    PayPal = models.ManyToManyField(PayPal, blank = True)
    Transferencia = models.ManyToManyField(Transferencia, blank = True)
    SMS = models.ManyToManyField(SMS, blank = True)

    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre_Per, self.Apellido1, self.Apellido2)

    class Meta:
        verbose_name = "Persona o Empresa"
        verbose_name_plural = "Personas o Empresas"
        #ordering = ['Nombre_Per', 'Apellido1', 'Apellido2']
        
class Lugar(models.Model):
    Lugar = models.CharField(max_length=50)
    Municipio = models.ForeignKey(Ciudad)
    URL = models.URLField()
    def __unicode__(self):
        return self.Lugar
    
    class Meta:
        verbose_name_plural = "Lugares"    
        ordering = ['Municipio']

class Tipo_Servicio(models.Model):
    Id = models.AutoField(primary_key = True) #El precio de un servicio puede variar
    Nombre = models.CharField(max_length=25)
    Precio = models.FloatField()
    def __unicode__(self):
        return self.Nombre  

    class Meta:
        verbose_name = "Tipo de Servicio"
        verbose_name_plural = "Tipo de Servicios"
        ordering = ['Nombre']
                        
class Cliente(models.Model):
    Id = models.AutoField(primary_key = True)
    Nombre = models.ForeignKey(Nombre)
    Apellido1 = models.ForeignKey(Apellido, related_name="Cliente_Apellido1", blank = True, verbose_name='Primer Apellido')
    Apellido2 = models.ForeignKey(Apellido, related_name="Cliente_Apellido2", blank = True, verbose_name='Segundo Apellido')
    FechaNaci = models.DateField(blank = True, verbose_name='Fecha de Nacimiento')
    FechaF = models.DateField(blank = True, verbose_name='Fecha del Servicio')
    Domicilio = models.CharField(max_length=250)
    Lugar = models.ForeignKey(Lugar)
    Municipio = models.ForeignKey(Ciudad)
    Tipo_Servicio = models.ForeignKey(Tipo_Servicio)
    def __unicode__(self):
        return u'%s %s %s' % (self.Nombre, self.Apellido1, self.Apellido2)
        
class Empleado(models.Model):
    Empleado = models.ForeignKey(Persona_Empresa)
    SS = models.CharField(max_length=25, verbose_name='S.S.')
    Transferencia = models.ForeignKey(Transferencia)
    def __unicode__(self):
        return unicode(self.Empleado) 

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        
class Pago_Empleado(models.Model):
    Empleado = models.ForeignKey(Persona_Empresa)
    Fecha = models.DateField()
    Servicios = models.FloatField()
    Bonificacion = models.FloatField()
    Cantidad = models.FloatField()
    def __unicode__(self):
        return self.Empleado 

    class Meta:
        verbose_name = "Pago de Empleado"
        verbose_name_plural = "Pago de Empleados"

def upload_path_handler(instance, filename):
    return "{Provincia}/{Municipio}/{Lugar}/{Domicilio}/{FServicio}/{file}".format(
                                                                    Provincia=instance.Cliente.Municipio.Provincia,
                                                                    Municipio=instance.Cliente.Municipio, 
                                                                    Lugar=instance.Cliente.Lugar, 
                                                                    Domicilio=instance.Cliente.Domicilio,
                                                                    FServicio=instance.FechaServicio, 
                                                                    file=filename)
                   
class Servicio(models.Model):
    Id = models.AutoField(primary_key = True)
    Persona_Empresa = models.ForeignKey(Persona_Empresa, related_name="Persona_Empresa", verbose_name='Persona o Empresa')
    Cliente = models.ForeignKey(Cliente)
    Empleado = models.ForeignKey(Empleado)
    FechaSolicitud = models.DateTimeField(verbose_name='Fecha de Solicitud')
    FechaServicio = models.DateTimeField(blank = True, verbose_name='Fecha del Servicio')
    FotoAntes = models.ImageField(upload_to=upload_path_handler, blank = True, verbose_name='Foto de Antes')
    FotoDespues = models.ImageField(upload_to=upload_path_handler,blank = True, verbose_name='Foto de Después')
    Tipo_Servicio = models.ForeignKey(Tipo_Servicio)
    def __unicode__(self):
        return u'Empleado: %s - Cliente: %s - Fecha Servicio: %s' % (self.Empleado, self.Cliente, self.FechaServicio)
    