from pathlib import Path
from fractions import Fraction as R
from functools import lru_cache
import json,time,sys
root=Path(__file__).resolve().parents[1]; mode=sys.argv[1]; start=time.monotonic(); checks=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if time.monotonic()-start>55:raise TimeoutError('frozen55s')
def plus(*vs):
 d={}
 for v in vs:
  for p,c in v.items():d[p]=d.get(p,R(0))+c
 return {p:c for p,c in d.items() if c}
def scale(v,c):return {p:c*x for p,x in v.items() if c*x}
@lru_cache(maxsize=4096)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def lv(x):
 ck(x>0)
 return plus({p:R(k) for p,k in factors(x.numerator).items()},{p:R(-k) for p,k in factors(x.denominator).items()})
def KL(p,q):
 z={}
 for a,b in zip(p,q):
  if a:ck(b>0);z=plus(z,scale(lv(a/b),a))
 return z
def CE(p,q):
 z={}
 for a,b in zip(p,q):
  if a:ck(b>0);z=plus(z,scale(lv(b),-a))
 return z
def entropy(p):return CE(p,p)
@lru_cache(maxsize=2048)
def ln_bounds(x):
 k=0
 while x>2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def series(t):
  z=(t-1)/(t+1);z2=z*z;term=z;s=R(0)
  for j in range(24):s+=2*term/(2*j+1);term*=z2
  return s,s+2*term/(49*(1-z2))
 a,b=series(x);c,d=series(R(2))
 return a+k*(c if k>=0 else d),b+k*(d if k>=0 else c)
def bounds(v):
 a=b=R(0)
 for p,c in v.items():
  l,h=ln_bounds(R(p));a+=c*(l if c>=0 else h);b+=c*(h if c>=0 else l)
 l,h=ln_bounds(R(2))
 return (a/h if a>=0 else a/l),(b/l if b>=0 else b/h)
def nonneg(v):return not v or bounds(v)[0]>=0
def walsh(t):
 a=list(t);s=1
 while s<len(a):
  for z in range(0,len(a),2*s):
   for j in range(s):u,v=a[z+j],a[z+j+s];a[z+j],a[z+j+s]=u+v,u-v
  s*=2
 return [R(x,len(a)) for x in a]
