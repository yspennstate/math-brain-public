"""Independent exact verifier for C009's rational-family certificate.

Only Python's standard library is used. Polynomial identities and all Bernstein
coefficients are checked in rational arithmetic, without numerical sampling.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
from functools import reduce
from math import comb, gcd, lcm
import json
BASE=Path(__file__).resolve().parent
checks=0

def check(value):
 global checks
 assert value
 checks+=1

def trim(p):
 p=list(map(F,p))
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def add(p,q):
 r=[F(0)]*max(len(p),len(q))
 for i,x in enumerate(p):r[i]+=x
 for i,x in enumerate(q):r[i]+=x
 return trim(r)

def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return trim(r)

def scale(p,c):return trim([x*c for x in p])

def product(ps):return reduce(mul,ps,[F(1)])

def exact_div(p,q):
 r=trim(p);q=trim(q);s=[F(0)]*max(1,len(r)-len(q)+1)
 while r!=[0] and len(r)>=len(q):
  k=len(r)-len(q);z=r[-1]/q[-1];s[k]+=z
  r=add(r,[F(0)]*k+scale(q,-z))
 check(r==[0])
 return trim(s)

def determinant(M):
 n=len(M);out=[F(0)]
 for perm in permutations(range(n)):
  inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  out=add(out,scale(product(M[i][perm[i]] for i in range(n)),(-1)**inv))
 return out

def primitive(p):
 common=reduce(lcm,(x.denominator for x in p),1)
 ints=[int(x*common) for x in p]
 common=reduce(gcd,(abs(x) for x in ints),0)
 return trim([F(x,common) for x in ints])

def bernstein(p,n):
 p=list(p)+[F(0)]*(n+1-len(p))
 return [sum((p[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)),F(0)) for i in range(n+1)]

def atom_data(a,b,c,u,v):
 out=[]
 for mask in range(8):
  bits=[(mask>>i)&1 for i in range(3)];sg=[2*z-1 for z in bits]
  m=[z if bit else 1-z for z,bit in zip([a,b,c],bits)]
  p0=m[0]*m[1]*m[2]
  f=-u*sg[0]*sg[1]*m[2]-v*sg[1]*sg[2]*m[0]
  d0=[sg[i]*reduce(lambda x,y:x*y,(m[j] for j in range(3) if j!=i),F(1)) for i in range(3)]
  e=[-v*sg[0]*sg[1]*sg[2],F(0),-u*sg[0]*sg[1]*sg[2]]
  E=[[F(0) if i==j else sg[i]*sg[j]*m[3-i-j] for j in range(3)] for i in range(3)]
  out.append((bits,[p0,f],d0,e,E))
 return out

C=json.loads((BASE/'rational_family_certificate.json').read_text())
a,b,c=map(F,C['diagonal']);u,v=map(F,C['edge_squares'])
D=list(map(F,C['D_coefficients']))
linear=[[24,-23],[3,-1],[16,23],[2,1],[24,1],[3,2],[16,-1],[1,-1]]
check(D==scale(product(mul(z,z) for z in linear),F(128)))
N=[[[F(0)] for j in range(3)] for i in range(3)]
data=atom_data(a,b,c,u,v)
for bits,p,d0,e,E in data:
 check(p[0]>0 and sum(p)>=0)
 D1=exact_div(D,p);D2=exact_div(D,mul(p,p));f=p[1]
 d=[[d0[i],e[i]] for i in range(3)]
 for i in range(3):
  for j in range(3):
   q=mul(add(scale(d[j],e[i]),scale(d[i],e[j])),D1)
   q=add(q,scale(mul(mul(d[i],d[j]),D2),-f))
   q=add(q,scale(D1,f*E[i][j]));N[i][j]=add(N[i][j],q)
for i in range(3):
 for j in range(3):
  check(N[i][j][0]==0);N[i][j]=trim(N[i][j][1:])
  check(N[i][j]==list(map(F,C['N_coefficients'][i][j])))
minor_results=[]
for entry in C['minors']:
 k=entry['order'];q=primitive(determinant([[N[i][j] for j in range(k)] for i in range(k)]))
 check(q==list(map(F,entry['polynomial_coefficients'])))
 bs=bernstein(q,entry['bernstein_degree'])
 check(bs==list(map(F,entry['bernstein_coefficients'])))
 for z in bs:check(z>=0)
 check(any(z>0 for z in bs))
 minor_results.append({'order':k,'degree':len(q)-1,'bernstein_degree':entry['bernstein_degree'],'positive_coefficients':sum(z>0 for z in bs),'zero_coefficients':sum(z==0 for z in bs),'minimum_positive_coefficient_divided_by_constant':str(min(z/bs[0] for z in bs if z>0))})
# Independent exact contraction conditions for the whole interval 0 <= t < 1.
check(u/a+v/c==b)
check(u/(1-a)+v/(1-c)==F(23,40)<1-b)
# An exact two-nonzero-edge obstruction to separate positivity by X_2 slices.
slice11=F(0)
for bits,p,d0,e,E in atom_data(F(1,4),F(1,2),F(1,2),F(1,16),F(1,64)):
 if bits[1]!=0:continue
 prob=sum(p);d=d0[0]+e[0]
 slice11+=2*e[0]*d/prob-p[1]*d*d/(prob*prob)
check(slice11<0)
# Feasibility of this obstruction point.
check(F(1,16)/F(1,4)+F(1,64)/F(1,2)<F(1,2))
check(F(1,16)/F(3,4)+F(1,64)/F(1,2)<F(1,2))
out={'status':'all exact checks passed','assertions':checks,'method':'standard-library Fraction polynomial identities and Bernstein positivity','minor_certificates':minor_results,'negative_middle_zero_slice_11':str(slice11)}
(BASE/'verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
