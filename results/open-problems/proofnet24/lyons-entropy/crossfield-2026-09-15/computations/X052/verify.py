#!/usr/bin/env python3
"""Exact determinant jets and high-precision log checks for X052."""
import json
from pathlib import Path
import sympy as s
import mpmath as mp
import numpy as np
mp.mp.dps=90
checks=0
def check(x):
 global checks
 assert bool(x)
 checks+=1
def num(x):
 return mp.mpf(str(s.N(s.re(x),100)))
I=s.I
n=4
eps=s.Rational(1,2**32)
V=s.Matrix([[1,1],[1,I],[1,-1],[1,-I]])/2
check(V.conjugate().T*V==s.eye(2))
N0=s.diag(eps,s.Rational(1,2))
N=N0+eps*s.Matrix([[1,I],[-I,-1]])/8
M=N-s.eye(2)/2
D=s.eye(n)/2
K=D+V*M*V.conjugate().T
E=s.Matrix([[1,(1+I)/3],[(1-I)/3,2]])
check(s.det(E)==s.Rational(16,9))
check(N*E!=E*N)
check((N-N0)**2==eps**2*s.eye(2)/32)
Hs=[s.diag(1,0),s.diag(0,1),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,I],[-I,0]])]
A=V*E*V.conjugate().T
q=s.Rational(1,2**n)
z=s.symbols('z',real=True)
atoms={}
grads={}
seconds={}
for mask in range(2**n):
 bits=[(mask>>i)&1 for i in range(n)]
 eta=s.diag(*[2 if b else -2 for b in bits])
 T=V.conjugate().T*eta*V
 f=s.expand(s.det(s.eye(2)+(M+z*E)*T))
 cols=[]
 for j,b in enumerate(bits):
  cols.append((K+z*A)[:,j] if b else (s.eye(n)-K-z*A)[:,j])
 direct=s.expand(s.det(s.Matrix.hstack(*cols)))
 check(s.expand(direct-q*f)==0)
 p=s.factor(direct.subs(z,0))
 check(p>0)
 atoms[mask]=p
 seconds[mask]=s.expand(direct).coeff(z,2)*2
 check(seconds[mask]==2*s.det(E)*q*s.det(T))
 grads[mask]=[s.simplify(q*s.trace((s.eye(2)+M*T).inv()*H*T)*s.det(s.eye(2)+M*T)) for H in Hs]
check(sum(atoms.values())==1)
for k in range(4): check(sum(grads[x][k] for x in atoms)==0)
check(sum(seconds.values())==0)
J=mp.mpf('0')
C=np.zeros((n,n))
Cexact=s.zeros(n)
for i in range(n):
 for j in range(i+1,n):
  c=s.simplify(abs(V[[i,j],:].det())**2)
  C[i,j]=C[j,i]=float(c)
  Cexact[i,j]=Cexact[j,i]=c
  for mask in range(2**n):
   if mask&(1<<i) or mask&(1<<j): continue
   p00=atoms[mask]; p10=atoms[mask|(1<<i)]; p01=atoms[mask|(1<<j)]; p11=atoms[mask|(1<<i)|(1<<j)]
   check(p10*p01>=p00*p11)
   if mask==(2**n-1)-(1<<i)-(1<<j):
    check(p10*p01>2**20*p00*p11)
   J+=num(c)*mp.log(num(p10*p01/(p00*p11)))/2**(n-2)
FI=s.zeros(4)
for mask,p in atoms.items():
 g=s.Matrix(grads[mask]); FI+=g*g.T/p
FIE=sum(num((sum(grads[mask][k]*[1,2,s.Rational(1,3),s.Rational(1,3)][k] for k in range(4)))**2/p) for mask,p in atoms.items())
negH=FIE+sum(num(seconds[x])*mp.log(num(atoms[x])) for x in atoms)
check(abs(negH-(FIE-2*num(s.det(E))*J))<mp.mpf('1e-65'))
def mix(P,Q): return s.simplify((s.trace(P)*s.trace(Q)-s.trace(P*Q))/2)
p0=atoms[0]; pf=atoms[2**n-1]
Cp=s.simplify(V.conjugate().T*K.inv()*V)
Cm=s.simplify(V.conjugate().T*(s.eye(n)-K).inv()*V)
check(Cp==N.inv())
check(Cm==(s.eye(2)-N).inv())
check(pf==s.det(N)/2**(n-2))
check(p0==s.det(s.eye(2)-N)/2**(n-2))
pdet=s.factor(pf*s.det(Cp)); qdet=s.factor(p0*s.det(Cm))
check(pdet==s.Rational(1,2**(n-2)))
check(pdet==qdet)
md=num(mix(Cp,Cm))*mp.sqrt(num(p0*pf))
cap=num(pdet+qdet)+mp.sqrt(num((pdet-qdet)**2)+4*md**2)
d=num(s.det(N)); d0=num(s.det(s.eye(2)-N))
T=(num(s.trace(N))-2*d)/(2*mp.sqrt(d*d0))
check(abs(cap-mp.mpf(2)**(3-n)*(1+T))<mp.mpf('1e-65'))
check(FIE>=2*num(s.det(E))*cap)
check(cap>J)
Sigma=s.Matrix(n,n,lambda i,j: K[i,i]*(1-K[i,i]) if i==j else -abs(K[i,j])**2)
check(sum(Cexact[i,j] for i in range(n) for j in range(i+1,n))==1)
for k in range(1,n+1):
 check((3*Sigma-Cexact)[:k,:k].det()>0)
Sn=np.array(Sigma,dtype=complex).real
Lambda=float(max(np.linalg.eigvals(np.linalg.solve(Sn,C)).real))
check(J>Lambda)
Q=s.zeros(4);Q[0,1]=Q[1,0]=s.Rational(1,2);Q[2,2]=Q[3,3]=-1
G=mp.matrix(4)
for i in range(4):
 for j in range(4): G[i,j]=num(FI[i,j])-2*J*num(Q[i,j])
evals=mp.eigsy(G,eigvals_only=True)
check(min(evals)>0)
# General two-positive-matrix mixed-area minimization, exact rational diagonal test.
P=s.diag(2,3); R=s.diag(5,7)
alpha=P[0,0]**2+R[0,0]**2
beta=P[1,1]**2+R[1,1]**2
exact=2*(s.det(P)+s.det(R)+s.sqrt((s.det(P)-s.det(R))**2+4*mix(P,R)**2))
check(s.simplify(exact-2*(s.sqrt(alpha*beta)+s.det(P)+s.det(R)))==0)
# Congruence invariance in a nonsymmetric positive example.
W=s.Matrix([[1,1],[0,1]])
check(mix(W.T*P*W,W.T*R*W)==mix(P,R))
out={"exact_and_high_precision_checks":checks,"n":n,"epsilon":str(eps),"J":str(J),"linear_design_Lambda":Lambda,"endpoint_mixed_area_capacity":str(cap),"direction_FI":str(FIE),"direction_negative_entropy_curvature":str(negH),"full_active_negative_Hessian_eigenvalues":[str(v) for v in evals],"identity_tolerance":"1e-65","scope":"Analytic theorem; finite checks supplement it."}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
