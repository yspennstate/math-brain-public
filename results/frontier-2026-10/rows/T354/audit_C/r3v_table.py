"""AUDIT_CCLOSED table: exact (x*/x0 - 1)/d on the three-valued b (r3v_out/) by n d, extrapolated to d = 0, against the closed
form c(s) of cclosed_3v.py (agent C, 20 Oct 2026). Two points: linear in d. Three or more: quadratic through the last three."""
import glob
import re
import subprocess

import numpy as np

rows = {}
for f in glob.glob("r3v_out/root_*.txt"):
    m = re.search(r"n (\d+) beta2 ([\d.]+) nd ([\d.]+) .*\(x\*/x0-1\)/d ([-\d.]+)", open(f).read())
    if m:
        rows.setdefault(round(float(m[3]), 6), []).append((1 - float(m[2]), int(m[1]), float(m[4])))
cf = {}
for line in subprocess.run(["python", "-X", "utf8", "cclosed_3v.py"], capture_output=True, text=True).stdout.splitlines():
    m = re.match(r"s\s+([\d.]+)\s+c ([-+\d.]+)$", line)
    if m:
        cf[float(m[1])] = float(m[2])
for s in sorted(rows):
    r = sorted(rows[s], reverse=True)
    d = np.array([v[0] for v in r])
    c = np.array([v[2] for v in r])
    lin = c[-1] - d[-1] * (c[-2] - c[-1]) / (d[-2] - d[-1]) if len(r) >= 2 else float("nan")
    quad = np.polyfit(d[-3:], c[-3:], 2)[-1] if len(r) >= 3 else float("nan")
    cells = "  ".join("d %.4f (n %d) %+.6f" % v for v in r)
    print("n d %4g: %s  -> d=0 linear %+.4f quad %+.4f | closed form %+.4f" % (s, cells, lin, quad, cf.get(s, float("nan"))))
