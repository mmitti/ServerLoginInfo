from . import component
import os
from . import utils
class DiskUsage(component.Component):
    def __init__(self):
        component.Component.__init__(self)
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
        return label + ":"+str(used*100/total)+"%"
    _disks = (("/", "ROOT"), ("/mnt/data", "DATA"), ("/mnt/dlna", "DLNA"))
    def show(self):
        ret = "FILE SYSTEM: "
        for v in self._disks:
            ret += self.getUsage(v[0], v[1]) + " "
        return ret
