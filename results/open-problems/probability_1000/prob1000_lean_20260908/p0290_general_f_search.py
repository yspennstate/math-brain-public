"""P0290 follow-up: on doubly monotone non-reversible chains, (a) are the eigenvalues ever complex? (b) is there ANY
nonnegative f whose autocovariance R_f(t) = E f(X_0) f(X_t) is non-monotone in t, or whose J_f(c) rises?
Search: random doubly monotone non-reversible generators (3, 4, 5 states) x random nonnegative f (plus all Boolean f);
R_f checked on a t-grid, J_f on a c-grid.  Also computes, for each chain, the min over unit f of the smallest
eigenvalue-weight sign structure: R_f(t) = sum_l A_l(f) e^{lambda_l t}; a rise needs some A_l(f) < 0.
"""
import itertools
import numpy as np
from p0290_boolean_image_search import stationary, doubly_monotone, is_reversible, random_dm_chain, J_curve, max_rise

def R_curve(Q, f, ts):
    pi = stationary(Q); lam, V = np.linalg.eig(Q); Vi = np.linalg.inv(V)
    A = ((pi * f) @ V) * (Vi @ f)
    return np.array([np.real(np.sum(A * np.exp(lam * t))) for t in ts]), A, lam

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(11)
    ts = np.linspace(0, 8, 400); cs = np.exp(np.linspace(np.log(0.05), np.log(60), 100))
    for m in (3, 4, 5):
        n_complex = 0; n_chain = 0; worst_R = 0.0; worst_J = 0.0; worst_case = None
        for trial in range(40):
            Q = random_dm_chain(rng, m)
            if Q is None: continue
            n_chain += 1
            lam = np.linalg.eigvals(Q)
            if np.max(abs(lam.imag)) > 1e-9: n_complex += 1
            fs = [np.array(b, float) for b in itertools.product([0, 1], repeat=m) if 0 < sum(b) < m]
            fs += [rng.uniform(0, 1, m) for _ in range(30)]
            for f in fs:
                R, A, lam = R_curve(Q, f, ts); riseR, _ = max_rise(R)
                J, a = J_curve(Q, f, cs); riseJ, _ = max_rise(J)
                if riseR > worst_R: worst_R = riseR
                if riseJ > worst_J: worst_J = riseJ; worst_case = (Q.copy(), f.copy())
        print(f"m={m}: chains={n_chain}, with complex eigenvalues={n_complex}; max rise of R_f over all f = {worst_R:.3e}; max rise of J_f = {worst_J:.3e}", flush=True)
        if worst_case is not None and worst_J > 1e-9:
            Q, f = worst_case; print("  witness Q=\n", np.round(Q, 4), "\n  f=", np.round(f, 4), " eigs", np.round(np.linalg.eigvals(Q), 4))
