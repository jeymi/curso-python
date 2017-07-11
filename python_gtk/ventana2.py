import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(btn):
	print btn 
	print 'HOLA MUNDO'

if __name__ == '__main__':

	ventana = Gtk.Window(title='Ejemplo 1')
	ventana.connect('delete-event', Gtk.main_quit)
	boton = Gtk.Button('Btn 1')

	boton.connect('clicked', imprimir_algo)
	boton2 = Gtk.Button('Btn 2')


	contenedor = Gtk.VBox()
	#contenedor.set_rows
	contenedor.pack_start(boton, False, True , 0)
	contenedor.pack_end(boton2, False, True , 0)
	ventana.add(contenedor)
	ventana.add(boton)
	ventana.show_all()

Gtk.main()