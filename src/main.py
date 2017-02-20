import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import pygtkcompat
import time

class EpochWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Epoch Time")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=20)
        self.add(hbox)
        
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)
        vbox_about = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox_about.set_homogeneous(False)
        
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)
        
        hbox.set_homogeneous(False)
        
        vbox = Gtk.Box()
        vbox.set_orientation(Gtk.Orientation.VERTICAL)
        vbox.set_spacing(5)
        hbox.add(vbox)
     
        global epoch_label
        current_epoch = str(int(time.time()))
        epoch_label = Gtk.Label()
        epoch_label.set_markup("<big>" + current_epoch + "</big>")
        vbox.pack_start(epoch_label, True, True, 0)
        epoch_label.set_selectable(True)

        
        button = Gtk.Button
        try:
            pb = GdkPixbuf.Pixbuf.new_from_file_at_size('../res/clock.png', 100, 100)
        except:
            pb = None
        img = Gtk.Image()
        img.set_from_pixbuf(pb)
        button = Gtk.Button(xalign=0.5, yalign=1)
        #button1.set_label(lbl)
        button.set_image(img)
        button.set_image_position(Gtk.PositionType.TOP)
        button.get_style_context().add_class("btn_article")
        button.set_always_show_image (True)
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)
        
               
        
        about = Gtk.Label()
        about.set_markup("\n\n\n" + "<small><a href=\"https://github.com/paulmadore/epoch-time-widget\" "
                         "title=\"Get the source\">source code</a>" + "\n\n" +  "copyright 2017 <a href=\"http://www.phm.link\" "
                         "title=\"About coder\">phm.link</a></small>")
        about.set_justify(Gtk.Justification.CENTER)
        
        vbox_left.pack_start(about, True, True, 0)
        


       
    def on_click_me_clicked(self, button):
        current_epoch = str(int(time.time()))
        print(current_epoch)
        epoch_label.set_text(current_epoch)




win = EpochWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()