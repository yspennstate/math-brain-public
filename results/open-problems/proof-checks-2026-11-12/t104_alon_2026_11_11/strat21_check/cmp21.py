import json, sys
a = json.load(open("replay_summary.json")); b = json.load(open("replay_summary.codex.json"))
def flat(d, p=""):
    out = {}
    if isinstance(d, dict):
        for k, v in d.items(): out.update(flat(v, p + "/" + k))
    elif isinstance(d, list):
        for i, v in enumerate(d): out.update(flat(v, p + "[%d]" % i))
    else: out[p] = d
    return out
fa, fb = flat(a), flat(b)
hk = [k for k in fb if isinstance(fb[k], str) and len(fb[k]) == 64 and all(c in "0123456789abcdef" for c in fb[k])]
same = sum(1 for k in hk if fa.get(k) == fb[k]); diff = [k for k in hk if fa.get(k) != fb[k]]
print("hash fields", len(hk), "equal", same, "differ", len(diff)); print("differ:", diff[:10])
other = [k for k in fb if k not in hk and fa.get(k) != fb[k]]
print("non-hash fields differing:", [(k, fa.get(k), fb[k]) for k in other][:12])
