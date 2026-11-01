"""Biased FEI+ for threshold functions: test a 'first element' reference.
For A != empty let i = the most desirable element of A (order by |w| decreasing), B = A minus i.
Reference:  Q(A) = V_i * R_i(B),  V_i = P_mu(min A = i),  R_i(empty) = 1 - omega_i,
            R_i(B) = omega_i * rho(|B|) * sigma_B^2 prod_{j in B} theta(j) / Z_{|B|}  (B != empty),
            theta(j) = min(1, (s / M_j)^a),  M_j = sigma^2-mass of the successors of i up to and including j,
            Z_s = e_s(sigma_j^2 theta(j), j successor of i),  rho(s) = 1/(s(s+1)).
Since sum_{A != empty} Q(A) = Var = sum_{A != empty} P, Gibbs gives LHS+ <= sum P log(sigma_A^2/Q(A)) =: Bd exactly
(no normalisation loss).  Bd = T1 + T2 + T3:
 T1 = sum_i V_i log(sigma_i^2 / V_i),   T2 = sum_i V_i h(omega_i),
 T3 = sum_{A, |A|>=2} P(A) [log s(s+1) + log Z_s - sum_{j in B} log theta(j)].
Report max Bd/J over adversarial LTFs and biases, with the split, and the true LHS+/J."""
import math, sys, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
polite()
A_EXP = 1.2
def h2(x):
    if x <= 0 or x >= 1: return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)
def esym(vals, s):
    e = np.zeros(s + 1); e[0] = 1.0
    for v in vals:
        e[1:] = e[1:] + v * e[:-1]
    return e[s]
def analyse(w, theta, mu):
    n = len(w); N = 1 << n
    xs = np.arange(N)
    X = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
    F = np.where(X @ w - theta > 0, 1, -1)
    Ft = biased_coeffs(F, mu); P = Ft ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    pc = popcounts(n)
    J = float((P * pc)[pc >= 2].sum()); Var = float(P[1:].sum()); I = float((P * pc).sum())
    if J < 1e-13: return None
    logsig = np.zeros(N)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(sig2[i])
    nz = (P > 1e-300) & (xs > 0)
    LHS = float((P[nz] * (logsig[nz] - np.log2(P[nz]))).sum())
    order = sorted(range(n), key=lambda j: (-abs(w[j]), j))
    pos = {j: r for r, j in enumerate(order)}
    T1 = T2 = T3 = 0.0
    # group sets by their most desirable element
    minel = np.full(N, -1)
    for S in range(1, N):
        els = [j for j in range(n) if S >> j & 1]
        minel[S] = min(els, key=lambda j: pos[j])
    for i in range(n):
        sel = (minel == i) & (P > 0)
        Vi = float(P[sel].sum())
        if Vi <= 1e-300: continue
        T1 += Vi * math.log2(sig2[i] / Vi)
        single = float(P[1 << i])
        om = (Vi - single) / Vi
        T2 += Vi * h2(om)
        succ = [j for j in order if pos[j] > pos[i]]
        for S in np.nonzero(sel)[0]:
            if S == (1 << i): continue
            B = [j for j in range(n) if (S >> j & 1) and j != i]
            s = len(B)
            M = {}; acc = 0.0
            for j in succ:
                acc += sig2[j]; M[j] = acc
            th = {j: min(1.0, (s / M[j]) ** A_EXP) if M[j] > 0 else 1.0 for j in succ}
            Z = esym([sig2[j] * th[j] for j in succ], s)
            cost = math.log2(s * (s + 1)) + math.log2(Z) - sum(math.log2(th[j]) for j in B)
            T3 += float(P[S]) * cost
    Bd = T1 + T2 + T3
    assert LHS <= Bd + 1e-9, (LHS, Bd)
    return dict(ratio=Bd / J, lhs=LHS / J, T1=T1 / J, T2=T2 / J, T3=T3 / J, IV=(I - Var) / J)
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
def rand_mu(n):
    kind = rng.integers(0, 4, n)
    mu = np.empty(n)
    for j in range(n):
        if kind[j] == 0: mu[j] = rng.uniform(-0.3, 0.3)
        elif kind[j] == 1: mu[j] = rng.uniform(-1, 1)
        else: mu[j] = rng.choice([-1, 1]) * (1 - 10.0 ** (-rng.uniform(1, 6)))
    return mu
best = None
for trial in range(1500):
    n = int(rng.integers(3, 8))
    w = np.abs(rng.standard_normal(n)) * np.exp(rng.uniform(-2, 2, n))
    theta = rng.uniform(-w.sum(), w.sum())
    mu = rand_mu(n)
    r = analyse(w, theta, mu)
    if r is None: continue
    # local adversarial improvement on mu
    for it in range(25):
        mu2 = mu.copy(); j = rng.integers(n)
        mu2[j] = np.clip(mu2[j] + rng.normal(0, 0.3) * (1 - abs(mu2[j]) + 1e-3), -1 + 1e-7, 1 - 1e-7)
        r2 = analyse(w, theta, mu2)
        if r2 is not None and r2['ratio'] > r['ratio']: mu, r = mu2, r2
    if best is None or r['ratio'] > best[0]['ratio']:
        best = (r, dict(n=n, w=np.round(w, 3).tolist(), theta=round(theta, 3), mu=np.round(mu, 6).tolist()))
    if trial % 100 == 99:
        print(f"trial {trial+1}: max Bd/J {best[0]['ratio']:.2f} (LHS/J {best[0]['lhs']:.2f}, T1 {best[0]['T1']:.2f}, T2 {best[0]['T2']:.2f}, T3 {best[0]['T3']:.2f}, (I-Var)/J {best[0]['IV']:.2f})", flush=True)
print("worst:", best)
