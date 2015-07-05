# -*- coding: utf-8 -*-
from . import component
from . import utils
import datetime
class Date(component.Component):
    def __init__(self):
        component.Component.__init__(self)
        return
    def show(self):
        return "DATE:" + utils.docmd("date").rstrip()

class StartDate(component.Component):
    def __init__(self):
        return
    def show(self):
        uptime = utils.cat("/proc/uptime").rsplit(" ")[0]
        stime = datetime.datetime.now() - datetime.timedelta(seconds = int(float(uptime)))

        return "START DATE:"+ stime.strftime("%Y年%m月%d日 %H時%M分")

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
