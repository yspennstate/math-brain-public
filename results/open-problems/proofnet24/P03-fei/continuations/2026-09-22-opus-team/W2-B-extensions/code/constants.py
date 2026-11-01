"""Constants of Theorem 1 and its corollaries (mpmath, 30 digits).

L(beta) = 2 ln((3 sqrt 3 / 2) beta) + 2,  C(L, d) = 3 + min_{a>1} [1 + ln d + ln(a/(a-1)) + a L] / ln 2,
minimiser a = (1 + sqrt(1 + 4/L))/2.  beta for: k halfspaces (no order condition) k^{3/2} 2/sqrt(pi);
co-monotone k halfspaces k 2/sqrt(pi); (kappa, m)-separable over units of size <= d, combined k times:
k^{3/2} kappa sqrt(m) (2/sqrt(pi)) 2^{(d-1)/2}.
Also checks the scalar inequality psi(u) >= 0 of Lemma D on a grid (the proof is by concavity).
"""
from mpmath import mp, mpf, sqrt, log, pi
mp.dps = 30

def L_of_beta(beta):
    return 2 * log(3 * sqrt(3) / 2 * beta) + 2

def C_of(L, d=1):
    a = (1 + sqrt(1 + 4 / L)) / 2
    return 3 + (1 + log(d) + log(a / (a - 1)) + a * L) / log(2), a

b0 = 2 / sqrt(pi)
L1 = L_of_beta(b0)
out = []
out.append("B = 3 sqrt(3/pi) = %s,  L1 = %s" % (mp.nstr(3 * sqrt(3 / pi), 20), mp.nstr(L1, 20)))
C, a = C_of(L1)
out.append("single LTF (F5 Theorem 1): C = %s  (a = %s)" % (mp.nstr(C, 15), mp.nstr(a, 12)))
out.append("")
out.append("Boolean functions of k halfspaces, arbitrary weights (L = L1 + 3 ln k) / co-monotone (L1 + 2 ln k):")
for k in (1, 2, 3, 4, 5, 8, 10, 16, 32, 100, 1000):
    Ca, _ = C_of(L1 + 3 * log(k))
    Cc, _ = C_of(L1 + 2 * log(k))
    out.append("  k=%5d  C_k = %s   co-monotone %s" % (k, mp.nstr(Ca, 10), mp.nstr(Cc, 10)))
out.append("  asymptotically C_k = 3 log2 k + log2 ln k + O(1)")
out.append("")
out.append("block-separable thresholds, units of size <= d (L = L1 + (d-1) ln 2, plus ln d in the normalisation):")
for d in (1, 2, 3, 4, 5, 6, 8, 10):
    Cd, _ = C_of(L1 + (d - 1) * log(2), d)
    out.append("  d=%2d  C = %s" % (d, mp.nstr(Cd, 10)))
out.append("")
out.append("separable functions of block sums (kappa changes per axis line, m groups), d = 1:")
for (kap, m, name) in [(1, 2, "sgn(L1(x')L2(x'') - theta)"), (2, 2, "disc/ellipse on disjoint sets"), (2, 1, "|w.x - theta| < t"),
                       (4, 2, "annulus on disjoint sets"), (1, 3, "sgn(L1 L2 L3 - theta), disjoint")]:
    Cs, _ = C_of(L1 + 2 * log(kap) + log(m))
    out.append("  kappa=%d m=%d  C = %s   (%s)" % (kap, m, mp.nstr(Cs, 10), name))
out.append("")
out.append("degree-2 PTFs whose quadratic part has a vertex cover of size s (Boolean function of s + 2^s halfspaces):")
for s in (1, 2, 3, 4, 5, 10):
    Cv, _ = C_of(L1 + 3 * log(s + 2 ** s))
    out.append("  s=%2d  C = %s" % (s, mp.nstr(Cv, 10)))
out.append("")
out.append("PTFs sgn(prod_{j<=D} (L_j - theta_j)) (Boolean function of 2D halfspaces):")
for D in (2, 3, 4, 5):
    Cp, _ = C_of(L1 + 3 * log(2 * D))
    out.append("  D=%d  C = %s" % (D, mp.nstr(Cp, 10)))
# scalar inequality of Lemma D: psi(u) = (u/2) log2(1/u) + (1-u/2) log2(2-u) + u - 1 >= 0 on (0,1]
worst = mpf(1)
N = 20000
for j in range(1, N + 1):
    u = mpf(j) / N
    psi = (u / 2) * log(1 / u, 2) + (1 - u / 2) * log(2 - u, 2) + u - 1
    worst = min(worst, psi)
out.append("")
out.append("Lemma D scalar check: min over u = j/20000 of psi(u) = %s (zero at u = 1; psi is concave, psi(0+) = psi(1) = 0)" % mp.nstr(worst, 8))
open("../logs/constants.log", "w").write("\n".join(out) + "\n")
print("\n".join(out))
