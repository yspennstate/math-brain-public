"""The two lemmas that finish Problem 3.3.

For a two-point measure with atoms at -a and b (a,b>0, a+b<=1), stationarity of xi at the origin fixes
the weights, and with A=a^2+s, B=b^2+s, s=R^2:

    xi(0)-1 has the sign of  Phi = b*A*(1-A) + a*B*(1-B),
    xi''(0) has the sign of  Psi = b*B*(3a^2-s) + a*A*(3b^2-s).

LEMMA A.  Psi >= 0 forces s <= 3/4, with equality only at a=b=1/2.
LEMMA B.  If s <= 3/4 then Phi >= 0, with equality only at a=b=1/2, s=3/4.

Together with the fact that any measure whose xi is stationary at the origin is a mixture of such pairs
taken from its own support, they give xi(0) >= 1 whenever xi''(0) >= 0 -- the whole theorem.
"""
import numpy as np

n = 1200
a = np.linspace(1e-4, 1.0, n)[:, None]
b = np.linspace(1e-4, 1.0, n)[None, :]
inside = (a + b <= 1.0)

print("LEMMA A: largest s admitting Psi >= 0, scanned over all pairs")
worst_s, arg = 0.0, None
for s in np.linspace(0.01, 1.2, 240):
    A = a * a + s; B = b * b + s
    Psi = b * B * (3 * a * a - s) + a * A * (3 * b * b - s)
    ok = inside & (Psi >= 0)
    if ok.any():
        worst_s = s
        i, j = np.unravel_index(np.argmax(np.where(ok, Psi, -np.inf)), ok.shape)
        arg = (float(a[i, 0]), float(b[0, j]))
print(f"  largest s with an admissible pair: {worst_s:.4f}   (claim: 3/4 = 0.75)")
print(f"  attained near a = {arg[0]:.4f}, b = {arg[1]:.4f}   (claim: 1/2, 1/2)")

print("\nLEMMA B: smallest Phi over all pairs, for s up to 3/4")
worst = (np.inf, None)
for s in np.linspace(1e-3, 0.75, 300):
    A = a * a + s; B = b * b + s
    Phi = b * A * (1 - A) + a * B * (1 - B)
    v = np.where(inside, Phi, np.inf)
    m = v.min()
    if m < worst[0]:
        i, j = np.unravel_index(v.argmin(), v.shape)
        worst = (float(m), (float(a[i, 0]), float(b[0, j]), s))
print(f"  smallest Phi: {worst[0]:.8f}   (claim: >= 0)")
print(f"  at a = {worst[1][0]:.4f}, b = {worst[1][1]:.4f}, s = {worst[1][2]:.4f}")
