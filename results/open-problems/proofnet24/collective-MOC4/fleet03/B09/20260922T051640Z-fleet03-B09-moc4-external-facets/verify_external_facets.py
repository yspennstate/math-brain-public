#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations, combinations

S4 = list(permutations(range(4)))
S3 = list(permutations(range(3)))
IDX4 = {p:i for i,p in enumerate(S4)}

E = (
    (1,1,1),
    (1,-1,-1),
    (-1,1,-1),
    (-1,-1,1),
)
BITS = ((0,0,0),(0,1,1),(1,0,1),(1,1,0))

PAIR_CLASSES = (
    frozenset((frozenset((0,1)), frozenset((2,3)))),
    frozenset((frozenset((0,2)), frozenset((1,3)))),
    frozenset((frozenset((0,3)), frozenset((1,2)))),
)
PCIDX = {pc:i for i,pc in enumerate(PAIR_CLASSES)}

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(q)))

def inv(p):
    r=[0]*len(p)
    for i,j in enumerate(p):
        r[j]=i
    return tuple(r)

def rho_of(p):
    out=[]
    for pc in PAIR_CLASSES:
        image=frozenset(frozenset(p[i] for i in S) for S in pc)
        out.append(PCIDX[image])
    return tuple(out)

def perm_matrix(p,n):
    return tuple(tuple(F(1) if p[i]==j else F(0) for j in range(n)) for i in range(n))

