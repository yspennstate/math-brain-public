"""Verify saved source physical prices and signed query label exactly."""
from pathlib import Path
from fractions import Fraction as F
import json,time
start=time.perf_counter();R=Path(__file__).resolve().parents[1]
source=Path('agents/A084/runs/20261023T035136Z-fleet03-A084-continuum-parameters/out/JOINT_CASES.json')
data=json.loads(source.read_text(encoding='utf-8'));I={};checks=0
def ck(b):
 global checks
 assert b;checks+=1
types=[('P',0)]+[('A',m) for m in range(6)]+[('L',m) for m in range(2,7)]
tabs=[(1,) if k=='P' else tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m)) for k,m in types]
for j in range(12):
 for x in json.loads((R/'out'/f'BLOCK_{j:02d}_STATES.json').read_text(encoding='utf-8')):I[tuple(x['state'])]=F(x['I'])
def child(t,j,b):return tuple(v for x,v in enumerate(t) if x>>j&1==b)
def canon(t):
 for j in range(len(t).bit_length()-1):
  if child(t,j,0)==child(t,j,1):return canon(child(t,j,0))
 return t
def add(*ps):
 d={}
 for p in ps:
  for k,v in p.items():d[k]=d.get(k,F(0))+v
 return {k:v for k,v in d.items() if v}
def mul(p,q):return {k:v*q for k,v in p.items() if v*q}
def unpack(p):return {int(k):F(v) for k,v in p.items() if F(v)}
rows=0
for item in data:
 pair=[j-2 for j in item['pair_original']];ss={tuple(tuple(t) for t in z['truths']):unpack(z['S']) for z in item['states_certificate']}
 def state(raw):
  out=[11]*4
  for j,t in zip(pair,raw):out[j]=tabs.index(tuple(t))
  return tuple(out)
 for z in item['rows']:
  raw=tuple(tuple(t) for t in z['state']);j=z['side'];coord=z['coordinate'];kids=[]
  for b in range(2):kids.append(raw[:j]+(canon(child(raw[j],coord,b)),)+raw[j+1:])
  expected=I[state(raw)]-(I[state(kids[0])]+I[state(kids[1])])/2
  ck(expected==F(z['physical_influence']));ck(expected>=0)
  e=add(mul(add(ss[kids[0]],ss[kids[1]]),F(1,2)),mul(ss[raw],-1));ck(e==unpack(z['query_excess']));rows+=1
ck(rows==2520);ck(time.perf_counter()-start<55)
out={'verdict':'PASS','source_rows':rows,'assertions':checks,'seconds':time.perf_counter()-start,'scope':'Physical influence and signed query-excess labels, using source S identities already independently proved exactly in ledger.py.'}
(R/'out/SOURCE_PRICES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
