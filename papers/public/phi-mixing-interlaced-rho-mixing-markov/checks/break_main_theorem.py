"""Adversarial numerical test of the manuscript's chain of inequalities on small finite Markov chains.

For a finite chain on a window {0,...,L} (stationary or time-inhomogeneous, random kernels) and random
disjoint index sets S, T with dist(S,T) >= n, compute the exact maximal correlation rho(X_S, X_T)
(second singular value of the normalised joint pmf) and compare it with

  Psi(sqrt(Delta))          the paper's robust bound, Delta = max over pairs s<t, t-s>=n in the window
                            of the row diameter max_{x,x'} TV(K_{s,t}(x,.), K_{s,t}(x',.))
  2 sqrt(Delta) cos(pi/(m+1))   the finite-path bound with m chronological blocks
  min(1, 2 sqrt(2 phi))     with phi = max over pairs of max_x TV(K_{s,t}(x,.), mu_t)

Any violation would falsify the argument.  Also verifies the six-state example exactly.
"""
import itertools, math, sys
import numpy as np

rng = np.random.default_rng(20260918)


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def maxcorr_from_joint(J):
    pa = J.sum(axis=1)
    pb = J.sum(axis=0)
    ia = pa > 1e-15
    ib = pb > 1e-15
    J = J[np.ix_(ia, ib)]
    pa = pa[ia]
    pb = pb[ib]
    M = J / np.sqrt(pa)[:, None] / np.sqrt(pb)[None, :]
    s = np.linalg.svd(M, compute_uv=False)
    return float(s[1]) if len(s) > 1 else 0.0


def path_law(mu0, kernels):
    """Joint law of (X_0,...,X_L) as an array of shape (d,)*(L+1)."""
    L = len(kernels)
    arr = mu0.copy()
    for t in range(L):
        K = kernels[t]
        arr = arr[..., None] * K[(None,) * (arr.ndim - 1) + (slice(None), slice(None))] if False else np.einsum('...i,ij->...ij', arr, K)
    return arr


def joint_ST(path, S, T):
    """Joint pmf matrix of (X_S, X_T) from the full path law."""
    L1 = path.ndim
    keep = sorted(S + T)
    drop = tuple(i for i in range(L1) if i not in keep)
    marg = path.sum(axis=drop) if drop else path
    # marg axes are in increasing time order over keep; move S axes first
    order = [keep.index(s) for s in sorted(S)] + [keep.index(t) for t in sorted(T)]
    marg = np.transpose(marg, order)
    d = path.shape[0]
    return marg.reshape(d ** len(S), d ** len(T))


def blocks(S, T):
    times = sorted([(s, 'S') for s in S] + [(t, 'T') for t in T])
    m = 1
    for a, b in zip(times, times[1:]):
        if a[1] != b[1]:
            m += 1
    return m


def Psi(r):
    return math.sin(min(2 * math.asin(min(r, 1.0)), math.pi / 2))


def window_coefficients(mu0, kernels, n):
    """Delta (row diameter) and phi (row-to-marginal) maximised over pairs s<t with t-s>=n."""
    L = len(kernels)
    d = mu0.shape[0]
    mus = [mu0]
    for K in kernels:
        mus.append(mus[-1] @ K)
    Delta = 0.0
    phi = 0.0
    for s in range(L + 1):
        Kst = np.eye(d)
        for t in range(s + 1, L + 1):
            Kst = Kst @ kernels[t - 1]
            if t - s >= n:
                rows = [x for x in range(d) if mus[s][x] > 1e-15]
                for x in rows:
                    phi = max(phi, tv(Kst[x], mus[t]))
                    for y in rows:
                        Delta = max(Delta, tv(Kst[x], Kst[y]))
    return Delta, phi


def random_sets(L, n, max_size):
    while True:
        pts = sorted(rng.choice(L + 1, size=rng.integers(2, max_size + 1), replace=False))
        col = rng.integers(0, 2, size=len(pts))
        S = [p for p, c in zip(pts, col) if c == 0]
        T = [p for p, c in zip(pts, col) if c == 1]
        if not S or not T:
            continue
        if min(abs(s - t) for s in S for t in T) >= n:
            return S, T


