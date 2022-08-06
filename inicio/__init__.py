import tkinter
from tkinter import ttk
import almacenamiento
import recarga
from tkinter import messagebox

almacenamiento.conectar(almacenamiento.id_usuario)
contenedor_principal = ''
contenedor_tabla = ''
tabla = ''

eliminacion_id = ''
eliminacion_cod = ''
eliminacion_int = ''
eliminacion_pre = ''

busqueda_id = ''
busqueda_cod = ''
busqueda_int = ''
busqueda_pre = ''

opcion_modificar = ''
id_modificar = ''
modificacion = ''


def arrancar_tabla(contenedor, ocultar_contenedor = '', consulta = [], visualizacion = False):

    consulta_vacia = False
    global tabla

    productos = ''

    if len(consulta) > 0:

        productos = almacenamiento.consultar(consulta[0], consulta[1])

        if productos == []:

            consulta_vacia = True
            messagebox.showerror('ERROR', 'ELEMENTO NO ENCONTRADO')

    else:

        productos = almacenamiento.mostrar()

    if (consulta_vacia == False and len(productos) != 0) or almacenamiento.mostrar() == []:

        if ocultar_contenedor != '':

            tabla.pack_forget()

        tabla = ttk.Treeview(contenedor, columns = ('id', 'nombre', 'codigo', 'inventario', 'precio'), show='headings')
        tabla.config(height = 16)
        tabla.heading('id', text ='Id')
        tabla.heading('nombre', text = 'Nombre')
        tabla.heading('codigo', text = 'Código')
        tabla.heading('inventario', text = 'Inventario')
        tabla.heading('precio', text = 'Precio')
        tabla.column('id', anchor = tkinter.CENTER)
        tabla.column('nombre', anchor = tkinter.CENTER)
        tabla.column('codigo', anchor = tkinter.CENTER)
        tabla.column('inventario', anchor = tkinter.CENTER)
        tabla.column('precio', anchor = tkinter.CENTER)

        for producto in productos:

            tabla.insert(parent = '', iid = producto[0], index = 'end', text = '', values = (producto[0], producto[1], producto[2], producto[3], producto[4]))

        tabla.pack(fill = tkinter.X)

        if visualizacion != False:

            visualizacion = almacenamiento.consulta_vista('id', visualizacion)

            if  len(visualizacion) > 0:

                visualizacion = visualizacion[len(visualizacion)-1][0]
                tabla.see(visualizacion)
      
