"""Exact toy for Janson's Problem 20.2 (third question, nu < 1, and second, nu = 1 with sigma^2 = infinity):
the number N_1 of boxes of size 1 in B_{n-1,n} (= number of outdegree-1 nodes of the simply generated tree T_n)
is NOT asymptotically normal when the law has two 'big' atoms at L^- and L^+ = (missing mass) -/+ A sqrt(n).
Law: atoms 0, 1 (bulk), 6 (medium, optional), L-, L+ (each mass pbig), LB (rarer, optional, mass pB).
We compute P(N_1 = k | S_n = n-1) exactly by enumerating the numbers of medium/big/rarer boxes (multinomial)."""
import sys, numpy as np
from math import lgamma, log, exp, sqrt
n = 4000; m = n - 1
mode = sys.argv[1] if len(sys.argv) > 1 else 'sub'   # 'sub' (nu<1, no medium, no rarer) or 'crit' (nu=1, sigma^2 'large')
A = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
delta = 0.05
if mode == 'sub':
    pi1 = 0.5; pM = 0.0; LM = 6; pB = 0.0; LB = 10 ** 6
    missing = m - pi1 * (n - 1)          # what one big box must supply so that the other n-1 bulk boxes sit at their mean
    Lm = int(round(missing - A * sqrt(n))); Lp = int(round(missing + A * sqrt(n)))
else:
    pi1 = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5; LM = int(sys.argv[3]) if len(sys.argv) > 3 else 6; pM = (float(sys.argv[4]) if len(sys.argv) > 4 else 100) / n; eps = 0.05; Sigma = 1000.0; LB = int(round(Sigma / eps)); pB = eps / n
    missing = m - (pi1 + pM * LM) * (n - 1)   # with the rarer atom absent, one rare box supplies this (bulk + medium at their means)
    Lm = int(round(missing - A * sqrt(n))); Lp = int(round(missing + A * sqrt(n)))
pbig = delta / 2 / n
p0 = 1 - pi1 - pM - 2 * pbig - pB
assert p0 > 0
nu = pi1 + pM * LM + pbig * (Lm + Lp) + pB * LB
print(f"mode={mode} n={n} A={A} L-={Lm} L+={Lp} LB={LB} nu={nu:.4f} pi1={pi1} n*pbig each={n*pbig}")
def lmult(counts, probs, ntot):
    """log of multinomial probability of counts (list), rest at prob p0."""
    rest = ntot - sum(counts)
    if rest < 0: return None
    v = lgamma(ntot + 1) - lgamma(rest + 1) + rest * log(p0)
    for c, p in zip(counts, probs):
        if c > 0 and p == 0: return None
        v += -lgamma(c + 1) + (c * log(p) if c > 0 else 0.0)
    return v
from collections import defaultdict
w = defaultdict(float)     # k -> unnormalised P(N_1 = k, S = m)
jMmax = int(4 * pM * n + 60) if pM > 0 else 0
for jm in range(0, 3):
    for jp in range(0, 3):
        for jB in range(0, 2 if pB > 0 else 1):
            for jM in range(0, jMmax + 1):
                k = m - jm * Lm - jp * Lp - jB * LB - jM * LM
                if k < 0: break
                lv = lmult([k, jM, jm, jp, jB], [pi1, pM, pbig, pbig, pB], n)
                if lv is None: continue
                w[(k, jm, jp)] += exp(lv - 0)  # scale later
Z = sum(w.values())
byk = defaultdict(float); bybranch = defaultdict(float)
for (k, jm, jp), v in w.items():
    byk[k] += v / Z; bybranch[(jm, jp)] += v / Z
print("branch probabilities (j-, j+):", {b: round(v, 4) for b, v in bybranch.items() if v > 1e-4})
ks = np.array(sorted(byk)); ps = np.array([byk[k] for k in ks])
mean = (ks * ps).sum(); sd = sqrt(((ks - mean) ** 2 * ps).sum())
z = (ks - n * pi1) / sqrt(n)
print(f"E[N_1|S=m] = {mean:.1f}  sd = {sd:.2f}  (n pi1 = {n*pi1}, sqrt(n pi1(1-pi1)) = {sqrt(n*pi1*(1-pi1)):.2f})")
# histogram of z in bins of width 0.5
bins = np.arange(-8, 8.5, 0.5)
h = np.zeros(len(bins) - 1)
for zi, pi in zip(z, ps):
    b = np.searchsorted(bins, zi, side='right') - 1
    if 0 <= b < len(h): h[b] += pi
for b0, hv in zip(bins[:-1], h):
    if hv > 0.002: print(f"  z in [{b0:+.1f},{b0+0.5:+.1f}): {hv:.3f} " + '#' * int(200 * hv))
# distance from the conjectured Gaussian N(0, pi1(1-pi1)): P(|z| < 1 sd)
s0 = sqrt(pi1 * (1 - pi1))
print("P(|z| <= s0) =", f"{ps[np.abs(z) <= s0].sum():.3f}", " (Gaussian would give 0.683)")
