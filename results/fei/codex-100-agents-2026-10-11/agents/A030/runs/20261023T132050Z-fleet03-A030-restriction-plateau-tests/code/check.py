from pathlib import Path
from fractions import Fraction as F
import itertools,time,json,hashlib,sys
RUN=Path(__file__).resolve().parents[1]
OLD=RUN.parents[1]/'runs/20261023T041014Z-fleet03-A030-restriction-plateau-tests/code/check.py'
h={'__file__':str(OLD)};exec(OLD.read_text(encoding='utf-8').split('rows=[]')[0],h)
coeff,kl,logf,add,positive,ZERO,enc=[h[k] for k in ['coeff','kl','logf','add','positive','ZERO','enc']]
start=time.perf_counter();pilot='--pilot' in sys.argv
checks=nodes=extinct=zero_reference_branches=nonfair=offtrue=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.perf_counter()-start<(55 if pilot else 170)
def nn(e):ck(positive(add((-1,e)))==ZERO)
def child(tab,i,s):return tuple(v for k,v in enumerate(tab) if (k>>i)&1==s)
def uniform(n):return {i:F(1,1<<n) for i in range(1<<n)}
def remove(k,i):return (k&((1<<i)-1))|((k>>(i+1))<<i)
def smooth(p,n):return {i:F(63,64)*p.get(i,F(0))+F(1,64*(1<<n)) for i in range(1<<n)}
def move(amp,ref,constant,i,s,n):
 global zero_reference_branches,nonfair
 out={}
 for k in {a&~(1<<i) for a in set(amp)|set(ref)}:
  a,b=amp.get(k,F(0)),amp.get(k|(1<<i),F(0));den=2*(a*a+b*b)
  K=(a+(-1)**s*b)**2/den if den else F(1,2)
  val=(ref.get(k,F(0))+ref.get(k|(1<<i),F(0)))*K
  if val:out[remove(k,i)]=val
 rho=sum(out.values(),F(0))
 if rho!=F(1,2):nonfair+=1
 if rho==0:
  zero_reference_branches+=1
  return uniform(n-1),F(0)
 return {k:v/rho for k,v in out.items()},2*rho*constant
def root(labels,cores):
 nc=(len(labels)-1).bit_length();nd=(len(cores[0])-1).bit_length();ell=len(cores)
 pi=[F(labels.count(j),len(labels)) for j in range(ell)]
 ca=[coeff(tuple(int(v==j) for v in labels)) for j in range(ell)]
 A=tuple(smooth({u:v*v/pi[j] for u,v in ca[j].items()},nc) for j in range(ell))
 R=tuple(smooth({t:v*v for t,v in coeff(core).items()},nd) for core in cores)
 return (labels,cores,A,R,tuple(p*F(64,63) for p in pi),tuple(F(64,63) for _ in cores),tuple(range(nc+nd)),nc)
def build(st):
 global extinct,offtrue
 labels,cores,A,R,mu,lam,rem,nc=st;ell=len(cores);amp={};qe={};qi={}
 for j,core in enumerate(cores):
  ca=coeff(tuple(int(v==j) for v in labels));b=coeff(core)
  ck(sum(A[j].values())==sum(R[j].values())==1)
  ck(all(v*v<=mu[j]*A[j].get(u,F(0)) for u,v in ca.items()))
  ck(all(v*v<=lam[j]*R[j].get(t,F(0)) for t,v in b.items()))
  pi=F(labels.count(j),len(labels));ck(mu[j]>=pi);ck(lam[j]>=1)
  if not pi:extinct+=1
  for u,v in ca.items():
   for t,w in b.items():
    key=u|(t<<nc);amp[key]=amp.get(key,F(0))+v*w;qi[key]=qi.get(key,F(0))+v*v*w*w
  for u,v in A[j].items():
   for t,w in R[j].items():
    key=u|(t<<nc);qe[key]=qe.get(key,F(0))+v*w/ell
 amp={k:v for k,v in amp.items() if v};p={k:v*v for k,v in amp.items()};qi={k:v for k,v in qi.items() if v}
 M=ell*sum(m*l for m,l in zip(mu,lam));ck(M>=ell)
 ck(sum(p.values())==sum(qe.values())==sum(qi.values())==1)
 ck(all(v<=M*qe[k] for k,v in p.items()));ck(all(v<=ell*qi[k] for k,v in p.items()))
 offtrue+=sum(v>0 and not p.get(k) for k,v in qe.items())
 # Declare an actual history-dependent old/new profile rule; BOTH references validated.
 q=qi if len(rem)%2 else qe
 D=kl(p,q);nn(add((1,logf(M)),(-1,D)))
 return amp,q,D,M
