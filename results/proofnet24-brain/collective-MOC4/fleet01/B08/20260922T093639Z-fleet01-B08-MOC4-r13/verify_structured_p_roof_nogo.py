from fractions import Fraction as F
from itertools import combinations, permutations

# Exact true-unitary zero-face witness, det = +1.
U = [
    [F(0), F(-16,25), F(48,65), F(-69,325)],
    [F(16,25), F(-72,125), F(-33,65), F(-48,1625)],
    [F(-69,325), F(48,1625), F(-16,65), F(-1536,1625)],
    [F(48,65), F(33,65), F(24,65), F(-16,65)],
]
pairs = list(combinations(range(4),2))
perms = list(permutations(range(4)))

def det(M):
    n=len(M)
    out=F(0)
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=F(-1 if inv%2 else 1)
        for i in range(n):
            t*=M[i][p[i]]
        out+=t
    return out

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

assert [[dot(U[i],U[j]) for j in range(4)] for i in range(4)] == [
    [F(int(i==j)) for j in range(4)] for i in range(4)
]
assert det(U)==1
assert [(i,j) for i in range(4) for j in range(4) if U[i][j]==0] == [(0,0)]

P=[[U[i][j]**2 for j in range(4)] for i in range(4)]
def m2(I,J):
    i,k=I; j,l=J
    return U[i][j]*U[k][l]-U[i][l]*U[k][j]
Q={(I,J):m2(I,J)**2 for I in pairs for J in pairs}
assert all(m2(I,J)!=0 for I in pairs for J in pairs)

# Exact complex spectra and support phase eta=1.
a=[(-1,0),(-1,4),(0,-4),(2,-2)]
b=[(4,0),(-3,-1),(-2,-4),(1,-2)]

def gadd(z,w): return (z[0]+w[0], z[1]+w[1])
def gmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def gprod(zs):
    z=(1,0)
    for w in zs: z=gmul(z,w)
    return z

# c_{I,J}=Re(a_{I^c} b_J) for eta=1.
c={}
for I in pairs:
    Ic=tuple(k for k in range(4) if k not in I)
    A=gprod([a[k] for k in Ic])
    for J in pairs:
        B=gprod([b[k] for k in J])
        c[I,J]=F(gmul(A,B)[0])

C_expected=[
    [64,-64,-96,96,80,80],
    [-32,112,104,-128,-80,-60],
    [-176,-64,96,-24,-100,-160],
    [32,48,8,-32,0,20],
    [16,64,32,-56,-20,0],
    [-28,-72,-28,58,15,-10],
]
assert [[c[I,J] for J in pairs] for I in pairs] == [[F(x) for x in row] for row in C_expected]

def qperm(p,I,J):
    return F(set(p[j] for j in J)==set(I))

def gscore(p):
    return sum(c[I,J]*qperm(p,I,J) for I in pairs for J in pairs)

g={p:gscore(p) for p in perms}
actual=sum(c[I,J]*Q[I,J] for I in pairs for J in pairs)

# Exact primal optimizer in the P-fiber.
lam={
    (1,0,2,3):F(256,4225),
    (1,0,3,2):F(576,4225),
    (1,3,0,2):F(1728,8125),
    (2,3,0,1):F(2304,2640625),
    (2,3,1,0):F(116721,2640625),
    (3,0,1,2):F(1728,8125),
    (3,1,0,2):F(5184,15625),
    (3,2,1,0):F(2304,2640625),
}
assert sum(lam.values())==1
for i in range(4):
    for j in range(4):
        assert sum(w for p,w in lam.items() if p[j]==i)==P[i][j]
roof=sum(w*g[p] for p,w in lam.items())

# Exact dual certificate: alpha + sum_j y_{sigma(j),j} >= g_sigma.
alpha=F(0)
y=[
    [83,0,-261,0],
    [0,221,-104,237],
    [0,204,-182,0],
    [0,152,22,88],
]
y=[[F(v) for v in row] for row in y]
slacks={}
for p in perms:
    lhs=alpha+sum(y[p[j]][j] for j in range(4))
    slacks[p]=lhs-g[p]
    assert slacks[p]>=0
dual=alpha+sum(y[i][j]*P[i][j] for i in range(4) for j in range(4))
assert dual==roof
assert roof==F(-31131344,528125)
assert actual==F(-640458398416,11156640625)
gap=actual-roof
assert gap==F(17191243584,11156640625) and gap>0
assert set(slacks.values())=={F(x) for x in [0,11,16,104,288,299,304,315,392,408,680]}

# Direct determinant check and comparison with the 24 MOC vertices.
def zadd(z,w): return (z[0]+w[0],z[1]+w[1])
def zmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def zscale(q,z): return (q*z[0],q*z[1])
def zprod(zs):
    z=(F(1),F(0))
    for w in zs: z=zmul(z,w)
    return z
A=[(F(x),F(y0)) for x,y0 in a]
B=[(F(x),F(y0)) for x,y0 in b]
M=[[None]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        z=(F(0),F(0))
        for k in range(4):
            z=zadd(z,zscale(U[i][k]*U[j][k],B[k]))
        if i==j: z=zadd(z,A[i])
        M[i][j]=z

def zdet(M):
    n=len(M); out=(F(0),F(0))
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=(F(-1 if inv%2 else 1),F(0))
        for i in range(n): t=zmul(t,M[i][p[i]])
        out=zadd(out,t)
    return out

D=zdet(M)
assert D==(F(711706004784,11156640625), F(-2067563419232,11156640625))
verts={}
for p in perms:
    verts[p]=zprod([zadd(A[p[j]],B[j]) for j in range(4)])
best=max(v[0] for v in verts.values())
assert best==600
assert D[0] < best

# The roof-optimal full vertex average differs from the true support by exactly the degree-two gap.
avg=sum(w*verts[p][0] for p,w in lam.items())
assert D[0]-avg==gap

print("PASS")
print("detU =", det(U))
print("actual_Q2_cost =", actual)
print("P_fiber_roof =", roof)
print("gap =", gap, "~", float(gap))
print("dual_slacks =", sorted(set(slacks.values())))
print("det_support_real =", D[0], "~", float(D[0]))
print("best_vertex_support =", best)
