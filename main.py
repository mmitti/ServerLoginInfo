# -*- coding: utf-8 -*-
import os
from Components import *
from Components import utils
import curses
import locale

locale.setlocale(locale.LC_ALL,"")

'''
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
'''


def main(screen):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(0, -1, -1)
    curses.init_pair(1,-1, curses.COLOR_RED)
    curses.init_pair(2, -1, curses.COLOR_GREEN)
    curses.init_pair(3, -1, curses.COLOR_CYAN)
    curses.init_pair(4, -1, curses.COLOR_YELLOW)
    width = screen.getmaxyx()[1] - 2
    height = screen.getmaxyx()[0]
    frame = curses.newwin(18, width, 0, 1)
    frame.bkgdset(1)
    utils.setBorder(frame)

    components = []

    components.append( loginHeader.LoginHeader(curses.newwin(1, width-2, 1, 2)) )
    if(width > 50):
        components.append( date.Uptime(curses.newwin(1, 30, 1, width - 29)) )
    components.append( date.Date(curses.newwin(1, width -3, 6, 3)) )
    components.append( system.System(curses.newwin(4, width -2, 2, 2)) )

    components.append( mem.MemInfo(curses.newwin(5, 35, 7, 2)) )

    components.append( disk.DiskUsage(curses.newwin(6, width - 37, 7, 37)) )
    components.append( service.ServiceStatus(curses.newwin(4, width-2, 13, 2)) )
    ld = loading.Loading(curses.newwin(1, width-2, height - 1, 2))
    components.append( ld )

    for i in range(20):
        for c in components:
            c.update()
        frame.refresh()
        ld.update(i, 20)
        for c in components:
            c.show()
        curses.napms(250)
'''
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
    text = a.show()
    w3.addstr(1,width - 2 - mlen(text) - 1,text)
    w3.addstr(2, 1, k.show())
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
'''




curses.wrapper(main)
