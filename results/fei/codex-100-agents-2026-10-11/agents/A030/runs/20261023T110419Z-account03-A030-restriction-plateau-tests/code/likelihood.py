from pathlib import Path
from fractions import Fraction as F
import itertools,time,json,hashlib,sys
RUN=Path(__file__).resolve().parents[1];OLD=RUN.parents[1]/'runs/20261023T041014Z-account03-A030-restriction-plateau-tests/code/check.py'
h={'__file__':str(OLD)};exec(OLD.read_text(encoding='utf-8').split('rows=[]')[0],h)
add,kl,coeff,positive,ZERO,enc,logf=[h[k] for k in ['add','kl','coeff','positive','ZERO','enc','logf']]
checks=nodes=nonfair=0;start=time.perf_counter();pilot='--pilot' in sys.argv
def ck(v):
 global checks
 checks+=1;assert v,checks;assert time.perf_counter()-start<55
def nonneg(e):ck(positive(add((-1,e)))==ZERO)
def child(t,i,s):return tuple(v for k,v in enumerate(t) if ((k>>i)&1)==s)
def build(st):
 labels,cores,refs,lams,remaining,nc=st;amp={};q={}
 for j,core in enumerate(cores):
  b=coeff(core);ck(sum(refs[j].values())==1);ck(all(v*v<=lams[j]*refs[j].get(t,F(0)) for t,v in b.items()))
  for u,c in coeff(tuple(int(x==j) for x in labels)).items():
   for t,v in b.items():key=u|(t<<nc);amp[key]=amp.get(key,F(0))+c*v
   for t,r in refs[j].items():key=u|(t<<nc);q[key]=q.get(key,F(0))+c*c*r
 amp={k:v for k,v in amp.items() if v};p={k:v*v for k,v in amp.items()};M=sum(lams)
 ck(sum(p.values())==sum(q.values())==1);ck(all(v<=M*q[k] for k,v in p.items()))
 D=kl(p,q);nonneg(add((1,logf(M)),(-1,D)))
 return amp,q,D,M
def source_step(core,ref,lam,i,s):
 global nonfair
 a=coeff(core);bases={k&~(1<<i) for k in set(a)|set(ref)};out={}
 for k in bases:
  x,y=a.get(k,F(0)),a.get(k|(1<<i),F(0));den=2*(x*x+y*y)
  ker=(x+(-1)**s*y)**2/den if den else F(1,2)
  mass=(ref.get(k,F(0))+ref.get(k|(1<<i),F(0)))*ker
  new=h['remove'](k,i)
  if mass:out[new]=mass
 rho=sum(out.values());ck(rho>0)
 if rho!=F(1,2):nonfair+=1
 return child(core,i,s),{k:v/rho for k,v in out.items()},2*rho*lam
def step(st,i):
 global nodes
 nodes+=1;amp,q,D,M=build(st);lab,cs,refs,lam,rem,nc=st;pos=rem.index(i)
 inh=h['transport'](amp,q,pos);kids=[]
 for s in (0,1):
  if pos<nc:new=(child(lab,pos,s),cs,refs,lam,tuple(j for j in rem if j!=i),nc-1)
  else:
   vals=[source_step(cs[j],refs[j],lam[j],pos-nc,s) for j in range(2)]
   new=(lab,tuple(x[0] for x in vals),tuple(x[1] for x in vals),tuple(x[2] for x in vals),tuple(j for j in rem if j!=i),nc)
  a,qq,dd,mm=build(new);ck(a==inh[s][0]);kids.append((new,dd,mm))
 ck((kids[0][2]+kids[1][2])/2==M)
 avg=add((F(1,2),kids[0][1]),(F(1,2),kids[1][1]));old=add((F(1,2),inh[0][2]),(F(1,2),inh[1][2]))
 raw=add((1,avg),(-1,old));refund=add((1,D),(-1,old));sigma=add((1,avg),(-1,D))
 ck(raw==add((1,sigma),(1,refund)));nonneg(refund)
 return kids
PD3=tuple(-1 if x==0 else 1 for x in range(8));MAJ=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
uniform={t:F(1,8) for t in range(8)}
root=((0,1),(PD3,MAJ),(uniform,uniform),(F(9,2),F(2)),(0,1,2,3),1)
Mroot=F(13,2);records=[]
orders=[(0,1,2,3)] if pilot else list(itertools.permutations(range(4)))+[None]
for order in orders:
 frontier=[(root,F(1))]
 for depth in range(4):
  nxt=[]
  for st,reach in frontier:
   i=order[depth] if order is not None else (min(st[4]) if st[0][0]==0 else max(st[4]))
   for child_st,D,M in step(st,i):nxt.append((child_st,reach/2))
  frontier=nxt;vals=[(w,build(st)[2],sum(st[3])) for st,w in frontier]
  ck(sum(w*M for w,D,M in vals)==Mroot)
  avgD=add(*((w,D) for w,D,M in vals));avglog=add(*((w,logf(M)) for w,D,M in vals))
  nonneg(add((1,logf(Mroot)),(-1,avglog)));nonneg(add((1,avglog),(-1,avgD)))
 records.append({'order':list(order) if order else 'adaptive','final_expected_KL':enc(avgD)})
ck(nodes==(15 if pilot else 375));ck(nonfair>0)
out={'status':'PASS','pilot':pilot,'checks':checks,'helper_assertions':h['checks'],'query_nodes':nodes,'nonfair_source_branch_receipts':nonfair,'initial_likelihood_sum':'13/2','complete_policies':len(orders),'records':records,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_fei':'OPEN'}
(RUN/'out'/('LIKELIHOOD_PILOT.json' if pilot else 'LIKELIHOOD.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
