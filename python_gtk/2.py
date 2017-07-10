import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#obtener el texto de input
entrada = Gtk.Entry()
entrada.get_text()

#agragar el texto al label
etiqueta = Gtk.Label()
etiqueta.set_markup('texto a agregar')                                                   