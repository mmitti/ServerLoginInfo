import component
import utils
class KernelVersion(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "KERNEL:" + utils.docmd("uname -r").rstrip()
