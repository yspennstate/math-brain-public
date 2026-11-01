from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; N=0
def ck(x):
 global N
 N+=1
 assert x,N
def fw(t):
 a=list(t); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(k):
    u,v=a[i+j],a[i+j+k]; a[i+j],a[i+j+k]=u+v,u-v
  k*=2
 return {s:F(v,len(a)) for s,v in enumerate(a) if v}
def add(*xs):
 r={}
 for d in xs:
  for k,v in d.items(): r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def scale(d,c): return {k:v*c for k,v in d.items() if v*c}
@lru_cache(None)
def log(q):
 q=F(q); assert q>0; r={}
 for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
  d=2
  while d*d<=n:
   while n%d==0: r[d]=r.get(d,0)+sgn; n//=d
   d+=1
  if n>1: r[n]=r.get(n,0)+sgn
 return {k:F(v) for k,v in r.items() if v}
def H(p): return add(*(scale(log(v),-v) for v in p.values() if v))
def CE(p,q): return add(*(scale(log(q[k]),-v) for k,v in p.items() if v))
def KL(p,q): return add(CE(p,q),scale(H(p),-1))
def unit(q):
 z=(q-1)/(q+1); z2=z*z; power=z; s=F(0)
 for k in range(48): s+=2*power/F(2*k+1); power*=z2
 e=2*abs(power)/(97*(1-z2)); return s-e,s+e
L2=unit(F(2))
@lru_cache(None)
def ln(q):
 q=F(q); k=0
 while q>=2: q/=2; k+=1
 while q<1: q*=2; k-=1
 lo,hi=unit(q)
 return lo+k*(L2[0] if k>=0 else L2[1]),hi+k*(L2[1] if k>=0 else L2[0])
def interval(expr):
 lo=hi=F(0)
 for q,v in expr.items():
  a,b=ln(q); lo+=v*(a if v>=0 else b); hi+=v*(b if v>=0 else a)
 return lo,hi
def spec(t): return {s:v*v for s,v in fw(t).items()}
TABLES=[[1 if w>>x&1 else -1 for x in range(4)] for w in range(16)]
def ref(j,mass=F(1)):
 return {s:mass*F(1+(j%2),3)**s.bit_count()*F(2-(j%2),3)**(2-s.bit_count()) for s in range(4)}
def calibrate(R,p):
 e=p.get(0,F(0)); out={0:e}
 if e<1:
  for s,v in R.items():
   if s: out[s]=(1-e)*v/(1-R[0])
 return {s:v for s,v in out.items() if v}
