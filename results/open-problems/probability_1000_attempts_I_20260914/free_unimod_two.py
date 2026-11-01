"""The two-atom case of Problem 3.3, in closed form.

Atoms at -a and b with a, b > 0 and a + b <= 1 (the support has diameter at most one), the valley at
the origin.  Writing A = a^2+R^2 and B = b^2+R^2, the stationarity condition xi'(0) = 0 fixes the two
weights, and then

    xi(0) = (bA + aB) / (bA^2 + aB^2),        xi''(0) >= 0  <=>  bB(3a^2-R^2) + aA(3b^2-R^2) >= 0.

So xi(0) >= 1 is equivalent to  b*A*(1-A) + a*B*(1-B) >= 0, to be proved under the second condition.
This scans the whole admissible region for a violation.
"""
import numpy as np

worst = (np.inf, None)
viol = 0
for a in np.linspace(0.002, 1.0, 500):
    bs = np.linspace(0.002, min(1.0 - a, a), 400)
    if len(bs) == 0: continue
    for b in bs:
        R2 = np.linspace(1e-6, 3.0, 600)
        A = a * a + R2; B = b * b + R2
        ok = b * B * (3 * a * a - R2) + a * A * (3 * b * b - R2) >= 0     # xi''(0) >= 0
        if not ok.any(): continue
        F = (b * A + a * B) / (b * A * A + a * B * B)
        f = F[ok].min()
        if f < worst[0]:
            worst = (f, (a, b, float(R2[ok][F[ok].argmin()])))
        if f < 1 - 1e-9: viol += 1
print(f"minimum of xi(0) over all admissible two-atom configurations: {worst[0]:.8f}")
a, b, R2 = worst[1]
print(f"  attained at a = {a:.4f}, b = {b:.4f}, R^2 = {R2:.4f}  (R = {np.sqrt(R2):.4f})")
print(f"  grid points strictly below 1: {viol}")
