#!/usr/bin/env python3
"""Finite diagnostics for the B12 harmonic first-mark / mixed-prefix report.

Standard library only. Exhaustive Boolean functions through n=4; this is
supporting evidence and not a finite proof of any universal claim.
"""
import hashlib
import json
import math


def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def pc(x):
    return x.bit_count()


def ent_term(x):
    return 0.0 if x <= 0.0 else x * math.log2(1.0 / x)


C_HARM = (2.0 / math.log(2.0)) * (1.0 + 1.0 / (2.0 * math.e))
C_ROOT = C_HARM + 1.0 / math.log(2.0)
T_VALUES = (0.25, 0.5, 0.75)

functions = 0
mixed_prefixes = 0
moment_checks = 0
shadow_checks = 0
max_root_ratio = 0.0
root_witness = None
max_moment_excess = 0.0
max_shadow_excess = 0.0

for n in range(1, 5):
    N = 1 << n
    for truth in range(1 << N):
        vals = [1.0 if ((truth >> x) & 1) else -1.0 for x in range(N)]
        hat = fwht(vals)
        p = [c * c for c in hat]
        I = sum(pc(s) * p[s] for s in range(N))
        if I < 1e-13:
            continue
        functions += 1

        p0 = p[0]
        v = [0.0] * n
        for s in range(1, N):
            k = pc(s)
            if p[s] == 0.0:
                continue
            for i in range(n):
                if (s >> i) & 1:
                    v[i] += p[s] / k
        Hroot = ent_term(p0) + sum(ent_term(x) for x in v)
        ratio = Hroot / I
        if ratio > max_root_ratio:
            max_root_ratio = ratio
            root_witness = (n, truth, I, Hroot)
        if Hroot > C_ROOT * I + 1e-10:
            raise AssertionError(("root", n, truth, Hroot, I))

        for A in range(1, N):
            a = pc(A)
            coeff = {}
            w = 0.0
            for B in range(N):
                if (B & A) == A:
                    T = B ^ A
                    q = p[B]
                    if q:
                        coeff[T] = q
                    w += q
            if w < 1e-15:
                continue
            mixed_prefixes += 1
            theta = (4 ** (a - 1)) * w

            for t in T_VALUES:
                lhs = sum((t ** pc(T)) * q for T, q in coeff.items())
                rhs = w * (theta ** ((1.0 - t) / (1.0 + t)))
                excess = lhs - rhs
                max_moment_excess = max(max_moment_excess, excess)
                moment_checks += 1
                if excess > 2e-10:
                    raise AssertionError(("moment", n, truth, A, t, lhs, rhs))

            vA = 0.0
            for B in range(N):
                if (B & A) == A:
                    vA += p[B] / math.comb(pc(B), a)
            if theta < 1.0 - 1e-15:
                lam = math.log(1.0 / theta)
                factor = min(1.0, math.factorial(a) * (2.0 / lam) ** a)
                rhs = w * factor
                excess = vA - rhs
                max_shadow_excess = max(max_shadow_excess, excess)
                shadow_checks += 1
                if excess > 2e-10:
                    raise AssertionError(("shadow", n, truth, A, vA, rhs, theta))


def majority_coeffs(m):
    N = 1 << m
    vals = []
    for x in range(N):
        M = 1 if pc(x) > m // 2 else -1
        vals.append((1 + M) / 2)
    return fwht(vals)


majority_rows = []
for m in range(3, 16, 2):
    r = (m - 1) // 2
    hat = majority_coeffs(m)
    weights = [hat[S] ** 2 / (pc(S) + 1) for S in range(1 << m)]
    V = sum(weights)
    Jh = sum(pc(S) * weights[S] for S in range(1 << m))
    Hh = sum(w * math.log2(V / w) for w in weights if w > 0.0)
    lower = (1.0 / 16.0) * math.log2(2 * r)
    if Hh + 1e-12 < lower:
        raise AssertionError(("majority-lower", m, Hh, lower))
    if V + Jh > 1.0 + 1e-10:
        raise AssertionError(("majority-budget", m, V, Jh))
    majority_rows.append(
        {
            "m": m,
            "V": V,
            "Jh": Jh,
            "Hh": Hh,
            "ratio": Hh / (V + Jh),
            "analytic_lower": lower,
        }
    )

result = {
    "boolean_functions_nonconstant_n_le_4": functions,
    "mixed_prefixes_nonzero": mixed_prefixes,
    "hypercontractive_moment_checks": moment_checks,
    "sparse_shadow_checks": shadow_checks,
    "C_harm_mass": C_HARM,
    "C_root": C_ROOT,
    "max_root_entropy_over_I": max_root_ratio,
    "root_witness": {
        "n": root_witness[0],
        "truth": root_witness[1],
        "I": root_witness[2],
        "Hroot": root_witness[3],
    },
    "max_moment_excess": max_moment_excess,
    "max_shadow_excess": max_shadow_excess,
    "majority_rows": majority_rows,
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
result["result_digest_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
print(json.dumps(result, indent=2, sort_keys=True))
