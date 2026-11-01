import psutil, runpy, sys
psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
sys.argv = ['full_matrix3.py', '4', '0.25', '6', '90', '1']; runpy.run_path('full_matrix3.py', run_name='__main__')
