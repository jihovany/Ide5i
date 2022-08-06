import tkinter
import registro
import usuarios

nombre_usuario = ''
clave = ''

def espaciado(espaciar):

	espaciado = tkinter.Label(espaciar)
	espaciado.config(bg = '#E8F0F2')
	espaciado.pack()

def arrancar(ventana, contenedor_registro = '', imagen = '', iniciada = ''):

	usuarios.conectar()
	
	menu_principal = tkinter.Menu(ventana)
	ventana.config(menu = menu_principal)

	if contenedor_registro != '':

		contenedor_registro.pack_forget()

	if iniciada != '':

		iniciada.pack_forget()


	global contenedor
	global nombre_usuario
	global clave
	nombre_usuario = tkinter.StringVar()
	clave = tkinter.StringVar()
	contenedor = tkinter.Frame(ventana)
	contenedor.config(bg = '#E8F0F2')

	for i in range(4):

		espaciado(contenedor)

	img = tkinter.Label(contenedor, image = imagen)
	img.config(bg = '#E8F0F2')
	img.pack()

	for i in range(2):

		espaciado(contenedor)

	label_usuario = tkinter.Label(contenedor, text = 'Nombre de Usuario:')
	label_usuario.config(bg = '#E8F0F2')
	label_usuario.pack()

	espaciado(contenedor)

	tkinter.Entry(contenedor, textvariable = nombre_usuario).pack()

	espaciado(contenedor)

	label_clave = tkinter.Label(contenedor, text = 'Contraseña:')
	label_clave.config(bg = '#E8F0F2')
	label_clave.pack()

	espaciado(contenedor)

	tkinter.Entry(contenedor, show = '*', textvariable = clave).pack()

	espaciado(contenedor)

	tkinter.Button(contenedor, text = 'Iniciar Sesión', command = lambda: usuarios.iniciar_sesion(nombre_usuario.get(), clave.get(), ventana, contenedor)).pack()

	espaciado(contenedor)
	espaciado(contenedor)
	espaciado(contenedor)

	label_registro = tkinter.Label(contenedor, text = '¿Aún no tienes una Cuenta?')
	label_registro.config(bg = '#E8F0F2', pady = 7)
	label_registro.pack()

	espaciado(contenedor)

	tkinter.Button(contenedor, text = 'Registrarte', command = lambda: registro.arrancar(ventana, contenedor, imagen)).pack()

	contenedor.pack()
