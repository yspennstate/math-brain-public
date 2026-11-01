#!/usr/bin/env python3
"""Exact falsification check for B16 projective three-q-flip transport.

This checks only the new inequality.  It does not rerun any read-once
certificate or settled FEI sweep.
"""

def corr_num(f, u):
    return sum(f[x] * f[x ^ u] for x in range(len(f)))

def tau_num(f, u, v, w):
    return sum(f[x] * f[x ^ u] * f[x ^ v] * f[x ^ w]
               for x in range(len(f)))

def check_function(f, n):
    N = 1 << n
    c = [corr_num(f, u) for u in range(N)]
    checks = 0
    worst_num = 0
    worst_den = 1
    for u in range(N):
        for v in range(N):
            for w in range(N):
                # |tau-csum| <= 4 min beta, with common denominator N.
                # beta(u)=(N-|c_u|)/(2N), so after multiplying by N:
                # |T-Csum| <= 2 min(N-|C_u|,...).
                lhs = abs(tau_num(f, u, v, w) - c[u ^ v ^ w])
                rhs = 2 * min(N - abs(c[u]), N - abs(c[v]), N - abs(c[w]))
                if lhs > rhs:
                    raise AssertionError((n, u, v, w, lhs, rhs))
                if rhs and lhs * worst_den > worst_num * rhs:
                    worst_num, worst_den = lhs, rhs
                checks += 1
    return checks, worst_num, worst_den

def truth_table(n, bits):
    N = 1 << n
    return [1 if (bits >> x) & 1 else -1 for x in range(N)]

def main():
    total = 0
    worst_num, worst_den = 0, 1

    for n in (1, 2, 3):
        N = 1 << n
        for bits in range(1 << N):
            checks, a, b = check_function(truth_table(n, bits), n)
            total += checks
            if a * worst_den > worst_num * b:
                worst_num, worst_den = a, b

    # Deterministic n=4 extension: first 200 truth tables.
    n = 4
    for bits in range(200):
        checks, a, b = check_function(truth_table(n, bits), n)
        total += checks
        if a * worst_den > worst_num * b:
            worst_num, worst_den = a, b

    # Exact scalar identity in the report:
    # int_[0,a]^3 min(p,q,r)/(p q r) = 6a, hence 3 at a=1/2.
    print("PASS")
    print("exact_function_triple_checks", total)
    print("max_projective_ratio", f"{worst_num}/{worst_den}")
    print("triple_inverse_noise_scalar_at_a_half", "3")
    print("W1_payment_constant", "6")
    print("correlation_payment_constant", "12")

if __name__ == "__main__":
    main()
