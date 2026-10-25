"""Print every arm of eval_lambda.json against lambda 0 and check that no blend beats it on hit@1 by more than one item or on MRR."""
import json, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "eval_lambda.json"), encoding="utf-8"))
best = None
for arm, res in d["arms"].items():
    p = res["pilot"]
    base = p["convex_0.00"]
    for k, v in p.items():
        if not isinstance(v, dict) or k.endswith("_0.00"):
            continue
        if best is None or v["mrr"] > best[2]["mrr"]:
            best = (arm, k, v)
print("lambda 0: hit@1", base["hit1"], "hit@5", base["hit5"], "hit@10", base["hit10"], "MRR", base["mrr"])
a, k, v = best
print(f"best blend by MRR: {a} {k}: hit@1 {v['hit1']} hit@5 {v['hit5']} hit@10 {v['hit10']} MRR {v['mrr']}, "
      f"{v['better']} answers up / {v['worse']} down")
print("no blend beats lambda 0" if v["mrr"] <= base["mrr"] + 0.001 else "A BLEND BEATS LAMBDA 0")
