# -*- coding: utf-8 -*-
#Módulo creado por Ing. Industrial Hermes Colina
{
    'name': "contaag_saleorder_email",

    'summary': """
        Modificaciones del modulo ventas en la plantilla orden de venta""",

    'description': """
        Campo de correo electronico en la informacion de cliente en la plantilla pedidos de ventas
    """,

    'author': "Ing. Hermes Colina",
    'website': "https://blogdelingenieroindustrialluz.blogspot.com/",
    
    #Siempre se debe agregar los módulos de los que depende el nuevo módulo para evitar errores
    #inesperados. (Ej. TypeError, ¡tal módulo no existe!)
    'depends': ['base'],

    #Agregar primero los wizard para prevenir errores de compilación.
    
    #Se han configurado permisos sobre los elementos que maneja este módulo
    #esto permite que solo los Usuarios con el permiso "Acceso datos empleados - nomina Drolanca"
    #puedan hacer uso correcto de los componentes aqui desarrollados, para activar este permiso
    #dirigirse a Configuración->Usuarios, y dentro del Usuario activar el permiso.

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/email.xml',
    ],

    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],

    #'qweb': [
    #    'static/src/bugfix/bugfix.xml',
    #    'static/src/xml/hr_templates.xml',
    #],
}