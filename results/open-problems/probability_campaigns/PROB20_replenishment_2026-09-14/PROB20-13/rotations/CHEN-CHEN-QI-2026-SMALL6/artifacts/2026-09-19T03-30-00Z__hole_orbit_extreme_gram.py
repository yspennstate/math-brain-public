from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter

E1 = [
    (1,1),(1,2),(2,3),(2,4),(3,1),(3,3),(3,5),(4,2),
    (4,4),(4,5),(5,2),(5,3),(5,6),(6,1),(6,4),(6,6),
]
S=set(E1)
ALL={(i,j) for i in range(1,7) for j in range(1,7)}
C=sorted(ALL-S)
P=1000003

def product_key(p,q):
    return (tuple(sorted((p[0],q[0]))), tuple(sorted((p[1],q[1]))))

def hinge_centers(pair):
    (r1,c1),(r2,c2)=pair
    out=[]
    for r0,c0 in E1:
        if ((r1,c0) in S and (r0,c1) in S and
            (r2,c0) in S and (r0,c2) in S):
            out.append((r0,c0))
    return out

PAIRS=[tuple(sorted(p)) for p in combinations(C,2)]
good=[p for p in PAIRS if not hinge_centers(p)]
assert len(good)==134
pair_to_idx={p:i for i,p in enumerate(good)}

base_keys={product_key(a,b) for a,b in combinations(E1,2)}
assert len(base_keys)==120
allkeys=[(ri,cj) for ri in combinations_with_replacement(range(1,7),2)
                 for cj in combinations_with_replacement(range(1,7),2)]
rowid={k:i for i,k in enumerate(k for k in allkeys if k not in base_keys)}
assert len(rowid)==321

def cand_base_cols(pair):
    a,b=pair
    cols=[]
    for c in E1:
        d={}
        for x in (a,b):
            k=product_key(x,c)
            if k not in base_keys:
                r=rowid[k]
                d[r]=d.get(r,0)+1
        cols.append(d)
    return cols

def cross_col(a,b):
    d={}
    for x in a:
        for y in b:
            k=product_key(x,y)
            if k not in base_keys:
                r=rowid[k]
                d[r]=d.get(r,0)+1
    return {r:v for r,v in d.items() if v}

cand_cols=[cand_base_cols(g) for g in good]

def rank_mod(cols):
    basis={}
    rank=0
    for vec in cols:
        v={r:(x%P) for r,x in vec.items() if x%P}
        while v:
            c=min(v)
            if c not in basis:
                inv=pow(v[c],P-2,P)
                v={r:(x*inv)%P for r,x in v.items() if (x*inv)%P}
                basis[c]=v
                rank+=1
                break
            b=basis[c]; a=v[c]
            nv=dict(v)
            for r,x in b.items():
                y=(nv.get(r,0)-a*x)%P
                if y: nv[r]=y
                elif r in nv: del nv[r]
            v=nv
    return rank

def cols_for(ids):
    ids=tuple(ids)
    cols=[]
    for i in ids:
        cols += cand_cols[i]
    for i,j in combinations(ids,2):
        cols.append(cross_col(good[i],good[j]))
    return cols

# Xu-Yan identities (8) and (9), instantiated on this E1 skeleton.
def normpair(a,b): return tuple(sorted((a,b)))
id8_pairs=set(); id9_pairs=set()
rows=range(1,7); cols=range(1,7)
for x,y,z in permutations(rows,3):
    for a,b,d in permutations(cols,3):
        req={(x,d),(y,b),(y,d)}
        if req <= S:
            p1=normpair((x,b),(z,a))
            p2=normpair((y,a),(z,d))
            if p1 in pair_to_idx and p2 in pair_to_idx and set(p1).isdisjoint(p2):
                id8_pairs.add(tuple(sorted((pair_to_idx[p1],pair_to_idx[p2]))))
