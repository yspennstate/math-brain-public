# From mu-hat(xi) = c(xi) mu-hat(2 xi/3) with c(xi) = (1+e^{-2 pi i xi/3})/2, |c|^2 = cos^2(pi xi/3):
#   I = int |mu-hat|^2 dxi = (3/2) int cos^2(pi eta/2) |mu-hat(eta)|^2 deta  (substitute eta = 2xi/3)
#     = (3/4) I + (3/4) int cos(pi eta) |mu-hat|^2 deta
# so  I = 3 * A(1/2),  A(t) = int f(x) f(x+t) dx  (Plancherel: int |mu-hat|^2 cos(pi eta) deta = A(1/2)).
# PREDICTION: ||f||_2^2 = 3 * int_0^{1/2} f(x) f(x+1/2) dx.   Check it on the solver density.
import numpy as np
R = 3*2**18
c = np.full(R, 1.0/R); edges = np.arange(R+1)/R
for _ in range(90):
    F = np.concatenate([[0.0], np.cumsum(c)]); new = np.zeros(R)
    for B in (0,1):
        a = (3*edges[:-1]-B)/2; b = (3*edges[1:]-B)/2
        new += 0.5*(np.interp(b, edges, F, left=0, right=1) - np.interp(a, edges, F, left=0, right=1))
    c = new/new.sum()
f = c*R; dx = 1.0/R; half = R//2
L2 = float(np.sum(f*f)*dx)
A_half = float(np.sum(f[:half]*f[half:])*dx)
print(f"||f||_2^2            = {L2:.6f}")
print(f"3 * A(1/2)           = {3*A_half:.6f}      (A(1/2) = {A_half:.6f})")
print(f"relative difference  = {abs(L2-3*A_half)/L2:.3e}")
# same identity one level down, as a control: the analogous relation at shift 1/2 for T_2 mu should NOT hold
g = c[:half] + c[half:]; fg = g*(g.size); dg = 1.0/g.size; hg = g.size//2
L2g = float(np.sum(fg*fg)*dg); Ag = float(np.sum(fg[:hg]*fg[hg:])*dg)
print(f"control on T_2 mu: ||g||_2^2 = {L2g:.6f} vs 3*A_g(1/2) = {3*Ag:.6f}  (should NOT match)")
