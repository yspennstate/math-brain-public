"""Deterministic verification of X012 identities; no search is used for proofs."""
import itertools
import json
from math import comb, log
import numpy as np
from pathlib import Path

ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(121203)

def subsets(n,k): return list(itertools.combinations(range(n),k))
def entropy(p):
 p=np.asarray(p);ok=p>0
 return float(-np.dot(p[ok],np.log(p[ok])))
def signs(m): return np.array(list(itertools.product([-1,1],repeat=m)),dtype=int)
def h(p):return entropy(np.array([p,1-p]))
def sector_transform(c,slots,k):
 E=signs(len(slots));J=subsets(len(slots),k)
 W=np.array([np.prod(E[:,S],axis=1) for S in J]).T
 return E,abs(W@c)**2/2**len(slots)
def two_form(U):return {S:np.linalg.det(U[list(S),:]) for S in subsets(U.shape[0],U.shape[1])}
def splitter_sectors(U,V):
 n=U.shape[0];ra=U.shape[1];rb=V.shape[1]
 a=two_form(U);b=two_form(V);sector_data=[];marg=np.zeros(2**n)
 for d in range(min(ra,rb)+1):
  m=ra+rb-2*d
  if d+m>n:continue
  for D in subsets(n,d):
   remainder=tuple(i for i in range(n) if i not in D)
   for C in itertools.combinations(remainder,m):
    cs=[]
    for S in itertools.combinations(C,ra-d):
     A=tuple(sorted(D+S));B=tuple(sorted(D+tuple(i for i in C if i not in S)))
     sg=(-1)**sum(j<i for i in A for j in B)
     cs.append(sg*a[A]*b[B])
    c=np.array(cs);E,q=sector_transform(c,C,ra-d)
    M=float(np.vdot(c,c).real);gain=entropy(q)-entropy(abs(c)**2)
    if ra-d==0:bound=m*log(2)
    elif ra-d==1:bound=log(2**m/(3*m-2))
    elif ra-d==2:bound=log(2**m/(comb(m,2)*(15-12/m)))
    else:bound=float('nan')
    sector_data.append((d,m,M,gain,bound))
    for eps,prob in zip(E,q):
     Aout=D+tuple(i for i,e in zip(C,eps) if e==1)
     mask=sum(1<<i for i in Aout);marg[mask]+=prob
 return a,b,sector_data,marg

def dpp_atoms(K):
 n=len(K);out=[]
 for S in range(2**n):
  M=np.column_stack([K[:,i] if S>>i&1 else np.eye(n)[:,i]-K[:,i] for i in range(n)])
  out.append(np.linalg.det(M).real)
 return np.maximum(out,0)

# Arbitrary complex mixed weight-two density matrices, checking the finite fourth-moment bound.
moment_results=[]
for m in [4,8,9,10]:
 N=comb(m,2);Z=rng.normal(size=(N,3))+1j*rng.normal(size=(N,3));R=Z@Z.conj().T;R/=np.trace(R)
 E=signs(m);W=np.array([np.prod(E[:,S],axis=1) for S in subsets(m,2)]).T
 F=np.einsum('bi,ij,bj->b',W,R,W).real
 fourth=float(np.mean(F**2));bound=15-12/m
 assert fourth<=bound+1e-12
 assert abs(np.mean(F)-1)<1e-12
 q=F/2**m
 assert entropy(q)>=m*log(2)-log(bound)-1e-12
 moment_results.append(dict(m=m,moment=fourth,bound=bound,entropy_gap=entropy(q)-entropy(np.diag(R).real)))

