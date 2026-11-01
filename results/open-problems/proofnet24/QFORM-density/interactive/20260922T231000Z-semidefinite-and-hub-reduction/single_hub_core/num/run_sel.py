import sys, time
import numpy as np
import tlperp_comb as t
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
N = int(sys.argv[1]); qs = [int(a) for a in sys.argv[2].split(',')]
zm, h = 8.0, 0.2
t0 = time.time()
base = t.frame_integral(N, 0.0, t.W, zmax_mult=zm, h=h)
print(f"N={N} zmax={zm*N:g} h={h} J(0)={base:.4f} ({time.time()-t0:.0f}s)", flush=True)
for name, u in (("aligned u=w", t.W), ("orthogonal u=p", t.P)):
    out = []
    for q in qs:
        J = t.frame_integral(N, 4*np.pi/q, u, zmax_mult=zm, h=h)
        out.append(f"q={q}:{J/base:.3f}")
        print(f"  {name} q={q} J/J0={J/base:.3f} ({time.time()-t0:.0f}s)", flush=True)
    print(f"  {name:15s} J/J0: " + "  ".join(out), flush=True)
