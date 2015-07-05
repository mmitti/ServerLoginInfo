import component
import utils
class KernelVersion(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "KERNEL:" + utils.docmd("uname -r").rstrip()
class Architecture(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "ARCH:" + utils.docmd("arch").rstrip()

class Distribution(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        try:
            s = utils.cat("/etc/issue").split("\n")
        except IOError:
            return ""
        return s[0]
