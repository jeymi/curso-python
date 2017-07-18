import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,Gio,GLib

from prueba import Mi_Ventana

class CursoPythonApp(Gtk.Application):

	def __init__( self,*args, **kwargs):
		super(CursoPythonApp,self).__init__(*args,application_id = 'ni.edu.udem.cursopython.jeymi',**kwargs)
		self.window = None



	def do_activate(self):
		if not self.window:
			self.window = Mi_Ventana(application=self, title = 'ventana principal')
		self.window.show_all()
		self.window.present()
	def do_startup(self):
		Gtk.Application.do_startup
		accion_otra_ventana = Gio.SimpleAction.new('balance', None)
		accion_otra_ventana.connect('activate', self.crear_balance)
		self.add_action(accion_otra_ventana)

		builder = Gtk.Builder.new_from_file('menu.xml')
		self.set_app_menu(builder.get_object('app-menu'))
	def crear_balance(self,action,params):
		print 'una accion'

if __name__ == '__main__':
	app = CursoPythonApp()
	app.run()
