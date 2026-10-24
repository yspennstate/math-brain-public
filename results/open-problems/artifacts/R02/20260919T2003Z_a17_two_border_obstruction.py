A = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1],
[-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,1],
[1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1],
[-1,1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,1],
[1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,1],
[1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,1,1],
[-1,1,-1,1,-1,-1,1,1,1,-1,-1,-1,-1,1,1,1,1],
[1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,-1,1,1,1],
[-1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,1],
[1,-1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,-1,1,1,1],
[-1,1,1,-1,1,1,-1,1,1,-1,-1,-1,1,-1,1,1,1],
[-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,1,1],
[1,1,-1,-1,1,-1,1,-1,1,1,-1,1,-1,-1,1,1,1],
[-1,-1,1,1,-1,1,1,-1,1,1,1,-1,-1,-1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

N = 1 << 16

def vec(mask):
    return [(-1 if (mask >> j) & 1 else 1) for j in range(16)] + [1]

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

best = 99
minimizers = []
for mask in range(N):
    y = vec(mask)
    s = [sum(a*b for a,b in zip(row,y)) for row in A]
    m = max(abs(z) for z in s)
    if m < best:
        best = m
        minimizers = [(mask,s)]
    elif m == best:
        minimizers.append((mask,s))

singletons = []
for mask,s in minimizers:
    active = [i for i,z in enumerate(s) if abs(z) == best]
    if len(active) == 1:
        singletons.append(mask)

# For projective r,y with final coordinate +1,
# r.y = 17 - 2 d_H(r,y) on the first sixteen coordinates.
# Hence |r.y| <= 5 iff 6 <= d_H(r,y) <= 11.
f = [0] * N
for mask in singletons:
    f[mask] = 1
annulus = [1 if 6 <= mask.bit_count() <= 11 else 0 for mask in range(N)]

# Exact XOR convolution counts G(r) = singleton y with |r.y|<=5.
F = fwht(f)
K = fwht(annulus)
conv = fwht([x*y for x,y in zip(F,K)])
counts = [x // N for x in conv]

min_good = min(counts)
max_good = max(counts)
min_attainers = sum(c == min_good for c in counts)
common_pair_lb = 2 * min_good - len(singletons)

assert best == 7
assert len(minimizers) == 21952
assert len(singletons) == 3780
assert sum(annulus) == 56134
assert min_good == 3120
assert max_good == 3780
assert min_attainers == 3
assert min_good > len(singletons) // 2
assert common_pair_lb == 2460
assert common_pair_lb > 0

print('R02 A17 two-border exact obstruction checker')
print('projective_signings_checked =', N)
print('A17_discrepancy =', best)
print('A17_minimizers =', len(minimizers))
print('singleton_minimizers =', len(singletons))
print('hamming_annulus_delta_masks_6_to_11 =', sum(annulus))
print('projective_border_rows_counted =', len(counts))
print('min_good_singletons_per_border_row =', min_good)
print('max_good_singletons_per_border_row =', max_good)
print('border_rows_attaining_min =', min_attainers)
print('half_singleton_count =', len(singletons)/2)
print('two_border_rows_common_singletons_lower_bound =', common_pair_lb)
print('THEOREM_CORE: every pair of projective added rows r1,r2 has')
print('a singleton A17 minimizer y with |r1.y|<=5 and |r2.y|<=5.')
print('COROLLARY: every 19x19 sign matrix having this A17 as its')
print('upper-left 17x17 principal block has discrepancy <= 7.')
print('PASS')
