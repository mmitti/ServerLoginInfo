# -*- coding: utf-8 -*-
import component
import utils
import datetime
class StartDate(component.Component):
    def __init__(self):
        return
    def show(self):
        uptime = utils.cat("/proc/uptime").rsplit(" ")[0]
        stime = datetime.datetime.now() - datetime.timedelta(seconds = int(float(uptime)))

        return "START DATE:"+ stime.strftime("%Y年%m月%d日 %H時%M分")
