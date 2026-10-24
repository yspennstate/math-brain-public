# Independent float check: scan t over the full period [0, pi) (no symmetry reduction) and p over (0, 1)
# including both sides of 1/2 and the seams; report min over t of F(t) - R(p) with R(p) = h2(p) - Delta(p)/2.
import numpy as np, json, sys
def h2(x):
    x = np.clip(x, 1e-300, 1-1e-16); return -(x*np.log2(x) + (1-x)*np.log2(1-x))
t = np.linspace(0, np.pi, 200001)[:-1]
ps = sorted(set(list(np.geomspace(1e-6, 0.5, 300)) + [0.0799, 0.08, 0.0816, 0.0817, 0.4899, 0.49, 0.4901, 0.4999, 0.5]
                + list(1 - np.geomspace(1e-6, 0.5, 120))))
worst = []
for p in ps:
    b = np.arcsin(np.sqrt(p))            # actual bias p, no reduction to min(p,1-p)
    F = h2(np.sin(t)**2) + h2(np.sin(t - b)**2)
    pb = min(p, 1-p); Delta = pb*np.log2((1-pb)/pb) if pb < 0.5 else 0.0
    Rp = h2(np.array([p]))[0] - Delta/2
    worst.append((float(F.min() - Rp), float(p), float(Delta/2)))
worst.sort()
out = {"n_p": len(ps), "n_t": len(t), "five_smallest_margins(min F - R, p, Delta/2)": worst[:5],
       "negative_count": sum(1 for w in worst if w[0] < -1e-12)}
json.dump(out, open(sys.argv[1], "w"), indent=1); print(json.dumps(out, indent=1))
