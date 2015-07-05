from . import component
from . import utils
class LoginHeader(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "Welcome To " + utils.docmd("uname -n").rstrip()
