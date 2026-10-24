from itertools import combinations
from fractions import Fraction

# Exact 8-element adversary used in account03/B11 POS3 run.
N = 8
GENERATORS = [
    (0,2),(0,5),(1,2),(1,3),(1,6),
    (2,4),(3,4),(3,5),(5,7),(6,7),
]

def closure(n, rels):
    R = [[False]*n for _ in range(n)]
    for a,b in rels:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    return R

R = closure(N, GENERATORS)

def extensions(elements):
    elements = tuple(elements)
    S = set(elements)
    preds = {x:{y for y in S if R[y][x]} for x in S}
    out = []
    def rec(prefix, rem):
        if not rem:
            out.append(tuple(prefix))
            return
        mins = sorted(x for x in rem if not (preds[x] & rem))
        for x in mins:
            rec(prefix+[x], rem-{x})
    rec([], set(S))
    return out

LE = extensions(range(N))
assert len(LE) == 121

def pnum(a,b):
    return sum(L.index(a) < L.index(b) for L in LE)

def incomparable(a,b):
    return not R[a][b] and not R[b][a]

# Width.
width = 0
witness = None
for r in range(1,N+1):
    for S in combinations(range(N),r):
        if all(incomparable(a,b) for a,b in combinations(S,2)):
            width = r
            witness = S
assert width == 3

# Strong-majority total order.
star = [[False]*N for _ in range(N)]
for a,b in combinations(range(N),2):
    if R[a][b]:
        star[a][b] = True
    elif R[b][a]:
        star[b][a] = True
    else:
        c = pnum(a,b)
        assert 2*c != len(LE)
        star[a][b] = (2*c > len(LE))
        star[b][a] = not star[a][b]

indeg = [sum(star[j][i] for j in range(N)) for i in range(N)]
majority_order = tuple(sorted(range(N), key=lambda x: indeg[x]))
assert majority_order == (1,0,3,6,2,5,4,7)
for i in range(N):
    for j in range(i+1,N):
        assert star[majority_order[i]][majority_order[j]]

def is_cover(a,b):
    if not R[a][b]:
        return False
    return not any(z not in (a,b) and R[a][z] and R[z][b] for z in range(N))

def canonical_blockers(x,y):
    pred = [z for z in range(N) if R[z][y] and incomparable(z,x)]
    succ = [z for z in range(N) if R[x][z] and incomparable(z,y)]
    mminus = [z for z in pred if not any(z != w and w in pred and R[z][w] for w in pred)]
    mplus = [z for z in succ if not any(z != w and w in succ and R[w][z] for w in succ)]
    return tuple(sorted(mminus)), tuple(sorted(mplus))

x,y = 1,0
mminus,mplus = canonical_blockers(x,y)
assert mminus == ()
assert mplus == (3,6)
assert all(is_cover(x,s) for s in mplus)

def relsig(z,a):
    if R[z][a]: return -1
    if R[a][z]: return 1
    return 0

distinguishers = tuple(
    z for z in range(N)
    if z not in mplus and relsig(z,3) != relsig(z,6)
)
assert distinguishers == (4,5)
earliest = min(distinguishers, key=lambda z: majority_order.index(z))
assert earliest == 5
assert R[3][5] and incomparable(6,5)

# Exact local probabilities: first boundary, fork, and earliest distinguisher are all extreme.
quoted = {
    (1,0):81,
    (0,3):89,
    (0,6):100,
    (3,6):82,
    (6,5):83,
    (2,6):55,
}
for pair,num in quoted.items():
    assert pnum(*pair) == num

for pair in [(1,0),(0,3),(0,6),(3,6),(6,5)]:
    assert 3*pnum(*pair) > 2*len(LE)
# But the next relevant pair is balanced, so this is not a target counterexample.
assert len(LE) <= 3*pnum(6,2) <= 2*len(LE)  # p(6<2)=66/121

# Exact two-element deletion/insertion fiber identity.
def allowed_interval(a,tau):
    pos = {v:i+1 for i,v in enumerate(tau)}
    m = len(tau)
    lo = max([pos[v] for v in tau if R[v][a]] or [0])
    hi = min([pos[v]-1 for v in tau if R[a][v]] or [m])
    assert lo <= hi
    return tuple(range(lo,hi+1))

def fiber_table(a,b):
    assert incomparable(a,b)
    Q = [v for v in range(N) if v not in (a,b)]
    LQ = extensions(Q)
    A=B=0
    rows=[]
    for tau in LQ:
        Ia = allowed_interval(a,tau)
        Ib = allowed_interval(b,tau)
        t = len(set(Ia).intersection(Ib))
        lt = sum(i<j for i in Ia for j in Ib)
        gt = sum(i>j for i in Ia for j in Ib)
        At = lt+t
        Bt = gt+t
        Tt = At+Bt
        # The sign-sum form of the skew.
        signsum = sum((j>i)-(j<i) for i in Ia for j in Ib)
        assert At-Bt == signsum
        assert Tt == len(Ia)*len(Ib)+t
        rows.append((tau,Ia,Ib,At,Bt,Tt))
        A += At
        B += Bt
    return rows,A,B

# Check the fiber identity against direct extension counts for every incomparable pair.
for a,b in combinations(range(N),2):
    if incomparable(a,b):
        rows,A,B = fiber_table(a,b)
        assert A == pnum(a,b)
        assert B == pnum(b,a)
        assert A+B == len(LE)

rows,A,B = fiber_table(3,6)
assert (A,B) == (82,39)
# A global >2 skew forces at least one >2 deletion fiber; here the maximal fiber is 4:1.
assert A > 2*B
skewed = [(tau,Ia,Ib,At,Bt) for tau,Ia,Ib,At,Bt,Tt in rows if At > 2*Bt]
assert skewed
max_row = max(rows, key=lambda row: Fraction(row[3],row[4]))
assert Fraction(max_row[3],max_row[4]) == 4
assert max_row[1] == (2,)
assert max_row[2] == (2,3,4,5)

# In this adversary every (3,6)-fiber has nested intervals with the same lower endpoint.
for tau,Ia,Ib,At,Bt,Tt in rows:
    assert Ia[0] == Ib[0]
    assert set(Ia).issubset(Ib)
    r,s = len(Ia),len(Ib)
    assert At == r*s - r*(r-1)//2
    assert Bt == r*(r+1)//2
    if At > 2*Bt:
        assert 2*(s-r) > r+1

print("extensions=121")
print("width=3 witness_antichain=%s" % (witness,))
print("majority_order=%s" % (majority_order,))
print("first_boundary=1<*0 count=81/121")
print("successor_blockers=(3,6); earliest_distinguisher=5")
print("local_counts: 0<3=89, 0<6=100, 3<6=82, 6<5=83")
print("balanced_escape: 6<2=66/121")
print("fiber_pair=3<6 global=82/39 over %d deletion extensions" % len(rows))
print("max_fiber_ratio=4/1 Ia=(2,) Ib=(2,3,4,5)")
print("POS3_TWO_GAP_FIBER_CHECK_PASS")
