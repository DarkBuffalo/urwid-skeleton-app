#!/usr/bin/python
# -*- coding: utf-8 -*-

import urwid
from urwid_satext.files_management import FileDialog
import time


#These palette is optional, but it's easier to use with some colors :)

const_PALETTE = [('title', 'black', 'light gray', 'standout,underline'),
                 ('default', 'default', 'default'),
                 ('default_focus', 'default,bold', 'default'),
                 ('directory', 'dark cyan, bold', 'default'),
                 ('directory_focus', 'dark cyan, bold', 'dark green'),
                 ('separator', 'brown', 'default'),
                 ]

def ok_cb(filename):
    """This callback is called when a file is choosen"""

    #We print the filename in the middle of the screen
    new_widget = urwid.Filler(urwid.Text(filename,align='center'))
    loop.widget = new_widget
    loop.draw_screen()
    #5 seconds pause
    time.sleep(5)
    #see you
    raise urwid.ExitMainLoop()

def cancel_cb(control):
    """This callback is called when user cancelled the dialog"""
    raise urwid.ExitMainLoop()

def test_quit(input):
    """We leave if user press 'esc'"""
    if input in ('esc',):
        raise urwid.ExitMainLoop()

fd = FileDialog(ok_cb, cancel_cb)
loop = urwid.MainLoop(fd, const_PALETTE, unhandled_input=test_quit)
loop.run()
