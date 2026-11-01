# For every frame on which p2_adversary.py / p2_ratio.py found a comb law, compare the curved marginal of the law found
# with that of plain interval laws (each X_i uniform on [0, 1]) on the same frame. For interval laws the offsets only
# translate (U, V), which moves s and the vertex b, so one evaluation per frame covers every interval law.
# The conjecture that intervals are extremal predicts that the interval value is at least the value found.
import sys, json, math
import numpy as np
from p2_adversary import Evaluator
from p2_lines import line_max

CS = (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0)

def curved_max(rho, ev, G, d, nb=41):
    ug = ev.x0u + d*np.arange(G); vg = ev.x0v + d*np.arange(G)
    vmarg = rho.sum(axis=1); vm = float(np.sum(vmarg*vg)/vmarg.sum())
    vs = float(math.sqrt(np.sum(vmarg*(vg - vm)**2)/vmarg.sum()))
    best = (0.0, None)
    for c in list(CS) + [-c for c in CS]:
        for b in vm + vs*np.linspace(-4, 4, nb):
            acc = np.zeros(G)
            for j in range(G):
                acc += np.interp(ug - c*(vg[j] - b)**2, ug, rho[j], left=0.0, right=0.0)
            val = acc.max()*d
            if val > best[0]:
                best = (float(val), (c, float(b)))
    return best

if __name__ == "__main__":
    try:
        import psutil, os
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        psutil.Process().cpu_affinity(list(range(2, os.cpu_count())))
    except Exception:
        pass
    for fn in sys.argv[1:]:
        for line in open(fn, encoding='utf-8'):
            if not line.strip():
                continue
            r = json.loads(line)
            D = np.array(r['frame']); m = D.shape[1]
            G, d = 512, 0.02
            ev = Evaluator(D, 1, G, d, cs=[], nb=1)
            rho = ev.density(np.zeros((m, 1)))
            cm, arg = curved_max(rho, ev, G, d)
            lm, lt = line_max(rho, ev.x0u, d, ndir=360, x0v=ev.x0v)
            print(json.dumps(dict(file=fn, m=m, seed=r['seed'], found_F=r['F'], found_arg=r['arg'],
                                  interval_curved=cm, interval_arg=arg, interval_line=lm,
                                  interval_ratio=cm/lm, mass=float(rho.sum()*d*d))), flush=True)
