"""Recompute AB30's published numbers from the rows in this folder: derive.py, then check.py.

    python recompute.py        exit 0 when every published claim matches, 1 otherwise

Kept so the command in README.md still works. The published values are in CLAIMS.json, not in code: derive.py computes
from the rows alone and writes results.json, and check.py compares the two files.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import derive  # noqa: E402
import check  # noqa: E402


def main():
    res = derive.derive()
    out = os.path.join(HERE, "results.json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)
        fh.write("\n")
    claims = json.load(io.open(os.path.join(HERE, "CLAIMS.json"), encoding="utf-8"))
    lines, bad = check.compare(res, claims, os.path.join(HERE, "STATUS.json"))
    print("\n".join(lines))
    print("\nNot recomputable from these rows:")
    for x in res.get("not_recomputable") or ["nothing"]:
        print("  " + x)
    print("\n%s" % ("every claim matches" if not bad else "DIFFERS: " + ", ".join(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
