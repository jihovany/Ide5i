import tkinter
import inicio_sesion
import usuarios
import sys
from PIL import Image, ImageTk
from tkinter import messagebox

nombre = ''
usuario = ''
clave = ''
contenedor = ''

def registrar():

	messagebox.showinfo('MENSAJE', 'REGISTRARSE')

def arrancar(ventana, contenedor_inicio_sesion, imagen):

	global nombre
	global usuario
	global clave
	global contenedor

	nombre = tkinter.StringVar()
	usuario = tkinter.StringVar()
	clave = tkinter.StringVar()

	contenedor_inicio_sesion.pack_forget()
	contenedor = tkinter.Frame(ventana)
	contenedor.config(bg = '#E8F0F2')

	for i in range(4):

		inicio_sesion.espaciado(contenedor)

	img = tkinter.Label(contenedor, image = imagen)
	img.config(bg = '#E8F0F2')
	img.pack()

	for i in range(2):

		inicio_sesion.espaciado(contenedor)

	label_nombre = tkinter.Label(contenedor, text = 'Nombre(s):')
	label_nombre.config(bg = '#E8F0F2')
	label_nombre.pack()

	inicio_sesion.espaciado(contenedor)

	tkinter.Entry(contenedor, textvariable = nombre).pack()

	inicio_sesion.espaciado(contenedor)

	label_usuario = tkinter.Label(contenedor, text = 'Nombre de Usuario:')
	label_usuario.config(bg = '#E8F0F2')
	label_usuario.pack()

	inicio_sesion.espaciado(contenedor)

	tkinter.Entry(contenedor, textvariable = usuario).pack()

	inicio_sesion.espaciado(contenedor)

	label_clave = tkinter.Label(contenedor, text = 'Contraseña:')
	label_clave.config(bg = '#E8F0F2')
	label_clave.pack()

	inicio_sesion.espaciado(contenedor)

	tkinter.Entry(contenedor, textvariable = clave).pack()

	inicio_sesion.espaciado(contenedor)

	tkinter.Button(contenedor, text = 'Registrarme', command = lambda: usuarios.registrar(nombre.get(), usuario.get(), clave.get(), ventana, contenedor, imagen)).pack()

	inicio_sesion.espaciado(contenedor)
	tkinter.Button(contenedor, text = 'Volver', command = lambda: inicio_sesion.arrancar(ventana, contenedor, imagen = imagen)).pack()

	contenedor.pack()