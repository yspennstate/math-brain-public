try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Recompute every constant of the PSD theorem; check the analytic inequalities numerically.
import numpy as np
from scipy import integrate

e = np.e; pi = np.pi
# Fejer kernel constant
fej = 1 / (2 * np.sin(1.0) ** 2)
print("Fejer constant 1/(2 sin^2 1) =", fej)
# check hat k: int (sin x/x)^2 e^{i tau x} dx = pi (1 - |tau|/2)_+
for tau in (0.0, 0.5, 1.3, 2.5):
    f = lambda x: (np.sinc(x / pi)) ** 2 * np.cos(tau * x)
    val, err = integrate.quad(f, -2000, 2000, limit=4000)
    print(f"  hat k({tau}) numeric {val:.5f}  formula {pi*max(0,1-abs(tau)/2):.5f}")
a1_fac = fej * 4 * np.sqrt(2)          # alpha_1 <= a1_fac * B   when |phi| <= B |t|^{-1/2}
a2_fac = fej * 2                       # alpha_2 <= a2_fac * B   when |phi| <= min(1, B/|t|), B >= 2
print("alpha_1 factor", a1_fac, " alpha_2 factor", a2_fac)

# no-pivot PSD thresholds and bounds
for k, c in ((1, 1 / 128), (2, 1 / 300), (3, 1 / 640)):
    fail = (2 * k + 16 * k + 64 * k * k) * c
    marg = 64 * k * c
    print(f"level {k}: c = 1/{round(1/c)} failure <= {fail:.4f} (<1), marginal <= {marg:.4f} (<=1/2)")
B1 = e ** 0.25 * np.sqrt(2 * pi) * 2          # Z_1^{-1/4} <= 2
H1 = a1_fac * B1
B2 = e ** 0.5 * 2 * pi * 4                    # Z_2^{-1/4} <= 4
H2 = a2_fac * B2
H3 = 6 * np.sqrt(e) * 4                       # Z_3^{-1/6} <= 4
print("B1", B1, "H1", H1, "| B2", B2, "H2", H2, "| H3", H3)

c1, c2, c3 = 1 / 128, 1 / 300, 1 / 640
A1 = max(4 * c1 ** -0.5, H1)
A2 = max(4 * np.sqrt(2) * c2 ** -0.5 * max(A1, 1), H2)
C1comp = lambda K, Kp: K * 3 * np.sqrt(Kp * (3 + np.log(Kp)))
C = max(C1comp(c3 ** -0.5, A2), H3)
print("A1", A1, "A2", A2, "C", C)

# check the layer-cake bound used in (C1): int_0^inf min(1, K' v^{-2}(1+2 log v) for v>=1, 1 for v<1) dv <= 3 sqrt(K'(3+log K'))
for Kp in (1.0, 10.0, 100.0, 4433.0, 1e6):
    f = lambda v: min(1.0, Kp * v ** -2 * (1 + 2 * np.log(v))) if v >= 1 else 1.0
    val = integrate.quad(f, 0, 50, limit=500)[0] + integrate.quad(f, 50, 1e5, limit=500)[0] + Kp * (3 + 2 * np.log(1e5)) / 1e5
    print(f"  (C1) K'={Kp:g}: layer cake {val:.3f} <= 3 sqrt(K'(3+log K')) = {3*np.sqrt(Kp*(3+np.log(Kp))):.3f}")
# check (C2) kernel bound: int_{-u}^{u} |y+d|^{-1/2} dy <= 4 sqrt2 u / sqrt(max(|d|,u))
worst = 0
for u in (1e-3, 0.1, 1.0):
    for d in np.linspace(0, 5, 101):
        val = integrate.quad(lambda y: abs(y + d) ** -0.5, -u, u, points=[-d] if abs(d) < u else None, limit=200)[0]
        worst = max(worst, val / (4 * np.sqrt(2) * u / np.sqrt(max(d, u))))
print("  (C2) max ratio kernel/bound:", worst)
# (C2) second step: int_0^{u^{-1/2}} min(1, K'/v) dv <= K'(1 + (1/2) log(1/u)) for K' >= 1, u <= 1
worst = 0
for Kp in (1.0, 3.0, 45.25):
    for u in (1e-8, 1e-4, 1e-2, 0.5, 1.0):
        U = u ** -0.5
        val = (min(U, Kp) + (Kp * np.log(U / Kp) if U > Kp else 0.0))
        worst = max(worst, val / (Kp * (1 + 0.5 * np.log(1 / u))))
print("  (C2) max ratio layer/bound:", worst)
