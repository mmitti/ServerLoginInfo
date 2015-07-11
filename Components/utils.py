import shlex, subprocess, math
import unicodedata

def docmd(cmd):
    cmd_list = shlex.split(cmd)
    ret = subprocess.check_output(cmd_list).decode('utf-8')
    return ret

def cat(path):
    f = open(path)
    ret = f.read()
    f.close()
    return ret

def addSIPrefix(val):
    prefix = ["", "k", "M", "G", "T", "P"]
    div = 0
    for p in prefix:
        if(val >= 1024**(div+1)):
            div = div + 1
            continue
        return str(round(val / 1024**div, 2)) + p
    return str(val)

def mlen(u):
   n = 0
   for c in u:
      wide_chars = u"WFA"
      eaw = unicodedata.east_asian_width(c)
      if(wide_chars.find(eaw) > -1):
         n +=1
   return n + len(u)

def setBorder(window):
    window.border()
