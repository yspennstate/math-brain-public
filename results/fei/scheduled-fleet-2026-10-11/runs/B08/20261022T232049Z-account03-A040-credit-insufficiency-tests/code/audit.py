from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
from arithmetic import *
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0

def ck(x):
 global checks
 assert x;checks+=1
 if time.perf_counter()-t0>55:raise RuntimeError('audit55s')
def overlap(a,b):ck(max(a[0],b[0])<=min(a[1],b[1]))
def read(k):return json.loads((R/'out'/k).read_text(encoding='utf-8'))
def iv(v):return tuple(F(x) for x in v)
def ln32(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(32)),F(0));return s,s+2*z**65/(65*(1-z*z))
L=ln32(F(2))
def log32(x):
 k=x.numerator.bit_length()-x.denominator.bit_length();v=x/F(2)**k
 if v<1:v*=2;k-=1
 a,b=ln32(v);return a/L[1]+k,b/L[0]+k
def phi32(x):return scale(log32(x),-x) if x else Z
margs=[F(j,64) for j in [15,3,9,9,7,7,21]];M=Z
for x in margs:M=add(M,add(phi32(x),phi32(1-x)))
margin=sub((F(265,64),)*2,M);bad=sub(margin,(F(1,64),)*2)
ck(margin[0]>F(1,800));ck(margin[1]<F(13,10000));ck(bad[1]<-F(7,500));ck(bad[0]>-F(3,200));overlap(margin,iv(read('REVIEW.json')['new_root_bank']))
g=(-1,-1,-1,1,1,1,1,1);f=family(g)
def direct(v):return tuple(F(sum(y*(-1 if (s&x).bit_count()%2 else 1) for x,y in enumerate(v)),len(v)) for s in range(len(v)))
for v in [f,restrict(f,4,0),restrict(f,4,1)]:ck(direct(v)==spectrum(v))
ck([infl(f,i) for i in range(7)]==margs);policies=[]
for name in ['POLICY_00.json','POLICY_01.json','POLICY_10.json','POLICY_11.json']:
 o=read(name);records=[]
 def addS(sr,w):
  for leaf in sr['terminal_laws']:records.append((w if sr['skipped'] else w/2,leaf))
 for node in o['nodes']:
  if node.get('skipped_irrelevant_core'):addS(node['S'],F(1,2))
  else:
   for sr in node['S_children']:addS(sr,F(1,4))
 ck(sum(w for w,_ in records)==1);total=Z;positive=Z;negative=Z;constantdebt=Z;constant_count=0
 for w,leaf in records:
  P=[F(x) for x in leaf['P']];Q=[F(x) for x in leaf['Q']];ck(sum(P)==sum(Q)==1);ck(all(not p or q>0 for p,q in zip(P,Q)));ce=Z
  for p,q in zip(P,Q):
   if p:ce=add(ce,scale(log(q),-p))
  overlap(ce,iv(leaf['CE']));ival=F(leaf['I']);bv=sub((4*ival,)*2,ce);total=add(total,scale(bv,w))
  if bv[0]>=0:positive=add(positive,scale(bv,w))
  elif bv[1]<=0:negative=add(negative,scale(neg(bv),w))
  else:ck(False)
  if ival==0:constant_count+=1;constantdebt=add(constantdebt,scale(ce,w))
 overlap(total,iv(o['full_final_terminal_bank']));overlap(sub(positive,negative),total);costs=iv(o['combined_previously_booked_and_future_debit']);final=sub(total,costs);overlap(final,margin);ck(final[0]>F(1,800));ck(sub(positive,add(negative,costs))[0]>F(1,800))
 if o['choices'][0]==1:ck(o['held_deficit']=='1/64');ck(o['second_query_retired_part_drift']=='1/64')
 policies.append({'choices':o['choices'],'terminal_occurrences':len(records),'constant_terminal_occurrences':constant_count,'constant_terminal_CE':fmt(constantdebt),'positive_terminal_pool':fmt(positive),'negative_terminal_liabilities':fmt(negative),'old_and_new_signed_costs':fmt(costs),'paid_margin':fmt(final)})
source=R.resolve().parents[2]/'A046/runs/20261021T192754Z-account03-A046-current-candidate-intake/CLAIMS.json';sc=[c for c in json.loads(source.read_text(encoding='utf-8')) if c['claim_id']=='A046-PRESCRIBED-SEPARATOR-RESERVE-RETIREMENT'][0];ck(hashlib.sha256(sc['exact_statement'].encode()).hexdigest()==sc['statement_sha256'])
out={'status':'PASS','checks':checks,'runtime_seconds':time.perf_counter()-t0,'source_statement_sha256':sc['statement_sha256'],'independent32term_root_margin':fmt(margin),'policy_full_terminal_audits':policies}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print({k:v for k,v in out.items() if k not in ['policy_full_terminal_audits','independent32term_root_margin']})
