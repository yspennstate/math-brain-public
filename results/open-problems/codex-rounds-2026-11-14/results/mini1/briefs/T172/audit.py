#!/usr/bin/env python3
"""Small arithmetic and pathwise audits for PROOF.md; standard library only."""

import json
import math
import os
import random
import resource
from collections import deque
from decimal import Decimal as D, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction as F
from pathlib import Path


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def exact_audit():
    c, k = 108, 144
    require(F(c * c, 243) == 48, "Chernoff coefficient")
    require(F(109, 1296) < F(1, 10), "remainder contraction")
    require(F(1296, 109) > 8, "intermediate degree ratio")
    require(F(4, k) + F(1, k * k) < F(1, 2), "service slack")
    # Positive terms of the exponential series prove the two log bounds.
    e5_lower = sum((F(5**j, math.factorial(j)) for j in range(16)), F(0))
    e6_lower = sum((F(6**j, math.factorial(j)) for j in range(16)), F(0))
    require(e5_lower > 129, "log(129)<5")
    require(e6_lower > 288, "log(288)<6")
    require(6 * 2**64 > 16 * 109, "first-level degree ratio")
    identities = 0
    for depth in range(2, 25):
        alpha = F(2**depth, 2**depth - 1)
        beta = [F(0)] + [2 * alpha * (1 - F(1, 2**j))
                             for j in range(1, depth + 1)]
        require(beta[-1] == 2, "last block exponent")
        for j in range(2, depth + 1):
            require(alpha / 2**(j - 1) + beta[j - 1] / 2 == alpha,
                    "balanced exponent")
            identities += 1
    # Derive this coefficient independently by adding the four contributions.
    coefficient = 1 + 5 * (2 * (c + 1)) + 1 + 1
    require(coefficient == 1093, "master-bound coefficient")
    require(1100 * 288 * 3 == 950400 < 10**6, "final coefficient")
    return {"balanced_exponent_identities": identities,
            "master_coefficient": coefficient, "rounded_final_constant": 950400,
            "exp5_positive_series_lower": str(e5_lower),
            "exp6_positive_series_lower": str(e6_lower)}


