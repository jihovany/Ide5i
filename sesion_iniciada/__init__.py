import tkinter
import inicio
import agregar
import recarga
import inicio_sesion
import sys
from PIL import Image, ImageTk



def programa(ventana):

	recarga.status_funcion(ventana)

	# Menu:

	menu_principal = tkinter.Menu(ventana)
	ventana.config(menu = menu_principal)

	menu_principal.add_command(label = 'Inicio/Recargar', command = lambda: inicio.arrancar(ventana, inicio.contenedor_principal, agregar.contenedor_principal, recarga.status.get()))
	menu_principal.add_command(label = 'Agregar', command = lambda: agregar.arrancar(ventana, agregar.contenedor_principal ,inicio.contenedor_principal, recarga.status.get()))

	if ( sys.platform.startswith('win') ):

		ventana.iconbitmap('./ide5i.ico')

	else:

		icono = Image.open('./ide5i.png')
		icono_renderizado = ImageTk.PhotoImage(icono)
		ventana.call('wm', 'iconphoto', ventana._w, icono_renderizado)

	imagen = Image.open('./ide5i.png')
	renderizado = ImageTk.PhotoImage(imagen)

	menu_principal.add_command(label = 'Cerrar Sesión', command = lambda: inicio_sesion.arrancar(ventana, inicio.contenedor_principal, imagen = renderizado, iniciada = agregar.contenedor_principal))
	menu_principal.add_command(label = 'Salir', command = ventana.quit)



	inicio.arrancar(ventana)