from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict

# Exact six-site non-exchangeable example for the weighted corank-one block-inflation theorem.
# Physical blocks: {0,1}, {2,3}, {4,5}.
BLOCKS = [(0,1),(2,3),(4,5)]

# Nonuniform unit block vectors, all rational by Pythagorean triples.
W_LOCAL = [
    [F(3,5), F(4,5)],
    [F(5,13), F(12,13)],
    [F(8,17), F(15,17)],
]
V_LOCAL = [[-w[1], w[0]] for w in W_LOCAL]

# Rational orthogonal quotient matrix. Row i spans quotient line U_i.
Q = [
    [F(1,3), F(2,3), F(2,3)],
    [F(2,3), F(1,3), F(-2,3)],
    [F(2,3), F(-2,3), F(1,3)],
]

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def embed(local,b):
    out=[F(0) for _ in range(6)]
    for j,x in enumerate(BLOCKS[b]):
        out[x]=local[j]
    return out

def outer(a,b):
    return [[a[i]*b[j] for j in range(6)] for i in range(6)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(6)] for i in range(6)]

def det2(P,e):
    a,b=e
    return P[a][a]*P[b][b]-P[a][b]*P[b][a]

# Exact local and quotient orthonormality.
for b in range(3):
    assert dot(W_LOCAL[b],W_LOCAL[b]) == 1
    assert dot(V_LOCAL[b],V_LOCAL[b]) == 1
    assert dot(W_LOCAL[b],V_LOCAL[b]) == 0
for i in range(3):
    for j in range(3):
        assert dot(Q[i],Q[j]) == (1 if i==j else 0)

W=[embed(W_LOCAL[b],b) for b in range(3)]
V=[embed(V_LOCAL[b],b) for b in range(3)]
U=[]
for i in range(3):
    u=[F(0) for _ in range(6)]
    for b in range(3):
        for x in range(6):
            u[x]+=Q[i][b]*W[b][x]
    U.append(u)

for i in range(3):
    for j in range(3):
        assert dot(U[i],U[j]) == (1 if i==j else 0)

# H_i = span(V_i, U_i), so P_i is rank two.
P=[]
for i in range(3):
    P.append(add(outer(V[i],V[i]),outer(U[i],U[i])))

# Full orthogonal decomposition.
for x in range(6):
    for y in range(6):
        want=F(1) if x==y else F(0)
        assert sum(P[i][x][y] for i in range(3)) == want

# Direct projection-DPP probabilities for each color on 2-subsets.
MU=[]
for i in range(3):
    mu={e:det2(P[i],e) for e in combinations(range(6),2)}
    assert all(v>=0 for v in mu.values())
    assert sum(mu.values()) == 1
    MU.append(mu)

# Quotient partition coupling. Each color gets exactly one quotient block.
# Identity has mass 1/9; two 3-cycles have mass 4/9 each.
PERMS=[
    ((0,1,2),F(1,9)),
    ((1,2,0),F(4,9)),
    ((2,0,1),F(4,9)),
]
for i in range(3):
    for b in range(3):
        got=sum(p for perm,p in PERMS if perm[i]==b)
        assert got == Q[i][b]*Q[i][b]

# Weighted lift. Block b is owned by color b. Z_b is sampled with law |w_b|^2.
JOINT=defaultdict(F)
for perm,pq in PERMS:
    inv={perm[i]:i for i in range(3)}  # block -> quotient color
    for choices in product([0,1], repeat=3):
        pz=F(1)
        for b,j in enumerate(choices):
            pz *= W_LOCAL[b][j]*W_LOCAL[b][j]
        sets=[set() for _ in range(3)]
        for b,B in enumerate(BLOCKS):
            owner=b
            qcolor=inv[b]
            z=B[choices[b]]
            if qcolor==owner:
                sets[owner].update(B)
            else:
                sets[owner].update(set(B)-{z})
                sets[qcolor].add(z)
        key=tuple(tuple(sorted(s)) for s in sets)
        JOINT[key]+=pq*pz

assert sum(JOINT.values()) == 1
for key,p in JOINT.items():
    assert p>=0
    union=set().union(*(set(s) for s in key))
    assert union == set(range(6))
    assert sum(len(s) for s in key) == 6

# Marginals exactly equal the direct rank-two projection DPPs.
MARG=[defaultdict(F) for _ in range(3)]
for key,p in JOINT.items():
    for i in range(3):
        MARG[i][key[i]] += p
for i in range(3):
    assert all(len(s)==2 for s in MARG[i])
    for e in combinations(range(6),2):
        assert MARG[i][e] == MU[i][e]

# The union of colors 1 and 2 has the correct rank-four DPP law by exact complement duality.
UNION12=defaultdict(F)
for key,p in JOINT.items():
    S=tuple(sorted(set(key[1]) | set(key[2])))
    UNION12[S]+=p
for S in combinations(range(6),4):
    comp=tuple(sorted(set(range(6))-set(S)))
    assert UNION12[S] == MU[0][comp]

# This is genuinely outside the prior exchangeability theorem: no P_i commutes with any
# within-block transposition, because every chosen w_b is nonuniform.
def conjugate_by_block_swap(M,b):
    a,c=BLOCKS[b]
    perm=list(range(6)); perm[a],perm[c]=perm[c],perm[a]
    return [[M[perm[x]][perm[y]] for y in range(6)] for x in range(6)]

for i in range(3):
    for b in range(3):
        swapped=conjugate_by_block_swap(P[i],b)
        assert any(swapped[x][y] != P[i][x][y] for x in range(6) for y in range(6))

print('joint_atoms',len(JOINT))
print('marginal_support_sizes',[sum(v!=0 for v in m.values()) for m in MARG])
print('nonexchangeable_all_9_color_block_checks',True)
print('all_exact_checks_passed')
