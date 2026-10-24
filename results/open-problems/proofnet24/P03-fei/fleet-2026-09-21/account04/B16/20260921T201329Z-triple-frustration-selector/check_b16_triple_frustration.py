from fractions import Fraction
import random

# Cube convention: old coordinates 0..n_old-1, dummy coordinate n_old.

def pts(d):
    return range(1 << d)

def mul(a, b):
    return tuple(x * y for x, y in zip(a, b))

def Q(phase, x, u, v):
    return phase[x] * phase[x ^ u] * phase[x ^ v] * phase[x ^ u ^ v]

def P(phase, u, v):
    d = (len(phase)).bit_length() - 1
    return Fraction(sum(Q(phase, x, u, v) == -1 for x in pts(d)), 1 << d)

def Dpair(H, h0, h1, u, v):
    g = mul(h0, h1)
    return P(H, u, v) + P(mul(H, g), u, v) - P(mul(H, h0), u, v) - P(mul(H, h1), u, v)

def Dtriple(H, f, h0, h1, u, v):
    return Dpair(H, h0, h1, u, v) - Dpair(mul(H, f), h0, h1, u, v)

def rhs(H, f, h0, h1, u, v):
    d = (len(H)).bit_length() - 1
    acc = 0
    for x in pts(d):
        acc += Q(H, x, u, v) * (1 - Q(h0, x, u, v)) * (1 - Q(h1, x, u, v)) * (1 - Q(f, x, u, v))
    return -Fraction(acc, 2 * (1 << d))

def phase_from_mask(d, mask):
    return tuple(-1 if ((mask >> x) & 1) else 1 for x in pts(d))

def slice_pair(n_old, c):
    d = n_old + 1
    dummy = n_old
    def in_A(x):
        return all(((x >> j) & 1) == 0 for j in range(c))
    out = []
    for b in (0, 1):
        arr = []
        for x in pts(d):
            neg = in_A(x) and (((x >> dummy) & 1) == b)
            arr.append(-1 if neg else 1)
        out.append(tuple(arr))
    return tuple(out)

def parent_g_old(n_old, c):
    arr = []
    for x in range(1 << n_old):
        neg = all(((x >> j) & 1) == 0 for j in range(c))
        arr.append(-1 if neg else 1)
    return tuple(arr)

def folded_influence(phase):
    n = (len(phase)).bit_length() - 1
    out = Fraction(0)
    for i in range(n):
        diff = sum(phase[x] != phase[x ^ (1 << i)] for x in range(1 << n))
        p = Fraction(diff, 1 << n)
        out += min(p, 1 - p)
    return out

def noise_prob(mask, d, p):
    k = mask.bit_count()
    return p ** k * (1 - p) ** (d - k)

random.seed(20260921)
n_old = 2
d = 3
h0, h1 = slice_pair(n_old, 2)

identity_checks = 0
for _ in range(1200):
    H = phase_from_mask(d, random.randrange(1 << (1 << d)))
    f = phase_from_mask(d, random.randrange(1 << (1 << d)))
    u = random.randrange(1 << d)
    v = random.randrange(1 << d)
    assert Dtriple(H, f, h0, h1, u, v) == rhs(H, f, h0, h1, u, v)
    identity_checks += 1

for fmask in [0, 1, 3, 5, 17, 85, 170, 255]:
    f = phase_from_mask(d, fmask)
    for u, v in [(1, 2), (1, 4), (2, 4), (3, 5), (7, 6)]:
        for Hmask in range(256):
            H = phase_from_mask(d, Hmask)
            assert Dtriple(H, f, h0, h1, u, v) == rhs(H, f, h0, h1, u, v)
            identity_checks += 1

support_checks = 0
for _ in range(1200):
    H = phase_from_mask(d, random.randrange(256))
    f = phase_from_mask(d, random.randrange(256))
    u = random.randrange(8)
    v = random.randrange(8)
    dtr = Dtriple(H, f, h0, h1, u, v)
    pairprob = Fraction(sum(Q(h0, x, u, v) == -1 and Q(h1, x, u, v) == -1 for x in range(8)), 8)
    tripleprob = Fraction(sum(Q(h0, x, u, v) == -1 and Q(h1, x, u, v) == -1 and Q(f, x, u, v) == -1 for x in range(8)), 8)
    assert abs(dtr) <= 4 * tripleprob <= 4 * pairprob
    support_checks += 1

J = folded_influence(parent_g_old(n_old, 2))
assert J == 1
noise_checks = 0
worst = Fraction(0)
worst_case = None
ps = [Fraction(1, 8), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)]
for _ in range(80):
    H = phase_from_mask(d, random.randrange(256))
    f = phase_from_mask(d, random.randrange(256))
    for s in ps:
        for t in ps:
            val = Fraction(0)
            for u in range(8):
                pu = noise_prob(u, d, s)
                for v in range(8):
                    pv = noise_prob(v, d, t)
                    val += pu * pv * abs(Dtriple(H, f, h0, h1, u, v))
            bound = 8 * s * t * (1 - s * t) * J
            assert val <= bound, (val, bound, s, t)
            ratio = val / bound if bound else Fraction(0)
            if ratio > worst:
                worst = ratio
                worst_case = (s, t, val, bound)
            noise_checks += 1

integ = 8 * (Fraction(1, 4) - Fraction(1, 64))
assert integ == Fraction(15, 8)

affine_checks = 0
for linear_mask in range(1 << n_old):
    for const in (0, 1):
        f = []
        for x in range(8):
            xo = x & 3
            parity = (linear_mask & xo).bit_count() & 1
            f.append(-1 if parity ^ const else 1)
        f = tuple(f)
        for Hmask in range(32):
            H = phase_from_mask(d, Hmask)
            for u, v in [(1, 2), (1, 4), (3, 5), (7, 6)]:
                assert Dtriple(H, f, h0, h1, u, v) == 0
                affine_checks += 1

h0c1, h1c1 = slice_pair(1, 1)
H = (1,) * 4
f = h0c1
u_old = 1
v_dummy = 2
obs = abs(Dtriple(H, f, h0c1, h1c1, u_old, v_dummy))
Jc1 = folded_influence(parent_g_old(1, 1))
assert obs == 4 and Jc1 == 0

print('PASS')
print('identity_checks', identity_checks)
print('support_checks', support_checks)
print('noise_checks', noise_checks)
print('worst_noise_ratio', f'{worst.numerator}/{worst.denominator}', float(worst), worst_case)
print('affine_zero_checks', affine_checks)
print('integrated_envelope_constant', f'{integ.numerator}/{integ.denominator}', float(integ))
print('generic_c1_obstruction_abs', obs, 'parent_J', Jc1)
