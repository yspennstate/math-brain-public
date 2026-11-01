# run a script at BelowNormal priority: python run_low.py script.py args...
import sys, psutil, runpy
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
sys.argv = sys.argv[1:]
runpy.run_path(sys.argv[0], run_name="__main__")
