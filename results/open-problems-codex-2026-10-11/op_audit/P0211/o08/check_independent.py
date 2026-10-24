"""Independent constructions; no claimant code or numerical output imported."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import factorial, comb, log, lgamma, sqrt
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigvalsh, eigvalsh_tridiagonal
import sympy as sy

ROOT=Path(__file__).resolve().parent
report={}
def parts(n,lo=1):
 if n==0: yield (); return
 for j in range(lo,n+1):
  for rest in parts(n-j,j): yield (j,)+rest
def moves(p,n,b):
 out=defaultdict(lambda:F(0))
 for i,j in combinations(range(len(p)),2):
  q=tuple(sorted([x for k,x in enumerate(p) if k not in (i,j)]+[p[i]+p[j]]))
  out[q]+=F(2,n)
 for i,size in enumerate(p):
  for cut in range(1,size):
   q=tuple(sorted([x for k,x in enumerate(p) if k!=i]+[cut,size-cut]))
   out[q]+=b
 return dict(out)
def projection(mask,n):
 cuts=[i for i in range(n) if mask>>i&1]
 return tuple(sorted((cuts[(i+1)%len(cuts)]-x)%n or n for i,x in enumerate(cuts)))
def edge_moves(mask,n,b):
 k=mask.bit_count()
 return {mask^(1<<i):(F(k-1,n) if mask>>i&1 else b) for i in range(n) if not(mask>>i&1) or k>1}
projection_count=0
for n in range(2,10):
 groups=defaultdict(list)
 for mask in range(1,1<<n): groups[projection(mask,n)].append(mask)
 for p,states in groups.items():
  c=Counter(p)
  assert len(states)*np.prod([factorial(v) for v in c.values()],dtype=object)==n*factorial(len(p)-1)
  for b in (F(1,n),F(3,7)):
   avg=defaultdict(lambda:F(0))
   for mask in states:
    for dest,rate in edge_moves(mask,n,b).items(): avg[projection(dest,n)]+=rate/len(states)
   assert dict(avg)==moves(p,n,b), (n,p,b,avg,moves(p,n,b))
   projection_count+=1
report['exact_projected_rate_cases']=projection_count

# Exact Boolean-lattice commutator on every layer.
commutators=0
for n in range(2,9):
 layers=[[sum(1<<i for i in S) for S in combinations(range(n),k)] for k in range(n+1)]
 U=[]
 for k in range(n): U.append(np.array([[int(s&t==s) for s in layers[k]] for t in layers[k+1]],dtype=np.int64))
 for k in range(n+1):
  d=len(layers[k]); up=U[k].T@U[k] if k<n else np.zeros((d,d),dtype=np.int64)
  down=U[k-1]@U[k-1].T if k else np.zeros((d,d),dtype=np.int64)
  assert np.array_equal(up-down,(n-2*k)*np.eye(d,dtype=np.int64)); commutators+=1
report['exact_commutator_layers']=commutators

def matrix(states,trans):
 idx={s:i for i,s in enumerate(states)}; G=np.zeros((len(states),len(states)))
 for i,s in enumerate(states):
  for q,r in trans(s).items(): G[i,idx[q]]+=float(r)
  G[i,i]=-sum(G[i])
 return G
def symmetric(G,logw):
 logw=np.array(logw); S=-G*np.exp((logw[:,None]-logw[None,:])/2)
 assert np.max(abs(S-S.T))<1e-8
 return (S+S.T)/2
def radial_eigs(n,b,l=None):
 if l is None:
  ks=np.arange(1,n+1,dtype=float); births=b*(n-ks); deaths=ks*(ks-1)/n; kill=np.zeros(n)
 else:
  ks=np.arange(l,n-l+1,dtype=float); births=b*(n-ks-l); deaths=(ks-1)*(ks-l)/n; kill=l*b+l*(ks-1)/n
 return eigvalsh_tridiagonal(births+deaths+kill,-np.sqrt(births[:-1]*deaths[1:]))
spec_cases=0; discrepancy=0.; gap_records=[]
for n in range(2,17):
 states=list(parts(n))
 for b in (1e-8,1/n**2,1/n,1.,100.):
  G=matrix(states,lambda p:moves(p,n,F(str(b))))
  logw=[len(p)*log(b*n)-sum(lgamma(v+1) for v in Counter(p).values()) for p in states]
  vals=eigvalsh(symmetric(G,logw)); gap=vals[1]; s=b+sqrt(b)+1/n
  assert gap>=s/6-1e-8 and gap<=4*s+1e-8
  assert gap>=b+2/n-1e-8
  assert gap<=radial_eigs(n,b)[1]+1e-8
  gap_records.append({'n':n,'beta':b,'gap':float(gap),'gap_over_s':float(gap/s)}); spec_cases+=1
  if n<=8:
   subsets=list(range(1,1<<n)); E=matrix(subsets,lambda m:edge_moves(m,n,F(str(b))))
   w=[m.bit_count()*log(b*n)-lgamma(m.bit_count()) for m in subsets]
   full=eigvalsh(symmetric(E,w)); expected=list(radial_eigs(n,b))
   for l in range(1,n//2+1): expected.extend(np.repeat(radial_eigs(n,b,l),comb(n,l)-comb(n,l-1)))
   err=float(max(abs(full-np.sort(expected)))); discrepancy=max(discrepancy,err); assert err<1e-8
report.update(partition_spectrum_cases=spec_cases,full_edge_sector_max_error=discrepancy,gaps=gap_records)

# Symbolic identities, derived from rates and successive h ratios.
k,n,a,b,l,r=sy.symbols('k n a b l r',positive=True)
upper=2*b*(n-k-1)/(k+a+2)+b+2*k*a/(n*(k+a-1))
direct=b*(n-k-1)*(1-(k+a)/(k+a+2))+k*(k-1)/n*(1-(k+a+1)/(k+a-1))+b+2*k/n
assert sy.simplify(direct-upper)==0
sector=b*(n-k-l)/(k+a+1)+l*b+(k-1)*((l-1)*k+l*a)/(n*(k+a-1))
direct=b*(n-k-l)*(1-(k+a)/(k+a+1))+(k-1)*(k-l)/n*(1-(k+a)/(k+a-1))+l*b+l*(k-1)/n
assert sy.simplify(direct-sector)==0
stage2=b*(n-r-2)/(r+a+1)+b+r*(a-1)/(n*(r+a-1))
direct=b*(n-r-2)*(1-(r+a)/(r+a+1))+r*r/n*(1-(r+a)/(r+a-1))+b+r/n
assert sy.simplify(direct-stage2)==0
report['symbolic_reciprocal_identities']=3

# Exhaustive exact marginal verification of both coupling stages.
couplings=0
for n in range(2,7):
 b=F(3,7)
 for X in range(1,1<<n):
  for Y in range(X+1,1<<n):
   common=X&Y; vacant=((1<<n)-1)^(X|Y); events=[]
   if X&Y==X and (X^Y).bit_count()==1:
    k=X.bit_count()
    for i in range(n):
     bit=1<<i
     if vacant&bit: events.append((X|bit,Y|bit,b))
     if common&bit:
      if k>1: events.append((X^bit,Y^bit,F(k-1,n)))
      events.append((X,Y^bit,F(1,n)))
    bit=X^Y; events.extend([(Y,Y,b),(X,X,F(k,n))])
   elif X.bit_count()==Y.bit_count() and (X^Y).bit_count()==2:
    r=common.bit_count()
    for i in range(n):
     bit=1<<i
     if vacant&bit: events.append((X|bit,Y|bit,b))
     if common&bit: events.append((X^bit,Y^bit,F(r,n)))
    events.append((X|Y,X|Y,b))
    if r: events.append((common,common,F(r,n)))
   else: continue
   for pos,start in enumerate((X,Y)):
    marginal=defaultdict(lambda:F(0))
    for x,y,rate in events:
     dest=(x,y)[pos]
     if dest!=start: marginal[dest]+=rate
    assert dict(marginal)==edge_moves(start,n,b),(n,X,Y,pos,marginal)
   couplings+=1
report['exact_coupling_pairs']=couplings

certificate_cases=0; min_ratio=100.
for nn in (8,9,12,16,32,100):
 for bb in np.geomspace(4/nn**2,1/16,13):
  aa=nn*sqrt(bb)
  for kk in range(1,nn):
   c=bb*(nn-kk-1)/(kk+aa+1)-kk*(kk-1)/(nn*(kk+aa-1))+bb+2*kk/nn
   assert c>=sqrt(bb)/5-1e-12; certificate_cases+=1
  for ll in range(1,nn//2+1):
   for kk in range(ll,nn-ll+1):
    c=bb*(nn-kk-ll)/(kk+aa+1)+ll*bb+(kk-1)*((ll-1)*kk+ll*aa)/(nn*(kk+aa-1))
    min_ratio=min(min_ratio,c/sqrt(bb)); assert c>=sqrt(bb)/5-1e-12; certificate_cases+=1
report.update(certificate_grid_cases=certificate_cases,sector_certificate_min_ratio=min_ratio)
(ROOT/'independent_results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='gaps'},indent=2))
