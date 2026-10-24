#!/usr/bin/env python3
"""Exact n=4 counterexample to full exterior-operator PSD.
Uses only the Python standard library. Every scalar operation is rational or
Gaussian rational; there is no floating-point test in this certificate.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations
import json
from pathlib import Path

@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    @staticmethod
    def of(x): return x if isinstance(x,G) else G(F(x))
    def __add__(self,other):
        o=G.of(other);return G(self.re+o.re,self.im+o.im)
    __radd__=__add__
    def __neg__(self): return G(-self.re,-self.im)
    def __sub__(self,o): return self+-G.of(o)
    def __rsub__(self,o): return G.of(o)+-self
    def __mul__(self,other):
        o=G.of(other)
        return G(self.re*o.re-self.im*o.im,self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def conjugate(self): return G(self.re,-self.im)
    def __str__(self):
        if not self.im:return str(self.re)
        return f'({self.re})+({self.im})i'

Z=G(); ONE=G(1); II=G(0,1)

def sign(p):return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def det(M):
    return sum((sign(p)*product(M[i][p[i]] for i in range(len(M))) for p in permutations(range(len(M)))),Z)

def product(xs):
    ans=ONE
    for x in xs:ans=ans*x
    return ans

def minor(M,rows,cols):return [[M[i][j] for j in cols] for i in rows]
def adjoint(M):return [[M[j][i].conjugate() for j in range(len(M))] for i in range(len(M[0]))]
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n):return [[G(int(i==j)) for j in range(n)] for i in range(n)]
def qform(x,T):return sum((x[i].conjugate()*T[i][j]*x[j] for i in range(len(x)) for j in range(len(x))),Z)
def mat_equal(A,B):return A==B

def poly_mul(a,b):
    out=[Z for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return out

def det_poly(K,A):
    n=len(K);out=[Z for _ in range(n+1)]
    for p in permutations(range(n)):
        term=[G(sign(p))]
        for i in range(n):term=poly_mul(term,[K[i][p[i]],A[i][p[i]]])
        for j,a in enumerate(term):out[j]=out[j]+a
    return out

N=4; pairs=list(combinations(range(N),2)); E=15
c=[0]*16
for m in [12,7,11]:c[m]=1
c[15]=-1
f=[sum(c[t] for t in range(16) if t&~s==0) for s in range(16)]
supermod=[]
for i,j in pairs:
    p=(1<<i)|(1<<j)
    for t in range(16):
        if t&p:continue
        d=f[t|p]+f[t]-f[t|1<<i]-f[t|1<<j]
        assert d>=0
        supermod.append({'pair':[i+1,j+1],'context':[k+1 for k in range(4) if t>>k&1],'difference':d})
assert len(supermod)==24

def exterior_coefficient(K):
    # T[I,J] = sum_S c[S] (-1)^(sum positions of I and J in S)
    #                  det K[S\\J,S\\I]. This is a polynomial cofactor formula.
    T=[[Z for _ in pairs] for _ in pairs]
    for mask,coef in enumerate(c):
        if not coef:continue
        S=[i for i in range(N) if mask>>i&1]; pos={x:j for j,x in enumerate(S)}
        for a,I in enumerate(pairs):
            if not set(I)<=set(S):continue
            for b,J in enumerate(pairs):
                if not set(J)<=set(S):continue
                sgn=(-1)**sum(pos[x] for x in I+J)
                T[a][b]=T[a][b]+coef*sgn*det(minor(K,[i for i in S if i not in J],[i for i in S if i not in I]))
    assert T==adjoint(T)
    return T

P=[[G(F(int(i==j or {i,j} in [{0,2},{1,3}]),2)) for j in range(4)] for i in range(4)]
assert P==adjoint(P) and mm(P,P)==P
assert sum((P[i][i] for i in range(4)),Z)==G(2)
eta=F(1,20)
K=[[(1-2*eta)*P[i][j]+(eta if i==j else 0) for j in range(4)] for i in range(4)]
T0=exterior_coefficient(P);T=exterior_coefficient(K)
x=list(map(G,[1,0,1,-1,0,0]))
assert qform(x,T0)==G(F(-1,4))
assert qform(x,T)==G(F(-11,200))
assert qform(x,T)==G(-F(1,4)+4*eta-2*eta*eta)
plucker=x[0]*x[5]-x[1]*x[4]+x[2]*x[3]
assert plucker==G(-1)

# A genuinely complex, Gaussian-rational version, using coordinate phases.
d=[ONE,II,ONE,ONE]
Kc=[[d[i]*K[i][j]*d[j].conjugate() for j in range(4)] for i in range(4)]
wedge_d=[d[i]*d[j] for i,j in pairs]
xc=[wedge_d[i]*x[i] for i in range(6)]
Tc=exterior_coefficient(Kc)
assert Tc==[[wedge_d[i]*T[i][j]*wedge_d[j].conjugate() for j in range(6)] for i in range(6)]
assert qform(xc,Tc)==G(F(-11,200))
plucker_c=xc[0]*xc[5]-xc[1]*xc[4]+xc[2]*xc[3]
assert plucker_c==-II

# Independent determinant-polynomial check of the normalization and orientation
# for a genuinely complex Hermitian direction at the complex interior kernel.
A=[[G(2),G(1,1),G(-1,2),II],
   [G(1,-1),G(-1),G(2),G(-1,-1)],
   [G(-1,-2),G(2),G(3),G(1)],
   [-II,G(-1,1),G(1),G(0)]]
assert A==adjoint(A)
coefficient_t2=Z
for mask,coef in enumerate(c):
    if coef:
        S=[i for i in range(4) if mask>>i&1]
        coefficient_t2=coefficient_t2+coef*det_poly(minor(Kc,S,S),minor(A,S,S))[2]
wedge_A=[[det(minor(A,I,J)) for J in pairs] for I in pairs]
trace= sum((Tc[i][j]*wedge_A[j][i] for i in range(6) for j in range(6)),Z)
assert trace==coefficient_t2

# Verify the complete boundary spectrum by its exact characteristic polynomial.
negative_T0=[[-a for a in row] for row in T0]
char=det_poly(negative_T0,eye(6))
expected=poly_mul([G(F(-1,4)),G(-1),G(1)],poly_mul(poly_mul([G(F(-1,2)),ONE],[G(F(-1,2)),ONE]),poly_mul([G(F(-1,2)),ONE],[G(F(-1,2)),ONE])))
assert char==expected

out={
 'status':'PASS: all arithmetic is exact rational or Gaussian rational',
 'pair_order':[[i+1,j+1] for i,j in pairs],
 'mobius':{str([i+1 for i in range(4) if m>>i&1]):v for m,v in enumerate(c) if v},
 'function_values_mask_order':f,
 'supermodularity_inequalities':supermod,
 'projection_matrix':P,'projection_operator':T0,
 'eta':eta,'interior_matrix':K,'interior_operator':T,
 'bivector':x,'projection_pairing':qform(x,T0),'interior_pairing':qform(x,T),
 'plucker':plucker,
 'complex_interior_matrix':Kc,'complex_bivector':xc,
 'complex_pairing':qform(xc,Tc),'complex_plucker':plucker_c,
 'coefficient_t2_check':coefficient_t2,
 'projection_characteristic_polynomial_ascending':char,
 'limits':'This disproves full T_f PSD for arbitrary supermodular f. It is not an entropy counterexample or a negative decomposable-vector pairing.'
}
path=Path(__file__).with_name('030_exterior_exact_certificate_output.json')
path.write_text(json.dumps(out,default=str,indent=2)+'\n')
print(out['status'])
print('q_projection =',qform(x,T0))
print('q_interior =',qform(x,T))
print('q_complex_interior =',qform(xc,Tc))
print('Plucker real =',plucker,'; complex =',plucker_c)
print('All 24 supermodularity inequalities hold exactly.')
print('Complex determinant t^2 coefficient = tr(T wedge^2 A) =',trace)
print('Boundary characteristic polynomial = (t-1/2)^4 (t^2-t-1/4).')
print('Saved',path)
