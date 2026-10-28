import gc,runpy,sys
from pathlib import Path
P=Path(__file__).resolve().parent
for name,args in [('check_inherited.py',[]),('check_radial_review.py',[]),('check_inherited.py',['--direct'])]:
 sys.argv=[str(P/name)]+args
 runpy.run_path(str(P/name),run_name='__main__')
 gc.collect()
