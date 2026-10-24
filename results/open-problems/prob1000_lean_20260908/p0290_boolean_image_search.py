"""P0290 (Leskela Problem 2): does Ross's workload monotonicity (1) hold for lambda(t) = f(X(t)) with f Boolean (or
deterministic) on a DOUBLY stochastically monotone CTMC X?

Light-traffic expansion (campaign proof file P0289, uniform remainder): with intensity eps F(ct), unit service,
    w(c) = eps a/2 + eps^2 J(c) + R_c,   0 <= R_c <= eps^3 M^3 / (2(1 - eps M)),   J(c) = int_0^1 (1-u) E[F(0)F(-cu)] du.
So (1) FAILS for small eps as soon as J rises somewhere.  For a REVERSIBLE X every autocovariance is a nonnegative
mixture of decaying exponentials and J is monotone (why the Codex attempt found nothing).  Doubly monotone chains
need not be reversible: this script searches 3-state (and 4-state) doubly monotone NON-reversible generators and
Boolean/nonnegative f for a rise of J.
Monotonicity criteria used (Keilson-Kester): for all i < i' and every up-set U = {k,...,m} not containing i, i':
    sum_{l in U} Q(i,l) <= sum_{l in U} Q(i',l);  and for every down-set D = {1..k} not containing i, i': the reverse.
Q* = time reversal, Q*(i,j) = pi(j) Q(j,i)/pi(i).
"""
import itertools
import numpy as np
from scipy.linalg import expm

def stationary(Q):
    w, v = np.linalg.eig(Q.T); k = np.argmin(abs(w)); p = np.real(v[:, k]); return p / p.sum()

def is_monotone(Q, tol=1e-12):
    m = Q.shape[0]
    for i in range(m):
        for ip in range(i+1, m):
            for k in range(m):
                U = list(range(k, m))
                if i not in U and ip not in U:
                    if Q[i, U].sum() > Q[ip, U].sum() + tol: return False
                D = list(range(0, k+1))
                if i not in D and ip not in D:
                    if Q[i, D].sum() < Q[ip, D].sum() - tol: return False
    return True

def reversal(Q):
    pi = stationary(Q); m = Q.shape[0]
    Qs = np.zeros_like(Q)
    for i in range(m):
        for j in range(m):
            Qs[i, j] = pi[j] * Q[j, i] / pi[i]
    return Qs

def doubly_monotone(Q):
    return is_monotone(Q) and is_monotone(reversal(Q))

def is_reversible(Q, tol=1e-9):
    pi = stationary(Q); return np.allclose(pi[:, None] * Q, (pi[:, None] * Q).T, atol=tol)

def J_curve(Q, f, cs, nu=None):
    """J(c) = sum_l A_l h(lambda_l c), h(z) = (e^z - 1 - z)/z^2, from the eigendecomposition of Q (exact, fast):
    E[F(0)F(t)] = sum_x pi(x) f(x) (P_t f)(x) = sum_l A_l e^{lambda_l t},  A_l = ((pi f)^T V)_l (V^{-1} f)_l."""
    pi = stationary(Q); a = pi @ f
    lam, V = np.linalg.eig(Q); Vi = np.linalg.inv(V)
    A = ((pi * f) @ V) * (Vi @ f)
    def h(z):
        z = np.asarray(z, dtype=complex); out = np.full(z.shape, 0.5, dtype=complex); nz = abs(z) > 1e-12
        out[nz] = (np.exp(z[nz]) - 1 - z[nz]) / z[nz]**2
        return out
    out = np.array([np.real(np.sum(A * h(lam * c))) for c in cs])
    return out, a

def max_rise(J):
    # largest J(c2) - J(c1) with c1 < c2
    best = 0.0; arg = None
    run_min = J[0]; run_arg = 0
    for k in range(1, len(J)):
        if J[k] - run_min > best: best = J[k] - run_min; arg = (run_arg, k)
        if J[k] < run_min: run_min = J[k]; run_arg = k
    return best, arg

def random_dm_chain(rng, m):
    """rejection sampling of doubly monotone non-reversible generators"""
    for _ in range(3000):
        Q = rng.uniform(0.05, 2.0, size=(m, m))
        # encourage a circulation: add a cyclic flow
        theta = rng.uniform(0, 1.0)
        for i in range(m - 1): Q[i, i+1] += theta
        Q[m-1, 0] += theta
        np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1))
        if doubly_monotone(Q) and not is_reversible(Q): return Q
    return None

if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    cs = np.exp(np.linspace(np.log(0.05), np.log(60), 120))
    # the hand example
    Qh = np.array([[-(1.2+0.1), 1.2, 0.1], [0.8, -(0.8+1.2), 1.2], [0.5, 0.8, -(0.5+0.8)]])
    print("hand example doubly monotone:", doubly_monotone(Qh), "reversible:", is_reversible(Qh), "eigs:", np.round(np.linalg.eigvals(Qh), 3))
    for f in (np.array([0, 1, 0.]), np.array([1, 0, 1.]), np.array([1, 0, 0.]), np.array([0, 0, 1.])):
        J, a = J_curve(Qh, f, cs); r, arg = max_rise(J)
        print(f"   f={f}: max rise of J = {r:.3e} at c=({cs[arg[0]]:.2f}->{cs[arg[1]]:.2f})" if arg else f"   f={f}: J monotone nonincreasing (max rise 0)")
    rng = np.random.default_rng(7)
    best = (0, None, None)
    for m in (3, 4):
        found = 0
        for trial in range(60 if m == 3 else 60):
            Q = random_dm_chain(rng, m)
            if Q is None: continue
            found += 1
            for f in [np.array(b, float) for b in itertools.product([0, 1], repeat=m) if 0 < sum(b) < m]:
                J, a = J_curve(Q, f, cs); r, arg = max_rise(J)
                if r > best[0]: best = (r, Q.copy(), f.copy(), arg)
        print(f"m={m}: {found} doubly monotone non-reversible chains sampled; best Boolean rise so far {best[0]:.3e}", flush=True)
    if best[1] is not None:
        r, Q, f, arg = best
        print("BEST: rise", r, "f", f, "c1->c2", cs[arg[0]], cs[arg[1]]); print("Q=\n", np.round(Q, 4)); print("pi", np.round(stationary(Q), 4), "eigs", np.round(np.linalg.eigvals(Q), 4))
