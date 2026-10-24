#!/usr/bin/env python3
# R18 run-specific finite checker. Full analytic proofs are in the paired run report.
import itertools, math, random
import numpy as np
SEED=202609161250
rng=random.Random(SEED); np.random.seed(SEED%(2**32))
lehmer=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
roots=np.roots(lehmer)
theta=max(r.real for r in roots if abs(r.imag)<1e-8); lam=1/theta
neutral=sorted([r for r in roots if abs(abs(r)-1)<1e-7 and r.imag>1e-8],key=lambda z:np.angle(z))
assert len(neutral)==4

def twice_area(r):
    a,b,c=map(float,r); s=(a+b+c)/2
    return 2*math.sqrt(max(0,s*(s-a)*(s-b)*(s-c)))
strict=[]; deg=[]; non=[]; mj=(1e9,None)
for r in itertools.product(range(1,5),repeat=3):
    mx=max(r); rest=sum(r)-mx
    if mx<rest:
        strict.append(r); j=twice_area(r)
        if j<mj[0]: mj=(j,r)
    elif mx==rest: deg.append(r)
    else: non.append(r)
assert (len(strict),len(deg),len(non))==(34,18,12)
assert abs(mj[0]-math.sqrt(3)/2)<1e-12
n=0
for mags in strict:
  for signs in itertools.product([-1,1],repeat=3):
    q=[signs[i]*mags[i] for i in range(3)]
    c0=(q[2]**2-q[0]**2-q[1]**2)/(2*q[0]*q[1]); assert abs(c0)<1
    for sg in [-1,1]:
      u=complex(c0,sg*math.sqrt(1-c0*c0)); w=(-q[0]-q[1]*u)/q[2]; v=w/u
      assert abs(q[0]+q[1]*u+q[2]*u*v)<2e-12
      da=-1j*q[0]; db=1j*q[2]*w
      assert abs(abs((da.conjugate()*db).imag)-twice_area(mags))<2e-11
      n+=1
assert n==544
print('PASS', 'theta',theta,'lambda',lam,'counts',len(strict),len(deg),len(non),'minJac',mj)