def contenido_inicio(ventana, contenedor_inicio = '', contenedor_agregar = ''):

    if contenedor_inicio != '':
    
        contenedor_inicio.pack_forget()

    if contenedor_agregar != '':

        contenedor_agregar.pack_forget()

    global contenedor_principal
    contenedor_principal = tkinter.Frame(ventana)

    encabezado_inicio = tkinter.Label(contenedor_principal, text = '¡Bienvenidos a Ide5i!')
    encabezado_inicio.config(bg = '#39A2DB', fg = 'white', pady = 30, font = ('Helvetica', 30), bd = 4, relief = 'groove')
    encabezado_inicio.pack(fill = tkinter.X)

    separador_inicio = tkinter.Label(contenedor_principal, text = '')
    separador_inicio.config(bg = '#E8F0F2',font = ('Helvetica', 5), bd = 4, relief = 'groove')
    separador_inicio.pack(fill = tkinter.X)

    global contenedor_tabla
    contenedor_tabla = tkinter.Frame(contenedor_principal)
    contenedor_tabla.config(bd = 4, relief = 'groove')
    contenedor_tabla.pack(fill = tkinter.X)

    arrancar_tabla(contenedor_tabla)

    separador_inicio2 = tkinter.Label(contenedor_principal, text = '')
    separador_inicio2.config(bg = '#E8F0F2',font = ('Helvetica', 5), bd = 4, relief = 'groove')
    separador_inicio2.pack(fill = tkinter.X)

    contenedor_opciones = tkinter.Frame(contenedor_principal)

    contenedor_opciones.config(bd = 4, relief = 'groove')
    contenedor_busqueda = tkinter.Frame(contenedor_opciones)
    contenedor_eliminacion = tkinter.Frame(contenedor_opciones)

    # Opciones Eliminar:

    opcion_eliminar_id = tkinter.Frame(contenedor_eliminacion)

    label_eliminacion = tkinter.Label(opcion_eliminar_id, text = 'Eliminar fila por Id:')
    label_eliminacion.config(pady = 9)
    label_eliminacion.grid(row = 0, column = 0)

    tkinter.Label(opcion_eliminar_id, text = '').grid(row = 0, column = 1)

    global eliminacion_id
    eliminacion_id = tkinter.StringVar()
    
    tkinter.Entry(opcion_eliminar_id, textvariable = eliminacion_id).grid(row = 0, column = 2)

    # Labels de espaciado:
    tkinter.Label(opcion_eliminar_id, text = '').grid(row = 0, column = 3)
    tkinter.Label(opcion_eliminar_id, text = '').grid(row = 0, column = 4)

    tkinter.Button(opcion_eliminar_id, text = 'ELIMINAR', command = lambda: almacenamiento.eliminacion('id', eliminacion_id.get(), ventana, contenedor_tabla)).grid(row = 0, column = 5)

    opcion_eliminar_id.pack(fill = tkinter.X)

    opcion_eliminar_codigo = tkinter.Frame(contenedor_eliminacion)

    label_eliminacion2 = tkinter.Label(opcion_eliminar_codigo, text = 'Eliminar Fila por Código:')
    label_eliminacion2.config(pady = 10)
    label_eliminacion2.grid(row = 0, column = 0)

    tkinter.Label(opcion_eliminar_codigo, text = '').grid(row = 0, column = 1)

    global eliminacion_cod
    eliminacion_cod = tkinter.StringVar()

    tkinter.Entry(opcion_eliminar_codigo, textvariable = eliminacion_cod).grid(row = 0, column = 2)

    # Labels de espaciado:
    tkinter.Label(opcion_eliminar_codigo, text = '').grid(row = 0, column = 3)
    tkinter.Label(opcion_eliminar_codigo, text = '').grid(row = 0, column = 4)

    tkinter.Button(opcion_eliminar_codigo, text = 'ELIMINAR', command = lambda: almacenamiento.eliminacion('codigo', eliminacion_cod.get(), ventana, contenedor_tabla)).grid(row = 0, column = 5)

    opcion_eliminar_codigo.pack(fill = tkinter.X)

    opcion_eliminar_inventario = tkinter.Frame(contenedor_eliminacion)

    label_eliminacion2 = tkinter.Label(opcion_eliminar_inventario, text = 'Eliminar Fila o Filas por Inventario:')
    label_eliminacion2.config(pady = 10)
    label_eliminacion2.grid(row = 0, column = 0)

    tkinter.Label(opcion_eliminar_inventario, text = '').grid(row = 0, column = 1)

    global eliminacion_int
    eliminacion_int = tkinter.StringVar()

    tkinter.Entry(opcion_eliminar_inventario, textvariable = eliminacion_int).grid(row = 0, column = 2)

    # Labels de espaciado:
    tkinter.Label(opcion_eliminar_inventario, text = '').grid(row = 0, column = 3)
    tkinter.Label(opcion_eliminar_inventario, text = '').grid(row = 0, column = 4)

    tkinter.Button(opcion_eliminar_inventario, text = 'ELIMINAR', command = lambda: almacenamiento.eliminacion('inventario', eliminacion_int.get(), ventana, contenedor_tabla)).grid(row = 0, column = 5)

    opcion_eliminar_inventario.pack(fill = tkinter.X)

    opcion_eliminar_precio = tkinter.Frame(contenedor_eliminacion)

    label_eliminacion2 = tkinter.Label(opcion_eliminar_precio, text = 'Eliminar de Fila o Filas por Precio:')
    label_eliminacion2.config(pady = 10)
    label_eliminacion2.grid(row = 0, column = 0)

    tkinter.Label(opcion_eliminar_precio, text = '').grid(row = 0, column = 1)

    global eliminacion_pre
    eliminacion_pre = tkinter.StringVar()

    tkinter.Entry(opcion_eliminar_precio, textvariable = eliminacion_pre).grid(row = 0, column = 2)

    # Labels de espaciado:
    tkinter.Label(opcion_eliminar_precio, text = '').grid(row = 0, column = 3)
    tkinter.Label(opcion_eliminar_precio, text = '').grid(row = 0, column = 4)

    tkinter.Button(opcion_eliminar_precio, text = 'ELIMINAR', command = lambda: almacenamiento.eliminacion('precio', eliminacion_pre.get(), ventana, contenedor_tabla)).grid(row = 0, column = 5)

    opcion_eliminar_precio.pack(fill = tkinter.X)

    # Opciones Busqueda: 

    opcion_busqueda_id = tkinter.Frame(contenedor_busqueda)

    label_busqueda_id = tkinter.Label(opcion_busqueda_id, text = 'Busqueda por Id:')
    label_busqueda_id.config(pady = 9)
    label_busqueda_id.grid(row = 0, column = 0)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_id).grid(row = 0, column = 1)

    global busqueda_id
    busqueda_id = tkinter.StringVar()

    tkinter.Entry(opcion_busqueda_id, textvariable = busqueda_id).grid(row = 0, column = 2)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_id).grid(row = 0, column = 3)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_id).grid(row = 0, column = 4)

    tkinter.Button(opcion_busqueda_id, text = 'Buscar', command = lambda: almacenamiento.seleccionar(tabla, busqueda_id.get())).grid(row = 0, column = 5)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_id).grid(row = 0, column = 6)

    opcion_busqueda_id.pack()

    opcion_busqueda_cod = tkinter.Frame(contenedor_busqueda)

    label_busqueda_cod = tkinter.Label(opcion_busqueda_cod, text = 'Busqueda por Código:')
    label_busqueda_cod.config(pady = 10)
    label_busqueda_cod.grid(row = 0, column = 0)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_cod).grid(row = 0, column = 1)

    global busqueda_cod
    busqueda_cod = tkinter.StringVar()
    tkinter.Entry(opcion_busqueda_cod, textvariable = busqueda_cod).grid(row = 0, column = 2)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_cod).grid(row = 0, column = 3)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_cod).grid(row = 0, column = 4)

    tkinter.Button(opcion_busqueda_cod, text = 'Buscar', command = lambda: almacenamiento.seleccionar_codigo(tabla, busqueda_cod.get())).grid(row = 0, column = 5)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_cod).grid(row = 0, column = 6)

    opcion_busqueda_cod.pack()


    opcion_busqueda_int = tkinter.Frame(contenedor_busqueda)

    label_busqueda_int = tkinter.Label(opcion_busqueda_int, text = 'Busqueda por Inventario:')
    label_busqueda_int.config(pady = 10)
    label_busqueda_int.grid(row = 0, column = 0)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_int).grid(row = 0, column = 1)

    global busqueda_int
    busqueda_int = tkinter.StringVar()

    tkinter.Entry(opcion_busqueda_int, textvariable = busqueda_int).grid(row = 0, column = 2)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_int).grid(row = 0, column = 3)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_int).grid(row = 0, column = 4)

    tkinter.Button(opcion_busqueda_int, text = 'Buscar', command = lambda: arrancar_tabla(contenedor_tabla, tabla, ['inventario', busqueda_int.get()])).grid(row = 0, column = 5)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_int).grid(row = 0, column = 6)

    opcion_busqueda_int.pack()


    opcion_busqueda_pre = tkinter.Frame(contenedor_busqueda)

    label_busqueda_pre = tkinter.Label(opcion_busqueda_pre, text = 'Busqueda por Precio:')
    label_busqueda_pre.config(pady = 10)
    label_busqueda_pre.grid(row = 0, column = 0)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_pre).grid(row = 0, column = 1)

    global busqueda_pre
    busqueda_pre = tkinter.StringVar()
    tkinter.Entry(opcion_busqueda_pre, textvariable = busqueda_pre).grid(row = 0, column = 2)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_pre).grid(row = 0, column = 3)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_pre).grid(row = 0, column = 4)

    tkinter.Button(opcion_busqueda_pre, text = 'Buscar', command = lambda: arrancar_tabla(contenedor_tabla, tabla, ['precio', busqueda_pre.get()])).grid(row = 0, column = 5)

    # Label de espaciado:
    tkinter.Label(opcion_busqueda_pre).grid(row = 0, column = 6)

    opcion_busqueda_pre.pack()

    # Cambios:

    global opcion_modificar
    opcion_modificar = tkinter.StringVar()
    opcion_modificar.set(None)

    global id_modificar
    id_modificar = tkinter.StringVar()

    global modificacion
    modificacion = tkinter.StringVar()


    contenedor_cambios = tkinter.Frame(contenedor_opciones)
    label_cambios = tkinter.Label(contenedor_cambios, text = 'Modificar Valor de una Fila:')
    label_cambios.grid(row = 0, column = 0)

    contenedor_cambios_id = tkinter.Frame(contenedor_cambios)
    label_id_cambio = tkinter.Label(contenedor_cambios_id, text = 'Id de la Fila:')
    label_id_cambio.config(pady = 10, padx = 7)
    label_id_cambio.grid(row = 0, column = 0)
    tkinter.Entry(contenedor_cambios_id, textvariable = id_modificar).grid(row = 0, column = 1)
    contenedor_cambios_id.grid(row = 1, column = 0)


    contenedor_cambios_opc = tkinter.Frame(contenedor_cambios)

    tkinter.Radiobutton(

        contenedor_cambios_opc,
        text = 'Nombre',
        value = 'nombre',
        variable = opcion_modificar

    ).grid(row = 0, column = 0)

    tkinter.Radiobutton(

        contenedor_cambios_opc,
        text = 'Código',
        value = 'codigo',
        variable = opcion_modificar
    ).grid(row = 0, column = 1)

    tkinter.Radiobutton(

        contenedor_cambios_opc,
        text = 'Inventario',
        value = 'inventario',
        variable = opcion_modificar

    ).grid(row = 0, column = 2)

    tkinter.Radiobutton(

        contenedor_cambios_opc,
        text = 'Precio',
        value = 'precio',
        variable = opcion_modificar

    ).grid(row = 0, column = 3)

    contenedor_cambios_opc.grid(row = 2, column = 0)

    contenedor_cambios_rem = tkinter.Frame(contenedor_cambios)

    label_rem = tkinter.Label(contenedor_cambios_rem, text = 'Valor de Remplazo:')
    label_rem.config(pady = 10, padx = 7)
    label_rem.grid(row = 0, column = 0)

    tkinter.Entry(contenedor_cambios_rem, textvariable = modificacion).grid(row = 0, column = 1)

    contenedor_cambios_rem.grid(row = 3, column = 0)

    tkinter.Button(contenedor_cambios, text = 'Modificar', command = lambda: almacenamiento.modificar_fila(opcion_modificar.get(), modificacion.get(), id_modificar.get(), ventana, contenedor_tabla )).grid(row = 4, column = 0)


    contenedor_eliminacion.pack(side = tkinter.LEFT, anchor = tkinter.NW)
    contenedor_busqueda.pack(side = tkinter.RIGHT, anchor = tkinter.NE)
    contenedor_cambios.pack(side = tkinter.TOP)
    contenedor_opciones.pack(fill = tkinter.X)


    separador_inicio3 = tkinter.Label(contenedor_principal, text = '')
    separador_inicio3.config(bg = '#E8F0F2',font = ('Helvetica', 40), bd = 4, relief = 'groove')
    separador_inicio3.pack(fill = tkinter.X)

    contenedor_principal.pack(fill = tkinter.X)

def arrancar(ventana, contenedor_inicio = '', contenedor_agregar = '', recargar = ''):

    global contenedor_tabla
    global tabla

    if recargar == 'CONSULTA':

        recarga.datos_busqueda = []
        arrancar_tabla(contenedor_tabla, tabla)

    elif recargar != 'INICIO':

        contenido_inicio(ventana, contenedor_inicio, contenedor_agregar)
        recarga.status.set('INICIO')
        recarga.datos_busqueda = []









