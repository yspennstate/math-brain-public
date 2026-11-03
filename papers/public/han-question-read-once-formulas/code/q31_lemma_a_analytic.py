# T021: an analytic proof of Lemma A and the sharper uniform bound it gives (replaces the numeric constant of
# q31_tree_bound_proof.py).
#
# Lemma A. For 0 < t <= 1:   t (4 ln 2 + ln(1/t))  <=  Phi(1, t)  <=  t (3 + ln(1/t)).
# Proof. Put b = sqrt(t). With h(x) = -x ln x,
#   Phi(1, t) = -2 b^2 ln b + G(b),   G(b) = (1+b)^2 ln(1+b) + (1-b)^2 ln(1-b).
# G is even, and with ln(1+b) = sum_k a_k b^k, a_k = (-1)^(k+1)/k (a_0 = 0), the coefficient of b^m in (1+b)^2 ln(1+b)
# is c_m = a_m + 2 a_{m-1} + a_{m-2}. So G(b) = 2 sum_n c_{2n} b^{2n}, with
#   c_2 = 3/2,   c_{2n} = 2/(2n-1) - 1/(2n) - 1/(2n-2) < 0 for n >= 2   (1/x is strictly convex),
# and sum |c_{2n}| < infinity (c_{2n} = O(n^-3)), so the series converges absolutely on [0, 1] and G(1) = 4 ln 2.
# Upper: G(b) <= 3 b^2. Lower: c_{2n} b^{2n} >= c_{2n} b^2 for n >= 2 (c_{2n} < 0, b^{2n} <= b^2), so
# G(b) >= b^2 (3 + 2 sum_{n>=2} c_{2n}) = b^2 G(1) = 4 ln 2 b^2. Add -2 b^2 ln b = t ln(1/t). QED.
# Both ends are sharp: the upper at t -> 0 (Phi(1,t) = t ln(1/t) + 3t + O(t^2)), the lower at t = 1 (Phi(1,1) = 4 ln 2).
#
# Corollary (any l, m > 0, Phi symmetric and 1-homogeneous): Phi(l, m) <= m (3 + ln_+(l/m)).
#   m <= l: Phi = l Phi(1, m/l) <= m (3 + ln(l/m)).  l < m: Phi <= l (3 + ln(m/l)) <= 3m, since x (3 + ln(m/x)) increases on (0, m].
# Gain bound. In r' - r = [(1-P) Phi(4mu^2, I^2) - Phi(c0^2, I^2) + P Phi(c0'^2/P^2, I^2)] / I, drop the middle term (Phi >= 0),
# use mu <= 1, c0'^2 <= 1 and P ln(1/P) <= 1/e:
#   r' - r <= I (3 + ln 4 + 2/e + 2 ln(1/I)) =: g3(I),   increasing on (0, 1] (g3' = 1 + ln 4 + 2/e + 2 ln(1/I) > 0).
# With Lemma B (I_{l+2}/I_l <= q = 2/(3 sqrt 3), I_1 <= 1/2):  sup D_k/I_k <= sum_{j>=0} [g3(q^j) + g3(q^j/2)].
import random, mpmath as mp
from q31_tree_entropy import step, Phi
mp.mp.dps = 120
ln2 = mp.log(2)
# 1. the coefficient facts
c = lambda n: mp.mpf(2) / (2 * n - 1) - mp.mpf(1) / (2 * n) - mp.mpf(1) / (2 * n - 2)
neg = all(c(n) < 0 for n in range(2, 5001))
G1 = 3 + 2 * mp.nsum(c, [2, mp.inf])
print("c_{2n} < 0 for 2 <= n <= 5000: %s;  3 + 2 sum_{n>=2} c_{2n} = %s,  4 ln 2 = %s,  diff %s" % (
    neg, mp.nstr(G1, 20), mp.nstr(4 * ln2, 20), mp.nstr(abs(G1 - 4 * ln2), 3)))
# 2. the two-sided bound on a grid down to t = 1e-80
mp.mp.dps = 400  # U - Phi = t^2/6 + O(t^3) and Phi cancels from O(sqrt t): 120 digits cannot resolve the gap at t = 1e-80
grid = [mp.mpf(10) ** (-k) for k in range(1, 81)] + [mp.mpf(j) / 4000 for j in range(1, 4001)]
lo_ok = hi_ok = True; lo_gap = hi_gap = mp.inf
for t in grid:
    v = Phi(mp.mpf(1), t); L = t * (4 * mp.log(2) + mp.log(1 / t)); U = t * (3 + mp.log(1 / t))
    lo_ok &= v >= L * (1 - mp.mpf(10) ** -300); hi_ok &= v <= U * (1 + mp.mpf(10) ** -300)
    lo_gap = min(lo_gap, (v - L) / t); hi_gap = min(hi_gap, (U - v) / t)
print("Lemma A on %d points t in [1e-80, 1]: lower holds %s (min (Phi-L)/t = %s, 0 at t=1), upper holds %s (min (U-Phi)/t = %s)" % (
    len(grid), lo_ok, mp.nstr(lo_gap, 5), hi_ok, mp.nstr(hi_gap, 5)))
mp.mp.dps = 120
# 3. corollary on random (l, m), both orders, across 60 decades
random.seed(3); cor = True
for _ in range(20000):
    l = mp.mpf(10) ** (-random.uniform(0, 60)); m = mp.mpf(10) ** (-random.uniform(0, 60))
    cor &= Phi(l, m) <= m * (3 + max(mp.mpf(0), mp.log(l / m))) * (1 + mp.mpf(10) ** -90)
print("corollary Phi(l,m) <= m(3 + ln_+(l/m)) on 20000 random pairs over 60 decades:", cor)
# 4. the new explicit bound
a3 = 3 + mp.log(4) + 2 / mp.e
g3 = lambda I: I * (a3 + 2 * mp.log(1 / I))
q = 2 / (3 * mp.sqrt(3))
B3 = sum(g3(q ** j) + g3(q ** j / 2) for j in range(0, 600))
C = 2 * mp.log(4); a = 1 + mp.log(4) + 2 / mp.e; g = lambda I: I * (a + 2 * mp.log(1 / I))
Bold = C * sum(g(q ** j) + g(q ** j / 2) for j in range(0, 600))
print("explicit uniform bound now: sup_trees D_k/I_k <= %s nats (was %s with the numeric C = 2 ln 4)" % (mp.nstr(B3, 8), mp.nstr(Bold, 8)))
# 5. controls: the gain bound g3 on random trees (exact recursion, 300 digits)
worst = mp.mpf(0); n = 0; skipped = 0; worst_r = mp.mpf(0)
with mp.workdps(300):
    for trial in range(400):
        st = (mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(0), mp.mpf(0))
        for Lv in range(random.randint(1, 14)):
            s = random.choice([2, 2, 3, 4, 5, 6, 8, 12, 20, 40])
            if 1 - abs(st[0]) < mp.mpf(10) ** -200: skipped += 1; break
            r0, I0 = st[4] / st[2], st[2]; st = step(st, s); n += 1
            worst = max(worst, (st[4] / st[2] - r0) / g3(I0)); worst_r = max(worst_r, st[4] / st[2])
print("controls on %d random steps: max gain / g3(I) = %s (<= 1), max D/I seen %s (<= %s); cut short %d" % (
    n, mp.nstr(worst, 6), mp.nstr(worst_r, 8), mp.nstr(B3, 6), skipped))
print("all checks pass:", neg and abs(G1 - 4 * ln2) < mp.mpf(10) ** -50 and lo_ok and hi_ok and cor and worst <= 1 and worst_r <= B3)
