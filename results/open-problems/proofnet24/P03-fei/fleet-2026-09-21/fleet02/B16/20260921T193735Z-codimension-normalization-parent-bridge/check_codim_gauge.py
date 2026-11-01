#!/usr/bin/env python3
from fractions import Fraction
import json

def chi(n, ell, b, x):
    # affine {±1} character on F_2^n
    return -1 if ((b ^ ((ell & x).bit_count() & 1)) & 1) else 1

def qflip_sign(vals, a, i, w):
    ei = 1 << i
    return vals[a] * vals[a ^ ei] * vals[a ^ w] * vals[a ^ ei ^ w]

def tau(vals, a, i):
    return vals[a] * vals[a ^ (1 << i)]

# 1) Exact codimension-normalization algebra.
codim_cases = 0
for c in range(2, 33):
    maxP = Fraction(1, 2 ** (c - 2))  # 2^(2-c)
    for m in range(c, 33):
        J = Fraction(m, 2 ** (c - 1)) # m*2^(1-c)
        min_mass_per_eta = 1 / maxP
        paid_per_eta = min_mass_per_eta * J
        assert paid_per_eta == Fraction(m, 2)
        assert paid_per_eta >= Fraction(c, 2)
        if c > 2:
            assert maxP < 1
        codim_cases += 1

# 2) Exhaustive affine-gauge invariance of physical q-flip signs in n=3.
n = 3
N = 1 << n
truth_tables = 0
affine_tests = 0
qflip_tests = 0
for mask in range(1 << N):
    vals = [1 if ((mask >> x) & 1) == 0 else -1 for x in range(N)]
    truth_tables += 1
    # Verify the q-flip sign equals the disagreement of two i-edge orientations.
    for a in range(N):
        for i in range(n):
            for w in range(1, N):
                if (w >> i) & 1:
                    continue
                if qflip_sign(vals, a, i, w) == -1:
                    active = tau(vals, a, i) != tau(vals, a ^ w, i)
                else:
                    active = tau(vals, a, i) != tau(vals, a ^ w, i)
                assert (qflip_sign(vals, a, i, w) == -1) == active
                qflip_tests += 1
    # All affine characters.
    for ell in range(1 << n):
        for b in (0,1):
            vals2 = [vals[x] * chi(n, ell, b, x) for x in range(N)]
            for a in range(N):
                for i in range(n):
                    # physical edge orientation changes by coordinate-constant sign
                    ratio = tau(vals2, a, i) * tau(vals, a, i)
                    assert ratio == (-1 if ((ell >> i) & 1) else 1)
                    for w in range(1, N):
                        if (w >> i) & 1:
                            continue
                        assert qflip_sign(vals2, a, i, w) == qflip_sign(vals, a, i, w)
                        assert (tau(vals2, a, i) != tau(vals2, a ^ w, i)) == (
                            tau(vals, a, i) != tau(vals, a ^ w, i)
                        )
                        affine_tests += 1

out = {
    "status": "PASS",
    "codimension_exact_cases": codim_cases,
    "truth_tables_n3": truth_tables,
    "qflip_identity_tests": qflip_tests,
    "affine_gauge_qflip_tests": affine_tests,
    "max_checked_codimension": 32,
    "claims_checked": [
        "P_max=2^(2-c) forces positive lift mass >=2^(c-2)*eta",
        "minimal mask-payment lower bound is (m_L/2)*eta >= (c/2)*eta",
        "mass-preserving direct positive lift is impossible for c>2 and eta>0",
        "q-flip relation sign equals physical two-edge orientation disagreement",
        "all q-flip relation signs and active indicators are invariant under affine-character gauge"
    ]
}
print(json.dumps(out, sort_keys=True, indent=2))
