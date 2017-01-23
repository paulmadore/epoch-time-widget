import gi
import pygtkcompat
import time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    """defines the main window"""

    def __init__(self, *args, **kwargs):
        pass
        
    def on_window_main_destroy(self, *args):
        Gtk.main_quit(*args)
        
    def on_get_epoch_clicked(self, button):
        builder = Gtk.Builder()
        builder.add_from_file("../glade/window_main_2.glade")
        label = builder.get_object('show_epoch')
        current_epoch = str(int(time.time()))
        label.set_selectable(True)
        label.set_css_name('epoch_time_output')
        print(current_epoch)
        label.set_text(current_epoch)

    def operate(object):
        builder = Gtk.Builder()
        builder.add_from_file("../glade/window_main_2.glade")
        window = builder.get_object("window_main")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('epoch.css')
        builder.connect_signals(MainWindow())
        window.show_all()
        Gtk.main()

if __name__ == '__main__':
    MainWindow().operate()
    
