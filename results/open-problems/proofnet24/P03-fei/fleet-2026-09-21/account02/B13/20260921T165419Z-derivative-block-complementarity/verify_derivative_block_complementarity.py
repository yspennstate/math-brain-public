#!/usr/bin/env python3
"""Exact finite checks for B13 derivative block complementarity.

Global output negation is quotiented by fixing f(0)=+1.  All inequalities
checked below are exact integer/rational statements; no floating arithmetic is
used in the exhaustive part.
"""
from itertools import combinations
import json, time

def insert_bit(y, i, b):
    lo = y & ((1 << i) - 1)
    hi = y >> i
    return lo | (b << i) | (hi << (i + 1))

def compress_bits(x, positions):
    z = 0
    for k, p in enumerate(positions):
        if (x >> p) & 1:
            z |= 1 << k
    return z

def derivative_vector(f, n, i):
    m = n - 1
    return [(f[insert_bit(y, i, 0)] - f[insert_bit(y, i, 1)]) // 2
            for y in range(1 << m)]

def block_stats(g, m, J):
    q = len(J)
    K = 1 << q
    Jset = set(J)
    C = tuple(p for p in range(m) if p not in Jset)
    W = 1 << len(C)
    slices = [[0] * W for _ in range(K)]
    M = 0
    for y, val in enumerate(g):
        if val:
            M += 1
        z = compress_bits(y, J)
        w = compress_bits(y, C)
        slices[z][w] = val
    assert M > 0

    norms = [sum(v * v for v in row) for row in slices]
    cx_num = sum(a * a for a in norms)       # C_phys = cx_num / M^2

    tr_num = 0                               # tr(rho_J^2) = tr_num / M^2
    for z in range(K):
        for zp in range(K):
            dot = sum(slices[z][w] * slices[zp][w] for w in range(W))
            tr_num += dot * dot

    B = []
    for D in range(K):
        val = 0
        for w in range(W):
            s = 0
            for z in range(K):
                sign = -1 if ((D & z).bit_count() & 1) else 1
                s += sign * slices[z][w]
            val += s * s
        B.append(val)
    assert sum(B) == M * K
    cy_num = sum(b * b for b in B)           # C_spec = cy_num / (M^2 K^2)

    # R = tr rho^2 + 1/K - C_phys - C_spec.
    # Common denominator M^2 K^2:
    r_num = tr_num * K * K + M * M * K - cx_num * K * K - cy_num
    e_num = M * M - tr_num                   # E_lin = e_num/M^2
    return M, K, cx_num, tr_num, cy_num, r_num, e_num, slices

def exhaustive(max_n=4):
    total_funcs = total_rows = total_blocks = total_singletons = 0
    r_zero = r_strict = final_equal = 0
    by_n = {}
    started = time.time()

    for n in range(1, max_n + 1):
        N = 1 << n
        nf = nr = nb = ns = 0
        # quotient global sign by fixing f(0)=+1
        for mask in range(1 << (N - 1)):
            f = [1] + [1 if ((mask >> (x - 1)) & 1) == 0 else -1
                       for x in range(1, N)]
            nf += 1
            for i in range(n):
                g = derivative_vector(f, n, i)
                if not any(g):
                    continue
                nr += 1
                m = n - 1
                for q in range(1, m + 1):
                    for J in combinations(range(m), q):
                        M, K, cx, tr, cy, r, e, slices = block_stats(g, m, J)
                        nb += 1
                        assert tr <= M * M
                        assert r >= 0
                        # C_phys + C_spec + E_lin + R = 1 + 1/K.
                        final_slack = M*M*K*K + M*M*K - cx*K*K - cy
                        assert final_slack == e*K*K + r
                        assert final_slack >= 0
                        if r == 0:
                            r_zero += 1
                        else:
                            r_strict += 1
                        if final_slack == 0:
                            final_equal += 1

                        if q == 1:
                            ns += 1
                            a = sum(v*v for v in slices[0])
                            b = sum(v*v for v in slices[1])
                            c = sum(slices[0][w] * slices[1][w]
                                    for w in range(len(slices[0])))
                            # Exact singleton form:
                            # (2c/M)^2 + ((a-b)/M)^2 <= 1.
                            assert 4*c*c + (a-b)*(a-b) <= (a+b)*(a+b)

        total_funcs += nf
        total_rows += nr
        total_blocks += nb
        total_singletons += ns
        by_n[str(n)] = {
            "functions_global_sign_fixed": nf,
            "nonzero_derivative_rows": nr,
            "block_checks": nb,
            "singleton_checks": ns,
        }

    return {
        "status": "PASS",
        "scope": "all Boolean functions n<=4 modulo global output negation",
        "functions_global_sign_fixed": total_funcs,
        "nonzero_derivative_rows": total_rows,
        "block_checks": total_blocks,
        "singleton_checks": total_singletons,
        "R_zero_checks": r_zero,
        "R_strict_checks": r_strict,
        "final_collision_equality_checks": final_equal,
        "by_n": by_n,
        "elapsed_seconds": round(time.time() - started, 6),
    }

def bent_values(d):
    assert d % 2 == 0
    out = []
    for z in range(1 << d):
        phase = 0
        for a in range(0, d, 2):
            phase ^= ((z >> a) & 1) & ((z >> (a + 1)) & 1)
        out.append(-1 if phase else 1)
    return out

def gated_row(k=3, d=4):
    g0 = bent_values(d)
    m = k + d
    row = []
    for x in range(1 << m):
        y = x & ((1 << k) - 1)
        z = x >> k
        row.append(g0[z] if y == 0 else 0)
    return row, m

def as_ratio(num, den):
    g = __import__("math").gcd(num, den)
    return f"{num//g}/{den//g}"

def gated_examples():
    row, m = gated_row()
    ans = {}
    blocks = {
        "controls": tuple(range(3)),
        "residual_bent_block": tuple(range(3, 7)),
        "all": tuple(range(7)),
    }
    for name, J in blocks.items():
        M, K, cx, tr, cy, r, e, _ = block_stats(row, m, J)
        ans[name] = {
            "q": len(J),
            "C_phys": as_ratio(cx, M*M),
            "C_spec": as_ratio(cy, M*M*K*K),
            "purity": as_ratio(tr, M*M),
            "E_lin": as_ratio(e, M*M),
            "R_mix": as_ratio(r, M*M*K*K),
            "rhs_1_plus_2^-q": as_ratio(K+1, K),
        }
    return ans

if __name__ == "__main__":
    result = exhaustive(4)
    result["gated_point_control_bent_residual"] = gated_examples()
    print(json.dumps(result, indent=2, sort_keys=True))
