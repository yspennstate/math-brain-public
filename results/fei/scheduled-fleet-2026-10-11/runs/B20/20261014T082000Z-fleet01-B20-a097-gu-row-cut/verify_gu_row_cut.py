#!/usr/bin/env python3
import math

LN2 = math.log(2.0)
C0 = 2.0 / LN2


def fwht(values):
    v = list(map(float, values))
    n = len(v)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = v[j], v[j + h]
                v[j], v[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in v]


def h2(q):
    if q <= 0.0 or q >= 1.0:
        return 0.0
    return -q * math.log2(q) - (1.0 - q) * math.log2(1.0 - q)


def dbern(q, r):
    ans = 0.0
    if q > 0.0:
        ans += q * math.log2(q / r)
    if q < 1.0:
        ans += (1.0 - q) * math.log2((1.0 - q) / (1.0 - r))
    return ans


def analyze(values):
    size = len(values)
    n = size.bit_length() - 1
    hat = fwht(values)
    p = [z * z for z in hat]
    pi = p[:]
    for bit in range(n):
        for a in range(size):
            if not ((a >> bit) & 1):
                pi[a] += pi[a | (1 << bit)]
    U = sum(p[a] * math.log2(pi[a] / p[a]) for a in range(size) if p[a] > 1e-300)
    I = sum(a.bit_count() * p[a] for a in range(size))
    W2 = sum(p[a] for a in range(size) if a.bit_count() == 2)
    M1 = sum(min(p[0], p[1 << i]) for i in range(n))
    K0 = K1 = Kge2 = BG = V1 = 0.0
    for i in range(n):
        ib = 1 << i
        for a_set in range(size):
            if a_set & ib:
                continue
            a, b = hat[a_set], hat[a_set | ib]
            m = a * a + b * b
            if m < 1e-300:
                continue
            M = pi[a_set]
            C = 0.0
            free = ((size - 1) ^ a_set ^ ib) & (size - 1)
            sub = free
            while True:
                t = a_set | sub
                C += hat[t] * hat[t | ib]
                if sub == 0:
                    break
                sub = (sub - 1) & free
            alpha = max(-1.0, min(1.0, 2.0 * a * b / m))
            beta = max(-1.0, min(1.0, 2.0 * C / M))
            K = m * dbern((1.0 + alpha) / 2.0, (1.0 + beta) / 2.0)
            s = b * b / m
            B = m * h2(s)
            Nup = pi[a_set | ib]
            Gamma = b * b * math.log2(M / Nup) if b * b > 1e-300 else 0.0
            BG += B - Gamma
            degree = a_set.bit_count()
            if degree == 0:
                K0 += K
            elif degree == 1:
                K1 += K
                V1 += m * math.log2(M / m)
            else:
                Kge2 += K
    G = BG + K0 + K1 + Kge2
    return {
        "U": U,
        "I": I,
        "G": G,
        "BG": BG,
        "K0": K0,
        "K1": K1,
        "Kge2": Kge2,
        "V1": V1,
        "W2": W2,
        "M1": M1,
    }


cases = 0
assertions = 0
min_singleton_slack = float("inf")
min_assembled_slack = float("inf")
max_v1_over_u = (-1.0, None)
for n in range(1, 5):
    size = 1 << n
    for mask in range(1 << (size - 1)):
        values = [1.0] + [1.0 if (mask >> (x - 1)) & 1 else -1.0 for x in range(1, size)]
        r = analyze(values)
        cases += 1
        singleton_slack = 0.5 * r["V1"] + C0 * r["W2"] - r["K1"]
        assembled_slack = r["BG"] + r["Kge2"] + 0.5 * r["V1"] + C0 * r["I"] - r["G"]
        min_singleton_slack = min(min_singleton_slack, singleton_slack)
        min_assembled_slack = min(min_assembled_slack, assembled_slack)
        assertions += 3
        assert singleton_slack > -2e-10
        assert assembled_slack > -2e-10
        assert r["K0"] <= C0 * r["M1"] + 2e-10
        if r["U"] > 1e-12 and r["V1"] / r["U"] > max_v1_over_u[0]:
            max_v1_over_u = (r["V1"] / r["U"], (n, mask, r))

n, mask, witness = max_v1_over_u[1]
assert max_v1_over_u[0] > 2.0
print("claim=B20-A097-GU-ROW-CUT-v1")
print("verdict=PASS_REDUCTION_AND_PRECISE_FAILED_TRANSFER")
print("exhaustive_boolean_signs_mod_output", cases)
print("assertions", assertions)
print("min_singleton_bound_slack", format(min_singleton_slack, ".12e"))
print("min_assembled_reduction_slack", format(min_assembled_slack, ".12e"))
print("false_transfer=V1_over_2_le_U")
print("counterexample_n", n)
print("counterexample_mask", mask)
print("counterexample_V1", format(witness["V1"], ".12e"))
print("counterexample_U", format(witness["U"], ".12e"))
print("counterexample_V1_over_U", format(max_v1_over_u[0], ".12e"))
print("unpaid=D_ge_2_plus_V1_over_2")
print("universal_GU=OPEN")
