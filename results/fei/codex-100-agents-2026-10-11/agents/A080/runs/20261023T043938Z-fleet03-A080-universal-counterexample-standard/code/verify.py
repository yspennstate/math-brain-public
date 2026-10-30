"""Standalone rational envelope checker, all physical rows, no solver imports."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
start=time.perf_counter();R=Path(__file__).resolve().parents[1];grid=1<<192;nchecks=0
def ck(x):
 global nchecks
 assert x;nchecks+=1
def read(n):return json.loads((R/'out'/n).read_text(encoding='utf-8'))
types=[('P',0)]+[('A',m) for m in range(6)]+[('L',m) for m in range(2,7)]
tabs=[(1,) if k=='P' else tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m)) for k,m in types]
def kid(t,j,b):return tuple(y for x,y in enumerate(t) if x>>j&1==b)
def canon(t):
 for j in range(len(t).bit_length()-1):
  if kid(t,j,0)==kid(t,j,1):return canon(kid(t,j,0))
 return t
actions=[]
for t in tabs:
 actions.append([(j,tuple(tabs.index(canon(kid(t,j,b))) for b in range(2))) for j in range(len(t).bit_length()-1)])
S={};I={};P={};rows=0;root=(11,)*4
for j in range(12):
 for d in read(f'BLOCK_{j:02d}_STATES.json'):
  k=tuple(d['state']);ck(k not in S);S[k]=d['S'];I[k]=F(d['I'])
 for d in read(f'ENVELOPE_{j:02d}.json'):
  k=tuple(d['state']);ck(k not in P);P[k]=d['rho_upper_grid']
ck(len(S)==len(I)==len(P)==20736)
A=(-S[root][1],-S[root][0]);minroot=None
for ts in product(range(12),repeat=4):
 rho=A[0] if ts==root else P[ts]
 if ts!=root:ck(rho>=0 and rho>=-S[ts][0])
 for j in range(4):
  for coordinate,children in actions[ts[j]]:
   keys=[ts[:j]+(c,)+ts[j+1:] for c in children];sump=P[keys[0]]+P[keys[1]]
   ck(2*rho>=sump);ck(I[ts]>=(I[keys[0]]+I[keys[1]])/2);rows+=1
   if ts==root:
    gap=F(2*rho-sump,2*grid);minroot=gap if minroot is None else min(minroot,gap)
ck(rows==241920);ck(minroot>F(379,100000))
l=read('LEDGER_VALIDATION.json');ck(F(l['both_touched_margin_lower_grid'],grid)>F(63,10000));ck(F(l['all_nonroot_margin_lower_grid'],grid)>F(379,100000))
ck(F(2857328,10**8)<F(A[0],grid)<=F(A[1],grid)<F(2857329,10**8))
ratio=(F(4)-F(S[root][1],grid)/I[root],F(4)-F(S[root][0],grid)/I[root]);ck(4<ratio[0]<=ratio[1]<5)
ck(time.perf_counter()-start<55)
result={'verdict':'PASS','boolean_profiles':len(S),'physical_query_rows':rows,'assertions':nchecks,'seconds':time.perf_counter()-start,'root_credit_interval':[str(F(x,grid)) for x in A],'root_I':str(I[root]),'root_ratio_interval':[str(x) for x in ratio],'root_ratio_between':'4 and5','root_min_continuation_margin':str(minroot),'no_solver_imports':True,'full_fei':'OPEN'}
(R/'out/INDEPENDENT_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k not in ['root_credit_interval','root_ratio_interval']}))
