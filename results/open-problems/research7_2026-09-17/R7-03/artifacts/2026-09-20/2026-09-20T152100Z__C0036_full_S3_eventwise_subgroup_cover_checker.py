from itertools import product, permutations
from math import comb
import sympy as sp

# Exact certificate for the S3 subgroup-cover proof of Lyons Conjecture 5.7.
# No floating point arithmetic is used.

# S3 = <r,s | r^3=s^2=e, srs=r^{-1}>, coordinates r^i s^j.
G = [(i,j) for j in (0,1) for i in range(3)]
idx = {g:k for k,g in enumerate(G)}

def mul(g,h):
    i,j=g; k,l=h
    return ((i + (-1 if j else 1)*k) % 3, (j+l) % 2)

def act_subset(a,mask):
    out=0
    for g in G:
        if (mask >> idx[g]) & 1:
            out |= 1 << idx[mul(a,g)]
    return out

# 16 left-translation orbits in 2^S3.
seen=set(); orbits=[]
for m in range(64):
    if m in seen:
        continue
    orb={act_subset(a,m) for a in G}
    seen |= orb
    orbits.append(sorted(orb))
assert len(orbits)==16
orbit_id={m:i for i,o in enumerate(orbits) for m in o}

# Orbit poset and all invariant increasing events (= upper ideals).
le=[[False]*16 for _ in range(16)]
for i,o in enumerate(orbits):
    for j,p in enumerate(orbits):
        le[i][j]=any((m & ~n)==0 for m in o for n in p)
upper=[]
for b in range(1<<16):
    ok=True
    for i in range(16):
        if (b>>i)&1:
            for j in range(16):
                if le[i][j] and not ((b>>j)&1):
                    ok=False; break
        if not ok: break
    if ok: upper.append(b)
assert len(upper)==76

# Exact probability polynomial of an invariant event under a product measure.
def event_poly(event_bits, params):
    out=sp.Integer(0)
    for mask in range(64):
        if not ((event_bits >> orbit_id[mask]) & 1):
            continue
        term=sp.Integer(1)
        for i,t in enumerate(params):
            term *= t if ((mask>>i)&1) else (1-t)
        out += term
    return sp.expand(out)

# Multivariate power-to-Bernstein conversion on [0,1]^d.
# If all coefficients are >=0, polynomial is >=0 on the cube.
def bernstein_coeffs(poly, variables):
    P=sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    if P.is_zero:
        return {(0,)*len(variables):sp.Rational(0)}
    degs=[max(0,int(P.degree(v))) for v in variables]
    coeff=P.as_dict()
    out={}
    for ks in product(*[range(n+1) for n in degs]):
        s=sp.Rational(0)
        for exps,a in coeff.items():
            if all(e<=k for e,k in zip(exps,ks)):
                f=sp.Rational(1)
                for e,k,n in zip(exps,ks,degs):
                    f *= sp.Rational(comb(k,e),comb(n,e))
                s += a*f
        out[ks]=sp.factor(s)
    return out

def nonnegative_bernstein(poly, variables):
    bc=bernstein_coeffs(poly,variables)
    return all(c>=0 for c in bc.values()), bc

# ---- C3 coset product certificate ----
# A3={e,r,r^2} gets parameter x^2, its other coset y^2; geometric mean p=xy.
x,y,z=sp.symbols('x y z', nonnegative=True)
A3=[idx[(0,0)],idx[(1,0)],idx[(2,0)]]
other=[idx[(0,1)],idx[(1,1)],idx[(2,1)]]
params3=[None]*6
for i in A3: params3[i]=x**2
for i in other: params3[i]=y**2
uniform3=[x*y]*6

c3_good=[]; c3_coeffs=[]; c3_kind={}
for i,U in enumerate(upper):
    D=sp.factor(event_poly(U,params3)-event_poly(U,uniform3))
    if D==0:
        c3_good.append(i); c3_kind[i]='zero'; continue
    q2=sp.cancel(D/(x-y)**2)
    if sp.denom(q2)==1:
        ok,bc=nonnegative_bernstein(q2,(x,y))
        if ok:
            c3_good.append(i); c3_kind[i]='square'; c3_coeffs += list(bc.values()); continue
    q4=sp.cancel(D/(x-y)**4)
    if sp.denom(q4)==1:
        ok,bc=nonnegative_bernstein(q4,(x,y))
        if ok:
            c3_good.append(i); c3_kind[i]='fourth'; c3_coeffs += list(bc.values()); continue