for x,y,z in permutations(rows,3):
    for a,b,c,d in permutations(cols,4):
        req={(x,a),(z,c),(y,a),(y,b),(z,b)}
        if req <= S:
            p1=normpair((x,c),(z,d))
            p2=normpair((x,d),(z,a))
            if p1 in pair_to_idx and p2 in pair_to_idx and set(p1).isdisjoint(p2):
                id9_pairs.add(tuple(sorted((pair_to_idx[p1],pair_to_idx[p2]))))
assert len(id8_pairs)==184
assert len(id9_pairs)==64
assert len(id8_pairs|id9_pairs)==248

def strip_violation(sel_ids):
    pairforms=[good[i] for i in sel_ids]
    for r1,r2 in combinations(range(1,7),2):
        R={r1,r2}
        for mask in range(1,1<<6):
            J={j+1 for j in range(6) if mask>>j & 1}
            q=len(J)
            cnt=sum(1 for p in E1 if p[0] in R and p[1] in J)
            cnt += sum(1 for a,b in pairforms if a[0] in R and b[0] in R and a[1] in J and b[1] in J)
            if cnt>q+1:
                return True
    for c1,c2 in combinations(range(1,7),2):
        Cc={c1,c2}
        for mask in range(1,1<<6):
            I={i+1 for i in range(6) if mask>>i & 1}
            q=len(I)
            cnt=sum(1 for p in E1 if p[1] in Cc and p[0] in I)
            cnt += sum(1 for a,b in pairforms if a[1] in Cc and b[1] in Cc and a[0] in I and b[0] in I)
            if cnt>q+1:
                return True
    return False

def map_cell(p,rp,cp): return (rp[p[0]-1],cp[p[1]-1])
autos=[]
for rp in permutations(range(1,7)):
    for cp in permutations(range(1,7)):
        if {map_cell(p,rp,cp) for p in E1}==S:
            autos.append((rp,cp))
assert len(autos)==8

def map_holes(h,a):
    rp,cp=a
    return tuple(sorted(map_cell(x,rp,cp) for x in h))

hole_pairs=list(combinations(C,2))
seen=set(); hole_orbits=[]
for h in hole_pairs:
    h=tuple(sorted(h))
    if h in seen: continue
    orb={map_holes(h,a) for a in autos}
    seen |= orb
    hole_orbits.append((min(orb),orb))
hole_orbits.sort()
assert len(hole_orbits)==31
assert Counter(len(o) for _,o in hole_orbits)==Counter({8:19,4:7,2:5})

