import tkinter
import almacenamiento
import recarga
from tkinter import messagebox

almacenamiento.conectar(almacenamiento.id_usuario)

contenedor_principal = ''
nombre_producto = ''
codigo_producto = ''
inventario_producto = ''
precio_producto = ''

def contenido_agregar(ventana, contenedor_agregar = '', contenedor_inicio = ''):

    global nombre_producto
    global codigo_producto
    global inventario_producto
    global precio_producto

    nombre_producto = tkinter.StringVar()
    codigo_producto = tkinter.StringVar()
    inventario_producto = tkinter.StringVar()
    precio_producto = tkinter.StringVar()

    def agregar_producto():

        global nombre_producto
        global codigo_producto
        global inventario_producto
        global precio_producto

        codigo_duplicado = False
        espacios_blancos = []
        error_codigo_precio = []

        if nombre_producto.get() == '':

            espacios_blancos.append('nombre')

        if codigo_producto.get() == '':

            espacios_blancos.append('codigo')

        if inventario_producto.get() == '':

            espacios_blancos.append('inventario')

        if precio_producto.get() == '':

            espacios_blancos.append('precio')

        if len(espacios_blancos) == 4:

            messagebox.showerror('ERROR', 'HAZ DEJADO TODOS LOS ESPACIOS EN BLANCO,\nINTENTALO DE NUEVO')

        elif len(espacios_blancos) > 1:

            resultado_espacios = ''

            for espacio in espacios_blancos:

                if espacio == espacios_blancos[len(espacios_blancos)-1]:

                    resultado_espacios += espacio.upper()

                else:

                    resultado_espacios += espacio.upper()+', '

            messagebox.showerror('\nERROR', f'HAZ DEJADO LOS ESPACIOS DE\n{resultado_espacios}\nEN BLANCO')

        elif len(espacios_blancos) == 1:

            messagebox.showerror('ERROR', f'HAZ DEJADO EL ESPACIO DE\n{espacios_blancos[0].upper()} EN BLANCO')

        else:

            try:

                float(inventario_producto.get())

            except:

                error_codigo_precio.append('inventario')

            try:

                float(precio_producto.get())

            except:

                error_codigo_precio.append('precio')

        if len(error_codigo_precio) == 2:

            messagebox.showerror('ERROR', 'HAZ INGRESADO DATOS INCORRECTOS\nEN INVENTARIO Y PRECIO')

        elif len(error_codigo_precio) == 1:

            messagebox.showerror('ERROR', f'HAZ INGRESADO INCORRECTAMENTE\nEL DATO DE {error_codigo_precio[0].upper()}')

        elif len(espacios_blancos) == 0 and codigo_producto.get() != '' and len(almacenamiento.consultar('codigo', codigo_producto.get(), False)) != 0:

            messagebox.showerror('ERROR', 'EL CÓDIGO INGRESADO\nYA EXISTE')
            codigo_duplicado = True

        if len(espacios_blancos) == 0 and len(error_codigo_precio) == 0 and codigo_duplicado == False:

            almacenamiento.agregar(nombre_producto.get(), codigo_producto.get(), inventario_producto.get(), precio_producto.get())

            nombre_producto.set('')
            codigo_producto.set('')
            inventario_producto.set('')
            precio_producto.set('')

    contenedor_inicio.pack_forget()

    if contenedor_agregar != '':

        contenedor_agregar.pack_forget()
    
    global contenedor_principal
    contenedor_principal = tkinter.Frame(ventana)
    contenedor_principal.config(bd = 4, relief = 'groove')

    encabezado_inicio = tkinter.Label(contenedor_principal, text = '¡Agregar Producto!')
    encabezado_inicio.config(bg = '#39A2DB', fg = 'white', pady = 30, font = ('Helvetica', 30), bd = 4, relief = 'groove')
    encabezado_inicio.pack(fill = tkinter.X)

    separador_inicio = tkinter.Label(contenedor_principal, text = '')
    separador_inicio.config(bg = '#E8F0F2', font = ('Helvetica', 5), bd = 4, relief = 'groove')
    separador_inicio.pack(fill = tkinter.X)

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Label(contenedor_principal, text = 'Ingresa los datos del Producto:').pack()

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Label(contenedor_principal, text = 'Nombre del Producto:').pack()
    tkinter.Entry(contenedor_principal, textvariable = nombre_producto).pack()

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Label(contenedor_principal, text = 'Código del Producto:').pack()
    tkinter.Entry(contenedor_principal, textvariable = codigo_producto).pack()

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Label(contenedor_principal, text = 'Inventario del Producto:').pack()
    tkinter.Entry(contenedor_principal, textvariable = inventario_producto).pack()

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Label(contenedor_principal, text = 'Precio del Producto:').pack()
    tkinter.Entry(contenedor_principal, textvariable = precio_producto).pack()

    # Contenedor de Espaciado:
    tkinter.Label(contenedor_principal).pack()

    tkinter.Button(contenedor_principal, text = 'Agregar Producto', command = agregar_producto).pack()

    # Contenedor de Espaciado:
    esp = tkinter.Label(contenedor_principal, text = '')
    esp.config(pady = 5)
    esp.pack()

    contenedor_principal.pack(fill = tkinter.X)

def arrancar(ventana, contenedor_agregar = '', contenedor_inicio = '', recargar = ''):

    if recargar != 'AGREGAR':

        contenido_agregar(ventana, contenedor_agregar, contenedor_inicio)
        recarga.status.set('AGREGAR')