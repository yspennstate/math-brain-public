"""Audit 2, eps>0 remainder uniform in n: the cubic Taylor remainder of psi(y) = (s+eps)/(s sqrt(y)+eps) at y = 1, measured
directly as sup |psi(y) - 1 - p1 u - p2 u^2/2 - p3 u^3/6| / u^4 over the y range the stream can reach (u = y - 1), with
p1, p2, p3 from the hand series (no derivative formula). 9/-1 model, |x| <= rho, V = x^2 + B2, y in [min g^2/V, max g^2/V]."""
import numpy as np
for rho in (0.5, 0.1):
    xs = np.linspace(-rho, rho, 201); B2 = 9.0
    ymin = min(min((x-1)**2, (x+9)**2)/(x*x+B2) for x in xs); ymax = max(max((x-1)**2, (x+9)**2)/(x*x+B2) for x in xs)
    y = np.linspace(ymin, ymax, 400001); u = y - 1; u = u[np.abs(u) > 1e-3]; y = 1 + u
    print(f"rho {rho}: y in [{ymin:.4f}, {ymax:.3f}]")
    for eps in (0, 0.1, 1, 3, 10, 100, 1e4):
        s = 3.0; r = s/(s+eps); p1 = -r/2; p2 = r/4 + r*r/2; p3 = -(3/8)*(r + 2*r*r + 2*r**3)
        psi = (s+eps)/(s*np.sqrt(y)+eps); R = psi - 1 - p1*u - p2*u**2/2 - p3*u**3/6
        q = np.abs(R)/u**4; i = q.argmax()
        near = np.abs(u) < 0.05
        print(f"  eps {eps:<6} r {r:.4f}  sup|R|/u^4 {q.max():.4g} at y {y[i]:.4f}   sup/r {q.max()/r:.4g}   near u=0: {q[near].max():.4f} (series 35/128 r-scaled check)")
