import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.ApplicationWindow):
	def __init__(self, *args, **kwargs):
		
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		#self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
		self.agragar_boton()
		self.agregar_lista()
		self.agregar_pasivo()
		self.agregar_pasivo1()
	

		
		
		
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)
	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,1,1)
		self.entrada2 = Gtk.Entry()
		self.contenedor.attach(self.entrada2,1,0,1,1)
	
		

	def agregar_pasivo1(self):
		self.entrada4 = Gtk.Entry()
		self.contenedor.attach(self.entrada4,0,1,1,1)
		self.entrada3 = Gtk.Entry()
		self.contenedor.attach(self.entrada3,1,1,1,1)

	def agragar_boton(self):
		self.boton = Gtk.Button('activo')
		self.contenedor.attach(self.boton,0,2,2,1)
		self.boton.connect('clicked',self.agregar_fila)
		self.boton2 = Gtk.Button('pasivo')
		self.contenedor.attach(self.boton2,0,3,2,1)
		self.boton2.connect('clicked',self.agregar_fila2)
		self.boton3 = Gtk.Button('total')
	 


		

	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str,float)
		self.lista_activos = Gtk.TreeView(self.modelo)
  
		descripcion = Gtk.CellRendererText()
		columna_descripcion =  Gtk.TreeViewColumn('descripcion',descripcion,text=0)
		monto = Gtk.CellRendererText()
		columna_monto =  Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)
		self.contenedor.attach_next_to(self.lista_activos,self.boton2,Gtk.PositionType.BOTTOM,2,2)
		

	def agregar_pasivo(self):
		self.modelo2 = Gtk.ListStore(str,float)
		self.lista_pasivos = Gtk.TreeView(self.modelo2)
  
		descripcion = Gtk.CellRendererText()
		columna_descripcion =  Gtk.TreeViewColumn('descripcion',descripcion,text=0)
		monto = Gtk.CellRendererText()
		columna_monto =  Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_pasivos.append_column(columna_descripcion)
		self.lista_pasivos.append_column(columna_monto)
		self.contenedor.attach_next_to(self.lista_pasivos,self.lista_activos,Gtk.PositionType.BOTTOM,2,2)
 

	def agregar_fila(self,btn):
		texto = self.entrada.get_text()
		num = self.entrada2.get_text()
		self.modelo.append([texto,float(num)])

	def agregar_fila2(self,btn):
		num2 = self.entrada3.get_text()
		texto2 = self.entrada4.get_text()
		self.modelo2.append([texto2,float(num2)])
	def agregar_fila3(self,btn):
		total = num+num2
		self.modelo3.append([total])


if __name__ == '__main__':
	ventana = Mi_Ventana()
	ventana.show_all()
	Gtk.main()