def rounded_parameter_audit():
    rows = []
    with localcontext() as ctx:
        ctx.prec = 1450
        ln2 = D(2).ln()
        for r in (185, 186, 190, 255, 256, 257, 511, 512, 513, 1023, 1024):
            for n in (2, 3, 17, 10**6):
                eps = D(2) ** -r
                rho = 1 - eps
                ell = D(r) * ln2
                h = (D(144) * n / eps).ln()
                depth = int(((1 + ell).ln() / ln2).to_integral_value(
                    rounding=ROUND_CEILING))
                alpha = D(2**depth) / (2**depth - 1)
                cap = D(288**depth)
                require(ell >= 128, "cutoff")
                require(D(2**depth - 1) >= ell, "depth ceiling upper")
                require(D(2**(depth - 1) - 1) < ell, "depth ceiling lower")
                require(cap <= 1 / eps.sqrt(), "D uniform envelope")
                require(cap <= 288 * (1 + ell)**9, "D polynomial envelope")
                require(eps ** (-alpha) <= ell.exp() * D(1).exp()
                        * (1 + D('1e-1000')), "exponent cost")
                lengths, times = [], []
                total = 1
                for j in range(1, depth + 1):
                    raw = D(144) * ((alpha / 2**(j - 1)) * ell).exp()
                    if j == 1:
                        raw *= h
                    length = int(raw.to_integral_value(rounding=ROUND_CEILING))
                    total *= length
                    lengths.append(length)
                    times.append(total)
                services, remainders, exact_remainders = [], [], []
                rho_fraction = F(2**r - 1, 2**r)
                for j in range(depth - 1):
                    mean = rho * times[0] if j == 0 else lengths[j] * remainders[j-1]
                    margin = D(108) * (D(times[j]) * h).sqrt()
                    service = int((mean - margin).to_integral_value(rounding=ROUND_FLOOR))
                    exact_mean = rho_fraction * times[0] if j == 0 else lengths[j] * exact_remainders[j-1]
                    exact_remainder = exact_mean - service
                    remainder = D(exact_remainder.numerator) / exact_remainder.denominator
                    require(margin <= remainder < margin + 1, "rounded remainder")
                    require(service > 0, "positive service")
                    services.append(service)
                    remainders.append(remainder)
                    exact_remainders.append(exact_remainder)
                # Check slot identities with rational arithmetic, independently
                # of the decimal means and the telescoping formula.
                for j in range(depth - 1):
                    used = sum(times[j] // times[i] * services[i] for i in range(j+1))
                    require(F(used) == rho_fraction * times[j] - exact_remainders[j],
                            "exact telescoping")
                    require(used < times[j], "slot feasibility")
                top_service = times[-1] - sum(
                    times[-1] // times[i] * services[i] for i in range(depth-1))
                require(F(top_service) == F(1, 2**r) * times[-1]
                        + lengths[-1] * exact_remainders[-1], "integer final service")
                probs = [remainders[j] / (2 * rho * times[j])
                         for j in range(depth - 2)]
                require(sum(probs, D(0)) < 1, "initial labels")
                min_degree_ratio, min_mu_h = D('Infinity'), D('Infinity')
                max_failure_ratio = D(0)
                for j in range(depth - 1):
                    aj = remainders[j]
                    tj = D(times[j])
                    mj = tj / 2 * sum((remainders[q] / times[q]
                                       for q in range(j, depth - 2)), D(0))
                    dj = rho * tj if j == 0 else lengths[j] * remainders[j-1]
                    mu, nu = dj - mj, rho * tj - mj
                    require(mj <= 5 * aj / 9, "deferred mean")
                    require(mu >= 24 * aj / 9, "factor degree-to-margin")
                    require(mu - aj / 3 >= services[j], "factor service target")
                    require(mu >= 4608 * h, "factor concentration")
                    require(aj / 9 <= nu <= tj, "binomial deviation range")
                    min_degree_ratio = min(min_degree_ratio, dj / aj)
                    min_mu_h = min(min_mu_h, mu / h)
                    block_count = sum(times[j] // times[i] for i in range(j+1))
                    ratio = tj * block_count * (-40 * h).exp() / aj
                    require(ratio <= 1, "residual failure contribution")
                    max_failure_ratio = max(max_failure_ratio, ratio)
                top_t = D(times[-1])
                lower_count = sum(times[-2] // times[i] for i in range(depth-1))
                top_failure = top_t * lower_count * (-40 * h).exp() / h
                require(top_failure <= 1, "top failure contribution")
                moment_coefficient = 9 + 4 * cap * eps / D(144)**3
                require(moment_coefficient <= 16, "port fluctuation")
                require(4 * (top_t * h).sqrt() + h <= eps * top_t / 2,
                        "negative matching-queue drift")
                products = [D(lengths[j]) * remainders[j-1]
                            for j in range(1, depth)]
                master = (2 * times[0] + 4 * sum(products[:-1], D(0))
                          + 5 * products[-1] + 34 * h / eps + eps * top_t)
                master_ratio = master / (cap * h * (alpha * ell).exp())
                final_ratio = master / (D(10**6) * h / eps * (1 + ell)**9)
                require(master_ratio <= 1093, "master finite bound")
                require(final_ratio <= 1, "displayed theorem bound")
                rows.append({"n": n, "epsilon": f"2^-{r}", "k": depth,
                             "min_d_over_a": f"{min_degree_ratio:.8E}",
                             "min_mu_over_h": f"{min_mu_h:.8E}",
                             "max_EF_over_a_bound": f"{max_failure_ratio:.8E}",
                             "top_EF_over_h_bound": f"{top_failure:.8E}",
                             "master_over_D_h_eps_power": f"{master_ratio:.8E}",
                             "master_over_theorem_bound": f"{final_ratio:.8E}"})
    return rows


def choose_perfect(ids, packets):
    by_edge = {(i, j): [] for i in range(2) for j in range(2)}
    for pid in sorted(ids):
        by_edge[packets[pid][1]].append(pid)
    for perm in ((0, 1), (1, 0)):
        if all(by_edge[(i, perm[i])] for i in range(2)):
            return [by_edge[(i, perm[i])][0] for i in range(2)]
    return []


def decompose(ids, packets):
    cells = {(i, j): [] for i in range(2) for j in range(2)}
    for pid in sorted(ids):
        cells[packets[pid][1]].append(pid)
    degree = max([sum(len(cells[(i,j)]) for j in range(2)) for i in range(2)]
                 + [sum(len(cells[(i,j)]) for i in range(2)) for j in range(2)])
    # Add anonymous edges to make a regular graph, then remove perfect matchings.
    for i in range(2):
        for j in range(2):
            row_deficit = degree - sum(len(cells[(i,q)]) for q in range(2))
            col_deficit = degree - sum(len(cells[(q,j)]) for q in range(2))
            cells[(i,j)].extend([None] * min(row_deficit, col_deficit))
    output = []
    for _ in range(degree):
        perm = next(p for p in ((0,1),(1,0)) if all(cells[(i,p[i])] for i in range(2)))
        matching = [cells[(i,perm[i])].pop(0) for i in range(2)]
        output.append([pid for pid in matching if pid is not None])
    require(sum(map(len, output)) == len(ids), "edge decomposition")
    return output


def pathwise_audit(depth, seed, top_blocks=32):
    rng = random.Random(seed)
    times = [3 * 2**j for j in range(depth)]
    rho = F(3,4)
    a = [rho * times[0] - 1]
    for _ in range(1, depth-1):
        a.append(2 * a[-1] - 1)
    probabilities = [a[j] / (2 * rho * times[j]) for j in range(depth-2)]
    denominator = math.lcm(*(p.denominator for p in probabilities)) if probabilities else 1
    label_limits, cumulative = [], 0
    for p in probabilities:
        cumulative += int(p * denominator)
        label_limits.append(cumulative)
    packets = []  # (birth slot, edge, initial level)
    alive = {}    # packet id -> current level
    fifo = deque()
    failures = {}
    identities, batches, premature = 0, 0, 0
    served = set()
    schedule = [depth] * times[-1]
    assigned = set()
    for level in range(1, depth):
        for start in range(0, times[-1], times[level-1]):
            first = next(s for s in range(start, start + times[level-1])
                         if s not in assigned)
            schedule[first] = level
            assigned.add(first)
    first_top_offset = schedule.index(depth)

    def original_ids(level, block):
        lo, hi = block * times[level-1], (block+1) * times[level-1]
        return {pid for pid, packet in enumerate(packets) if lo <= packet[0] < hi}

    def offline_residual(block):
        remaining = original_ids(depth, block)
        for level in range(1, depth):
            first = block * times[-1] // times[level-1]
            for b in range(first, first + times[-1] // times[level-1]):
                eligible = {pid for pid in remaining if packets[pid][0] // times[level-1] == b
                            and packets[pid][2] <= level}
                remaining.difference_update(choose_perfect(eligible, packets))
        return remaining

    for t in range((top_blocks + 2) * times[-1]):
        slot_level = schedule[t % times[-1]]

        if slot_level < depth:
            level = slot_level
            block = t // times[level-1] - 1
            if block >= 0:
                original = original_ids(level, block)
                premature += sum(1 for pid in original if pid in alive and alive[pid] < level)
                require(not any(pid in alive and alive[pid] < level for pid in original),
                        "parent started before lower promotions")
                eligible = {pid for pid in original if alive.get(pid) == level}
                matching = choose_perfect(eligible, packets)
                failed = int(not matching)
                for pid in matching:
                    del alive[pid]
                    served.add(pid)
                for pid in eligible.difference(matching):
                    alive[pid] = level + 1
                misses = failed
                if level > 1:
                    first_child = block * 2
                    misses += sum(failures[(level-1, b)]
                                  for b in range(first_child, first_child+2))
                failures[(level, block)] = misses
                prescribed = sum(times[level-1] // times[q-1] for q in range(1, level+1))
                remaining = original.intersection(alive)
                for side in (0,1):
                    for port in range(2):
                        arrivals = sum(packets[pid][1][side] == port for pid in original)
                        residual = sum(packets[pid][1][side] == port for pid in remaining)
                        require(residual == arrivals - prescribed + misses,
                                "pathwise residual identity")
                        identities += 1
        else:
            first_top_slot = t % times[-1] == first_top_offset
            if first_top_slot:
                block = t // times[-1] - 1
                if block >= 0:
                    original = original_ids(depth, block)
                    require(not any(pid in alive and alive[pid] < depth for pid in original),
                            "top insertion before lower promotions")
                    online_residual = original.intersection(alive)
                    offline = offline_residual(block)
                    require(online_residual == offline, "disjoint original-data construction")
                    fifo.extend(decompose(online_residual, packets))
                    batches += 1
            if fifo:
                for pid in fifo.popleft():
                    require(alive[pid] == depth, "final service eligibility")
                    del alive[pid]
                    served.add(pid)

        if t < top_blocks * times[-1]:
            for i in range(2):
                for j in range(2):
                    if rng.randrange(8) < 3:
                        draw = rng.randrange(denominator)
                        initial = 1
                        for q, limit in enumerate(label_limits):
                            if draw < limit:
                                initial = q + 2
                                break
                        pid = len(packets)
                        packets.append((t, (i,j), initial))
                        alive[pid] = initial
    require(len(served) + len(alive) == len(packets), "packet conservation")
    return {"k": depth, "seed": seed, "original_top_blocks": top_blocks,
            "packets": len(packets), "residual_port_identities": identities,
            "online_offline_batch_comparisons": batches,
            "premature_parent_packets": premature, "packets_remaining": len(alive)}


def main():
    require(os.environ.get("OMP_NUM_THREADS") == "1", "one-thread environment")
    # The tool environment inherits nice 20; invoking nice -n 15 cannot lower
    # its priority further on this sandbox. Check the actual inherited value.
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    require(priority >= 15, "background process priority")
    resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
    arithmetic = exact_audit()
    parameters = rounded_parameter_audit()
    pathwise = [pathwise_audit(depth, seed) for depth in (2,3,4)
                for seed in (172, 2026, 37521)]
    result = {"scope": "verification of PROOF.md, not a simulation at its tiny epsilon",
              "OMP_NUM_THREADS": "1", "effective_nice": priority,
              "decimal_precision": 1450, "exact_arithmetic": arithmetic,
              "parameter_cases": parameters, "pathwise_cases": pathwise,
              "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    Path("AUDIT_DATA.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS exact arithmetic: {arithmetic['balanced_exponent_identities']} exponent identities; final coefficient 950400 < 1000000")
    print(f"PASS rounded parameters: {len(parameters)} cases, n=2..1000000, epsilon=2^-185..2^-1024")
    print(f"PASS pathwise timing: {sum(p['residual_port_identities'] for p in pathwise)} port identities; {sum(p['online_offline_batch_comparisons'] for p in pathwise)} online/offline batch comparisons")
    print(f"PASS resources: OMP_NUM_THREADS=1, effective nice={priority}, peak RSS={result['peak_rss_bytes']} bytes")
    print("Wrote AUDIT_DATA.json")


if __name__ == "__main__":
    main()
