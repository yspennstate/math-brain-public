#!/usr/bin/env python3
from fractions import Fraction
import json, random

def aa(m):
    return Fraction(1, (1 << m) * m)

stats = {}

# 1. Exact central multiplier Hodge-Shapley ladder.
ladder_cases = 0
ladder_position_terms = 0
for q in range(3, 200, 2):
    for k in range(1, q, 2):
        r = (q-k)//2
        eps = 2*aa(q)*(aa(k)-aa(q))
        eta = []
        for ell in range(1, r+1):
            m = k + 2*ell
            val = 2*aa(q)*(aa(m-2)-aa(m))
            assert val > 0
            eta.append(val)
        assert sum(eta, Fraction()) == eps
        assert sum(eta, Fraction())/r == eps/r
        ladder_cases += 1
        ladder_position_terms += r
stats["central_multiplier_ladder_cases"] = ladder_cases
stats["ladder_position_terms"] = ladder_position_terms

# 2. Exact Fourier-square coefficient at a four-set Q.
qmode_cases = 0
qmode_terms = 0
for m in range(4, 9):
    Q = (1 << 4) - 1
    for seed in range(100):
        rng = random.Random((m << 16) + seed)
        b = [0] * (1 << m)
        for R in range(1 << m):
            if R.bit_count() % 2:
                b[R] = rng.randrange(-7, 8)
        total = sum(b[R]*b[R ^ Q] for R in range(1 << m))
        cls = [0] * 5
        for R in range(1 << m):
            cls[(R & Q).bit_count()] += b[R]*b[R ^ Q]
            qmode_terms += 1
        assert total == sum(cls)
        assert cls[0] == cls[4]
        assert cls[1] == cls[3]
        outside = ((1 << m)-1) ^ Q
        c13 = 0
        sub = outside
        while True:
            if sub.bit_count() % 2 == 0:
                for i in range(4):
                    R = sub | (1 << i)
                    T = Q ^ (1 << i)
                    c13 += 2*b[R]*b[sub | T]
            if sub == 0:
                break
            sub = (sub-1) & outside
        assert c13 == cls[1] + cls[3]
        qmode_cases += 1
stats["qmode_decomposition_cases"] = qmode_cases
stats["qmode_terms_checked"] = qmode_terms

# 3. Ordered-min q-flip is exactly one physical ordered flag.
def vals_from_bits(n, bits):
    N = 1 << n
    out = [1]
    out.extend(-1 if ((bits >> (x-1)) & 1) else 1 for x in range(1, N))
    return out

def least_i(v):
    return (v & -v).bit_length()-1

def deriv(vals, i, x0):
    assert ((x0 >> i) & 1) == 0
    return (vals[x0] - vals[x0 ^ (1 << i)]) // 2

flag_cases = frustrated_cases = orientation_cases = 0
families = [(2, range(1 << ((1 << 2)-1))),
            (3, range(1 << ((1 << 3)-1))),
            (4, range(1024))]
for n, bit_iter in families:
    N = 1 << n
    for bits in bit_iter:
        vals = vals_from_bits(n, bits)
        for a0 in range(N):
            for v in range(1, N):
                if v.bit_count() < 2:
                    continue
                i = least_i(v)
                ei = 1 << i
                w = v ^ ei
                assert ((w >> i) & 1) == 0
                assert all(j > i for j in range(n) if (w >> j) & 1)
                e1 = vals[a0] * vals[a0 ^ ei]
                e2 = vals[a0 ^ v] * vals[a0 ^ v ^ ei]
                z = e1 * e2
                base = a0 if ((a0 >> i) & 1) == 0 else a0 ^ ei
                other = (a0 ^ v) if (((a0 ^ v) >> i) & 1) == 0 else (a0 ^ v ^ ei)
                assert base ^ w == other
                d1 = deriv(vals, i, base)
                d2 = deriv(vals, i, base ^ w)
                p = int((d1*d1) != (d2*d2))
                o = int(d1 != 0 and d2 == -d1)
                kap = (d1-d2)**2
                assert z == (-1 if p else 1)
                assert kap == p + 4*o
                flag_cases += 1
                frustrated_cases += p
                orientation_cases += o
stats["physical_flag_cases"] = flag_cases
stats["frustrated_flag_instances"] = frustrated_cases
stats["opposite_orientation_instances"] = orientation_cases

# 4. All-background affine-plane Hodge integrand relation.
s = Fraction(3, 5)
c = Fraction(4, 5)
tan2 = (s/c)**2

def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

def cscale(q, z):
    return (q*z[0], q*z[1])

IPOW = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]
rng = random.Random(1609)
hodge_cases = 0
for bdeg in range(21):
    U = bdeg + 4
    for _ in range(40):
        sigma = rng.choice([-1, 1])
        Z = (Fraction(rng.randrange(-5, 6), 7),
             Fraction(rng.randrange(-5, 6), 11))
        bg = rng.choice([-1, 1])
        yi = rng.choice([-1, 1])
        prodT = sigma * yi  # chi_Q=1 on RM(1,D)
        low = cmul(Z, IPOW[(bdeg+1) % 4])
        low = cscale(Fraction(bg*yi) * s**(bdeg+1) * c**(U-bdeg-1), low)
        high = cmul(Z, IPOW[(bdeg+3) % 4])
        high = cscale(Fraction(bg*prodT) * s**(bdeg+3) * c**(U-bdeg-3), high)
        assert high == cscale(Fraction(-sigma) * tan2, low)
        hodge_cases += 1
stats["background_hodge_integrand_cases"] = hodge_cases

stats["status"] = "PASS"
print(json.dumps(stats, sort_keys=True, indent=2))
