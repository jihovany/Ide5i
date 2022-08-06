import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import inicio
import inicio_sesion
import agregar
import recarga
import sys

ventana = tkinter.Tk()
ventana.config(bg = '#E8F0F2', bd = 5, relief = 'groove')
ventana.minsize(700, 700)
ventana.title('Ide5i - Sistema de Inventario')

# Icono para Windows o GNU/Linux:

if ( sys.platform.startswith('win') ):

	ventana.iconbitmap('./ide5i.ico')

else:

	icono = Image.open('./ide5i.png')
	icono_renderizado = ImageTk.PhotoImage(icono)
	ventana.call('wm', 'iconphoto', ventana._w, icono_renderizado)

recarga.status_funcion(ventana)

imagen = Image.open('./ide5i.png')
renderizado = ImageTk.PhotoImage(imagen)

inicio_sesion.arrancar(ventana, imagen = renderizado)

ventana.mainloop()

