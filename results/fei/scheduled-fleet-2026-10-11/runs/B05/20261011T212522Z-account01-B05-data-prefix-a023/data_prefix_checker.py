#!/usr/bin/env python3
"""Deterministic checks for the B05 A023 one-coordinate-per-pair prefix.

The direct checks build genuine Boolean restrictions and normalized Walsh
spectra.  The aggregated checks use the exact closed form.  No randomness.
All logarithms are base 2.
"""

import math


def h2(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0 - t) * math.log2(1.0 - t)


def jphase(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return 1.0 - h2(0.5 + math.sqrt(t * (1.0 - t)))


def fwht(values):
    out = [float(x) for x in values]
    n = len(out)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                a, b = out[j], out[j + step]
                out[j], out[j + step] = a + b, a - b
        step *= 2
    return [x / n for x in out]


def restricted_children(k, m):
    """b_m,b'_m after u_1=...=u_m=0.

    Remaining bits are v_1,...,v_m followed by the intact (u,v) pairs.
    """
    h = k // 2
    n = k - m
    b = []
    for x in range(1 << n):
        exponent = 0
        offset = m
        for j in range(h - m):
            u = (x >> (offset + 2 * j)) & 1
            v = (x >> (offset + 2 * j + 1)) & 1
            exponent ^= u & v
        b.append(-1.0 if exponent else 1.0)
    bp = b[:]
    bp[0] *= -1.0
    return b, bp


def packet(children, phase=False):
    uhat, vhat = map(fwht, children)
    total = 0.0
    for u, v in zip(uhat, vhat):
        a = 0.5 * (u + v)
        d = 0.5 * (u - v)
        q = a * a + d * d
        if q == 0.0:
            continue
        theta = d * d / q
        total += q * (jphase(theta) if phase else h2(theta))
    return total


def closed(k, m, phase=False):
    rho = 2.0 ** (-k / 2)
    delta = rho * rho
    c = (2.0 ** m) * rho
    vals = []
    for sign in (1.0, -1.0):
        qbar = (sign - rho) ** 2 + rho * rho
        theta = rho * rho / qbar
        vals.append(qbar * (jphase(theta) if phase else h2(theta)))
    A = 0.5 * (vals[0] + vals[1])
    B = 0.5 * (vals[0] - vals[1])
    return A - 2.0 * delta + c * (B + 2.0 * rho), A, B


def check_k(k):
    h = k // 2
    delta = 2.0 ** (-k)
    eps = math.sqrt(delta)
    direct_L = []
    direct_Q = []
    for m in range(h + 1):
        ch = restricted_children(k, m)
        L = packet(ch, False)
        Q = packet(ch, True)
        direct_L.append(L)
        direct_Q.append(Q)
        assert abs(L - closed(k, m, False)[0]) < 5e-12
        assert abs(Q - closed(k, m, True)[0]) < 5e-12
    _, AL, _ = closed(k, 0, False)
    gamma = 0.5 * (AL - 2.0 * delta)
    assert gamma >= -1e-13
    for m in range(h):
        assert abs((direct_L[m] - 0.5 * direct_L[m + 1]) - gamma) < 5e-12
    telescoped = sum((2.0 ** (-m)) * gamma for m in range(h)) + eps * direct_L[h]
    assert abs(telescoped - direct_L[0]) < 5e-12
    terminal_bound = 2.0 * delta + (delta ** 1.5) * (k + math.log2(math.e))
    assert eps * direct_L[h] <= terminal_bound + 1e-12
    # The source JS estimate gives eps*Q_h <= 2 delta/ln 2.
    assert eps * direct_Q[h] <= 2.0 * delta / math.log(2.0) + 1e-12
    return {
        "k": k,
        "delta": delta,
        "L0_over_delta": direct_L[0] / delta,
        "single_raw_credit_over_delta": gamma / delta,
        "credit_sum_over_delta": sum((2.0 ** (-m)) * gamma for m in range(h)) / delta,
        "terminal_expected_L_over_delta": eps * direct_L[h] / delta,
        "terminal_expected_Q_over_delta": eps * direct_Q[h] / delta,
        "terminal_bound_ratio": eps * direct_L[h] / terminal_bound,
    }


if __name__ == "__main__":
    print("DIRECT BOOLEAN/WALSH AND CLOSED-FORM CHECKS")
    assertions = 0
    for kval in (2, 4, 6, 8, 10, 12):
        print(check_k(kval))
        assertions += 6 * (kval // 2 + 1) + 5
    print("AGGREGATED LARGE-k CHECKS")
    for kval in (16, 20, 24, 32, 40, 60):
        h = kval // 2
        delta = 2.0 ** (-kval)
        eps = math.sqrt(delta)
        L0, A, _ = closed(kval, 0, False)
        Lh = closed(kval, h, False)[0]
        gamma = 0.5 * (A - 2.0 * delta)
        credit_sum = 2.0 * gamma * (1.0 - eps)
        assert gamma >= 0.0
        assert abs(L0 - credit_sum - eps * Lh) < 1e-12
        bound = 2.0 * delta + delta ** 1.5 * (kval + math.log2(math.e))
        assert eps * Lh <= bound
        print({
            "k": kval,
            "L0/delta": L0 / delta,
            "credit_sum/delta": credit_sum / delta,
            "terminal_L/delta": eps * Lh / delta,
            "terminal_bound_ratio": eps * Lh / bound,
        })
        assertions += 3
    print({"deterministic_assertion_lower_bound": assertions, "failures": 0, "randomness": "NONE"})
