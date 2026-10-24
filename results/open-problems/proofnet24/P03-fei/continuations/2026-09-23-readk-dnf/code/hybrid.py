"""Hybrid first-element reference for the biased strengthened inequality of threshold functions.
Per first element i (desirability order), psi_i = E_{x<i}[f(x^{i<-1}) - f(x^{i<-0})] as a function of the successors.
Q(A) = V_i * R_i(B) with V_i = sigma_i^2 E psi_i^2 (exact), R_i(empty) = 1 - omega_i (exact), and for B != empty
R_i(B) = omega_i * rho(kappa) * prod_{j in succ} r_j^{[j in B]} (1-r_j)^{[j not in B]} / (1 - prod(1-r_j)),   summed over
kappa >= 1 with rho(kappa) = 1/(kappa(kappa+1)) (a mixture over the level parameter, lower-bounded by the best kappa),
r_j = min(1/2, max(sigma_j^2 theta_kappa(j), c Inf_j(psi_i)/Var(psi_i))), theta_kappa(j) = min(1,(kappa/M_j)^a),
M_j = sigma^2-mass of the successors up to j.  Bound Bd = sum_{A != empty} P log(sigma_A^2/Q(A)) (>= LHS+ by Gibbs).
Report max Bd/J on adversarial LTFs and on the slow-log probe family."""
import math, sys, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts, polite
polite()
A_EXP = 1.2; CI = 0.5; JCUT = 1e-13
def h2(x):
    return 0.0 if x <= 0 or x >= 1 else -x * math.log2(x) - (1 - x) * math.log2(1 - x)
def analyse(w, theta, mu, kmax=None):
    n = len(w); N = 1 << n; xs = np.arange(N)
    X = 1 - 2 * ((xs[:, None] >> np.arange(n)[None, :]) & 1)
    F = np.where(X @ w - theta > 0, 1, -1)
    Ft = biased_coeffs(F, mu); P = Ft ** 2
    sig2 = 1 - np.asarray(mu) ** 2
    pc = popcounts(n)
    J = float((P * pc)[pc >= 2].sum())
    if J < JCUT: return None
    logsig = np.zeros(N)
    for i in range(n): logsig += ((xs >> i) & 1) * math.log2(max(sig2[i], 1e-300))
    nz = (P > 1e-300) & (xs > 0)
    LHS = float((P[nz] * (logsig[nz] - np.log2(P[nz]))).sum())
    order = sorted(range(n), key=lambda j: (-abs(w[j]), j)); pos = {j: r for r, j in enumerate(order)}
    minel = np.full(N, -1)
    for S in range(1, N):
        minel[S] = min((j for j in range(n) if S >> j & 1), key=lambda j: pos[j])
    Bd = 0.0
    for i in range(n):
        sel = (minel == i) & (P > 0)
        Vi = float(P[sel].sum())
        if Vi <= 1e-300: continue
        Bd += Vi * math.log2(sig2[i] / Vi)
        single = float(P[1 << i]); Wi = Vi - single; om = Wi / Vi
        Bd += Vi * h2(om)
        if Wi <= 1e-300: continue
        succ = [j for j in order if pos[j] > pos[i]]
        # psi_i spectrum: P({i} u B) / sigma_i^2 for B subset succ; Inf_j(psi) = sum over B containing j
        infl = {j: float(P[sel & ((xs >> j) & 1 == 1)].sum()) / sig2[i] for j in succ}
        varpsi = Wi / sig2[i]
        M = {}; acc = 0.0
        for j in succ:
            acc += sig2[j]; M[j] = acc
        kmx = kmax or max(1, len(succ))
        for S in np.nonzero(sel)[0]:
            if S == (1 << i): continue
            inB = {j: bool(S >> j & 1) for j in succ}
            best = -1e300
            for kap in range(1, kmx + 1):
                r = {j: min(0.5, max(sig2[j] * min(1.0, (kap / M[j]) ** A_EXP) if M[j] > 0 else 0.5, CI * infl[j] / varpsi)) for j in succ}
                lp = sum(math.log2(r[j]) if inB[j] else math.log2(1 - r[j]) for j in succ)
                pz = math.prod(1 - r[j] for j in succ)
                lp -= math.log2(1 - pz)
                lp += -math.log2(kap * (kap + 1))
                best = max(best, lp)
            # R_i(B) = omega R'(B); log2 R'(B) >= best (mixture over kappa lower-bounded by its best component)
            cost = float(logsig[S] - math.log2(sig2[i])) - best   # log(1/omega) is already in V_i h(omega)
            Bd += float(P[S]) * cost
    assert LHS <= Bd + 1e-9, (LHS, Bd)
    return dict(ratio=Bd / J, lhs=LHS / J)
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'probe'
    if mode == 'probe':
        for eps in (1e-2, 1e-4, 1e-6, 1e-9, 1e-12):
            r = analyse(np.array([3.0, 2.0, 1.0]), 1.9, np.array([0.0, 1 - 2 * eps, 0.0]))
            print(f"probe eps={eps:.0e}: Bd/J {r['ratio']:6.2f}  LHS/J {r['lhs']:5.2f}", flush=True)
        # more slow-log families: frozen successor among several active ones; frozen predecessor; two frozen
        for eps in (1e-3, 1e-6, 1e-9, 1e-12):
            for (w, th, mu, tag) in [
                ([4.0, 2.0, 1.0, 1.0, 1.0], 2.9, [0.0, 1 - 2 * eps, 0.0, 0.0, 0.0], "frozen succ + 3 active"),
                ([4.0, 2.0, 1.0, 1.0], 0.9, [1 - 2 * eps, 0.0, 0.0, 0.0], "frozen first"),
                ([3.0, 2.0, 2.0, 1.0], 2.9, [0.0, 1 - 2 * eps, 1 - 2 * eps, 0.0], "two frozen succ"),
                ([3.0, 2.0, 1.0, 1.0], 2.9, [0.0, -(1 - 2 * eps), 0.0, 0.0], "frozen succ (low)"),
            ]:
                r = analyse(np.array(w), th, np.array(mu))
                if r: print(f"{tag:26s} eps={eps:.0e}: Bd/J {r['ratio']:6.2f}  LHS/J {r['lhs']:5.2f}", flush=True)
    else:
        rng = np.random.default_rng(int(sys.argv[2]))
        best = None
        for trial in range(int(sys.argv[3])):
            n = int(rng.integers(3, 7))
            w = np.abs(rng.standard_normal(n)) * np.exp(rng.uniform(-2, 2, n))
            th = rng.uniform(-w.sum(), w.sum())
            mu = np.array([rng.uniform(-0.3, 0.3) if rng.random() < 0.3 else rng.choice([-1, 1]) * (1 - 10.0 ** (-rng.uniform(0.3, 8))) for _ in range(n)])
            r = analyse(w, th, mu)
            if r is None: continue
            if best is None or r['ratio'] > best[0]['ratio']:
                best = (r, dict(w=np.round(w, 3).tolist(), th=round(th, 3), mu=mu.tolist()))
            if trial % 200 == 199: print(f"trial {trial+1}: max Bd/J {best[0]['ratio']:.2f} (LHS/J {best[0]['lhs']:.2f})", flush=True)
        print("worst:", best)
