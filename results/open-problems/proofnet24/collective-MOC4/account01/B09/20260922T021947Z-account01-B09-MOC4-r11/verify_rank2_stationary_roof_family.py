from itertools import combinations, permutations
import sympy as sp

Q = sp.Rational
x = sp.symbols("x", real=True)
I0, I1 = Q(177,100), Q(89,50)
xm = (I0+I1)/2

U = sp.Matrix([
[-Q(220,243), Q(71,243), -Q(62,243), Q(14,81)],
[-Q(61,243), -Q(220,243), -Q(68,243), -Q(16,81)],
[ Q(68,243), Q(62,243), -Q(215,243), -Q(22,81)],
[-Q(16,81), Q(14,81), Q(22,81), -Q(25,27)]
])
b = [-4,-2,3,-1]
C = sp.simplify(U*sp.diag(*b)*U.T)
assert U*U.T == sp.eye(4)

a = [
 (81*x+266)/81,
 4*(184113*x-208055)/(81*(4131*x-6755)),
 (43821*x-83110)/(27*(729*x+280)),
 (65043*x+41476)/(3*(21141*x+3088))
]
X = sp.simplify(sp.diag(*a)+C)

def check_sign(expr, wanted):
    expr=sp.cancel(expr)
    num, den = sp.fraction(expr)
    pn,pd = sp.Poly(num,x), sp.Poly(den,x)
    assert pn.count_roots(I0,I1)==0
    assert pd.count_roots(I0,I1)==0
    assert sp.sign(expr.subs(x,xm)) == wanted
    return (pn.degree(), pd.degree())

# Exact rank two throughout the interval.
for rs in combinations(range(4),3):
    for cs in combinations(range(4),3):
        assert sp.cancel(X.extract(rs,cs).det()) == 0
check_sign(X.extract((0,1),(0,1)).det(), +1)

# Source-valid simple spectra and nonzero pair sums throughout the interval.
for i,j in combinations(range(4),2):
    check_sign(a[i]-a[j], sp.sign((a[i]-a[j]).subs(x,xm)))
for i in range(4):
    for j in range(4):
        check_sign(a[i]+b[j], sp.sign((a[i]+b[j]).subs(x,xm)))

# All 12 row/column swaps are strictly below current support h=det=0.
swap_values = {}
for p,q in combinations(range(4),2):
    P = sp.eye(4)
    P[p,p]=P[q,q]=0
    P[p,q]=P[q,p]=1
    for kind,V in (("col",U*P),("row",P*U)):
        e=sp.factor((sp.diag(*a)+V*sp.diag(*b)*V.T).det())
        check_sign(e,-1)
        swap_values[(kind,p,q)]=e

H=sp.Matrix([
[Q(1,2),Q(1,2),Q(1,2),Q(1,2)],
[Q(1,2),Q(1,2),-Q(1,2),-Q(1,2)],
[Q(1,2),-Q(1,2),Q(1,2),-Q(1,2)],
[Q(1,2),-Q(1,2),-Q(1,2),Q(1,2)]])
hs=sp.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
P0=U.applyfunc(lambda z:z*z)
D=(H*P0*H.T)[1:,1:]
pairs=[(0,1),(0,2),(0,3)]
def comp(S): return tuple(i for i in range(4) if i not in S)
def d2(S,T): return sp.factor(U.extract(S,T).det()**2)
Rmat=sp.zeros(3)
for i,S in enumerate(pairs):
    for j,T in enumerate(pairs):
        Rmat[i,j]=sp.factor(d2(S,T)+d2(S,comp(T)))
assert Rmat == sp.Matrix([
[Q(47665,59049),Q(2692,59049),Q(8692,59049)],
[Q(8692,59049),Q(45844,59049),Q(4513,59049)],
[Q(2692,59049),Q(10513,59049),Q(45844,59049)]])
assert D == sp.Matrix([
[Q(46513,59049),Q(1540,59049),-Q(2860,59049)],
[Q(2860,59049),Q(44044,59049),Q(95,59049)],
[-Q(1540,59049),-Q(145,59049),Q(44044,59049)]])

def prod_idx(z,inds):
    out=sp.Integer(1)
    for i in inds: out*=z[i]
    return sp.factor(out)
