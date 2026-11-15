"""gen_lib6.py - one representative of every class of monotone functions on n inputs (default 6) that can be told
apart by (G_p, J_p, Pr_p) at two generic biases; functions that differ by a permutation of the inputs coincide there.
usage: python gen_lib6.py [n] > lib6.txt      lines: n hex
"""
import sys

import numpy as np

from tower_vi import monotone_tables, stats_grid


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    tabs = [x for x in monotone_tables(n) if x not in (0, (1 << (1 << n)) - 1)]
    sys.stderr.write("monotone tables: %d\n" % len(tabs))
    seen = {}
    ps = [0.3711, 0.6127]
    step = 40000
    N = 1 << n
    for lo in range(0, len(tabs), step):
        chunk = tabs[lo:lo + step]
        arr = np.array(chunk, dtype=np.uint64)
        b = ((arr[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(np.uint8)
        G, J, P = stats_grid(b, n, ps)
        key = np.round(np.hstack([G, np.where(np.isfinite(J), J, 0.0), P]) * 1e9).astype(np.int64)
        for r in range(len(chunk)):
            kk = key[r].tobytes()
            if kk not in seen:
                seen[kk] = chunk[r]
    sys.stderr.write("classes: %d\n" % len(seen))
    for tb in seen.values():
        print(n, "%x" % tb)


if __name__ == "__main__":
    main()