def influences(t):return [R(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)]
rows=[]
for m in ([2] if mode=='pilot' else [2,3,4,5]):
 L=2**m;u=R(1,L*L);N=L*L
 G=[1-2*int((x&(L-1))==(x>>m)) for x in range(N)]
 H=[(-1 if ((x&(L-1))&(x>>m)).bit_count()%2 else 1) for x in range(N)]
 F=[G[x>>1] if x%2==0 else H[x>>1] for x in range(2*N)]
 ag,ah,af=walsh(G),walsh(H),walsh(F);pg=[x*x for x in ag];ph=[x*x for x in ah];pf=[x*x for x in af]
 q=[(g+h)/2 for g,h in zip(pg,ph)];Q=[u/2]*(2*N)
 p0=R((L-2)**2,L*L);A=R((L-2)**2,(L-2)**2+1);D=A+R(4*(L-1),5)
 ck(all(x==u for x in ph));ck(pg[0]==p0)
 for s in range(L):
  for t in range(L):
   i=s+L*t;ck(pg[i]==(p0 if i==0 else 4*u if s==t else 0))
 rg=sum(u*p/(p+u) for p in pg);rh=1-rg
 ck(rg==D/(L*L));ck(0<rg<1);ck(rg!=R(1,2))
 qg=[u*p/(p+u)/rg for p in pg];qh=[u*u/(p+u)/rh for p in pg]
 ck(sum(qg)==sum(qh)==1)
 for i in range(N):
  ck(qg[i]==(A/D if i==0 else R(4,5)/D if pg[i] else 0))
  ck(qg[i]*rg+qh[i]*rh==u)
 ig,ih,iff=influences(G),influences(H),influences(F)
 ck(sum(ig)==R(4*m,L));ck(sum(ih)==m)
 ck(iff[0]==R(L-1,2*L));ck(sum(iff)==R(m+1,2)+R(4*m-1,2*L))
 ck(R(sum(g*h for g,h in zip(G,H)),N)==R(1,L))
 hf,hg,hh=entropy(pf),entropy(pg),entropy(ph)
 cf,cg,ch=CE(pf,Q),CE(pg,qg),CE(ph,qh)
 ck(cf=={2:R(2*m+1)})
 E=plus(KL(pf,Q),scale(KL(q,[u]*N),-1));O=KL([R(1,2)]*2,[rg,rh]);delta=plus(hf,scale(plus(hg,hh),R(-1,2)))
 ck(nonneg(E));ck(nonneg(O));ck(nonneg(delta))
 ck(cf==plus(delta,E,O,scale(plus(cg,ch),R(1,2))))
 dF=plus(cf,{2:-4*sum(iff)});dG=plus(cg,{2:-4*sum(ig)});dH=plus(ch,{2:-4*sum(ih)})
 ck(dF==plus(scale(plus(dG,dH),R(1,2)),delta,E,O,{2:-4*iff[0]}))
 margin=4*sum(iff)-R(1,8)-(2*m+1)
 ck(margin==R(7,8)+R(8*m-2,L));ck(margin>R(7,8))
 ck(all(x<=R(5,4*L) for x in qg))
 ck(bounds(plus(cg,{2:-R(2*m-1,2)}))[0]>0)
 ck(bounds(plus({2:R(2*m+1)},scale(ch,-1)))[0]>0)
 if m>=5:ck(bounds(dG)[0]>0)
 ck(bounds(dH)[1]<0)
 # Explicit invertible nonempty diagonal minor; vacuum changes cannot affect it.
 ck(all(qg[s+L*s]>0 for s in range(1,L)))
 ck(all(qg[s+L*t]==0 for s in range(1,L) for t in range(1,L) if s!=t))
 for x in [R(1,2),R(1),R(2)]:
  tilted=[qg[i]*x**i.bit_count() for i in range(N)];z=sum(tilted[1:]);rho=pg[0]
  projected=[rho]+[(1-rho)*v/z for v in tilted[1:]]
  ck(sum(projected)==1);ck(all(projected[s+L*s]>0 for s in range(1,L)))
 # Forward fee of replacing the inherited sparse child by uniform projection is infinite.
 bad=[i for i in range(N) if qg[i]==0 and u>0];ck(len(bad)==L*L-L)
 rows.append({'m':m,'rank_lower_bound_with_signed_vacuum':L-1,'I_root':str(sum(iff)),'old_debit':str(R(1,8)),'original_rate4_reserve':str(margin),'reference_branch_G':str(rg),'G_deficit_interval':[str(x) for x in bounds(dG)],'H_deficit_interval':[str(x) for x in bounds(dH)]})
compressed=[]
for m in range(2,33):
 L=2**m;A=R((L-2)**2,(L-2)**2+1);D=A+R(4*(L-1),5)
 ck(A>=R(4,5));ck(R(4*L,5)<=D<=L);ck(2*m<=L)
 ck(R(7,8)+R(8*m-2,L)>R(7,8))
 if m>=5:ck(R(16*m,L)<=R(m,2))
 compressed.append({'m':m,'minor_size':L-1,'positive_uniform_bound':str(R(5,4*L))})
m=10;L=2**m;u=R(1,L*L);p0=R((L-2)**2,L*L)
pg3=[p0,4*(L-1)*u,R(0)];ph3=[u,(L-1)*u,1-R(1,L)];q3=[(a+b)/2 for a,b in zip(pg3,ph3)]
ck(sum(pg3)==sum(ph3)==sum(q3)==1)
JS=scale(plus(KL(pg3,q3),KL(ph3,q3)),R(1,2))
excess=plus(JS,{2:-R(7,8)-R(8*m-2,L)})
ck(bounds(excess)[0]>R(87,2048))
ck(bounds(plus({2:R(1)+R(8*m-2,L)},scale(JS,-1)))[0]>0)
for m in range(10,33):ck(2**m>68*m-4)
out={'status':'PASS','mode':mode,'truth_table_cases':len(rows),'exact_assertions':checks,'seconds':time.monotonic()-start,'cases':rows,'compressed_certificates':compressed,'projection_m10_excess_interval':[str(x) for x in bounds(excess)],'rung':'finite exact validation plus all-m analytic proof; not peer/Lean acceptance'}
(root/'out'/f'{mode}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['cases','compressed_certificates']}))
