import sympy as sp, json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
z=sp.Symbol('z');n=4;edges=list(combinations(range(n),2));small=[0]+[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i,j in edges];tail=[s for s in range(16) if s.bit_count()>=3]
x=list(map(sp.Integer,[200,201,202,208]));r=list(map(sp.Integer,[600,1600,400,2000]));L=sp.Matrix(4,4,lambda i,j:2*r[i]*r[j]/(x[i]+x[j]))
w=[]
for s in range(16):
 ids=[i for i in range(4) if s>>i&1]
 v=sp.prod(r[i]**2/x[i] for i in ids)*sp.prod(((x[i]-x[j])/(x[i]+x[j]))**2 for i,j in combinations(ids,2));w.append(v)
Z=sum(w[s]*z**s.bit_count() for s in range(16))
print('weights done',flush=True)
J=sp.eye(4)+z*L
adj=J.adjugate(method='domain-ge');Pnum=sp.simplify(z*L*adj)
assert sp.expand(J.det(method='domain-ge')-Z)==0
for v in Pnum:assert sp.Poly(v,z).degree()<=4
print('K polynomial done',flush=True)
D=sp.zeros(6,10)
for e,(i,j) in enumerate(edges):D[e,i]=Pnum[j,j];D[e,j]=Pnum[i,i];D[e,4+e]=-2*Pnum[i,j]
A=sp.zeros(4,10)
for i in range(4):A[i,i]=Z
M=sp.zeros(11,10);M[0,:]=-sp.ones(1,4)*A+sp.ones(1,6)*D
for i in range(4):
 M[1+i,:]=A[i,:]-sum((D[e,:] for e,ed in enumerate(edges) if i in ed),sp.zeros(1,10))
for e in range(6):M[5+e,:]=D[e,:]
alpha=[sp.Integer(5)]+[sp.Rational(51,50)]*10
# Lagrange values g_S(T) are coefficients of degree<=2 interpolants on low counts.
def g(s,t):
 k=t.bit_count()
 if s==0:return 1-k+k*(k-1)//2
 if s.bit_count()==1:return (2-k)*int(s&t==s)
 return int(s&t==s)
for idx,s in enumerate(small):
 worst=w[s]+sum(w[t]*abs(g(s,t))*sum(abs(g(a,t)) for a in small) for t in tail)
 assert worst<alpha[idx]*w[s],(s,worst/w[s])
print('Gram alpha bounds done',flush=True)
# Bounds [floor(c*1000)/1000, floor(c*1000+1)/1000] verified by final verifier.
clo=[sp.Rational(11987,1000),sp.Rational(10606,1000),sp.Rational(7863,1000),sp.Rational(11997,1000),sp.Rational(8135,1000),sp.Rational(8448,1000)]
Fhat=sp.zeros(10)
for i in range(4):Fhat[i,i]=sp.Rational(3,1000)
for c,(i,j),e in zip(clo,edges,range(6)):Fhat[i,j]=Fhat[j,i]=c;Fhat[4+e,4+e]=-2*c
# z^2 Z (lower Fisher - upper frozen curvature)
Q=sp.zeros(10)
for a,s in enumerate(small):Q+=z**(2-s.bit_count())*(M[a,:].T*M[a,:])/(alpha[a]*w[s])
Q-=z**2*Z*Fhat
print('matrix polynomial formed',flush=True)
coeffs=[sp.zeros(10) for _ in range(11)]
for i in range(10):
 for j in range(i,10):
  pol=sp.Poly(sp.expand(Q[i,j]),z)
  for (k,),v in pol.terms():coeffs[k][i,j]=coeffs[k][j,i]=v
while coeffs and coeffs[-1]==sp.zeros(10):coeffs.pop()
print('degree',len(coeffs)-1,flush=True)
def dumpmat(mat):return [[str(v) for v in mat.row(i)] for i in range(mat.rows)]
data={'x':list(map(str,x)),'r':list(map(str,r)),'L':dumpmat(L),'weights':list(map(str,w)),'Z_coefficients':[str(sp.expand(Z).coeff(z,k)) for k in range(5)],'K_numerator_coefficients':[dumpmat(Pnum.applyfunc(lambda v:sp.expand(v).coeff(z,k))) for k in range(5)],'polynomial_coefficients':[dumpmat(v) for v in coeffs],'alpha':list(map(str,alpha)),'small_masks':small,'log_lower':list(map(str,clo))}
Path('computations/C053/polynomial_data.json').write_text(json.dumps(data,indent=2))
print('saved',flush=True)
