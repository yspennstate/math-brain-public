# Pointwise inner integrals at 30 digits (mpmath), T=2, d=1, after shifting by the others' common answer v:
#   step 1: record i answers a1=-1, the others v1=+1.  Weights at g1 (density factors of the step-1 output):
#     wa = phi(g1 - (a1 - v1)) / 2  [P, i in batch 1]   w0 = phi(g1 + v1) / 2 [Q, i in batch 1]   wc = phi(g1)/2 [i in batch 2]
#   step 2, mode ANTI (a2=1, v2=-1, the conjectured pair): P: wa N(0) + wc N(2);  Q: w0 N(0) + wc N(1)
#   step 2, mode SAME (a2=v2=1):                           P: wa N(0) + wc N(0);  Q: w0 N(0) + wc N(-1)
# I_mode(g1) = int (p - e^eps q)_+ dg2.  The conjectured pair's D(P_S||Q_S) = int I_anti dg1.
import mpmath as mp
mp.mp.dps = 30
s, eps = mp.mpf(1), mp.mpf('0.5')
E = mp.e ** eps
phi = lambda x: mp.npdf(x, 0, s)
def I(g1, mode):
    wa, w0, wc = phi(g1 + 2) / 2, phi(g1 + 1) / 2, phi(g1) / 2
    if mode == "anti": f = lambda y: max(0, wa * phi(y) + wc * phi(y - 2) - E * (w0 * phi(y) + wc * phi(y - 1)))
    else:              f = lambda y: max(0, wa * phi(y) + wc * phi(y) - E * (w0 * phi(y) + wc * phi(y + 1)))
    return mp.quad(f, [-14, -3, -1, 0, 1, 2, 3, 14])
for g1 in ["-4", "-3", "-2.5", "-2", "-1.5", "-1.2", "-1", "-0.5", "0"]:
    x = mp.mpf(g1); a, b = I(x, "anti"), I(x, "same")
    print("g1 %5s  I_anti %s  I_same %s  diff %s" % (g1, mp.nstr(a, 12), mp.nstr(b, 12), mp.nstr(b - a, 6)), flush=True)
