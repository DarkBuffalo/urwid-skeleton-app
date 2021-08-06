#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
                   ,,▄▄▄▄▄▄▄▄,,
              ▄▄▀▀`             '▀▀¥▄▄
      gP  ,▄▀'                         ▀R▄
   ╓µµ`▌▄▀-                               '▀▄
    ▐N'                                      ▀▄
   ▄         N,                                ▀
   C         C ▀▄,                              ▐
  j      ▌w  ▌    ▀N▄,          N   "▄           ▌
   ▌     ▓ "N█        '╙ⁿM∞▄,    ▀   █ *w,       ▌
   ▐⌐   █▄▄                   ⁿ▄, ▐⌐ █   ▐"═▄    ▌
    ▀   ▓ ▀                      ▀▄▐∩▌    U   ╙▄/
     ▓  ▐        ,,,,            , ▀█     ▌   ▐
      ▌ █      ▄▀▀▀▀╙▀`      ▀▀▀-╙▀▀      ▓   █
   ,∞N█ █          ╓⌐          ,⌐         █  ,▌
   ▌  ╙▌█          █▌          █▌         █╓▄▀ ╙µ
  "µ╙╗ ██                                 █▄  Å ▌
   ▀ █▀ ▀                ╒▓               ▌▌▄▌  ▌
    ▀▄            / ,          ╔ W          ¬C ▓
      ▀▄▄          '   ╙▀▀▀'     ▓        ▄,,▄▀
        └µ        , ┌,                   ▄`
          ⁿw,      ,C▌ ▐   ▌ U]        ▄▀
             '"M∞▄µ▌▐    ▐   U]  ,▄∞▀╜
                     -  `╙````
"""

import urwid
from urwid_satext.sat_widgets import Menu
import time

from command import CommandPrompt


#These palette is optional, but it's easier to use with some colors :)

const_PALETTE = [('menubar', 'light gray,bold', 'light blue'),
                 ('menubar_focus', 'light gray,bold', 'dark blue'),
                 ('menuitem', 'light gray,bold', 'light blue'),
                 ('menuitem_focus', 'light gray,bold', 'dark blue'),
                 ('status_bar', 'black', 'light gray'),
                 ]

class MenuDemo(object):

    def __init__(self):
        self._frame = urwid.Frame(urwid.Filler(urwid.Text([
             ("\n\n"
             "  ████████   ██                    ██                            ██   ██████  ██       ██\n"
             " ██░░░░░░   ░██                   ░██                           ░██  ██░░░░██░██      ░██\n"
             "░██        ██████  ██████   ██████░██        ██████  ██████     ░██ ██    ░░ ░██      ░██\n"
             "░█████████░░░██░  ░░░░░░██ ░░██░░█░██       ██░░░░██░░██░░█  ██████░██       ░██      ░██\n"
             "░░░░░░░░██  ░██    ███████  ░██ ░ ░██      ░██   ░██ ░██ ░  ██░░░██░██       ░██      ░██\n"
             "       ░██  ░██   ██░░░░██  ░██   ░██      ░██   ░██ ░██   ░██  ░██░░██    ██░██      ░██\n"
             " ████████   ░░██ ░░████████░███   ░████████░░██████ ░███   ░░██████ ░░██████ ░████████░██\n"
             "░░░░░░░░     ░░   ░░░░░░░░ ░░░    ░░░░░░░░  ░░░░░░  ░░░     ░░░░░░   ░░░░░░  ░░░░░░░░ ░░ \n"
             "StarLordCLI :: version 0.0.1                                                 ")
            ], align='center')))
        self.loop = urwid.MainLoop(self._frame, const_PALETTE, unhandled_input=self.keyHandler)
        # Creation du menu
        self._frame.set_header(self.buildMenu())

        # creation de la bar de status
        self.status_bar = urwid.AttrWrap(urwid.Text("Type help for instructions, :q to quit."), "status_bar")
        self.command_prompt = CommandPrompt(self)
        self.footer = urwid.Pile([urwid.AttrMap(self.status_bar, 'footer'), self.command_prompt])
        self._frame.set_footer(self.footer)

        # Focus sur le menu
        self._frame.set_focus('header')

    def run(self):
        self.loop.run()

    def _messageExit(self, message):
        # We print the menu data in the middle of the screen
        new_widget = urwid.Filler(urwid.Text(message, align='center'))
        self._frame.set_body(new_widget)
        self.loop.draw_screen()
        self._frame.set_focus('header')


    def menu_cb(self, menu_data):
        self._messageExit("Menu selected: %s/%s" % menu_data)

    def exit_cb(self, menu_data):
        self._messageExit("Exiting throught 'Quitter' menu item")
        time.sleep(1)
        raise urwid.ExitMainLoop()

    def buildMenu(self):
        """Construction du menu"""
        self.menu = Menu(self.loop)
        _menu1 = "Fichier"
        self.menu.addMenu(_menu1, "Help", self.menu_cb) # Adding a menu is quite easy
        self.menu.addMenu(_menu1, "Item 2", self.menu_cb) # Here the callback is always the same,
        self.menu.addMenu(_menu1, "Item 3", self.menu_cb) # but you use different ones in real life :)
        self.menu.addMenu(_menu1, "Quitter (C-x)", self.exit_cb, 'ctrl x') # You can also add a shortcut
        _menu2 = "Menu 2"
        self.menu.addMenu(_menu2, "Item 1", self.menu_cb)
        self.menu.addMenu(_menu2, "Item 2", self.menu_cb)
        self.menu.addMenu(_menu2, "Item 3", self.menu_cb)
        return self.menu

    def keyHandler(self, input):
        """We leave if user press a quit char"""
        #if input in ('esc','q','Q'):
        #    raise urwid.ExitMainLoop()
        if input == ':':
            self._frame.set_focus('footer')
            self.command_prompt.set_caption(':')
        if input == '/':
            self._frame.set_focus('footer')
            self.command_prompt.set_caption('/')
        # add change focus on tab key
        if input == 'tab':
            foc = self._frame.get_focus()
            if foc == 'header':
                self._frame.set_focus('body')
            if foc == 'body':
                self._frame.set_focus('header')
        else:
            return self.menu.checkShortcuts(input) #needed to manage shortcuts

demo = MenuDemo()
demo.run()
