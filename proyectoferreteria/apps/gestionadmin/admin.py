from django.contrib import admin
from django.db import models
from proyectoferreteria.apps.gestionadmin.models import FormaPago, MetodoPago, Garantia, Marca, Categoria, Proveedor,Cliente, Planilla, Empleado, Producto, Factura, TurnoEmpleado
from django.core.paginator import Paginator
# Register your models here.
##@admin.register(Factura)




class MarcaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('idMarca','nombreMarca')
   
admin.site.register(Marca, MarcaAdmin)


class ClienteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Cliente','Nombre_Cliente','Correo_Cliente','Direccion_Cliente','Telefono_Cliente')
    ##list_filter = ('Nombre_Cliente','Id_Cliente')
    ##list_display_links = ('Id_Cliente', 'Correo_Cliente')
    search_fields = ('Nombre_Cliente','Id_Cliente')

admin.site.register(Cliente, ClienteAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display =('Id_Categoria','Descripcion_Categoria')
    search_fields =('Id_Categoria','Descripcion_Categoria')

admin.site.register(Categoria,CategoriaAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Proveedor','Nombre_Proveedor','Correo_Proveedor','Direccion_Proveedor','Telefono_Proveedor')
    search_fields = ('Id_Proveedor','Nombre_Proveedor','Correo_Proveedor','Direccion_Proveedor','Telefono_Proveedor')

admin.site.register(Proveedor,ProveedorAdmin)

class GarantiaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Garantia','Descripcion_Garantia','Tiempo_Garantia_Mes')
    search_fields = ('Id_Garantia','Descripcion_Garantia','Tiempo_Garantia_Mes')
admin.site.register(Garantia,GarantiaAdmin) 
    

class FormaPagoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Forma_Pago','Descripcion_Forma_Pago')
    search_fields= ('Id_Forma_Pago','Descripcion_Forma_Pago')
admin.site.register(FormaPago,FormaPagoAdmin)

class MetodoPagoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('idMetodoPago','descripcionMetodoPago')
    search_fields= ('idMetodoPago','descripcionMetodoPago')
admin.site.register(MetodoPago, MetodoPagoAdmin)

class PlanillaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Planilla','Sueldo_Base','IHSS','RAP')
    search_fields = ('Id_Planilla','Sueldo_Base','IHSS','RAP')
admin.site.register(Planilla,PlanillaAdmin)


class EmpleadoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Empleado','Id_Turno','Id_Planilla','Nombre_Empleado','Direccion_Empleado','Telefono_Empleado')
    search_fields = ('Id_Empleado','Id_Turno','Id_Planilla','Nombre_Empleado','Direccion_Empleado','Telefono_Empleado')
admin.site.register(Empleado,EmpleadoAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Producto','Nombre_Producto','Precio_Venta','Precio_Compra','Id_Marca','Id_Categoria','Id_Garantia','Existencia','Existencia_Minima')
    search_fields = ('Id_Producto','Nombre_Producto','Precio_Venta','Precio_Compra','Id_Marca','Id_Categoria','Id_Garantia','Existencia','Existencia_Minima')
admin.site.register(Producto,ProductoAdmin)


class TurnoEmpleadoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Turno','Turno','Hora_de_Entrada','Hora_de_Salida')
    search_fields = ('Id_Turno','Turno','Hora_de_Entrada','Hora_de_Salida')
admin.site.register(TurnoEmpleado,TurnoEmpleadoAdmin)

class FacturaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('Id_Factura','Id_Empleado','Id_Cliente','Id_MetodoPago','Id_FormaPago','Numero_Sar','Codigo_CAI','ISV18','ISV15','Total_Factura')
    search_fields = ('Id_Factura','Total_Factura')
admin.site.register(Factura, FacturaAdmin)



