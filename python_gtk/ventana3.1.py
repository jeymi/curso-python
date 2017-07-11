import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_boton()
		self.agregar_texto()
		self.agregar_label()
		self.agregar_salida()
		self.contenedor()

	def Imprimir(self, btn):
		impreso = self.texto.get_text()
		self.label_1.set_text(impreso)

	def agregar_boton(self):	
		self.btn_1 = Gtk.Button('Resaltar texto escrito')
		self.btn_1.connect('clicked', self.Imprimir)

	def agregar_texto(self):	
		self.texto = Gtk.Entry()

	def agregar_label(self):	
		self.label_1 = Gtk.Label('Mostrar el texto')

	def agregar_salida(self):	
		self.btnexit = Gtk.Button('Finalizar')
		self.btnexit.connect('clicked', Gtk.main_quit)

	def contenedor(self):	
		self.box = Gtk.VBox()
		self.box.pack_start(self.texto, True, False, 0)
		self.box.pack_start(self.btn_1, True, False, 0)
		self.box.pack_start(self.label_1, True, False, 0)
		self.box.pack_start(self.btnexit, True, False, 0)
		self.add(self.box)

if __name__ == '__main__':			
	ventana = Mi_Ventana()
	ventana.show_all()
Gtk.main()