def madd(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def mscale(c,A):
    return tuple(tuple(c*A[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def mtranspose(A):
    return tuple(tuple(A[i][j] for i in range(len(A))) for j in range(len(A[0])))

def mmul(A,B):
    BT=mtranspose(B)
    return tuple(tuple(sum((x*y for x,y in zip(A[i],BT[j])),F(0))
                       for j in range(len(BT))) for i in range(len(A)))

def matrix_abs_le(A,B):
    return all(abs(A[i][j]) <= B[i][j] for i in range(len(A)) for j in range(len(A[0])))

def rowsums(A):
    return tuple(sum(row,F(0)) for row in A)

def colsums(A):
    return rowsums(mtranspose(A))

J4=tuple(tuple(F(1) for _ in range(4)) for _ in range(4))
EF=tuple(tuple(F(x) for x in row) for row in E)
ET=mtranspose(EF)

def D_of_P(P):
    return mscale(F(1,4), mmul(mmul(ET,P),EF))

def qpm(R,D):
    return mscale(F(1,2),madd(R,D)), mscale(F(1,2),madd(R,mscale(F(-1),D)))

def external_vertex(tau,rhop):
    rt=rho_of(tau)
    P=mscale(F(1,3),madd(J4,mscale(F(-1),perm_matrix(tau,4))))
    D=D_of_P(P)
    R=madd(mscale(F(1,3),perm_matrix(rt,3)), mscale(F(2,3),perm_matrix(rhop,3)))
    return P,R,D

# Saxl4 feature columns P_{I,J}, k=0,1,2. k=3,4 are complementary/trivial equivalents.
FEATURES=[]
FEATURES.append(tuple(F(1) for _ in S4))
for k in (1,2):
    subsets=list(combinations(range(4),k))
    for I in subsets:
        I=set(I)
        for J in subsets:
            J=set(J)
            FEATURES.append(tuple(F(1) if {p[i] for i in I}==J else F(0) for p in S4))

def functional_signature(coeff):
    return tuple(sum((coeff[i]*feat[i] for i in range(24)),F(0)) for feat in FEATURES)

def coeff_external(tau,rhop):
    rt=rho_of(tau)
    coeff=[F(0)]*24
    for p in S4:
        if rho_of(p)==rt or rho_of(p)==rhop:
            coeff[IDX4[p]] += F(1,6)
    coeff[IDX4[tau]] -= F(1,3)
    return tuple(coeff)

def p4(s):
    return tuple(int(ch)-1 for ch in s)

# One of Drury's ten equivalent forms:
# u(f)=1/3(f(3214)+f(4132)+f(3421)+f(2341)-f(3241)).
U0=[F(0)]*24
for s,c in (("3214",1),("4132",1),("3421",1),("2341",1),("3241",-1)):
    U0[IDX4[p4(s)]] += F(c,3)
U0=tuple(U0)

def transform_coeff(c,l,r):
    out=[F(0)]*24
    rinv=inv(r)
    for s in S4:
        t=compose(compose(l,s),rinv)
        out[IDX4[t]] += c[IDX4[s]]
    return tuple(out)

def gmul(z,w):
    a,b=z; c,d=w
    return (a*c-b*d,a*d+b*c)

def gadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def endpoint_real(a,b,sig):
    z=(1,0)
    for i in range(4):
        z=gmul(z,gadd(a[i],b[sig[i]]))
    return F(z[0])

def external_value(f,tau,rhop):
    rt=rho_of(tau)
    Bt=sum((f[p] for p in S4 if rho_of(p)==rt),F(0))/4
    Bp=sum((f[p] for p in S4 if rho_of(p)==rhop),F(0))/4
    return F(2,3)*(Bt+Bp)-F(1,3)*f[tau]

def det_hexagon_singleton_violations(P,R,D):
    qp,qm=qpm(R,D)
    count=0
    for u,r in enumerate(BITS):
        for v,c in enumerate(BITS):
            N=tuple(tuple(qm[i][j] if (r[i]^c[j])==0 else qp[i][j]
                          for j in range(3)) for i in range(3))
            prods=[]
            for rho in S3:
                prod=F(1)
                for i in range(3):
                    prod*=N[i][rho[i]]
                prods.append(prod)
            # A unique positive determinant monomial and five exact zeros
            # violates det N=0 by the triangle/polygon necessity.
            positives=[x for x in prods if x>0]
            if len(positives)==1:
                count+=1
    return count

# 48 external coordinate candidates: for each tau, two pair-class derangements.
EXTERNAL=[]
for tau in S4:
    rt=rho_of(tau)
    der=[rp for rp in S3 if all(rp[i]!=rt[i] for i in range(3))]
    assert len(der)==2
    for rp in der:
        P,R,D=external_vertex(tau,rp)
        assert rowsums(P)==(F(1),)*4 and colsums(P)==(F(1),)*4
        assert rowsums(R)==(F(1),)*3 and colsums(R)==(F(1),)*3
        assert all(x>=0 for row in P for x in row)
        assert all(x>=0 for row in R for x in row)
        assert matrix_abs_le(D,R)
        qp,qm=qpm(R,D)
        assert all(x>=0 for A in (qp,qm) for row in A for x in row)
        assert det_hexagon_singleton_violations(P,R,D)==12
        EXTERNAL.append((tau,rp,P,R,D))
assert len(EXTERNAL)==48

# Exact equality of the 48 external functionals with Drury's left-right u orbit on Saxl4.
external_sigs={functional_signature(coeff_external(tau,rp)) for tau,rp,_,_,_ in EXTERNAL}
u_sigs={functional_signature(transform_coeff(U0,l,r)) for l in S4 for r in S4}
assert len(external_sigs)==48
assert len(u_sigs)==48
assert external_sigs==u_sigs

# Current campaign-lead hard support datum.
A=((-4,4),(0,-1),(-3,2),(-4,-4))
B=((-4,-4),(2,-1),(2,-4),(4,-1))
f={p:endpoint_real(A,B,p) for p in S4}
M=max(f.values())
ext_values=[external_value(f,tau,rp) for tau,rp,_,_,_ in EXTERNAL]
assert M==F(256)
assert max(ext_values)==F(178)
assert M-max(ext_values)==F(78)

print("PASS MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1")
print("saxl_feature_count =",len(FEATURES))
print("external_functionals =",len(external_sigs))
print("drury_u_orbit =",len(u_sigs))
print("external_coordinate_candidates =",len(EXTERNAL))
print("hexagon_singleton_violations_per_external = 12")
print("lead_endpoint_max =",M)
print("lead_external_max =",max(ext_values))
print("lead_external_margin =",M-max(ext_values))
