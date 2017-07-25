import random
import gi
#import logging


# importar modulo que contiene clase base de actividad.
#from sugar3.activity import activity

#from sugar3.graphics.toolbarbox import ToolbarBox

# boton para toolbar
#from sugar3.activity.widgets import (

    #ActivityToolbarButton,
    #StopButton
#)

#from ppt_utils import OPCIONES

#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk, Gdk, GdkPixbuf
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#logger = logging.getLogger(__name__)

#ventanas



class continentes(Gtk.Window):



	def __init__(self, *args, **kwargs):
		super(continentes, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
  		self.agregar_contenedor()
    		self.agregar_boton()
      		self.agregar_lista()
      		self.agregar_lista2()



	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
  		self.add(self.contenedor)
		#self.set_canvas(self.contenedor)
		#self.agregar_boton
	def agregar_boton(self):
		self.boton = Gtk.Button('America')
  		self.contenedor.attach(self.boton,3,3,1,1)
		self.boton.connect('clicked',self.lista_poblacion_america)
  		self.boton2 = Gtk.Button('Europa')
  		self.contenedor.attach(self.boton2,3,3,1,1)
		self.boton.connect('clicked',self.lista_poblacion_europa)
  		#self.boton3 = Gtk.Button('Asia')
  	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str)
		self.lista_poblacion_america = Gtk.TreeView(self.modelo)
  		pais_cellrenderer = Gtk.CellRendererText()
		columna_paises =  Gtk.TreeViewColumn(
		'poblacion',
		pais_cellrenderer,
		text=0)


		self.lista_poblacion_america.append_column(columna_paises)
  		self.contenedor.attach_next_to(self.lista_poblacion_america, self.boton, Gtk.PositionType.BOTTOM, 1,1)
  	def agregar_lista2(self):
		self.modelo = Gtk.ListStore(str)
		self.lista_poblacion_europa = Gtk.TreeView(self.modelo)
  		pais_cellrenderer = Gtk.CellRendererText()
		columna_paises =  Gtk.TreeViewColumn(
		'poblacion',
		pais_cellrenderer,
		text=0)


		self.lista_poblacion_europa.append_column(columna_paises)
  		self.contenedor.attach_next_to(self.lista_poblacion_europa, self.boton, Gtk.PositionType.BOTTOM, 1,1)
  		


  	def lista_poblacion_america(self,btn=None):
       		if len(self.modelo) == 0:
       			self.modelo.append(['91 000.'])
       			self.modelo.append(['43 823 000.'])
       			self.modelo.append([' 375 000.'])
       			self.modelo.append([' 284 000.'])
       			self.modelo.append([' 382 000.'])
       			self.modelo.append([' 11 066 000.'])
       			self.modelo.append([' 207 012 000.'])
       			self.modelo.append([' 36 477 000.'])
       			self.modelo.append([' 18 286 000.'])
       			self.modelo.append([' 49 067 000.'])
       			self.modelo.append([' 4 949 000.'])
       			self.modelo.append([' 11 240 000.'])
       			self.modelo.append([' 71 000..'])
       			self.modelo.append([' 16 656 000.'])
       			self.modelo.append([' 6 551 000.'])
       			self.modelo.append([' 325 318 000.'])
       			self.modelo.append([' 104 000.'])
       			self.modelo.append([' 16 896 000.'])
       			self.modelo.append([' 746 000.'])
       			self.modelo.append([' 11 284 000.'])
       			self.modelo.append([' 8 795 000.'])
       			self.modelo.append([' 2 735 000.'])
       			self.modelo.append([' 122 916 000.'])
       			self.modelo.append([' 6 361 000.'])
       			self.modelo.append([' 3 842 000.'])
       			self.modelo.append([' 6 905 000.'])
       			self.modelo.append([' 31 660 000.'])
       			self.modelo.append([' 10 123 000.'])
       			self.modelo.append([' 46 000.'])
       			self.modelo.append([' 110 000.'])
       			self.modelo.append([' 173 000.'])
       			self.modelo.append([' 570 000.'])
       			self.modelo.append([' 1 735 000.'])
       			self.modelo.append([' 3 487 000.'])
       			self.modelo.append([' 31 236 000.'])
    def lista_poblacion_europa(self,btn=None):
    	if len(self.modelo) ==0:
    		self.modelo.append([' 2 874 000.'])
	       	self.modelo.append([' 82 605 000.'])
	       	self.modelo.append([' 79 000.'])
	       	self.modelo.append([' 2 993 000.'])
	       	self.modelo.append([' 8 787 000.'])
	       	self.modelo.append([' 9 829 000.'])
	       	self.modelo.append([' 11 359 000.'])
	       	self.modelo.append([' 9 508 000.'])
	       	self.modelo.append([' 3 424 000.'])
	       	self.modelo.append([' 7 110 000.'])
	       	self.modelo.append([' 850 000.'])
	       	self.modelo.append([' 800.'])
	       	self.modelo.append([' 4 175 000.'])
	       	self.modelo.append([' 5 753 000.'])
	       	self.modelo.append([' 5 433 000.'])
	       	self.modelo.append([' 2 066 000.'])
	       	self.modelo.append([' 46 491 000.'])
	       	self.modelo.append([' 1 316 000.'])
	       	self.modelo.append([' 5 505 000.'])
	       	self.modelo.append([' 64 765 000.'])
	       	self.modelo.append([' 3 713 000.'])
	       	self.modelo.append([' 11 548 000.'])
	       	self.modelo.append([' 9 805 000.'])
	       	self.modelo.append([' 4 809 000.'])
	       	self.modelo.append([' 336 000.'])
	       	self.modelo.append([' 60 674 000.'])
	       	self.modelo.append([' 17 926 000.'])
	       	self.modelo.append([' 1 953 000.'])
	       	self.modelo.append([' 38 000.'])
	       	self.modelo.append([' 2 851 000.'])
	       	self.modelo.append([' 590 000.'])
	       	self.modelo.append([' 2 073 000.'])
	       	self.modelo.append([' 437 000.'])
	       	self.modelo.append([' 3 569 000.'])
	       	self.modelo.append([' 39 000.'])
	       	self.modelo.append([' 622 000.'])
	       	self.modelo.append([' 5 265 000.'])
	       	self.modelo.append([' 17 095 000.'])
	       	self.modelo.append([' 38 370 000'])
	       	self.modelo.append([' 10 265 000.'])
	       	self.modelo.append([' 65 893 000.'])
	       	self.modelo.append([' 10 573 000.'])
	       	self.modelo.append([' 19 659 000.'])
	       	self.modelo.append([' 146 823 000.'])
	       	self.modelo.append([' 33 000.'])
	       	self.modelo.append([' 7 056 000.'])
	       	self.modelo.append([' 9 977 000.'])
	       	self.modelo.append([' 8 402 000.'])
	       	self.modelo.append([' 79 806 000.'])
	       	self.modelo.append([' 42 594 000.'])
       		
if __name__ == '__main__':
	ventana = continentes()
	ventana.show_all()

Gtk.main()