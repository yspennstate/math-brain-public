import numpy as np
from jperp import triple_law, S
N = 4
z, p = triple_law(N)
d = {tuple(int(x) for x in zz): pp for zz, pp in zip(z, p)}
rng = np.random.default_rng(1)
K = rng.integers(0, N, size=(2_000_000, 8))
Z = K @ S
u, c = np.unique(Z, axis=0, return_counts=True)
emp = c / len(Z)
top = np.argsort(-emp)[:6]
print("support: law %d, sampled %d; total prob %.6f" % (len(p), len(u), p.sum()))
for i in top:
    print(tuple(int(x) for x in u[i]), "empirical %.5f  computed %.5f" % (emp[i], d.get(tuple(u[i]), 0.0)))
miss = sum(1 for zz in u if tuple(zz) not in d)
print("sampled triples missing from the law:", miss)
