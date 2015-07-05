# -*- coding: utf-8 -*-
import os
from Components import *
import curses
import locale
import unicodedata

locale.setlocale(locale.LC_ALL,"")
h = loginHeader.LoginHeader()
u = date.Uptime()
#s = date.StartDate()
k = system.KernelVersion()
a = system.Architecture()
dis = system.Distribution()
#d = date.Date()
ms = mem.SwapUsage()
mm = mem.MemUsage()
#du = disk.DiskUsage();
#ss = service.ServiceStatus();


def mlen(u):
   n = 0
   for c in u:
      wide_chars = u"WFA"
      eaw = unicodedata.east_asian_width(c)
      if(wide_chars.find(eaw) > -1):
         n +=1
   return n + len(u)

def setBorder(window):
    #window.border('|', '|', '-', '-', '+', '+', '+', '+')
    window.border()
def main(screen):
    frame = curses.initscr()
    width = curses.tigetnum("cols") - 2
    w = curses.newwin(11, width, 0, 1)

    w2 = curses.newwin(5, 35, 6, 2)
    w3 = curses.newwin(4, width-4, 2, 2)
    w.addstr(1, 1, h.show())
    text = u.show()
    w.addstr(1, width - mlen(text)-1, text)
    text = "MEM"
    w2.addstr(1, int((35-mlen(text))/2) -1 , text)
    w2.addstr(2, 1, mm.show())
    w2.addstr(3,1, ms.show())

    w3.addstr(1, 1, dis.show() )
    w3.addstr(2, 1, k.show()+a.show())

    setBorder(w)
    setBorder(w2)
    setBorder(w3)

    frame.refresh()
    w.refresh()
    w2.refresh()
    w3.refresh()
    curses.napms(5000)

curses.wrapper(main)
