# -*- coding: utf-8 -*-
import os
from Components import *
h = loginHeader.LoginHeader()
u = uptime.Uptime()
s = startDate.StartDate()
k = kernel.KernelVersion()
a = arch.Architecture()
d = date.Date()
ms = mem.SwapUsage()
print h.show()
print u.show()
print s.show()
print k.show()
print a.show()
print d.show()
print ms.show()
