"""P0290: targeted search for a doubly monotone (non-reversible) chain and a Boolean f whose light-traffic
coefficient J_f(c) RISES somewhere (which would refute Leskela's Problem 2 for Boolean images via the uniform
light-traffic expansion).  Hill-climb over 4- and 5-state generators inside the doubly-monotone cone, objective =
max over Boolean f of the largest rise of J_f on a c-grid; secondary report: largest rise of the autocovariance R_f
itself, verified by expm at the two times.
"""
import itertools
import numpy as np
from scipy.linalg import expm
from p0290_boolean_image_search import stationary, doubly_monotone, is_reversible, J_curve, max_rise
from p0290_general_f_search import R_curve

def objective(Q, fs, cs):
    best = 0.0; arg = None
    for f in fs:
        J, a = J_curve(Q, f, cs); r, ar = max_rise(J)
        if r > best: best, arg = r, (f, ar)
    return best, arg

def make_Q(x, m):
    Q = np.abs(x.reshape(m, m)); np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1)); return Q

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(5)
    cs = np.exp(np.linspace(np.log(0.05), np.log(80), 90)); ts = np.linspace(0, 10, 500)
    for m in (4, 5):
        fs = [np.array(b, float) for b in itertools.product([0, 1], repeat=m) if 0 < sum(b) < m]
        bestJ = 0.0; bestR = 0.0; witR = None; witJ = None
        for restart in range(12 if m == 4 else 8):
            # feasible start: sample until doubly monotone
            for _ in range(4000):
                x = rng.uniform(0.05, 2.0, m*m)
                Q = make_Q(x, m)
                if doubly_monotone(Q): break
            else:
                continue
            cur, _ = objective(Q, fs, cs)
            for it in range(150):
                y = x * np.exp(rng.normal(0, 0.25, m*m))
                Qy = make_Q(y, m)
                if not doubly_monotone(Qy): continue
                val, arg = objective(Qy, fs, cs)
                # secondary: R rise
                for f in fs:
                    R, A, lam = R_curve(Qy, f, ts); rr, arR = max_rise(R)
                    if rr > bestR: bestR = rr; witR = (Qy.copy(), f.copy(), ts[arR[0]], ts[arR[1]])
                if val >= cur:
                    x, Q, cur = y, Qy, val
                    if val > bestJ: bestJ = val; witJ = (Qy.copy(), arg[0].copy(), cs[arg[1][0]], cs[arg[1][1]])
            print(f"m={m} restart {restart}: local best J-rise {cur:.3e}; global best J-rise {bestJ:.3e}; best R-rise {bestR:.3e}", flush=True)
        if witR is not None:
            Q, f, t1, t2 = witR; pi = stationary(Q)
            r1 = f @ (pi * (expm(Q*t1) @ f)); r2 = f @ (pi * (expm(Q*t2) @ f))
            print(f"m={m} R-rise witness verified by expm: R({t1:.3f})={r1:.6f} -> R({t2:.3f})={r2:.6f} (rise {r2-r1:+.3e}); f={f}; reversible={is_reversible(Q)}; eigs={np.round(np.linalg.eigvals(Q),3)}")
            print("  Q=\n", np.round(Q, 4))
        if witJ is not None:
            Q, f, c1, c2 = witJ
            print(f"m={m} J-RISE WITNESS: f={f}, c1={c1:.3f} -> c2={c2:.3f}, rise {bestJ:.3e}; eigs={np.round(np.linalg.eigvals(Q),3)}\n  Q=\n", np.round(Q, 4))
