"""Exact verifier for HARD8-03 checkpoint 2026-09-16T10:11:07Z.
Pure Python / standard library only.  All ranks use exact Fraction arithmetic.
"""
from fractions import Fraction
from itertools import product
from collections import Counter, deque


def rank_q(vectors):
    if not vectors:
        return 0
    a = [list(map(Fraction, v)) for v in vectors]
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        p = next((i for i in range(r, m) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [a[i][j] - f*a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def dissociated(vectors):
    """Subset sums are all distinct iff there is no nonzero {-1,0,1} relation."""
    if not vectors:
        return True
    d = len(vectors[0])
    sums = {(0,)*d}
    for v in vectors:
        new = []
        for s in sums:
            t = tuple(s[j] + v[j] for j in range(d))
            if t in sums:
                return False
            new.append(t)
        sums.update(new)
    return True


def all_maximal_dissociated(cols):
    n = len(cols)
    cache = {}
    def isd(mask):
        if mask not in cache:
            cache[mask] = dissociated([cols[i] for i in range(n) if (mask >> i) & 1])
        return cache[mask]
    out, full = [], (1 << n) - 1
    for mask in range(1 << n):
        if not isd(mask):
            continue
        rem, maximal = full ^ mask, True
        while rem:
            bit = rem & -rem
            if isd(mask | bit):
                maximal = False
                break
            rem -= bit
        if maximal:
            out.append(mask)
    return out


def signed_data(basis, universe):
    """For each target: min negative width and intersection of supports of all reps."""
    d, b = len(universe[0]), len(basis)
    index = {v:i for i,v in enumerate(universe)}
    width = [99]*len(universe)
    essential = [(1 << b)-1]*len(universe)
    reps = [0]*len(universe)
    for coeff in product((-1,0,1), repeat=b):
        out = [0]*d
        neg, support = 0, 0
        for j,(c,v) in enumerate(zip(coeff,basis)):
            if c:
                support |= 1 << j
                neg += c < 0
                for q in range(d):
                    out[q] += c*v[q]
        ti = index.get(tuple(out))
        if ti is not None:
            reps[ti] += 1
            if neg < width[ti]:
                width[ti] = neg
            essential[ti] &= support
    return width, essential, reps


def coordinate_columns(hs):
    rows = list(product(*[range(h) for h in hs]))
    cols, groups = [], []
    for j,h in enumerate(hs):
        g = []
        for a in range(h):
            g.append(len(cols))
            cols.append(tuple(int(x[j] == a) for x in rows))
        groups.append(g)
    return cols, groups


def mask_of(indices):
    m = 0
    for i in indices:
        m |= 1 << i
    return m


def basis_from_mask(cols, mask):
    inds = [i for i in range(len(cols)) if (mask >> i) & 1]
    return inds, [cols[i] for i in inds]


def verify_equal_sum_blocks():
    # Coordinate indicators are a concrete realization of the abstract relation geometry.
    cases = [(2,3), (2,2,3), (2,3,3), (3,4)]
    results = []
    for hs in cases:
        cols, groups = coordinate_columns(hs)
        maximal = all_maximal_dissociated(cols)
        r = rank_q(cols)
        assert r == 1 + sum(h-1 for h in hs)
        profiles = {}
        maxk = max(hs)
        for k in range(maxk+1):
            profiles[k] = 10**9
        for mask in maximal:
            complete, omitted = [], []
            for g in groups:
                sel = [i for i in g if (mask >> i) & 1]
                if len(sel) == len(g):
                    complete.append(g)
                else:
                    miss = [i for i in g if not ((mask >> i) & 1)]
                    assert len(miss) == 1
                    omitted.append(miss[0])
            assert len(complete) == 1
            inds,basis = basis_from_mask(cols, mask)
            widths, _, reps = signed_data(basis, cols)
            for oi in omitted:
                j = next(j for j,g in enumerate(groups) if oi in g)
                assert widths[oi] == hs[j]-1
                assert reps[oi] == 1
            for k in profiles:
                heavy = [cols[i] for i,w in enumerate(widths) if w > k]
                profiles[k] = min(profiles[k], rank_q(heavy))
        for k in profiles:
            Nk = sum((h-1) > k for h in hs)
            assert profiles[k] == max(0, Nk-1)
            assert (k+1)*profiles[k] <= r
        results.append((hs, r, len(maximal), profiles))
    return results


def verify_nullity_one():
    examples = []
    V1 = [(1,0),(0,1),(1,1)]
    examples.append((V1, 2, 1))
    V2,_ = coordinate_columns((2,2))
    examples.append((V2, 2, 2))
    P = [
        (1,1,0,0,0,0),
        (0,0,1,1,0,0),
        (0,0,0,0,1,1),
    ]
    N = [
        (1,0,1,0,1,0),
        (0,1,0,1,0,1),
    ]
    V3 = P + N
    examples.append((V3, 3, 2))
    results = []
    for cols,a,b in examples:
        r = rank_q(cols)
        assert len(cols) == r+1
        maximal = all_maximal_dissociated(cols)
        prof = {}
        for k in range(max(a,b)+1):
            best = 10**9
            for mask in maximal:
                _,basis = basis_from_mask(cols,mask)
                widths,_,_ = signed_data(basis,cols)
                best = min(best, rank_q([cols[i] for i,w in enumerate(widths) if w>k]))
            prof[k] = best
        for k,v in prof.items():
            expect = 1 if k < min(a-1,b-1) else 0
            assert v == expect
            assert (k+1)*v <= r
        results.append((len(cols),r,a,b,len(maximal),prof))
    return results


V14 = [
(1,0,0,1,0),(1,0,0,0,1),(0,1,0,1,1),
(0,0,1,1,1),(1,0,1,1,1),(1,1,1,1,1),
(0,0,1,0,0),(0,1,1,0,0),(0,1,0,1,0),(1,0,1,1,0),
(1,1,1,1,0),(0,1,0,0,1),(1,0,1,0,1),(1,1,1,0,1),
]


def verify_rank5_exchange():
    maximal = all_maximal_dissociated(V14)
    assert len(maximal) == 623
    assert Counter(m.bit_count() for m in maximal) == Counter({6:403,7:220})
    mset = set(maximal)

    widths, essentials, reps, heavy_rank = {}, {}, {}, {}
    for mask in maximal:
        inds,basis = basis_from_mask(V14,mask)
        w,e,nrep = signed_data(basis,V14)
        widths[mask], essentials[mask], reps[mask] = w,e,nrep
        heavy_rank[mask] = rank_q([V14[i] for i,x in enumerate(w) if x>1])

        # Exhaustive finite check of Theorem 3.1 on every omitted target.
        pos = {global_i:local_i for local_i,global_i in enumerate(inds)}
        for v in range(len(V14)):
            if (mask >> v) & 1:
                continue
            assert nrep[v] > 0
            for s in inds:
                swapped = (mask ^ (1 << s)) | (1 << v)
                _,sbasis = basis_from_mask(V14,swapped)
                actual = dissociated(sbasis)
                predicted = bool(e[v] & (1 << pos[s]))
                assert actual == predicted

    dist = Counter(heavy_rank.values())
    assert dist == Counter({0:120,1:153,2:150,3:113,4:70,5:17})

    bad = mask_of([0,1,2,3,4,5])
    loc = mask_of([0,1,3,5,8,10])
    repaired = mask_of([0,1,2,4,5,6])
    assert heavy_rank[bad] == 5
    assert [widths[bad][i] for i in range(6,14)] == [2,3,2,2,2,2,2,2]
    assert heavy_rank[repaired] == 0
    assert {i:widths[repaired][i] for i in range(14) if not ((repaired>>i)&1)} == {
        3:1,7:1,8:1,9:0,10:1,11:1,12:0,13:1}

    bad_inds,bad_basis = basis_from_mask(V14,bad)
    target = V14[6]
    all_reps = []
    for coeff in product((-1,0,1), repeat=len(bad_basis)):
        out = tuple(sum(c*v[j] for c,v in zip(coeff,bad_basis)) for j in range(5))
        if out == target:
            all_reps.append(coeff)
    assert all_reps == [(0,0,-1,1,-1,1)]
    local3 = bad_inds.index(3)
    assert essentials[bad][6] & (1 << local3)
    assert repaired == ((bad ^ (1<<3)) | (1<<6))

    graphs = {}
    for size in (6,7):
        vs = [m for m in maximal if m.bit_count()==size]
        s = set(vs)
        adj = {m:set() for m in vs}
        for m in vs:
            inside = [i for i in range(14) if (m>>i)&1]
            outside = [j for j in range(14) if not ((m>>j)&1)]
            for i in inside:
                for j in outside:
                    m2 = (m ^ (1<<i)) | (1<<j)
                    if m2 in s:
                        adj[m].add(m2)
        seen={vs[0]}; q=deque([vs[0]])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); q.append(y)
        assert len(seen)==len(vs)
        graphs[size]=(vs,adj)

    assert heavy_rank[loc] == 2
    assert {i:widths[loc][i] for i in range(14) if widths[loc][i]>1} == {6:2,9:2}
    loc_neigh = [heavy_rank[x] for x in graphs[6][1][loc]]
    assert len(loc_neigh)==16
    assert Counter(loc_neigh) == Counter({2:7,3:6,4:3})

    path = [mask_of(x) for x in (
        [0,1,3,5,8,10],
        [0,3,5,8,10,11],
        [0,4,5,8,10,11],
        [0,4,6,8,10,11])]
    assert [heavy_rank[x] for x in path] == [2,2,2,0]
    for a,b in zip(path,path[1:]):
        assert b in graphs[6][1][a]

    local_minima = {}
    sublevel = {}
    for size,(vs,adj) in graphs.items():
        lm = [m for m in vs if all(heavy_rank[y] >= heavy_rank[m] for y in adj[m])]
        local_minima[size] = Counter(heavy_rank[m] for m in lm)
        checks={}
        for h in range(6):
            nodes={m for m in vs if heavy_rank[m] <= h}
            seen=set(); comps=0; ok=True
            for start in nodes:
                if start in seen:
                    continue
                comps += 1
                c=[]; seen.add(start); q=deque([start])
                while q:
                    x=q.popleft(); c.append(x)
                    for y in adj[x]:
                        if y in nodes and y not in seen:
                            seen.add(y); q.append(y)
                ok &= any(heavy_rank[x]==0 for x in c)
            assert ok
            checks[h]=(len(nodes),comps,ok)
        sublevel[size]=checks
    assert local_minima[6] == Counter({1:26,2:20,0:17})
    assert local_minima[7] == Counter({0:103})

    return {
        "maximal":len(maximal),
        "sizes":Counter(m.bit_count() for m in maximal),
        "heavy_distribution":dist,
        "local_neighbor_distribution":Counter(loc_neigh),
        "local_minima_size6":local_minima[6],
        "local_minima_size7":local_minima[7],
        "sublevel":sublevel,
    }


def main():
    print("equal_sum_blocks")
    for row in verify_equal_sum_blocks():
        print(row)
    print("nullity_one")
    for row in verify_nullity_one():
        print(row)
    print("rank5_exchange")
    print(verify_rank5_exchange())
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
