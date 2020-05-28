from django.db import models
from datetime import date
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db.models.functions import Concat
import datetime
from django.core.paginator import Paginator

now= datetime.datetime.now()
# Create your models here.
from django.core.exceptions import ValidationError
"""Validaciones"""
def validar_mayor_a_tres(value):
    if value<3:
        raise ValidationError('Numero debe ser mayor que 2')

def validarquenoseacero(value):
    if(value)<1:
         raise ValidationError('Numero debe ser mayor que 1')

def validarsueldo(value):
    if value<1000:
        raise ValidationError('Sueldo invalido debe ser mayor a 999')
    if value>200000:
        raise ValidationError('Sueldo invalido debe ser menor a 200000')

def validarhora(value):
    lista=[]
    for indice in value:
        lista.append(indice)
    if lista[2]!=":":
        raise ValidationError('Hora inválida el formato es por ejemplo: 12:45')
    if not (len(value)) > 4:
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')
    if lista[0]=="3" or lista[0]=="4" or lista[0]=="5" or lista[0]=="6" or lista[0]=="7" or lista[0]=="8" or lista[0]=="9":
        raise ValidationError('Hora incorrecta el formato es por ejemplo: 12:45')

def validarnombre(value):
    lista=[]
    n=0
    for indice in value:
        
        lista.append(indice)
        if(lista[n]=="0" or lista[n]=="1" or lista[n]=="2" or lista[n]=="3" or lista[n]=="4" or lista[n]=="5" or lista[n]=="6" or lista[n]=="7" or lista[n]=="8" or lista[n]=="9"):
             raise ValidationError('Nombre incorrecto, solo se permite ingresar letras')
        n=n+1
    
    
    if (len(lista))<3:
        raise ValidationError('El texto es inválido debe ser mayor a 3 caracteres, digite de nuevo')
    
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
        raise ValidationError('El texto debe ser valido digite de nuevo')


    lista=[]
    vocal=["a","e","i","o","u","á","é","í","ó","ú"]
    cont=0
    for i in vocal:
        for j in value:
            if(i==j):
                cont+=1
    if(cont<1):
     raise ValidationError('El texto es inválido, digite de nuevo')   
    
def validardireccion(value):
    lista=[]
    for indice in value:
        lista.append(indice)
    
    if(len(lista)<30):
        raise ValidationError('La direccion debe contener al menos 30 caracteres')
    if lista[0]=="a" and lista [1]=="b" and lista[2]=="c":
        raise ValidationError('La direccion debe ser válida digite de nuevo debe contener al menos 1 vocal')

    if lista[0]=="." or lista[1]==",":
       raise ValidationError('La direccion no puede contener un punto al inicio')
     
def validarnumero(value):
    numeros=[]
    n=0
    for indice in value:
        numeros.append(indice)
        if(numeros[n]!="0" and numeros[n]!="1" and numeros[n]!="2" and numeros[n]!="3" and numeros[n]!="4" and numeros[n]!="5" and numeros[n]!="6" and numeros[n]!="7" and numeros[n]!="8" and numeros[n]!="9"):
            raise ValidationError('El numero no puede contener letras')
        n=n+1
        
    if ((numeros[0]=="0") or (numeros[0]=="1") or (numeros[0]=="4") or (numeros[0]=="5") or (numeros[0]=="6")):
        raise ValidationError('El numero no es válido, intente de nuevo')
    if(len(numeros))<8:
        raise ValidationError('El numero debe contener al menos 8 digitos, intente de nuevo')
    if("-" in numeros or ("." in numeros)):
        raise ValidationError('El numero debe contener al menos 8 digitos, ejemplo 99234567')

def validartamaño(value):
    if  value<1:
        raise ValidationError('El numero no puede ser menor a 0')
    if  value>999999999:
        raise ValidationError('El numero no puede ser mayor a 9 digitos')

def validarnegativos(value):
    if value<0:
        raise ValidationError('El numero no puede ser menor que 0')
    if value>1000000000:
        raise ValidationError('El numero no puede ser superior a 100')

def validarcorreoexistenteProveedor(value):
    listaE = Proveedor.objects.all()
    for data in listaE:
        if(data.Correo_Proveedor==value):
            raise ValidationError('El correo ya existe')

def validarcorreoexistenteCliente(value):
    listaE = Cliente.objects.all()
    for data in listaE:
        if(data.Correo_Cliente==value):
            raise ValidationError('El correo ya existe')


"""Clases"""

