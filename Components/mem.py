from . import component
from . import utils
import math
class _SwapUsage(component.Component):
    def __init__(self, w):
        super().__init__(w)

        meminfo = utils.cat("/proc/meminfo").rstrip().split("\n")
        swap_total = -1
        swap_free = 0

        for text in meminfo:
            tmp = text.split()
            tmp[0] = tmp[0].replace(":", "")
            if tmp[0] == "SwapTotal":
                swap_total = int(tmp[1])
            elif tmp[0] == "SwapFree":
                swap_free = int(tmp[1])
        text = "SWAP:"
        if swap_total == -1:
            text += "N/A"
        else:
            swap_use = swap_total - swap_free
            text += utils.addSIPrefix(swap_use * 1024)+ "/" +utils.addSIPrefix(swap_total* 1024) + " (" +str(int(swap_free * 100 /swap_total))  +"%Free)"
        self.window.addstr(3, 1, text)
        return


class _MemUsage(component.Component):
    def __init__(self, w):
        super().__init__(w)
        meminfo = utils.cat("/proc/meminfo").rstrip().split("\n")
        mem_total = -1
        mem_free = mem_buff = mem_cache = mem_slab = 0
        for text in meminfo:
            tmp = text.split()
            tmp[0] = tmp[0].replace(":", "")
            if tmp[0] == "MemTotal":
                mem_total = int(tmp[1])
            elif tmp[0] == "MemFree":
                mem_free = int(tmp[1])
            elif tmp[0] == "Buffers":
                mem_buff = int(tmp[1])
            elif tmp[0] == "Cached":
                mem_cache = int(tmp[1])
            elif tmp[0] == "Slab":
                mem_slab = int(tmp[1])
        text = "MEM:"
        if mem_total == -1:
            text += "N/A"
        else:
            mem_actual_free = mem_free + mem_buff + mem_cache + mem_slab
            mem_use = mem_total - mem_actual_free
            text += utils.addSIPrefix(mem_use * 1024)+ "/" +utils.addSIPrefix(mem_total* 1024) + " ("+str(int(mem_actual_free*100/mem_total))+"%Free)"

        w.addstr(2, 1, text)
        return
class MemInfo(component.Component):
    mem = None
    swap = None
    def __init__(self, w):
        super().__init__(w)
        utils.setBorder(w)
        self.swap = _SwapUsage(w)
        self.mem = _MemUsage(w)
        text = "MEM"
        width = self.window.getmaxyx()[1]
        self.window.addstr(1, int((width-utils.mlen(text))/2) -1 , text)
        return

    def show(self):
        self.window.refresh();
        return
