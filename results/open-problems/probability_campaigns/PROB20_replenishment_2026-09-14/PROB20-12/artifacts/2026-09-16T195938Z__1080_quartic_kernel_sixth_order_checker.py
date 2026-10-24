from sympy import Matrix,Rational,simplify,factor,symbols,zeros,eye
from itertools import combinations

EDGES=list(combinations(range(6),2)); EIDX={e:i for i,e in enumerate(EDGES)}
COLS=[(0,1),(2,3),(4,5)]

def coeffvec(nonzero):
    v=[0]*45
    for c,e,a in nonzero: v[15*c+EIDX[tuple(e)]]=a
    return v

V1080=coeffvec(
    [(0,e,1) for e in [(0,1),(4,5)]]+
    [(1,e,-1) for e in [(2,3),(2,4),(3,5)]]+
    [(2,e,-1) for e in [(0,2),(0,3),(1,2),(1,3),(2,3),(2,5),(3,4)]])

Qeq=Matrix([
 [Rational(4,17),-Rational(10,17),-Rational(2,17),Rational(13,17),0,0],
 [Rational(2,17),-Rational(5,17),Rational(16,17),-Rational(2,17),0,0],
 [0,0,0,0,Rational(4,5),Rational(3,5)],
 [Rational(13,17),Rational(10,17),Rational(2,17),Rational(4,17),0,0],
 [0,0,0,0,Rational(3,5),-Rational(4,5)],
 [Rational(10,17),-Rational(8,17),-Rational(5,17),-Rational(10,17),0,0]])
assert simplify(Qeq.T*Qeq-eye(6))==zeros(6)

def E(i,j):
    M=zeros(6); M[i,j]=1; M[j,i]=-1; return M

# Hessian-kernel coordinate map from the prior exact checker.
def B_from_z(z):
    return (z[0]*E(0,1) + z[1]*E(0,3) + z[2]*E(0,5)
            + z[3]*(2*E(0,2)+E(1,2)) + z[4]*E(1,3)
            + z[5]*E(1,5) + z[6]*E(2,4) + z[7]*E(2,5)
            + z[8]*E(3,5))

def objective_series_coeffs(B, order=6):
    # Exact Cayley expansion: (I-tB)(I+tB)^(-1)Q = Q + sum_{n>=1} 2(-1)^n t^n B^n Q.
    Qc=[Qeq]
    for n in range(1,order+1):
        Qc.append(2*((-1)**n)*(B**n)*Qeq)
    coeff=[Rational(0)]*(order+1)
    for c,(ca,cb) in enumerate(COLS):
        for edge in EDGES:
            w=V1080[15*c+EIDX[edge]]
            if not w: continue
            i,j=edge
            minor=[]
            for n in range(order+1):
                minor.append(sum(Qc[k][i,ca]*Qc[n-k][j,cb]-Qc[k][j,ca]*Qc[n-k][i,cb]
                                 for k in range(n+1)))
            for n in range(order+1):
                coeff[n] += w*sum(minor[k]*minor[n-k] for k in range(n+1))
    return [factor(simplify(x)) for x in coeff]

# CASE I: z3=0; a nontrivial quartic-null branch with z7 potentially nonzero.
a,b,c,d,r=symbols('a b c d r', real=True)
zI=[a,b,2*d,0,c,d,0,r,0]
BI=B_from_z(zI)
coI=objective_series_coeffs(BI,6)
assert all(simplify(x)==0 for x in coI[:6])
Q1=100*a*a-480*a*b+960*a*c+2232*b*b-3148*b*c+4593*c*c
expectedI=-Rational(4,289)*d*d*r*r*Q1
assert simplify(coI[6]-expectedI)==0
M1=Matrix([[100,-240,480],[-240,2232,-1574],[480,-1574,4593]])
assert M1[:1,:1].det()==100
assert M1[:2,:2].det()==165600
assert M1.det()==361250000
print('CASE_I_COEFF_T6', factor(coI[6]))
print('CASE_I_Q1_POSITIVE_DEFINITE', [100,165600,361250000])

# CASE II: z7=0; another nontrivial quartic-null branch with z3 potentially nonzero.
b,d,s,e=symbols('b d s e', real=True)
zII=[12*b,b,2*d-Rational(25,2)*b,s,-2*b,d,0,0,e]
BII=B_from_z(zII)
coII=objective_series_coeffs(BII,6)
assert all(simplify(x)==0 for x in coII[:6])
P2=(57241*b**4 -6250*b**3*d -19680*b**3*e +625*b**2*d**2
    +3936*b**2*d*e +15030*b**2*e**2 -2890*b*d*e**2 +289*d**2*e**2)
expectedII=-Rational(100,289)*s*s*P2
assert simplify(coII[6]-expectedII)==0
A=625*b*b+289*e*e
BB=-2*b*(3125*b*b-1968*b*e+1445*e*e)
C=b*b*(57241*b*b-19680*b*e+15030*e*e)
assert simplify(P2-(A*d*d+BB*d+C))==0
Delta_good=factor(4*A*C-BB*BB)
expected_delta=20*b*b*(5202000*b**4+2606425*b*b*e*e+451129*e**4)
assert simplify(Delta_good-expected_delta)==0
inner_det=57241*15030-9840**2
assert inner_det>0
print('CASE_II_COEFF_T6', factor(coII[6]))
print('CASE_II_QUADRATIC_A', factor(A))
print('CASE_II_4AC_MINUS_B2', Delta_good)
print('CASE_II_C_INNER_PD_MINORS', 57241, inner_det)

# Equality-foliation finite self-check at the base point: columns 0..3 live in S={0,1,3,5}, columns 4..5 in T={2,4}.
S={0,1,3,5}; T={2,4}
for i in T:
    for j in range(4): assert Qeq[i,j]==0
for i in S:
    for j in (4,5): assert Qeq[i,j]==0

def probs(Q):
    out=[]
    for ca,cb in COLS:
        for i,j in EDGES:
            m=simplify(Q[i,ca]*Q[j,cb]-Q[i,cb]*Q[j,ca])
            out.append(simplify(m*m))
    return out
assert simplify(sum(Rational(v)*p for v,p in zip(V1080,probs(Qeq))))==0
print('EQUALITY_BLOCK_BASEPOINT_EXACT', 'PASS')
print('ALL EXACT CHECKS PASSED')
