#!/usr/bin/env python3
# coding: utf8 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class CounterApp():
    def __init__(self):
        self.w = Gtk.Window(title="Minutnik")
        self.w.resize(800,400)

        vbox = Gtk.VBox(spacing=2)
        self.w.add(vbox)

        self.label = Gtk.Label("")   #I create new label, where will be shown the remaining time.
        vbox.pack_start(self.label, True, True, 0)

        hbox = Gtk.HBox()
        vbox.pack_start(hbox, True, True, 0)

        #now I create buttons for some ingredients, which I want to cook. For every one there is separate
        #function for counting down proper time
        jajko_twardo = Gtk.Button("Jajko na twardo") 
        jajko_twardo.connect("clicked", self.jajko_twardo_clicked)
        hbox.pack_start(jajko_twardo, True, True, 0)

        jajko_miekko = Gtk.Button("Jajko na miękko")
        jajko_miekko.connect("clicked", self.jajko_miekko_clicked)
        hbox.pack_start(jajko_miekko, True, True, 0)

        ryz = Gtk.Button("Ryz")
        ryz.connect("clicked", self.ryz_clicked)
        hbox.pack_start(ryz, True, True, 0) 

        hbox = Gtk.HBox()
        vbox.pack_start(hbox, True, True, 0)    

        makaron = Gtk.Button("Makaron")
        makaron.connect("clicked", self.makaron_clicked)
        hbox.pack_start(makaron, True, True, 0)

        ziemniaki = Gtk.Button("Ziemniaki")
        ziemniaki.connect("clicked", self.ziemniaki_clicked)
        hbox.pack_start(ziemniaki, True, True, 0)

        brokul = Gtk.Button("Brokuł")
        brokul.connect("clicked", self.brokul_clicked)
        hbox.pack_start(brokul, True, True, 0)  

        kasza = Gtk.Button("Kasza")
        kasza.connect("clicked", self.kasza_clicked)
        hbox.pack_start(kasza, True, True, 0)

        budyn = Gtk.Button("Budyń")
        budyn.connect("clicked", self.budyn_clicked)
        hbox.pack_start(budyn, True, True, 0)

        hbox = Gtk.HBox()
        vbox.pack_start(hbox, True, True, 0)

        zamknij = Gtk.Button("Zamknij")
        zamknij.connect("clicked", self.zamknij_clicked)
        hbox.pack_start(zamknij, True, True, 0)

        self.w.show_all()

    def jajko_twardo_clicked(self, counter):
        counter = 480
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 480-counter)
            counter -= 1

    def jajko_miekko_clicked(self, counter):
        counter = 180
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 180-counter)
            counter -= 1

    def ryz_clicked(self, counter):
        counter = 780
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 780-counter)
            counter -= 1

    def makaron_clicked(self, counter):
        counter = 480
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 480-counter)
            counter -= 1

    def ziemniaki_clicked(self, counter):
        counter = 1200
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 1200-counter)
            counter -= 1

    def brokul_clicked(self, counter):
        counter = 300
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 300-counter)
            counter -= 1

    def kasza_clicked(self, counter):
        counter = 900
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 900-counter)
            counter -= 1

    def budyn_clicked(self, counter):
        counter = 120
        while counter >= 0:
            GObject.timeout_add(counter * 1000, self.countdown_function_method1, 120-counter)
            counter -= 1

    def countdown_function_method1(self, counter):
        if counter > 0:
            self.label.set_text("Pozostało: " + str(counter))
        else:
            self.label.set_text("Gotowe!")

    def zamknij_clicked(self, counter):
        Gtk.main_quit()

if __name__ == "__main__":
    app = CounterApp()
    Gtk.main()