WITNESSES = {((1, 3), (1, 4)): [((3, 4), (4, 6)), ((2, 1), (3, 6)), ((2, 6), (6, 2)), ((4, 3), (5, 1)), ((2, 2), (5, 5)), ((1, 5), (1, 6)), ((5, 4), (6, 5)), ((3, 2), (6, 3)), ((2, 5), (4, 1))], ((1, 3), (1, 5)): [((2, 2), (3, 4)), ((3, 2), (4, 6)), ((2, 6), (6, 2)), ((2, 1), (3, 6)), ((4, 3), (5, 1)), ((1, 6), (5, 5)), ((5, 4), (6, 5)), ((1, 4), (6, 3)), ((2, 5), (4, 1))], ((1, 3), (2, 1)): [((1, 6), (5, 4)), ((1, 4), (3, 2)), ((3, 4), (5, 5)), ((2, 6), (6, 5)), ((3, 6), (6, 2)), ((1, 5), (4, 3)), ((2, 2), (5, 1)), ((2, 5), (4, 6)), ((4, 1), (6, 3))], ((1, 3), (2, 5)): [((3, 6), (5, 4)), ((1, 5), (3, 4)), ((2, 2), (4, 6)), ((2, 6), (6, 5)), ((5, 5), (6, 2)), ((1, 6), (4, 1)), ((4, 3), (5, 1)), ((2, 1), (3, 2)), ((1, 4), (6, 3))], ((1, 3), (3, 2)): [((1, 6), (5, 4)), ((1, 4), (4, 3)), ((1, 5), (5, 1)), ((2, 1), (6, 5)), ((2, 5), (4, 6)), ((2, 6), (6, 2)), ((3, 6), (4, 1)), ((5, 5), (6, 3)), ((2, 2), (3, 4))], ((1, 3), (3, 4)): [((1, 5), (6, 2)), ((2, 2), (5, 5)), ((2, 1), (3, 2)), ((5, 4), (6, 5)), ((2, 5), (3, 6)), ((1, 4), (4, 3)), ((1, 6), (4, 1)), ((4, 6), (6, 3)), ((2, 6), (5, 1))], ((1, 3), (3, 6)): [((1, 6), (5, 4)), ((2, 2), (4, 1)), ((2, 1), (6, 5)), ((2, 5), (4, 6)), ((1, 4), (4, 3)), ((3, 2), (6, 3)), ((1, 5), (6, 2)), ((3, 4), (5, 1)), ((2, 6), (5, 5))], ((1, 3), (4, 1)): [((1, 6), (5, 4)), ((1, 4), (2, 5)), ((3, 2), (6, 3)), ((2, 6), (6, 2)), ((2, 2), (5, 5)), ((5, 1), (6, 5)), ((3, 4), (4, 6)), ((1, 5), (3, 6)), ((2, 1), (4, 3))], ((1, 3), (4, 3)): [((2, 1), (6, 2)), ((2, 2), (4, 6)), ((2, 6), (3, 4)), ((3, 6), (4, 1)), ((5, 5), (6, 3)), ((1, 4), (6, 5)), ((1, 5), (5, 1)), ((1, 6), (2, 5)), ((3, 2), (5, 4))], ((1, 3), (4, 6)): [((1, 5), (3, 4)), ((1, 4), (2, 6)), ((5, 1), (6, 5)), ((2, 2), (5, 5)), ((3, 6), (5, 4)), ((4, 3), (6, 2)), ((2, 1), (3, 2)), ((1, 6), (4, 1)), ((2, 5), (6, 3))], ((1, 5), (1, 6)): [((1, 3), (3, 4)), ((1, 4), (6, 5)), ((3, 2), (4, 6)), ((2, 1), (3, 6)), ((5, 5), (6, 2)), ((2, 6), (4, 3)), ((2, 2), (5, 1)), ((2, 5), (5, 4)), ((4, 1), (6, 3))], ((1, 5), (2, 5)): [((1, 3), (3, 4)), ((1, 4), (4, 6)), ((5, 4), (6, 5)), ((2, 2), (5, 5)), ((2, 6), (5, 1)), ((4, 3), (6, 2)), ((2, 1), (3, 2)), ((1, 6), (6, 3)), ((3, 6), (4, 1))], ((1, 5), (2, 6)): [((2, 2), (3, 4)), ((3, 2), (6, 5)), ((1, 3), (6, 2)), ((4, 1), (5, 5)), ((1, 4), (5, 1)), ((3, 6), (5, 4)), ((2, 1), (4, 3)), ((1, 6), (2, 5)), ((4, 6), (6, 3))], ((1, 5), (3, 2)): [((1, 3), (3, 4)), ((1, 4), (4, 6)), ((1, 6), (6, 3)), ((2, 1), (6, 2)), ((2, 2), (5, 5)), ((3, 6), (5, 4)), ((2, 5), (4, 1)), ((2, 6), (4, 3)), ((5, 1), (6, 5))], ((1, 5), (3, 4)): [((2, 2), (5, 1)), ((2, 1), (3, 6)), ((1, 3), (6, 2)), ((2, 6), (4, 3)), ((5, 5), (6, 3)), ((1, 6), (5, 4)), ((1, 4), (6, 5)), ((3, 2), (4, 6)), ((2, 5), (4, 1))], ((1, 5), (3, 6)): [((1, 4), (4, 3)), ((1, 3), (2, 6)), ((5, 5), (6, 2)), ((2, 1), (6, 5)), ((2, 5), (5, 4)), ((4, 6), (6, 3)), ((3, 4), (5, 1)), ((1, 6), (3, 2)), ((2, 2), (4, 1))], ((1, 5), (5, 1)): [((1, 3), (3, 4)), ((1, 4), (4, 6)), ((3, 6), (5, 4)), ((2, 6), (4, 3)), ((2, 1), (6, 2)), ((2, 2), (5, 5)), ((3, 2), (6, 5)), ((1, 6), (6, 3)), ((2, 5), (4, 1))], ((1, 5), (5, 4)): [((1, 3), (3, 4)), ((1, 4), (4, 6)), ((2, 2), (5, 1)), ((2, 1), (6, 5)), ((2, 5), (3, 2)), ((2, 6), (5, 5)), ((1, 6), (6, 3)), ((4, 3), (6, 2)), ((3, 6), (4, 1))], ((1, 5), (5, 5)): [((2, 6), (3, 4)), ((1, 3), (3, 6)), ((2, 1), (6, 2)), ((2, 2), (4, 6)), ((1, 4), (6, 3)), ((4, 3), (5, 1)), ((3, 2), (5, 4)), ((2, 5), (4, 1)), ((1, 6), (6, 5))], ((3, 2), (3, 4)): [((1, 3), (5, 4)), ((1, 4), (4, 6)), ((1, 6), (2, 1)), ((5, 1), (6, 5)), ((4, 3), (6, 2)), ((2, 5), (6, 3)), ((2, 2), (5, 5)), ((1, 5), (2, 6)), ((3, 6), (4, 1))], ((3, 2), (3, 6)): [((1, 3), (5, 4)), ((1, 4), (6, 5)), ((1, 5), (4, 3)), ((5, 5), (6, 2)), ((1, 6), (2, 1)), ((4, 6), (5, 1)), ((2, 2), (4, 1)), ((2, 5), (6, 3)), ((2, 6), (3, 4))], ((3, 2), (4, 1)): [((1, 3), (5, 4)), ((1, 4), (2, 5)), ((2, 2), (6, 3)), ((1, 6), (2, 1)), ((4, 3), (6, 5)), ((3, 6), (6, 2)), ((3, 4), (5, 5)), ((1, 5), (2, 6)), ((4, 6), (5, 1))], ((3, 2), (4, 3)): [((1, 5), (2, 1)), ((1, 6), (4, 1)), ((1, 4), (6, 3)), ((1, 3), (5, 5)), ((2, 6), (6, 2)), ((2, 2), (3, 4)), ((2, 5), (4, 6)), ((5, 1), (6, 5)), ((3, 6), (5, 4))], ((3, 2), (4, 6)): [((1, 4), (6, 3)), ((1, 3), (2, 5)), ((2, 2), (3, 4)), ((2, 1), (6, 5)), ((3, 6), (4, 3)), ((4, 1), (5, 4)), ((5, 5), (6, 2)), ((2, 6), (5, 1)), ((1, 5), (1, 6))], ((3, 2), (5, 1)): [((1, 3), (3, 4)), ((1, 4), (2, 6)), ((2, 1), (4, 3)), ((4, 6), (6, 3)), ((1, 5), (6, 2)), ((5, 4), (6, 5)), ((2, 2), (5, 5)), ((1, 6), (4, 1)), ((2, 5), (3, 6))], ((3, 2), (5, 4)): [((1, 5), (2, 1)), ((1, 6), (4, 1)), ((2, 2), (4, 6)), ((2, 5), (6, 3)), ((5, 1), (6, 5)), ((1, 3), (5, 5)), ((3, 6), (6, 2)), ((2, 6), (3, 4)), ((1, 4), (4, 3))], ((3, 2), (5, 5)): [((1, 4), (6, 3)), ((1, 3), (3, 6)), ((1, 6), (4, 1)), ((1, 5), (6, 2)), ((5, 4), (6, 5)), ((2, 1), (4, 3)), ((2, 6), (5, 1)), ((2, 5), (4, 6)), ((2, 2), (3, 4))], ((3, 2), (6, 2)): [((1, 3), (3, 4)), ((1, 4), (2, 6)), ((4, 3), (5, 1)), ((1, 6), (5, 5)), ((2, 5), (4, 1)), ((2, 1), (3, 6)), ((5, 4), (6, 5)), ((2, 2), (6, 3)), ((1, 5), (4, 6))], ((3, 2), (6, 5)): [((1, 3), (5, 4)), ((1, 4), (2, 5)), ((3, 4), (6, 2)), ((2, 6), (4, 3)), ((1, 5), (4, 6)), ((2, 2), (5, 1)), ((2, 1), (3, 6)), ((1, 6), (5, 5)), ((4, 1), (6, 3))], ((3, 6), (4, 6)): [((1, 3), (3, 4)), ((1, 4), (6, 5)), ((1, 5), (5, 1)), ((4, 3), (6, 2)), ((2, 2), (5, 5)), ((1, 6), (2, 6)), ((2, 1), (3, 2)), ((4, 1), (5, 4)), ((2, 5), (6, 3))], ((3, 6), (5, 5)): [((1, 6), (4, 1)), ((2, 2), (4, 6)), ((1, 4), (6, 3)), ((1, 3), (2, 5)), ((1, 5), (6, 2)), ((2, 6), (3, 4)), ((4, 3), (5, 1)), ((3, 2), (5, 4)), ((2, 1), (6, 5))]}
assert set(WITNESSES)=={rep for rep,_ in hole_orbits}

