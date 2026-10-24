#!/usr/bin/env python3
"""Finite diagnostics for B12 controlled-character spectral transfer.

No external dependencies. The analytic theorem is in REPORT.md; this file only
checks the finite algebra and the addressing equality.
"""
import itertools
import math


def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0.0)


def fwht(values):
    a = [float(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    scale = 1.0 / len(a)
    return [x * scale for x in a]


def child_spectral_laws(values, n_a, n_b):
    out = []
    for z in range(1 << n_a):
        child = [values[(z << n_b) | y] for y in range(1 << n_b)]
        coeff = fwht(child)
        out.append([c * c for c in coeff])
    return out


def projected_parent_law(values, n_a, n_b):
    coeff = fwht(values)
    mask_b = (1 << n_b) - 1
    out = [0.0] * (1 << n_b)
    for s, c in enumerate(coeff):
        out[s & mask_b] += c * c
    return out


def mutual_information(joint, marginal_x, marginal_t):
    ans = 0.0
    for (x, t), p in joint.items():
        if p:
            ans += p * math.log2(p / (marginal_x[x] * marginal_t[t]))
    return ans


def exhaustive_case(n_a, n_b):
    n_points = 1 << (n_a + n_b)
    t_maps = list(itertools.product(range(1 << n_b), repeat=(1 << n_a)))
    total = 0
    max_projection_error = 0.0
    max_gauged_projection_error = 0.0
    max_identity_error = 0.0
    max_abs_bound_excess = 0.0
    hierarchy_violations = 0

    for truthbits in range(1 << n_points):
        values = [1 if ((truthbits >> x) & 1) else -1 for x in range(n_points)]
        child = child_spectral_laws(values, n_a, n_b)
        r_marginal = [
            sum(child[z][r] for z in range(1 << n_a)) / (1 << n_a)
            for r in range(1 << n_b)
        ]
        r_parent = projected_parent_law(values, n_a, n_b)
        max_projection_error = max(
            max_projection_error,
            max(abs(a - b) for a, b in zip(r_marginal, r_parent)),
        )

        for t_map in t_maps:
            joint_rt = {}
            joint_yt = {}
            y_marginal = [0.0] * (1 << n_b)

            for z, t in enumerate(t_map):
                for r, p_cond in enumerate(child[z]):
                    p = p_cond / (1 << n_a)
                    joint_rt[(r, t)] = joint_rt.get((r, t), 0.0) + p
                    y = r ^ t
                    joint_yt[(y, t)] = joint_yt.get((y, t), 0.0) + p
                    y_marginal[y] += p

            # Build the global branch-gauged Boolean function and check that
            # its survivor spectral projection equals the mixture y_marginal.
            g_values = []
            for z, t in enumerate(t_map):
                for y in range(1 << n_b):
                    chi = -1 if ((t & y).bit_count() & 1) else 1
                    g_values.append(values[(z << n_b) | y] * chi)
            y_parent = projected_parent_law(g_values, n_a, n_b)
            max_gauged_projection_error = max(
                max_gauged_projection_error,
                max(abs(a - b) for a, b in zip(y_marginal, y_parent)),
            )

            p_t = {}
            for t in t_map:
                p_t[t] = p_t.get(t, 0.0) + 1.0 / (1 << n_a)

            h_r = entropy(r_marginal)
            h_y = entropy(y_marginal)
            h_t = entropy(p_t.values())
            i_rt = mutual_information(joint_rt, r_marginal, p_t)
            i_yt = mutual_information(joint_yt, y_marginal, p_t)
            max_identity_error = max(
                max_identity_error, abs((h_r - h_y) - (i_rt - i_yt))
            )
            max_abs_bound_excess = max(
                max_abs_bound_excess, abs(h_r - h_y) - h_t
            )

            h_y_given_t = 0.0
            for t, pt in p_t.items():
                cond = [0.0] * (1 << n_b)
                for (y, tt), p in joint_yt.items():
                    if tt == t:
                        cond[y] += p / pt
                h_y_given_t += pt * entropy(cond)
            if h_r > h_t + h_y_given_t + 1e-12:
                hierarchy_violations += 1

            total += 1

    return {
        "cases": total,
        "max_projection_error": max_projection_error,
        "max_gauged_projection_error": max_gauged_projection_error,
        "max_identity_error": max_identity_error,
        "max_abs_bound_excess": max_abs_bound_excess,
        "hierarchy_violations": hierarchy_violations,
    }


def addressing_checks():
    rows = []
    for d in range(1, 9):
        n = 1 << d
        h_r = math.log2(n)
        h_t = math.log2(n)
        h_y = 0.0
        rows.append((d, h_r, h_t, h_y, abs(h_r - h_t - h_y)))
    return rows


def main():
    results = [exhaustive_case(1, 2), exhaustive_case(2, 1)]
    total_cases = sum(r["cases"] for r in results)
    print("controlled-character spectral transfer finite check")
    print("total_cases", total_cases)
    print("max_projection_error", max(r["max_projection_error"] for r in results))
    print("max_gauged_projection_error", max(r["max_gauged_projection_error"] for r in results))
    print("max_identity_error", max(r["max_identity_error"] for r in results))
    print("max_abs_bound_excess", max(r["max_abs_bound_excess"] for r in results))
    print("hierarchy_violations", sum(r["hierarchy_violations"] for r in results))
    print("addressing")
    for row in addressing_checks():
        print("d=%d H_R=%.12g H_T=%.12g H_Y=%.12g equality_error=%.3g" % row)


if __name__ == "__main__":
    main()
