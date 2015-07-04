# -*- coding: utf-8 -*-
import component
import utils
import datetime
class Uptime(component.Component):
    def __init__(self):
        return
    def show(self):
        ret = "UPTIME:"
        uptime = utils.cat("/proc/uptime").split()[0]
        delt = datetime.timedelta(seconds = int(float(uptime)))
        days = delt.days
        sec = delt.seconds
        dtime = datetime.datetime(1900, 1, 1) + datetime.timedelta(seconds = delt.seconds)
        if days > 0:
            ret += str(days) + "日 "
        ret += dtime.strftime("%H時間%M分%S秒")
        return ret
