import json,time,sys
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv
spec={'helper_version':'A019-biased-exposure-v1','family':'F=1 at x0 and h(y)s(z,w) at x1; actual private-core query, nonlinear two-bit mask, both complete child references retained','domain':'pilot every one-bit core; full every core in dimensions1,2,3, every private query, point-defect mask and its negative, exact-spectrum and uniform supplied child core references; parent core reference is their actual conditional spectral lift','case_count':16 if pilot else 3216,'symmetry':'none on cores; two fixed masks only, no quotient claim','arithmetic':'integer Walsh, Fraction spectra/reference masses; exact rational prime-log identities; certified36-term logarithm intervals','memory_estimate_MB':100,'maximum_runtime_seconds':60}
(R/'out'/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2))
start=time.monotonic();checks=cases=nonflat=nonconstant_children=0
def ck(x):
 global checks
 checks+=1;assert x
@lru_cache(None)
def factor(x):
 d={};p=2
 while p*p<=x:
  while x%p==0:d[p]=d.get(p,0)+1;x//=p
  p+=1
 if x>1:d[x]=d.get(x,0)+1
 return tuple(d.items())
def add(*terms):
 out={}
 for scale,f in terms:
  for p,v in f.items():out[p]=out.get(p,Q(0))+scale*v
 return {p:v for p,v in out.items() if v}
def logform(q):
 ck(q>0);d={}
 for p,v in factor(q.numerator):d[p]=d.get(p,0)+v
 for p,v in factor(q.denominator):d[p]=d.get(p,0)-v
 return {p:Q(v) for p,v in d.items() if v}
def ce(ps,qs):return add(*[(-p,logform(q)) for p,q in zip(ps,qs) if p])
def eta(p):return {} if not p else add((-p,logform(p)))
def psi(mu):return add((1,eta((1+mu)**2/4)),(1,eta((1-mu)**2/4)),(1-mu*mu,{2:Q(1)}),(-Q(1,2),eta(mu*mu)))
def lnunit(q):
 z=(q-1)/(q+1);l=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(36)),Q(0));return l,l+2*z**73/(73*(1-z*z))
l2,u2=lnunit(Q(2))
@lru_cache(None)
def lp(p):
 k=p.bit_length()-1;l,u=lnunit(Q(p,1<<k));return Q(k)+l/u2,Q(k)+u/l2
def interval(f):
 l=u=Q(0)
 for p,v in f.items():
  a,b=lp(p);l+=v*(a if v>0 else b);u+=v*(b if v>0 else a)
 return l,u
def nonnegative(f):
 if not f:return True
 return interval(f)[0]>=0
def fw(tt):
 a=list(tt);w=1
 while w<len(a):
  for b in range(0,len(a),2*w):
   for j in range(b,b+w):a[j],a[j+w]=a[j]+a[j+w],a[j]-a[j+w]
  w*=2
 return tuple(Q(x,len(a)) for x in a)
def spectrum(tt):return tuple(c*c for c in fw(tt))
def actualgate(h,s):return tuple(1 if x==0 else h[y]*s[b] for b in range(4) for y in range(len(h)) for x in range(2))
@lru_cache(None)
def gate(h,qh,sign):
 s=tuple(sign*x for x in (-1,1,1,1));mu=Q(sum(h),len(h))*Q(sum(s),4)
 pf=spectrum(actualgate(h,s));qg=tuple(q/4 for b in range(4) for q in qh)
 qf=[]
 for t in range(4*len(h)):
  row=pf[2*t]+pf[2*t+1];qd=(qg[t]+int(t==0))/2
  qf.extend((qd*pf[2*t]/row,qd*pf[2*t+1]/row) if row else (qd/2,qd/2))
 ck(sum(qf)==1);ck(sum(pf)==1)
 ph=spectrum(h);ch=ce(ph,qh);cf=ce(pf,qf)
 p=mu*mu/(1+mu*mu);q=qg[0]/(1+qg[0])
 kl=add((1,ce((p,1-p),(q,1-q))),(-1,ce((p,1-p),(p,1-p))))
 D=add(((1+mu*mu)/2,kl));ck(nonnegative(D))
 ck(cf==add((Q(1,2),ch),(1,{2:Q(1)}),(1,psi(mu)),(-1,D)))
 return cf,D,ch,pf
