"""Independent event simulation; stdlib only, no author code imported.

Run serially. The path supremum includes both sides of every event and the
horizon: between events W-hQ is affine. Deque endpoints suffice for both
LCFS preemptive-resume and the half-to-each-end symmetric discipline.
"""
import json
import math
import random
import resource
import signal
import statistics
import time
from collections import deque
from fractions import Fraction as F
from pathlib import Path


def timeout(signum, frame):
    raise TimeoutError("240 second wall-clock budget")


signal.signal(signal.SIGALRM, timeout)
signal.alarm(240)
START = time.monotonic()
OUT = Path(__file__).with_name("referee_simulation.json")


def simulate(rate, h, horizon, discipline, rng, draw, whole_cycle=False):
    jobs = deque()  # [original requirement, remaining requirement]
    t = work = maximum = work_error = 0.0
    next_arrival = rng.expovariate(rate)
    ncycles = arrivals = events = maxq = reward = 0

    def observe():
        nonlocal maximum, maxq
        maximum = max(maximum, abs(work - h * len(jobs)))
        maxq = max(maxq, len(jobs))

    while t < horizon:
        n = len(jobs)
        if n == 0:
            left = right = math.inf
        elif n == 1 or discipline == "LCFS":
            left, right = math.inf, jobs[-1][1]
        else:
            left, right = 2 * jobs[0][1], 2 * jobs[-1][1]
        departure = min(left, right)
        wait_arrival = next_arrival - t
        remaining_horizon = horizon - t
        dt = min(departure, wait_arrival, remaining_horizon)
        if n:
            if n == 1 or discipline == "LCFS":
                jobs[-1][1] = max(0.0, jobs[-1][1] - dt)
            else:
                jobs[0][1] = max(0.0, jobs[0][1] - dt / 2)
                jobs[-1][1] = max(0.0, jobs[-1][1] - dt / 2)
            work -= dt
        t += dt
        observe()  # left limit: especially necessary before departures
        if remaining_horizon <= min(departure, wait_arrival):
            break
        if departure <= wait_arrival:
            if left == departure:
                jobs.popleft()
            if right == departure:
                jobs.pop()
            if not jobs:
                work_error = max(work_error, abs(work))
                work = 0.0
                if whole_cycle:
                    observe()
                    break
        else:
            b = draw(rng)
            if not jobs:
                ncycles += 1
            if whole_cycle and len(jobs) <= 3:
                marked_work = sum(x for mark, x in jobs if mark == 4.0)
                reward += int(marked_work > 1.5 and b == 4.0)
            item = [b, b]
            # Insertion probabilities equal the service fractions at n+1.
            if discipline == "mixed_ends" and jobs and rng.random() < 0.5:
                jobs.appendleft(item)
            else:
                jobs.append(item)
            work += b
            arrivals += 1
            next_arrival = t + rng.expovariate(rate)
        events += 1
        observe()
        if events % 4096 == 0:
            err = abs(work - sum(x for _, x in jobs))
            work_error = max(work_error, err)
            assert err < 1e-7 * max(1.0, work), (discipline, t, err)
    return dict(supremum=maximum, maxq=maxq, cycles=ncycles,
                arrivals=arrivals, events=events, time=t,
                cycle_reward=reward, conservation_error=work_error)


def summary(values):
    ordered = sorted(values)
    return dict(mean=statistics.mean(values), median=statistics.median(values),
                p90=ordered[math.ceil(0.9 * len(ordered)) - 1],
                p_gt_half=sum(x > 0.5 for x in values) / len(values),
                p_gt_one=sum(x > 1 for x in values) / len(values),
                mean_se=statistics.stdev(values) / math.sqrt(len(values)))


def main():
    record = dict(seed=981173, alpha=2.5, xmin=0.6, mean_B=1,
                  second_moment_B=1.8, h=0.9,
                  third_moment_B="infinite", T=0.25, repetitions=48,
                  results=[], cycle_checks=[], status="running")
    def save():
        record["elapsed_seconds"] = time.monotonic() - START
        record["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        OUT.write_text(json.dumps(record, indent=2) + "\n")

    try:
        for di, discipline in enumerate(("LCFS", "mixed_ends")):
            for r in (32, 64, 128, 256, 512):
                paths = []
                for rep in range(record["repetitions"]):
                    # Reproduce each path without depending on previous runs.
                    rng = random.Random(record["seed"] + di * 10000000 + r * 1000 + rep)
                    paths.append(simulate(1 - 1 / r, 0.9, 0.25 * r * r,
                                          discipline, rng,
                                          lambda g: 0.6 * (1 - g.random()) ** (-1 / 2.5)))
                row = dict(discipline=discipline, r=r,
                           rho=1 - 1 / r,
                           scaled_supremum=summary([x["supremum"] / r for x in paths]),
                           mean_scaled_maxq=statistics.mean(x["maxq"] / r for x in paths),
                           mean_scaled_cycles=statistics.mean(x["cycles"] / r for x in paths),
                           events=sum(x["events"] for x in paths),
                           max_conservation_error=max(x["conservation_error"] for x in paths))
                record["results"].append(row)
                save()
                s = row["scaled_supremum"]
                print(f"{discipline:12} r={r:4} median={s['median']:.6f} "
                      f"mean={s['mean']:.6f} p90={s['p90']:.6f} "
                      f"P(>1)={s['p_gt_one']:.4f}", flush=True)

        # Independent exact target, not the predicates or service law of the
        # author's programs. B=1 (4/5), 4 (1/5); rho=4/5, lambda=1/2.
        # H(original=4)=1/2 and its residual is Uniform(0,4).
        rho = F(4, 5)
        pi = sum((1 - rho) * rho ** n * sum(
            F(math.comb(n, k), 2 ** n) * (1 - F(3, 8) ** k / math.factorial(k))
            for k in range(1, n + 1)) for n in range(1, 4))
        expected = 5 * F(1, 5) * pi
        record["cycle_target"] = dict(predicate="Q<=3 and V_{original=4}>3/2",
                                      pi_exact=str(pi), reward_exact=str(expected),
                                      expected_reward=float(expected), expected_length=10,
                                      cycles_per_discipline=20000)
        for di, discipline in enumerate(("LCFS", "mixed_ends")):
            rng = random.Random(397777 + di)
            paths = [simulate(0.5, 1.25, math.inf, discipline, rng,
                              lambda g: 4.0 if g.random() < 0.2 else 1.0,
                              whole_cycle=True) for _ in range(20000)]
            vals = [x["cycle_reward"] for x in paths]
            obs = statistics.mean(vals)
            se = statistics.stdev(vals) / math.sqrt(len(vals))
            row = dict(discipline=discipline, mean_reward=obs, standard_error=se,
                       z=(obs - float(expected)) / se,
                       mean_length=statistics.mean(x["time"] for x in paths))
            record["cycle_checks"].append(row)
            print("cycle", discipline, json.dumps(row), flush=True)
            save()
        record["status"] = "complete"
    except TimeoutError as exc:
        record["status"] = str(exc)
    save()
    print("status", record["status"], "elapsed", record["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
