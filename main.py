# Soubor main.py
#
# Copyright 2021 vikdev
#
# Tento program je svobodný software: můžete jej dále šířit a nebo upravovat
#  za podmínek licence GNU General Public License zveřejněné uživatelem
# Free Software Foundation, buď verze 3 licence, nebo
# (dle vašeho uvážení) jakákoli novější verze.
#
# Tento program je distribuován v naději, že bude užitečný,
# ale BEZ JAKÉKOLI ZÁRUKY; bez dokonce předpokládané záruky
# PRODEJNOST nebo VHODNOST PRO KONKRÉTNÍ ÚČEL. Viz
# GNU General Public License pro více informací.
#
# Měli jste obdržet kopii GNU General Public License
# spolu s tímto programem. Pokud ne, viz <http://www.gnu.org/licenses/>.


import sys
import gi
# Since a system can have multiple versions
# of GTK + installed, we want to make 
# sure that we are importing GTK + 3.
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
  
  
class HeaderBarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title ="textedit")
        self.set_border_width(10)
        self.set_default_size(700, 1200)
  
        # Create HeaderBar.
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "TextEdit"
        self.set_titlebar(hb)
          
        # Create Button
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name ="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        hb.pack_end(button)
        
        # Create Box
        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button("Otevřít projekt",("OpenProjectWindow"))
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)
        
        hb.pack_start(box)
        self.add(Gtk.TextView())


  
win = HeaderBarWindow()
win.connect("destroy", Gtk.main_quit)
# Display the window.
win.show_all()
# Start the GTK + processing loop
Gtk.main()
class DialogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Opravdu chcete změny zahodit?")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Zrušit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Ponechat")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Zahodit")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print('"Click me" button was clicked')

    def on_open_clicked(self, button):
        print('"Open" button was clicked')

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = DialogWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
class OpenProjectWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Otevřít Projekt")
