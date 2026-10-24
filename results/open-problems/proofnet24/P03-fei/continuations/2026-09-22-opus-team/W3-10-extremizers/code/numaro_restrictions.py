"""(d) prime restrictions of Numaro's g by arity: max J (balanced), max rho_0, max H/I over sampled restrictions,
split prime / composite.  A restriction fixes 18-k coordinates to constants (random free set and values)."""
import sys, time
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, is_prime, compress, relevant
polite()
out = open('../logs/numaro_restrictions.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
g = np.load('../../inputs/numaro18_pm1_table.npy').astype(np.int8)
n = 18
rng = np.random.default_rng(777)
x_all = np.arange(1 << n)
def restrict(free, fixed_vals):
    k = len(free)
    y = np.arange(1 << k)
    x = np.zeros(1 << k, dtype=np.int64)
    for j, i in enumerate(free):
        x |= ((y >> j) & 1) << i
    x |= fixed_vals
    return g[x]
best = {}
t0 = time.time()
for k in range(3, 13):
    nsamp = 6000 if k <= 8 else 2500
    rec = {('J', 1): -1, ('J', 0): -1, ('rho', 1): -1, ('rho', 0): -1, ('ratio', 1): -1, ('ratio', 0): -1}
    nbal = 0; nprime = 0; ntot = 0
    seen = set()
    for s in range(nsamp):
        # bias the free set toward core coordinates half the time
        if rng.random() < 0.5:
            free = sorted(rng.choice(18, size=k, replace=False).tolist())
        else:
            ncore = min(9, max(0, k - int(rng.integers(0, min(k, 9) + 1))))
            ncore = min(ncore, k)
            core = rng.choice(9, size=ncore, replace=False).tolist()
            aux = rng.choice(np.arange(9, 18), size=k - ncore, replace=False).tolist() if k - ncore <= 9 else None
            if aux is None: continue
            free = sorted(core + aux)
        fixed = [i for i in range(18) if i not in free]
        vals = 0
        for i in fixed:
            if rng.random() < 0.5: vals |= 1 << i
        t = restrict(free, vals)
        key = t.tobytes()
        if key in seen: continue
        seen.add(key)
        if len(relevant(t)) < k: continue
        ntot += 1
        st = stats(t)
        pr = int(is_prime(t))
        nprime += pr
        if abs(st['mean']) < 1e-12 and st['I'] > 1 + 1e-9:
            nbal += 1
            rec[('J', pr)] = max(rec[('J', pr)], st['H'] / (st['I'] - 1))
        rec[('rho', pr)] = max(rec[('rho', pr)], st['rho0'])
        rec[('ratio', pr)] = max(rec[('ratio', pr)], st['ratio'])
    log('arity %2d: %5d distinct full-support restrictions (%d prime, %d balanced) | max J prime %.5f comp %.5f | max rho0 prime %.5f comp %.5f | max H/I prime %.5f comp %.5f  [%.0fs]' % (
        k, ntot, nprime, nbal, rec[('J', 1)], rec[('J', 0)], rec[('rho', 1)], rec[('rho', 0)], rec[('ratio', 1)], rec[('ratio', 0)], time.time() - t0))
