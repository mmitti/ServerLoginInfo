# -*- coding: utf-8 -*-
import os
from Components import *
h = loginHeader.LoginHeader()
u = date.Uptime()
s = date.StartDate()
k = kernel.KernelVersion()
a = arch.Architecture()
d = date.Date()
ms = mem.SwapUsage()
mm = mem.MemUsage()
du = disk.DiskUsage();
print h.show()
print u.show()
print s.show()
print k.show()
print a.show()
print d.show()
print ms.show()
print mm.show()
print du.show()
