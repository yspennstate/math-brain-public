SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T19:54:43Z.
attacking: a product-preserving private-transverse-bank smoother for the null-hub form, using the sharp one-dimensional product-projection density bound before the square singularity.

# Early calculation

Let

Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2,

with the usual exact-rank-three null-hub normalization: original coordinates independent with one-dimensional density caps 1, beta perpendicular to g, gamma=||g||_2>0, d != 0. Split the leaf indices as J disjoint_union K and assume only

- g_K = 0,
- beta_K != 0,
- ell_K = a beta_K for some real a.

There is no restriction on ell_J or beta_J. Put rho=||beta_K||_2, B=beta_K dot X_K, C=beta_J dot X_J, G=g dot X_J, L=ell_J dot X_J. Then

Q = 2(X_0+L+aB)G + d(B+C)^2
  = R + d(B + C + aG/d)^2,

where

R = 2X_0 G + 2LG - 2aCG - (a^2/d)G^2.

Thus, conditional on the J-bank, R is an affine function of the genuinely independent original coordinate X_0 with slope 2G. For fixed G=y !=0, the conditional density of R is capped by 1/(2|y|). For any probability density capped by m,

sup_t int |w-t|^(-1/2) f(w) dw <= 2 sqrt(2m),

by the one-dimensional bathtub principle. Consequently

sup_t E(|R-t|^(-1/2) | X_J) <= 2 |G|^(-1/2).

The sharp product-projection theorem of Livshyts--Paouris--Pivovarov applied to G/gamma gives ||p_G||_infinity <= sqrt(2)/gamma. A second bathtub step yields

E |G|^(-1/2) <= 2 sqrt(2) (sqrt(2)/gamma)^(1/2)
                  = 2^(7/4) gamma^(-1/2),

hence

H := sup_t E|R-t|^(-1/2) <= 2^(11/4) gamma^(-1/2).            (E1)

Independently, B is an original-product projection on the disjoint K-bank, so LPP gives

||p_B||_infinity <= sqrt(2)/rho.                                 (E2)

Conditioning on all variables outside K, the random square d(B+c)^2 has density envelope

p(s | outside K) <= [sqrt(2)/(rho sqrt(|d|))] |s|^(-1/2)         (E3)

on the sign-compatible half-line, uniformly in the random center c=C+aG/d. Therefore

||p_Q||_infinity
 <= [sqrt(2)/(rho sqrt(|d|))] H
 <= 2^(13/4) / [rho sqrt(|d| gamma)].                            (E4)

Numerically 2^(13/4)=9.513656920021768.

This does not use independence after a rotation: the only two projection bounds are applied separately to two literal disjoint original-coordinate product banks J and K. It does not use pointwise quadratic-phase decay, arbitrary-joint coarea, or a conditional density cap as independence. The completed report will check the target normalization and splice the designated fleet04/B18 result at a concrete inequality.