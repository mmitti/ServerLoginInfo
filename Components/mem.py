import component
import utils
import math
class SwapUsage(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        meminfo = utils.cat("/proc/meminfo").rstrip().split("\n")
        swap_total = -1
        swap_free = -1

        for text in meminfo:
            tmp = text.split()
            tmp[0] = tmp[0].replace(":", "")
            if tmp[0] == "SwapTotal":
                swap_total = int(tmp[1])
            elif tmp[0] == "SwapFree":
                swap_free = int(tmp[1])

        if swap_total == -1:
            return "SWAP:N/A"
        swap_use = swap_total - swap_free
        return "SWAP:" + str( round(swap_use/1024, 2) ) + "M/" + str(round(swap_total/1024, 2)) + "M (" +str(int(swap_free * 100 /swap_total))  +"%Free)"