def activation():
 cases=0
 for n in range(1,4):
  for w in range(1<<(1<<n)):
   if w.bit_count()!=1<<(n-1): continue
   t=[1 if w>>x&1 else -1 for x in range(1<<n)]; g=fw(t); pg=spec(t)
   for r in range(1,(5 if n<3 else 3)+1):
    p=F(1,2**r); mask=(1<<r)-1
    true=spec([t[x>>r] if x&mask==0 else 1 for x in range(1<<(r+n))])
    # Independently recurse the original physical-leaf sampler; keep J and S.
    c={s<<r:v for s,v in g.items()}; joint={(r+1,s<<r):v for s,v in pg.items()}
    for j in reversed(range(r)):
     u=c; v={0:F(1)}; nxt={}; nj={}
     for T in set(u)|set(v):
      a,b=u.get(T,0),v.get(T,0)
      for bit,coeff in [(0,(a+b)/2),(1,(a-b)/2)]:
       if coeff: nxt[T|(bit<<j)]=coeff
     for branch in [joint,{(j+1,0):F(1)}]:
      for (J,T),m in branch.items():
       a,b=u.get(T,0),v.get(T,0); eps=(a-b)**2/(2*(a*a+b*b))
       for bit,prob in [(0,1-eps),(1,eps)]:
        key=J,T|(bit<<j); nj[key]=nj.get(key,0)+m*prob/2
     c=nxt; joint={k:v for k,v in nj.items() if v}
    marginal={}
    for (J,S),v in joint.items(): marginal[S]=marginal.get(S,0)+v
    ck(marginal==true); ck(sum(joint.values())==1)
    eps=[]; B={}
    for k in range(1,r+1):
     m=1-F(1,2**(k-1)); q=(1+m*m)/2; e=(1-m)**2/(2*(1+m*m)); eps.append(e)
     B=add(B,scale(H({0:e,1:1-e}),F(1,2**(r-k))*q),{2:F(1,2**(r-k))*(1-m*m)/2})
    closed={}
    for J in range(1,r+1):
     for U in range(1<<J):
      if not U:
       prob=F(1,2**J)
       for i in range(1,J+1): prob*=1-eps[r-i]
      else:
       m=U.bit_length(); prob=F(1,2**J)*eps[r-m]*F(1,2**(m-1))
       for i in range(m+1,J+1): prob*=1-eps[r-i]
      if prob: closed[J,U]=prob
    for T,m in pg.items():
     for U in range(1<<r): closed[r+1,U|(T<<r)]=p*p*m
    ck(joint==closed)
    A=add({2:2*r*p*(2-p)},scale(log((1-p)**2),-(1-p)**2))
    ck(add(H(joint),scale(H(true),-1))==add({2:2*(1-p)},B,scale(A,-1)))
    for R in [pg,{s:F(1,(1<<n)-1) for s in range(1,1<<n)},{s:F(1,2*((1<<n)-1)) for s in range(1,1<<n)}]:
     Q={0:(1-p)**2}
     for U in range(1,1<<r): Q[U]=p*p
     for T,v in R.items():
      for U in range(1<<r): Q[U|(T<<r)]=p*p*v
     ck(sum(Q.values())==1-p+p*sum(R.values()))
     ck(CE(true,Q)==add(scale(CE(pg,R),p),A))
     ck(KL(true,Q)==scale(KL(pg,R),p))
    cases+=1
 coeff=[]
 for r in range(1,6):
  p=F(1,2**r); coeff.append(add({2:2*(2-p)},scale(log((1-p)**2),-(1-p)**2/(r*p))))
 for i in [0,1,3,4]: ck(interval(add(coeff[2],scale(coeff[i],-1)))[0]>0)
 ck(interval(add(coeff[2],{2:F(-9,2)}))[0]>0)
 ck(L2[0]>F(2,3)); ck(4+2/(6*L2[0])<F(9,2))
 ck(interval(add(coeff[2],{2:-F(4536,1000)}))[0]>0)
 ck(interval(add(coeff[2],{2:-F(4537,1000)}))[1]<0)
 return {'activation_pairs':cases,'reference_variants':3,'sharp_r':3,'C_act_interval':['4.536','4.537']}
def comb_table(leaves):
 a=len(leaves)-1; mask=(1<<a)-1
 return [leaves[next((j for j in range(a) if not (x>>j)&1),a)][x>>a] for x in range(1<<(a+2))]
