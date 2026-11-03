# T021: a uniform bound D_k/I_k <= 5 + ln 4 = 6.386 nats for EVERY read-once formula and every coordinate.
# Identity. In the general recursion (q31_readonce_general.stepP), put Psi(c0, I) = Phi(c0^2, I^2)/I. Since
# Phi(c0'^2, I^2 P^2) = P^2 Phi(c0'^2/P^2, I^2), the gain is
#   r' - r = (1 - P) Phi(4mu^2, I^2)/I + Psi(c0', I') - Psi(c0, I),
# and from the leaf state (c0, I, D) = (0, 1, 0), where Psi = 0,
#   D_k/I_k = r_L = sum_l (I_l - I_{l+1}) Phi(4mu_l^2, I_l^2)/I_l^2 + Psi(c0_L, I_L).          (*)
# Bound. Card 9's corollary Phi(l, m) <= m(3 + ln_+(l/m)) with mu <= 1 gives Phi(4mu^2, I^2)/I^2 <= a + 2 ln(1/I), a = 3 + ln 4,
# and Psi(c0, I) <= I(3 + 2 ln(1/I)) (c0^2 <= 1). As ln(1/x) >= ln(1/I_l) on [I_{l+1}, I_l],
#   r_L <= int_{I_L}^1 (a + 2 ln 1/x) dx + I_L(3 + 2 ln 1/I_L) = a + 2 - I_L (a - 1) < 5 + ln 4.
# The continuum value pi^2/2 is (*) with mu = 1/2 and P -> 1: int_0^1 Phi(1, x^2)/x^2 dx.
import random, mpmath as mp, numpy as np
from q31_tree_entropy import Phi
from q31_readonce_general import stepP
mp.mp.dps = 400
a = 3 + mp.log(4); B = a + 2
def run(Ps):
    st = (mp.mpf(0), mp.mpf(1), mp.mpf(0)); S = mp.mpf(0); worst_id = mp.mpf(0); worst_r = mp.mpf(0); slack = mp.inf
    for P in Ps:
        c0, I, D = st; mu = (1 - c0) / 2
        S += (1 - P) * Phi(4 * mu ** 2, I ** 2) / I
        st = stepP(st, P); c0, I, D = st
        r = D / I; rhs = S + Phi(c0 ** 2, I ** 2) / I
        worst_id = max(worst_id, abs(r - rhs) / max(1, abs(r))); worst_r = max(worst_r, r)
        slack = min(slack, (B - I * (a - 1)) - r)
    return worst_id, worst_r, slack
random.seed(5); wid = mp.mpf(0); wr = mp.mpf(0); ws = mp.inf; nseq = 0; nsteps = 0
gens = [lambda: mp.mpf(random.random()),
        lambda: 1 - mp.mpf(10) ** -random.uniform(0, 6),
        lambda: mp.mpf(random.choice([0.3, 0.45, 0.5, 0.6, 0.9])),
        lambda: 1 - mp.mpf(10) ** -random.uniform(0, 3) if random.random() < 0.8 else mp.mpf(random.random())]
for g in gens:
    for t in range(60):
        Ps = [g() for _ in range(random.randint(5, 150))]
        Ps = [min(max(P, mp.mpf(10) ** -12), 1 - mp.mpf(10) ** -12) for P in Ps]
        i, r, s = run(Ps); wid = max(wid, i); wr = max(wr, r); ws = min(ws, s); nseq += 1; nsteps += len(Ps)
print("identity (*) on %d random P sequences (%d steps, 4 generators, 400 digits): max relative error %s" % (nseq, nsteps, mp.nstr(wid, 3)))
print("max D_k/I_k seen %s; min slack to a + 2 - I_L(a-1) = %s (>= 0); bound 5 + ln 4 = %s" % (mp.nstr(wr, 10), mp.nstr(ws, 6), mp.nstr(B, 10)))
d = mp.mpf("0.001"); i, r, s = run([1 - d] * 15000)
print("P = 1 - 0.001 for 15000 levels: D/I = %s (pi^2/2 = %s), identity error %s, slack %s" % (mp.nstr(r, 10), mp.nstr(mp.pi ** 2 / 2, 10), mp.nstr(i, 3), mp.nstr(s, 6)))
# Truth tables: the bound on random read-once NAND trees (exact D_k from entropies), reusing q31_readonce_check's trees
from q31_tree_entropy import wht, ent
import q31_readonce_check as C
rng = random.Random(23); top = 0.0; cases = 0
for trial in range(40):
    n = rng.randint(3, 13); t = C.rand_tree(n, rng)
    if t[0] == "x": continue
    N = 1 << n; X = np.where(((np.arange(N)[:, None] >> np.arange(n)[None, :]) & 1) == 1, -1, 1)
    f = C.evalt(t, X); c = wht(f); H = ent(c); S_ = np.arange(N)
    for k in range(n):
        m = 1 << k; lo = S_[(S_ & m) == 0]
        Dk = H - (ent(wht(f[lo])) + ent(wht(f[lo | m]))) / 2; Ik = float((c[lo | m] ** 2).sum())
        top = max(top, Dk / Ik); cases += 1
print("truth tables: %d coordinates of 40 random read-once trees, max D_k/I_k = %.6f <= %.6f: %s" % (cases, top, float(B), top <= float(B)))
print("all checks pass:", wid < mp.mpf(10) ** -100 and ws >= 0 and wr < B and top <= float(B))
