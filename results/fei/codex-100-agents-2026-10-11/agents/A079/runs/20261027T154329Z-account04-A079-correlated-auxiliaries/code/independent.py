from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,time

ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(x):
 global checks
 assert x
 checks+=1
def times(xs):
 y=Q(1)
 for x in xs:y*=x
 return y
def all_labels(n):return list(product((0,1),repeat=n))
def base(p):return {s:times(x if bit else 1-x for bit,x in zip(s,p)) for s in all_labels(len(p))}
def puncture(p):
 a=base(p);z=1-a[(0,)*len(p)]
 return {s:(x/z if any(s) else Q(0)) for s,x in a.items()}
def first_occupied(p):
 z=1-times(1-x for x in p);out=[]
 for j in range(len(p)):
  weight=times(1-x for x in p[:j])*p[j]/z
  if weight:out.append((weight,tuple(Q(0) if i<j else Q(1) if i==j else x for i,x in enumerate(p))))
 return out
def push(a,remaining):
 out={s:Q(0) for s in all_labels(len(remaining))}
 for s,x in a.items():out[tuple(s[i] for i in remaining)]+=x
 return out
def direct_transform(truth):
 labels=list(truth)
 return {a:sum((truth[x]*(-1)**sum(i*j for i,j in zip(a,x)) for x in labels),Q(0))/len(labels) for a in labels}
def entropy_ratio_identity(p,q,u):
 # At a boundary cardinality-one projection, u/q is constant on its entire face.
 z=sum(q[s] for s in q if sum(s)==1)
 check(sum(u.values())==1)
 for s,x in u.items():
  if x:check(x/q[s]==1/z)
 check(sum(p[s] for s in p if sum(s)==1)==1)
 # Both expectations of log(u/q) equal log(1/z), an exact identity before taking logs.

def main():
 start=time.perf_counter();models=0;marginals=0;boundaries=0
 for n in range(1,5):
  labels=all_labels(n);zero=(0,)*n;p=tuple(Q(1,4) if i%2 else Q(3,4) for i in range(n));bp=puncture(p)
  pieces=first_occupied(p);check(len(pieces)<=n);check(sum(w for w,_ in pieces)==1)
  for s in labels:check(sum(w*base(a)[s] for w,a in pieces)==bp[s])
  for mask in range(1<<n):
   rem=tuple(i for i in range(n) if mask>>i&1);pp=push(bp,rem);pr=tuple(p[i] for i in rem)
   survival=(1-times(1-x for x in pr))/(1-times(1-x for x in p))
   check(pp[(0,)*len(rem)]==1-survival)
   if survival:
    br=puncture(pr)
    for s in pp:
     if any(s):check(pp[s]==survival*br[s])
   marginals+=1
  t=tuple(Q(2) if i%2 else Q(1,2) for i in range(n));r=Q(2,7)
  q={s:Q(1,5) if s==zero else Q(4,5)*bp[s] for s in labels}
  raw={s:q[s]*times(z for i,z in enumerate(t) if s[i]) for s in labels if any(s)};Z=sum(raw.values())
  direct={s:r if s==zero else (1-r)*raw[s]/Z for s in labels}
  pnew=tuple(x*y/(1-x+x*y) for x,y in zip(p,t));bn=puncture(pnew)
  check(direct=={s:r if s==zero else (1-r)*bn[s] for s in labels});models+=1
  # Genuine boundary projection for an ACTUAL Boolean dictator, n<=3.
  if n<=3:
   truth={s:(-1)**s[0] for s in labels};coeff=direct_transform(truth);true={s:x*x for s,x in coeff.items()}
   check(sum(true.values())==1);check(sum(sum(s)*v for s,v in true.items())==1);check(true[zero]==0)
   z=sum(q[s] for s in labels if sum(s)==1)
   u={s:q[s]/z if sum(s)==1 else Q(0) for s in labels}
   entropy_ratio_identity(true,q,u);boundaries+=1
  # Categorical boundary really is necessary: its support contains every singleton.
  alpha={s:Q(1,n) if sum(s)==1 else Q(0) for s in labels}
  for mask in range(1<<n):
   rem=tuple(i for i in range(n) if mask>>i&1);a=push(alpha,rem);check(a[(0,)*len(rem)]==1-Q(len(rem),n))
   for s,x in a.items():
    if any(s):check(x==(Q(1,n) if sum(s)==1 else Q(0)))
  # Exact first-occupied cover has the sharp d lower bound by the singleton support argument.
  check(sum(1 for s,v in bp.items() if v and sum(s)==1)==n)
 # Direct-character Boolean query audit, independent of FWHT and integer bit masks.
 queries=0
 for n in range(3):
  labels=all_labels(n)
  for table in range(1<<(1<<n)):
   truth={s:(-1 if table>>i&1 else 1) for i,s in enumerate(labels)};c=direct_transform(truth);P={s:x*x for s,x in c.items()}
   check(sum(P.values())==1)
   for i in range(n):
    rem=tuple(j for j in range(n) if j!=i);pm=push(P,rem);children=[]
    for bit in (0,1):
     ct={tuple(s[j] for j in rem):v for s,v in truth.items() if s[i]==bit};cc=direct_transform(ct);children.append({s:x*x for s,x in cc.items()})
    check(all((children[0][s]+children[1][s])/2==pm[s] for s in pm))
    check(all(children[b][s]<=2*pm[s] for b in (0,1) for s in pm));queries+=1
 # Actual AND2 tensors: the uniform true spectrum and phase energy are recomputed.
 ands=[]
 for n in (4,6,8):
  # Factor the direct two-coordinate character sums, rather than transform2^n twice.
  h={(a,b):(-1 if a==b==0 else 1) for a,b in all_labels(2)};hc=direct_transform(h)
  check(all(v*v==Q(1,4) for v in hc.values()))
  coeff={s:times(hc[s[i:i+2]] for i in range(0,n,2)) for s in all_labels(n)}
  check(all(v*v==Q(1,1<<n) for v in coeff.values()))
  check(sum(sum(s)*v*v for s,v in coeff.items())==Q(n,2));ands.append(n)
 result={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'direct_reference_models':models,'full_marginals':marginals,'actual_dictator_boundary_projections':boundaries,'direct_Boolean_queries':queries,'actual_AND2_dimensions':ands,'arithmetic':'Fraction, full labelled character sums, independent first-occupied decomposition; no author-code import or floating sign'}
 (ROOT/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':main()
