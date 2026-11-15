"""Merge fpp row files, dropping exact duplicates (same n, a, W, seed, k and first sample). usage: fpp_merge.py OUT IN1 IN2 ..."""
import json, sys
seen, kept, dup = set(), 0, 0
with open(sys.argv[1], "w") as out:
    for path in sys.argv[2:]:
        for line in open(path):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            key = (r["n"], r["a"], r["W"], r.get("seed"), r.get("k"), round(r["T"][0], 3) if r["T"] else None)
            if key in seen:
                dup += 1
                continue
            seen.add(key)
            out.write(line if line.endswith("\n") else line + "\n")
            kept += 1
print("kept", kept, "duplicates dropped", dup)
