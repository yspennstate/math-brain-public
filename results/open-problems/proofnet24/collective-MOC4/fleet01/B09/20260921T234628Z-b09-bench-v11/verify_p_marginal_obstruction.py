from fractions import Fraction as F
from itertools import combinations, permutations

U = [
    [F(492,625), F(-31,625), F(-48,125), F(12,25)],
    [F(-9,25), F(12,25), F(-4,5), F(0)],
    [F(-36,125), F(48,125), F(9,25), F(4,5)],
    [F(-256,625), F(-492,625), F(-36,125), F(9,25)],
]
a = [(F(-2),F(-3)), (F(-2),F(0)), (F(3),F(1)), (F(-1),F(-2))]
b = [(F(3),F(0)), (F(2),F(-1)), (F(3),F(-2)), (F(2),F(3))]
PERMS = list(permutations(range(4)))

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def scale(q,z): return (q*z[0], q*z[1])
def prod(xs):
    z=(F(1),F(0))
    for x in xs: z=mul(z,x)
    return z

def det(M):
    n=len(M)
    if n==0: return F(1)
    if n==1: return M[0][0]
    s=F(0)
    for j in range(n):
        m=[row[:j]+row[j+1:] for row in M[1:]]
        s += (F(1) if j%2==0 else F(-1))*M[0][j]*det(m)
    return s

# Exact orthogonality.
for i in range(4):
    for j in range(4):
        s=sum(U[k][i]*U[k][j] for k in range(4))
        assert s == (F(1) if i==j else F(0))

subs={k:list(combinations(range(4),k)) for k in range(5)}
p={}
for k in range(5):
    for S in subs[k]:
        for T in subs[k]:
            d=det([[U[i][j] for j in T] for i in S])
            p[(S,T)] = d*d

def idxprod(vals, inds):
    return prod([vals[i] for i in inds])

# Cauchy-Binet principal-minor expansion.
D=(F(0),F(0))
for k in range(5):
    for S in subs[k]:
        Sc=tuple(i for i in range(4) if i not in S)
        for T in subs[k]:
            D=add(D, scale(p[(S,T)], mul(idxprod(a,Sc), idxprod(b,T))))

assert D == (F(-28853804,390625), F(-9702716,390625))

def z_sigma(sig):
    return prod([add(a[i],b[sig[i]]) for i in range(4)])

Z=[z_sigma(s) for s in PERMS]

# Exact 3-vertex hull certificate. Permutations are 1-based in the report.
tri = [(0,1,3,2),(1,0,2,3),(1,2,3,0)]
lam = [F(15487992,46953125), F(78732333,234765625), F(78593332,234765625)]
assert sum(lam)==1 and all(x>0 for x in lam)
comb=(F(0),F(0))
for w,sig in zip(lam,tri):
    comb=add(comb,scale(w,z_sigma(sig)))
assert comb==D
assert [z_sigma(s) for s in tri] == [(F(-90),F(10)),(F(20),F(-28)),(F(-152),F(-56))]

# Stronger no-go: no spectrum-dependent convex representation can both
# reproduce D and preserve the first-order marginals P_ij=|u_ij|^2.
# Certificate direction c(z)=8 Re z + 5 Im z.
def c(z): return F(8)*z[0]+F(5)*z[1]

# Dual affine majorant on permutation vertices, using only the independent
# upper-left 3x3 one-point marginals.
constant=F(176)
Y = [
    [F(-250), F(16), F(-356)],
    [F(-604), F(-596), F(-1196)],
    [F(1020), F(1020), F(432)],
]
for sig,z in zip(PERMS,Z):
    rhs=constant
    for i in range(3):
        if sig[i] < 3:
            rhs += Y[i][sig[i]]
    assert c(z) <= rhs

P=[[U[i][j]*U[i][j] for j in range(4)] for i in range(4)]
dual_bound=constant+sum(Y[i][j]*P[i][j] for i in range(3) for j in range(3))
target=c(D)
gap=target-dual_bound

assert dual_bound == F(-281803724,390625)
assert target == F(-279344012,390625)
assert gap == F(2459712,390625) and gap > 0

print("PASS")
print("D =", D)
print("three-point weights =", lam)
print("dual_bound =", dual_bound)
print("target =", target)
print("gap =", gap)