def step(st,i):
 global nodes
 nodes+=1;labels,cores,A,R,mu,lam,rem,nc=st;ell=len(cores);pos=rem.index(i)
 amp,q,D,M=build(st);inh=h['transport'](amp,q,pos);kids=[]
 for s in (0,1):
  if pos<nc:
   lab=child(labels,pos,s);cs=cores;RR=R;ll=lam;AA=[];mm=[]
   for j in range(ell):
    ca=coeff(tuple(int(v==j) for v in labels));a,m=move(ca,A[j],mu[j],pos,s,nc);AA.append(a);mm.append(m)
   nc2=nc-1
  else:
   lab=labels;AA=A;mm=mu;cs=[];RR=[];ll=[];nc2=nc
   for j in range(ell):
    rr,l=move(coeff(cores[j]),R[j],lam[j],pos-nc,s,(len(cores[j])-1).bit_length())
    ck(l>0);cs.append(child(cores[j],pos-nc,s));RR.append(rr);ll.append(l)
  ns=(tuple(lab),tuple(cs),tuple(AA),tuple(RR),tuple(mm),tuple(ll),tuple(k for k in rem if k!=i),nc2)
  a,qq,dd,MM=build(ns);ck(a==inh[s][0]);kids.append((ns,dd,MM))
 ck(sum(k[2] for k in kids)/2==M)
 for j in range(ell):ck(sum(k[0][4][j]*k[0][5][j] for k in kids)/2==mu[j]*lam[j])
 avg=add(*((F(1,2),k[1]) for k in kids));old=add(*((F(1,2),inh[s][2]) for s in (0,1)))
 raw=add((1,avg),(-1,old));refund=add((1,D),(-1,old));sigma=add((1,avg),(-1,D))
 ck(raw==add((1,sigma),(1,refund)));nn(refund)
 return kids
PD=(1,1,1,-1);SHIFT=(1,1,-1,1);OR=(-1,1,1,1);Z=(1,-1,1,-1);NZ=tuple(-v for v in Z)
cases=[('binary',(0,1),(PD,SHIFT))]
if not pilot:
 for labels in [(0,1,2,1),(0,0,1,2),(0,1,2,0),(0,2,1,2),(0,1,2,2)]:
  for cores in [(PD,SHIFT,OR),(Z,NZ,PD)]:cases.append(('ternary',labels,cores))
records=[];policies=0
for name,labels,cores in cases:
 st0=root(labels,cores);M0=build(st0)[3];orders=list(itertools.permutations(st0[6]))
 if not pilot and labels==(0,1,2,1) and cores==(PD,SHIFT,OR):orders.append(None)
 for order in orders:
  policies+=1;frontier=[(st0,F(1))]
  for depth in range(len(st0[6])):
   nxt=[]
   for st,reach in frontier:
    i=order[depth] if order else (min(st[6]) if st[0][0]==0 else max(st[6]))
    for ns,D,M in step(st,i):nxt.append((ns,reach/2))
   frontier=nxt;vals=[(w,build(st)[2],build(st)[3]) for st,w in frontier]
   ck(sum(w*M for w,D,M in vals)==M0)
   avgD=add(*((w,D) for w,D,M in vals));avlog=add(*((w,logf(M)) for w,D,M in vals))
   nn(add((1,logf(M0)),(-1,avlog)));nn(add((1,avlog),(-1,avgD)))
  records.append({'labels':list(labels),'cores':[list(c) for c in cores],'order':list(order) if order else 'adaptive','final_expected_KL':enc(avgD)})
ck(nodes==(42 if pilot else 3657));ck(zero_reference_branches>0);ck(extinct>0);ck(offtrue>0)
ck(3**8<2**13);ck(64**32<2*63**32)
# Independently reconstruct the sharp coherence example without the helper.
parity=tuple((-1)**((y+z)%2) for z in (0,1) for y in (0,1))
ck(coeff(parity)=={3:F(1)})
out={'status':'PASS','pilot':pilot,'query_nodes':nodes,'policies':policies,'checks':checks,'helper_assertions':h['checks'],'zero_controller_reference_branches':zero_reference_branches,'extinct_label_build_receipts':extinct,'nonfair_branch_receipts':nonfair,'off_true_reference_row_receipts':offtrue,'initial_uniform_bound':'ell*(64/63)^2','reserve':'strictly greater than3/16 for all even r>=4','records':records,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start,'full_fei':'OPEN'}
(RUN/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