def full_rectangles(holes):
    occupied=ALL-set(holes)
    total=0
    for rs in combinations(range(1,7),2):
        for cs in combinations(range(1,7),2):
            if all((r,c) in occupied for r in rs for c in cs):
                total += 1
    return total

same_line_orbits=0
distinct_orbits=0
for holes, matching in WITNESSES.items():
    holes=tuple(sorted(holes))
    rem=set(C)-set(holes)
    assert len(rem)==18
    used=set()
    ids=[]
    for p in matching:
        p=tuple(sorted(p))
        assert p in pair_to_idx
        assert not hinge_centers(p)
        assert not (set(p) & used)
        used |= set(p)
        ids.append(pair_to_idx[p])
    assert used==rem and len(ids)==9

    # Exact product-space certificate: 180 off-diagonal columns outside the
    # 120 independent base-base products have full rank mod prime. Therefore
    # they are also independent over Q.
    mixed=cols_for(ids)
    assert len(mixed)==180
    assert rank_mod(mixed)==180

    # These representatives also evade the two explicit Xu-Yan local
    # identities and every 2-row / 2-column strip overload.
    for i,j in combinations(ids,2):
        ij=tuple(sorted((i,j)))
        assert ij not in id8_pairs
        assert ij not in id9_pairs
    assert not strip_violation(ids)

    same = holes[0][0]==holes[1][0] or holes[0][1]==holes[1][1]
    fr=full_rectangles(holes)
    if same:
        same_line_orbits += 1
        assert fr==180
    else:
        distinct_orbits += 1
        assert fr==176

assert same_line_orbits==10
assert distinct_orbits==21
assert Counter('same' if (a[0]==b[0] or a[1]==b[1]) else 'distinct'
               for a,b in hole_pairs)==Counter({'same':48,'distinct':142})

print('AUT_E1 order=8 hole_orbits=31 sizes={2:5,4:7,8:19}')
print('FULL_GRAM_FIBRE same_line_raw=48 distinct_raw=142 same_line_orbits=10 distinct_orbits=21')
print('FULL_GRAM_FIBRE rectangle_dimensions same_line=180 distinct=176')
print('XUYAN_LOCAL identity8_pair_patterns=184 identity9_pair_patterns=64 union=248')
print('HARD_HOLE_WITNESSES count=31 all_cover_remaining_18_cells=True all_hinge_free=True')
print('HARD_HOLE_WITNESSES all_mixed_product_rank_mod_p=180_of_180=True')
print('HARD_HOLE_WITNESSES all_avoid_XuYan_8_9_and_strip_overload=True')
print('INTERPRETATION full mod-p rank certifies full rational rank; hence each hole orbit has a displayed decomposition with no nonzero coefficient-preserving zero-diagonal Gram perturbation inside its displayed span')
print('ALL_EXACT_CHECKS_PASS')
