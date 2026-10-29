# agent B: independent check of the slice drift against a direct Gaussian expectation of the online-SGD increments.
# Model (statement of T240): lambda_i = w_i.x/sqrt N, nu_n = v_n.x/sqrt N jointly Gaussian with cov [[Q, R], [R^T, I]],
# g(z) = erf(z/sqrt2), delta_i = g'(lambda_i) (sum_n g(nu_n) - sum_k g(lambda_k)).
# dR_in/dt = eta E[delta_i nu_n],  dQ_ik/dt = eta E[delta_i lambda_k + delta_k lambda_i] + eta^2 E[delta_i delta_k].
import sys, math, numpy as np
sys.path[:0] = ['scripts']
import check_symmetric_closed as cs
from scipy.special import erf
from iv_exact import I, S
import iv_scm
from fractions import Fraction as F
g = lambda z: erf(z / math.sqrt(2)); gp = lambda z: math.sqrt(2 / math.pi) * np.exp(-z * z / 2)
rng = np.random.default_rng(20261018)
def mc(q, c, r, eta, n=2_000_000, reps=10):
    G = np.array([[q, c, r, r], [c, q, r, r], [r, r, 1, 0], [r, r, 0, 1]]); L = np.linalg.cholesky(G)
    acc = []
    for _ in range(reps):
        z = rng.standard_normal((n, 4)) @ L.T
        l1, l2, n1, n2 = z.T
        err = g(n1) + g(n2) - g(l1) - g(l2)
        d1, d2 = gp(l1) * err, gp(l2) * err
        dq = eta * 2 * np.mean(d1 * l1) + eta ** 2 * np.mean(d1 * d1)
        dc = eta * np.mean(d1 * l2 + d2 * l1) + eta ** 2 * np.mean(d1 * d2)
        dr = eta * np.mean(d1 * n1)
        acc.append([dq, dc, dr])
    a = np.array(acc); return a.mean(0), a.std(0) / math.sqrt(reps)
for (q, c, r) in [(1.0, 0.0, 0.0), (0.6, 0.2, 0.3), (0.3677197, 0.3253855, 0.4143942), (0.9, 0.05, 0.45)]:
    for eta in (0.5, 0.4998):
        m, s = mc(q, c, r, eta)
        cl = cs.closed(q, c, r, eta)[3:]
        iv = [float(F(v.v.lo + v.v.hi, 2 * S)) for v in iv_scm.symmetric_driver([I.of(F(x)) for x in (q, c, r)], I.of(F(eta)))]
        print('x=(%.4f,%.4f,%.4f) eta=%.4f' % (q, c, r, eta), ' MC', np.round(m, 6), '+-', np.round(s, 6),
              ' closed', np.round(cl, 6), ' iv', np.round(iv, 6), ' z', np.round((m - cl) / s, 2), flush=True)