def run_random(trials, d, L, n, max_size, stationary):
    worst = []
    for k in range(trials):
        if stationary:
            P = rng.dirichlet(np.ones(d) * rng.uniform(0.2, 2.0), size=d)
            # sharpen some rows to make phi large-ish sometimes
            if rng.uniform() < 0.3:
                P = P ** rng.uniform(1, 6)
                P /= P.sum(axis=1, keepdims=True)
            w, v = np.linalg.eig(P.T)
            pi = np.real(v[:, np.argmin(np.abs(w - 1))])
            pi = np.abs(pi) / np.abs(pi).sum()
            mu0 = pi
            kernels = [P] * L
        else:
            mu0 = rng.dirichlet(np.ones(d))
            kernels = []
            for t in range(L):
                K = rng.dirichlet(np.ones(d) * rng.uniform(0.2, 2.0), size=d)
                if rng.uniform() < 0.3:
                    K = K ** rng.uniform(1, 6)
                    K /= K.sum(axis=1, keepdims=True)
                kernels.append(K)
        path = path_law(mu0, kernels)
        Delta, phi = window_coefficients(mu0, kernels, n)
        for _ in range(8):
            S, T = random_sets(L, n, max_size)
            rho = maxcorr_from_joint(joint_ST(path, S, T))
            m = blocks(S, T)
            b_psi = Psi(math.sqrt(Delta))
            b_path = min(1.0, 2 * math.sqrt(Delta) * math.cos(math.pi / (m + 1)))
            b_phi = min(1.0, 2 * math.sqrt(2 * phi))
            worst.append((rho - b_psi, rho, b_psi, b_path, b_phi, Delta, phi, S, T))
            if rho > b_psi + 1e-9 or rho > b_path + 1e-9 or rho > b_phi + 1e-9:
                print("VIOLATION", rho, b_psi, b_path, b_phi, Delta, phi, S, T)
    worst.sort(key=lambda r: -r[0])
    return worst


def six_state_exact(eps):
    states = list(itertools.product((-1, 1), (-1, 0, 1)))
    nu = {-1: eps, 0: 1 - 2 * eps, 1: eps}
    pi = np.array([nu[v] / 2 for u, v in states])
    P = np.array([[pi[j] * (1 + u * vp) for j, (up, vp) in enumerate(states)] for (u, v) in states])
    return pi, P


if __name__ == '__main__':
    # 1. six-state example: rho*(1) = sqrt(2 eps), rho*(2) = 0, phi(1) = eps
    for eps in (0.01, 0.1, 0.25, 0.4):
        pi, P = six_state_exact(eps)
        path = path_law(pi, [P] * 6)
        Delta, phi = window_coefficients(pi, [P] * 6, 1)
        best1 = 0.0
        best2 = 0.0
        for _ in range(300):
            S, T = random_sets(6, 1, 5)
            r = maxcorr_from_joint(joint_ST(path, S, T))
            best1 = max(best1, r)
            if min(abs(s - t) for s in S for t in T) >= 2:
                best2 = max(best2, r)
        # exhaustive over all 2-colourings of a 5-window for lag 1
        ex = 0.0
        for pts in itertools.combinations(range(6), 4):
            for col in itertools.product((0, 1), repeat=4):
                S = [p for p, c in zip(pts, col) if c == 0]
                T = [p for p, c in zip(pts, col) if c == 1]
                if S and T:
                    ex = max(ex, maxcorr_from_joint(joint_ST(path, S, T)))
        print(f"six-state eps={eps}: phi_window={phi:.6f} (claim {eps}), Delta={Delta:.6f} (claim {2*eps}), "
              f"max rho lag1 random={best1:.6f} exhaustive4pts={ex:.6f} (claim sqrt(2eps)={math.sqrt(2*eps):.6f}), "
              f"max rho lag>=2={best2:.2e} (claim 0)")
    # 2. random chains
    for stationary in (True, False):
        for (d, L, n, ms, trials) in ((3, 9, 1, 6, 150), (4, 8, 1, 6, 150), (5, 7, 1, 5, 100), (3, 9, 2, 6, 150), (6, 6, 1, 5, 40)):
            worst = run_random(trials, d, L, n, ms, stationary)
            w = worst[0]
            print(f"{'stationary' if stationary else 'inhomog.'} d={d} L={L} n={n}: {len(worst)} tests, "
                  f"max(rho - Psi(sqrt(Delta))) = {w[0]:+.6f} at rho={w[1]:.4f}, Psi={w[2]:.4f}, path={w[3]:.4f}, "
                  f"2sqrt(2phi)={w[4]:.4f}, Delta={w[5]:.4f}, phi={w[6]:.4f}, S={w[7]}, T={w[8]}")
    print("done")
