"""Compare Codex's STRAT19 replay_summary.json with my fresh replay's: every hash field must agree, every stage PASS."""
import json, sys

def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, path + "[%d]" % i)
    else:
        yield path, o

a = dict(walk(json.load(open(sys.argv[1], encoding="utf-8"))))
b = dict(walk(json.load(open(sys.argv[2], encoding="utf-8"))))
hk = [k for k in a if "sha" in k.lower() or "hash" in k.lower()]
hk += [k for k, v in a.items() if isinstance(v, str) and len(v) == 64 and all(c in "0123456789abcdef" for c in v) and k not in hk]
same = sum(1 for k in hk if a.get(k) == b.get(k))
diff = [k for k in hk if a.get(k) != b.get(k)]
print("hash fields", len(hk), "equal", same)
for k in diff[:20]:
    print("DIFF", k, a.get(k), b.get(k))
st = [(k, v) for k, v in b.items() if isinstance(v, str) and v in ("PASS", "FAIL")]
print("my replay stage statuses: PASS", sum(v == "PASS" for _, v in st), "FAIL", sum(v == "FAIL" for _, v in st))
print("keys only in one:", sorted(set(a) ^ set(b))[:10])
