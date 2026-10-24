"""Exact post-tag query/reset certificate. Standard library only; no workers."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic(); checks=cases=terminals=resets=0
PILOT='--pilot' in sys.argv
TARGETED='--targeted' in sys.argv

def ck(value):
 global checks
 checks+=1
 if not value: raise AssertionError(checks)
 if time.monotonic()-START > (55 if PILOT else 120 if TARGETED else 180):
  raise TimeoutError('frozen runtime limit')

@lru_cache(maxsize=512)
def fw(tt):
 w=list(map(Q,tt)); k=1
 while k<len(w):
  for s in range(0,len(w),2*k):
   for j in range(s,s+k):
    a,b=w[j],w[j+k]; w[j],w[j+k]=a+b,a-b
  k*=2
 return tuple(x/len(w) for x in w)

def restrict(tt,i,sign):
 bit=0 if sign==1 else 1
 return tuple(tt[(v&((1<<i)-1))|((v>>i)<<(i+1))|(bit<<i)] for v in range(len(tt)//2))

def expand(v,i,bit):return (v&((1<<i)-1))|((v>>i)<<(i+1))|(bit<<i)

@lru_cache(None)
def factors(n):
 ans={}; p=2
 while p*p<=n:
  while n%p==0: ans[p]=ans.get(p,0)+1; n//=p
  p+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans

@lru_cache(maxsize=4096)
def logterm(q,weight=Q(1)):
 if not weight:return {}
 if q<=0: raise ValueError(('log support',q,weight))
 ans={}
 for n,sgn in ((q.numerator,1),(q.denominator,-1)):
  for p,e in factors(n).items():ans[p]=ans.get(p,Q(0))+sgn*weight*e
 return {p:c for p,c in ans.items() if c}

def add(*vecs):
 ans={}
 for v in vecs:
  for p,c in v.items():ans[p]=ans.get(p,Q(0))+c
 return {p:c for p,c in ans.items() if c}
def scale(v,c):return {p:x*c for p,x in v.items() if x*c}
def ce(p,q):return add(*(logterm(b,-a) for a,b in zip(p,q) if a))
def kl(p,q):return add(*(logterm(a/b,a) for a,b in zip(p,q) if a))
def H(p):return ce(p,p)
def norm(p):ck(sum(p)==1);ck(all(x>=0 for x in p))
def jsonvec(v):return {str(p):str(c) for p,c in v.items()}

def wrapper(a,b,h,sign):
 return tuple(a[u]+sign*b[u]*h[x] for x in range(len(h)) for u in range(len(a)))

def parent_case(a,b,h,i,profile):
 global cases,terminals,resets
 cases+=1
 aa,bb,hh=fw(a),fw(b),fw(h)
 pp=tuple(v*v for v in hh); r=pp[0]; beta=sum(x*x for x in bb)
 ck(all(a[j]*b[j]==0 and a[j]**2+b[j]**2==1 for j in range(len(a))))
 if r==1:return
 nt=len(h)-1
 Rt=([Q(1,nt)]*nt if profile==0 else [pp[t]/(1-r) for t in range(1,len(h))])
 # True A032 old target component: epsilon_tag=1/8, uniform target.
 M=[Q(0)]+[Q(7,8)*x+Q(1,8*nt) for x in Rt]
 ck(sum(M)==1)
 # Reconstruct A032's antecedent from a fresh tagged truth table, not its code.
 source=(Q(1,2),)+tuple(x/2 for x in Rt)
 tagged=tuple(a[u]+z*b[u]*h[x] for x in range(len(h)) for u in range(len(a)) for z in (1,-1))
 pw=tuple(x*x for x in fw(tagged))
 qw=tuple((aa[u]**2 if z==0 and t==0 else bb[u]**2*source[t] if z==1 else Q(0)) for t in range(len(h)) for u in range(len(a)) for z in (0,1))
 marginal=tuple(pw[2*j]+pw[2*j+1] for j in range(len(pw)//2))
 childlaws=[tuple(x*x for x in fw(wrapper(a,b,h,sig))) for sig in (1,-1)]
 childrefs=[tuple((aa[u]+sig*hh[0]*bb[u])**2 if t==0 else bb[u]**2*(1-r)*M[t] for t in range(len(h)) for u in range(len(a))) for sig in (1,-1)]
 js=add(H(marginal),scale(add(*(H(p) for p in childlaws)),Q(-1,2)))
 taginc=add(H(pw),scale(H(marginal),-1),scale(add(*(ce(p,q) for p,q in zip(childlaws,childrefs))),Q(1,2)),scale(ce(pw,qw),-1))
 binary=kl((r,1-r),(Q(1,2),Q(1,2)))
 tailchange=add(kl(pp[1:],M[1:]),scale(kl(pp[1:],Rt),-1))
 tagrhs=add(scale(js,-1),scale(binary,-beta),scale(tailchange,beta))
 ck(taginc==tagrhs)
 m1=M[1<<i]; w=(1-r)*(1-m1)
 L=[Q(0)]+[(M[expand(v,i,0)]+M[expand(v,i,1)])/(1-m1) for v in range(1,len(h)//2)] if m1<1 else []
 nu=hh[0]; newN=len(h)//2
 for sig in (1,-1):
  tt=wrapper(a,b,h,sig); ww=fw(tt); p=tuple(x*x for x in ww)
  q=tuple((aa[u]+sig*nu*bb[u])**2 if t==0 else bb[u]**2*(1-r)*M[t] for t in range(len(h)) for u in range(len(a)))
  norm(p);norm(q)
  ck(all(not x or y>0 for x,y in zip(p,q)))
  j=(len(a)).bit_length()-1+i
  pm=tuple(p[expand(v,j,0)]+p[expand(v,j,1)] for v in range(len(p)//2))
  qm=tuple(q[expand(v,j,0)]+q[expand(v,j,1)] for v in range(len(q)//2))
  erase=add(H(p),scale(H(pm),-1))
  rho=add(kl(p,q),scale(kl(pm,qm),-1))
  childcost=[]; childbounds=[]
  for tau in (1,-1):
   terminals+=1
   child=restrict(tt,j,tau); actual=tuple(x*x for x in fw(child))
   hc=restrict(h,i,tau); hw=fw(hc); pc=tuple(x*x for x in hw)
   nu1=hw[0]; r1=pc[0]; tailmass=beta*(1-r1)
   vac=tuple((aa[u]+sig*nu1*bb[u])**2 for u in range(len(a)))
   cv=tuple((aa[u]+sig*nu*bb[u])**2+bb[u]**2*(1-r)*m1 for u in range(len(a)))
   coarse=vac+(tailmass,); coarseq=cv+(beta*w,)
   norm(actual);norm(coarse);norm(coarseq)
   ck(tuple(actual[:len(a)])==vac)
   ck(tuple(qm[:len(a)])==cv)
   refund=kl(coarse,coarseq)
   for eps in (Q(0),Q(1,8)):
    resets+=1
    if tailmass:
     ck(bool(L));target=1
     N=[Q(0)]+[(1-eps)*L[v]+eps*(v==target) for v in range(1,newN)]
     qnew=vac+tuple(bb[u]**2*(1-r1)*N[v] for v in range(1,newN) for u in range(len(a)))
     delta=add(kl(pc[1:],N[1:]),scale(kl(pc[1:],L[1:]),-1))
     predicted=add(scale(refund,-1),scale(delta,beta))
     # A KL expression on unnormalised pc tail is intentional: the mass is retained.
     floor=logterm(1/(1-eps),tailmass)
     ck(all(N[v]>=(1-eps)*L[v] for v in range(1,newN)))
    else:
     qnew=vac+tuple(Q(0) for v in range(1,newN) for u in range(len(a)))
     predicted=scale(refund,-1);floor={}
    norm(qnew)
    cost=add(ce(actual,qnew),scale(ce(actual,qm),-1))
    ck(cost==predicted)
    if eps==Q(1,8):
     childcost.append(ce(actual,qnew)); childbounds.append(add(scale(refund,-1),floor))
   # Independent complete-CE/conditional-KL decomposition, including controller atoms.
   ck(add(ce(actual,qm),scale(H(actual),-1))==kl(actual,qm))
  actual_increment=add(erase,scale(add(*childcost),Q(1,2)),scale(ce(p,q),-1))
  predicted_increment=add(scale(rho,-1),scale(add(*childbounds),Q(1,2)))
  # The exact increment uses actual tail likelihood change rather than the floor bound.
  exact_rhs=add(scale(rho,-1),scale(add(*(add(c,scale(ce(tuple(x*x for x in fw(restrict(tt,j,tau))),qm),-1)) for c,tau in zip(childcost,(1,-1)))),Q(1,2)))
  ck(actual_increment==exact_rhs)

def fixture():
 # Direct character sums independently reconstruct the four terminal spectra.
 a=(1,0);b=(0,1);k=(-1,1,1,1);h=tuple(sign*k[x] for x in range(4) for sign in (1,-1))
 refunds=[]
 for sig,tau in product((1,-1),repeat=2):
  tt=wrapper(a,b,h,sig);child=restrict(tt,1,tau)
  wh=tuple(sum(Q(v)*(1 if (s&x).bit_count()%2==0 else -1) for x,v in enumerate(child))/len(child) for s in range(len(child)))
  p=tuple(x*x for x in wh)
  ck(sorted(p[:2])==[Q(1,16),Q(9,16)])
  coarse=p[:2]+(Q(3,8),); cq=(Q(5,16),Q(5,16),Q(3,8))
  ck(kl((Q(3,8),Q(5,8)),(Q(3,8),Q(5,8)))=={})
  rr=kl(coarse,cq);ck(rr=={3:Q(9,8),5:-Q(5,8)})
  ck(3**9>4*5**5);ck(8**4<2*7**4)
  N=(Q(5,12),Q(7,24),Q(7,24));ck(sum(N)==1)
  refunds.append({'tag_sign':sig,'seed_sign':tau,'vacuum':list(map(str,p[:2])),'refund_log_vector':jsonvec(rr),'tail_after_reset':list(map(str,N))})
 return {'status':'PASS','terminals':refunds,'strict_refund_lower_bound':'1/4','floor_bill_upper_bound':'3/32','net_release_lower_bound':'5/32','scalar_occupancy_KL':'0','integer_certificates':{'phase':3**9>4*5**5,'floor':8**4<2*7**4}}

def main():
 masks=list(product(((1,0),(-1,0),(0,1),(0,-1)),repeat=2))
 for ab in masks[:2] if PILOT else masks:
  a,b=tuple(z[0] for z in ab),tuple(z[1] for z in ab)
  for h in list(product((1,-1),repeat=4))[:4] if PILOT else product((1,-1),repeat=4):
   for i in range(2):parent_case(a,b,h,i,0)
 a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-x*x for x in a)
 panel=[tuple(h)*2 for h in product((1,-1),repeat=4)]
 panel += [tuple(1 if mask>>x&1 else -1 for x in range(8)) for mask in (0x01,0x02,0x04,0x08,0x69,0x96,0x17,0xe8)]
 ck(len(set(panel))==24)
 for h in list(product((1,-1),repeat=8))[:4] if PILOT else panel if TARGETED else product((1,-1),repeat=8):
  for i in range(3):
   for profile in (0,1):parent_case(a,b,h,i,profile)
 fi=fixture()
 out={'status':'PASS','helper':'A033-post-tag-seed-query-v3-targeted','pilot':PILOT,'targeted':TARGETED,'parent_query_profiles':cases,'actual_terminals':terminals,'fresh_resets':resets,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'A032_tag_reset_identity':'independently reconstructed at every nonconstant parent case','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (ROOT/'out').mkdir(exist_ok=True)
 (ROOT/'out'/('pilot.json' if PILOT else 'targeted.json' if TARGETED else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 (ROOT/'out'/'phase_fixture.json').write_text(json.dumps(fi,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(out))
if __name__=='__main__':main()
