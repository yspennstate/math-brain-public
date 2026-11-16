"""End-to-end check of Conjecture F on the two-eigenvalue family (an agent, 11 Nov 2026).

Family: weighted graphs whose Laplacian is lam x x^t + mu (Pi - x x^t), x a unit sum-zero vector, 0 <= mu <= lam,
that is w_ij = mu/n - g x_i x_j with g = lam - mu, nonnegative iff mu >= n g max_{i<j} x_i x_j.
Claim (from Psi >= 0 and the monotonicity of Gval in lam):
    lambda_min(G, [2,1^(n-2)]) >= ((n-2)/(n-1)) lambda_min(G, [2,2,1^(n-4)]).
This script does not use Psi or Gval: it builds the Specht modules (Young's orthogonal form, alon_search.py) and
compares the two smallest eigenvalues directly.
usage: family_F_check.py nmax trials
"""
import sys
import numpy as np

sys.path.insert(0, "~/brain-repo/06_math_research/t104_alon_agent_2026_11_11")
from alon_search import edge_ops, lam as lmin  # noqa: E402


def vectors(n, rng, k):
    out = []
    star = np.array([n - 1.0] + [-1.0] * (n - 1))
    edge = np.array([1.0, -1.0] + [0.0] * (n - 2))
    out += [star, edge]
    for j in range(2, n - 1):                      # K_{1,j} padded, two-block vectors
        v = np.array([float(j)] + [-1.0] * j + [0.0] * (n - 1 - j)); out.append(v)
        v = np.array([float(n - j)] * j + [-float(j)] * (n - j)); out.append(v)
    for _ in range(k):
        kind = rng.integers(0, 5)
        if kind == 0:
            v = rng.normal(0, 1, n)
        elif kind == 1:
            v = star + rng.normal(0, 1, n) * 10.0 ** rng.uniform(-4, 0)
        elif kind == 2:
            v = edge + rng.normal(0, 1, n) * 10.0 ** rng.uniform(-5, -0.5)
        elif kind == 3:
            v = rng.choice([-2.0, -1.0, 0.0, 1.0, 3.0], n) + 1e-3 * rng.normal(0, 1, n)
        else:
            v = np.exp(rng.normal(0, 1.5, n)) * rng.choice([-1.0, 1.0], n)
        out.append(v)
    res = []
    for v in out:
        v = v - v.mean()
        nv = np.linalg.norm(v)
        if nv > 1e-9:
            res.append(v / nv)
    return res


def main():
    nmax, trials = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(2026)
    for n in range(5, nmax + 1):
        tau = (2,) + (1,) * (n - 2)
        sig = (2, 2) + (1,) * (n - 4)
        At, edges, _, _ = edge_ops(tau)
        As, _, _, _ = edge_ops(sig)
        c = (n - 2.0) / (n - 1.0)
        worst = (1e9, None)
        cnt = 0
        nz = 0
        for x in vectors(n, rng, trials):
            m = max(x[i] * x[j] for i in range(n) for j in range(i + 1, n))
            g = 1.0
            for mult in (1.0, 1.0 + 1e-3, 1.1, 2.0, 10.0):
                mu = n * g * max(m, 0.0) * mult + (0.0 if mult == 1.0 else 1e-12)
                w = np.array([mu / n - g * x[i - 1] * x[j - 1] for (i, j) in edges])
                assert w.min() > -1e-12
                w = np.maximum(w, 0.0)
                lt, _ = lmin(At, w)
                ls, _ = lmin(As, w)
                cnt += 1
                if ls > 1e-9:
                    nz += 1
                    r = lt / ls
                    if r < worst[0]:
                        worst = (r, (x.copy(), mult))
                assert lt >= c * ls - 1e-8 * max(1.0, ls), (n, lt, ls, x, mult)
        x, mult = worst[1]
        print("n=%d: %d graphs (%d with lambda_min(sigma) > 0), smallest ratio %.9f against (n-2)/(n-1) = %.9f, at mult %.3g, x = %s"
              % (n, cnt, nz, worst[0], c, mult, np.array2string(np.sort(x)[::-1], precision=4)), flush=True)


if __name__ == "__main__":
    main()
