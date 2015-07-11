# -*- coding: utf-8 -*-
from . import component
from . import utils
import datetime
import curses
class _Date(component.Component):
    def __init__(self, w):
        super().__init__(w)
        return
    def update(self):
        text = "DATE:" + utils.docmd("date").rstrip()
        self.window.addstr(0, 0, text)
        return

class _StartDate(component.Component):
    def __init__(self, w):
        super().__init__(w)
        return
    def update(self):
        width = self.window.getmaxyx()[1]
        if(width < 80):
            return
        uptime = utils.cat("/proc/uptime").rsplit(" ")[0]
        stime = datetime.datetime.now() - datetime.timedelta(seconds = int(float(uptime)))

        text =  "START DATE:"+ stime.strftime("%Y年%m月%d日 %H時%M分").rstrip()
        self.window.addstr(0, width - utils.mlen(text)-1, text)
        return
class Date(component.Component):
    date = None
    start = None
    def __init__(self, w):
        super().__init__(w)
        self.date = _Date(w)
        self.start = _StartDate(w)
        return
    def update(self):
        self.window.clear()
        self.date.update()
        self.start.update()
        return
    def show(self):
        self.window.refresh();
        return

class Uptime(component.Component):
    def __init__(self, w):
        super().__init__(w)
        self.window.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', curses.ACS_VLINE)
        return
    def update(self):
        text = "UPTIME:"
        uptime = utils.cat("/proc/uptime").split()[0]
        delt = datetime.timedelta(seconds = int(float(uptime)))
        days = delt.days
        sec = delt.seconds
        dtime = datetime.datetime(1900, 1, 1) + datetime.timedelta(seconds = delt.seconds)
        if days > 0:
            text += str(days) + "日 "
        text += dtime.strftime("%H時間%M分%S秒")
        text = text.rstrip()
        width = self.window.getmaxyx()[1]
        self.window.addstr(0, width - utils.mlen(text)-1, text)
        return
    def show(self):
        self.window.refresh()
