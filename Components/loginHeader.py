from . import component
from . import utils
import curses
class LoginHeader(component.Component):
    window = None
    def __init__(self, w):
        super().__init__(w)
        self.window.border(' ', ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE, ' ')
        self.window.addstr(0, 0, "Welcome To " + utils.docmd("uname -n").rstrip())
        return
    def update(self):
        return
    def show(self):
        self.window.refresh()
        return
