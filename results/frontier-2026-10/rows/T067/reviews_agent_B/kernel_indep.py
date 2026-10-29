"""Independent numerical test of Prop 6.2 (prop:kernel) of paper_draft_q4_d2_c259/main.tex: K(a,b;m) >= 0 on
rho(4 Simplex - 1)^2 x [0, M]. K is built from the printed text only (Table 2 features, Appendix A coefficients);
no code is shared with the author's certifier. Random search (uniform, vertex-biased, small-norm samples) for the
minimum of K and of K / (AB(A+B)) at m = 0 and m = M, then local refinement."""
import sys, json, itertools
from fractions import Fraction as Fr
import numpy as np

rho = 677 / 1000
M = 1375940705703331 / 3799912185593856
g24 = float(Fr(-44673597587449418976423934191113, 1462309266444848905334068011200160) + Fr(1743, 480965))
G = {0: 32189/5000, 1: 307513/304635, 2: 1349531/958408, 3: 13119169/971828, 8: 2046290/998719,
     10: 10803745609/1218540000, 11: 649352/585675, 12: -96567/5000, 13: -33529637/939631, 14: -96567/5000,
     15: 1007541/284861, 16: 2858842/731359, 17: 8086351/894289, 18: 314989/778090, 19: -293112/998719,
     20: 390816/998719, 21: 2119698/387547, 22: -760908/859123, 23: -9410/911487, 24: g24,
     29: -1454253/671354, 30: -1640643/978656, 31: -146556/998719, 32: -505057/629438}
PERMS = np.array(list(itertools.permutations(range(4))))
beta = 1e-6


def K(a, b, m):  # a, b: (n, 4)
    A = (a * a).sum(1); B = (b * b).sum(1); c = (a * b).sum(1); s = 1 + c / 4
    H = a + b + a * b - c[:, None] / 4; N = (H * H).sum(1); J = (H ** 3).sum(1)
    ta = (a ** 3).sum(1); tb = (b ** 3).sum(1); sa = (a ** 4).sum(1); sb = (b ** 4).sum(1)
    p = lambda i, j: (a ** i * b ** j).sum(1)
    p21, p12, p22 = p(2, 1), p(1, 2), p(2, 2); ell = p21 + p12
    p31 = p(3, 1) + p(1, 3); p32p23 = p(3, 2) + p(2, 3); p33 = p(3, 3); p42p24 = p(4, 2) + p(2, 4)
    F3 = J / s ** 2; F4 = N ** 2 / s ** 3; kap = c * ell - (B * ta + A * tb) / 3
    c4perm = sum(((a * b[:, P]).sum(1)) ** 4 for P in PERMS)
    phi = {0: m * (F3 - ta - tb), 1: A * B * (A + B) - m * (F4 - A ** 2 - B ** 2), 2: (A + B) * (c ** 2 - A * B / 3),
           3: m * (c ** 2 - A * B / 3), 8: c ** 3 - 2 / 3 * ta * tb, 10: m * c * (A + B), 11: c * ta * tb, 12: m * ell,
           13: m * (p22 - A * B / 4), 14: m * p31, 15: m * c * (ta + tb), 16: m * ell * (A + B), 17: m * kap,
           18: m * (p32p23 - (B * ta + A * tb) / 4), 19: c * p22 - ta * tb / 3, 20: p33 - ta * tb / 4,
           21: p42p24 - (B * sa + A * sb) / 4, 22: m * c * (A ** 2 + B ** 2), 23: 24 * c ** 4 - c4perm,
           24: A * B * (A + B) - m * (A ** 2 + B ** 2), 29: c * p31 - (B * sa + A * sb) / 3,
           30: p21 ** 2 + p12 ** 2 - (B * sa + A * sb - A * B * (A + B) / 4) / 3, 31: p21 * p12 - ta * tb / 3,
           32: (A + B) * (p22 - A * B / 4)}
    k = 2 / 3 * ta * tb - N * c ** 2 / s - beta * m * A * B + sum(G[j] * phi[j] for j in G)
    return k, A * B * (A + B)


def msg(p):
    return rho * (4 * p - 1)


rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
out = []
for m in (0.0, M):
    worst = (np.inf, None); worst_r = (np.inf, None)
    for alpha in (1.0, 0.3, 0.1):
        for scale in (1.0, 0.3, 0.05):
            pa = rng.dirichlet([alpha] * 4, n); pb = rng.dirichlet([alpha] * 4, n)
            sa_ = rng.uniform(0, 1, (n, 1)) ** (1 / scale if scale < 1 else 1) if scale < 1 else 1
            a = msg(pa) * sa_; b = msg(pb) * (rng.uniform(0, 1, (n, 1)) if scale < 1 else 1)
            k, d = K(a, b, m); r = k / np.maximum(d, 1e-300)
            i = int(np.argmin(k)); j = int(np.argmin(r))
            if k[i] < worst[0]: worst = (float(k[i]), (a[i].tolist(), b[i].tolist()))
            if r[j] < worst_r[0]: worst_r = (float(r[j]), (a[j].tolist(), b[j].tolist(), float(k[j]), float(d[j])))
    out.append({"m": m, "min_K": worst[0], "argmin": worst[1], "min_K_over_ABApB": worst_r[0], "argmin_ratio": worst_r[1]})
for o in out: print(json.dumps(o))
