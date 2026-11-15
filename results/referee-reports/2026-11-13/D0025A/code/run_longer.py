#!/usr/bin/env python3
import csv,subprocess,time,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
# Diagnostic follow-up justified by observed dependence on initial conditions.
jobs=[]
for K in [1,2]:
 for t in [.3,.5,.7]:jobs.append([100000,K,t*K,.3,.2,125,888000+K+round(t*100),10000,10000,'random'])
 jobs.append([100000,K,K/2,.3,.2,125,777123+K,10000,10000,'phase'])
 for t in [.35,.5,.65]:jobs.append([2000,K,t*K,.3,.2,125,777000+K+round(t*100),100000,200000,'random'])
for idx,job in enumerate(jobs):
 state=json.loads(Path('~/.claude/compute/compute_state.json').read_text())
 if state.get('status')=='distress':print('Stopped at distress',flush=True);break
 begin=time.time();raw=subprocess.check_output([str(ROOT/'code/ring_sim')]+list(map(str,job)),text=True)
 with (ROOT/'data/ring_currents.csv').open('a') as f:f.write(raw)
 row=next(csv.reader([raw]));print(f'{idx+1}/{len(jobs)} {job[:3]} {job[-1]} J={row[12]} wall={time.time()-begin:.1f}',flush=True)