def comb():
 general=equal=scalar=0
 tuples=list(product(range(16),repeat=2))+[(i,j,(i+j)%16) for i,j in product(range(16),repeat=2)]
 for ids in tuples:
  a=len(ids)-1; leaves=[TABLES[i] for i in ids]; spectra=[fw(t) for t in leaves]; ps=[spec(t) for t in leaves]
  w=[F(1,2**(j+1)) for j in range(a)]+[F(1,2**a)]
  actual=fw(comb_table(leaves)); P={s:v*v for s,v in actual.items()}
  suffix=spectra[-1].copy(); expected={}
  for j in reversed(range(a)):
   for T in set(spectra[j])|set(suffix):
    diff=(spectra[j].get(T,0)-suffix.get(T,0))/2**(j+1)
    for low in range(1<<j):
     if diff: expected[(T<<a)|(1<<j)|low]=diff*(-1)**low.bit_count()
   suffix={T:(spectra[j].get(T,0)+suffix.get(T,0))/2 for T in set(spectra[j])|set(suffix)}
  expected.update({T<<a:v for T,v in suffix.items() if v}); ck(actual==expected)
  q={T:sum(w[j]*ps[j].get(T,0) for j in range(a+1)) for T in range(4)}; q={T:v for T,v in q.items() if v}
  ck(q=={T:sum(v for s,v in P.items() if s>>a==T) for T in q})
  R=[ref(j,F(1,2) if j%2 else F(1)) for j in range(a+1)]; mix={T:sum(w[j]*R[j][T] for j in range(a+1)) for T in range(4)}
  Q={s:mix[s>>a]*v/q[s>>a] for s,v in P.items()}
  for T in range(4):
   if T not in q: Q[T<<a]=mix[T]
  ck(sum(Q.values())==sum(w[j]*sum(R[j].values()) for j in range(a+1)))
  JS=add(H(q),scale(add(*(scale(H(ps[j]),w[j]) for j in range(a+1))),-1)); kap={}
  for T,v in q.items():
   pp={j:w[j]*ps[j].get(T,0)/v for j in range(a+1) if ps[j].get(T,0)}
   rr={j:w[j]*R[j][T]/mix[T] for j in range(a+1)}
   kap=add(kap,scale(KL(pp,rr),v))
  B=add(H(P),scale(H(q),-1))
  ck(CE(P,Q)==add(B,add(*(scale(CE(ps[j],R[j]),w[j]) for j in range(a+1))),JS,scale(kap,-1)))
  general+=1
 groups={}
 for i,t in enumerate(TABLES): groups.setdefault(tuple(sorted(spec(t).items())),[]).append(i)
 for group in groups.values():
  for ids in product(group,repeat=3):
   a=2; P=spec(comb_table([TABLES[i] for i in ids])); p=spec(TABLES[ids[0]]); R=ref(0,F(1,2)); Q={}
   for s,v in P.items(): Q[s]=R[s>>a]*v/p[s>>a]
   for T in R:
    if T not in p: Q[T<<a]=R[T]
   ck(sum(Q.values())==sum(R.values())); ck(KL(P,Q)==KL(p,R))
   data=sum((s>>a).bit_count()*v for s,v in P.items()); ck(data==sum(T.bit_count()*v for T,v in p.items()))
   Is=sum((s&3).bit_count()*v for s,v in P.items()); B=add(H(P),scale(H(p),-1))
   ck(interval(add({2:F(41,8)*Is},scale(B,-1)))[0]>=0); equal+=1
 for a in range(1,9):
  for labels in product([-1,1],repeat=a+1):
   t=[labels[next((j for j in range(a) if not (x>>j)&1),a)] for x in range(1<<a)]; P=spec(t)
   Is=sum(s.bit_count()*v for s,v in P.items()); V=1-P.get(0,0)
   ck(interval(add({2:F(41,8)*Is-2*V},scale(H(P),-1)))[0]>=0); scalar+=1
 return {'general_combs':general,'equal_spectrum_combs':equal,'scalar_combs':scalar,'general_reference_includes_subprobability':True}
def disjoint():
 cases=0
 for i,j in product(range(16),repeat=2):
  G,Ht=TABLES[i],TABLES[j]; pg,ph=spec(G),spec(Ht); mu,nu=fw(G).get(0,0),fw(Ht).get(0,0)
  t=[G[(x>>1)&3] if not x&1 else Ht[x>>3] for x in range(32)]; P=spec(t); d=(1-mu*nu)/2
  q={T:sum(v for s,v in P.items() if s>>1==T) for T in {s>>1 for s in P}}
  for variant in range(2):
   rg,rh=calibrate(ref(variant),pg),calibrate(ref(variant+1),ph)
   mix={}
   for T,v in rg.items(): mix[T]=mix.get(T,0)+v/2
   for T,v in rh.items(): mix[T<<2]=mix.get(T<<2,0)+v/2
   Q={s:mix[s>>1]*v/q[s>>1] for s,v in P.items()}
   for T,v in mix.items():
    if T not in q: Q[T<<1]=v
   ck(sum(Q.values())==1)
   ck(KL(P,Q)==scale(add(KL(pg,rg),KL(ph,rh)),F(1,2)))
   delta=add(H(P),scale(add(H(pg),H(ph)),F(-1,2)))
   # C_dis =2+4/ln2; multiply the comparison by ln2.
   lo,hi=interval(delta); ck(2*d*L2[0]+4*d-hi>=0)
   ck(CE(P,Q)==add(scale(add(CE(pg,rg),CE(ph,rh)),F(1,2)),delta))
   ck(interval(add(CE(pg,ref(variant)),scale(CE(pg,rg),-1)))[0]>=0)
   cases+=1
 return {'disjoint_pairs':256,'reference_cases':cases,'C_dis':'2+4/ln(2)','core_deficit_retained':True}
if __name__=='__main__':
 mode=sys.argv[1]; start=time.monotonic(); result=globals()[mode](); result.update(assertions=N,seconds=time.monotonic()-start)
 (OUT/(mode.upper()+'_RESULTS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8'); print(json.dumps(result))
