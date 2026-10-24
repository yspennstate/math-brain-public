from fractions import Fraction as Q
from itertools import permutations, combinations

S4=list(permutations(range(4)))
Splus={
 (0,2,3,1),(0,3,1,2),(1,2,0,3),(1,3,2,0),
 (2,0,1,3),(2,1,3,0),(3,0,2,1),(3,1,0,2),
}
Sminus={
 (0,1,3,2),(0,2,1,3),(1,0,2,3),(1,3,0,2),
 (2,0,3,1),(2,3,1,0),(3,1,2,0),(3,2,0,1),
}
assert len(Splus)==len(Sminus)==8 and not (Splus&Sminus)

def Z(r=0,i=0): return (Q(r),Q(i))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x): return (x[0],-x[1])
def scale(c,x): return (c*x[0],c*x[1])
def n2(x): return x[0]*x[0]+x[1]*x[1]
def sumz(xs):
    out=Z()
    for x in xs: out=add(out,x)
    return out

def mm(A,B):
    return [[sumz(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def diag(v): return [[v[i] if i==j else Z() for j in range(4)] for i in range(4)]
def sign(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1

def det(A):
    n=len(A)
    if n==0: return Z(1)
    out=Z()
    for p in permutations(range(n)):
        s=-1 if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2 else 1
        t=Z(1)
        for i in range(n): t=mul(t,A[i][p[i]])
        out=add(out,scale(Q(s),t))
    return out

def minor(U,I,J): return det([[U[i][j] for j in J] for i in I])

def H(z):
    rows=[
      [Z(1),Z(1),Z(1),Z(1)],
      [Z(1),z,Z(-1),scale(Q(-1),z)],
      [Z(1),Z(-1),Z(1),Z(-1)],
      [Z(1),scale(Q(-1),z),Z(-1),z],
    ]
    return [[scale(Q(1,2),x) for x in row] for row in rows]

def law(r):
    nu={p:Q(0) for p in S4}
    for p in Splus: nu[p]=(1+r)/16
    for p in Sminus: nu[p]=(1-r)/16
    assert min(nu.values())>=0 and sum(nu.values())==1
    return nu

def check_all_compounds(U,nu):
    I4=[[Z(1 if i==j else 0) for j in range(4)] for i in range(4)]
    assert mm(U,adj(U))==I4
    for k in range(5):
        subs=list(combinations(range(4),k))
        for I in subs:
            FI=frozenset(I)
            for J in subs:
                actual=n2(minor(U,I,J))
                lifted=sum(w for p,w in nu.items()
                           if frozenset(p[j] for j in J)==FI)
                assert actual==lifted, (k,I,J,actual,lifted)

# Endpoint laws: direct finite certificates for the two real Hadamards.
check_all_compounds(H(Z(1)),law(Q(1)))
check_all_compounds(H(Z(-1)),law(Q(-1)))

# Nontrivial exact interior phase z=3/5+4i/5.
z=Z(Q(3,5),Q(4,5))
U=H(z)
nu=law(Q(3,5))
check_all_compounds(U,nu)
assert sorted(set(nu.values()))==[Q(0),Q(1,40),Q(1,10)]

# Exact Cauchy-Binet / target-hull equality for generic Gaussian-integer spectra.
a=[Z(2,1),Z(-1,3),Z(4,-2),Z(-3,-1)]
b=[Z(1,-2),Z(3,1),Z(-2,2),Z(5,-1)]
B=mm(mm(U,diag(b)),adj(U))
D=det([[add(diag(a)[i][j],B[i][j]) for j in range(4)] for i in range(4)])
def vertex(p):
    out=Z(1)
    for j in range(4): out=mul(out,add(a[p[j]],b[j]))
    return out
Dlift=sumz(scale(w,vertex(p)) for p,w in nu.items())
assert D==Dlift==(Q(-466,5),Q(143,5))

print('PASS MOC4-COMPLEX-HADAMARD-COMMON-LIFT-v1')
print('phase = 3/5 + 4i/5')
print('weights: 8 x 1/10, 8 x 1/40, 8 x 0')
print('all k=0,1,2,3,4 compound marginals matched exactly')
print('det =',D)
