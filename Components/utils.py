import shlex, subprocess

def docmd(cmd):
    cmd_list = shlex.split(cmd)
    return subprocess.check_output(cmd_list)
def cat(path):
    f = open(path)
    ret = f.read()
    f.close()
    return ret