A={3:Q(9,8),2:Q(-1)}
transport={'positive':None,'negative':None}
for n in ([1] if pilot else [1,2,3]):
 N=1<<n
 for mask in range(1<<N):
  h=tuple(1-2*((mask>>v)&1) for v in range(N));ph=spectrum(h)
  if len({p for p in ph if p})>1:nonflat+=1
  for query in range(n):
   children=[]
   for b in (0,1):children.append(tuple(h[(u&((1<<query)-1))|(((u>>query)<<1|b)<<query)] for u in range(N//2)))
   pchild=[spectrum(t) for t in children]
   d=Q(sum(a!=b for a,b in zip(*children)),N//2)
   if all(abs(sum(t))<len(t) for t in children):nonconstant_children+=1
   beta=Q(sum(h),N);betas=[Q(sum(t),N//2) for t in children]
   for kind in ('exact','uniform'):
    qchild=pchild if kind=='exact' else [tuple(Q(1,N//2) for _ in range(N//2))]*2
    qh=[Q(0)]*N
    for u in range(N//2):
     j=(u&((1<<query)-1))|((u>>query)<<(query+1));row=ph[j]+ph[j|(1<<query)]
     qrow=(qchild[0][u]+qchild[1][u])/2
     for b in (0,1):qh[j|(b<<query)]=qrow*(ph[j|(b<<query)]/row if row else Q(1,2))
    qh=tuple(qh);ck(sum(qh)==1)
    for sign in (1,-1):
     cases+=1
     if time.monotonic()-start>60:raise TimeoutError('frozen deadline')
     root=gate(h,qh,sign);child=[gate(children[b],qchild[b],sign) for b in (0,1)]
     curvature=add((1,psi(beta/2)),(-Q(1,2),psi(betas[0]/2)),(-Q(1,2),psi(betas[1]/2)))
     ck(nonnegative(curvature));ck(nonnegative(add((d,A),(-1,curvature))))
     deltaD=add((Q(1,2),child[0][1]),(Q(1,2),child[1][1]),(-1,root[1]))
     lhs=add((1,root[0]),(-Q(1,2),child[0][0]),(-Q(1,2),child[1][0]))
     rhs=add((Q(1,2),root[2]),(-Q(1,4),child[0][2]),(-Q(1,4),child[1][2]),(1,curvature),(1,deltaD))
     ck(lhs==rhs)
     tt=actualgate(h,tuple(sign*x for x in (-1,1,1,1)));bit=query+1
     ck(Q(sum(tt[v]!=tt[v^(1<<bit)] for v in range(len(tt))),len(tt))==d/2)
     if deltaD:
      lo,hi=interval(deltaD);direction='positive' if lo>0 else 'negative' if hi<0 else None
      if direction and transport[direction] is None:
       transport[direction]={'n':n,'core_mask':mask,'query':query,'reference_kind':kind,'mask_sign':sign,'core_disagreement':str(d),'child_means':[str(v) for v in betas],'deltaD_prime_log':{str(p):str(v) for p,v in deltaD.items()},'enclosure':[str(lo),str(hi)]}
       (R/'out/FIRST_TRANSPORT_SIGNS.json').write_text(json.dumps(transport,indent=2))
 (R/'out/PARTIAL.json').write_text(json.dumps({'completed_dimension':n,'cases':cases,'checks':checks,'seconds':time.monotonic()-start},indent=2))
# Sharp bound has an actual Boolean equality: h is a queried character.
ck(add((1,psi(Q(0))),(-1,psi(Q(1,2))))==A)
out={'status':'PASS','cases':cases,'checks':checks,'nonflat_core_tables':nonflat,'queries_with_two_nonconstant_children':nonconstant_children,'seconds':time.monotonic()-start,'sharp_coefficient':'9/8 log2(3)-1','transport_sign_witnesses':transport,'full_fei':'OPEN'}
(R/'out'/('PILOT_CHECK.json' if pilot else 'EXPOSURE_CHECK.json')).write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='transport_sign_witnesses'}))
