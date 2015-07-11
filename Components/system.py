from . import component
from . import utils
class _KernelVersion(component.Component):
    def __init__(self, w):
        super().__init__(w)
        text = "KERNEL:" + utils.docmd("uname -r").rstrip()
        width = self.window.getmaxyx()[1]
        self.window.addnstr(2, 1, text, width -2 )
        return
    def show(self):
        return
class _Architecture(component.Component):
    def __init__(self, w):
        super().__init__(w)
        width = self.window.getmaxyx()[1]
        text = " ARCH:" + utils.docmd("arch").rstrip()
        self.window.addstr(1, width - utils.mlen(text) - 1 , text)
        return

class _Distribution(component.Component):
    def __init__(self, w):
        super().__init__(w)
        try:
            text = utils.cat("/etc/issue").split("\n")[0].rstrip()
            width = self.window.getmaxyx()[1]
            self.window.addnstr(1, 1, text, width -2 )
        except IOError:
            self.window.addstr(1, 1, "Distribution:N/A")
        return
class System(component.Component):
    kernel = None
    arch = None
    dist = None
    def __init__(self, w):
        super().__init__(w)
        utils.setBorder(w)
        kener = _KernelVersion(w)
        dist = _Distribution(w)
        arch = _Architecture(w)
        return

    def show(self):
        self.window.refresh()
        return
