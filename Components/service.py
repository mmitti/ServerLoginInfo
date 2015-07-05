# -*- coding: utf-8 -*-
from . import component
from . import utils
import datetime
class ServiceStatus(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        ret = "SERVICE:"
        loaded_count = 0
        active_count = 0
        failed_count = 0
        running_count = 0
        text =  utils.docmd("systemctl list-units -t service").replace("\xe2\x97\x8f", "").split("\n")
        for l in text:
            line = l.split()
            if len(line) == 0:
                break
            elif line[0] == "UNIT":
                continue

            if line[1] == "loaded":
                loaded_count += 1

            if line[2] == "active":
                active_count += 1
            elif line[2] == "failed":
                failed_count += 1

            if line[3] == "running":
                 running_count += 1
        ret += str(loaded_count) + "Loaded, " + str(active_count) + "Active, " \
            + str(failed_count) + "Failed, " + str(running_count) + "Running"
        if failed_count > 0:
            ret += " @see systemctl list-units -t service[WARN]"
        else:
            ret += "[OK]"
        return ret
