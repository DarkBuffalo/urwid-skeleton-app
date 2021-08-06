#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid
from urwid_satext.sat_widgets import Menu
import time


#These palette is optional, but it's easier to use with some colors :)

const_PALETTE = [('menubar', 'light gray,bold', 'dark red'),
                 ('menubar_focus', 'light gray,bold', 'dark green'),
                 ('menuitem', 'light gray,bold', 'dark red'),
                 ('menuitem_focus', 'light gray,bold', 'dark green'),
                 ]

class MenuDemo(object):

    def __init__(self):
        _frame = urwid.Frame(urwid.Filler(urwid.Text('Menu demo', align='center')))
        self.loop = urwid.MainLoop(_frame, const_PALETTE, unhandled_input=self.keyHandler)
        _frame.set_header(self.buildMenu())
        _frame.set_focus('header')

    def run(self):
        self.loop.run()

    def _messageExit(self, message):
        #We print the menu data in the middle of the screen
        new_widget = urwid.Filler(urwid.Text(message, align='center'))
        self.loop.widget = new_widget
        self.loop.draw_screen()
        #5 seconds pause
        time.sleep(5)
        #see you
        raise urwid.ExitMainLoop()

    def menu_cb(self, menu_data):
        self._messageExit("Menu selected: %s/%s" % menu_data)

    def exit_cb(self, menu_data):
        self._messageExit("Exiting throught 'Exit' menu item")

    def buildMenu(self):
        self.menu = Menu(self.loop)
        _menu1 = "Menu 1"
        self.menu.addMenu(_menu1, "Item 1", self.menu_cb) #Adding a menu is quite easy
        self.menu.addMenu(_menu1, "Item 2", self.menu_cb) #Here the callback is always the same,
        self.menu.addMenu(_menu1, "Item 3", self.menu_cb) #but you use different ones in real life :)
        self.menu.addMenu(_menu1, "Exit (C-x)", self.exit_cb, 'ctrl x') #You can also add a shortcut
        _menu2 = "Menu 2"
        self.menu.addMenu(_menu2, "Item 1", self.menu_cb)
        self.menu.addMenu(_menu2, "Item 2", self.menu_cb)
        self.menu.addMenu(_menu2, "Item 3", self.menu_cb)
        return self.menu

    def keyHandler(self, input):
        """We leave if user press a quit char"""
        if input in ('esc','q','Q'):
            raise urwid.ExitMainLoop()
        else:
            return self.menu.checkShortcuts(input) #needed to manage shortcuts

demo = MenuDemo()
demo.run()
