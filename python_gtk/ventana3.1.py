import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		Gtk.Window.__init__(self,title='ventana')
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500, 300)
		self.connect('delete-event', Gtk.main_quit)

        self.agregar_boton()
        self.agregar_txt()
        self.agregar_label()
        self.btnsalir()

        #self.agregar_contenedor()
        self.box = Gtk.VBox()
        self.box.pack_start(self.texto, True, True , 0)
        self.box.pack_start(self.boton, True, True , 0)
        self.box.pack_start(self.label1, True, True , 0)
        self.box.pack_start(self.btnsalir, True, True , 0)


        self.add(self.box)

	'''def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		#self.agregar_boton()'''
	def imprimir(self,btn):
		imprimir = self.texto.get_text()
		self.label1.set_text(imprimir)
	def agregar_boton(self):
		self.boton=Gtk.Button('juju')
		self.boton.connect('clicked',self.imprimir)
	def agregar_label(self):
		self.label1 = Gtk.label('aceptar valor')
	def agregar_txt(self):
		self.texto = Gtk.Entry()
	def btnsalir(self):
		self.btnsalir = Gtk.Button('salir')
		self.btnsalir.connect('clicked',Gtk.main_quit)

	
if __name__ == '__main__':
	a=MiVentana()
	a.show_all()
	Gtk.main()