# A rank-two projection and a noncommuting rank-seven projection in dimension nine.
n=9
U=np.linalg.qr(rng.normal(size=(n,2))+1j*rng.normal(size=(n,2)))[0]
V=np.linalg.qr(rng.normal(size=(n,7))+1j*rng.normal(size=(n,7)))[0]
a,b,data,marg=splitter_sectors(U,V)
P=U@U.conj().T;Q=V@V.conj().T
mid=dpp_atoms((P+Q)/2)
input_h=entropy(abs(np.array(list(a.values())))**2)+entropy(abs(np.array(list(b.values())))**2)
full_gain=sum(row[3] for row in data);lower=sum(row[2]*row[4] for row in data)
assert abs(sum(row[2] for row in data)-1)<1e-12
assert max(abs(marg-mid))<2e-14
assert all(g>=M*bound-1e-12 for _,_,M,g,bound in data)
assert full_gain>=lower>=log(128/123)-1e-12
midgap=entropy(mid)-input_h/2
assert 2*midgap>=full_gain-1e-12

# Real decomposable sector family contradicting sector monotonicity.
t=1/32
A=np.array([[1,0],[1,1],[0,1],[0,1]],dtype=float)
B=np.array([[1,0],[1,0],[0,1],[t,-1]],dtype=float)
a0=two_form(A);b0=two_form(B)
shuffle=[1,-1,1,1,-1,1]
c=np.array([sg*a0[S]*b0[tuple(i for i in range(4) if i not in S)] for sg,S in zip(shuffle,subsets(4,2))])
E,qq=sector_transform(c,tuple(range(4)),2)
sector_loss=entropy(qq)-entropy(c*c)
assert sector_loss<0
X=a0[(0,1)]*a0[(2,3)];Y=-a0[(0,2)]*a0[(1,3)]
Xp=b0[(0,1)]*b0[(2,3)];Yp=-b0[(0,2)]*b0[(1,3)]
AA=c[0]*c[5];BB=c[1]*c[4];CC=c[2]*c[3]
discriminant=AA*AA+BB*BB+CC*CC-2*(AA*BB+AA*CC+BB*CC)
assert abs(discriminant-(X*Yp-Y*Xp)**2)<1e-12

# Four-site complementary vanishing-minor compensation theorem, including complex phases.
sparse_results=[]
for case in range(6):
 A=rng.normal(size=(4,2))+1j*rng.normal(size=(4,2))
 B=rng.normal(size=(4,2))+1j*rng.normal(size=(4,2))
 A[3]=(0.3+0.7j)*A[2]
 B[1]=(-0.6+0.8j)*B[0]
 U=np.linalg.qr(A)[0];V=np.linalg.qr(B)[0]
 aa,bb,dd,mm=splitter_sectors(U,V)
 alpha=abs(aa[(0,1)])**2;beta=abs(bb[(2,3)])**2
 assert abs(aa[(2,3)])<1e-14 and abs(bb[(0,1)])<1e-14
 actual=sum(z[3] for z in dd)
 gamma=2*log(2)*(alpha+beta-2*np.sqrt(alpha*beta*(1-alpha)*(1-beta)))
 assert actual>=gamma-1e-12
 P0=U@U.conj().T;P1=V@V.conj().T
 pm=dpp_atoms((P0+P1)/2)
 assert max(abs(mm-pm))<1e-14
 sparse_results.append(dict(case=case,alpha=alpha,beta=beta,full_gain=actual,lower_bound=gamma,active_support_rank=int(np.linalg.matrix_rank(np.column_stack((U,V)))),commutator_norm=float(np.linalg.norm(P0@P1-P1@P0))))

report=dict(sparse_compensation_checks=sparse_results,moment_checks=moment_results,rank_two_rank_seven=dict(n=n,sector_count=len(data),full_gain=full_gain,sector_lower_bound=lower,midpoint_gap=midgap,marginal_error=float(max(abs(marg-mid)))),real_sector_obstruction=dict(t=t,coefficients=c.tolist(),unnormalized_gain=sector_loss,discriminant=discriminant),universal_midpoint_lower_bound=log(128/123)/2)
print(json.dumps(report,indent=2))
(ROOT/'check-results.json').write_text(json.dumps(report,indent=2)+'\n')
