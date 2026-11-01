from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0;GRID=1<<120
def ck(x):
 global CHECKS
 assert x
 CHECKS+=1
 if time.perf_counter()-START>55:raise TimeoutError('frozen 55 second cap')
def floor(x):return F(x.numerator//x.denominator,GRID)
def quant(lo,hi):return (floor(lo*GRID),-floor(-hi*GRID))
def add(*args):return quant(sum((a for a,b in args),F(0)),sum((b for a,b in args),F(0)))
def neg(v):return (-v[1],-v[0])
def scale(v,a):return quant(v[0]*a,v[1]*a) if a>=0 else quant(v[1]*a,v[0]*a)
def exact(a):return (F(a),F(a))
def lnraw(x):
 z=(x-1)/(x+1);z2=z*z;power=z;s=F(0)
 for j in range(48):s+=power/(2*j+1);power*=z2
 return 2*s,2*s+2*power/(97*(1-z2))
LN2=lnraw(F(2))
@lru_cache(None)
def log(x):
 x=F(x);assert x>0;k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=lnraw(x)
 return quant(k+lo/LN2[1],k+hi/LN2[0])
def logrange(a,b):return log(a)[0],log(b)[1]
def plog(x):return scale(log(x),x) if x else exact(0)
def hb(x):return neg(add(plog(x),plog(1-x)))
def hp(r):
 if r<=1:return exact(0)
 d=F(1,1<<r);p=(1-2*d)**2
 return add(hb(p),scale(log((1<<r)-1),1-p))
def entropy(p):return neg(add(*(plog(x) for x in p.values() if x)))
def spectrum(t):
 a=list(t);N=len(a);n=N.bit_length()-1;k=1
 while k<N:
  for b in range(0,N,2*k):
   for j in range(b,b+k):u,v=a[j],a[j+k];a[j],a[j+k]=u+v,u-v
  k*=2
 p={s:F(x*x,N*N) for s,x in enumerate(a) if x};ck(sum(p.values())==1)
 ds=[sum((v for s,v in p.items() if s>>j&1),F(0)) for j in range(n)]
 for j in range(n):ck(ds[j]==F(sum(t[x]!=t[x^(1<<j)] for x in range(N)),N))
 return p,ds
def restrict(t,j,b):return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def table(m,r):
 def core(z):
  a=1
  for j in range(m):
   if (z>>(r*j))&((1<<r)-1)==(1<<r)-1:a=-a
  return a
 return tuple(1-2*((u>>1)&1) if not u&1 else core(u>>3) if u&4 else 1 for u in range(1<<(3+m*r)))
def bracket(v,ds):
 def poly(c):
  prod=F(1)
  for d,n in ds:prod*=(1-c*d/v)**n
  return 1-c-prod
 lo=F(1,2);hi=F(1);ck(poly(lo)>0 and poly(hi)<0)
 for _ in range(56):
  mid=(lo+hi)/2
  if poly(mid)>0:lo=mid
  else:hi=mid
 ck(poly(lo)>0 and poly(hi)<0)
 return lo,hi
def certify(m,r):
 delta=F(1,1<<r);mu=(1-2*delta)**m;t=(1-mu)/2;p0=(1-t)**2/4;v=1-p0
 groups=[(F(1,2),2),(t/2,1),(delta/2,m*r)]
 ds=[d for d,n in groups for _ in range(n)];lo,hi=bracket(v,groups)
 terms=[neg(plog(p0)),scale(logrange(v/hi,v/lo),-v)]
 for d,n in groups:
  terms.extend([scale(logrange(lo*d/v,hi*d/v),-n*d),scale(logrange(1-hi*d/v,1-lo*d/v),-n*(v-d))])
 CE=add(*terms);G=add(*(scale(hb(d),n) for d,n in groups),exact(-2))
 Hcore=scale(hp(r),m)
 H0=add(exact(1),scale(plog(p0),-2),scale(plog(t*t/4),-2),scale(add(Hcore,plog(mu*mu)),F(1,4)),exact(1-mu*mu))
 Hf=add(exact(2),scale(hp(r),F(m-1,4)),scale(hp(r-1),F(1,8)))
 I0=1+t/2+F(m*r,2)*delta;If=1+F(m*r-1,2)*delta;rem=t/2+delta/2
 ck(I0-If==rem)
 S=add(exact(4*If),neg(Hf));A=add(CE,neg(H0));edge=add(H0,neg(Hf),exact(-4*rem))
 # max interval is valid also when edge crosses zero.
 L=add(A,(max(F(0),edge[0]),max(F(0),edge[1])))
 remain=add(S,neg(L));excess=add(CE,exact(-4*I0))
 ck(A[0]>=0 and S[0]>=2)
 # Exact global ledger identity independent of the edge sign.
 identity=add(S,neg(A),neg(edge),CE,exact(-4*I0));ck(identity[0]<=0<=identity[1] and identity[1]-identity[0]<F(1,1<<35))
 if m<=3 and m*r<=6:
  tt=table(m,r);p,di=spectrum(tt);ck(di==ds and p[0]==p0)
  actual=entropy(p);ck(actual[0]<=H0[1] and H0[0]<=actual[1])
  leaves=[(restrict(tt,2,0),F(1,2))]
  bb=restrict(tt,2,1)
  leaves.extend([(restrict(bb,2,b),F(1,4)) for b in (0,1)])
  HH=exact(0);II=F(0)
  for leaf,w in leaves:
   pp,dd=spectrum(leaf);HH=add(HH,scale(entropy(pp),w));II+=w*sum(dd)
  ck(II==If and HH[0]<=Hf[1] and Hf[0]<=HH[1])
  # Both data restrictions nonconstant, verified on actual data truth table.
  cc=tuple(__import__('functools').reduce(lambda a,j:a*(-1 if (z>>(r*j))&((1<<r)-1)==(1<<r)-1 else 1),range(m),1) for z in range(1<<(m*r)))
  ck(all(len(set(restrict(cc,0,b)))==2 for b in (0,1)))
 if (m,r)==(2,3):ck(G[0]>S[1] and remain[0]>1)
 if (m,r)==(64,2):ck(excess[0]>1 and remain[1]<-1)
 if (m,r)==(128,2):ck(excess[0]>4)
 def serial(v):return [str(x) for x in v]
 row={'m':m,'r':r,'physical_dimension':3+m*r,'canonical_root_bracket':serial((lo,hi)),'G':serial(G),'CE':serial(CE),'H0':serial(H0),'Hf':serial(Hf),'I0':str(I0),'If':str(If),'R':str(rem),'source_KL':serial(A),'signed_query_deficit':serial(edge),'same_unused_S':serial(S),'full_liability':serial(L),'remaining':serial(remain),'CE_minus_4I':serial(excess),'decimal_display_only':{k:[float(x) for x in val] for k,val in [('G',G),('CE',CE),('H0',H0),('Hf',Hf),('S',S),('liability',L),('remaining',remain),('CE_minus_4I',excess)]}}
 (R/f'out/CERT_m{m}_r{r}.json').write_text(json.dumps(row,indent=2),encoding='utf-8')
 return row
cases=[(2,3),(64,2)] if '--pilot' in sys.argv else [(2,2),(2,3),(3,2),(16,2),(32,2),(64,2),(128,2)]
rows=[certify(m,r) for m,r in cases]
# Limiting canonical CE coefficient exceeds1 by an exact rational-log certificate.
alpha=add(scale(log(F(15,2)),F(1,4)),scale(log(F(15,13)),F(13,8)))
ck(alpha[0]>F(21,20))
result={'status':'PASS','rung':'exact interval certificates plus analytic derivation; no Lean claim','cases':len(rows),'assertions':CHECKS,'runtime_seconds':time.perf_counter()-START,'alpha_interval':[str(x) for x in alpha],'alpha_decimal_display':[float(x) for x in alpha],'case_displays':[{'m':x['m'],'r':x['r'],**x['decimal_display_only']} for x in rows]}
(R/('out/PILOT.json' if '--pilot' in sys.argv else 'out/CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
