from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import json,time,sys
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
cap=50 if pilot else 180
kernel={'__file__':str(ROOT/'code'/'check_shared.py')}
exec((ROOT/'code'/'check_shared.py').read_text(encoding='utf-8').split('# Exact five-variable local module:')[0],kernel)
split,restrict=kernel['split'],kernel['restrict'];add,mul=kernel['add'],kernel['mul'];emit=kernel['emit']
vals=kernel['table'](4,2)
beta=(Q(326522370791,10**12),Q(326522370792,10**12))
def walk(order,adaptive=False):
 totals=dict(raw=Q(0),exposure=Q(0),joint=(Q(0),Q(0)),leafI=Q(0),leafH=(Q(0),Q(0)),contexts=0)
 def visit(t,labels,pending,fixed,weight):
  if time.perf_counter()-start>cap:raise RuntimeError('frozen cap')
  if not pending:
   # All shared phase and selectors are fixed; keep actual terminal tables.
   totals['leafI']+=weight*kernel['influence'](t)
   totals['leafH']=add(totals['leafH'],mul(kernel['entropy_table'](t),weight));return
  unit=pending[0]
  if adaptive and len(pending)==3 and fixed.get(8)==0:
   # After selector0=0 expose the first core pair before selector1.
   unit=next(v for v in pending if v.startswith('p'))
  remainder=[v for v in pending if v!=unit]
  if unit.startswith('s'):
   query=8 if unit=='s0' else 13;index=labels.index(query)
   phase=split(t,index);d=phase['d'];W=phase['W'];B=phase['B'];U=sum(v in labels for v in range(4))
   assert d in [Q(0),Q(1,32),Q(1,16)]
   if d:
    assert B[0]>4*d
    totals['raw']+=weight*W
    totals['joint']=add(totals['joint'],mul((B[0]-4*d,B[1]-4*d),weight))
   totals['exposure']+=weight*U;totals['contexts']+=1
   childlabels=[v for v in labels if v!=query]
   for bit in [0,1]:visit(restrict(t,index,bit),childlabels,remainder,{**fixed,query:bit},weight/2)
  else:
   pair=[0,1] if unit=='p0' else [2,3]
   for outcome in range(4):
    child=t;childlabels=list(labels);more=dict(fixed)
    for j,query in enumerate(pair):
     child=restrict(child,childlabels.index(query),(outcome>>j)&1);childlabels.remove(query);more[query]=(outcome>>j)&1
    visit(child,childlabels,remainder,more,weight/4)
 visit(vals,list(range(14)),list(order),{},Q(1))
 expected=(Q(8)+totals['exposure'])/32
 assert totals['raw']==expected
 wanted=(beta[0]-Q(1,4),beta[1]-Q(1,4))
 assert totals['joint'][0]<=wanted[1] and totals['joint'][1]>=wanted[0]
 assert totals['leafI']==Q(17,4)
 return dict(order=list(order),adaptive=adaptive,selector_raw=str(totals['raw']),expected_exposure=str(totals['exposure']),selector_joint=emit(totals['joint']),terminal_I=str(totals['leafI']),terminal_H=emit(totals['leafH']),selector_contexts=totals['contexts'])
orders=[('s0','s1','p0','p1'),('p0','p1','s0','s1')] if pilot else list(permutations(['s0','s1','p0','p1']))
records=[]
for order in orders:
 records.append(walk(order))
 with (ROOT/'out'/('exposure_pilot.jsonl' if pilot else 'exposure_records.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(records[-1])+'\n')
if not pilot:records.append(walk(('s0','s1','p0','p1'),True))
out=dict(helper_version='A035-shared-phase-exposure-v1',pilot=pilot,runtime_seconds=time.perf_counter()-start,policy_count=len(records),selector_context_count=sum(r['selector_contexts'] for r in records),records=records,scope='Selector-only exposure; actual terminal entropy retained; no whole-tree adaptive payment inferred.')
(ROOT/'out'/('exposure_pilot.json' if pilot else 'exposure_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
print('Extremes:',min(records,key=lambda r:Q(r['selector_raw'])),max(records,key=lambda r:Q(r['selector_raw'])))
if not pilot:print('Adaptive:',records[-1])
