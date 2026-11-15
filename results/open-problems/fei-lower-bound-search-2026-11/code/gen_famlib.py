"""gen_famlib.py - turn the main campaign's families.json (structured seeds, truth tables as hex) into a tower library.
usage: python gen_famlib.py PATH/families.json OUT.txt [maxn]
Writes lines "n hex" (the format tower_vi.py --libfile reads) and OUT.txt.names with "index n name H I mean H/(I-1)".
Only entries with a table on 7 <= n <= maxn inputs are kept (smaller ones are already in the exhaustive library).
"""
import json
import sys

import numpy as np

from bias_check import uniform_HI


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 18
    out = open(sys.argv[2], "w", encoding="utf-8")
    names = open(sys.argv[2] + ".names", "w", encoding="utf-8")
    seen = set()
    kept = 0
    for idx, e in enumerate(data):
        if not isinstance(e, dict):
            continue
        hx = e.get("tt_hex")
        if not isinstance(hx, str):
            continue
        n = (4 * len(hx)).bit_length() - 1
        if 4 * len(hx) != 1 << n or n < 7 or n > maxn:
            continue
        tab = int(hx, 16)
        if (n, tab) in seen:
            continue
        seen.add((n, tab))
        vals = np.array([1.0 - 2.0 * ((tab >> x) & 1) for x in range(1 << n)]) if n <= 16 else None
        if vals is None:
            bits = np.unpackbits(np.frombuffer(tab.to_bytes((1 << n) // 8, "little"), dtype=np.uint8), bitorder="little")
            vals = 1.0 - 2.0 * bits.astype(np.float64)
        H, I, m = uniform_HI(vals)
        name = str(e.get("name", e.get("family", idx)))
        sc = H / (I - 1) if abs(m) < 1e-12 and I > 1 else float("nan")
        out.write("%d %x\n" % (n, tab))
        names.write("%d %d %s H=%.9f I=%.9f mean=%.6f bal=%.9f HI=%.9f\n" % (kept, n, name, H, I, m, sc, H / I))
        kept += 1
    out.close()
    names.close()
    print("entries", len(data), "kept", kept)


if __name__ == "__main__":
    main()
