import math


def lower_const(q):
    return 0.5 * (3/(2*math.pi))**q

# Hausdorff--Young/cap exponent algebra.
for q in (2, 3, 4, 10):
    p = q/(q-1)
    assert abs((p-1)*(q-1)-1) < 1e-12
    hy_cap = 2*math.pi * 2**(-((p-1)*(q-1)))
    assert abs(hy_cap-math.pi) < 1e-12
    print('q', q, 'p', p, 'HYcap', hy_cap)

# Quantitative lower-bound constants for the separated-fragment stress family.
for q in (1.0, 1.5, 1.9, 2.0):
    c = lower_const(q)
    print(f'q={q:.1f} coefficient={c:.15f}')
    for N in (10, 100, 1000):
        value = c * N**(2-q) * (1-1/N)
        print(' ', N, f'{value:.15f}')

# Base-10 center differences are unique in a finite stress set.
N = 8
centers = [10**k for k in range(1, N+1)]
diffs = {}
for k, x in enumerate(centers):
    for l, y in enumerate(centers):
        if k == l:
            continue
        d = x-y
        assert d not in diffs
        diffs[d] = (k,l)
ds = sorted(diffs)
mindiff = min(b-a for a,b in zip(ds,ds[1:]))
print('ordered_difference_count', len(diffs), 'min_spacing', mindiff)

partner = math.sqrt(2/(3*math.pi))
assert abs(partner-0.46065886596178063) < 1e-15
print('partner_fejer_coeff', partner)
print('STATUS=PASS')
