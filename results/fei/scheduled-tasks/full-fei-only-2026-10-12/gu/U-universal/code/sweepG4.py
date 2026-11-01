import numpy as np, json, time
from sweepG import evalf, compose
g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
def andk(k): return np.array([-1 if x == (1 << k) - 1 else 1 for x in range(1 << k)])
def ork(k): return np.array([1 if x == 0 else -1 for x in range(1 << k)])
maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
xor2 = np.array([1, -1, -1, 1])
t0 = time.time()
cases = {}
# alternating AND/OR trees of fan-in 2, depth d (n = 2^d)
f = np.array([1, -1]) # dictator on 1 bit: index bit=1 -> -1
cur = f; nb = 1
for d in range(1, 5):
    gate = andk(2) if d % 2 == 1 else ork(2)
    cur = compose(gate, 2, cur, nb); nb *= 2
    cases[f'ANDOR depth{d}'] = cur
# fan-in 3 alternating, depth 2 (n=9) and AND3 o OR3 o x
a3o3 = compose(andk(3), 3, ork(3), 3); cases['AND3 o OR3'] = a3o3
cases['OR3 o AND3'] = compose(ork(3), 3, andk(3), 3)
cases['AND2 o OR2 o g5'] = compose(andk(2), 2, compose(ork(2), 2, g5, 5), 10)
cases['maj3 o AND2 o x'] = compose(maj3, 3, andk(2), 2)
cases['maj3 o maj3 o AND2'] = compose(maj3, 3, compose(maj3, 3, andk(2), 2), 6)
for k, t in cases.items():
    r = evalf(t); print(f"{k:20s} n={r['n']:2d} G/I={r['GI']:.3f} U/I={r['UI']:.3f} H/I={r['HI']:.3f} minloc={r['minloc']:.3f} maxloc={r['maxloc']:.3f} ({time.time()-t0:.0f}s)", flush=True)
