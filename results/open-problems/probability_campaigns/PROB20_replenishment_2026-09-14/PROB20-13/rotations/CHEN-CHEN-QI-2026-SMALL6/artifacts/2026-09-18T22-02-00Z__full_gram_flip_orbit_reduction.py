from itertools import combinations, permutations
from collections import defaultdict, Counter
from math import factorial, comb, lcm

SOURCE_E1 = [
    (1,1),(1,2),(2,3),(2,4),(3,1),(3,3),(3,5),(4,2),
    (4,4),(4,5),(5,2),(5,3),(5,6),(6,1),(6,4),(6,6),
]
SOURCE_E2 = [
    ((1,4),(6,5)),((1,5),(2,2)),((3,6),(6,2)),((2,6),(4,3)),
    ((1,6),(2,5)),((3,4),(5,1)),((1,3),(4,1)),((5,5),(6,3)),
]
SOURCE_HOLES = [(2,1),(3,2),(4,6),(5,4)]
EXTENSIONS = list(combinations(SOURCE_HOLES, 2))
ZERO_KERNEL_EXTENSIONS = (2,3,5)

def form_key(form):
    return tuple(sorted(form.items()))

def single(p, c=1):
    return {p:c}

def pairform(p, q, sign=1):
    return {p:1, q:sign}

def square_poly(form):
    out = defaultdict(int)
    for p, cp in form.items():
        for q, cq in form.items():
            key = (tuple(sorted((p[0],q[0]))),
                   tuple(sorted((p[1],q[1]))))
            out[key] += cp*cq
    return dict(out)

def sum_poly(forms):
    out = defaultdict(int)
    for f in forms:
        for k,v in square_poly(f).items():
            out[k] += v
    return {k:v for k,v in out.items() if v}

def displayed_forms(ext_idx):
    return ([single(p) for p in SOURCE_E1] +
            [pairform(*e) for e in SOURCE_E2] +
            [pairform(*EXTENSIONS[ext_idx])])

def reduced_forms(ext_idx):
    forms = displayed_forms(ext_idx)

    def rem(f):
        target = form_key(f)
        for i,g in enumerate(forms):
            if form_key(g) == target:
                forms.pop(i)
                return
        raise AssertionError(("form not found", f))

    if ext_idx == 2:
        # Simultaneous two-flip identity:
        # (z34+z51)^2+(z21+z54)^2+z31^2+z24^2
        # = (z31+z54)^2+(z24+z51)^2+z34^2+z21^2.
        rem(pairform((3,4),(5,1)))
        rem(pairform((2,1),(5,4)))
        rem(single((3,1)))
        rem(single((2,4)))
        forms += [pairform((3,1),(5,4)),
                  pairform((2,4),(5,1)),
                  single((3,4)),
                  single((2,1))]
        # z34^2+z35^2+z44^2+z45^2
        # = (z34+z45)^2+(z35-z44)^2.
        for p in [(3,4),(3,5),(4,4),(4,5)]:
            rem(single(p))
        forms += [pairform((3,4),(4,5),+1),
                  pairform((3,5),(4,4),-1)]

    elif ext_idx == 3:
        # (z36+z62)^2+(z32+z46)^2+z66^2+z42^2
        # = (z32+z66)^2+(z36+z42)^2+z62^2+z46^2.
        rem(pairform((3,6),(6,2)))
        rem(pairform((3,2),(4,6)))
        rem(single((6,6)))
        rem(single((4,2)))
        forms += [pairform((3,2),(6,6)),
                  pairform((3,6),(4,2)),
                  single((6,2)),
                  single((4,6))]
        # z11^2+z12^2+z61^2+z62^2
        # = (z11+z62)^2+(z12-z61)^2.
        for p in [(1,1),(1,2),(6,1),(6,2)]:
            rem(single(p))
        forms += [pairform((1,1),(6,2),+1),
                  pairform((1,2),(6,1),-1)]

    elif ext_idx == 5:
        # (z46+z54)^2+z44^2+z56^2
        # = z46^2+z54^2+(z44+z56)^2.
        rem(pairform((4,6),(5,4)))
        rem(single((4,4)))
        rem(single((5,6)))
        forms += [single((4,6)),
                  single((5,4)),
                  pairform((4,4),(5,6),+1)]
        # z23^2+z24^2+z53^2+z54^2
        # = (z23+z54)^2+(z24-z53)^2.
        for p in [(2,3),(2,4),(5,3),(5,4)]:
            rem(single(p))
        forms += [pairform((2,3),(5,4),+1),
                  pairform((2,4),(5,3),-1)]
    else:
        raise AssertionError("not one of the zero-kernel extensions")

    return forms

def occupied_cells(ext_idx):
    S = set(SOURCE_E1)
    for a,b in SOURCE_E2 + [EXTENSIONS[ext_idx]]:
        S.add(a); S.add(b)
    return S

def full_rectangles(S):
    S = set(S)
    out = []
    for i,k in combinations(range(1,7),2):
        for j,l in combinations(range(1,7),2):
            cells = ((i,j),(i,l),(k,j),(k,l))
            if all(p in S for p in cells):
                out.append(cells)
    return out

def map_cell(p, row_perm, col_perm):
    return (row_perm[p[0]-1], col_perm[p[1]-1])