aic=[prod_idx(a,[j for j in range(4) if j!=i]) for i in range(4)]
bic=[prod_idx(b,[j for j in range(4) if j!=i]) for i in range(4)]
W=sp.Matrix(4,4,lambda i,j: sp.expand(aic[i]*b[j]+a[i]*bic[j]))
Aminus=[]; Bminus=[]; Aplus=[]; Bplus=[]
for S in pairs:
    Aminus.append(sp.expand(prod_idx(a,comp(S))-prod_idx(a,S)))
    Aplus.append(sp.expand(prod_idx(a,comp(S))+prod_idx(a,S)))
for T in pairs:
    Bminus.append(sp.expand(prod_idx(b,T)-prod_idx(b,comp(T))))
    Bplus.append(sp.expand(prod_idx(b,T)+prod_idx(b,comp(T))))
Y=sp.Matrix(3,3,lambda i,j: sp.expand(Aminus[i]*Bminus[j]))
Z=hs.T*Y*hs/8
K=sp.simplify((H*(W+Z)*H.T)[1:,1:])

Ksign=[[-1,+1,-1],[-1,+1,-1],[+1,+1,+1]]
for i in range(3):
    for j in range(3):
        check_sign(K[i,j],Ksign[i][j])
def absk(i,j): return Ksign[i][j]*K[i,j]

E0=(0,1,2); E1=(1,2,0); E2=(2,0,1)
O0=(0,2,1); O1=(2,1,0); O2=(1,0,2)
mchoice={E0:(1,1), E1:(1,2), O1:(1,1), O2:(2,2)}
def mcost(p):
    prodsg=sp.prod(Ksign[i][p[i]] for i in range(3))
    if prodsg>0: return sp.Integer(0)
    loc=mchoice[p]
    cand=absk(*loc)
    for i in range(3):
        other=(i,p[i])
        if other!=loc:
            check_sign(absk(*other)-cand,+1)
    return cand

L=max(sp.Integer(0),Rmat[2,2]-Rmat[0,1],Rmat[1,1]-Rmat[0,2])
Ue=min(Rmat[0,0],Rmat[1,1],Rmat[2,2])
assert L==Q(14384,19683) and Ue==Q(45844,59049)
def weights(t):
    return {E0:t,E1:Rmat[0,1]-Rmat[2,2]+t,E2:Rmat[0,2]-Rmat[1,1]+t,
            O0:Rmat[0,0]-t,O1:Rmat[1,1]-t,O2:Rmat[2,2]-t}
wL,wU=weights(L),weights(Ue)
for w in (wL,wU):
    assert all(v>=0 for v in w.values()) and sum(w.values())==1
ML=sp.factor(sum(wL[p]*mcost(p) for p in wL))
MU=sp.factor(sum(wU[p]*mcost(p) for p in wU))
check_sign(MU-ML,+1)

S=sp.factor(sum(Rmat[i,j]*absk(i,j)-D[i,j]*K[i,j] for i in range(3) for j in range(3)))
SPRgap=sp.factor(S-2*MU)
check_sign(SPRgap,+1)
expected_gap = -5*(
 417505228780624817193*x**4
 -7878953468924386283610*x**3
 -8079182274144688129197*x**2
 +24854794555730927932854*x
 -530351345114699817160
)/(Q(10460353203)*(729*x+280)*(4131*x-6755)*(21141*x+3088))
assert sp.cancel(SPRgap-expected_gap)==0

# All 24 target vertices are pairwise distinct; two retain opposite signs.
verts={}
for p in permutations(range(4)):
    verts[p]=sp.factor(sp.prod(a[i]+b[p[i]] for i in range(4)))
for p,q in combinations(list(verts),2):
    check_sign(verts[p]-verts[q], sp.sign((verts[p]-verts[q]).subs(x,xm)))
ppos=(2,3,1,0); pneg=(3,1,0,2)
check_sign(verts[ppos],+1)
check_sign(verts[pneg],-1)

print("PASS MOC4-RANK2-STATIONARY-ROOF-FAMILY-v1")
print("interval =", I0, I1)
print("rank2 = exact on whole interval")
print("strict_pair_top_swaps = 12/12 on whole interval")
print("M_U_minus_M_L_mid =", sp.factor((MU-ML).subs(x,xm)))
print("SPR_gap_mid =", sp.factor(SPRgap.subs(x,xm)))
print("positive_vertex =", ppos, sp.factor(verts[ppos]))
print("negative_vertex =", pneg, sp.factor(verts[pneg]))
