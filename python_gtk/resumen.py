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
		self.contenedor.set.column_homogeneous(True)
		self.add(self.contenedor)
	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		set.contenedor.attach(self.entrada,0,0,1,1)
	def agragar_boton(self):
		self.boton = Gtk.Button('agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTOM,
			1,
			1
			)
	def agregar_lista(self):
		'''crear un treeview:
		1. crear el model d edatos Gtk.ListStore(type,type,...,type)
		2. crear el widget  que contiene o muestra los datos del modelo,
		treeview[<models>]
		3. definir las columnas y su contenido
			3.1. crear celda para cada columna de la fila
			los cellrenderer son widgets que sirven para mostrar contenido dentro de otros widgets dependiendo de su tipo.
			3.2. crear columnas(treeviez=wcolumn) del treeview que mostraran los datos usando cellrenderer widgets como elementos hijos.
			args: (titulo,cellrender,posicion en el modelo de la info a mostrar)
			3.3. agragar cada treeviewcolumn ak treeview widget
		'''
		self.modelo = Gtk.ListStore(str,float)
		self.lista_activos = Gtk.TreeView(self.model)

		descripcion = Gtk.CellRemdererText()
		columna_descripcion =  Gtk.TreeViewColumn('descripcion',descripcion,text=0)
		monto = Gtk.CellRemdererText()
		columna_monto =  Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_activos.append_Column(columna_descripcion)
		self.lista_activos.append_Column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTOM,
			1,
			1
			)
if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()
Gtk.main()
