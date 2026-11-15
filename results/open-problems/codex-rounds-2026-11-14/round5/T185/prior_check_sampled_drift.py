"""Exact arithmetic and cohort checks. Standard library; no random simulation.

Run from this folder with nice 15 and the single-thread environment in LOG.md.
All generated data are written beside this script.
"""

import json
import math
import os
import resource
import sys
import time
from fractions import Fraction as Q
from pathlib import Path


def lower_cpu_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    finite = [60] + [x for x in (soft, hard) if x != resource.RLIM_INFINITY]
    cap = min(finite)
    resource.setrlimit(resource.RLIMIT_CPU, (cap, hard))


def exponential_inverse_bounds(t, order=80):
    """Rational enclosures of exp(-t), using the positive exp(t) series."""
    term = Q(1)
    partial = term
    for k in range(1, order + 1):
        term *= t / k
        partial += term
    first_omitted = term * t / (order + 1)
    ratio = t / (order + 2)
    assert 0 <= ratio < 1
    remainder_bound = first_omitted / (1 - ratio)
    return 1 / (partial + remainder_bound), 1 / partial


def unnormalized_poisson_tail(t, first):
    """Upper bound on sum_{k >= first} t^k/k!, without exp(-t)."""
    assert first + 1 > t
    return t**first / math.factorial(first) / (1 - t / (first + 1))


