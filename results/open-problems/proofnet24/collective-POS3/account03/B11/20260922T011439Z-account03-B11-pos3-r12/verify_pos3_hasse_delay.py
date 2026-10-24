from itertools import permutations, combinations
from fractions import Fraction

def closure(n, rel):
    R = [[False]*n for _ in range(n)]
    for a,b in rel:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    return R

def extensions(n, R):
    out = []
    for p in permutations(range(n)):
        pos = [0]*n
        for i,v in enumerate(p):
            pos[v] = i
        ok = True
        for a in range(n):
            for b in range(n):
                if R[a][b] and pos[a] >= pos[b]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(p)
    return out

def incomparable(R,a,b):
    return a != b and not R[a][b] and not R[b][a]

def width(n,R):
    best = 1
    for r in range(2,n+1):
        for S in combinations(range(n),r):
            if all(incomparable(R,a,b) for a,b in combinations(S,2)):
                best = r
    return best

def count_before(exts,a,b):
    return sum(p.index(a) < p.index(b) for p in exts)

def majority_order(n,R,exts):
    E = len(exts)
    wins = [[False]*n for _ in range(n)]
    for a,b in combinations(range(n),2):
        c = count_before(exts,a,b)
        if 2*c > E:
            wins[a][b] = True
        elif 2*c < E:
            wins[b][a] = True
        else:
            raise AssertionError("tie in chosen adversary")
    scores = [sum(row) for row in wins]
    order = sorted(range(n), key=lambda x: -scores[x])
    assert scores[order[0]] == n-1
    for i in range(n):
        for j in range(i+1,n):
            assert wins[order[i]][order[j]]
    return order

def canonical_blockers(n,R,x,y):
    pred = [z for z in range(n) if R[z][y] and incomparable(R,z,x)]
    succ = [z for z in range(n) if R[x][z] and incomparable(R,z,y)]
    mminus = [z for z in pred if not any(R[z][w] for w in pred)]
    mplus = [z for z in succ if not any(R[w][z] for w in succ)]
    return mminus,mplus

def is_cover(R,a,b):
    if not R[a][b]:
        return False
    n=len(R)
    return not any(R[a][z] and R[z][b] for z in range(n) if z not in (a,b))

def autonomous_pair(n,R,a,b):
    if not incomparable(R,a,b):
        return False
    for z in range(n):
        if z in (a,b):
            continue
        ra = (-1 if R[z][a] else (1 if R[a][z] else 0))
        rb = (-1 if R[z][b] else (1 if R[b][z] else 0))
        if ra != rb:
            return False
    return True

def distinguishers(n,R,a,b):
    out=[]
    for z in range(n):
        if z in (a,b):
            continue
        ra = (-1 if R[z][a] else (1 if R[a][z] else 0))
        rb = (-1 if R[z][b] else (1 if R[b][z] else 0))
        if ra != rb:
            out.append(z)
    return out

# Exact seven-element adversary to the stronger local endpoint-fork claim.
n=7
rel = [(0,2),(0,3),(0,4),(0,5),(0,6),
       (1,2),(1,5),(2,5),(4,5),(4,6)]
R=closure(n,rel)
exts=extensions(n,R)
E=len(exts)
assert E==79
assert width(n,R)==3

# Generic Hasse compression check on every incomparable pair in this poset.
for x,y in permutations(range(n),2):
    if not incomparable(R,x,y):
        continue
    mm,mp=canonical_blockers(n,R,x,y)
    assert all(is_cover(R,m,y) for m in mm)
    assert all(is_cover(R,x,s) for s in mp)
    assert len(mm) <= 2 and len(mp) <= 2

order=majority_order(n,R,exts)
assert order == [0,1,4,2,3,6,5]
x,y=order[0],order[1]
assert incomparable(R,x,y)
mm,mp=canonical_blockers(n,R,x,y)
assert mm == []
assert mp == [3,4]

counts = {
    "0<1": count_before(exts,0,1),
    "1<3": count_before(exts,1,3),
    "1<4": count_before(exts,1,4),
    "3<4": count_before(exts,3,4),
    "2<3": count_before(exts,2,3),
}
assert counts == {"0<1":54,"1<3":65,"1<4":55,"3<4":23,"2<3":42}
assert 3*counts["0<1"] > 2*E
assert 3*counts["1<3"] > 2*E
assert 3*counts["1<4"] > 2*E
assert 3*counts["3<4"] < E
assert E < 3*counts["2<3"] < 2*E

# The endpoint sibling pair is not autonomous. Vertex 6 distinguishes it:
# 4<6 while 3 || 6, and it occurs strictly after the second majority block.
assert not autonomous_pair(n,R,3,4)
ds=distinguishers(n,R,3,4)
assert 6 in ds
assert R[4][6] and incomparable(R,3,6)
assert order.index(6) > order.index(1)

print("POS3_HASSE_DELAY_CHECK")
print("linear_extensions",E)
print("width",width(n,R))
print("majority_order"," ".join(map(str,order)))
print("first_boundary",x,y)
print("canonical_predecessor_blockers",mm)
print("canonical_successor_blockers",mp)
for k,v in counts.items():
    print(k,v,E-v,f"{v}/{E}")
print("sibling_distinguishers",ds)
print("vertex6_relation","4<6_and_3||6")
print("POS3_HASSE_DELAY_CHECK_PASS")
