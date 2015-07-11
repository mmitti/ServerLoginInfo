from . import component
import os
from . import utils
class DiskUsage(component.Component):
    def __init__(self, w):
        super().__init__(w)
        utils.setBorder(w)
        text = "FILE SYSTEM/USAGE"
        width = self.window.getmaxyx()[1]
        self.window.addstr(1, int((width-utils.mlen(text))/2) -1 , text)
        text = ""
        i = 2
        for v in self._disks:
            self.window.addstr(i, 1, self.getUsage(v[0], v[1]))
            i = i + 1

        return
    def getUsage(self, path, label):
        try:
            s = os.statvfs(path)
        except OSError:
            return label + ":N/A"
        #avail = s.f_bsize * s.f_bavail
        total = s.f_bsize * s.f_blocks
        free = s.f_bsize * s.f_bfree
        used = total - free
        return label + ":"+str(round(used*100/total, 2))+"%"
    _disks = (("/", "ROOT"), ("/mnt/data", "DATA"), ("/mnt/dlna", "DLNA"))
    def show(self):
        self.window.refresh()
