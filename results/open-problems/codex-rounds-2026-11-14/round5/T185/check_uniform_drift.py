"""Exact event-driven checks of the uniform-drift lemma; standard library only."""

import copy
import json
import os
import resource
import sys
import time
from fractions import Fraction as F
from pathlib import Path


def limits():
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    finite = [60] + [x for x in (soft, hard) if x != resource.RLIM_INFINITY]
    resource.setrlimit(resource.RLIMIT_CPU, (min(finite), hard))
    assert all(os.environ.get(k) == "1" for k in
               ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"))


def work(groups):
    return [sum((F(g[0]) * g[1] for g in route), F(0)) for route in groups]


def maximum(groups):
    w = work(groups)
    return w[0] + max(w[1:])


def states(t):
    n, huge = 65544, 10**7
    return [
        [[], [], []],
        [[[1, F(1, 2), True]], [], []],
        [[], [[10, F(1), True]], []],
        [[], [[10, F(1), True]], [[6, F(1), True]]],
        [[[n, F(1), True]], [], []],
        [[[n, F(1), True]], [[huge, F(1, huge), True]], []],
        [[[n, F(1), True]], [[huge, F(1, huge), True]],
         [[2 * huge, F(3, 4 * huge), True]]],
        [[[n, F(1), True]], [[2, F(1), True]],
         [[huge, F(1, huge), True]]],
        [[[n, F(1), True], [huge, F(1, huge**2), True]],
         [[256, F(1, 512), True], [3, F(1, 2), True]],
         [[257, F(1, 257), True]]],
        [[[20, F(1, 2), True]], [[10, F(1, 3), True]],
         [[20, F(1, 8), True]]],
        [[[1, F(1, 7), True]], [[20, F(1, 20), True]],
         [[30, F(1, 60), True]]],
        [[[n, F(1), True]], [[10, F(1), True]],
         [[huge, F(1, huge**2), True]]],
        [[], [[4, F(1), True]], [[1, F(1, 100), True]]],
        [[[n, F(1), True]], [[256, F(1, 256), True]],
         [[257, F(1, 257), True]]],
    ]


def schedules(t):
    tiny = F(1, 10**8)
    return [
        [],
        [(tiny, 1, 1), (2 * tiny, 2, 1), (t / 2, 0, 1)],
        [(tiny, 1, 300), (tiny, 2, 7), (t / 2, 2, 4)],
        [(t * k / 13, k % 3, 1) for k in range(1, 13)],
        [(t / 4, 1, 1), (t / 2, 2, 1), (3 * t / 4, 1, 1)],
        [(tiny, 0, 10), (t - tiny, 1, 100), (t - tiny, 2, 100)],
    ]


def check_path(initial, schedule, weights, horizon):
    groups = copy.deepcopy(initial)
    initial_work = work(groups)
    m = max(initial_work[1:])
    initial_m = maximum(groups)
    totals = [sum(count for _, route, count in schedule if route == j) for j in range(3)]
    local_total = totals[1] + totals[2]
    arrivals = sorted(schedule)
    t = F(0)
    q_integral = F(0)
    actual_local = [F(0), F(0)]
    regulators = [F(0), F(0)]
    supremum = [F(0), F(0)]
    counts_arrived = [0, 0, 0]
    busy = jumps = F(0)
    records = []
    i = 0
    original_departures = 0
    while t < horizon:
        counts = [sum(g[0] for g in route) for route in groups]
        old = [sum(g[0] for g in groups[j] if g[2]) for j in range(3)]
        h = weights[1] * counts[1] + weights[2] * counts[2]
        x = (weights[0] * counts[0] / (weights[0] * counts[0] + h)
             if counts[0] else F(0))
        q = 1 - x
        rates = [x, q if counts[1] else F(0), q if counts[2] else F(0)]
        assert all(rate >= 0 for rate in rates)
        assert x + rates[1] <= 1 and x + rates[2] <= 1
        next_t = min(horizon, arrivals[i][0] if i < len(arrivals) else horizon)
        for j in range(3):
            if counts[j]:
                next_t = min(next_t, *(t + g[1] * counts[j] / rates[j] for g in groups[j]))
        dt = next_t - t
        assert dt > 0
        q_integral += q * dt
        busy += dt * bool(sum(counts))
        records.append((next_t, q_integral, tuple(old[1:])))
        for j in range(3):
            if counts[j]:
                for g in groups[j]:
                    g[1] -= rates[j] * dt / counts[j]
                    assert g[1] >= 0
                    if g[1] == 0 and g[2]:
                        original_departures += 1
            groups[j] = [g for g in groups[j] if g[1]]
        for j in (1, 2):
            actual_local[j - 1] += rates[j] * dt
            if not counts[j]:
                regulators[j - 1] += q * dt
            supremum[j - 1] = max(supremum[j - 1],
                q_integral - initial_work[j] - counts_arrived[j])
        t = next_t
        while i < len(arrivals) and arrivals[i][0] == t:
            _, j, count = arrivals[i]
            before = maximum(groups)
            groups[j].append([count, F(1), False])
            counts_arrived[j] += count
            jumps += maximum(groups) - before
            i += 1
        assert len(records) < 300
    assert counts_arrived == totals
    final = work(groups)
    delta = maximum(groups) - initial_m
    benchmark = totals[0] - horizon + max(totals[1:])
    assert delta == jumps - busy  # Independent event-by-event maximum-work balance.
    assert final[0] == initial_work[0] + totals[0] - horizon + q_integral
    for j in (1, 2):
        assert regulators[j - 1] == supremum[j - 1]
        assert final[j] == initial_work[j] + totals[j] - q_integral + regulators[j - 1]
        assert actual_local[j - 1] == q_integral - regulators[j - 1]
    assert delta <= benchmark + max(F(0), q_integral - m)
    if m >= horizon:
        assert delta <= benchmark
    threshold_checks = 0
    if initial_work[0] > horizon:
        r = initial_work[0] - horizon
        c = max(weights[1:])
        for k in (1, 2, 4, 16, 256):
            threshold_times = []
            for j in (0, 1):
                high = [(end, area) for end, area, original in records if original[j] > k]
                threshold_times.append(high[-1] if high else (F(0), F(0)))
            tau, q_tau = max(threshold_times)
            if tau:
                # Select the route independently by its last high-count interval.
                j = threshold_times.index((tau, q_tau))
                assert q_tau <= initial_work[j + 1] * (1 + F(local_total, k))
            assert q_integral - q_tau <= c * horizon * (2 * k + local_total) / (weights[0] * r)
            bound = m * (1 + F(local_total, k)) + c * horizon * (2 * k + local_total) / (weights[0] * r)
            assert q_integral <= bound
            threshold_checks += 1
    return {
        "events": len(records), "threshold_checks": threshold_checks,
        "original_departure_events": original_departures,
        "positive_Q_minus_m": int(q_integral > m),
        "emptied_for_positive_time": int(busy < horizon),
        "large_local_path": int(m >= horizon),
    }


def constants():
    t, k, r = F(4), 256, F(65536)
    error = t * t / k + t * (2 * k + t) / r
    bound = -F(1, 5) + error
    assert error == F(385, 4096)
    assert bound == -F(2171, 20480)
    # Independent common-denominator calculation, without the error formula.
    assert -4096 + 1280 + 640 + 5 == -2171
    assert F(-4096 + 1280 + 640 + 5, 20480) == bound
    b = r + 2 * t
    assert b == 65544
    # Verify the split at the exact boundary and on either side.
    for m in (F(0), F(1), F(3999, 1000), F(4), F(5), F(100000)):
        for extra in (F(1, 1000), F(1), F(100)):
            maximum_work = b + extra
            if m < t:
                w0 = maximum_work - m
                assert w0 - t > r
                assert -F(1, 5) + m * t / k + t * (2 * k + t) / (w0 - t) <= bound
    # The no-arrival trial uses only a symbolic positive exponential, never
    # floating underflow. Check its finite algebraic prefactor exactly.
    epsilon, nu, d = -bound, F(6, 5), 2 * b
    h = d + t * (b + nu * d) / epsilon
    assert h > d > 0
    return {"T": str(t), "K": k, "R0": str(r), "B": str(b),
            "error": str(error), "drift_upper_bound": str(bound),
            "trial_duration_D": str(d), "trial_cost_prefactor_H": str(h),
            "trial_success_probability": "exp(-(6/5)*131088)"}


def main():
    limits()
    started = time.monotonic()
    result = {"exact_paths": 0}
    for t in (F(1), F(4)):
        for initial in states(t):
            for schedule in schedules(t):
                for weights in ((F(1), F(1), F(1)), (F(2), F(3), F(5)),
                                (F(1), F(1, 100), F(100)),
                                (F(1), F(10**6), F(1))):
                    counts = check_path(initial, schedule, weights, t)
                    result["exact_paths"] += 1
                    for key, value in counts.items():
                        result[key] = result.get(key, 0) + value
    assert result["positive_Q_minus_m"] > 0
    assert result["emptied_for_positive_time"] > 0
    result["constants"] = constants()
    result["status"] = "all exact checks passed"
    result["elapsed_seconds"] = round(time.monotonic() - started, 4)
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result["peak_RSS_bytes"] = raw if sys.platform == "darwin" else raw * 1024
    result["process_nice"] = os.getpriority(os.PRIO_PROCESS, 0)
    result["cpu_limit_seconds"] = resource.getrlimit(resource.RLIMIT_CPU)[0]
    assert result["peak_RSS_bytes"] < 1024**3
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("uniform_drift_checks.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
