#!/usr/bin/env python3
"""Serial experiment runner. No more than one simulation worker, inherited nice 10."""
import datetime,subprocess,json,os
from pathlib import Path
assert os.getpriority(os.PRIO_PROCESS,0)>=10
runs=[]
for q,T in [(.1,4000),(.3,1200),(.6,600),(.85,400)]:
 for mode in [0,1]:
  path=f'data/q{q:g}_mode{mode}.csv'
  cmd=['code/simulate',str(q),'2000',str(T),'24000',str(mode),path,str(260026+int(q*1000)+mode*100000)]
  start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  result=subprocess.run(cmd,check=True,capture_output=True,text=True)
  rec={'command':cmd,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout':result.stdout.strip()}
  runs.append(rec);Path('data/runs.json').write_text(json.dumps(runs,indent=2)+'\n')
  print(result.stdout,flush=True,end='')
