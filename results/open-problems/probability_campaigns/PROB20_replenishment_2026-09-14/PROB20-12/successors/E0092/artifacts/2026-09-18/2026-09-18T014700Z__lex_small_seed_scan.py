from math import comb
from fractions import Fraction
from collections import Counter

# Exact small-b scan for the E0092 good-shell condition.
# Lexicographic seed order is itertools.product([0,1], repeat=3*b-1):
# the rightmost seed bit varies fastest. Arithmetic is integer/rational only.

def bits_of_index(idx, L):
    return [(idx >> (L - 1 - j)) & 1 for j in range(L)]

def toeplitz_rows(bits, b):
    N = 2*b
    rows = []
    for r in range(b):
        mask = 0
        for c in range(N):
            if bits[c-r+b-1]:
                mask |= 1 << c
        rows.append(mask)
    return rows

def rank_f2(rows):
    basis = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length()-1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                break
    return len(basis)

def shell_counts(rows, b):
    N = 2*b
    out = [Counter() for _ in range(N+1)]
    for z in range(1 << N):
        image = 0
        for r, row in enumerate(rows):
            if ((row & z).bit_count() & 1):
                image |= 1 << r
        out[z.bit_count()][image] += 1
    return out

def good_with_worst_ratio(rows, b):
    N = 2*b
    counts = shell_counts(rows, b)
    worst = Fraction(0,1)
    worst_w = None
    for w, cnt in enumerate(counts):
        C = comb(N,w)
        # Q_w = [2^b sum_x c_x^2 - C^2]/C^2.
        q_num = (1 << b) * sum(v*v for v in cnt.values()) - C*C
        # Q_w <= eta_w = 2(N+1)2^b/C is equivalent to q_num <= rhs.
        rhs = 2*(N+1)*(1 << b)*C
        ratio = Fraction(q_num, rhs)
        if ratio > worst:
            worst, worst_w = ratio, w
        if q_num > rhs:
            return False, worst, worst_w
    return True, worst, worst_w

def first_good_full_rank_seed(b, stop_after):
    L = 3*b-1
    for idx in range(stop_after+1):
        bits = bits_of_index(idx, L)
        rows = toeplitz_rows(bits, b)
        if rank_f2(rows) < b:
            continue
        good, worst, worst_w = good_with_worst_ratio(rows, b)
        if good:
            return idx, ''.join(map(str,bits)), rows, worst, worst_w
    raise RuntimeError('no good seed in certified scan range')

def projection_ratio(b,w):
    # For M=[0 I_b], image is the chosen subset in the second half.
    C = comb(2*b,w)
    sq = 0
    for j in range(max(0,w-b), min(b,w)+1):
        sq += comb(b,j) * comb(b,w-j)**2
    q_num = (1 << b)*sq - C*C
    rhs = 2*(2*b+1)*(1 << b)*C
    return Fraction(q_num, rhs)

expected = {
  2:(2,'00010'),
  3:(4,'00000100'),
  4:(8,'00000001000'),
  5:(16,'00000000010000'),
  6:(32,'00000000000100000'),
  7:(64,'00000000000001000000'),
  8:(128,'00000000000000010000000'),
  9:(515,'00000000000000001000000011'),
}
for b in range(2,10):
    idx, seed, rows, worst, worst_w = first_good_full_rank_seed(b, expected[b][0])
    assert (idx,seed) == expected[b]
    rowstrings = [format(r, f'0{2*b}b')[::-1] for r in rows]
    print(f'b={b} lex_index={idx} seed={seed} worst_ratio={worst} shell={worst_w}')
    print(' rows=' + ','.join(rowstrings))

# The trivial projection pattern is lex-first through b=8, but fails at b=9.
assert projection_ratio(9,5) == Fraction(49345,41344)
assert projection_ratio(9,6) == Fraction(1241411,1074944)
assert projection_ratio(9,5) > 1 and projection_ratio(9,6) > 1
print('b=9 projection [0 I_9] fails:')
print(' shell5 ratio=', projection_ratio(9,5))
print(' shell6 ratio=', projection_ratio(9,6))
print('ALL EXACT SMALL-SEED CHECKS PASSED')
