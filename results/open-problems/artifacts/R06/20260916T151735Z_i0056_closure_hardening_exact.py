from fractions import Fraction
from math import comb
from itertools import combinations

print("R06 I0056 closure-hardening exact checker")

# A. Exhaustive local boundary-move verification on all simple graphs with <=6 vertices.
# For every graph, finite K, and v outside K with r=|N(v)∩K|>=2:
#   e(K∪{v})-e(K) = deg(v)-2r
#   b(K∪{v}) <= b(K)-1+(deg(v)-r)
# Also, if every boundary vertex has exactly one neighbour in K, then b(K)=e(K).
def graph_from_mask(n, mask):
    edges=list(combinations(range(n),2))
    adj=[0]*n
    for k,(u,v) in enumerate(edges):
        if (mask>>k)&1:
            adj[u] |= 1<<v
            adj[v] |= 1<<u
    return adj

def boundary_mask(adj,K,n):
    nb=0
    kk=K
    while kk:
        lsb=kk & -kk
        u=lsb.bit_length()-1
        nb |= adj[u]
        kk -= lsb
    return nb & (((1<<n)-1)^K)

def edge_boundary_count(adj,K,n):
    outside=((1<<n)-1)^K
    s=0
    kk=K
    while kk:
        lsb=kk & -kk
        u=lsb.bit_length()-1
        s += (adj[u] & outside).bit_count()
        kk -= lsb
    return s

checked_moves=0
checked_terminal=0
for n in range(1,7):
    E=n*(n-1)//2
    for mask in range(1<<E):
        adj=graph_from_mask(n,mask)
        full=(1<<n)-1
        for K in range(1,full):  # nonempty proper
            B=boundary_mask(adj,K,n)
            e=edge_boundary_count(adj,K,n)
            b=B.bit_count()
            # terminal multiplicity-one check
            terminal=True
            bb=B
            while bb:
                lsb=bb & -bb
                v=lsb.bit_length()-1
                r=(adj[v]&K).bit_count()
                if r != 1:
                    terminal=False
                    break
                bb-=lsb
            if terminal:
                assert b==e
                checked_terminal+=1

            outside=full^K
            vv=outside
            while vv:
                lsb=vv & -vv
                v=lsb.bit_length()-1
                vv-=lsb
                r=(adj[v]&K).bit_count()
                if r<2:
                    continue
                deg=adj[v].bit_count()
                K2=K|lsb
                b2=boundary_mask(adj,K2,n).bit_count()
                e2=edge_boundary_count(adj,K2,n)
                assert e2-e == deg-2*r
                assert b2 <= b-1+(deg-r)
                checked_moves += 1

print("exhaustive local simple-graph move checks n<=6:", checked_moves, "PASS")
print("exhaustive terminal multiplicity-one checks n<=6:", checked_terminal, "PASS")

# B. Pure algebra of the closure theorem in the d-regular setting.
# h=d-3+x, x>=0. Termination coeff h-d+4=1+x;
# backward gain h-d+3=x.
for d in range(2,201):
    for x_num in range(0,21):
        x=Fraction(x_num,10)
        h=Fraction(d-3,1)+x
        assert h-d+4 == 1+x
        assert h-d+3 == x
print("closure theorem threshold algebra d<=200, x in {0,.1,...,2}: PASS")

# C. Source regular/co-regular f>=5 threshold using exact rational squares.
# Admissibility: 1/d+1/f <= 1/2.
checked_pairs=0
equal_pairs=[]
for d in range(3,501):
    for f in range(5,501):
        if Fraction(1,d)+Fraction(1,f)>Fraction(1,2):
            continue
        phi2=Fraction((d-2)**2,1)-Fraction(4*(d-2),f-2)
        rhs2=Fraction((d-3)**2,1)
        assert phi2>=rhs2
        if phi2==rhs2:
            equal_pairs.append((d,f))
        checked_pairs += 1
assert equal_pairs==[(3,6)]
print("admissible f>=5 threshold sweep d,f<=500:", checked_pairs, "PASS")
print("threshold equality pair in sweep:", equal_pairs)

# D. Quadrangular adversarial obstruction:
# Phi_E(d,4)^2 - (d-3)^2 = -1 exactly.
for d in range(4,501):
    diff=Fraction((d-2)**2,1)-Fraction(4*(d-2),2)-Fraction((d-3)**2,1)
    assert diff==-1
print("f=4 obstruction exact for d=4..500: PASS")

# E. Frozen H_{5,5}.
d=f=5
phi2=Fraction((d-2)**2,1)-Fraction(4*(d-2),f-2)
assert phi2==5
assert phi2>Fraction((d-3)**2,1)
print("H55 exact: Phi_E^2=5, threshold sqrt(5)>2, certified interval [sqrt(5),sqrt(5)], width=0: PASS")

# F. General t-closure algebra (auxiliary self-check only):
# close vertices with r>=t+1. Terminal crossing multiplicity <=t.
# If h>d-2t-2, process terminates. If additionally h>=t(d-t-2),
# the same argument yields h_V>=h/t.
for d in range(3,30):
    for t in range(1,d):
        for r in range(t+1,d+1):
            assert d-2*r <= d-2*t-2
            assert d-r-1 <= d-t-2
print("auxiliary t-closure local algebra: PASS")

print("PASS")
