# Check the shifted two-dimensional Brascamp-Lieb bound int int prod_i |f^_i(zeta w_i + xi v_i + c_i)| <= (4 pi)^2
# for an orthonormal pair (w, v) with w_i^2 + v_i^2 <= 1/2, comb and uniform laws, and several shifts c.
import numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
rng = np.random.default_rng(7)
def frame(m, tries=100000):
    for _ in range(tries):
        A = rng.normal(size=(m, 2)); Q, _ = np.linalg.qr(A)
        if np.max(Q[:, 0]**2 + Q[:, 1]**2) <= 0.5: return Q[:, 0], Q[:, 1]
    return None
T = np.arange(-400.0, 400.0, 0.002)                     # table of |f^| on a fine grid, interpolated below
def table_uniform(): return np.abs(np.sinc(T/(2*np.pi)))
def table_comb(pos, N):
    D = np.zeros_like(T, dtype=complex)
    for x in pos: D += np.exp(1j*T*x)
    return np.abs(D/len(pos))*np.abs(np.sinc(T/(2*np.pi*N)))
for m in (6, 10, 16):
    fr = frame(m)
    if fr is None: print("m=%d: no frame with leverages <= 1/2 found" % m); continue
    w, v = fr
    for law in ("uniform", "comb"):
        N = 8
        tabs = [table_uniform() if law == "uniform" else
                table_comb(np.sort(rng.choice(20, N, replace=False)).astype(float), N) for _ in range(m)]
        for shift in (0.0, 5.0, 100.0):
            c = shift*rng.normal(size=m)
            h, R = (0.02, 80.0) if law == "uniform" else (0.01, 60.0)
            g = np.arange(-R, R, h); tot = 0.0
            for z in g:
                F = np.ones_like(g)
                for i in range(m):
                    F *= np.interp(z*w[i] + g*v[i] + c[i], T, tabs[i])
                tot += F.sum()*h*h
            print("m=%2d %-7s shift=%5.1f  integral=%8.3f   (4pi)^2=%.1f" % (m, law, shift, tot, (4*np.pi)**2), flush=True)
