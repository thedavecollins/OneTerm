#!/usr/bin/env python
import sys
import pango
import gtk
import vte

class OneTerm(gtk.Window):

    def __init__(self):
        super(OneTerm, self).__init__()

        self.set_title("OneTerm")
        self.connect("destroy", self.on_destroy)

        font = pango.FontDescription()
        font.set_family("Monospace")
        # font size
        font.set_size(14 * pango.SCALE)
        font.set_weight(pango.WEIGHT_NORMAL)
        font.set_stretch(pango.STRETCH_NORMAL)

        terminal = vte.Terminal()
        terminal.connect ("child-exited", lambda term: gtk.main_quit())
        terminal.set_scrollback_lines(5000)
        terminal.set_encoding("UTF-8")
        terminal.set_font_full(font, True)

        terminal.fork_command("bash")

        self.fullscreen()                                                                                                                               
        color = gtk.gdk.Color(0,0,0)
        self.modify_bg(gtk.STATE_NORMAL, color)
        self.f  = gtk.Fixed()
        self.add(self.f)
        self.f.put(terminal, 10, 10)
        self.terminal = terminal
        self.connect('window-state-event', self.on_window_state_event)                                                                                        
        self.show_all()

    def on_window_state_event(self, widget, event):
        self.terminal.set_size_request(800,self.get_size()[1] - 10)
        
        self.f.move(self.terminal, (self.get_size()[0] - 800 )/2, 10)

    def on_destroy(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    win = OneTerm()
    gtk.main()
