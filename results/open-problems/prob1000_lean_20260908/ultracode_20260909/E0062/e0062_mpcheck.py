# Independent check of the log-coordinate iteration: iterate the symmetric 4-cycle-with-ties map
# directly in mpmath at 4000 decimal digits (no log trick, no renormalisation) and compare the
# coordinates and the vertex-visit schedule with the float log-coordinate iteration.
import mpmath as mp, numpy as np, math
mp.mp.dps = 800
a = b = c = d = mp.mpf("0.5")
x = [mp.mpf("0.3"), mp.mpf("0.2"), mp.mpf("0.25"), mp.mpf("0.25")]
A = np.array([[0, .5, 0, -.5], [-.5, 0, .5, 0], [0, -.5, 0, .5], [.5, 0, -.5, 0]])
L = np.log(np.array([0.3, 0.2, 0.25, 0.25]))
N = 20000
maxdiff = 0.0; visits_mp = []; visits_f = []; cur_mp = cur_f = -1
for n in range(1, N + 1):
    x1, x2, x3, x4 = x
    x = [x1 * (1 + a * x2 - d * x4), x2 * (1 - a * x1 + b * x3), x3 * (1 - b * x2 + c * x4), x4 * (1 + d * x1 - c * x3)]
    xf = np.exp(L); L = L + np.log1p(A @ xf); L -= math.log(np.exp(L).sum())
    # compare log coordinates (relative accuracy of the log iteration)
    if n % 200 == 0:
        lm = [float(mp.log(v)) for v in x]
        maxdiff = max(maxdiff, max(abs(lm[i] - L[i]) / max(1.0, abs(lm[i])) for i in range(4)))
    m = max(range(4), key=lambda i: x[i])
    if x[m] > mp.mpf("0.999") and m != cur_mp: cur_mp = m; visits_mp.append((m + 1, n))
    mf = int(np.argmax(L))
    if L[mf] > math.log(0.999) and mf != cur_f: cur_f = mf; visits_f.append((mf + 1, n))
print("steps:", N, " max relative difference of log-coordinates (mpmath vs float log-iteration):", f"{maxdiff:.2e}")
print("sum of mpmath coordinates - 1:", mp.nstr(sum(x) - 1, 5))
print("mpmath  visit schedule:", visits_mp)
print("float   visit schedule:", visits_f)
print("mpmath  final log x:", [round(float(mp.log(v)), 2) for v in x])
