#!/usr/bin/env python3
"""Sanity checks for B13 block-parity Booleanity and KL modal tax.

This is finite engineering evidence only; the report contains the analytic proofs.
Global sign is quotiented by fixing f(0)=-1.
"""
import json
import math
import time


def fwht_normalized(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for base in range(0, n, 2*h):
            for j in range(h):
                x = a[base+j]
                y = a[base+h+j]
                a[base+j] = x + y
                a[base+h+j] = x - y
        h *= 2
    return [x/n for x in a]


def binary_kl_bits(x, y):
    eps = 1e-15
    if y <= eps:
        return 0.0 if x <= eps else float("inf")
    if y >= 1-eps:
        return 0.0 if x >= 1-eps else float("inf")
    out = 0.0
    if x > eps:
        out += x * math.log2(x/y)
    if x < 1-eps:
        out += (1-x) * math.log2((1-x)/(1-y))
    return out


def modal_gamma_bits(alpha, m_plus, m_minus):
    """Closed-form conditional KL lower bound from max P+ + max P- <= 1."""
    if m_plus + m_minus <= 1 + 1e-14:
        return 0.0
    if alpha <= 1e-14 or alpha >= 1-1e-14:
        return 0.0
    l1 = alpha*math.log(m_plus) + (1-alpha)*math.log(1-m_minus)
    l2 = alpha*math.log(1-m_plus) + (1-alpha)*math.log(m_minus)
    m = max(l1, l2)
    return -(m + math.log(math.exp(l1-m) + math.exp(l2-m))) / math.log(2.0)


def check_dimension(n):
    N = 1 << n
    reps = 1 << (N-1)
    min_cap_margin = float("inf")
    min_kl_margin = float("inf")
    nondegenerate_cap_blocks = 0
    block_instances = 0

    for code in range(reps):
        f = [-1.0] * N
        for x in range(1, N):
            f[x] = 1.0 if ((code >> (x-1)) & 1) else -1.0

        hat = fwht_normalized(f)
        mu = [z*z for z in hat]
        q = []
        for i in range(n):
            q.append(sum(mu[s] for s in range(N) if ((s >> i) & 1)))

        Q = []
        for s in range(N):
            z = 1.0
            for i in range(n):
                z *= q[i] if ((s >> i) & 1) else (1-q[i])
            Q.append(z)

        tc = 0.0
        for p, r in zip(mu, Q):
            if p > 1e-16:
                if r <= 0.0:
                    tc = float("inf")
                    break
                tc += p * math.log2(p/r)

        for J in range(1, N):
            block_instances += 1
            even = [s for s in range(N) if ((s & J).bit_count() % 2) == 0]
            odd = [s for s in range(N) if ((s & J).bit_count() % 2) == 1]
            alpha = sum(mu[s] for s in even)
            beta = sum(Q[s] for s in even)

            # Exact conditional cap consequence:
            # max(mu(.|even)) + max(mu(.|odd)) <= 1.
            if 1e-14 < alpha < 1-1e-14:
                p_plus = max(mu[s] for s in even) / alpha
                p_minus = max(mu[s] for s in odd) / (1-alpha)
                margin = 1.0 - p_plus - p_minus
                min_cap_margin = min(min_cap_margin, margin)
                nondegenerate_cap_blocks += 1
                if margin < -2e-12:
                    raise AssertionError(("cap", n, code, J, margin))

            # Modal KL lower bound.
            bound = binary_kl_bits(alpha, beta)
            if (1e-14 < alpha < 1-1e-14 and
                    1e-14 < beta < 1-1e-14):
                m_plus = max(Q[s] for s in even) / beta
                m_minus = max(Q[s] for s in odd) / (1-beta)
                bound += modal_gamma_bits(alpha, m_plus, m_minus)
            kl_margin = tc - bound
            min_kl_margin = min(min_kl_margin, kl_margin)
            if kl_margin < -3e-11:
                raise AssertionError(("kl", n, code, J, tc, bound, kl_margin))

    if min_cap_margin == float("inf"):
        min_cap_margin = None
    return {
        "n": n,
        "boolean_representatives_mod_global_sign": reps,
        "nonempty_block_instances": block_instances,
        "nondegenerate_cap_blocks": nondegenerate_cap_blocks,
        "minimum_cap_margin": min_cap_margin,
        "minimum_tc_minus_modal_block_bound_bits": min_kl_margin,
    }


def relaxed_product_obstruction(n=64, q=1/64):
    """Non-Boolean product profile showing one-block parity caps cannot close FEI."""
    h = -q*math.log2(q) - (1-q)*math.log2(1-q)
    W = (1-q)**n
    r = q/(1-q)
    rows = []
    for k in range(1, n+1):
        beta = (1 + (1-2*q)**k) / 2
        m_plus = W / beta
        m_minus = W * r / (1-beta)
        rows.append((k, beta, m_plus, m_minus, m_plus+m_minus))
    worst = max(rows, key=lambda x: x[-1])
    return {
        "n": n,
        "q": q,
        "total_influence_of_product_profile": n*q,
        "product_entropy_over_influence": h/q,
        "largest_over_block_sizes_of_mplus_plus_mminus": worst[-1],
        "attained_at_block_size": worst[0],
        "matched_product_empty_atom": W,
        "all_single_block_modal_taxes_zero": worst[-1] <= 1.0,
        "note": "This is a relaxed non-Boolean obstruction, not a Boolean counterexample.",
    }


def main():
    t0 = time.time()
    dimensions = [check_dimension(n) for n in range(1, 5)]
    out = {
        "schema": "b13-block-parity-kl-verification-v1",
        "dimensions": dimensions,
        "totals": {
            "boolean_representatives_mod_global_sign": sum(
                d["boolean_representatives_mod_global_sign"] for d in dimensions
            ),
            "nonempty_block_instances": sum(
                d["nonempty_block_instances"] for d in dimensions
            ),
            "nondegenerate_cap_blocks": sum(
                d["nondegenerate_cap_blocks"] for d in dimensions
            ),
        },
        "relaxed_product_obstruction": relaxed_product_obstruction(),
        "elapsed_seconds": time.time() - t0,
        "status": "PASS",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
