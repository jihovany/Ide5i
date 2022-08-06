import sqlite3
import inicio
from tkinter import messagebox
import recarga

conexion = ''
ejecutar = ''
id_usuario = ''

def conectar(id_user):

    global conexion
    global ejecutar
    global id_usuario
    id_usuario = id_user

    conexion = sqlite3.connect('database.db')
    ejecutar = conexion.cursor()

    ejecutar.execute(f"""CREATE TABLE IF NOT EXISTS productos_{id_usuario}(

        id int,
        nombre varchar(255),
        codigo varchar(255),
        inventario int,
        precio int

    );
    """)

    conexion.commit()

def agregar(nombre, codigo, inventario, precio):

    ejecutar.execute(f'SELECT * FROM productos_{id_usuario}')
    productos = ejecutar.fetchall()

    if len(productos) == 0:

        ejecutar.execute(f'INSERT INTO productos_{id_usuario} VALUES ("1", "{nombre}", "{codigo}", "{inventario}", "{precio}");')

    else:

        indice_final = (productos[len(productos)-1][0]+1)
        ejecutar.execute(f'INSERT INTO productos_{id_usuario} VALUES ("{indice_final}", "{nombre}", "{codigo}", "{inventario}", "{precio}");')

    conexion.commit()

def mostrar():

    ejecutar.execute(f'SELECT * FROM productos_{id_usuario}')
    productos = ejecutar.fetchall()
    
    return productos

def eliminacion(columna, ubicacion, ventana, contenedor_inicio):

    if ubicacion == '':

        messagebox.showerror('ERROR', 'NO HAZ INGRESADO NADA')

    else:

        ejecutar.execute(f'SELECT * FROM productos_{id_usuario} WHERE {columna} = "{ubicacion}";')
        productos = ejecutar.fetchall()

        if productos == []:

            messagebox.showerror('ERROR', 'ERROR ELEMENTO NO ENCONTRADO')

        else:

            id_producto = productos[len(productos)-1][0]
            ejecutar.execute(f'DELETE FROM productos_{id_usuario} WHERE {columna} = "{ubicacion}";')

            if recarga.datos_busqueda != [] and len(consultar(recarga.datos_busqueda[0], recarga.datos_busqueda[1])) == 0:

                recarga.datos_busqueda = []

            i = 0

            while len(productos) != 0:

                ejecutar.execute(f'UPDATE productos_{id_usuario} SET id = id-1 WHERE id > {productos[0][0]-i};')
                productos.pop(0)
                i += 1

            conexion.commit()

            inicio.eliminacion_id.set('')
            inicio.eliminacion_cod.set('')
            inicio.eliminacion_int.set('')
            inicio.eliminacion_pre.set('')
            inicio.arrancar_tabla(contenedor_inicio, inicio.tabla, recarga.datos_busqueda, id_producto)

def consultar(columna, condicion, consulta_inicio = True):

    productos = ''

    if condicion == '':

        messagebox.showerror('ERROR','NO HAZ INGRESADO NADA')

    else:

        ejecutar.execute(f'SELECT * FROM productos_{id_usuario} WHERE {columna} = "{condicion}";')
        productos = ejecutar.fetchall()

        if consulta_inicio:

            recarga.status.set('CONSULTA')
            recarga.datos_busqueda = [columna, condicion]

        inicio.busqueda_id.set('')
        inicio.busqueda_cod.set('')
        inicio.busqueda_int.set('')
        inicio.busqueda_pre.set('')

    return productos

def seleccionar(tabla, busqueda):

    inicio.busqueda_id.set('')
    inicio.busqueda_cod.set('')
    inicio.busqueda_int.set('')
    inicio.busqueda_pre.set('')

    try:

        if busqueda == '':

            messagebox.showerror('ERROR', 'NO HAZ INGRESADO NADA')

        else:

            inicio.tabla.see(int(busqueda))
            inicio.tabla.selection_set(int(busqueda))

    except:

        messagebox.showerror('ERROR', 'NO EXISTE DICHO ELEMENTO EN LA TABLA')

def seleccionar_codigo(tabla, condicion):

    if condicion == '':

        messagebox.showerror('ERROR', 'NO HAZ INGRESADO NADA')

    else:

        resultados = consultar('codigo', condicion)

        if len(resultados) != 0:

            for resultado in resultados:

                inicio.tabla.see(resultado[0])
                inicio.tabla.selection_set(resultado[0])     
        else:

            messagebox.showerror('ERROR', 'NO EXISTE DICHO ELEMENTO EN LA TABLA')

def modificar_fila(columna, modificacion, id_fila, ventana, contenedor_inicio):

    espacios_blancos = []
    error_id_modificacion = []
    codigo_duplicado = False
    id_fuera_rango = False

    if id_fila == '':

        espacios_blancos.append('Id de la Fila')

    if columna == 'None':

        espacios_blancos.append('Columna ha Modificar')

    if modificacion == '':

        espacios_blancos.append('Modificación')

    if len(espacios_blancos) == 3:

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

            float(id_fila)

        except:

            error_id_modificacion.append('id')

        if consultar('id', id_fila, False) == []:
     
            id_fuera_rango = True
        
        if columna != 'nombre' and columna != 'codigo':

            try:

                float(modificacion)

            except:

                error_id_modificacion.append('modificacion')

    if len(error_id_modificacion) == 2:

        messagebox.showerror('ERROR', 'HAZ INGRESADO DATOS INCORRECTOS\nEN EL ID DE LA FILA Y\nEL CAMPO A MODIFICAR')

    elif len(error_id_modificacion) == 1:

        messagebox.showerror('ERROR', f'HAZ INGRESADO INCORRECTAMENTE\nEL DATO DE {error_id_modificacion[0].upper()}')

    elif id_fuera_rango:

        messagebox.showerror('ERROR', 'El ID INGRESADO NO\nEXISTE DENTRO DE\nLA TABLA')

    elif len(espacios_blancos) == 0 and columna == 'codigo' and len(consultar(columna, modificacion, False)) != 0:

        messagebox.showerror('ERROR', 'EL CÓDIGO INGRESADO\nYA EXISTE')
        codigo_duplicado = True

    if len(espacios_blancos) == 0 and len(error_id_modificacion) == 0 and codigo_duplicado == False and id_fuera_rango == False:

        ejecutar.execute(f'UPDATE productos_{id_usuario} SET {columna} = "{modificacion}" WHERE id = {id_fila};')
        conexion.commit()

        inicio.opcion_modificar.set(None)
        inicio.id_modificar.set('')
        inicio.modificacion.set('')

        inicio.arrancar_tabla(contenedor_inicio, inicio.tabla, recarga.datos_busqueda)

        inicio.tabla.see(int(id_fila))
        inicio.tabla.selection_set(int(id_fila))    

def consulta_vista(columna, condicion):

    ejecutar.execute(f'SELECT * FROM productos_{id_usuario} WHERE {columna} <= "{condicion}";')
    productos = ejecutar.fetchall()

    if len(productos) == 0:

        productos = False

    return productos