def outward_decimal(interval, digits=12):
    scale = 10**digits
    lo, hi = interval
    lower = (lo * scale).numerator // (lo * scale).denominator
    h = hi * scale
    upper = -((-h.numerator) // h.denominator)

    def render(integer):
        sign = "-" if integer < 0 else ""
        integer = abs(integer)
        return f"{sign}{integer // scale}.{integer % scale:0{digits}d}"

    return [render(lower), render(upper)]


def check_poisson_limit():
    t = Q(4)
    exp_lo, exp_hi = exponential_inverse_bounds(t)
    # Condition on total arrivals: n fair +/-1 steps. Enumerate their law.
    partial = Q(0)
    previous_q = Q(0)
    order = 70
    for n in range(order + 1):
        qn = Q(sum(abs(2 * k - n) * math.comb(n, k)
                   for k in range(n + 1)), 2**n)
        if n:
            k = n - 1
            return_probability = (Q(math.comb(k, k // 2), 2**k)
                                  if k % 2 == 0 else Q(0))
            # Independently: E|S_{k+1}|-E|S_k| = P(S_k=0).
            assert qn - previous_q == return_probability
        previous_q = qn
        partial += t**n / math.factorial(n) * qn
    remainder = t * unnormalized_poisson_tail(t, order)
    abs_interval = (exp_lo * partial, exp_hi * (partial + remainder))
    first_interval = tuple(-Q(3, 10) * t + v / 2 for v in abs_interval)

    # Independent double sum of max(m,n), with separate Pois(2) counts.
    cutoff = 40
    lam = Q(2)
    terms = [lam**k / math.factorial(k) for k in range(cutoff + 1)]
    double_sum = sum((max(m, n) * terms[m] * terms[n]
                      for m in range(cutoff + 1)
                      for n in range(cutoff + 1)), Q(0))
    # Outside the square, max(X,Y) <= X+Y and a union bound applies.
    # Its expectation is <= 4*(sum_{k>=cutoff}2^k/k!
    #                           +sum_{k>=cutoff+1}2^k/k!), since exp(-2)<=1.
    double_tail = 4 * (unnormalized_poisson_tail(lam, cutoff)
                       + unnormalized_poisson_tail(lam, cutoff + 1))
    second_interval = (-Q(4, 5) * t + exp_lo * double_sum,
                       -Q(4, 5) * t + exp_hi * double_sum + double_tail)
    intersection = (max(first_interval[0], second_interval[0]),
                    min(first_interval[1], second_interval[1]))
    assert intersection[0] <= intersection[1] < -Q(1, 5)
    assert first_interval[1] - first_interval[0] < Q(1, 10**40)
    assert second_interval[1] - second_interval[0] < Q(1, 10**30)
    # Cauchy bound: -(3/10)*4 + sqrt(4)/2 = -1/5.
    assert -Q(3, 10) * 4 + Q(2, 2) == -Q(1, 5)
    return {
        "d_4_conditional_random_walk_interval": outward_decimal(first_interval),
        "d_4_independent_double_sum_interval": outward_decimal(second_interval),
        "absolute_difference_mean_interval": outward_decimal(abs_interval),
        "cauchy_upper_bound": "-1/5",
        "conditional_series_terms": order + 1,
        "double_sum_terms": (cutoff + 1)**2,
    }


def epsilon(n, t, a0=Q(1), amin=Q(1), b=Q(2)):
    return (b / (amin * n) + a0 / (amin * n**3)
            + t * (a0 / 5 + b) / (amin * n**4)
            + b * t**2 / (a0 * n))


def allocation(groups, weights):
    """Alpha=1 allocation, exact rational KKT computation."""
    counts = [sum(group[0] for group in route) for route in groups]
    n0, n1, n2 = counts
    assert n0 > 0
    h = weights[1] * n1 + weights[2] * n2
    x = weights[0] * n0 / (weights[0] * n0 + h)
    rates = [x, 1 - x if n1 else Q(0), 1 - x if n2 else Q(0)]
    assert x + rates[1] <= 1 and x + rates[2] <= 1
    if h:
        assert weights[0] * n0 / x == h / (1 - x)
    return counts, rates


def workload(groups):
    return [sum((count * remaining for count, remaining, _ in route), Q(0))
            for route in groups]


def maximum_link_workload(groups):
    w = workload(groups)
    return w[0] + max(w[1:])


def initial_groups(n, variant):
    k, r, eta = n**3, Q(1, n**4), Q(1, n**8)
    groups = [[[n, 1 - eta, True]], [], []]
    if variant in (1, 2):
        groups[variant] = [[k, r, True]]
    elif variant == 3:
        groups[1] = [[k // 2, r, True]]
        groups[2] = [[k - k // 2, r / 2, True]]
    elif variant == 4:
        groups[1] = [[k // 2, r, True], [k - k // 2, r / 2, True]]
    elif variant == 5:
        groups[0].append([k, r, True])
        groups[1] = [[k, r, True]]
    elif variant == 6:
        groups[0] = [[2 * n, Q(1, 2) - eta, True], [k, r, True]]
        groups[2] = [[1, Q(1, n), True]]
    return groups


def arrival_schedule(n, horizon, pattern):
    tiny = Q(1, n**6)
    if pattern == 0:
        return []
    if pattern == 1:
        return [(tiny, 1, 1), (2 * tiny, 2, 1), (3 * tiny, 1, 1),
                (horizon / 3, 0, 1), (horizon / 2, 2, 1),
                (2 * horizon / 3, 1, 1)]
    if pattern == 2:
        return [(tiny, 1, 4), (tiny, 2, 4), (tiny, 0, 2),
                (horizon / 2, 1, 2), (horizon / 2, 2, 2)]
    return [(horizon * k / 11, k % 3, 1) for k in range(1, 11)]


def check_path(n, horizon, weights, variant, pattern):
    """Compressed cohorts represent even N^3 originals without arrays."""
    assert horizon < n * (1 - Q(1, n**8))
    groups = initial_groups(n, variant)
    start_work = workload(groups)
    original_n0 = sum(g[0] for g in groups[0])
    start_m = maximum_link_workload(groups)
    m = max(start_work[1:])
    arrivals = sorted(arrival_schedule(n, horizon, pattern))
    totals = [sum(count for _, j, count in arrivals if j == route)
              for route in range(3)]
    a0, amin = weights[0], min(weights[1:])
    b = weights[1] + weights[2]
    l = totals[1] + totals[2]
    arrival_count_area = sum((count * (horizon - when)
                              for when, route, count in arrivals if route in (1, 2)), Q(0))
    d_bound = Q(1, n**4) * (a0 * (original_n0 + totals[0]) + b * (n**3 + l)) / amin
    t, lost, jump_sum = Q(0), Q(0), Q(0)
    original_local_service = Q(0)
    c = max(weights[1:])
    residual_count_bound = start_work[0] - horizon
    assert residual_count_bound > 0
    index, events = 0, 0
    cleared_at = Q(0) if variant == 0 else None
    while t < horizon:
        counts, rates = allocation(groups, weights)
        assert counts[0] >= n
        assert counts[0] >= residual_count_bound
        old_local_rate = sum((rates[j] * Q(sum(g[0] for g in groups[j] if g[2]), counts[j])
                              for j in (1, 2) if counts[j]), Q(0))
        new_local_counts = sum(g[0] for route in groups[1:] for g in route if not g[2])
        assert 1 - rates[0] - old_local_rate <= c * new_local_counts / (a0 * counts[0])
        next_t = min(horizon, arrivals[index][0] if index < len(arrivals) else horizon)
        for route in range(3):
            if counts[route]:
                per_file = rates[route] / counts[route]
                assert per_file > 0
                next_t = min(next_t, *(t + g[1] / per_file for g in groups[route]))
        dt = next_t - t
        assert dt >= 0
        lost += (1 - rates[0]) * dt
        original_local_service += old_local_rate * dt
        for route in range(3):
            if counts[route]:
                for g in groups[route]:
                    g[1] -= rates[route] * dt / counts[route]
                    assert g[1] >= 0
            groups[route] = [g for g in groups[route] if g[1] > 0]
        t = next_t
        if cleared_at is None and not any(g[2] for route in groups[1:] for g in route):
            cleared_at = t
        while index < len(arrivals) and arrivals[index][0] == t:
            _, route, count = arrivals[index]
            before = maximum_link_workload(groups)
            groups[route].append([count, Q(1), False])
            jump_sum += maximum_link_workload(groups) - before
            index += 1
        events += 1
        assert events < 100
    assert index == len(arrivals)
    end_work = workload(groups)
    delta = maximum_link_workload(groups) - start_m
    benchmark = totals[0] - horizon + max(totals[1:])
    # Independent checks: integrated loss, exact work balance, and unit
    # maximum-link draining between all arrivals.
    assert lost == end_work[0] - start_work[0] - totals[0] + horizon
    assert delta == -horizon + jump_sum
    assert -m <= delta - benchmark <= lost
    if variant != 6:
        assert lost <= d_bound + b * horizon * l / (a0 * n)
    assert original_local_service <= sum(start_work[1:])
    assert lost <= sum(start_work[1:]) + c * arrival_count_area / (a0 * residual_count_bound)
    if variant != 6 and d_bound < horizon:
        assert cleared_at is not None and cleared_at <= d_bound
    return events


def main():
    lower_cpu_limit()
    started = time.monotonic()
    assert all(os.environ.get(name) == "1" for name in
               ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"))
    # Recheck the obstruction by its independently averaged velocity.
    rho = (Q(1, 5), Q(1, 2), Q(1, 2))
    assert (rho[0] + rho[1], rho[0] + rho[2]) == (Q(7, 10), Q(7, 10))
    for g0 in (Q(1, 3), Q(1), Q(4)):
        for g1 in (Q(-10), Q(0), Q(7)):
            for g2 in (Q(-3), Q(0), Q(11)):
                input_gradient = sum(a * g for a, g in zip(rho, (g0, g1, g2)))
                d1, d2 = input_gradient - g1, input_gradient - g2
                assert (d1 + d2) / 2 == g0 / 5
                assert max(d1, d2) == g0 / 5 + abs(g1 - g2) / 2
    for n in (2, 8, 200):
        # Independent direct-jump generator of M at the earlier exact state.
        direct = rho[0] + rho[1] + rho[2] * (1 - Q(1, n)) - 1
        assert direct == Q(1, 5) - Q(1, 2 * n)

    poisson = check_poisson_limit()
    eps = epsilon(200, Q(4))
    bound = -Q(1, 5) + eps
    assert eps == Q(1700001305, 10**10)
    assert bound == Q(-299998695, 10**10) < -Q(29, 1000)
    wider_bound = -Q(1, 5) + Q(1, 100) + Q(8, 95)
    assert wider_bound == -Q(201, 1900)
    cases = events = 0
    for n in (8, 32, 200):
        for horizon in (Q(1), Q(4)):
            for weights in ((Q(1), Q(1), Q(1)), (Q(2), Q(3), Q(5)),
                            (Q(1), Q(1, 100), Q(100))):
                for variant in range(7):
                    for pattern in range(4):
                        events += check_path(n, horizon, weights, variant, pattern)
                        cases += 1
    rss_raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss_raw if sys.platform == "darwin" else 1024 * rss_raw
    assert rss_bytes < 1024**3
    result = {
        "status": "all exact checks passed",
        "earlier_gradient_checks": 27,
        "poisson": poisson,
        "finite_N_200_T_4_equal_weights_alpha_1": {
            "epsilon_exact": str(eps), "expected_increment_upper_bound_exact": str(bound),
            "upper_bound_decimal": outward_decimal((bound, bound)),
        },
        "wider_class_N_100_T_4_equal_weights_alpha_1": {
            "expected_increment_upper_bound_exact": str(wider_bound),
            "upper_bound_decimal_interval": outward_decimal((wider_bound, wider_bound)),
        },
        "exact_cohort_paths": cases,
        "cohort_events": events,
        "path_checks": ["clearing despite arrivals", "through service loss",
                        "workload sandwich", "independent unit drain identity",
                        "original-local service accounting", "workload lower bound on counts"],
        "elapsed_seconds": round(time.monotonic() - started, 4),
        "peak_RSS_bytes": rss_bytes,
        "process_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "cpu_limit_seconds": resource.getrlimit(resource.RLIMIT_CPU)[0],
    }
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("sampled_drift_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
