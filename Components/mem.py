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
        swap_free = 0

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

class MemUsage(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
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
        if mem_total == -1:
            return "MEM:N/A"
        mem_actual_free = mem_free + mem_buff + mem_cache + mem_slab
        mem_use = mem_total - mem_actual_free
        return "MEM:" + str( round(mem_use/1024, 2) ) + "M/" + str(round(mem_total/1024, 2)) + "M ("+str(int(mem_actual_free*100/mem_total))+"%Free)"
