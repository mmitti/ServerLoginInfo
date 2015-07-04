import component
import utils
class Date(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "DATE:" + utils.docmd("date").rstrip()
