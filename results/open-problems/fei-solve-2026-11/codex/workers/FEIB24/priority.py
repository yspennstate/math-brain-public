"""Run one process politely without attempting to renice beyond macOS limits."""
import os,sys
level=os.getpriority(os.PRIO_PROCESS,0)
if level<10: os.nice(10-level)
os.execvp(sys.argv[1],sys.argv[1:])
