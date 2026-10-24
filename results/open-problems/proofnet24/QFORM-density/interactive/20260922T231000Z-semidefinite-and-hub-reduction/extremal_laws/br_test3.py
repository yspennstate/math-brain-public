"""For n = 3: best interval configuration sup_{b,s} p (centred unit intervals, arbitrary b), then the
best-response functions g_i on a wide grid and the top measure-one set.  usage: python br_test3.py NAME"""
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time, sys
from scipy.optimize import minimize
from q3tools import Law, density, g_partial, top_set

U = [Law([-0.5],[0.5]) for _ in range(3)]
def mats():
    e = np.ones(3)/np.sqrt(3)
    d = {"I-2ee": np.eye(3) - 2*np.outer(e,e),
         "exa": np.array([[.5,.5,1/np.sqrt(2)],[.5,.5,-1/np.sqrt(2)],[1/np.sqrt(2),-1/np.sqrt(2),0]]),
         "2I-J": 2*np.eye(3) - np.ones((3,3)),
         "mJI": -(np.ones((3,3)) - np.eye(3)),
         "d11m1": np.diag([1.,1.,-1.]),
         "d41m1": np.diag([4.,1.,-1.])}
    rng = np.random.default_rng(11)
    for k in range(6):
        M = rng.normal(size=(3,3)); M = (M+M.T)/2
        w = np.linalg.eigvalsh(M); d["rand%d"%k] = M/np.min(np.abs(w))
    return d

name = sys.argv[1]; A = mats()[name]
T0 = time.time(); budget = 420
rng = np.random.default_rng(5)
best = None
for k in range(4):
    p0 = np.zeros(4) if k == 0 else np.concatenate([rng.normal(scale=1.0, size=3), [rng.normal(scale=0.5)]])
    r = minimize(lambda p: -density(A, p[:3], p[3], U, m_per_unit=90), p0, method='Nelder-Mead',
                 options=dict(xatol=1e-3, fatol=1e-5, maxiter=250))
    if best is None or r.fun < best.fun: best = r
    print(f"  start {k}: {-r.fun:.4f} at {np.round(r.x,3)}  t={time.time()-T0:.0f}s", flush=True)
    if time.time() - T0 > budget*0.6: break
r = minimize(lambda p: -density(A, p[:3], p[3], U, m_per_unit=220), best.x, method='Nelder-Mead',
             options=dict(xatol=1e-4, fatol=1e-6, maxiter=120))
b, s = r.x[:3], r.x[3]; val = -r.fun
print(f"{name}: eig={np.round(np.linalg.eigvalsh(A),3)} interval-opt p*={val:.4f} b={np.round(b,3)} s={s:.4f} t={time.time()-T0:.0f}s", flush=True)
grid = np.arange(-4, 4, 1/100) + 1/200
for i in range(3):
    g = g_partial(A, b, s, i, U, grid, m_per_unit=250, eta=0.004)
    tv, ivs = top_set(g, grid, 1/100)
    inside = np.abs(grid) < 0.5
    print(f"   coord {i}: top-set value {tv:.4f} (interval value {np.sum(g[inside])/100:.4f}); set = " +
          ", ".join("[%.2f,%.2f]" % iv for iv in ivs), flush=True)
    np.save(f"g_{name}_{i}.npy", np.vstack([grid, g]))
print("done", time.time()-T0, flush=True)
