"""Reconstruct six published policy trees from independent raw-DAG spectra."""
import audit_hull as a
from fractions import Fraction as F
import json,time
from pathlib import Path
START=time.perf_counter();c=a.c
def unpack(p):return {None if k=='constant' else F(k):F(v) for k,v in p.items()}
states={}
for line in (a.R/'out/CASES.jsonl').read_text(encoding='utf-8').splitlines():
 z=json.loads(line);states[z['core'],tuple(z['tag'])]={k:unpack(z[k]) for k in ('S','R')}
peer=Path(r'agents\A072\runs\20261023T015130Z-fleet03-A072-exact-walsh-engine')
source=json.loads((peer/'out/HULL_CASES.json').read_text(encoding='utf-8'))
def iv(z):return tuple(F(v,1<<192) for v in z)
def pathkey(z):return tuple(tuple(x) for x in z)
def avg(xs):return c.scale(c.add(*xs),F(1,len(xs)))
receipts=[]
for p in source['financial_policies']:
 j=p['core'];rows={pathkey(z['path']):z for z in p['rows']};leaves={pathkey(z['path']):z for z in p['terminals']}
 root=states[j,(-1,)*6];base=a.mul(root['S'],-1)
 offset=iv(p['initial_debit']) if 'initial_debit' in p else c.point(0)
 labels=[iv(z) for z in p.get('initial_labels',[])]
 a.overlap(c.add(*labels),offset)
 a.overlap(c.add(a.ev(base),offset),iv(p['initial_credit']))
 weighted=[];leafcount=0;rowcount=0
 def visit(tag,path,credit,old):
  global leafcount,rowcount
  node=states[j,tag];D=a.add(node['S'],credit)
  a.overlap(c.add(a.ev(D),offset),c.add(*old))
  if path in leaves:
   z=leaves[path];leafcount+=1
   a.ck(F(z['reach'])==F(1,1<<len(path)))
   a.overlap(a.ev(node['S']),iv(z['S']))
   a.overlap(c.add(a.ev(credit),offset),iv(z['credit']))
   a.overlap(c.add(a.ev(D),offset),iv(z['debit']))
   a.ck(len(old)==len(z['booked_labels']))
   for x,y in zip(old,z['booked_labels']):a.overlap(x,iv(y))
   weighted.append(c.scale(c.add(a.ev(credit),offset),F(z['reach'])))
   return
  z=rows[path];rowcount+=1;i=z['original_coordinate'];a.ck(tag[i]==-1)
  a.ck(F(z['reach'])==F(1,1<<len(path)))
  tags=[tag[:i]+(b,)+tag[i+1:] for b in (0,1)]
  children=[states[j,t] for t in tags]
  spare=a.sub(credit,a.mean([x['R'] for x in children]));a.nonnegative(spare)
  credits=[a.add(x['R'],spare) for x in children]
  debits=[a.add(x['S'],cr) for x,cr in zip(children,credits)]
  e=a.sub(a.mean([x['S'] for x in children]),node['S']);T=a.mean(debits)
  a.ck(T==a.add(D,e));a.ck(a.mean(credits)==credit)
  a.overlap(a.ev(e),iv(z['e']));a.overlap(c.add(a.ev(T),offset),iv(z['T']))
  a.overlap(c.add(a.ev(credit),offset),iv(z['credit']))
  a.overlap(c.add(a.ev(D),offset),iv(z['old_booked']));a.ck(z['new_flow']==[0,0])
  if not T and offset==c.point(0):
   a.ck(all(not d for d in debits));kernels=[c.point(1)]*2
  else:
   denominator=c.add(a.ev(T),offset);c.pos(denominator)
   kernels=[c.div(c.add(a.ev(d),offset),denominator) for d in debits]
  for b in range(2):
   a.overlap(c.add(a.ev(credits[b]),offset),iv(z['child_credits'][b]))
   a.overlap(c.add(a.ev(debits[b]),offset),iv(z['child_debits'][b]))
  outgoing=[[c.mul(x,k) for x in old+[a.ev(e)]] for k in kernels]
  for k,L in enumerate(old+[a.ev(e)]):a.overlap(avg([ls[k] for ls in outgoing]),L)
  for b in (0,1):visit(tags[b],path+((i,b),),credits[b],outgoing[b])
 visit((-1,)*6,(),base,labels)
 a.ck(rowcount==len(rows) and leafcount==len(leaves))
 a.ck(sum(F(z['reach']) for z in leaves.values())==1)
 a.overlap(c.add(*weighted),c.add(a.ev(base),offset))
 receipts.append(dict(core=j,policy=p['order'],rows=rowcount,leaves=leafcount,source_initial_debit_used_only_as_additive_inherited_spare='initial_debit' in p,source_stop_reaches=p['source_stop_reaches'],zero_new_flow=True))
 a.save('FINANCIAL_VALIDATION.json',dict(passed=True,policies=receipts,checks=a.COUNT,helper_checks=c.COUNT,runtime_seconds=time.perf_counter()-START,exact_equalities='rational profiles and conditional-mean algebra in INDEPENDENT_PROOF.md',interval_overlap_role='comparison diagnostics only; never an equality proof',scope='source policy choices reconstructed using independent raw labelled S/R; positive initial-debit amounts are source inputs, not newly audited source-prefix funding'))
 a.ck(time.perf_counter()-START<55)
print(json.dumps(dict(passed=True,policies=len(receipts),checks=a.COUNT,helper_checks=c.COUNT,runtime_seconds=time.perf_counter()-START)))
