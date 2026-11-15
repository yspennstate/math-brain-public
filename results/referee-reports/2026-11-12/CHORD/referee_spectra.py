"""Independent, single-process high-precision audit; no author modules imported.

Run one size or a small group per invocation. Each invocation has a 240s alarm.
All output files are relative to this script's folder. Only mpmath is required.
"""
import argparse
import csv
import json
import os
from pathlib import Path
import signal
import time

os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
import mpmath as mp

ROOT = Path(__file__).resolve().parent
WEIGHTS = ["0.01", "0.03", "0.1", "0.3", "1", "3", "10", "30", "100"]


def alarm_handler(signum, frame):
    raise TimeoutError("240-second computation limit")


def matrices(n, k, w):
    # Build from an unordered edge list, deriving every degree from that list.
    edges = [(i, (i + 1) % n, mp.mpf(1)) for i in range(n)] + [(0, k, w)]
    d = [mp.mpf(0)] * n
    lap = mp.matrix(n)
    for i, j, c in edges:
        d[i] += c
        d[j] += c
        lap[i, i] += c
        lap[j, j] += c
        lap[i, j] -= c
        lap[j, i] -= c
    normalized = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            normalized[i, j] = lap[i, j] / mp.sqrt(d[i] * d[j])
    # Independently implement the MH acceptance rule from P and uniform target.
    K = mp.matrix(n)
    for i, j, c in edges:
        pij, pji = c / d[i], c / d[j]
        K[i, j] = pij * min(mp.mpf(1), pji / pij)
        K[j, i] = pji * min(mp.mpf(1), pij / pji)
    for i in range(n):
        K[i, i] = 1 - mp.fsum(K[i, j] for j in range(n) if i != j)
    assert max(abs(K[i, j] - K[j, i]) for i in range(n) for j in range(n)) < mp.mpf("1e-48")
    return edges, d, lap, normalized, mp.eye(n) - K


def audit(n, k, weight):
    w = mp.mpf(weight)
    theta = 2 * mp.pi / n
    alpha = mp.pi * k / n
    a = 1 - mp.cos(theta)
    b = w / (2 + w)
    edges, d, lap, normalized, mh = matrices(n, k, w)
    rw_evals = mp.eigsy(normalized, eigvals_only=True)
    mh_evals = mp.eigsy(mh, eigvals_only=True)
    gamma, eta = rw_evals[1], mh_evals[1]
    rw_bound = a / (1 + 2 * w * mp.cos(alpha) ** 2 / (n + w))
    bracket = a**2 * mp.cos(alpha)**2 + mp.sin(theta)**2 * mp.sin(alpha)**2
    mh_bound = a - 4 * b / n * bracket
    f = mp.matrix([mp.cos(theta * i - alpha) for i in range(n)])
    mean = mp.fsum(d[i] * f[i] for i in range(n)) / mp.fsum(d)
    variance = mp.fsum(d[i] * (f[i] - mean)**2 for i in range(n))
    # Compute the Rayleigh quotients directly, without using the proposed bounds.
    energy = mp.fsum(c * (f[i] - f[j])**2 for i, j, c in edges)
    rw_rayleigh = energy / variance
    mh_rayleigh = (f.T * mh * f)[0] / mp.fsum(v**2 for v in f)
    tol = mp.mpf("1e-45")
    assert abs(rw_evals[0]) < tol and abs(mh_evals[0]) < tol
    assert gamma > 0 and eta > 0
    assert abs(rw_rayleigh - rw_bound) < tol
    assert abs(mh_rayleigh - mh_bound) < tol
    assert gamma <= rw_bound + tol and eta <= mh_bound + tol
    assert mh_bound < a
    if 2 * k == n:
        assert abs(gamma - a) < tol
    else:
        assert gamma < rw_bound < a
    return dict(n=n, k=k, w=weight, a=a, gamma=gamma, rw_bound=rw_bound,
                rw_slack=rw_bound-gamma, rw_relative_slack=(rw_bound-gamma)/gamma,
                mh_gap=eta, mh_bound=mh_bound, mh_slack=mh_bound-eta,
                mh_relative_slack=(mh_bound-eta)/eta,
                rw_formula_residual=abs(rw_rayleigh-rw_bound),
                mh_formula_residual=abs(mh_rayleigh-mh_bound),
                antipodal_residual=abs(gamma-a) if 2*k == n else mp.mpf(0))


def serial(row):
    return {key: mp.nstr(value, 45) if isinstance(value, mp.mpf) else value
            for key, value in row.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, required=True)
    parser.add_argument("--weights", nargs="+", default=WEIGHTS)
    parser.add_argument("--tag", default="")
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(240)
    mp.mp.dps = 55
    start = time.monotonic()
    for n in args.sizes:
        rows = [audit(n, k, w) for k in range(2, n//2+1) for w in args.weights]
        name = ROOT / f"referee_spectra{args.tag}_n{n}.csv"
        with name.open("w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(serial(row) for row in rows)
        summary = dict(n=n, cases=len(rows), precision_digits=mp.mp.dps,
                       max_antipodal_error=max(row["antipodal_residual"] for row in rows),
                       max_rw_formula_error=max(row["rw_formula_residual"] for row in rows),
                       max_mh_formula_error=max(row["mh_formula_residual"] for row in rows),
                       max_rw_relative_slack=max(row["rw_relative_slack"] for row in rows),
                       max_mh_relative_slack=max(row["mh_relative_slack"] for row in rows),
                       cumulative_seconds=round(time.monotonic()-start, 3), passed=True)
        print(json.dumps(serial(summary)), flush=True)


if __name__ == "__main__":
    main()
