import component
import utils
class Architecture(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "ARCH:" + utils.docmd("arch").rstrip()
