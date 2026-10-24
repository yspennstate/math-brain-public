SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T19:18:01Z.
attacking: convert the r30 E2→E3 spectral lift into a marginal-free overlap funnel using the new physical cross-E3 receiver, then identify the forced overlap-one/two determinant geometry in the latest account02/B07 rank-two carrier state.

# Early substantive calculation

Let A be real symmetric with sigma_3(A)>=1. Let eta_(I,J) in [0,1] be any fractional E2 packet supported on disjoint physical row/column banks, with mass

Omega = sum eta_(I,J) det A[I,J]^2.

By r30's spectral-extension theorem, the induced fractional E3 lift has total mass at least Omega/9 and only overlap classes h=0,1,2. Write those masses Z0,Z1,Z2.

Use the fresh marginal-free physical cross-E3 theorem QFORM-CROSS-E3-MARGINALFREE-L1-v1 with constant
C_E3=3*2^(4/3)*exp(1/3).

Fix tau in (0,1/9). If Z0>=tau Omega, h=0 coarse role-coloring retains at least Z0/64 inside one literal disjoint physical cross block. Its full E3 volume is at least tau Omega/64, hence

||p_Q||_infinity <= C_E3 (64/tau)^(1/6) Omega^(-1/6),

with a continuous C_0 density.

If Z0<tau Omega, then Z1+Z2>(1/9-tau)Omega. Coarse role coloring retains P1>=(16/3125)Z1 and P2>=(1/64)Z2. Therefore

max(P1,P2) >= (16/4149)(Z1+Z2)
            > [16(1/9-tau)/4149] Omega.

At tau=1/144 this becomes the clean dichotomy

(continuous payment) ||p_Q||_infinity <= C_E3*9216^(1/6)*Omega^(-1/6) <48.308 Omega^(-1/6),

or

(role-consistent shared-coordinate packet) max(P1,P2) > 5 Omega/12447.

This removes the row-marginal gate from the entire overlap-zero branch. The only unpaid spectral extensions are now overlap one or overlap two, i.e. genuinely shared-coordinate third-minor geometry.

For the overlap-two raw lift there is an exact inverse-free principal-core identity. If I,J are disjoint physical pairs, H=I union J and B=A[H,H], then

sum_(r in J,c in I) det A[I union {r}, J union {c}]^2
 = ||Cof(B)[J,I]||_F^2
 = ||adj(B)[I,J]||_F^2.

Thus the h=2 part of the r30 fractional lift is exactly

Z2 = (1/9) sum_(I,J) eta_(I,J) ||adj(A[I union J,I union J])[I,J]||_F^2.

This identity keeps all determinant weights and never divides by det(B).

Full QFORM remains open; the next analytic debt is to spend the resulting overlap-one/two shared-coordinate packet while retaining arbitrary same-bank curvature and the genuine nonzero rough tail.
