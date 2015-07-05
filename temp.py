# -*- coding: utf-8 -*-
import os
import curses

def main(screen):
    frame = curses.initscr()
    w = curses.newwin(10, curses.tigetnum("cols") - 2, 0, 1)
    w2 = curses.newwin(6, 40, 2, 2)
    w.addstr(1, 34, "mmitti server")
    w2.addstr(1, 10, "Component A")

    w.move(9, 39)
    w.border('|', '|', '-', '-', '+', '+', '+', '+')
    w2.border('|', '|', '-', '-', '+', '+', '+', '+')

    frame.refresh()
    w.refresh()
    w2.refresh()
    curses.napms(1000)

curses.wrapper(main)
