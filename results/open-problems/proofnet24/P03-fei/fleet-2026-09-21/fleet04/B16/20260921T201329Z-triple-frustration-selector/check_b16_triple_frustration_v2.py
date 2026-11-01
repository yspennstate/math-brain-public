from fractions import Fraction
import random


def mul(a, b):
    return tuple(x * y for x, y in zip(a, b))


def qsign(phase, x, u, v):
    return phase[x] * phase[x ^ u] * phase[x ^ v] * phase[x ^ u ^ v]


def pfrust(phase, u, v):
    size = len(phase)
    return Fraction(sum(qsign(phase, x, u, v) == -1 for x in range(size)), size)


def dpair(H, h0, h1, u, v):
    g = mul(h0, h1)
    return pfrust(H, u, v) + pfrust(mul(H, g), u, v) - pfrust(mul(H, h0), u, v) - pfrust(mul(H, h1), u, v)


def dtriple(H, f, h0, h1, u, v):
    return dpair(H, h0, h1, u, v) - dpair(mul(H, f), h0, h1, u, v)


def rhs(H, f, h0, h1, u, v):
    size = len(H)
    total = 0
    for x in range(size):
        total += qsign(H, x, u, v) * (1 - qsign(h0, x, u, v)) * (1 - qsign(h1, x, u, v)) * (1 - qsign(f, x, u, v))
    return -Fraction(total, 2 * size)


def phase(mask, d):
    return tuple(-1 if (mask >> x) & 1 else 1 for x in range(1 << d))


def slices(n_old, codim):
    d = n_old + 1
    dummy = n_old
    out = []
    for b in (0, 1):
        arr = []
        for x in range(1 << d):
            in_a = all(((x >> j) & 1) == 0 for j in range(codim))
            neg = in_a and (((x >> dummy) & 1) == b)
            arr.append(-1 if neg else 1)
        out.append(tuple(arr))
    return tuple(out)


def parent(n_old, codim):
    arr = []
    for x in range(1 << n_old):
        in_a = all(((x >> j) & 1) == 0 for j in range(codim))
        arr.append(-1 if in_a else 1)
    return tuple(arr)


def folded_influence(g):
    n = (len(g)).bit_length() - 1
    out = Fraction(0)
    for i in range(n):
        p = Fraction(sum(g[x] != g[x ^ (1 << i)] for x in range(1 << n)), 1 << n)
        out += min(p, 1 - p)
    return out


def noise_weight(mask, d, p):
    k = mask.bit_count()
    return p**k * (1 - p)**(d - k)


random.seed(20260921)
n_old = 2
d = 3
h0, h1 = slices(n_old, 2)

identity_checks = 0
for _ in range(2000):
    H = phase(random.randrange(256), d)
    f = phase(random.randrange(256), d)
    u = random.randrange(8)
    v = random.randrange(8)
    assert dtriple(H, f, h0, h1, u, v) == rhs(H, f, h0, h1, u, v)
    identity_checks += 1

support_checks = 0
for _ in range(2000):
    H = phase(random.randrange(256), d)
    f = phase(random.randrange(256), d)
    u = random.randrange(8)
    v = random.randrange(8)
    lhs = abs(dtriple(H, f, h0, h1, u, v))
    triple = Fraction(sum(qsign(h0, x, u, v) == -1 and qsign(h1, x, u, v) == -1 and qsign(f, x, u, v) == -1 for x in range(8)), 8)
    pair = Fraction(sum(qsign(h0, x, u, v) == -1 and qsign(h1, x, u, v) == -1 for x in range(8)), 8)
    assert lhs <= 4 * triple <= 4 * pair
    support_checks += 1

J = folded_influence(parent(n_old, 2))
assert J == 1
ps = [Fraction(1, 8), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)]
noise_checks = 0
worst = Fraction(0)
for _ in range(64):
    H = phase(random.randrange(256), d)
    f = phase(random.randrange(256), d)
    for s in ps:
        for t in ps:
            lhs = Fraction(0)
            for u in range(8):
                for v in range(8):
                    lhs += noise_weight(u, d, s) * noise_weight(v, d, t) * abs(dtriple(H, f, h0, h1, u, v))
            bound = 8 * s * t * (1 - s * t) * J
            assert lhs <= bound
            if bound:
                worst = max(worst, lhs / bound)
            noise_checks += 1

# Every affine character has trivial plaquette sign, so the phase switch vanishes.
affine_checks = 0
for linear in range(1 << n_old):
    for const in (0, 1):
        f = []
        for x in range(8):
            old = x & 3
            bit = ((linear & old).bit_count() & 1) ^ const
            f.append(-1 if bit else 1)
        f = tuple(f)
        for Hmask in range(64):
            H = phase(Hmask, d)
            for u, v in ((1, 2), (1, 4), (3, 5), (7, 6)):
                assert dtriple(H, f, h0, h1, u, v) == 0
                affine_checks += 1

# Generic c=1 obstruction when the phase is allowed to depend on the dummy bit.
h0c1, h1c1 = slices(1, 1)
Hc1 = (1, 1, 1, 1)
fc1 = h0c1
u_old = 1
v_dummy = 2
obstruction = abs(dtriple(Hc1, fc1, h0c1, h1c1, u_old, v_dummy))
Jc1 = folded_influence(parent(1, 1))
assert obstruction == 4
assert Jc1 == 0

integrated_constant = 8 * (Fraction(1, 4) - Fraction(1, 64))
assert integrated_constant == Fraction(15, 8)

print('PASS')
print('identity_checks', identity_checks)
print('support_checks', support_checks)
print('noise_checks', noise_checks)
print('worst_noise_ratio', f'{worst.numerator}/{worst.denominator}', float(worst))
print('affine_zero_checks', affine_checks)
print('integrated_envelope_constant', '15/8', float(integrated_constant))
print('generic_c1_obstruction_abs', obstruction, 'parent_J', Jc1)
