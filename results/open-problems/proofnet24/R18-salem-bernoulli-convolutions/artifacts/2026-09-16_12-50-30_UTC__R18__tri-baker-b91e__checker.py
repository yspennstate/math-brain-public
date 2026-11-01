#!/usr/bin/env python3
from fractions import Fraction
import itertools
D=10
mc=[1,1,0,-1,-1,-1,-1,-1,0,1,1]
def mval(x): return x**10+x**9-x**7-x**6-x**5-x**4-x**3+x+1
x0=Fraction(147,125); v=mval(x0)
assert v<0 and x0**13>8
print('m_L(147/125) =',v)
print('(147/125)^13 =',x0**13,'> 8')
print('Thus the Salem root theta_L>147/125 and theta_L^13>8.')
def mulx(v):
    w=[0]*D
    for i,a in enumerate(v):
        if i+1<D: w[i+1]+=a
        else:
            for j in range(D): w[j]-=a*mc[j]
    return tuple(w)
powers=[(1,)+(0,)*(D-1)]
for n in range(1,25): powers.append(mulx(powers[-1]))
Q=[-4,-3,-2,-1,1,2,3,4]
tested=0; solutions=[]
for a in range(1,13):
  for b in range(1,13):
    pa=powers[a]; pn=powers[a+b]
    for q1,q2,q3 in itertools.product(Q,repeat=3):
      tested+=1
      rem=tuple(q1*(1 if j==0 else 0)+q2*pa[j]+q3*pn[j] for j in range(D))
      if all(x==0 for x in rem): solutions.append((a,b,q1,q2,q3))
print('exact tuples tested =',tested)
print('exact divisibility solutions =',solutions)
assert tested==73728 and solutions==[]
print('PASS: no residual-alphabet three-term multiple of m_L.')
