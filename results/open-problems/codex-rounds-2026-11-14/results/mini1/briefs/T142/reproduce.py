#!/usr/bin/env python3
"""Rebuild, enumerate sequentially, and audit; each child has a wall deadline."""
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "launch under nice -n 15"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

subprocess.run(["clang", "-std=c11", "-O3", "-Wall", "-Wextra", "-Wconversion",
                "exact_lcs.c", "-o", "exact_lcs"], check=True, timeout=120)
for method in ("bits", "dp"):
    with open(f"results_{method}.jsonl", "w") as data, open(f"run_{method}.txt", "w") as log:
        subprocess.run(["./exact_lcs", method, "12"], stdout=data, stderr=log,
                       check=True, timeout=1100)
with open("audit.txt", "w") as output:
    subprocess.run([sys.executable, "audit.py"], stdout=output, check=True, timeout=120)
print((ROOT / "audit.txt").read_text(), end="")
