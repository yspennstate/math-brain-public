"""Confirm the anisotropic one-sided least-sv scaling that drives the product cascade.

Model: M is N x n with i.i.d. rows m_i ~ N(0, Sigma), Sigma = diag(1,...,1, eps^2)
(one exponentially-small eigenvalue). The cascade lemma claims

    min over |T|=n of smin(M[T,:])  ~  sqrt(n * lambda_min(Sigma)) * (isotropic one-sided min)
                                     =  eps * sqrt(n) * e^{-H(alpha) N / d_F + o(N)}.

So, holding N,n fixed and varying eps, the minimum should scale LINEARLY in eps
(slope 1 on a log-log plot), and the ratio min(eps)/min(1) should track eps.

We compute the exact min over all row-supports of size n at small N, for several eps,
and report the log-log slope of min vs eps (predicted 1.0) and min(eps)/(eps*min(1)).
Light compute: small matrices only.
"""
import itertools
import numpy as np


def min_over_rowsupports(M, n):
    N = M.shape[0]
    best = np.inf
    for T in itertools.combinations(range(N), n):
        s = np.linalg.svd(M[list(T), :], compute_uv=False)[-1]
        if s < best:
            best = s
    return best


def run(N, n, epss, ntrials, seed0):
    # For each trial draw ONE standard Gaussian G (N x n); then M(eps) = G @ diag(1..1,eps)
    # so the same randomness is reused across eps (isolates the eps-scaling cleanly).
    rows = []
    for eps in epss:
        vals = []
        for t in range(ntrials):
            rng = np.random.default_rng(seed0 + t)
            G = rng.standard_normal((N, n))
            scale = np.ones(n); scale[-1] = eps
            M = G * scale  # columns scaled => rows have covariance diag(1..1,eps^2)
            vals.append(min_over_rowsupports(M, n))
        rows.append(np.array(vals))
    return rows


def main():
    N, n = 10, 5
    epss = np.array([1.0, 0.3, 0.1, 0.03, 0.01])
    ntrials = 6
    rows = run(N, n, epss, ntrials, 7000)
    med = np.array([np.median(r) for r in rows])
    print(f"N={N} n={n} trials={ntrials}")
    print(f"{'eps':>8} {'median min':>14} {'min/(eps*min@1)':>18}")
    base = med[0]  # min at eps=1
    for eps, m in zip(epss, med):
        print(f"{eps:>8.3f} {m:>14.5f} {m/(eps*base):>18.3f}")
    # log-log slope of median-min vs eps (predicted 1.0)
    slope = np.polyfit(np.log(epss), np.log(med), 1)[0]
    print(f"log-log slope d log(min)/d log(eps) = {slope:.3f}  (predicted 1.0)")
    print("If slope ~ 1 and the last column ~ 1, the sqrt(lambda_min) = eps factor is confirmed.")


if __name__ == "__main__":
    main()
