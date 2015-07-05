import shlex, subprocess, math

def docmd(cmd):
    cmd_list = shlex.split(cmd)
    return subprocess.check_output(cmd_list)
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
