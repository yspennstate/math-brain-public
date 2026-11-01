"""Biased FEI+ for OR_m, AND_m, XOR_m at arbitrary biases.
Claim: Phi = sum_j ln(1/a_j)(a_j - Z) <= 2 (sum_j (1-a_j) - 1 + Z) =: 2R, Z = prod a_j (induction).
OR_m: C_OR = 2 + 4 log2(e) = 7.7708 (sharp as m=2, q->0); XOR_m: C_XOR = 2 log2(e).
Checks: (1) Phi <= 2R on random and adversarial inputs; (2) closed forms vs brute-force biased spectra;
(3) sup of the biased FEI+ ratio of OR_m by search; (4) negative control: the inequality with 1.9 instead of 2
fails near q->0."""
import math, numpy as np
from biased_feiplus import biased_coeffs
from feicore import popcounts
LOG2E = 1 / math.log(2)

def phi_R(a):
    a = np.asarray(a, dtype=float); Z = float(np.prod(a))
    Phi = float(np.sum(np.log(1 / a) * (a - Z))); R = float(np.sum(1 - a) - 1 + Z)
    return Phi, R

def brute(kind, qs):
    m = len(qs); N = 1 << m; xs = np.arange(N)
    bits = (xs[:, None] >> np.arange(m)[None, :]) & 1          # bit=1 means x_j = -1
    true = bits == 0                                          # x_j = +1 means input true
    if kind == 'OR':
        F = np.where(true.any(axis=1), -1, 1)                 # -1 = true
    elif kind == 'XOR':
        F = np.where(true.sum(axis=1) % 2 == 1, -1, 1)
    mu = 2 * np.asarray(qs) - 1                               # E x_j, x_j = +1 w.p. q_j
    P = biased_coeffs(F, mu) ** 2
    pc = popcounts(m); sig2 = 1 - mu ** 2
    logsig = np.zeros(N)
    for j in range(m): logsig += ((xs >> j) & 1) * math.log2(sig2[j])
    sel = (xs > 0) & (P > 1e-300)
    Hp = float((P[sel] * (logsig[sel] - np.log2(P[sel]))).sum())
    exc = float((P * pc).sum() - P[1:].sum())
    return Hp, exc

import mpmath as mp
mp.mp.dps = 60
def phi_R_exact(a):
    a = [mp.mpf(float(x)) for x in a]; Z = mp.fprod(a)
    return mp.fsum([mp.log(1/x)*(x - Z) for x in a]), mp.fsum([1 - x for x in a]) - 1 + Z
rng = np.random.default_rng(5)
worst_exact = mp.mpf(0); flagged = 0; violations = 0
for t in range(200000):
    m = int(rng.integers(1, 12))
    mode = t % 4
    if mode == 0: a = rng.uniform(0, 1, m)
    elif mode == 1: a = 1 - rng.uniform(0, 1, m) ** 4
    elif mode == 2: a = rng.uniform(0, 1, m) ** 6
    else: a = 1 - 10 ** rng.uniform(-8, 0, m)
    a = np.clip(a, 1e-300, 1)
    Phi, R = phi_R(a)
    if R > 0 and Phi > 1.99 * R:          # float screen; decide in 60-digit arithmetic
        flagged += 1
        Pe, Re = phi_R_exact(a)
        if Re > 0:
            worst_exact = max(worst_exact, Pe / Re)
            if Pe > 2 * Re: violations += 1
print('(1) 200000 random inputs; float screen flagged', flagged, 'cases (ratio > 1.99);')
print('    their exact 60-digit max Phi/R =', mp.nstr(worst_exact, 15), '; exact violations of Phi <= 2R:', violations)
maxdiff = 0.0
for t in range(300):
    m = int(rng.integers(1, 9)); q = rng.uniform(0.001, 0.999, m)
    for kind in ('OR', 'XOR'):
        Hp, exc = brute(kind, q)
        if kind == 'OR':
            a = 1 - q; Z = float(np.prod(a)); L = np.log2(1 / a)
            closed_H = 2 * exc + 2 * 4 * Z * float(np.sum(L * (a - Z)))
            closed_exc = 4 * Z * float(np.sum(q) - 1 + Z)
        else:
            a = (2 * q - 1) ** 2; A = float(np.prod(a))
            closed_H = float(np.sum(np.log2(1 / np.maximum(a, 1e-300)) * (a - A)))
            closed_exc = float(np.sum(1 - a) - 1 + A)
        maxdiff = max(maxdiff, abs(Hp - closed_H), abs(exc - closed_exc))
print('(2) closed forms match brute-force biased spectra: max abs diff %.2e' % maxdiff)
best = 0.0; arg = None
for t in range(4000):
    m = int(rng.integers(2, 8)); q = 10 ** rng.uniform(-6, -0.01, m)
    Hp, exc = brute('OR', q)
    if exc > 1e-14 and Hp / exc > best: best, arg = Hp / exc, (m, q.round(8).tolist())
print('(3) float search: max biased FEI+ ratio of OR_m = %.6f at m=%d, q=%s' % (best, arg[0], arg[1]))
ae = [1 - mp.mpf(float(x)) for x in arg[1]]; Ze = mp.fprod(ae)
Pe = mp.fsum([mp.log(1/x)*(x - Ze) for x in ae]); Re = mp.fsum([1 - x for x in ae]) - 1 + Ze
print('    same instance in 60-digit closed form: %s; 2+4log2(e) = %s' % (mp.nstr(2 + 2*(Pe/Re)/mp.log(2), 12), mp.nstr(2 + 4/mp.log(2), 12)))
for q in (1e-2, 1e-4, 1e-6):
    Hp, exc = brute('OR', [q, q]); print('    OR_2 at q=%g: ratio %.5f' % (q, Hp / exc))
a = np.array([1 - 1e-4, 1 - 1e-4]); Phi, R = phi_R(a)
print('(4) negative control: at a=(1-1e-4)^2, Phi/R = %.5f > 1.9, so the constant 2 cannot be lowered' % (Phi / R))
