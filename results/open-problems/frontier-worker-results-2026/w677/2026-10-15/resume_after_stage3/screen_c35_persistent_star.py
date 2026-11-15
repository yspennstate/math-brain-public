"""Numerical screening only: persistent-star / fresh-child return operator.

Linear PGF interpolation, bisection, and all arithmetic here are floating
point. No output is a rigorous bound. No empirical-law sampling is used.
"""
import argparse
import ctypes
import hashlib
import json
import math
from pathlib import Path
import time


def interp(values, x):
    n = len(values) - 1
    if x <= 0:
        return values[0]
    if x >= 1:
        return values[n]
    t = x * n
    i = int(t)
    return values[i] + (t - i) * (values[i + 1] - values[i])


def transform(d, values, mean, deadline):
    p = 1.0 / (d + 1)
    q = p
    crit = (1 - p * (1 - p)) / (1 - p)
    if mean >= crit:
        return None, {"status": "input_mean_at_or_above_clan_critical",
                      "input_mean": mean, "clan_critical_mean": crit}
    n = len(values) - 1
    output = []
    min_joint = 1.0
    last_t = None
    for j in range(n + 1):
        if j % 64 == 0 and time.monotonic() > deadline:
            raise TimeoutError("bounded command budget reached")
        z = j / n
        ts = [(p * z) ** 2]
        for k in range(1, d + 1):
            if j == n and k == d:
                b = 1.0
            else:
                lo, hi = 0.0, 1.0
                for _ in range(48):
                    b = (lo + hi) / 2
                    f = p * p * z + p * k * q * b + (1 - p) * interp(values, b)
                    if f > b:
                        lo = b
                    else:
                        hi = b
                b = (lo + hi) / 2
            a = p * z + k * q * b
            t = a * a * b ** k - sum(math.comb(k, i) * ts[i] * b ** (k - i)
                                    for i in range(k))
            ts.append(t)
        min_joint = min(min_joint, min(ts))
        output.append(sum(math.comb(d, k) * ts[k] for k in range(d + 1)))
        if j == n:
            last_t = ts
    activation = sum(math.comb(d - 1, k - 1) * last_t[k] for k in range(1, d + 1))
    den = 1 - p * (1 - p) - (1 - p) * mean
    root_clan = p * (1 - (1 - p) * mean) / den
    leaf_clan = p * p / den
    out_mean = 2 * root_clan + d * activation * leaf_clan
    min_increment = min(output[i + 1] - output[i] for i in range(n))
    min_second = min(output[i + 2] - 2 * output[i + 1] + output[i] for i in range(n - 1))
    report = {"status": "numerical_evidence", "input_mean": mean,
              "output_mean": out_mean, "leaf_activation": activation,
              "phi_0": output[0], "phi_half": interp(output, 0.5),
              "mass_at_z1": output[-1], "min_joint_pgf": min_joint,
              "min_grid_increment": min_increment, "min_grid_second_difference": min_second,
              "clan_critical_mean": crit}
    if min_joint < -1e-8 or abs(output[-1] - 1) > 1e-8 or min_increment < -1e-8 or min_second < -1e-7:
        report["status"] = "numerical_sanity_failure"
    return output, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degrees", default="2,4,5,6")
    ap.add_argument("--grid", type=int, default=512)
    ap.add_argument("--iterations", type=int, default=20)
    ap.add_argument("--seconds", type=float, default=180)
    ap.add_argument("--out", default="C35_STAR_SCREEN_512.json")
    args = ap.parse_args()
    if args.grid < 8 or args.seconds > 480:
        raise ValueError("grid >= 8 and bounded command <= 480 s required")
    started = time.monotonic()
    deadline = started + args.seconds
    record = {"status": "incomplete", "rigorous": False,
              "method": "float PGF grid interpolation and scalar bisection",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "grid": args.grid, "iterations_requested": args.iterations,
              "memory_size_estimate_bytes": 64 * (args.grid + 1) * 6,
              "degrees": {}}
    class MemoryStatus(ctypes.Structure):
        _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [
            (name, ctypes.c_ulonglong) for name in ("total_phys", "avail_phys", "total_page",
            "avail_page", "total_virtual", "avail_virtual", "avail_extended")]
    memory = MemoryStatus()
    memory.length = ctypes.sizeof(memory)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
        raise RuntimeError("free-memory check failed")
    record["free_memory_before_bytes"] = memory.avail_phys
    if memory.avail_phys < 2 * 1024 ** 3:
        record["status"] = "not_started_low_memory"
        Path(args.out).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": record["status"], "file": args.out}))
        return
    path = Path(args.out)
    def save():
        record["elapsed_seconds"] = time.monotonic() - started
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    try:
        for d in map(int, args.degrees.split(",")):
            beta = 1 / d
            values = [1 - beta + beta * i / args.grid for i in range(args.grid + 1)]
            mean = beta
            rec = {"ordinary_p": 1 / (d + 1), "sterile_tail_beta": beta, "steps": []}
            record["degrees"][str(d)] = rec
            save()
            for h in range(args.iterations):
                new_values, step = transform(d, values, mean, deadline)
                step["blocks"] = h + 1
                step["lowest_resident_depth_relative_to_block_root"] = 2 * h + 1
                rec["steps"].append(step)
                save()
                if new_values is None or step["status"] != "numerical_evidence":
                    break
                values, mean = new_values, step["output_mean"]
            rec["last_grid"] = values
            rec["last_finite_mean"] = mean
            save()
        record["status"] = "complete_numerical_screen"
    except TimeoutError as exc:
        record["stop_reason"] = str(exc)
    save()
    print(json.dumps({"file": str(path), "status": record["status"], "rigorous": False,
                      "degrees": {d: {"steps": len(x["steps"]), "last": x["steps"][-1]}
                                  for d, x in record["degrees"].items()}}, separators=(",", ":")))


if __name__ == "__main__":
    main()
