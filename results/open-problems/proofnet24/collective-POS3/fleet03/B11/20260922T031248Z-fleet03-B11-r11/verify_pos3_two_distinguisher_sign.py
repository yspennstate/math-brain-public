from itertools import product, permutations
from fractions import Fraction


def count_word(intervals, word):
    total = 0
    for vals in product(*[intervals[x] for x in word]):
        if all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1)):
            total += 1
    return total


case_a = 0
case_b = 0
range_a = [Fraction(1), Fraction(0)]
range_b = [Fraction(1), Fraction(0)]

# Canonical opposite-sign case A: a<z and b<w; all other special pairs incomparable.
# I_a=I_b=[0,m-1]; J_z and J_w are weakly right-shifted from I.
for m in range(1, 6):
    I = tuple(range(m))
    for dz in range(0, m + 3):
        for ez in range(0, 4):
            J = tuple(range(dz, m + ez))
            if not J:
                continue
            for dw in range(0, m + 3):
                for ew in range(0, 4):
                    K = tuple(range(dw, m + ew))
                    if not K:
                        continue
                    q = {'a': I, 'b': I, 'z': J, 'w': K}
                    n1 = count_word(q, ('a', 'z', 'b', 'w'))
                    n2 = count_word(q, ('a', 'b', 'z', 'w'))
                    n3 = count_word(q, ('a', 'b', 'w', 'z'))
                    n4 = count_word(q, ('b', 'w', 'a', 'z'))
                    n5 = count_word(q, ('b', 'a', 'w', 'z'))
                    n6 = count_word(q, ('b', 'a', 'z', 'w'))
                    assert n2 == n6
                    assert n3 == n5
                    assert n1 <= n2
                    assert n4 <= n5
                    A = n1 + n2 + n3
                    B = n4 + n5 + n6
                    p = Fraction(A, A + B)
                    assert Fraction(1, 3) <= p <= Fraction(2, 3)
                    range_a[0] = min(range_a[0], p)
                    range_a[1] = max(range_a[1], p)
                    case_a += 1

# Canonical opposite-sign case B: w<a<z and b is incomparable with w,a,z.
# I_a=I_b=[0,m-1], w is weakly left-shifted and z weakly right-shifted.
for m in range(1, 6):
    I = tuple(range(m))
    for lw in range(-3, 1):
        for uw in range(lw, m):
            W = tuple(range(lw, uw + 1))
            for lz in range(0, m + 3):
                for uz in range(max(lz, m - 1), m + 3):
                    Z = tuple(range(lz, uz + 1))
                    q = {'a': I, 'b': I, 'w': W, 'z': Z}
                    n1 = count_word(q, ('b', 'w', 'a', 'z'))
                    n2 = count_word(q, ('w', 'b', 'a', 'z'))
                    n3 = count_word(q, ('w', 'a', 'b', 'z'))
                    n4 = count_word(q, ('w', 'a', 'z', 'b'))
                    assert n2 == n3
                    assert n1 <= n2
                    assert n4 <= n3
                    A = n3 + n4
                    B = n1 + n2
                    p = Fraction(A, A + B)
                    assert Fraction(1, 3) <= p <= Fraction(2, 3)
                    range_b[0] = min(range_b[0], p)
                    range_b[1] = max(range_b[1], p)
                    case_b += 1


def closure_from_mask(n, mask):
    R = [[False] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> k) & 1:
                R[i][j] = True
            k += 1
    for t in range(n):
        for i in range(n):
            if R[i][t]:
                for j in range(n):
                    if R[t][j]:
                        R[i][j] = True
    return tuple(tuple(row) for row in R)


def linear_extensions(R):
    n = len(R)
    out = []
    for perm in permutations(range(n)):
        pos = [0] * n
        for k, x in enumerate(perm):
            pos[x] = k
        if all(not R[i][j] or pos[i] < pos[j]
               for i in range(n) for j in range(n)):
            out.append(pos)
    return out


def inc(R, a, b):
    return not R[a][b] and not R[b][a]


def relation(R, z, a):
    if R[z][a]:
        return -1
    if R[a][z]:
        return 1
    return 0


def sign(R, a, b, z):
    ra, rb = relation(R, z, a), relation(R, z, b)
    if ra == rb:
        return None
    if ra == 0 and rb == -1:  # z<b, z||a
        return +1
    if ra == 1 and rb == 0:   # a<z, z||b
        return +1
    if ra == -1 and rb == 0:  # z<a, z||b
        return -1
    if ra == 0 and rb == 1:   # b<z, z||a
        return -1
    raise AssertionError('incomparable pair has impossible distinguisher type')


# Exhaust every naturally labelled five-point poset; duplicates collapse after closure.
n = 5
closures = {}
for mask in range(1 << (n * (n - 1) // 2)):
    R = closure_from_mask(n, mask)
    closures[R] = None

pairs = 0
opp = 0
for R in closures:
    exts = linear_extensions(R)
    E = len(exts)
    for a in range(n):
        for b in range(a + 1, n):
            if not inc(R, a, b):
                continue
            pairs += 1
            ds = [(z, sign(R, a, b, z)) for z in range(n)
                  if z not in (a, b) and sign(R, a, b, z) is not None]
            if len(ds) == 2 and ds[0][1] * ds[1][1] == -1:
                opp += 1
                Nab = sum(pos[a] < pos[b] for pos in exts)
                p = Fraction(Nab, E)
                assert Fraction(1, 3) <= p <= Fraction(2, 3)

# Sharp warning: same-sign distinguishers can be extreme.
# Relations 0<2, 0<4, 1<4; examine (a,b)=(1,2).
R = [[False] * 5 for _ in range(5)]
for i, j in ((0, 2), (0, 4), (1, 4)):
    R[i][j] = True
R = tuple(tuple(row) for row in R)
exts = linear_extensions(R)
N = sum(pos[1] < pos[2] for pos in exts)
ds = [(z, sign(R, 1, 2, z)) for z in range(5)
      if z not in (1, 2) and sign(R, 1, 2, z) is not None]
assert len(exts) == 25 and N == 20 and ds == [(0, 1), (4, 1)]

print('caseA_interval_instances', case_a, 'probability_range', range_a)
print('caseB_interval_instances', case_b, 'probability_range', range_b)
print('n5_unique_naturally_labeled_closures', len(closures))
print('n5_incomparable_pairs_tested', pairs)
print('n5_opposite_sign_exactly_two_pairs', opp)
print('same_sign_witness_extensions', len(exts),
      'N_1_before_2', N, 'probability', Fraction(N, len(exts)),
      'distinguishers', ds)
print('POS3_TWO_DISTINGUISHER_SIGN_CHECK_PASS')
