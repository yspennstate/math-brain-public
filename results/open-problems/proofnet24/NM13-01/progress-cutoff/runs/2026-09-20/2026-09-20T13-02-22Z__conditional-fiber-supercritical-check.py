import itertools
import math
import numpy as np
from scipy.linalg import expm

# Exact finite S3 data (floating evaluation of rational/permutation matrices).
els = list(itertools.permutations(range(3)))
idx = {p: i for i, p in enumerate(els)}
e = (0, 1, 2)

def compose(p, q):
    return tuple(p[q[i]] for i in range(3))

def transp(i, j):
    p = list(e)
    p[i], p[j] = p[j], p[i]
    return tuple(p)

def right_perm(g):
    M = np.zeros((6, 6), dtype=float)
    for x in els:
        y = compose(x, g)
        M[idx[x], idx[y]] = 1.0
    return M

a = transp(0, 1)
b = transp(1, 2)
c = transp(0, 2)
Ra, Rb, Rc = map(right_perm, [a, b, c])
PW = (Ra + Rb) / 2
sev = np.linalg.eigvalsh(PW)
comm = Ra @ PW - PW @ Ra
commnorm = np.linalg.svd(comm, compute_uv=False)[0]

print('S3 refresh eigenvalues:', np.round(sev, 12))
print('S3 one-sided gap:', 1 - sev[-2])
print('||[R_a,P_W]||_2:', commnorm, 'target', math.sqrt(3) / 2)
print('aWa != W:', {compose(compose(a, w), a) for w in [a, b]} != {a, b})

# Degree-six Ramanujan lower gap and residual refresh on M x S3.
gamma_R = 1 - 2 * math.sqrt(5) / 6
eta_A = min((6 / 8) * gamma_R, (2 / 8) * (1 / 2))
print('Ramanujan degree-6 gap lower:', gamma_R)
print('residual refresh gap lower:', eta_A, 'target 1/8')
weighted_comm = (2 / 8) * commnorm
print('||[R_voltage,P_Arefresh]|| lower/exact on constant-M sector:', weighted_comm,
      'target', math.sqrt(3) / 8)

D = 20
rate_G = rate_L = 6 / D
rate_A = 8 / D
gapH = min(rate_G * gamma_R, rate_L * gamma_R, rate_A * eta_A)
print('D:', D, 'rates', rate_G, rate_L, rate_A)
print('global gap lower:', gapH, 'target 1/20')

beta = 0.5 * (1 - math.log(5) / math.log(19))
residual_exp_m = 0.05 - 0.25 / math.log(5)
global_exp_m = 0.55 - 0.25 / math.log(5)
print('cutoff center: 50 log_5 n = (25/6) log_5 N + O(1)')
print('non-LRE beta:', beta)
print('conditional residual L2 exponent in m:', residual_exp_m)
print('naive global-hidden L2 exponent in m:', global_exp_m)

# Finite 96-state sanity model: G=L=C2^2 (each K4), fiber S3.
C2sq = [(0, 0), (1, 0), (0, 1), (1, 1)]
ci = {x: i for i, x in enumerate(C2sq)}
gens = [(1, 0), (0, 1), (1, 1)]
def add2(x, y):
    return (x[0] ^ y[0], x[1] ^ y[1])

states = [(g, l, s) for g in C2sq for l in C2sq for s in els]
si = {x: i for i, x in enumerate(states)}
Ntoy = len(states)
Q = np.zeros((Ntoy, Ntoy))
for st in states:
    i = si[st]
    g, l, s = st
    for u in gens:
        Q[i, si[(add2(g, u), l, s)]] += 1 / 8
    for v in gens:
        Q[i, si[(g, add2(l, v), compose(s, a))]] += 1 / 8
    for w in [a, b]:
        Q[i, si[(g, l, compose(s, w))]] += 1 / 8
assert np.max(np.abs(Q - Q.T)) < 1e-12
assert np.max(np.abs(Q.sum(1) - 1)) < 1e-12
eig = np.linalg.eigvalsh(Q)
gap = 1 - eig[-2]
print('toy states:', Ntoy, 'Q symmetric/stochastic: YES', 'actual gap:', gap, 'bound', 1 / 8)

PG = np.zeros((4, 4))
for x in C2sq:
    for u in gens:
        PG[ci[x], ci[add2(x, u)]] += 1 / 3
piH = np.ones(Ntoy) / Ntoy
pi4 = np.ones(4) / 4
startH = np.zeros(Ntoy)
startH[si[((0, 0), (0, 0), e)]] = 1
start4 = np.zeros(4)
start4[ci[(0, 0)]] = 1

def tv(p, q):
    return 0.5 * np.abs(p - q).sum()

for t in [0.5, 1, 2, 4, 8, 12]:
    muH = startH @ expm(t * (Q - np.eye(Ntoy)))
    mu4 = start4 @ expm((3 / 8 * t) * (PG - np.eye(4)))
    dG = tv(mu4, pi4)
    dL = dG
    dH = tv(muH, piH)
    eps = 0.5 * math.sqrt(5) * math.exp(-(2 / 8) * (1 / 2) * t)
    ok = dH + 1e-10 >= max(dG, dL) and dH <= dG + dL + eps + 1e-10
    print(f't={t:4.1f} dH={dH:.12f} dG=dL={dG:.12f} eps={eps:.12f} sandwich={ok}')

assert abs(commnorm - math.sqrt(3) / 2) < 1e-12
assert abs(eta_A - 1 / 8) < 1e-12
assert abs(gapH - 1 / 20) < 1e-12
assert residual_exp_m < 0 < global_exp_m
assert beta > 0
print('ALL_CHECKS_PASS')
