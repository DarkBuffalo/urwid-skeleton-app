# -*- coding: utf-8 -*-

import urwid
import socket


class CommandPrompt(urwid.Edit):
    """
    Ligne de commande dans le style de l'application Mutt
    """

    def __init__(self, parent):
        urwid.Edit.__init__(self, '')
        self.history = []
        self.history_offset = 0
        self.parent = parent

    def clear(self):
        self.set_caption('')
        self.set_edit_text('')

    def keypress(self, size, key):
        if key == 'backspace':
            if self.edit_text == '':
                self.set_caption('')
                self.parent.main_loop.draw_screen()
                self.parent.context.set_focus('body')
            else:
                return urwid.Edit.keypress(self, size, key)
        
        #### QUAND ON APPUI SUR ENTRE
        elif key == 'enter' and not self.get_edit_text() == '':
            
            ####SI LA COMMANDE COMMENCE PAR /
            if self.caption == '/':
                pattern = self.get_edit_text()
                self.clear()
                self.parent.main_frame.search(pattern)
                return
            command = self.get_edit_text()

            # add command to history
            self.history.append(command)
            self.history_offset = 0

            command = command.split(' ', 1)

            if command[0] in ('menu', 'm'):
                try:
                    self.clear()
                    query = command[1]
                    if query == 'bc':
                        self.parent.status_bar.set_text(' Searching for: "' + query + '"')

                    else:
                        self.parent.status_bar.set_text(' No results found for: "' + query + '"')
                    self.parent._frame.set_focus('body')
                except IndexError:
                    self.parent.status_bar.set_text(' Precisez votre demande')
                    self.parent.main_loop.draw_screen()
                    self.parent._frame.set_focus('body')
                except socket.gaierror:
                    self.parent.status_bar.set_text(' Vous n\'avez probablement pas d\'internet')
                    self.parent._frame.set_focus('body')

            elif command[0] in('help','h','aide'):
                self.clear() #on vide la bar de commande
                self.parent.status_bar.set_text(' help... ') # on affiche da,s la status_bar
                self.parent._frame.set_focus('body')
                
            elif command[0] == 'print':
                self.clear() #on vide la bar de commande
                self.parent.status_bar.set_text(' print... ') # on affiche da,s la status_bar
                self.parent._frame.set_focus('body')

            elif command[0] == 'del':
                self.clear() #on vide la bar de commande
                self.parent.status_bar.set_text(' Deleted ') # on affiche da,s la status_bar
                self.parent._frame.set_focus('body') #on met le foccus sur le main
            
            elif command[0] in ('quit', 'q'):
                raise urwid.ExitMainLoop()
            
            else:
                self.parent.status_bar.set_text(' Erreur: Il n\'y a pas de commande "' + command[0] + '"')
                self.clear()
                self.parent._frame.set_focus('body') #on met le foccus sur le main
                #pass

        elif key in ('esc', 'ctrl x'):
            self.parent._frame.set_focus('body')
            self.history_offset = 0
            self.clear()
        elif key in ('ctrl p', 'up'):
            if self.get_edit_text() not in self.history:
                self.current_command = self.get_edit_text()
            try:
                self.history_offset -= 1
                command = self.history[self.history_offset]
                self.set_edit_text(command)
                self.set_edit_pos(len(command))
            except IndexError:
                self.history_offset += 1
        elif key in ('ctrl n', 'down'):
            if self.get_edit_text() not in self.history:
                self.current_command = self.get_edit_text()
            try:
                self.history_offset += 1
                if self.history_offset == 0:
                    command = self.current_command
                elif self.history_offset < 0:
                    command = self.history[self.history_offset]
                else:
                    raise IndexError
                self.set_edit_text(command)
                self.set_edit_pos(len(command))
            except IndexError:
                self.history_offset -= 1
        else:
            return urwid.Edit.keypress(self, size, key)