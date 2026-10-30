from fractions import Fraction as Q
from itertools import permutations


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def dot(n, z):
    return n[0] * z[0] + n[1] * z[1]


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


P = list(permutations(range(4)))
NAMES = [''.join(str(j + 1) for j in p) for p in P]


def analyze(a, b, gates):
    def vertex(p):
        z = (1, 0)
        for i, j in enumerate(p):
            z = mul(z, (a[i][0] + b[j][0], a[i][1] + b[j][1]))
        return z

    V = {n: vertex(p) for n, p in zip(NAMES, P)}
    labels = {}
    for n, z in V.items():
        labels.setdefault(z, []).append(n)
    pts = sorted(labels)
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    H = lo[:-1] + hi[:-1]

    (c1, s1), (c2, s2), (c3, s3) = gates
    assert c1 * c1 + s1 * s1 == 1
    assert c2 * c2 + s2 * s2 == 1
    assert c3 * c3 + s3 * s3 == 1
    A, B = c1 * c1, s1 * s1
    u, v = c2 * c2, s2 * s2
    r, t = c3 * c3, s3 * s3
    w0 = {
        '1234': A * u * r, '1243': A * u * t,
        '1324': A * r * v, '1423': A * v * t,
        '2134': B * u * r, '2143': B * u * t,
        '3124': B * r * v, '4123': B * v * t,
    }
    w1 = {
        '1423': B * v * t, '2413': B * u * t,
        '2431': B * u * r, '3421': B * r * v,
        '4123': A * v * t, '4213': A * u * t,
        '4231': A * u * r, '4321': A * r * v,
    }
    assert sum(w0.values()) == 1 and sum(w1.values()) == 1

    rows = []
    for k, p in enumerate(H):
        q = H[(k + 1) % len(H)]
        dx, dy = q[0] - p[0], q[1] - p[1]
        n = (dy, -dx)
        M = dot(n, p)
        d = {nm: Q(M - dot(n, z)) for nm, z in V.items()}
        assert all(x >= 0 for x in d.values())

        chi = d['1423'] - d['4123']
        assert chi == d['1243'] - d['2143'] + d['2413'] - d['4213']
        assert chi == d['1324'] - d['3124'] + d['3421'] - d['4321']

        delta0 = sum(w * d[nm] for nm, w in w0.items())
        delta1 = sum(w * d[nm] for nm, w in w1.items())
        target = A * B * v * t * chi * chi
        payment = delta0 * delta1 - target

        R0 = u * r * (A * d['1234'] + B * d['2134'])
        R1 = u * r * (B * d['2431'] + A * d['4231'])
        x = abs(chi)
        if chi >= 0:
            E0 = (R0 + A * x * v * t) * (R1 + B * x * (1 - u * r))
            E1 = (R0 + A * x * (1 - u * r)) * (R1 + B * x * v * t)
        else:
            E0 = (R0 + B * x * v * t) * (R1 + A * x * (1 - u * r))
            E1 = (R0 + B * x * (1 - u * r)) * (R1 + A * x * v * t)
        reserve_lb = min(E0, E1) - target
        assert payment >= reserve_lb
        rows.append((labels[p][0], labels[q][0], payment, reserve_lb, chi))
    return [labels[p][0] for p in H], rows


stress_a = [(10, -13), (-18, 17), (-20, 5), (-20, 11)]
stress_b = [(17, -18), (-22, 3), (-19, -7), (2, 7)]
stress_g = [
    (Q(3, 5), Q(4, 5)),
    (Q(7, 25), Q(24, 25)),
    (Q(7, 25), Q(24, 25)),
]
H, rows = analyze(stress_a, stress_b, stress_g)
assert H == ['4213', '2143', '2134', '2431', '2413', '1423', '1432', '1234', '1243']
assert all(r[3] > 0 for r in rows)
print('stress_hull =', H)
for x, y, pay, lb, chi in rows:
    print(f'{x}--{y} payment={pay} reserve_lb={lb} chi={chi}')
print('stress_min_payment =', min(r[2] for r in rows))
print('stress_min_reserve_lb =', min(r[3] for r in rows))

res_a = [(-4, -1), (-4, -4), (2, -6), (-4, -6)]
res_b = [(-3, 4), (5, -3), (-1, 2), (-5, -3)]
res_g = [
    (Q(24, 25), Q(7, 25)),
    (Q(5, 13), Q(12, 13)),
    (Q(21, 29), Q(20, 29)),
]
H2, rows2 = analyze(res_a, res_b, res_g)
r = [z for z in rows2 if {z[0], z[1]} == {'4231', '2431'}]
assert len(r) == 1
x, y, pay, lb, chi = r[0]
assert pay > 0 and lb < 0
print('residual_hull =', H2)
print(f'residual_edge={x}--{y} payment={pay} reserve_lb={lb} chi={chi}')
print('PASS MOC4-ONE-CYCLE-RESERVE-BOUND-v1')