exceptions=[i for i in range(76) if i not in c3_good]
expected=[11,19,24,29,48,51,54,57,62,65,68,71]
assert exceptions==expected
assert len(c3_good)==64
assert sum(v=='zero' for v in c3_kind.values())==9
assert sum(v=='square' for v in c3_kind.values())==54
assert sum(v=='fourth' for v in c3_kind.values())==1
assert all(c>=0 for c in c3_coeffs)

# ---- C2 coset product certificate for the 12 exceptions ----
# H=<s>; right cosets are {e,s}, {r,r^2 s}, {r^2,rs}.
A,B,C=sp.symbols('A B C', nonnegative=True)
blocks=[
    [idx[(0,0)],idx[(0,1)]],
    [idx[(1,0)],idx[(2,1)]],
    [idx[(2,0)],idx[(1,1)]],
]
params2=[None]*6
for block,t in zip(blocks,(A,B,C)):
    for i in block: params2[i]=t

# The 12 exceptions form six classes under permutations of block variables.
reps=[11,29,48,54,65,71]
rep_expected={
    11:{11,19,24},
    29:{29},
    48:{48},
    54:{51,54,62},
    65:{57,65,68},
    71:{71},
}

def permuted(poly,perm):
    return sp.expand(poly.xreplace({A:perm[0],B:perm[1],C:perm[2]}))

for rep in reps:
    F=event_poly(upper[rep],params2)
    members=set()
    forms={permuted(F,p) for p in permutations((A,B,C))}
    for i in exceptions:
        if event_poly(upper[i],params2) in forms:
            members.add(i)
    assert members==rep_expected[rep], (rep,members)

# For each representative, pairwise geometric smoothing A,B -> sqrt(AB),
# then smoothing (g,g,C) -> (p,p,p), p=(g^2 C)^(1/3).
xx,yy,cc=sp.symbols('xx yy cc', nonnegative=True)
u,v=sp.symbols('u v', nonnegative=True)
c2_coeffs=[]
for rep in reps:
    F=event_poly(upper[rep],params2)
    D1=sp.factor(F.subs({A:xx**2,B:yy**2,C:cc})
                 -F.subs({A:xx*yy,B:xx*yy,C:cc}))
    q1=sp.cancel(D1/(xx-yy)**2)
    assert sp.denom(q1)==1
    ok1,bc1=nonnegative_bernstein(q1,(xx,yy,cc))
    assert ok1, rep

    # Put g=u^3 and C=v^3, so the common geometric mean is p=u^2 v.
    uniform=[u**2*v]*6
    D2=sp.factor(F.subs({A:u**3,B:u**3,C:v**3})
                 -event_poly(upper[rep],uniform))
    q2=sp.cancel(D2/(u-v)**2)
    assert sp.denom(q2)==1
    ok2,bc2=nonnegative_bernstein(q2,(u,v))
    assert ok2, rep
    c2_coeffs += list(bc1.values())+list(bc2.values())

assert all(c>=0 for c in c2_coeffs)

c3_pos=[c for c in c3_coeffs if c>0]
c2_pos=[c for c in c2_coeffs if c>0]
print('subset_orbits',len(orbits))
print('invariant_upper_sets',len(upper))
print('c3_certified_events',len(c3_good))
print('c3_exception_indices',exceptions)
print('c3_certificate_kinds',{'zero':9,'square':54,'fourth':1})
print('c3_bernstein_coefficients',len(c3_coeffs))
print('c3_zero_coefficients',sum(c==0 for c in c3_coeffs))
print('c3_min_positive_coefficient',min(c3_pos))
print('c2_exception_representatives',reps)
print('c2_bernstein_coefficients',len(c2_coeffs))
print('c2_zero_coefficients',sum(c==0 for c in c2_coeffs))
print('c2_min_positive_coefficient',min(c2_pos))
print('ALL_EXACT_S3_SUBGROUP_COVER_CERTIFICATES_PASS')
