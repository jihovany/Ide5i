import sqlite3
import registro
import inicio_sesion
import sesion_iniciada
import almacenamiento
import recarga
import tkinter
from tkinter import messagebox

conexion = ''
ejecutar = ''
id_tabla = ''

def conectar():

    global conexion
    global ejecutar

    conexion = sqlite3.connect('database.db')
    ejecutar = conexion.cursor()

    ejecutar.execute(f"""CREATE TABLE IF NOT EXISTS usuarios(

        id integer primary key autoincrement,
        nombre varchar(255),
        nombre_usuario var_char(255),
        clave var_char(255)

    );
    """)

    conexion.commit()

def registrar(nombre, usuario, clave, ventana, contenedor_registro, imagen):

    espacios_blancos = []

    if nombre == '':

        espacios_blancos.append('NOMBRE')

    if usuario == '':

        espacios_blancos.append('NOMBRE DE USUARIO')

    if clave == '':

        espacios_blancos.append('CONTRASEÑA')

    if len(espacios_blancos) == 3:

        messagebox.showerror('ERROR', 'TODOS LOS CAMPOS ESTÁN VACÍOS')

    elif len(espacios_blancos) > 1:

        texto_error = f'{espacios_blancos[0]} Y {espacios_blancos[1]}'

        messagebox.showerror('ERROR', f'{texto_error}\nESTÁN VACÍOS')

    elif len(espacios_blancos) == 1:

        messagebox.showerror('ERROR', f'{espacios_blancos[0]}\nESTÁ VACÍO')

    else:

        usuario = usuario.lower()

        if len(consulta_usuario(usuario)) == 0:
        
            ejecutar.execute(f'INSERT INTO usuarios VALUES (null, "{nombre}", "{usuario}", "{clave}");')
            conexion.commit()
            messagebox.showinfo('', 'USUARIO REGISTRADO\nCON ÉXITO')
            inicio_sesion.arrancar(ventana, contenedor_registro, imagen)

        else:

            messagebox.showerror('ERROR', 'EL NOMBRE DE USUARIO\nINGRESADO YA EXISTE')

def consulta_usuario(usuario):

    ejecutar.execute(f'SELECT * FROM usuarios WHERE nombre_usuario == "{usuario}";')
    productos = ejecutar.fetchall()

    return productos

def iniciar_sesion(nombre_usuario, clave, ventana, contenedor_inicio):

    global id_tabla

    if nombre_usuario == '' and clave == '':

        messagebox.showerror('ERROR', 'EL CAMPO DEL NOMBRE DE USUARIO Y\nLA CONTRASEÑA ESTÁN VACÍOS')

    elif nombre_usuario == '':

        messagebox.showerror('ERROR', 'EL CAMPO DEL NOMBRE DE\nUSUARIO ESTÁ VACÍO')

    elif clave == '':

        messagebox.showerror('ERROR', 'EL CAMPO DE LA CONTRASEÑA\nESTÁ VACÍO')

    else:

        nombre_usuario = nombre_usuario.lower()

        if len(consulta_usuario(nombre_usuario)) == 0:

            messagebox.showerror('ERROR', 'EL NOMBRE DE USUARIO\nINGRESADO NO ESTÁ REGISTRADO')

        else:

            if (consulta_usuario(nombre_usuario))[0][3] == clave:

                id_tabla = consulta_usuario(nombre_usuario)[0][0]
                contenedor_inicio.pack_forget()
                
                almacenamiento.conectar(id_tabla)
                sesion_iniciada.programa(ventana)

            else:

                messagebox.showerror('ERROR', 'CONTRASEÑA INCORRECTA')

