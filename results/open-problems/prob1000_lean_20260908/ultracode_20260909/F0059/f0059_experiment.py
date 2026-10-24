# Two-scale criterion vs exact probabilities for sparse irregular weight sequences.
# rho = 1 throughout (w_k^{1/k} -> 1 along the support). h(k) = log(k w_k)/k.
# At n = C*b (b a support point) and m = round(lam*n) we compute exactly
#   P(Y(1) >= b) = 1 - Z_{<b}(m,n)/Z(m,n)
# and the predicted log-odds from the tilt criterion:
#   log(A1/A0) ~ log n + log w_b + b log t - log Phi_<(t),  Psi_<(t) = (m-b)/(n-1).
import math, numpy as np, sys
from f0059_dp import logZ_table, tilt_root, logPhi

def run(name, supp, w, lam, C, targets):
    logw = {k: math.log(w[k]) for k in supp}
    print("== %s   lam=%g C=%d" % (name, lam, C))
    print("   support:", supp)
    print("   h(k)=log(k w_k)/k:", ["%d:%.4f" % (k, math.log(k*w[k])/k) for k in supp if k>0])
    for b in targets:
        n = C*b; m = int(round(lam*n))
        if lam == 1: m = n-1
        Z = logZ_table(logw, supp, n, m)
        Zc = logZ_table(logw, [k for k in supp if k < b], n, m)
        logZ, logZc = Z[n,m], Zc[n,m]
        p = 1 - math.exp(logZc - logZ)
        x = logZ - logZc
        exact_logodds = (math.log(math.expm1(x)) if 0 < x < 700 else (x if x >= 700 else -37.0))
        # free-energy prediction summed over i = number of b-boxes:
        # log A_i - log A_0 ~ log C(n,i) + i log w_b + [(n-i) log Phi_<(t_i) - (m-ib) log t_i] - [n log Phi_<(t_0) - m log t_0]
        def F(mm, nn):
            tt = tilt_root(w, supp, b, mm/nn); return nn*logPhi(w, supp, b, tt) - mm*math.log(tt)
        F0 = F(m, n)
        terms = []
        kmax_below = max(k for k in supp if k < b)
        for i in range(1, m//b + 1):
            if n - i <= 0 or m - i*b < 0 or (m - i*b) >= kmax_below*(n-i): break
            terms.append(math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1) + i*logw[b] + F(m-i*b, n-i) - F0)
        pred = terms[0]; predall = np.logaddexp.reduce(terms)
        t = tilt_root(w, supp, b, (m-b)/(n-1))
        # prior-record scale below b and the gap
        below = [k for k in supp if 0 < k < b]
        hb = math.log(b*w[b])/b
        a = max(below, key=lambda k: math.log(k*w[k])/k)
        ha = math.log(a*w[a])/a
        print("   b=%5d n=%6d m=%6d  P(Y1>=b)=%.6f  exact log-odds=%9.3f  pred(i=1)=%9.3f pred(all i)=%9.3f  tilt t-1=%.5f  argmax_below=%d  b*(h(b)-h(a))=%8.3f"
              % (b, n, m, p, exact_logodds, pred, predall, t-1, a, b*(hb-ha)))
    sys.stdout.flush()

# Example 1: Janson-type support, weights (k+1)^-4 (h increasing => every scale a record)
supp1 = [0,1,2,6,24,120,720]
w1 = {k: (k+1.0)**-4 for k in supp1}
if "part2" not in sys.argv and "part3" not in sys.argv: run("E1 (k+1)^-4 on {0,1,2,6,24,120,720}", supp1, w1, 1.0, 3, [24,120,720])

# Example 2: same support, but h made NON-monotone: kill scale 120 (tiny weight) so that
# 120 is not a record (h(120) < h(24)); keep 720 a record.
w2 = dict(w1); w2[120] = math.exp(-0.5*120)/120   # h(120) = -0.5, far below h(24)
w2[720] = 0.3/720                                # h(720) = log(0.3)/720 ~ -0.0017, a record
if "part2" not in sys.argv and "part3" not in sys.argv: run("E2 scale 120 killed, 720 record", supp1, w2, 1.0, 3, [24,120,720])

# Example 3: 720 a record but with a small gap over the best lower scale (24):
# h(24) = log(24 w_24)/24 ; choose w_720 so that 720*(h(720)-h(24)) = +2 only.
w3 = dict(w1)
h24 = math.log(120*w1[120])/120   # the true argmax below 720 is scale 120
w3[720] = math.exp(720*(h24 + 2.0/720))/720
if "part2" not in sys.argv and "part3" not in sys.argv: run("E3 720 record with gap b*(h(b)-h(a))=+2", supp1, w3, 1.0, 3, [720])
if "part3" not in sys.argv: run("E3b same weights, C=2 (two b-boxes could fit only if excess allows)", supp1, w3, 1.0, 2, [720])
# Example 4: 720 just BELOW the record level (gap -2): predicted absent-ish
w4 = dict(w1); w4[720] = math.exp(720*(h24 - 2.0/720))/720
if "part3" not in sys.argv: run("E4 720 below record by b*gap=-2", supp1, w4, 1.0, 3, [720])
# Example 5: lam = 2 (m = 2n) to leave the tree case
run("E5 lam=2, weights (k+1)^-4", supp1, w1, 2.0, 2, [120,720])
run("E6 lam=2, E2 weights", supp1, w2, 2.0, 2, [120,720])
