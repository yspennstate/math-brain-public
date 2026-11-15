"""extract_record.py - pull the 18-variable record seed (PM(K33) with nine coins) out of the main campaign's
families.json, check its balanced tower score H/(I-1), and write it as a library line "18 hex".
usage: python extract_record.py PATH/families.json OUT.txt
"""
import json
import sys

import numpy as np

from bias_check import uniform_HI


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    hits = [e for e in data if isinstance(e, dict) and "coin" in json.dumps({k: v for k, v in e.items() if not isinstance(v, (list, str)) or len(v) < 200}).lower()]
    print("entries", len(data), "with 'coin':", len(hits))
    for e in hits:
        print({k: (v if not isinstance(v, (list, str)) or len(v) < 80 else "<%s len %d>" % (type(v).__name__, len(v))) for k, v in e.items()})
    for e in hits:
        for k, v in e.items():
            tab = None
            if isinstance(v, str) and len(v) == (1 << 18) // 4:
                tab = int(v, 16)
            elif isinstance(v, str) and len(v) == 1 << 18 and set(v) <= set("01"):
                tab = int(v[::-1], 2)
            elif isinstance(v, list) and len(v) == 1 << 18:
                tab = sum(1 << x for x, b in enumerate(v) if b in (1, -1, True) and (b == 1 if set(v) <= {0, 1} else b == -1))
            if tab is None:
                continue
            vals = np.array([1.0 - 2.0 * ((tab >> x) & 1) for x in range(1 << 18)])
            H, I, m = uniform_HI(vals)
            print("field", k, "H=%.12f I=%.12f mean=%.6f H/(I-1)=%.12f" % (H, I, m, H / (I - 1)))
            if abs(m) < 1e-12:
                with open(sys.argv[2], "w", encoding="utf-8") as fh:
                    fh.write("18 %x\n" % tab)
                print("written", sys.argv[2])
                return


if __name__ == "__main__":
    main()
