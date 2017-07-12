import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agragar_boton()
		self.agregar_lista()
		
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)
	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,3,1)
		self.entrada2 = Gtk.Entry()
		self.contenedor.attach(self.entrada2,3,0,1,1)
	def agragar_boton(self):
		self.boton = Gtk.Button('agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			4,
			1,
			)
		self.boton.connect('clicked',self.agregar_fila)
	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str,float)
		self.lista_activos = Gtk.TreeView(self.modelo)
  
		descripcion = Gtk.CellRendererText()
		columna_descripcion =  Gtk.TreeViewColumn('descripcion',descripcion,text=0)
		monto = Gtk.CellRendererText()
		columna_monto =  Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			1,
			1
			)

	def agregar_fila(self,btn):
		texto = self.entrada.get_text()
		num = self.entrada2.get_text()
		self.modelo.append([texto,float(num)])
if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()
Gtk.main()