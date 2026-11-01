# Exact change of basis for a slice d = 1[N = s] between the product measure mu (biases q_i) and its exponential tilt
# R (biases q^R_i = q_i u/(1 - q_i + q_i u), chosen so that E_R N = s).  On the slice dR/dmu = kappa is constant, so
#     d~_mu(B) = kappa^{-1} sum_{T subset of B} alpha_T beta_{B\T} d~_R(T),
#     alpha_i = sqrt(q^R_i(1-q^R_i)) / sqrt(q_i(1-q_i)),   beta_i = (q^R_i - q_i) / sqrt(q_i(1-q_i)).
# The T = empty term alone gives d~_mu(B) ~ rho beta_B (rho = mu(N = s)); with w_i = beta_i^2/(1+beta_i^2) the spectral
# law is then close to the product measure P_w, and for the conjunction it reproduces Psi/Var -> ln 4 + 2q ln(1/q)/(1-q).
# This script checks the identity exactly and reports how much of the mu-spectrum the leading term carries.
import mpmath as mp, random, sys
from slab_damped import biased_transform, popcount
mp.mp.dps = 60
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
worst = mp.mpf(0)
for trial in range(12):
    m = rng.randint(3, 7)
    q = [mp.mpf(rng.choice([rng.uniform(0.01, 0.2), rng.uniform(0.2, 0.8)])) for _ in range(m)]
    mean = mp.fsum(q)
    s = min(m, int(mp.floor(mean)) + rng.randint(1, 3))          # a slice above the mean
    # tilt parameter u solving E_R N = s (bisection on log u); s = m is the conjunction (u = infinity): skip it
    if s >= m: continue
    lo, hi = mp.mpf(0), mp.mpf(60)
    for _ in range(200):
        mid = (lo + hi) / 2; u = mp.e ** mid
        if mp.fsum(qi * u / (1 - qi + qi * u) for qi in q) < s: lo = mid
        else: hi = mid
    u = mp.e ** ((lo + hi) / 2)
    qR = [qi * u / (1 - qi + qi * u) for qi in q]
    d = [1 if bin(y).count('1') == s else 0 for y in range(1 << m)]
    cmu = biased_transform(d, q); cR = biased_transform(d, qR)
    # kappa = dR/dmu on the slice = u^s / prod(1 - q_i + q_i u)
    kappa = u ** s / mp.fprod(1 - qi + qi * u for qi in q)
    alpha = [mp.sqrt(qR[i] * (1 - qR[i]) / (q[i] * (1 - q[i]))) for i in range(m)]
    beta = [(qR[i] - q[i]) / mp.sqrt(q[i] * (1 - q[i])) for i in range(m)]
    err = mp.mpf(0); lead_share = mp.mpf(0); tot = mp.mpf(0)
    for B in range(1 << m):
        acc = mp.mpf(0)
        T = B
        while True:                                    # all subsets T of B
            a = mp.mpf(1)
            for i in range(m):
                if (B >> i) & 1: a *= alpha[i] if (T >> i) & 1 else beta[i]
            acc += a * cR[T]
            if T == 0: break
            T = (T - 1) & B
        pred = acc / kappa
        err = max(err, abs(pred - cmu[B]) / (abs(cmu[B]) + mp.mpf(10) ** -40))
        if B:
            lead = mp.fprod(beta[i] for i in range(m) if (B >> i) & 1) * cmu[0]
            lead_share += lead * cmu[B]; tot += cmu[B] ** 2
    worst = max(worst, err)
    print('m %d s %d (mean %.2f) u %.3g  identity rel err %s  <lead, d~>/||d~||^2 over B != 0: %.4f'
          % (m, s, float(mean), float(u), mp.nstr(err, 3), float(lead_share / tot)))
print('max identity relative error', mp.nstr(worst, 3))
