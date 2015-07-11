class Component:
    window = None
    def __init__(self, w):
        self.window = w
        return
    def update(self):
        return
    def show(self):
        return
class VoidComponent(Component):
    def __init__(self):
        return
