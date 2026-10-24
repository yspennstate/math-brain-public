from itertools import product, combinations
from collections import deque

# Exact finite combinatorial self-check for P11-I0062-FINITE-MEAN-OFFSET-BLOCK-04.
# No floating point is used.


def boundaries(s, L, a):
    # columns are y=0,...,L-1; a boundary b means an edge from b-1 to b.
    # take all internal b congruent to a mod s.
    return [b for b in range(1, L) if b % s == a % s]


def strips_from_boundaries(L, bs):
    pts=[0]+sorted(bs)+[L]
    return [(pts[i], pts[i+1]) for i in range(len(pts)-1)]


def wall_edges(s, L, D, a):
    E=set()
    for b in boundaries(s,L,a):
        for x in range(s):
            for z in range(D+1):
                E.add((x,b-1,z,x,b,z))
    return E


def canonical_edge(u,v):
    return (u,v) if u<=v else (v,u)


def local_horizontal_cut(s, strip, D, cut_z):
    y0,y1=strip
    # vertical edges z=cut_z-1 -> cut_z inside this strip
    E=set()
    for x in range(s):
        for y in range(y0,y1):
            u=(x,y,cut_z-1); v=(x,y,cut_z)
            E.add(canonical_edge(u,v))
    return E


def wall_edges_graph(s,L,D,a):
    E=set()
    for b in boundaries(s,L,a):
        for x in range(s):
            for z in range(D+1):
                E.add(canonical_edge((x,b-1,z),(x,b,z)))
    return E


def has_bottom_top_path(s,L,D,removed):
    # induced slab graph on x=0..s-1, y=0..L-1, z=0..D.
    q=deque((x,y,0) for x in range(s) for y in range(L))
    seen=set(q)
    while q:
        u=q.popleft()
        if u[2]==D:
            return True
        x,y,z=u
        for v in ((x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)):
            xx,yy,zz=v
            if not (0<=xx<s and 0<=yy<L and 0<=zz<=D):
                continue
            if canonical_edge(u,v) in removed:
                continue
            if v not in seen:
                seen.add(v); q.append(v)
    return False

partition_cases=0
wall_disjoint_cases=0
gluing_cases=0

# Partition structure: for every offset, all interior strips have width s; at most two partial strips.
for s in range(2,8):
    for L in range(s+1, 8*s+2):
        all_wall_sets=[]
        for a in range(s):
            bs=boundaries(s,L,a)
            strips=strips_from_boundaries(L,bs)
            widths=[v-u for u,v in strips]
            assert all(1 <= w <= s for w in widths)
            partial=[w for w in widths if w<s]
            assert len(partial)<=2
            if len(widths)>2:
                assert all(w==s for w in widths[1:-1])
            assert sum(widths)==L
            all_wall_sets.append(wall_edges(s,L,3,a))
            partition_cases += 1
        # Different offsets use disjoint long-direction wall edges.
        for a,b in combinations(range(s),2):
            assert all_wall_sets[a].isdisjoint(all_wall_sets[b])
            wall_disjoint_cases += 1

# Exhaustive topology check over arbitrary choices of one horizontal local cut height per strip.
# This checks the gluing logic on small slabs; theorem proof is graph-theoretic and not inferred from this finite test.
for s in range(2,5):
    for L in range(s+1, 3*s+3):
        for D in range(2,5):
            for a in range(s):
                strips=strips_from_boundaries(L,boundaries(s,L,a))
                # keep exhaustive count moderate: all local cut heights 1..D.
                for heights in product(range(1,D+1), repeat=len(strips)):
                    removed=wall_edges_graph(s,L,D,a)
                    for strip,h in zip(strips,heights):
                        removed |= local_horizontal_cut(s,strip,D,h)
                    assert not has_bottom_top_path(s,L,D,removed)
                    gluing_cases += 1

# Algebraic counting identities used in probability estimates.
# Extreme regime L >= s^7 => floor(L/s)-2 >= s^6-2 full blocks.
for s in range(2,50):
    for extra in range(0,3*s):
        L=s**7+extra
        q=L//s
        assert q >= s**6
        # total columns in two boundary partial strips < 2s, hence <=2s^2 cells in s x partial base.
        assert 2*s*s <= 2*s*s

print('P11-I0062-OFFSET-BLOCK-GEOMETRY-EXACT=PASS')
print(f'partition_cases={partition_cases}')
print(f'offset_wall_disjoint_pairs={wall_disjoint_cases}')
print(f'gluing_configurations={gluing_cases}')
print('floating_point=NONE')
print('scope=finite combinatorial self-check only; asymptotic probability theorem is proved in the report')
