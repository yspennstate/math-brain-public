# Independent check of a consequence of A063's coarsening bound 0 <= R <= (B-J)/2 for singleton blocks:
# J_i <= B_i for every coordinate of every Boolean function on n<=4 variables
# (J_i = JS divergence of the two child spectra, B_i = H(S_i | S_-i)).
import sys, json, numpy as np
sys.argv = [sys.argv[0], sys.argv[1]]
sys.path.insert(0, "code")
import sandwich_all as sa
out = {}
for m in range(1, 5):
    r = sa.analyze(m)
    worst = -1e9; arg = None; ratio_max = 0.0
    for j, q in enumerate(r["per"]):
        diff = q["J"] - q["B"]
        k = int(np.argmax(diff))
        if diff[k] > worst:
            worst, arg = float(diff[k]), (int(r["T"][k]), j)
        with np.errstate(divide="ignore", invalid="ignore"):
            rr = np.where(q["B"] > 1e-12, q["J"] / np.where(q["B"] > 1e-12, q["B"], 1), 0)
        ratio_max = max(ratio_max, float(rr.max()))
    out[f"n={m}"] = {"max_(g,i) (J_i - B_i)": worst, "at (truth table, coord)": arg, "max J_i/B_i": ratio_max}
print(json.dumps(out, indent=1))
json.dump(out, open("out/check_JB.json", "w"), indent=1)
