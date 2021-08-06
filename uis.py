import urwid

class UI(object):
    
    @staticmethod
    def help():
        return {
            'content': urwid.Text([
                ('underline', "\nBasic Commands\n\n"),
                ('Chancli utilizes the official 4chan API, which can be found at https://github.com/4chan/4chan-API.\n\n'),
                ('highlight', "listboards"), " - list available boards aside their code\n",
                ('highlight', "open <id>"), " - open a thread from the current window, specified by its index\n",
                ('highlight', "board <code>"), " - display the first page (ex: board g)\n",
                ('highlight', "board <code> <page>"), " - display the nth page starting from 1\n",
                ('highlight', "thread <board> <id>"), " - open a specific thread\n",
                ('highlight', "archive <code>"), " - display archived threads from a board\n\n",
                ('highlight', "help"), " - show this page\n",
                ('highlight', "license"), " - display the license page\n",
                ('highlight', "exit/quit/q"), " - exit the application"
                ]),
            'status': "Help page"
        }