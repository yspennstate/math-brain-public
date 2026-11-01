import numpy as np, json, time
from sweepG import evalf, compose
g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
def andk(k): return np.array([-1 if x == (1 << k) - 1 else 1 for x in range(1 << k)])
def ork(k): return np.array([1 if x == 0 else -1 for x in range(1 << k)])
maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)])
sel = np.array([ (1-2*((x>>1)&1)) if (x&1)==0 else (1-2*((x>>2)&1)) for x in range(8)])  # addressing a=1
t0 = time.time()
cases = {'and3 o g5': compose(andk(3), 3, g5, 5), 'or3 o g5': compose(ork(3), 3, g5, 5), 'and4 o g5': compose(andk(4), 4, g5, 5),
         'sel o g5': compose(sel, 3, g5, 5), 'g5 o and3': compose(g5, 5, andk(3), 3), 'g5 o and4': compose(g5, 5, andk(4), 4)}
for k, t in cases.items():
    r = evalf(t); print(f"{k:12s} n={r['n']:2d} G/I={r['GI']:.3f} U/I={r['UI']:.3f} H/I={r['HI']:.3f} minloc={r['minloc']:.3f} maxloc={r['maxloc']:.3f} ({time.time()-t0:.0f}s)", flush=True)
