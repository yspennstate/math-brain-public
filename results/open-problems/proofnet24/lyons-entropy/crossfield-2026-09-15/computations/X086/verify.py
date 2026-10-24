"""Exact physical coefficient checks plus a numerical diagnostic of logarithm identities."""
from itertools import product
from pathlib import Path
from fractions import Fraction
import json
import sympy as s
import math
R=s.Rational; I=s.I
checks=0

def eq(x,y,label):
    global checks
    d=x-y
    if isinstance(d,s.MatrixBase): ok=all(s.simplify(v)==0 for v in d)
    else: ok=s.simplify(d)==0
    assert ok,label
    checks+=1

def atom(K,y):
    eye=s.eye(K.rows)
    C=s.Matrix.hstack(*[(K if y[j] else eye-K)[:,j] for j in range(K.rows)])
    return s.simplify(C.det(method='domain-ge'))

def reflection(v):
    v=s.Matrix(v)
    return s.eye(len(v))-2*v*v.T/(v.T*v)[0]
Q=reflection([1,2,3,4])*s.diag(1,I,(3+4*I)/5,1)*reflection([1,1,1,1])
V=Q[:,2:]; J=s.simplify((s.eye(4)-V*V.adjoint())/2)
eq(V.adjoint()*V,s.eye(2),'isometry')
eq(J*V,s.zeros(4,2),'orthogonal background')
ys=list(product((0,1),repeat=4))
inputs=[s.zeros(2),s.eye(2),s.diag(1,0),s.diag(0,1),s.Matrix([[R(1,2),R(1,2)],[R(1,2),R(1,2)]]),s.Matrix([[R(1,2),I/2],[-I/2,R(1,2)]])]
laws=[{y:atom(s.simplify(J+V*M*V.adjoint()),y) for y in ys} for M in inputs]
M=s.Matrix([[R(49,100),(1+I)/200],[(1-I)/200,R(51,100)]])
A=s.Matrix([[R(2,3),(1+2*I)/20],[(1-2*I)/20,R(3,5)]])
E={}; P={}; G={}; S={}; q={}
for y in ys:
    alpha,gamma,b1,b2,br,bi=[L[y] for L in laws]
    z=s.simplify(br-(b1+b2)/2+I*(bi-(b1+b2)/2))
    B=s.Matrix([[b1,z],[s.conjugate(z),b2]])
    E[y]=(alpha,B,gamma)
    eq(B.det(),alpha*gamma,'local Gaussian effect')
    q[y]=s.simplify(alpha+gamma-s.trace(B))
    P[y]=s.simplify(alpha+s.trace((B-alpha*s.eye(2))*M)+q[y]*M.det())
    G[y]=s.simplify(B-alpha*s.eye(2)+q[y]*M.adjugate())
    S[y]=s.simplify(G[y]/P[y])
    eq(G[y].det(),q[y]*P[y],'local gradient determinant')
    eq(P[y],atom(s.simplify(J+V*M*V.adjoint()),y),'measured atom')
eq(sum(P.values()),1,'normalization')
eq(sum(q.values()),0,'acceleration normalization')
eq(sum((P[y]*S[y] for y in ys),s.zeros(2)),s.zeros(2),'centered score')
fibers={}
for y in ys:
    for z in ys:
        w=tuple(a+b for a,b in zip(y,z))
        fibers.setdefault(w,[]).append((y,z))
for w,pairs in fibers.items():
    val=sum(P[y]*P[z]*(S[y]-S[z]).det() for y,z in pairs)
    eq(val,0,'conditional exterior area '+str(w))
# Pauli tetrahedral frame data; exact complex Bloch vectors.
sig=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
ns=[s.Matrix([0,0,1]),s.Matrix([2*s.sqrt(2)/3,0,-R(1,3)]),s.Matrix([-s.sqrt(2)/3,s.sqrt(6)/3,-R(1,3)]),s.Matrix([-s.sqrt(2)/3,-s.sqrt(6)/3,-R(1,3)])]
Hs=[s.simplify((sig[0]+sum((n[j]*sig[j+1] for j in range(3)),s.zeros(2)))/4) for n in ns]
eq(sum(Hs,s.zeros(2)),s.eye(2),'tetra Parseval')
eq(sum((n*n.T for n in ns),s.zeros(3)),s.eye(3)*R(4,3),'tetra second moment')
for H in Hs:
    eq(H.det(),0,'tetra rank one')
    eq(s.trace(H),R(1,2),'tetra row norm')
assert Hs[0]*Hs[1]-Hs[1]*Hs[0]!=s.zeros(2)
checks+=1
central=[]
for y in ys:
    Sy=2*sum(((2*y[i]-1)*Hs[i] for i in range(4)),s.zeros(2))
    central.append(s.Matrix([s.simplify(s.trace(Sy*P)/2) for P in sig]))
eq(sum((v*v.T/16 for v in central),s.zeros(4)),s.diag(1,R(1,3),R(1,3),R(1,3)),'central full score moment')
gap=R(16384,12291)-R(262144,250047)
assert gap>R(1,4);checks+=1
# Logarithm identities are evaluated only as algebra diagnostics, not used for theorem signs.
num=lambda x:float(s.N(s.re(x),18))
F=sum(num(P[y])*num(s.trace(A*S[y]))**2 for y in ys)
Qlog=sum(num(q[y])*math.log(num(P[y])) for y in ys)
L=0.; decomposition=0.; maxosc=0.
for w,pairs in fibers.items():
    masses=[num(P[y]*P[z]) for y,z in pairs]
    total=sum(masses);mx=max(masses);mn=min(masses)
    maxosc=max(maxosc,math.log(mx/mn))
    for (y,z),m in zip(pairs,masses):
        D=S[y]-S[z]
        dd=num(D.det());lin=num(s.trace(A*D));omega=math.log(mx/m)
        L+=m*dd*math.log(m/total)
        disc=lin*lin-4*num(A.det())*dd
        assert disc>-1e-10
        decomposition+=m*((2-omega)*lin*lin+omega*disc)/4
assert abs(L-2*Qlog)<2e-11
assert abs(decomposition-(F+2*num(A.det())*Qlog))<2e-11
out={'exact_assertions':checks,'physical_outcomes':len(ys),'all_coefficient_fibers':len(fibers),'central_tetra_moment':['1','1/3','1/3','1/3'],'proved_radius':'1/128','full_Hessian_Frobenius_bound':'1/8','intermediate_gap':str(gap),'diagnostic_fiber_oscillation':maxosc,'diagnostic_log_identity_error':abs(L-2*Qlog),'diagnostic_decomposition_error':abs(decomposition-(F+2*num(A.det())*Qlog))}
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
