# Adversarial two-route slices: coordinate 0 with q = eps, L 'up' coordinates with q = p, L-1 'down' coordinates
# with q = 1-p, target s = L.  Route A: y0 = 1 and nothing else flips; route B: every up and down coordinate flips.
# eps = p^(2L-1) * gamma balances the routes.  Prints Psi/Var and the ratio for the threshold J-form.
import mpmath as mp, sys
from slice_simple import run
from isoper3 import biased_P
mp.mp.dps = 60
def thr_ratio(q, t):
    r = len(q); f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q); sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    V = mp.fsum(P[1:]); I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r))
    lhs = mp.fsum(P[A] * mp.log(mp.fprod(sig2[i] for i in range(r) if A >> i & 1) / P[A]) for A in range(1, 1 << r) if P[A] > 0)
    return float(lhs / (I - V)), float(lhs / I)
for L in (2, 3, 4, 5):
    for p in ('0.3', '0.1', '0.01', '1e-4'):
        for gamma in ('0.01', '1', '100'):
            pp = mp.mpf(p); eps = pp ** (2 * L - 1) * mp.mpf(gamma)
            if eps >= 0.5: continue
            q = [eps] + [pp] * L + [1 - pp] * (L - 1)
            Sr, Pr, rho, Lam = run(len(q), L, q)
            # the threshold with one extra coordinate j (bias 1/2) whose slice indicator is this d: T_{L+1, n+1}
            tr = thr_ratio(q + [mp.mpf('0.5')], L + 1) if len(q) + 1 <= 11 else (None, None)
            print('L', L, 'p', p, 'gamma', gamma, 'Psi/Var %.4f' % Pr, 'S/Var %.3f' % Sr, 'rho %.3g' % rho, 'Lam %.3f' % Lam,
                  'thr LHS/(I-V) nats', None if tr[0] is None else '%.4f' % tr[0], flush=True)
