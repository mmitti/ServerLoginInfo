# -*- coding: utf-8 -*-
import os
import curses

frame = curses.initscr()
w = curses.newwin(10, curses.tigetnum("cols") - 2, 0, 1)
dummy_frame = curses.newwin(1, 1, 9, curses.tigetnum("cols"))
w2 = curses.newwin(6, 40, 2, 2)
w.addstr(1, 34, "mmitti server")
w2.addstr(1, 10, "Component A")

w.move(9, 39)
w.border()
w2.border()

w.refresh()
w2.refresh()
dummy_frame.refresh()
