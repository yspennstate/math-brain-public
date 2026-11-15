#!/usr/bin/env python3
"""Extend the same certificate computation to K_5,5 using a partition transfer."""
from collections import defaultdict
from functools import lru_cache
import json
import os
from pathlib import Path
import resource
import signal
import time

from check_bipartite import (add, mul, shift, independent_sectors,
                            uniform_counts, divide_one_minus_q, transform, serial)


@lru_cache(None)
def transition(partition, subset):
    """Left blocks intersecting the neighbor subset merge through the new vertex."""
    if not subset:
        return partition
    merged = 0
    untouched = []
    for block in partition:
        if block & subset:
            merged |= block
        else:
            untouched.append(block)
    return tuple(sorted(untouched+[merged]))


def transfer_sectors(m, n, e, f):
    # State: (partition of left vertices, marked-edge bits, isolated right count,
    #         selected unmarked edge count).
    dp = {(tuple(1 << i for i in range(m)), 0, 0, 0): 1}
    for right in range(n):
        choices = []
        for subset in range(1 << m):
            state, marked_count = 0, 0
            for bit, (left, col) in enumerate((e, f)):
                if col == right and subset & (1 << left):
                    state |= 1 << bit
                    marked_count += 1
            choices.append((subset, state, subset.bit_count()-marked_count))
        out = defaultdict(int)
        for (part, state, isolated, degree), count in dp.items():
            for subset, extra, weight_degree in choices:
                key = (transition(part, subset), state | extra,
                       isolated+int(subset == 0), degree+weight_degree)
                out[key] += count
        dp = out
    sectors = [defaultdict(int) for _ in range(4)]
    for (part, state, isolated, degree), count in dp.items():
        sectors[state][len(part)+isolated, degree] += count
    return [dict(p) for p in sectors]


def main():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(1100)
    print("nice_priority", os.getpriority(os.PRIO_PROCESS, 0), flush=True)
    start = time.monotonic()
    rows = json.loads(Path("certificates.json").read_text())
    # Audit the new method against all previously independently verified cases.
    for row in rows:
        m, n, name = row["m"], row["n"], row["orbit"]
        assert m*n <= 16
        f = {"same_left": (0,1), "same_right": (1,0), "disjoint": (1,1)}[name]
        sectors = transfer_sectors(m, n, (0,0), f)
        edges = [(i,m+j) for i in range(m) for j in range(n)]
        index = f[0]*n+f[1]
        assert sectors == independent_sectors(m+n, edges, 0, index)
        print("TRANSFER_BASELINE", m, n, name, "agreement=True", flush=True)
    # Only this fixed new graph is allowed; no large-graph argument is accepted.
    m, n = 5, 5
    for name, f in [("same_left",(0,1)),("same_right",(1,0)),("disjoint",(1,1))]:
        sectors = transfer_sectors(m, n, (0,0), f)
        edges = [(i,m+j) for i in range(m) for j in range(n)]
        other = independent_sectors(m+n, edges, 0, f[0]*n+f[1])
        assert sectors == other, (name, "transfer/vertex decomposition mismatch")
        a, b, c, d = sectors
        rayleigh = add(mul(b,c), mul(a,d), -1)
        qmin = min(i for i,j in rayleigh)
        wmin = min(j for i,j in rayleigh)
        reduced = divide_one_minus_q(shift(rayleigh, di=-qmin, dj=-wmin))
        cert, degree = transform(reduced)
        assert cert and all(v > 0 for v in cert.values())
        row = {"m": m, "n": n, "orbit": name,
               "forest": uniform_counts(sectors, m+n, True),
               "connected": uniform_counts(sectors, m+n, False),
               "q_power": qmin, "w_power": wmin, "reduced": serial(reduced),
               "sectors": [serial(p) for p in sectors],
               "certificates": [{"offset": 0, "degree": degree,
                   "terms": len(cert), "negative_terms": 0,
                   "minimum": min(cert.values()), "polynomial": serial(cert)}]}
        rows.append(row)
        print("EXTENDED", m, n, name, "q_power", qmin, "w_power", wmin,
              "degree", degree, "terms", len(cert), "minimum", min(cert.values()),
              "forest", row["forest"], "connected", row["connected"], flush=True)
    Path("extended_certificates.json").write_text(json.dumps(rows, indent=2)+"\n")
    print("elapsed_seconds", round(time.monotonic()-start, 3), flush=True)
    print("peak_rss_bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, flush=True)


if __name__ == "__main__":
    main()
