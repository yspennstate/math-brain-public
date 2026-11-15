"""Aggregate saved torus experiments; no continuum threshold claim."""
import csv
import json
from collections import defaultdict
from pathlib import Path
import platform
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
rows = []
for path in sorted((ROOT / "data").glob("torus_*.csv")):
    with path.open() as file:
        rows += list(csv.DictReader(file))
groups = defaultdict(list)
for row in rows:
    groups[float(row["L"]), int(row["resolution"]), float(row["alpha_requested"])].append(row)
summary = []
for (L, resolution, alpha), values in sorted(groups.items()):
    item = {"L": L, "resolution": resolution, "alpha_requested": alpha,
            "alpha_grid": float(values[0]["alpha_grid"]), "replicates": len(values)}
    for phase in ("claimed", "vacant"):
        for conn in (4, 8):
            prefix = f"{phase}{conn}"
            hits = sum(int(v[f"{prefix}_wrap_any"]) for v in values)
            item[f"{prefix}_wrap_count"] = hits
            item[f"{prefix}_wrap_rate"] = hits / len(values)
            item[f"{prefix}_largest_fraction_torus_mean"] = float(np.mean([float(v[f"{prefix}_largest_fraction_torus"]) for v in values]))
            item[f"{prefix}_largest_fraction_phase_mean"] = float(np.mean([float(v[f"{prefix}_largest_fraction_phase"]) for v in values]))
    item["claimed_fraction_mean"] = float(np.mean([float(v["claimed_fraction"]) for v in values]))
    summary.append(item)
if summary:
    with (ROOT / "data" / "summary.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(summary[0]))
        writer.writeheader()
        writer.writerows(summary)
checks = {"runs": len(rows), "platform": platform.platform(),
          "blocking_pairs": sum(int(v["blocking_pairs"]) for v in rows),
          "audited_pairs": sum(int(v["audit_pairs"]) for v in rows),
          "max_peak_rss_native": max([float(v["peak_rss_native"]) for v in rows], default=0),
          "max_density_error": max([abs(float(v["claimed_fraction"]) - min(1., float(v["density"]) * float(v["alpha_grid"]))) for v in rows], default=0),
          "total_allocation_and_audit_seconds": sum(float(v["seconds"]) for v in rows)}
if platform.system() == "Darwin":
    checks["max_peak_rss_MiB"] = checks["max_peak_rss_native"] / 2**20
else:
    checks["max_peak_rss_MiB"] = checks["max_peak_rss_native"] / 1024

# Check monotone claimed occupancy and winding under increasing equal quotas.
by_seed = defaultdict(list)
for row in rows:
    by_seed[row["L"], row["resolution"], row["seed"]].append(row)
violations = []
for key, values in by_seed.items():
    values.sort(key=lambda v: float(v["alpha_grid"]))
    for a, b in zip(values, values[1:]):
        for conn in (4, 8):
            if int(a[f"claimed{conn}_wrap_any"]) > int(b[f"claimed{conn}_wrap_any"]):
                violations.append([key, "claimed winding", a["alpha_grid"], b["alpha_grid"]])
            if int(a[f"vacant{conn}_wrap_any"]) < int(b[f"vacant{conn}_wrap_any"]):
                violations.append([key, "vacant winding", a["alpha_grid"], b["alpha_grid"]])
            if int(a[f"claimed{conn}_largest"]) > int(b[f"claimed{conn}_largest"]):
                violations.append([key, "claimed largest size", a["alpha_grid"], b["alpha_grid"]])
            if int(a[f"vacant{conn}_largest"]) < int(b[f"vacant{conn}_largest"]):
                violations.append([key, "vacant largest size", a["alpha_grid"], b["alpha_grid"]])
checks["monotonicity_violations"] = violations
assert checks["blocking_pairs"] == 0
assert checks["max_density_error"] < 1e-12
assert not violations
(ROOT / "data" / "audit_summary.json").write_text(json.dumps(checks, indent=2) + "\n")

def half_crossing(x, y):
    exact = [float(a) for a, b in zip(x, y) if abs(b-.5) < 1e-12]
    if exact:
        return (min(exact)+max(exact))/2
    for a, b, u, v in zip(x, x[1:], y, y[1:]):
        if u < .5 < v:
            return float(a+(.5-u)/(v-u)*(b-a))
    return None

thresholds = []
by_grid = defaultdict(list)
for item in summary:
    by_grid[item["L"], item["resolution"]].append(item)
for (L, resolution), values in sorted(by_grid.items()):
    values.sort(key=lambda v: v["alpha_grid"])
    x = [v["alpha_grid"] for v in values]
    item = {"L": L, "resolution": resolution, "replicates": values[0]["replicates"]}
    for phase in ("claimed", "vacant"):
        for conn in (4, 8):
            y = [v[f"{phase}{conn}_wrap_rate"] for v in values]
            if phase == "vacant":
                y = [1-p for p in y]
            item[f"{phase}{conn}_half_winding_crossover"] = half_crossing(x, y)
    thresholds.append(item)
if thresholds:
    with (ROOT / "data" / "finite_grid_crossovers.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(thresholds[0]))
        writer.writeheader()
        writer.writerows(thresholds)
print(json.dumps(checks, indent=2))
for item in summary:
    if item["alpha_requested"] in (.6, .65, .675, .7, .725, .75, .8):
        print(f'L={item["L"]:g} r={item["resolution"]} a={item["alpha_grid"]:.6f} n={item["replicates"]} C4={item["claimed4_wrap_rate"]:.3f} U4={item["vacant4_wrap_rate"]:.3f} C8={item["claimed8_wrap_rate"]:.3f} U8={item["vacant8_wrap_rate"]:.3f}')
