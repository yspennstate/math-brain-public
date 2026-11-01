"""Scan kn_gibbs over n, q, n*lambda; one JSON line per point to kn_scan_<n>.jsonl."""
import sys, json
from mpmath import mpf
from kn_gibbs import run
n = int(sys.argv[1])
with open(f"kn_scan_{n}.jsonl", "w") as out:
    for q in ["0.3", "0.5", "0.618", "0.9"]:
        for nl in ["0.25", "0.5", "1", "2", "3", "4", "6", "8", "12", "16", "32"]:
            out.write(json.dumps(run(n, q, mpf(nl) / n)) + "\n"); out.flush()
