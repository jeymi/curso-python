import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def Imprimir_algo(btn):
    print btn
    print 'Hola Mundo'

if __name__ == '__main__':

    ventana = Gtk.Window(title = 'Example_3')
    ventana.connect('delete-event', Gtk.main_quit)
    boton_1 = Gtk.Button('Btn 1')
    boton_2 = Gtk.Button('Btn 2')
    boton_3 = Gtk.Button('Btn 3')
    boton_4 = Gtk.Button('Btn 4')
    #boton_4 = Gtk.Button('Btn 4')
    contenedor = Gtk.Grid()
    contenedor.set_column_homogeneous(True)
    contenedor.set_row_homogeneous(False)
    contenedor.attach(boton_1, 0, 0, 3, 1)
    contenedor.attach(boton_2, 1, 1, 1, 1)
    contenedor.attach(boton_3, 2, 1, 1, 1)
    contenedor.attach(boton_4, 0, 3, 1, 1)
    ventana.add(contenedor)
    ventana.add(boton_1)
    ventana.add(boton_2)
    ventana.add(boton_3)
    ventana.add(boton_4)
    ventana.show_all()

Gtk.main()