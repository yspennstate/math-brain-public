from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from itertools import product
import time,json,sys,hashlib
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0;local=0;updates=0;trees=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
 if time.monotonic()-start>55:raise TimeoutError('frozen55seconds')
def atanh(x):
 z=x*x;t=x;s=F(0)
 for j in range(20):s+=t/(2*j+1);t*=z
 return 2*s,2*s+2*t/(41*(1-z))
ln2=atanh(F(1,3));GRID=1<<100
@lru_cache(None)
def log(x):
 ck(x>0);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=atanh((x-1)/(x+1));lo=F(k)+lo/ln2[1];hi=F(k)+hi/ln2[0]
 return F((lo*GRID).__floor__(),GRID),F((hi*GRID).__ceil__(),GRID)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(x,t):return (x[0]*t,x[1]*t) if t>=0 else (x[1]*t,x[0]*t)
Z=(F(0),F(0))
def avg(x,y):return mul(add(x,y),F(1,2))
def overlaps_zero(x):ck(x[0]<=0<=x[1])
def ce(P,Q):
 ans=Z
 for p,q in zip(P,Q):
  if p:ck(q>0);ans=add(ans,mul(log(1/q),p))
 return ans
def D(P,Q):
 if P==Q:return Z
 out=Z
 for p,q in zip(P,Q):
  if p:ck(q>0);out=add(out,mul(log(p/q),p))
 return out
def H(P):return ce(P,P)
@lru_cache(None)
def spectrum(n,table):
 a=[F(1 if table>>j&1 else -1) for j in range(1<<n)]
 for b in range(n):
  for j in range(1<<n):
   if not j>>b&1:
    v,w=a[j],a[j|(1<<b)];a[j],a[j|(1<<b)]=v+w,v-w
 return tuple((v/(1<<n))**2 for v in a)
@lru_cache(None)
def influence(n,table):
 return sum((F((bool(table>>j&1)!=bool(table>>(j^(1<<b))&1)),1<<n) for j in range(1<<n) for b in range(n)),F(0))
def child(n,table,i,b):
 out=0
 for y in range(1<<(n-1)):
  x=(y&((1<<i)-1))|((y>>i)<<(i+1))|(b<<i)
  out|=((table>>x)&1)<<y
 return out
def projection(Q,n,i):
 out=[F(0)]*(1<<(n-1))
 for j,q in enumerate(Q):out[(j&((1<<i)-1))|((j>>(i+1))<<i)]+=q
 return tuple(out)
def groups(n,kind):
 if kind==0:return tuple(int(j!=0) for j in range(1<<n))
 if kind==1:return tuple(j.bit_count()%2 for j in range(1<<n))
 return tuple(range(1<<n))
def convert(P,Q,labels,t):
 global updates
 updates+=1;ps={};qs={}
 for p,q,l in zip(P,Q,labels):ps[l]=ps.get(l,F(0))+p;qs[l]=qs.get(l,F(0))+q
 rs={l:(1-t)*qs[l]+t*ps[l] for l in qs}
 R=tuple(q*rs[l]/qs[l] if qs[l] else F(0) for q,l in zip(Q,labels))
 ck(sum(R)==1);ck(all(not p or r>0 for p,r in zip(P,R)))
 fee=D(R,Q);excess=sub(sub(D(P,Q),D(P,R)),fee)
 if t==0 or t==1 or R==Q:overlaps_zero(excess);cert=Z
 else:
  cert=mul(add(D(tuple(rs.values()),tuple(qs.values())),D(tuple(qs.values()),tuple(rs.values()))),(1-t)/t)
  overlaps_zero(sub(excess,cert));ck(cert[0]>0)
 return R,fee,cert
def refs(P):
 N=len(P);u=tuple([F(1,N)]*N)
 return [P,u,tuple((p+q)/2 for p,q in zip(P,u)),tuple(F(3,4)*int(i==0)+F(1,4)*q for i,q in enumerate(u))]
def query(n,table,Q,i):
 global local
 local+=1;P=spectrum(n,table);Qp=projection(Q,n,i);Pm=projection(P,n,i)
 t0,t1=child(n,table,i,0),child(n,table,i,1);P0=spectrum(n-1,t0);P1=spectrum(n-1,t1)
 ck(tuple((x+y)/2 for x,y in zip(P0,P1))==Pm)
 L=sub(D(P,Q),D(Pm,Qp));J=avg(D(P0,Pm),D(P1,Pm))
 overlaps_zero(sub(sub(avg(D(P0,Qp),D(P1,Qp)),D(P,Q)),sub(J,L)))
 If= influence(n,table)-(influence(n-1,t0)+influence(n-1,t1))/2
 ck(If>=0)
 if If:ck(J[1] <= F(2)*If/ln2[0]);ck(3*If-J[1]>0)
 else:ck(P0==P1);ck(J==Z)
 # KL contraction is exact sum of occupied conditional-pair divergences.
 cond=Z
 for j,m in enumerate(Pm):
  if not m:continue
  idx=(j&((1<<i)-1))|((j>>i)<<(i+1));p=(P[idx]/m,P[idx|(1<<i)]/m)
  r=(Q[idx]/Qp[j],Q[idx|(1<<i)]/Qp[j]);cond=add(cond,mul(D(p,r),m))
 overlaps_zero(sub(L,cond))
 return t0,t1,Qp,L,J,If
