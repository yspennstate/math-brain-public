from fractions import Fraction
from itertools import permutations

# Exact Gaussian-integer arithmetic for the previously exposed 2+2 boundary datum.
# Complex number x+iy is stored as (x,y).
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def neg(z): return (-z[0],-z[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def prod(xs):
    z=(1,0)
    for x in xs: z=mul(z,x)
    return z

minus_a=[(-3,0),(-2,0),(1,-3),(1,-2)]
a=[neg(z) for z in minus_a]
b=[(-1,0),(0,0),(1,0),(1,1)]
S4=list(permutations(range(4)))

def vertex(sig):
    return prod(add(a[i],b[sig[i]]) for i in range(4))

V={sig:vertex(sig) for sig in S4}
f={sig:Fraction(V[sig][1],1) for sig in S4}  # L(z)=Im z

# S4 -> S3 quotient by the Klein four subgroup, represented by action on
# the three complementary-pair matchings of {0,1,2,3}.
matchings=[
    frozenset((frozenset((0,1)),frozenset((2,3)))),
    frozenset((frozenset((0,2)),frozenset((1,3)))),
    frozenset((frozenset((0,3)),frozenset((1,2)))),
]

def rho(sig):
    out=[]
    for m in matchings:
        image=frozenset(frozenset(sig[i] for i in pair) for pair in m)
        out.append(matchings.index(image))
    return tuple(out)

fibers={}
for sig in S4:
    fibers.setdefault(rho(sig),[]).append(sig)
assert sorted(len(v) for v in fibers.values()) == [4]*6

B={r:sum((f[s] for s in ss),Fraction(0,1))/4 for r,ss in fibers.items()}

# account03/B09 external Saxl functionals:
# e_{tau,rho'}=(2/3)(B_{rho_tau}+B_{rho'})-(1/3)f(tau),
# with rho' one of the two S3 permutations pointwise deranging rho_tau.
external=[]
for tau in S4:
    rt=rho(tau)
    der=[rp for rp in fibers if all(rp[i] != rt[i] for i in range(3))]
    assert len(der)==2
    for rp in der:
        e=Fraction(2,3)*(B[rt]+B[rp])-Fraction(1,3)*f[tau]
        external.append((e,tau,rt,rp))
assert len(external)==48

face=[s for s in S4 if set(s[:2])=={0,1} and set(s[2:])=={2,3}]
outside=[s for s in S4 if s not in face]
M=max(f.values())
E=max(x[0] for x in external)
assert M == 0
assert max(f[s] for s in outside) == -12
assert E == -22
assert M-E == 22
assert sum((Fraction(V[s][0],1) for s in face),Fraction(0,1))/4 == Fraction(-119,4)
assert all(V[s][1]==0 for s in face)

print('permutation_support_values_sorted =', sorted(set(f.values()), reverse=True))
print('face_vertices =', [(s,V[s]) for s in face])
print('M =', M)
print('max_outside_face =', max(f[s] for s in outside))
print('fiber_means =', sorted(B.items()))
print('external_count =', len(external))
print('max_external =', E)
print('external_gap =', M-E)
print('external_maximizers =', [(tau,rt,rp) for e,tau,rt,rp in external if e==E])
print('block_det_average =', Fraction(-119,4))
