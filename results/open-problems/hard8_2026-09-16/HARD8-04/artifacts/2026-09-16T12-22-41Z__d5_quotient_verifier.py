from math import isqrt

TEST_REPS = {
1: (-1,0,0,0,1),
2: (-1,-1,0,1,1),
3: (-2,0,0,1,1),
5: (-2,-1,0,1,2),
6: (-3,0,1,1,1),
7: (-3,0,0,1,2),
10: (-4,1,1,1,1),
13: (-4,-1,1,2,2),
14: (-4,-1,1,1,3),
15: (-4,-1,0,2,3),
17: (-5,0,1,2,2),
19: (-5,-1,2,2,2),
21: (-5,0,0,1,4),
22: (-5,-1,0,3,3),
23: (-6,1,1,2,2),
26: (-5,-1,-1,3,4),
29: (-6,-1,1,2,4),
30: (-5,-3,1,3,4),
31: (-7,1,2,2,2),
34: (-7,0,1,3,3),
35: (-7,0,1,2,4),
37: (-7,-1,2,2,4),
42: (-8,1,1,3,3),
58: (-9,-1,3,3,4),
93: (-12,1,3,4,4),
110: (-13,1,3,4,5),
145: (-15,2,3,4,6),
203: (-18,4,4,5,5),
290: (-21,1,5,7,8),
}
TESTSET = [1,2,3,5,6,7,10,13,14,15,17,19,21,22,23,26,29,30,31,34,35,37,42,58,93,110,145,203,290]


def qform4(x):
    assert len(x) == 4
    return sum(t*t for t in x) + sum(x[i]*x[j] for i in range(4) for j in range(i+1,4))


def q_energy(n, step):
    return sum((n[i] - n[(i+step)%5])**2 for i in range(5)) // 2


def autocorr(n, shift):
    return sum(n[i] * n[(i+shift)%5] for i in range(5))


def tau(u):
    return tuple(u[(2*r) % 5] for r in range(5))

# 1. Verify the full 290-Theorem test certificate.
for N in TESTSET:
    u = TEST_REPS[N]
    assert sum(u) == 0
    assert sum(t*t for t in u) == 2*N
    assert qform4(u[:4]) == N
print('BHARGAVA_HANKE_TEST_VALUES_VERIFIED', len(TESTSET))

# 2. Build a deterministic meet-in-the-middle table that finds A4 vectors
#    of half squared norm 2s for all s in a finite consistency range.
MAX_S = 500
B = isqrt(4*MAX_S)
if B*B < 4*MAX_S:
    B += 1
vals = range(-B, B+1)
triple = {}
for c in vals:
    cc = c*c
    for d in vals:
        ccd = cc + d*d
        for e in vals:
            sq = ccd + e*e
            if sq <= 4*MAX_S:
                key = (c+d+e, sq)
                if key not in triple:
                    triple[key] = (c,d,e)

def find_u(s):
    if s == 1:
        return (-1,-1,0,1,1)
    if s == 2:
        return (-2,-1,1,1,1)
    if s == 3:
        return (-3,0,1,1,1)
    target_sq = 4*s
    lim = isqrt(4*s)
    if lim*lim < 4*s:
        lim += 1
    for a in range(-lim, lim+1):
        for b in range(-lim, lim+1):
            rem = target_sq - a*a - b*b
            if rem < 0:
                continue
            key = (-(a+b), rem)
            t = triple.get(key)
            if t is None:
                continue
            u = (a,b) + t
            if max(abs(x) for x in u) <= lim:
                assert sum(u) == 0
                assert sum(x*x for x in u) == target_sq
                return u
    raise AssertionError(f'no A4 vector found for s={s}')

# 3. Verify every quotient equation for s<=MAX_S.
cert_count = 0
energy_swap_count = 0
for s in range(1, MAX_S+1):
    u = find_u(s)
    assert sum(u) == 0
    assert sum(x*x for x in u) == 4*s
    if s >= 4:
        assert max(abs(x) for x in u)**2 <= 4*s
    assert max(abs(x) for x in u) <= s

    tu = tau(u)
    n1 = (s-1, s, s, s, s)
    n2 = tuple(s+x for x in u)
    n3 = tuple(s+x for x in tu)
    n4 = (s,s,s,s,s)
    blocks = (n1,n2,n3,n4)

    assert [sum(n) for n in blocks] == [5*s-1,5*s,5*s,5*s]
    for n in blocks:
        assert all(0 <= x <= 2*s for x in n)

    q1u, q2u = q_energy(u,1), q_energy(u,2)
    assert q_energy(tu,1) == q2u
    assert q_energy(tu,2) == q1u
    assert q1u + q2u == 10*s
    energy_swap_count += 2

    assert sum(q_energy(n,1) for n in blocks) == 10*s+1
    assert sum(q_energy(n,2) for n in blocks) == 10*s+1

    v = 10*s
    h = 2*s
    target0 = h*(v-2) + (v+1)
    target_nonzero = h*(v-2)
    got = [sum(autocorr(n,sh) for n in blocks) for sh in range(5)]
    assert got[0] == target0
    assert all(got[sh] == target_nonzero for sh in range(1,5))
    cert_count += 1

print('D5_QUOTIENT_CERTIFICATES_VERIFIED', cert_count)
print('ENERGY_SWAP_IDENTITIES_VERIFIED', energy_swap_count)
print('FINITE_RANGE', f's=1..{MAX_S}', f'v=10..{10*MAX_S}')
print('ALL_EXACT_D5_CHECKS_PASSED')