class Marca (models.Model):
    idMarca=models.AutoField(verbose_name='Id', primary_key=True, validators=[validartamaño])
    nombreMarca= models.CharField(verbose_name='Descripción', max_length=30, validators=[validarnombre])
    def __str__(self):
        return '{}'.format(self.nombreMarca)

    
    
"""1.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
2.-Se agrego el models.Autofield para que sea autoincremental"""
class Categoria (models.Model):
    Id_Categoria=models.AutoField(verbose_name='Id', primary_key=True, validators=[validartamaño])
    Descripcion_Categoria=models.CharField(verbose_name='Descripción',max_length=30,validators=[validarnombre])

    def __str__(self):
        return '{}'.format(self.Descripcion_Categoria)
    

"""5.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
6.-Se agrego el models.Autofield para que sea autoincremental"""
class Proveedor (models.Model):
    Id_Proveedor = models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Nombre_Proveedor=models.CharField(verbose_name='Nombre',max_length=35,validators=[validarnombre])
    Correo_Proveedor=models.EmailField(verbose_name='Correo',max_length=30,blank=True, validators=[validarcorreoexistenteProveedor])
    Direccion_Proveedor=models.TextField(verbose_name='Dirección',max_length=100, validators=[validardireccion])
    Telefono_Proveedor=models.CharField(verbose_name='Telefono',max_length=8, validators=[validarnumero])
     
    def __str__(self):
        return '{}'.format(str(self.Id_Proveedor)+" "+self.Nombre_Proveedor)

"""3.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
4.-Se agrego el models.Autofield para que sea autoincremental"""
class Garantia (models.Model):
    Id_Garantia = models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Descripcion_Garantia=models.TextField(verbose_name='Descripcion',)
    Tiempo_Garantia_Mes=models.IntegerField(verbose_name='Garantia',)

    def __str__(self):
        return '{}'.format(self.Descripcion_Garantia)

"""7.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
8.-Se agrego el models.Autofield para que sea autoincremental"""
class FormaPago(models.Model):
    Id_Forma_Pago=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Descripcion_Forma_Pago=models.TextField(verbose_name='  Descripcion',max_length=30,validators=[validarnombre])
    def __str__(self):
        return '{}'.format(str(self.Id_Forma_Pago)+" "+self.Descripcion_Forma_Pago)

"""10.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
11.-Se agrego el models.Autofield para que sea autoincremental
26.- no se aplicaron los cambios anteriores porque explotaba"""
class MetodoPago(models.Model):
    idMetodoPago=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    descripcionMetodoPago=models.TextField(verbose_name='Descripcion',max_length=30, validators=[validarnombre])
    def __str__(self):
        return '{}'.format(str(self.idMetodoPago)+" "+self.descripcionMetodoPago)

"""12.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
13.-Se agrego el models.Autofield para que sea autoincremental"""
class Cliente(models.Model):
    Id_Cliente=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Nombre_Cliente=models.CharField(verbose_name='Nombre',max_length=30, validators=[validarnombre])
    Correo_Cliente=models.EmailField(verbose_name='Correo',max_length=30, blank=True,validators=[validarcorreoexistenteCliente])
    Direccion_Cliente=models.TextField(verbose_name='Dirección',max_length=100, validators=[validardireccion])
    Telefono_Cliente=models.CharField(verbose_name='Teléfono',max_length=8, validators=[validarnumero])
    
    def __str__(self):
        return '{}'.format(str(self.Id_Cliente)+" "+self.Nombre_Cliente)

"""14.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
15.-Se agrego el models.Autofield para que sea autoincremental"""
class TurnoEmpleado(models.Model):
    Id_Turno=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Turno=models.CharField(verbose_name='Turno',max_length=30, validators=[validarnombre])
    Hora_de_Entrada=models.CharField(verbose_name='Hora entrada',max_length=5, validators=[validarhora])
    Hora_de_Salida=models.CharField(verbose_name='Hora salida',max_length=5, validators=[validarhora])
    def __str__(self):
        return '{}'.format(str(self.Id_Turno)+" "+self.Turno)


"""9.-Se valido que el IHSS y el RAP no fueran numeros negativos"""
"""16.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
17.-Se agrego el models.Autofield para que sea autoincremental
18.-Se elimino el sueldo base de la impresion porque creaba un error que hay que resolver"""
class Planilla(models.Model):
    Id_Planilla=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Sueldo_Base=models.IntegerField(verbose_name='Sueldo Base',validators=[validarsueldo])
    IHSS=models.IntegerField(verbose_name='IHSS',validators=[validarnegativos])
    RAP=models.IntegerField(verbose_name='RAP',validators=[validarnegativos])

    def __str__(self):
        return '{}'.format(str(self.Id_Planilla)+" "+str(self.Sueldo_Base))

