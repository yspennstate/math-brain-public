"""Initialize an exact replay worker without importing the numerical solver."""
import os,resource,sys
from exact_bernstein import data

def initialize():
    try:os.setpriority(os.PRIO_PROCESS,0,5)
    except PermissionError:pass
    if sys.platform.startswith('linux'):
        resource.setrlimit(resource.RLIMIT_AS,(600*1024**2,600*1024**2))
    data()
