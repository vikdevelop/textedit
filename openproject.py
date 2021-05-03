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
        self.set_default_size(1024, 500)
  
        # Create HeaderBar.
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Otevřít Projekt"
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
  
        button = Gtk.LinkButton("src/openproject.py")
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)
