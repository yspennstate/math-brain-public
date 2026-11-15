"""Small deterministic search for a capacity/layer proof certificate.

Floating point output proposes parameters; it is not the proof certificate.
Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B optimize_layers.py
"""

import ctypes
import json
import math
import os
from pathlib import Path
import resource
import sys


def guard():
    if os.environ.get("OMP_NUM_THREADS") != "1":
        raise RuntimeError("set OMP_NUM_THREADS=1")
    # Lower both limits: macOS does not accept its reported INT64_MAX
    # unlimited sentinel when passed back as an explicit hard limit.
    for kind, requested in ((resource.RLIMIT_CPU, 60),
                            (resource.RLIMIT_RSS, 256 * 1024 * 1024)):
        soft, hard = resource.getrlimit(kind)
        cap = requested if hard == resource.RLIM_INFINITY else min(requested, hard)
        try:
            resource.setrlimit(kind, (cap, cap))
        except ValueError:
            if kind != resource.RLIMIT_RSS:
                raise
            print("RSS hard limit unavailable on this macOS; reporting measured peak RSS")
    lib = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = lib.getpriority(0, 0)
    err = ctypes.get_errno()
    if err or priority < 15:
        raise RuntimeError(f"unverified scheduling: nice={priority}, errno={err}")
    print(f"niceness={priority}; OMP_NUM_THREADS=1; CPU limit=60s")


def evaluate(a, b, t, c, q):
    # Exp(u |B_t|^2) maximal inequality, with its optimizing u.
    z = (a - 1) ** 2 / t
    if z <= 3:
        return None
    exit_bound = math.exp(-(z - 3) / 2) * (z / 3) ** 1.5
    energy = (8 / 3) * math.sqrt(2 / math.pi) / math.sqrt(t)
    p = exit_bound + c * energy
    if not 0 < p < 1 - q:
        return None
    # q is the good-layer fraction; 1-q is the bad-layer fraction.
    d = ((1 - q) * math.log((1 - q) / p)
         + q * math.log(q / (1 - p)))
    tail_exponent = d / math.log(b)
    g = 1 / (1 + a) - b / (b * b + a)
    h = c * g
    delta = -q * math.log1p(-h) / math.log(b)
    if tail_exponent <= 1:
        return None
    return dict(a=a, b=b, t=t, c=c, q=q, p=p,
                exit_bound=exit_bound, green_min=g, hit_bound=h,
                tail_exponent=tail_exponent, delta=delta)


def main():
    guard()
    best = None
    count = 0
    # 8*11*7*16*19 = 187264 evaluations, no stochastic sampling.
    for a in (1.5, 2, 2.5, 3, 4, 5, 6, 8):
        for ratio in (1.1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 5, 6, 8):
            b = a * ratio
            for z in (14, 18, 22, 26, 30, 36, 44):
                t = (a - 1) ** 2 / z
                for c_units in range(1, 17):
                    c = c_units * (a - 1) / 1000
                    for q_units in range(1, 20):
                        q = q_units / 40
                        count += 1
                        result = evaluate(a, b, t, c, q)
                        if result and (best is None or result["delta"] > best["delta"]):
                            best = result
    original = evaluate(2, 4, 1 / 25, 1 / 200, 1 / 4)
    data = {"evaluations": count, "best_grid_point": best,
            "original_parameters_with_chernoff": original,
            "original_published_delta": -math.log1p(-1 / 1800) / (4 * math.log(4)),
            "note": "exploratory floating point; use PROOF.md for certification"}
    Path("layer_search.json").write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss * 1024
    print(f"peak_RSS_bytes={rss_bytes}")
    if rss_bytes >= 1024 ** 3:
        raise RuntimeError("memory budget exceeded")


if __name__ == "__main__":
    main()
