from . import component
from . import utils
import curses
class Loading(component.Component):
    def __init__(self, w):
        super().__init__(w)
        return
    def update(self, p = None, max = None):
        if(p == None):
            return
        width = self.window.getmaxyx()[1]
        i = (p + 1) * width / max
        i = min(i, width - 1)
        text = "\u2B1B" * int(i)
        self.window.addstr(0, 0, text)
    def show(self):
        self.window.refresh()
        return
