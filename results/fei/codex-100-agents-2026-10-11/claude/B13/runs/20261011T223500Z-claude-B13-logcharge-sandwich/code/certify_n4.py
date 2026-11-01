# Certify the n<=4 maxima: closed forms for the maximizers (point functions) evaluated with mpmath
# interval arithmetic, and the float gap to the next distinct value (float error budget 1e-11).
import json, sys, numpy as np, mpmath
from mpmath import iv
iv.dps = 40
OUT = sys.argv[1]
r = {}
for name in ("ratio", "minD", "minL"):
    a = np.load(f"{OUT}/n4_{name}.npy")
    vals = np.unique(np.round(a[a > -0.5], 12))
    top, second = vals[-1], vals[-2]
    r[name] = {"float_top": float(top), "float_second_distinct": float(second), "gap": float(top - second),
               "argmax_count": int(np.sum(np.abs(a - top) < 1e-9))}
l3, l7, l10 = iv.log(3, 2), iv.log(7, 2), iv.log(10, 2)
r["closed_forms"] = {
    "C_3 = 16/3 - (3/2)log2 3 (3-bit point function)": str(iv.mpf(16) / 3 - iv.mpf(3) / 2 * l3),
    "C_4 = 12 - (49/16)log2 7 (4-bit point function)": str(12 - iv.mpf(49) / 16 * l7),
    "K_3 = K_4 = 12 - (9/2)log2 3 (3-bit point function, any coordinate)": str(12 - iv.mpf(9) / 2 * l3),
    "KL_3 = KL_4 = (3 + log2 10)/4 (3-bit point function)": str((3 + l10) / 4),
    "C_2 = 2, K_2 = 4, KL_2 = 1 (AND2)": "exact rationals",
}
print(json.dumps(r, indent=1))
json.dump(r, open(f"{OUT}/certify_n4.json", "w"), indent=1)
