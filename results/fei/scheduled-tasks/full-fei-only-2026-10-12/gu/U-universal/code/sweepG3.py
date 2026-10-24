import numpy as np, json, time
from sweepG import evalf, compose
from feilib import nbits
g5 = np.array(json.load(open("../data/anneal_G.json"))["5"]["table"])
def activate(g, r):
    n_g = nbits(len(g)); n = n_g + r; N = 1 << n; xs = np.arange(N)
    gx = g[xs & ((1 << n_g) - 1)]; z = xs >> n_g
    return np.where(z == 0, gx, 1)
def parity_lift(g):
    n_g = nbits(len(g)); n = n_g + 1; N = 1 << n; xs = np.arange(N); z = (xs >> n_g) & 1
    x = xs & ((1 << n_g) - 1)
    xz = np.where(z == 1, x ^ ((1 << n_g) - 1), x)   # x_i z: flipping all bits when z=-1
    return g[xz]
def balance(g):  # g (x) dictator on a fresh bit -> balanced
    n_g = nbits(len(g)); N = 1 << (n_g + 1); xs = np.arange(N)
    return np.where((xs >> n_g) & 1, -g[xs & ((1 << n_g) - 1)], g[xs & ((1 << n_g) - 1)])
t0 = time.time()
cases = {'g5 parity lift': parity_lift(g5)}
gb = balance(g5)
for r in [1, 2, 4, 6, 8]: cases[f'activate(g5*x, r={r})'] = activate(gb, r)
for r in [2, 4, 6]: cases[f'activate(g5, r={r})'] = activate(g5, r)
for k, t in cases.items():
    res = evalf(t); print(f"{k:24s} n={res['n']:2d} G/I={res['GI']:.3f} U/I={res['UI']:.3f} H/I={res['HI']:.3f} minloc={res['minloc']:.3f} maxloc={res['maxloc']:.3f} ({time.time()-t0:.0f}s)", flush=True)
