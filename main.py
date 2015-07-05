# -*- coding: utf-8 -*-
import os
from Components import *
import curses
import locale
import unicodedata

locale.setlocale(locale.LC_ALL,"")
h = loginHeader.LoginHeader()
u = date.Uptime()
s = date.StartDate()
k = system.KernelVersion()
a = system.Architecture()
dis = system.Distribution()
d = date.Date()
ms = mem.SwapUsage()
mm = mem.MemUsage()
du = disk.DiskUsage();
ss = service.ServiceStatus();


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
    w = curses.newwin(17, width, 0, 1)

    w2 = curses.newwin(5, 35, 7, 2)
    w3 = curses.newwin(4, width-2, 2, 2)

    w4 = curses.newwin(1, width-2, 6, 2)
    w5 = curses.newwin(6, width - 1 - 36, 7, 37)

    w6 = curses.newwin(3, width-2, 13, 2)
    w.addstr(1, 1, h.show())
    text = u.show()
    w.addstr(1, width - mlen(text)-1, text)
    text = "MEM"
    w2.addstr(1, int((35-mlen(text))/2) -1 , text)
    w2.addstr(2, 1, mm.show())
    w2.addstr(3,1, ms.show())

    w3.addstr(1, 1, dis.show() )
    w3.addstr(2, 1, k.show()+a.show())
    w4.addstr(0, 1, d.show() )
    text = s.show()
    w4.addstr(0, width-2 - mlen(text) - 1, text )

    text = "FILE SYSTEM"
    w5.addstr(1, int((width - 1 - 36-len(text))/2) -1 , text)
    text = du.show().rstrip().split("\n")
    w5.addstr(2, 1 , text[0])
    w5.addstr(3, 1 , text[1])
    w5.addstr(4, 1 , text[2])

    w6.addstr(1, 1, ss.show())

    setBorder(w)
    setBorder(w2)
    setBorder(w3)

    setBorder(w5)

    setBorder(w6)

    frame.refresh()
    w.refresh()
    w2.refresh()
    w3.refresh()
    w4.refresh()

    w5.refresh()

    w6.refresh()
    curses.napms(5000)

curses.wrapper(main)
