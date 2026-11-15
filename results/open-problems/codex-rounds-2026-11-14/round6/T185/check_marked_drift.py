"""Exact marked-file trajectories, using per-route service clocks.

Standard library only. All output stays beside this script. These are
deterministic pathwise checks, not stochastic simulations or a proof.
"""

import json
import os
import resource
import sys
import time
from fractions import Fraction as F
from pathlib import Path


def limits():
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    cap = min([60] + [x for x in (soft, hard) if x != resource.RLIM_INFINITY])
    resource.setrlimit(resource.RLIMIT_CPU, (cap, hard))
    assert all(os.environ.get(k) == "1" for k in
               ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"))
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def moments(pmf):
    assert sum(p for b, p in pmf) == 1
    direct = [sum((p * b**k for b, p in pmf), F(0)) for k in (1, 2)]
    # Independent layer-cake integral, exact for finite support.
    points = [F(0)] + sorted(b for b, p in pmf)
    tail = [sum(((right**k - left**k) * sum(p for b, p in pmf if b >= right)
                 for left, right in zip(points, points[1:])), F(0)) for k in (1, 2)]
    assert direct == tail
    return direct


def check_constants():
    laws = [[(F(1, 2), F(1, 2)), (F(3, 2), F(1, 2))],
            [(F(1, 4), F(1, 2)), (F(7, 4), F(1, 2))]]
    assert moments(laws[0]) == [F(1), F(5, 4)]
    assert moments(laws[1]) == [F(1), F(25, 16)]
    rho = (F(1, 5), F(1, 2), F(1, 2))
    assert rho[0] + max(rho[1:]) == F(7, 10)
    variance_rate = F(1, 2) * F(25, 16) + F(1, 2) * F(5, 4)
    assert variance_rate == F(45, 32)
    t, k, r, b0 = F(8), 512, F(65536), F(3, 2)
    assert variance_rate * t == F(45, 4) <= F(7, 2)**2
    d = -F(3, 10) * t + F(7, 4)
    error = t**2 / k + b0 * t * (2 * k + t) / r
    drift = d + error
    assert (d, error, drift, r + 2 * t) == (
        -F(13, 20), F(643, 2048), -F(3441, 10240), F(65552))
    # Independent denominator calculation of the final drift.
    assert F(-6656 + 1280 + 1935, 10240) == drift

    # Infinite-variance dyadic law: finite sums + exact geometric remainder.
    for exponent in range(17):
        h = F(2)**exponent
        probabilities = [F(3, 4**(n + 1)) for n in range(exponent + 1)]
        remainder_mass = F(1, 4**(exponent + 1))
        assert sum(probabilities) + remainder_mass == 1
        cap_mean = sum((p * 2**n for n, p in enumerate(probabilities)), F(0)) + h * remainder_mass
        cap_second = sum((p * 4**n for n, p in enumerate(probabilities)), F(0)) + h**2 * remainder_mass
        # Independent survival-integral formulas across dyadic intervals.
        tail_excess = F(1, 2**(exponent + 1))
        survival_cap_second = 1 + sum((F(4**(j + 1) - 4**j, 4**(j + 1))
                                      for j in range(exponent)), F(0))
        assert F(3, 2) - cap_mean == tail_excess
        assert cap_second == survival_cap_second == F(3 * exponent + 4, 4)
        # The uncapped second moment adds 3/4 at every atom.
        assert sum((p * 4**n for n, p in enumerate(probabilities)), F(0)) == F(3 * (exponent + 1), 4)
    t, k, r = F(192), 4096, F(2**20)
    local_rate, eta, cap_variance = F(2, 3), F(1, 48), F(4, 3)
    assert cap_variance * t == 16**2
    d_infinite = -F(3, 10) * t + 2 * 16 + eta * t
    error_infinite = local_rate * t**2 / k + b0 * t * (2 * k + local_rate * t) / r
    infinite_drift = d_infinite + error_infinite
    assert d_infinite == -F(108, 5)
    assert error_infinite == 6 + F(2925, 1280)
    assert infinite_drift == -F(17043, 1280)
    assert r + 2 * t == 1048960
    assert F(-27648 + 7680 + 2925, 1280) == infinite_drift
    return {
        "bounded_random_sizes": {"T": "8", "K": 512, "R0": "65536", "B": "65552",
                                 "d_upper": str(d), "error": str(error), "drift_upper": str(drift)},
        "infinite_variance_local_sizes": {
            "T": "192", "K": 4096, "R0": "1048576", "B": "1048960",
            "mean_local_size": "3/2", "local_second_moment": "infinite",
            "cap_h": "16", "cap_second_moment": "4", "eta": "1/48",
            "d_upper": str(d_infinite), "error": str(error_infinite), "drift_upper": str(infinite_drift)},
        "dyadic_moment_checks": 17,
    }


def initial_states():
    big, tiny = 10**7, F(1, 10**12)
    return [
        [[], [], []],
        [[(1, F(3, 2))], [], []],
        [[], [(1, F(10**8))], []],
        [[], [(20, F(1, 2))], [(1, F(10**6))]],
        [[(70000, F(3, 2))], [], []],
        [[(70000, F(3, 2))], [(big, F(1, big))], []],
        [[(70000, F(3, 2))], [(big, F(3, 2 * big))], [(2 * big, F(1, 3 * big))]],
        [[(70000, F(3, 2))], [(512, F(1, 1024)), (4, F(1, 4))], [(513, F(1, 513))]],
        [[(100, F(1, 2))], [(2, F(10**5))], [(big, tiny)]],
        [[(big, tiny), (70000, F(1))], [(big, tiny)], [(big, 2 * tiny)]],
        [[(1, F(1, 100))], [(3, F(1, 5))], [(1, F(1, 10))]],
        [[(10000, F(3, 2))], [(512, F(1, 512))], [(513, F(1, 1026))]],
        [[(200, F(3, 2))], [(1, F(1000))], [(1, F(1000))]],
        [[(200, F(3, 2))], [(big, F(1, big))], [(3, F(1, 100))]],
    ]


def schedules(t):
    e = F(1, 10**9)
    return [
        [],
        [(e, 1, 1, F(1, 4)), (2 * e, 2, 1, F(3, 2)), (t / 2, 0, 1, F(1, 2))],
        [(e, 1, 1000, F(1, 1000)), (e, 2, 7, F(10**6)), (t / 2, 2, 3, F(1, 2))],
        [(t * j / 15, j % 3, 1, F(1, 2) if j % 3 == 0 else F(2)**(j - 6)) for j in range(1, 15)],
        [(t / 4, 1, 1, F(7, 4)), (t / 2, 2, 1, F(1, 2)), (3 * t / 4, 1, 1, F(1, 4))],
        [(e, 0, 10, F(3, 2)), (t - e, 1, 100, F(10**9)), (t - e, 2, 100, e)],
        [(t, 0, 1, F(3, 2)), (t, 1, 2, F(2**20)), (t, 2, 3, F(1, 8))],
    ]


def check_path(initial, arrivals, weights, horizon):
    # A cohort is (count, target service-clock level, original flag).
    cohorts = [[(n, size, True) for n, size in route] for route in initial]
    clock = [F(0)] * 3

    def workloads():
        return [sum((n * (target - clock[j]) for n, target, original in cohorts[j]), F(0))
                for j in range(3)]

    def maximum():
        w = workloads()
        return w[0] + max(w[1:])

    arrivals = sorted(arrivals)
    initial_work = workloads()
    m, initial_m = max(initial_work[1:]), maximum()
    totals = [sum((n * size for when, route, n, size in arrivals if route == j), F(0)) for j in range(3)]
    count_total = sum(n for when, route, n, size in arrivals if route in (1, 2))
    t = Q = busy = jump_sum = F(0)
    actual = [F(0)] * 3
    regulators, supremum = [F(0)] * 2, [F(0)] * 2
    arrived_work, original_service = [F(0)] * 3, [F(0)] * 2
    intervals = []
    i = departures = mixed = 0
    b0 = F(3, 2)
    assert all(size <= b0 for n, size in initial[0])
    assert all(size <= b0 for when, route, n, size in arrivals if route == 0)
    while t < horizon:
        counts = [sum(n for n, target, original in route) for route in cohorts]
        old = [sum(n for n, target, original in route if original) for route in cohorts]
        denominator = sum(weights[j] * counts[j] for j in range(3))
        x = weights[0] * counts[0] / denominator if counts[0] else F(0)
        q = 1 - x
        rates = [x, q if counts[1] else F(0), q if counts[2] else F(0)]
        if counts[0] and (counts[1] or counts[2]):
            assert weights[0] * counts[0] / x == sum(weights[j] * counts[j] for j in (1, 2)) / q
        assert x + rates[1] <= 1 and x + rates[2] <= 1
        next_event = min(horizon, arrivals[i][0] if i < len(arrivals) else horizon)
        for j in range(3):
            if counts[j]:
                next_event = min(next_event, *(t + (target - clock[j]) * counts[j] / rates[j]
                                                for n, target, original in cohorts[j]))
        dt = next_event - t
        assert dt > 0
        before = maximum()
        Q += q * dt
        busy += dt * bool(sum(counts))
        intervals.append((next_event, Q, tuple(old[1:])))
        for j in range(3):
            actual[j] += rates[j] * dt
            if counts[j]:
                clock[j] += rates[j] * dt / counts[j]
            assert all(target >= clock[j] for n, target, original in cohorts[j])
        for j in (1, 2):
            if not counts[j]:
                regulators[j - 1] += q * dt
            else:
                original_service[j - 1] += q * dt * F(old[j], counts[j])
                mixed += int(0 < old[j] < counts[j])
            supremum[j - 1] = max(supremum[j - 1], Q - initial_work[j] - arrived_work[j])
        # Independent property: M drains at unit rate whenever nonempty.
        assert maximum() - before == -dt * bool(sum(counts))
        for j in range(3):
            departures += sum(1 for n, target, original in cohorts[j] if original and target == clock[j])
            cohorts[j] = [(n, target, original) for n, target, original in cohorts[j] if target > clock[j]]
        t = next_event
        while i < len(arrivals) and arrivals[i][0] == t:
            when, j, n, size = arrivals[i]
            before = maximum()
            cohorts[j].append((n, clock[j] + size, False))
            arrived_work[j] += n * size
            jump_sum += maximum() - before
            i += 1
        assert len(intervals) < 400
    assert arrived_work == totals
    final = workloads()
    delta = maximum() - initial_m
    assert delta == jump_sum - busy
    assert final[0] == initial_work[0] + totals[0] - horizon + Q
    for j in (1, 2):
        assert regulators[j - 1] == supremum[j - 1]
        assert final[j] == initial_work[j] + totals[j] - Q + regulators[j - 1]
        assert original_service[j - 1] <= initial_work[j]
    benchmark = totals[0] - horizon + max(totals[1:])
    assert delta <= benchmark + max(F(0), Q - m)
    if m >= horizon:
        assert delta <= benchmark
    checked = high_count_barriers = 0
    if initial_work[0] > horizon:
        r = initial_work[0] - horizon
        assert sum(n for n, target, original in cohorts[0]) >= final[0] / b0 >= r / b0
        for k in (1, 2, 4, 16, 512):
            barrier = m * (1 + F(count_total, k))
            for end, area, original in intervals:
                if max(original) > k:
                    assert area <= barrier
                    high_count_barriers += 1
            bound = barrier + max(weights[1:]) * b0 * horizon * (2 * k + count_total) / (weights[0] * r)
            assert Q <= bound
            checked += 1
    return {
        "paths": 1, "events": len(intervals), "threshold_checks": checked,
        "high_count_barrier_checks": high_count_barriers,
        "original_departure_events": departures, "mixed_cohort_intervals": mixed,
        "Q_greater_than_m": int(Q > m), "positive_empty_time": int(busy < horizon),
        "large_local_paths": int(m >= horizon),
    }


def main():
    limits()
    started = time.monotonic()
    result = {"constants": check_constants()}
    counts = {}
    for t in (F(1), F(8), F(192)):
        for initial in initial_states():
            for arrivals in schedules(t):
                for weights in ((F(1), F(1), F(1)), (F(2), F(3), F(5)),
                                (F(1), F(1, 100), F(100)), (F(1), F(10**6), F(1))):
                    for key, value in check_path(initial, arrivals, weights, t).items():
                        counts[key] = counts.get(key, 0) + value
    assert all(counts[key] > 0 for key in counts)
    result["path_checks"] = counts
    result["status"] = "all exact checks passed"
    result["elapsed_seconds"] = round(time.monotonic() - started, 4)
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result["peak_RSS_bytes"] = raw if sys.platform == "darwin" else raw * 1024
    result["process_nice"] = os.getpriority(os.PRIO_PROCESS, 0)
    result["cpu_limit_seconds"] = resource.getrlimit(resource.RLIMIT_CPU)[0]
    assert result["peak_RSS_bytes"] < 1024**3
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("marked_drift_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
