#!/usr/bin/env python3
import itertools, math, json, random

TOL = 2e-12
S_GRID = (0.125, 0.5, 1.0, 1.7, 2.3, 3.1)

def rm1_masks(n):
    N = 1 << n
    out = []
    for a0 in (0, 1):
        for coeff in itertools.product((0, 1), repeat=n):
            bits = []
            for x in range(N):
                v = a0
                for i, c in enumerate(coeff):
                    if c:
                        v ^= (x >> i) & 1
                bits.append(v)
            out.append(tuple(bits))
    return tuple(out)

def bxor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))

def beta(z, m):
    N = len(z)
    return sum(1 if (z[i] ^ m[i]) == 0 else -1 for i in range(N)) / N

def packet_component(M, z, g, s):
    # 2 sin(su)sin(sv)=cos(s beta(z+m+g))-cos(s beta(z+m)).
    return sum(
        0.5 * (math.cos(s * beta(z, bxor(m, g))) - math.cos(s * beta(z, m)))
        for m in M
    ) / len(M)

def gate_packet(M, b, g, s):
    zero = (0,) * len(b)
    return packet_component(M, b, g, s) - packet_component(M, zero, g, s)

def codim1_mask(n, i, value):
    N = 1 << n
    return tuple(1 if ((x >> i) & 1) == value else 0 for x in range(N))

rng = random.Random(180311)
affine_checks = 0
max_affine_abs = 0.0
membership_checks = 0

for n in range(1, 6):
    M = rm1_masks(n)
    Mset = set(M)
    N = 1 << n
    if n <= 3:
        phases = [
            tuple((mask >> x) & 1 for x in range(N))
            for mask in range(1 << N)
        ]
    else:
        phases = [tuple(rng.randrange(2) for _ in range(N)) for _ in range(96)]
    for i in range(n):
        for value in (0, 1):
            g = codim1_mask(n, i, value)
            assert g in Mset
            membership_checks += 1
    for g in M:
        for b in phases:
            for s in S_GRID:
                val = gate_packet(M, b, g, s)
                affine_checks += 1
                max_affine_abs = max(max_affine_abs, abs(val))
                if abs(val) > TOL:
                    raise AssertionError((n, s, val))

# Exact codimension-two refutation to an overextension:
# n=2, singleton gate g=b=1_{00}.  RM(1,2) is the 8-word even-parity code.
# Directly G(s) = (cos s + 3)/4 - cos(s/2), nonzero for generic s.
n = 2
M = rm1_masks(n)
g = (1, 0, 0, 0)
b = g
counter = {}
for s in (0.5, 1.0, 2.0):
    direct = gate_packet(M, b, g, s)
    closed = (math.cos(s) + 3.0) / 4.0 - math.cos(s / 2.0)
    if abs(direct - closed) > TOL:
        raise AssertionError(("closed-form mismatch", s, direct, closed))
    if not (direct > 0):
        raise AssertionError(("expected nonzero positive counterexample", s, direct))
    counter[str(s)] = direct

# Clone-square sanity mechanism: tau_g=tau0*tau1 invariance does not kill
# the two-clone second difference.  On the 4-state orbit take F=(a,b,b,a).
# Then (I-tau_g)F=0 while D=(I-tau0)(I-tau1)F is generally nonzero.
clone_checks = 0
for a, bb in ((0.0, 1.0), (2.0, -1.0), (3.5, 0.25)):
    F = (a, bb, bb, a)
    tau0 = (F[1], F[0], F[3], F[2])
    tau1 = (F[2], F[3], F[0], F[1])
    taug = (F[3], F[2], F[1], F[0])
    coarse = tuple(F[i] - taug[i] for i in range(4))
    D = tuple(F[i] - tau0[i] - tau1[i] + taug[i] for i in range(4))
    expected = (2*(a-bb), -2*(a-bb), -2*(a-bb), 2*(a-bb))
    assert max(abs(x) for x in coarse) <= TOL
    assert max(abs(D[i] - expected[i]) for i in range(4)) <= TOL
    clone_checks += 1

out = {
    "status": "PASS",
    "theorem": "g in M implies the signed gate packet vanishes pointwise in Borel time",
    "affine_gate_packet_checks": affine_checks,
    "max_abs_affine_gate_packet": max_affine_abs,
    "codim1_membership_checks": membership_checks,
    "codim2_counterexample": {
        "n": 2,
        "gate_and_phase": "singleton 1_{00}",
        "closed_form": "(cos(s)+3)/4-cos(s/2)",
        "values": counter,
        "small_s_leading_term": "s^4/128"
    },
    "clone_square_sanity_checks": clone_checks,
    "scope_note": "finite checks are self-check evidence; the all-dimensional theorem is algebraic"
}
print(json.dumps(out, indent=2, sort_keys=True))
