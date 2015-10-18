# -*- coding: utf-8 -*-
import os
from Components import *
from Components import utils
import curses
import locale

locale.setlocale(locale.LC_ALL,"")

def main(screen):
    curses.curs_set(0)
    curses.use_default_colors()
    curses.init_pair(0, -1, -1)
    curses.init_pair(1,-1, curses.COLOR_RED)
    curses.init_pair(2, -1, curses.COLOR_GREEN)
    curses.init_pair(3, -1, curses.COLOR_CYAN)
    curses.init_pair(4, -1, curses.COLOR_YELLOW)
    width = screen.getmaxyx()[1] - 2
    if(width < 60):
        return
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

    for i in range(5):
        for c in components:
            c.update()
        frame.refresh()
        ld.update(i, 5)
        for c in components:
            c.show()
        curses.napms(900)
curses.wrapper(main)