"""18.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
19.-Se agrego el models.Autofield para que sea autoincremental"""
class Empleado(models.Model):
    Id_Empleado=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Id_Turno=models.ForeignKey(TurnoEmpleado, verbose_name='Turno', null=False, blank=False, on_delete=models.PROTECT)
    Id_Planilla=models.ForeignKey(Planilla, verbose_name='Planilla', null=False, blank=False, on_delete=models.PROTECT)
    Nombre_Empleado=models.CharField(verbose_name='Nombre',max_length=30,validators=[validarnombre])
    Direccion_Empleado=models.TextField(verbose_name='Direccion',max_length=100, validators=[validardireccion])
    Telefono_Empleado=models.CharField(verbose_name='Telefono',max_length=8, validators=[validarnumero])
    def __str__(self):
        return '{}'.format(str(self.Id_Empleado)+" "+self.Nombre_Empleado)


"""20.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
21.-Se agrego el models.Autofield para que sea autoincremental"""
class Producto(models.Model):
    Id_Producto=models.AutoField(verbose_name='Id',primary_key=True, validators=[validartamaño])
    Nombre_Producto=models.CharField(verbose_name='Nombre',max_length=40, validators=[validarnombre])
    Precio_Venta=models.IntegerField(verbose_name='Precio Venta',validators=[validarquenoseacero])
    Precio_Compra=models.IntegerField(verbose_name='Precio Compra',validators=[validarquenoseacero])
    Id_Marca=models.ForeignKey(Marca,verbose_name='Marca', null=False, blank=False, on_delete=models.PROTECT)
    Id_Categoria=models.ForeignKey(Categoria, verbose_name='Categoria', null=False, blank=False, on_delete=models.PROTECT)
    Id_Garantia=models.ForeignKey(Garantia,verbose_name='Garantia', null=False, blank=False, on_delete=models.PROTECT)
    Existencia=models.IntegerField(verbose_name='Existencia',validators=[validarquenoseacero])
    Existencia_Minima=models.IntegerField(verbose_name='Existencia Minima',validators=[validar_mayor_a_tres])
    def __str__(self):
        return '{}'.format(str(self.Id_Producto)+" "+self.Nombre_Producto)

"""22.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
23.-Se agrego el models.Autofield para que sea autoincremental"""
class Factura(models.Model):
    Id_Factura=models.AutoField(verbose_name='Id de factura',primary_key=True, validators=[validartamaño])
    Id_Empleado=models.ForeignKey(Empleado, verbose_name='Empleado', null=False, blank=False, on_delete=models.PROTECT)
    Id_Cliente=models.ForeignKey(Cliente, verbose_name='Cliente', null=True, blank=True, on_delete=models.PROTECT)
    Id_MetodoPago=models.ForeignKey(MetodoPago, verbose_name='Metodo de pago',null=False, blank=False, on_delete=models.PROTECT)
    Id_FormaPago=models.ForeignKey(FormaPago, verbose_name='Forma de Pago',null=False, blank=False, on_delete=models.PROTECT)
    Numero_Sar=models.CharField(verbose_name='Numero de la SAR',max_length=15, default='004-340-345KN')
    #Para presentarse no puede ser ManyToManyField
    Id_producto=models.ManyToManyField(Producto, verbose_name='Producto')
    Fecha=models.DateTimeField(auto_now_add=True)
    Codigo_CAI=models.CharField(max_length=35, verbose_name='Codigo CAI',  default='114-560-345KJ')
    ISV18=models.FloatField(validators=[validarnegativos], verbose_name='ISV al 18%')
    ISV15=models.FloatField(validators=[validarnegativos], verbose_name='ISV al 15%')
    Total_Factura=models.FloatField(verbose_name='Total')
    def __str__(self):
        return '{}'.format(str(self.Id_Factura)+" "+str(self.Id_Empleado))

"""24.-Se modifico el guien bajo para hacer mas legible y se cambiaron minusculas por mayusculas
25.-Se agrego el models.Autofield para que sea autoincremental"""
#class FacturaDetalle(models.Model):
#    Id_Factura_Detalle = models.AutoField(primary_key=True, validators=[validartamaño])
#    Id_Factura = models.OneToOneField(Factura, on_delete=models.PROTECT)
#    Id_Producto=models.ForeignKey(Producto, null=False, blank=False, on_delete=models.PROTECT)
#    Cantidad = models.IntegerField(validators=[validarquenoseacero])
#
#    def __str__(self):
#        return '{}'.format(" "+str(self.Id_Factura_Detalle)+" "+""+str(self.Id_Factura))



