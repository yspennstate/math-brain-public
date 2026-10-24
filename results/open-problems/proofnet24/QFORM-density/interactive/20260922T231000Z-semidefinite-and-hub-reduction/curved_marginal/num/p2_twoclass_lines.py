# The two-class frame of Example 5.2 of single_hub_core (m = 4, every leverage 1/2, the pair (1,1,1,1)/2,
# (1,1,-1,-1)/2 rotated by tan theta = sqrt 2) with comb laws X_i uniform on N teeth of width 1/N at 0, 1, ..., N-1.
# single_hub_core/num/p2_lattice_output.txt found the curved density well above the flat marginal of U (1.187 against
# 0.478 at N = 4). Here the curved maximum is set against the best line over 360 directions for the same laws.
import sys, math, json
import numpy as np
from p2_adversary import Evaluator
from p2_lines import line_max

def twoclass():
    u0 = np.array([1, 1, 1, 1])/2.0; v0 = np.array([1, 1, -1, -1])/2.0
    th = math.atan(math.sqrt(2.0))
    u = math.cos(th)*u0 + math.sin(th)*v0
    v = -math.sin(th)*u0 + math.cos(th)*v0
    return np.vstack([u, v])

def run(N, G, delta):
    D = twoclass()
    pos = np.array([np.arange(N, dtype=float)]*4)            # tooth left ends 0..N-1
    ev = Evaluator(D, N, G, delta, cs=[], nb=1)
    rho = ev.density(pos)
    d = ev.delta
    ug = ev.x0u + d*np.arange(G); vg = ev.x0v + d*np.arange(G)
    best = (0.0, None)
    vmarg = rho.sum(axis=1); vm = float(np.sum(vmarg*vg)/vmarg.sum())
    vs = float(math.sqrt(np.sum(vmarg*(vg - vm)**2)/vmarg.sum()))
    for c in (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, -0.001, -0.003, -0.01, -0.03, -0.1, -0.3):
        for b in vm + vs*np.linspace(-3, 3, 25):
            acc = np.zeros(G)
            for j in range(G):
                acc += np.interp(ug - c*(vg[j] - b)**2, ug, rho[j], left=0.0, right=0.0)
            val = acc.max()*d
            if val > best[0]:
                best = (float(val), (c, float(b)))
    flatU = float((rho.sum(axis=0)*d).max())
    lm, lt = line_max(rho, ev.x0u, d, ndir=360, x0v=ev.x0v)
    return dict(N=N, curved_max=best[0], at=best[1], flat_U=flatU, line_max=lm, line_dir=lt,
                ratio=best[0]/lm, mass=float(rho.sum()*d*d))

if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    for N, G, delta in ((4, 1024, 0.02), (8, 1024, 0.03), (12, 1536, 0.025)):
        print(json.dumps(run(N, G, delta)), flush=True)
