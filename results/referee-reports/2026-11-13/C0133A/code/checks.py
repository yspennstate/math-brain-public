"""Single-process numerical checks for C0133. No recurrence inference from a run."""
import csv
import json
import math
import os
import random
import resource
import statistics
import time
from pathlib import Path

if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data"
SEED = 13320261113


def wilson(k, n):
    z = 1.959963984540054
    p = k / n
    center = (p + z*z/(2*n)) / (1 + z*z/n)
    radius = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / (1 + z*z/n)
    return [center-radius, center+radius]


def walk(model, seed, horizon):
    rng = random.Random(seed)
    x = y = 0
    counts = {}
    last_return = 0
    returns = []
    excursions = []
    peak = 0
    peak_first_coord = 0
    late_speed = 0.0
    for n in range(1, horizon+1):
        pos = (x, y)
        i = counts.get(pos, 0) + 1
        counts[pos] = i
        if model == "simple":
            beta = 0.0
        elif model == "finite_two":
            beta = 0.8 if i == 1 else (-0.8 if i == 2 else 0.0)
        elif model == "infinite_periodic":
            beta = 0.8 if i % 2 else -0.8
        elif model == "infinite_blocks":
            beta = 0.8 if (i.bit_length()-1) % 2 == 0 else -0.8
        else:
            raise ValueError(model)
        u = rng.random()
        if u < (1+beta)/4:
            x += 1
        elif u < 0.5:
            x -= 1
        elif u < 0.75:
            y += 1
        else:
            y -= 1
        peak = max(peak, abs(x)+abs(y))
        peak_first_coord = max(peak_first_coord, abs(x))
        if n >= horizon//2:
            late_speed = max(late_speed, abs(x)/n)
        if x == 0 and y == 0:
            returns.append(n)
            excursions.append({"duration": n-last_return, "peak_l1": peak,
                               "peak_abs_x": peak_first_coord, "end_time": n})
            last_return = n
            peak = peak_first_coord = 0
    row = {"model": model, "seed": seed, "horizon": horizon,
           "returns": len(returns), "return_in_second_half": int(last_return >= horizon//2),
           "last_return": last_return, "final_x": x, "final_y": y,
           "range": len(counts), "max_abs_x_over_n_second_half": late_speed,
           "max_completed_excursion": max((a["duration"] for a in excursions), default=0),
           "max_completed_peak_l1": max((a["peak_l1"] for a in excursions), default=0),
           "censored_excursion_length": horizon-last_return,
           "censored_peak_l1": peak}
    return row, excursions


def check_counts():
    """Independent finite checks of the two sums in proof (6)."""
    rng = random.Random(SEED+1)
    successes = 0
    for trial in range(100):
        # Positive drift ensures many finite levels in this finite test.
        xs = [0]
        for _ in range(2000):
            u = rng.random()
            xs.append(xs[-1] + (1 if u < 0.65 else -1 if u < 0.8 else 0))
        hitting = {}
        visits = {}
        for n, x in enumerate(xs):
            hitting.setdefault(x, n)
            visits.setdefault(x, []).append(n)
        for L in [1, 2, 5, 11]:
            M = min(100, max(hitting)-L)
            end = hitting[M+L]
            cardinalities = []
            durations = []
            for m in range(M+1):
                ts = [n for n in visits[m] if hitting[m] <= n < hitting[m+L]]
                cardinalities.append(len(ts))
                durations.append(max(ts)-hitting[m])
            assert sum(cardinalities) <= end
            assert sum(durations) <= L*end
            # Check strict-growth implication separately at every level.
            for m in range(M+1):
                a = [n for n in visits[m] if hitting[m] <= n < hitting[m+1]]
                b = [n for n in visits[m] if hitting[m] <= n < hitting[m+L]]
                assert max(a) <= max(b)
                if max(a) < max(b):
                    assert len(a) < len(b)
            successes += 1
    return {"paths": 100, "path_length": 2000, "sum_checks": successes,
            "strict_growth_implication": "passed"}


def trap_check():
    """Simulate the specified 0,e1 two-cycle event, stopping at first deviation."""
    rng = random.Random(SEED+2)
    trials = 20000
    cookies = 80
    marked = survived = 0
    for _ in range(trials):
        a = rng.randrange(4)
        b = rng.randrange(4)
        if a != 0 or b != 1:  # directions +e1 at 0, -e1 at e1
            continue
        marked += 1
        good = True
        for i in range(1, cookies+1):
            p = 1 - 3*2.0**(-i-4)
            if rng.random() >= p or rng.random() >= p:
                good = False
                break
        survived += int(good)
    product = 1/16
    for i in range(1, cookies+1):
        product *= (1 - 3*2.0**(-i-4))**2
    via_logs = math.exp(-math.log(16) + 2*sum(math.log1p(-3*2.0**(-i-4))
                                               for i in range(1, cookies+1)))
    assert abs(product-via_logs) < 1e-14
    # Union bound for any later non-mark departure, given the prefix.
    tail_error = 6*2.0**(-cookies-4)
    return {"trials": trials, "mark_pairs": marked, "survivals": survived,
            "frequency": survived/trials, "wilson_95": wilson(survived, trials),
            "cookies_per_site": cookies, "event_probability_product": product,
            "event_probability_via_logs": via_logs,
            "conditional_tail_error_bound": tail_error,
            "completed_two_step_excursions_on_success": cookies,
            "maximum_distance_on_success": 1,
            "maximum_abs_x_over_n_after_time_2k": "1/(2k+1)"}


def main():
    started = time.monotonic()
    rows = []
    summaries = {}
    with (OUT / "completed_excursions.csv").open("w", newline="") as ef:
        ew = csv.DictWriter(ef, fieldnames=["model", "run", "duration", "peak_l1", "peak_abs_x", "end_time"])
        ew.writeheader()
        for mi, model in enumerate(["simple", "finite_two", "infinite_periodic", "infinite_blocks"]):
            subset = []
            for run in range(64):
                row, excursions = walk(model, SEED + mi*100000 + run, 65536)
                row["run"] = run
                rows.append(row)
                subset.append(row)
                ew.writerows(dict(model=model, run=run, **e) for e in excursions)
            k = sum(r["return_in_second_half"] for r in subset)
            summaries[model] = {"runs": 64, "horizon": 65536,
                "return_in_second_half_count": k, "frequency": k/64,
                "wilson_95": wilson(k,64),
                "median_returns": statistics.median(r["returns"] for r in subset),
                "max_completed_excursion": max(r["max_completed_excursion"] for r in subset),
                "median_censored_excursion_length": statistics.median(r["censored_excursion_length"] for r in subset),
                "max_late_abs_x_over_n": max(r["max_abs_x_over_n_second_half"] for r in subset)}
            print(model, summaries[model], flush=True)
    with (OUT / "walks.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    result = {"seed": SEED, "priority": os.getpriority(os.PRIO_PROCESS,0),
              "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "workers": 1, "models": summaries, "counting_checks": check_counts(),
              "trap": trap_check(), "elapsed_seconds": time.monotonic()-started,
              "interpretation": "Return frequencies are finite-horizon proxies, not estimates of infinite recurrence probability."}
    (OUT / "checks.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result["trap"], indent=2), flush=True)
    print("counting",result["counting_checks"], "seconds",result["elapsed_seconds"], flush=True)


if __name__ == "__main__":
    main()
