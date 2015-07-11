# -*- coding: utf-8 -*-
from . import component
from . import utils
import datetime, curses
class ServiceStatus(component.Component):
    def __init__(self, w):
        super().__init__(w)
        utils.setBorder(w)
        loaded_count = 0
        active_count = 0
        failed_count = 0
        running_count = 0
        text =  utils.docmd("systemctl list-units -t service").replace("\xe2\x97\x8f", "").split("\n")
        for l in text:
            line = l.split()
            if len(line) == 0:
                break
            elif line[0] == "UNIT":
                continue

            if line[1] == "loaded":
                loaded_count += 1

            if line[2] == "active":
                active_count += 1
            elif line[2] == "failed":
                failed_count += 1

            if line[3] == "running":
                 running_count += 1
        text = str(loaded_count) + "Loaded, " + str(active_count) + "Active, " \
            + str(failed_count) + "Failed, " + str(running_count) + "Running"
        if failed_count > 0:
            text += " @see systemctl list-units -t service"

        width = self.window.getmaxyx()[1]
        self.window.addnstr(2, 1, text, width-2)
        text = "[OK]"
        color = 2
        if failed_count > 0:
            text = "[WARN]"
            color = 4
        self.window.addstr(2, width - utils.mlen(text) - 1, text, curses.color_pair(color))
        text = "SERVICE"
        self.window.addstr(1, int((width-utils.mlen(text))/2) -1 , text)
        return

    def show(self):
        self.window.refresh();
        return