def perm_order(p):
    seen = [False]*len(p)
    o = 1
    for i in range(len(p)):
        if not seen[i]:
            j=i; n=0
            while not seen[j]:
                seen[j]=True
                n += 1
                j = p[j]-1
            o = lcm(o,n)
    return o

def automorphism_group():
    E1 = set(SOURCE_E1)
    autos = []
    for rp in permutations(range(1,7)):
        for cp in permutations(range(1,7)):
            if {map_cell(p,rp,cp) for p in E1} == E1:
                autos.append((rp,cp))
    return autos

def cycles_on_set(auto, S):
    rp,cp = auto
    S = set(S)
    seen=set()
    lens=[]
    for x in sorted(S):
        if x in seen:
            continue
        y=x; n=0
        while y not in seen:
            seen.add(y)
            n += 1
            y = map_cell(y,rp,cp)
        lens.append(n)
    return sorted(lens)

def count_commuting_involutions_with_fixed(cycle_counter, fixed_points=2):
    # An N=25 augmentation of the 20 complement cells is an involution
    # with exactly 2 fixed points (holes) and 9 transpositions (two-edges).
    # It is fixed by g iff that involution commutes with g.
    dp = {0:1}
    for length, c in sorted(cycle_counter.items()):
        local = defaultdict(int)
        for p in range(c//2 + 1):
            s = c - 2*p
            cycle_pairings = (factorial(c) //
                              (factorial(s)*(2**p)*factorial(p)))
            phase_choices = length**p
            if length % 2 == 1:
                local[s*length] += cycle_pairings*phase_choices
            else:
                for a in range(s+1):
                    local[a*length] += (cycle_pairings*phase_choices*
                                        comb(s,a))
        new = defaultdict(int)
        for f0,v0 in dp.items():
            for f1,v1 in local.items():
                new[f0+f1] += v0*v1
        dp = dict(new)
    return dp.get(fixed_points,0)

def pair_orbit_count(autos, complement):
    pairs = list(combinations(sorted(complement),2))
    seen=set()
    count=0
    sizes=[]
    for P in pairs:
        if P in seen:
            continue
        orb = {
            tuple(sorted(map_cell(x,*a) for x in P))
            for a in autos
        }
        seen |= orb
        count += 1
        sizes.append(len(orb))
    return count, Counter(sizes)

def main():
    for idx in ZERO_KERNEL_EXTENSIONS:
        original = displayed_forms(idx)
        reduced = reduced_forms(idx)
        assert len(original) == 25
        assert len(reduced) == 23
        assert sum_poly(original) == sum_poly(reduced)
        print("EXPLICIT_REDUCTION ext=%d added=%s N=25 -> %d POLY_MATCH=True" %
              (idx, EXTENSIONS[idx], len(reduced)))

    # After PSD forces every hole row/column of a Gram matrix to zero,
    # same-row/column cross terms are individually fixed. Each fully
    # occupied 2x2 rectangle leaves exactly one opposite-diagonal transfer.
    for idx in ZERO_KERNEL_EXTENSIONS:
        occ = occupied_cells(idx)
        rects = full_rectangles(occ)
        assert len(occ) == 34
        assert len(rects) == 176
        print("FULL_GRAM_FIBRE ext=%d occupied=34 rectangle_transfer_dim=176" %
              idx)

    autos = automorphism_group()
    assert len(autos) == 8
    orders = sorted(lcm(perm_order(rp),perm_order(cp)) for rp,cp in autos)
    assert orders == [1,2,2,2,2,2,4,4]
    print("AUT_GROUP size=8 element_orders=%s" % orders)

    allcells = {(i,j) for i in range(1,7) for j in range(1,7)}
    complement = allcells - set(SOURCE_E1)
    cycle_types = [Counter(cycles_on_set(a, complement)) for a in autos]
    type_counter = Counter(tuple(sorted(ct.items())) for ct in cycle_types)
    expected_types = Counter({
        ((1,20),):1,
        ((1,4),(2,8)):1,
        ((1,2),(2,9)):4,
        ((2,2),(4,4)):2,
    })
    assert type_counter == expected_types
    print("COMPLEMENT_CYCLE_TYPES %s" % dict(type_counter))

    pair_count, orbit_sizes = pair_orbit_count(autos, complement)
    assert pair_count == 31
    assert orbit_sizes == Counter({8:19,4:7,2:5})
    print("COMPLEMENT_UNORDERED_PAIR_ORBITS count=31 sizes=%s" %
          dict(sorted(orbit_sizes.items())))

    fixed = [count_commuting_involutions_with_fixed(ct,2)
             for ct in cycle_types]
    expected = sorted([6547290750,66894] + [80218]*4 + [146]*2,
                      reverse=True)
    assert sorted(fixed, reverse=True) == expected
    burnside_sum = sum(fixed)
    assert burnside_sum == 6547678808
    assert burnside_sum % 8 == 0
    n_orbits = burnside_sum // 8
    assert n_orbits == 818459851
    print("N25_FIXED_COUNTS %s" % fixed)
    print("N25_BURNSIDE_SUM=%d N25_AUGMENTATION_ORBITS=%d" %
          (burnside_sum,n_orbits))

    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
