import sympy as sp
import itertools

I=sp.I
wpairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
idx={p:k for k,p in enumerate(wpairs)}
classes=[((0,1),(2,3),1),((0,2),(1,3),-1),((0,3),(1,2),1)]

def wedge_pair(a,b):
    if a==b: return None,0
    return ((a,b),1) if a<b else ((b,a),-1)

def dlam2(X):
    M=sp.zeros(6,6)
    for c,(r,s) in enumerate(wpairs):
        for a in range(4):
            z=X[a,r]
            if z:
                p,sg=wedge_pair(a,s)
                if p is not None: M[idx[p],c]+=sg*z
        for b in range(4):
            z=X[b,s]
            if z:
                p,sg=wedge_pair(r,b)
                if p is not None: M[idx[p],c]+=sg*z
    return M

# Real Spin(6) basis fixed by * conjugation.
F=sp.zeros(6,6)
for a,(p,q,sgn) in enumerate(classes):
    F[idx[p],2*a]=1/sp.sqrt(2)
    F[idx[q],2*a]=sgn/sp.sqrt(2)
    F[idx[p],2*a+1]=I/sp.sqrt(2)
    F[idx[q],2*a+1]=-I*sgn/sp.sqrt(2)
assert sp.simplify(F.conjugate().T*F)==sp.eye(6)

# Identify each coordinate SU(2) root plane inside the complementary-pair block basis.
dictionary={}
for r,s in itertools.combinations(range(4),2):
    X=sp.zeros(4); X[r,s]=1; X[s,r]=-1
    Y=sp.zeros(4); Y[r,s]=I; Y[s,r]=I
    RX=sp.simplify(F.conjugate().T*dlam2(X)*F)
    RY=sp.simplify(F.conjugate().T*dlam2(Y)*F)
    active=[]
    for a,b in itertools.combinations(range(3),2):
        Zx=RX[2*a:2*a+2,2*b:2*b+2]
        Zy=RY[2*a:2*a+2,2*b:2*b+2]
        if Zx!=sp.zeros(2) or Zy!=sp.zeros(2): active.append((a,b,Zx,Zy))
    assert len(active)==1
    a,b,Zx,Zy=active[0]
    assert RX[2*b:2*b+2,2*a:2*a+2] == -Zx.T
    assert RY[2*b:2*b+2,2*a:2*a+2] == -Zy.T
    dets=(sp.det(Zx),sp.det(Zy))
    assert dets[0]==dets[1] and abs(dets[0])==1
    sector='conformal' if dets[0]==1 else 'anticonformal'
    dictionary[(r,s)]=(a,b,sector,Zx,Zy)

expected={
 (0,1):(1,2,'anticonformal'),
 (2,3):(1,2,'conformal'),
 (0,2):(0,2,'anticonformal'),
 (1,3):(0,2,'conformal'),
 (0,3):(0,1,'anticonformal'),
 (1,2):(0,1,'conformal'),
}
for rs,(a,b,sector,Zx,Zy) in dictionary.items(): assert (a,b,sector)==expected[rs]

# Exact symbolic check of the third- and fourth-derivative formulas used on a mixed Schur kernel.
z11,z12,z21,z22=sp.symbols('z11 z12 z21 z22')
Z=sp.Matrix([[z11,z12],[z21,z22]])
P=Z*Z.T; Q=Z.T*Z

def qdet(A,B): return sp.expand((A+B).det()-A.det()-B.det())
aa=sp.symbols('a0:4'); gg=sp.symbols('g0:4')
A=sp.Matrix(2,2,aa); G=sp.Matrix(2,2,gg)
A1=Z*G; A2=-P*A; A3=-Z*Q*G; A4=P*P*A
G1=-Z.T*A; G2=-Q*G; G3=Q*Z.T*A; G4=Q*Q*G
t=sp.symbols('t')
At=A+t*A1+t**2*A2/sp.Integer(2)+t**3*A3/sp.Integer(6)+t**4*A4/sp.Integer(24)
Gt=G+t*G1+t**2*G2/sp.Integer(2)+t**3*G3/sp.Integer(6)+t**4*G4/sp.Integer(24)
assert sp.expand(sp.diff(At.det(),t,3).subs(t,0)-(qdet(A,A3)+3*qdet(A1,A2)))==0
assert sp.expand(sp.diff(Gt.det(),t,3).subs(t,0)-(qdet(G,G3)+3*qdet(G1,G2)))==0
assert sp.expand(sp.diff(At.det(),t,4).subs(t,0)-(qdet(A,A4)+4*qdet(A1,A3)+3*qdet(A2,A2)))==0
assert sp.expand(sp.diff(Gt.det(),t,4).subs(t,0)-(qdet(G,G4)+4*qdet(G1,G3)+3*qdet(G2,G2)))==0
inner=lambda X,Y: sp.trace(X.T*Y)
RA=sp.Rational(1,2)*sum(At[i,j]**2 for i in range(2) for j in range(2))
RG=sp.Rational(1,2)*sum(Gt[i,j]**2 for i in range(2) for j in range(2))
RA3=sp.expand(sp.diff(RA,t,3).subs(t,0)); RG3=sp.expand(sp.diff(RG,t,3).subs(t,0))
assert sp.expand(RA3+4*inner(Z.T*A,Q*G))==0
assert sp.expand(RG3-4*inner(Z.T*A,Q*G))==0
RA4=sp.expand(sp.diff(RA,t,4).subs(t,0)); RG4=sp.expand(sp.diff(RG,t,4).subs(t,0))
expected_RA4=sp.expand(4*(inner(A,P*P*A)-inner(G,Q*Q*G)))
assert sp.expand(RA4-expected_RA4)==0
assert sp.expand(RG4+expected_RA4)==0

print('PASS MOC4-SPIN6-ROOT-PAIR-DICTIONARY-v1')
for rs in sorted(dictionary):
    a,b,sector,Zx,Zy=dictionary[rs]
    print(f'pair {rs}: block planes {a}<->{b}, sector={sector}, dets=({int(Zx.det())},{int(Zy.det())})')
print('PASS MOC4-MIXED-SCHUR-CUBIC-GATE-v1 symbolic third-derivative identities')
print('PASS MOC4-MIXED-SCHUR-QUARTIC-GATE-v1 symbolic fourth-derivative identities')
