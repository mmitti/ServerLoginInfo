# -*- coding: utf-8 -*-
import os
from Components import *
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
print h.show()
print u.show()
print s.show()
print dis.show()
print k.show()
print a.show()
print d.show()
print ms.show()
print mm.show()
print du.show()
print ss.show()