def history(n,table,Q,depth=0):
 P=spectrum(n,table)
 # An outcome-dependent order; the current truth table controls the next coordinate.
 if n==0:return ce(P,Q),F(0),Z
 i=(table.bit_count()+depth)%n
 t0,t1,Qp,L,J,If=query(n,table,Q,i)
 bills=[];spent=[];certs=[]
 for b,tb in enumerate([t0,t1]):
  Pb=spectrum(n-1,tb);labels=groups(n-1,(depth+b)%3);alpha=[F(1),F(1,2),F(1,4)][(table+b+depth)%3]
  R,fee,paygap=convert(Pb,Qp,labels,alpha)
  bill,jspent,certificate=history(n-1,tb,R,depth+1)
  bills.append(add(fee,bill));spent.append(jspent);certs.append(add(paygap,certificate))
 release=add(sub(H(P),avg(H(spectrum(n-1,t0)),H(spectrum(n-1,t1)))),L)
 return add(release,avg(*bills)),If+sum(spent)/2,add(sub((3*If,3*If),J),avg(*certs))
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';maxn=2 if mode=='pilot' else 3
batch=int(sys.argv[2]) if mode=='batch' else None
case_index=-1;selected=0
for n in range(maxn+1):
 for table in range(1<<(1<<n)):
  case_index+=1
  if batch is not None and not batch*32<=case_index<(batch+1)*32:continue
  selected+=1
  P=spectrum(n,table);ck(sum(P)==1)
  for Q in refs(P):
   ck(sum(Q)==1)
   for i in range(n):query(n,table,Q,i)
   for kind in range(3):
    for t in [F(0),F(1,4),F(1,2),F(1)]:convert(P,Q,groups(n,kind),t)
   bill,spent,certificate=history(n,table,Q);ck(spent==influence(n,table))
   overlaps_zero(sub(sub(add(ce(P,Q),(3*spent,3*spent)),bill),certificate))
   if spent:ck(certificate[0]>0)
   else:ck(certificate[1]>=0) # Exact zero handled componentwise above, overlap only diagnostic.
   for s in [F(1),F(1,2)]:
    SQ=tuple(s*q for q in Q);fee=log(1/s);overlaps_zero(sub(add(ce(P,Q),fee),ce(P,SQ)))
    actual=add(bill,fee);bound=add(ce(P,SQ),(3*spent,3*spent))
    overlaps_zero(sub(sub(bound,actual),certificate));trees+=1
# Explicit infinite-interface negative control: true-kernel versus projected AND2 child.
P=spectrum(2,8);ck(P==tuple([F(1,4)]*4));ck(projection(P,2,0)==(F(1,2),F(1,2)))
ck(spectrum(1,child(2,8,0,0))==(F(1),F(0)))
# Bank coefficients and exact geometric finite-domain certificate.
e=F(15,4096);smax=F(151,8192)
ck(4*(1-e)-F(135,92)-1==F(35751,23552))
ck(12*(1-e)-320*smax-F(37,8)==F(1467,1024));ck(F(1467,1024)>1)
width_cases=0
for a in range(1,25):
 for b in range(12,25):
  L=a+b;lowerI=F(a,1<<(a-1));S=F(9*L+34,1<<L);E=F(2*(L+2),1<<L)
  ck(S/lowerI<=smax);ck(E/lowerI<=e)
for length in range(5):
 for widths in product([1,2,3],repeat=length):
  d=13;S=F(0);E=F(0)
  for j,r in enumerate(widths,1):
   d+=r;S+=F((1+j*(j+1))*d,1<<d);E+=F(2*d,1<<d)
  ck(S<=smax);ck(E<=e);width_cases+=1
out={'mode':mode,'batch':batch,'truth_tables':selected,'local_queries_including_tree_reuse':local,'profile_updates_including_tree_reuse':updates,'mass_aware_histories':trees,'scalar_width_cases':width_cases,'assertions':checks,'seconds':time.monotonic()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sign_convention':'Signs certified componentwise; identity interval overlaps are diagnostics, not standalone equality certificates'}
name=('BATCH_'+str(batch).zfill(2) if batch is not None else mode.upper())+'.json'
ROOT.joinpath('out',name).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
