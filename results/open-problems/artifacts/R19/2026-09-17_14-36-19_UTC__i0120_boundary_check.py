from math import gcd

P = 37
K = 14
DEN = 15
T = (15,30,55,25,35,230,5,40,65,10,45,50,1,2)
Y = (3,6,11,5,7,46,1,8,13,2,9,10)
LEVELS = (1,3,5,15)


def folded(x, m):
    x %= m
    return min(x, m-x)


def witnesses(v, m):
    return [a for a in range(m) if all(DEN * folded(a*x, m) >= m for x in v)]


def gcd_proper_omissions(v, l):
    out = []
    for i in range(len(v)):
        g = l
        for j, x in enumerate(v):
            if j != i:
                g = gcd(g, x)
        if g > 1:
            out.append((i, g))
    return out


def e_q(v, q):
    return sum(x % q != 0 for x in v)


print('R19 I0120 exact factor-aligned boundary obstruction check')
print('base prime p =', P)
print('T =', T)

assert len(T) == K
assert all(x % P != 0 for x in T)

for l in LEVELS:
    m = P*l
    v = tuple(x % m for x in T)
    assert (v[1] - 2*v[0]) % m == 0
    ws = witnesses(v, m)
    gp = gcd_proper_omissions(v, l)
    assert ws == []
    assert gp == []
    row = {
        'level': l,
        'modulus': m,
        'relation_residue': (v[1]-2*v[0]) % m,
        'witness_count': len(ws),
        'gcd_proper_omissions': gp,
        'e3': e_q(v, 3),
        'e5': e_q(v, 5),
    }
    print(row)

assert e_q(T, 5) == 2
assert e_q(T, 3) >= 2

# The first 12 coordinates are a q=5 inflation of a 12-coordinate
# no-witness core Y at level 3 (modulus 111).
assert T[:12] == tuple(5*y for y in Y)
assert T[12:] == (1,2)
assert gcd(T[12], 15) == gcd(T[13], 15) == 1
M0 = P*3
assert all(y % P != 0 for y in Y)
assert (Y[1] - 2*Y[0]) % M0 == 0
assert witnesses(Y, M0) == []
print('core_Y_level3 =', Y)
print('core_Y_modulus =', M0, 'witness_count =', len(witnesses(Y, M0)))
print('inflation_identity = PASS: T[:12] = 5*Y and last two coordinates are units 1,2')

# Exact gcd-boundary criterion specialized to l=15:
# the gcd clause can hold iff some prime q|15 has e_q <= 1.
# Here both e_3 and e_5 are at least two, with e_5 exactly two.
assert e_q(T, 3) >= 2 and e_q(T, 5) >= 2
assert gcd_proper_omissions(T, 15) == []
print('boundary_counts_at_l15 =', {'e3': e_q(T,3), 'e5': e_q(T,5)})
print('ALL_EXACT_CHECKS_PASS')
