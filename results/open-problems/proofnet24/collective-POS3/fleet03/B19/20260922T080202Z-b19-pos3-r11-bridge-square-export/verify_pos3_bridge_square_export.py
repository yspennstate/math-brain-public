#!/usr/bin/env python3
from itertools import combinations

N=9
COVERS=[(0,1),(1,3),(1,4),(2,5),(2,7),(3,5),(3,7),(4,6),(5,6),(6,8)]
CORE=(2,3,4,5,7)
LEFT=(2,3); Q=4; RIGHT=(5,7)

succ=[set() for _ in range(N)]
for a,b in COVERS: succ[a].add(b)
changed=True
while changed:
    changed=False
    for a in range(N):
        new=set().union(*(succ[b] for b in list(succ[a]))) if succ[a] else set()
        if not new.issubset(succ[a]):
            succ[a]|=new; changed=True

def lt(a,b): return b in succ[a]
def inc(a,b): return a!=b and not lt(a,b) and not lt(b,a)
def cover(a,b):
    return lt(a,b) and not any(lt(a,z) and lt(z,b) for z in range(N) if z not in (a,b))
def width_le_3():
    return not any(all(inc(a,b) for a,b in combinations(S,2)) for S in combinations(range(N),4))

pred=[set() for _ in range(N)]
for a in range(N):
    for b in succ[a]: pred[b].add(a)

exts=[]
def rec(prefix,used):
    if len(prefix)==N:
        exts.append(tuple(prefix)); return
    for v in range(N):
        if v not in used and pred[v].issubset(used):
            rec(prefix+[v], used|{v})
rec([],set())
E=len(exts)
def count(a,b): return sum(L.index(a)<L.index(b) for L in exts)
def balanced(a,b):
    c=count(a,b)
    return 3*c>=E and 3*c<=2*E
def swap_ok(L,a,b):
    X=list(L); ia=X.index(a); ib=X.index(b); X[ia],X[ib]=X[ib],X[ia]
    pos={v:i for i,v in enumerate(X)}
    return all(pos[x]<pos[y] for x in range(N) for y in succ[x])

assert E==64
assert width_le_3()
assert all(cover(l,r) for l in LEFT for r in RIGHT)
assert all(inc(Q,v) for v in LEFT+RIGHT)

bridge_counts={(l,Q):count(l,Q) for l in LEFT}
bridge_counts.update({(Q,r):count(Q,r) for r in RIGHT})
assert bridge_counts=={(2,4):52,(3,4):44,(4,5):44,(4,7):52}
assert all(3*c>2*E for c in bridge_counts.values())
assert count(2,3)==46 and not balanced(2,3)
assert count(5,7)==46 and not balanced(5,7)

balanced_pairs=[]
for a,b in combinations(range(N),2):
    if inc(a,b) and balanced(a,b): balanced_pairs.append((a,b,count(a,b)))
assert balanced_pairs==[(1,2,36),(6,7,28)]

def defect_data(a,b):
    maj=[L for L in exts if L.index(a)<L.index(b)]
    mino=[L for L in exts if L.index(b)<L.index(a)]
    dm=[L for L in maj if not swap_ok(L,a,b)]
    dn=[L for L in mino if not swap_ok(L,a,b)]
    U=[z for z in range(N) if z not in (a,b) and cover(a,z) and inc(z,b)]
    D=[z for z in range(N) if z not in (a,b) and cover(z,b) and inc(z,a)]
    return len(maj),len(mino),len(dm),len(dn),U,D,dm

m,n,dm,dn,U,D,DML=defect_data(2,3)
assert (m,n,dm,dn,U,D)==(46,18,28,0,[],[1])
assert all(L.index(2)<L.index(1)<L.index(3) for L in DML)
assert count(1,2)==36 and E-count(1,2)==28

m2,n2,dm2,dn2,U2,D2,DMR=defect_data(5,7)
assert (m2,n2,dm2,dn2,U2,D2)==(46,18,28,0,[6],[])
assert all(L.index(5)<L.index(6)<L.index(7) for L in DMR)
assert count(6,7)==28

print("E =",E)
print("width_le_3 =",width_le_3())
print("four_bridge_counts =",bridge_counts)
print("lower_sibling_count_2_before_3 =",count(2,3),"/",E)
print("upper_sibling_count_5_before_7 =",count(5,7),"/",E)
print("balanced_pairs =",balanced_pairs)
print("lower_sibling_defect =",(m,n,dm,dn,U,D))
print("upper_sibling_defect =",(m2,n2,dm2,dn2,U2,D2))
print("POS3_B19_BRIDGE_SQUARE_EXPORT_WITNESS_PASS")
