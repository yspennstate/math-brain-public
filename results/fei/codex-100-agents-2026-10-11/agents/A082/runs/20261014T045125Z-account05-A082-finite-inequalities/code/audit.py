from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import sys,time,json
ROOT=Path(__file__).resolve().parents[1]
t0=time.perf_counter(); assertions=0
pilot='--pilot' in sys.argv
def ck(x):
 global assertions
 assertions+=1
 assert x, assertions
 assert time.perf_counter()-t0 < (55 if pilot else 180)
def ln_unit(x):
 z=(x-1)/(x+1); s=Q(0)
 for j in range(24): s+=2*z**(2*j+1)/(2*j+1)
 return s,s+2*z**49/(49*(1-z*z))
LN2=ln_unit(Q(2))
@lru_cache(maxsize=20000)
def log2(x):
 ck(x>0); k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=ln_unit(x)
 return Q(k)+lo/LN2[1],Q(k)+hi/LN2[0]
def entropy(p):
 lo=hi=Q(0)
 for a in p:
  if a:
   l,h=log2(1/a);lo+=a*l;hi+=a*h
 return lo,hi
def direct(t):
 return [Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def influences(t):
 return [Q(sum(v!=t[x^(1<<j)] for x,v in enumerate(t)),len(t)) for j in range(len(t).bit_length()-1)]
def table(n,m):return [1 if (m>>x)&1 else -1 for x in range(1<<n)]
def KL(u,q):
 lo=hi=Q(0)
 for a,b in zip(u,q):
  if a:
   l,h=log2(a/b);lo+=a*l;hi+=a*h
 return lo,hi
cases=0;rows=0;max_loss=Q(0)
for d in [1,2,3]:
 for bm in range(1,1<<(1<<d),2):
  b=table(d,bm);c=b[:];c[0]=-1;beta=direct(b);Ib=sum(influences(b));Ic=sum(influences(c));delta=Q(1,1<<d)
  for r in [1,2]:
   for gm in range(1<<(1<<r)):
    if pilot and cases>=20:break
    g=table(r,gm);a=direct(g);eg=influences(g)
    parent=[g[x>>d] if x%len(b)==0 else b[x%len(b)] for x in range(1<<(d+r))]
    A=direct(parent);e=influences(parent)
    ck(sum(v*v for v in A)==1)
    IX=sum(e[d:]);IY=sum(e[:d]);ck(IX==delta*sum(eg));ck(IY==((1+a[0])*Ib+(1-a[0])*Ic)/2)
    for V in range(1<<r):
     for T in range(1<<d):ck(A[T+(V<<d)]==(beta[T] if V==0 else 0)+delta*(a[V]-(1 if V==0 else 0)))
    upper=Q(0)
    for i in range(r):
     ck(abs(a[1<<i])<=eg[i]);ck(e[d+i]==delta*eg[i])
     if not eg[i]:continue
     rows+=1;rho=1-delta+delta*(a[0]**2+a[1<<i]**2)
     mu=[];ref=[];ug=[];qg=[]
     for V in range(1<<r):
      if V&(1<<i):continue
      uv=[];qv=[]
      for T in range(1<<d):
       p=A[T+(V<<d)]**2;pu=A[T+((V|(1<<i))<<d)]**2
       uv.append(pu/e[d+i]);qv.append(p+pu)
      mu.extend(uv);ref.extend(qv);ug.append(sum(uv));qg.append(sum(qv))
      if V==0:
       ck(sum(qv)==rho)
       if a[1<<i]:
        q=[v/rho for v in qv];ck(sum(q)==1)
        for T,v in enumerate(q):ck(v==((beta[T]+delta*(a[0]-1))**2+delta**2*a[1<<i]**2)/rho)
        l,h=KL([delta]*len(b),q);upper+=delta*a[1<<i]**2*h
       else:l=h=Q(0)
      else:
       # Nonexceptional conditional laws coincide; zero derivative cells require no division.
       if sum(uv):
        ck(all(u*sum(qv)==q*sum(uv) for u,q in zip(uv,qv)))
     ck(sum(mu)==sum(ref)==1)
     # Chain rule replay with independent interval arithmetic.
     fl,fh=KL(mu,ref);ql,qh=KL(ug,qg)
     expected_lo=delta*a[1<<i]**2*l;expected_hi=delta*a[1<<i]**2*h
     ck(e[d+i]*(fl-qh)<=expected_hi and e[d+i]*(fh-ql)>=expected_lo)
    budget=2*IY+Q(9,8)*IX
    ck(upper<=budget)
    if Ib and Ic:ck(upper<=IY/2+Q(9,8)*IX)
    cases+=1
    if cases%100==0:(ROOT/'out/CHECKPOINT.json').write_text(json.dumps({'cases':cases,'assertions':assertions}))
   if pilot and cases>=20:break
  if pilot and cases>=20:break
 if pilot and cases>=20:break
bank=[]
if not pilot:
 ck(cases==2760)
 ck(LN2[0]>Q(2,3))
 # exp(1)>1+1+1/2+1/6+1/24=65/24>8/3; hence 2/(e ln2)<9/8.
 ck(Q(65,24)>Q(8,3))
 for d in [2,3,4,8,16,32,64]:
  delta=Q(1,1<<d);p0=(1-2*delta)**2;z=(1-delta)**2+delta**2
  el,eh=entropy([p0]);Hl=el+4*delta*(1-delta)*(2*d-2);Hh=eh+4*delta*(1-delta)*(2*d-2)
  l,h=log2(delta/z);Dl=(1-delta)*(d-1)+delta*l;Dh=(1-delta)*(d-1)+delta*h
  ck(Dl>=d-2);ck(Dh<=d);ck(Hh<=8*d*delta)
  S4l=4*d*delta-Hh/2;S4h=4*d*delta-Hl/2
  ck(S4l>=0);ck(S4h<=5*delta);ck(S4l+d*delta>=delta*Dh)
  for C in [Q(4),Q(9,2),Q(19,4)]:ck(Dl-(S4h+(C-4)*d*delta)/delta>=(5-C)*d-7)
  bank.append({'d':d,'D0_interval':[str(Dl),str(Dh)],'S4_over_e_interval':[str(S4l/delta),str(S4h/delta)]})
result={'status':'PASS','cases':cases,'gate_rows':rows,'assertions':assertions,'runtime_seconds':time.perf_counter()-t0,'log_terms':24,'bank_certificates':bank,'arithmetic':'direct character sums and physical edges; rational log intervals; no floating sign decisions'}
(ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='bank_certificates'}))
