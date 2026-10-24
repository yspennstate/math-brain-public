"""Exact local identities and a corrected failed-PSD certificate for X020.

The cut theorem is analytic in agents/X020.md. This verifier independently
checks finite cofactor identities and records one rational counterexample to
dropping decomposability in the attempted operator extension.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import numpy as np

PAIRS=list(combinations(range(6),2))
TRIPLES=list(combinations(range(6),3))
VP=list(combinations(range(4),2))

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def trans(A): return [list(c) for c in zip(*A)]
def mul(A,B): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def outer(x): return [[a*b for b in x] for a in x]
def det(A):
 A=[r[:] for r in A]; ans=F(1)
 for j in range(len(A)):
  k=next((k for k in range(j,len(A)) if A[k][j]),None)
  if k is None:return F(0)
  if k!=j:A[k],A[j]=A[j],A[k];ans=-ans
  pivot=A[j][j];ans*=pivot
  for k in range(j+1,len(A)):
   f=A[k][j]/pivot
   for l in range(j+1,len(A)): A[k][l]-=f*A[j][l]
 return ans
def reflector(v):
 n=sum(a*a for a in v)
 return [[F(i==j)-F(2*v[i]*v[j],n) for j in range(6)] for i in range(6)]
Q=mul(mul(reflector([1,2,3,4,5,6]),reflector([2,-1,3,-2,1,4])),reflector([3,1,-2,4,2,-1]))
assert mul(trans(Q),Q)==eye(6)
U=[r[:2] for r in Q]; V=[r[2:] for r in Q]
def minors(cols,rows): return det([[Q[i][j] for j in cols] for i in rows])
h=[minors([0,1],p)**2 for p in PAIRS]
T=[[minors([0,1,2+s],m) for s in range(4)] for m in TRIPLES]
assert mul(trans(T),T)==eye(4)
effects=[outer(row) for row in T]
for m,E in zip(TRIPLES,effects):
 assert sum(E[i][i] for i in range(4))==sum(h[j] for j,p in enumerate(PAIRS) if set(p)<=set(m))
def Bmat(family):
 out=[[F(0) for _ in range(4)] for _ in range(4)]
 for j in family:out=add(out,effects[j])
 return out
def shifted(A,t):return [[F(t)*(i==j)-A[i][j] for j in range(len(A))] for i in range(len(A))]
for j,p in enumerate(PAIRS):
 inds=[i for i,m in enumerate(TRIPLES) if set(p)<=set(m)]
 B=Bmat(inds);s=sum(U[i][k]**2 for i in p for k in range(2));hh=h[j]
 for t in range(5):assert det(shifted(B,t))==(F(t*t)-s*t+hh)*(F(t)-hh)**2
 for omit in inds:
  B3=Bmat([i for i in inds if i!=omit])
  assert det(B3)==0 and det(shifted(B3,hh))==0

# Exact sign check for a rational nondecomposable two-form.
mask=980443
inds=[i for i in range(20) if mask>>i&1]
d=[sum(set(p)<=set(TRIPLES[i]) for i in inds) for p in PAIRS]
Z=[[det([[V[i][j] for j in pp] for i in p]) for pp in VP] for p in PAIRS]
TS=[[[det([[V[i][a],V[i][b],U[i][s]] for i in m]) for a,b in VP] for m in TRIPLES] for s in range(2)]
HH=[[sum(Z[p][i]*Z[p][j]*min(2,d[p]) for p in range(15))-sum(TS[s][m][i]*TS[s][m][j] for s in range(2) for m in inds) for j in range(6)] for i in range(6)]
vals,vecs=np.linalg.eigh(np.array(HH,dtype=float))
z=[int(round(float(x)*1000000)) for x in vecs[:,0]]
energy=sum(F(z[i])*HH[i][j]*z[j] for i in range(6) for j in range(6))
norm=sum(v*v for v in z)
plucker=z[0]*z[5]-z[1]*z[4]+z[2]*z[3]
assert energy<0 and plucker!=0
out={'orthogonal_frame_exact':True,'cofactor_isometry_exact':True,'trace_identities':20,'full_pair_star_characteristic_polynomials':15,'partial_pair_star_zero_and_h_roots':60,'failed_psd_extension':{'family':[TRIPLES[i] for i in inds],'integer_two_form_coordinates':z,'plucker_quadric_value':plucker,'exact_normalized_rayleigh_quotient':str(energy/norm),'float_normalized_rayleigh_quotient':float(energy/norm)}}
Path(__file__).with_name('verified_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
