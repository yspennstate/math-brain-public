try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time
from scipy.integrate import quad
# constants
f = lambda mu: min(np.pi, 8*mu**-2*(6.2 + max(0.0, np.log(16*mu*mu)))) if mu > 0 else np.pi
C_ind = quad(f, 0, 1, limit=200)[0] + quad(f, 1, np.inf, limit=200)[0]
C_def = 2*np.pi*np.sqrt(2)
C_ball = 3/(4*np.pi)*max(C_ind, C_def)
C_CG = 3*(4*np.pi/3)**(2/3)*C_ball
print(f"C_ind={C_ind:.3f} C_def={C_def:.3f} C_ball={C_ball:.3f} C_CG={C_CG:.3f}", flush=True)
# numerical check: X uniform on unit ball, P = sum m_k (x_k - c_k)^2; max_s p(s) * |det|^{1/3}
rng = np.random.default_rng(3)
def ball(N):
    g = rng.normal(size=(N,3)); g /= np.linalg.norm(g, axis=1)[:,None]
    return g * rng.random(N)[:,None]**(1/3)
X = ball(3_000_000)
worst = 0
T0 = time.time()
cases = []
for sig in [(1,1,1),(1,1,-1)]:
    for logs in [(0,0,0),(2,0,-2),(3,-1.5,-1.5),(-2,1,1),(4,0,-4),(1,1,-2),(0,-3,3)]:
        cases.append((sig, logs))
for (sig, logs) in cases:
    m = np.array(sig)*np.exp(np.array(logs))
    for trial in range(4):
        c = rng.normal(scale=[0.0,0.4,0.9,1.5][trial], size=3)
        P = ((X - c)**2 * m).sum(1)
        # adaptive histogram: bin width relative to spread, refined around the max
        lo, hi = np.quantile(P, [0.0005, 0.9995])
        w = (hi-lo)/4000
        h, e = np.histogram(P, bins=np.arange(lo, hi+w, w))
        k = np.argmax(h); pk = h[k]/len(P)/w
        # refine: window test with smaller bins around the peak
        cen = (e[k]+e[k+1])/2
        best = pk
        for ww in [w/4, w/16]:
            best = max(best, np.mean(np.abs(P-cen) < ww/2)/ww)
        val = best*np.prod(np.abs(m))**(1/3)
        worst = max(worst, val)
        cases_line = f"sig={sig} logm={logs} c={np.round(c,2)}  max p={best:.4f}  p*|det|^(1/3)={val:.4f}"
        if trial == 3 or val > 1.5: print(cases_line, flush=True)
print("worst p*|det|^{1/3} =", worst, " bound C_ball =", C_ball, " time", time.time()-T0, flush=True)
