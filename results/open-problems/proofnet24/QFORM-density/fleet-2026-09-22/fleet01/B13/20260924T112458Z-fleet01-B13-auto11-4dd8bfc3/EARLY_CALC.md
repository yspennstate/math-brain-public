SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-24T11:24:58.245005Z.
attacking: pay the translation-gradient misalignment endpoint from fleet02/B13 r13 by converting its weighted L1 affine defect into exterior-product currency, then use the physical rank-one-pair transverse-affine smoother to force either true quadratic product-set spread or a diffuse affine-wedge packet.

# Early calculation — affine-gradient wedge compiler

Full unrestricted QFORM remains OPEN; continuity remains separate.

Use the corrected designated-partner normal form from fleet02/B13 r13:

A = M_C + F,
M_C = D_C + lambda v v^T, |C|<=4, s_3(M_C)>=s_*,
F = D_(C^c) + mu w w^T,
||D_(C^c)||op <= C_D/rho,
|mu| <= C_u/rho^2,
C_D=2sqrt(30 pi), C_u=32sqrt(6)e.

For an optimizer-free finite-union unit-product witness E and partner trimming G=prod G_i, write p=rho ell, ell=|J|. Put

kappa_i = inf_(alpha,beta) esssup_(x in G_i) |x^2-alpha x-beta|,
S_kappa=sum_i kappa_i^2.

Choose the partner shell centers m_i, so radii r_i<=8 kappa_i. Define on H=C^c

g_i = 2 d_i m_i + 2 mu w_i (w^T m),
Gamma = inf_alpha sum_(i in H) kappa_i |g_i-alpha v_i|.

The corrected partner theorem gives

8 Gamma + 64 A_rho S_kappa >= p/(8 K_core),
A_rho=(C_D+C_u/rho)/rho.                                      (E1)

New scale split: if 64 A_rho S_kappa >= ell/2 then

S_kappa >= p/[128(C_D+C_u/rho)].                                (E2)

Otherwise the centered Taylor remainder of F on G is <ell/2. Since total trimmed marginal mass is <=p/2, the full Taylor affine core

Q_aff(x)=x^T M_C x + 2(Fm)^T x - m^T Fm

has mass >=p/2 in an interval of length <2ell, hence slab ratio >=rho/4. If rho>=8K_core, (E1) also yields

Gamma >= p/(128 K_core).                                        (E3)

For i,j in H put

D_ij=v_i g_j-v_j g_i.

Condition Q_aff on every original coordinate except i,j. Its pair quadratic block is lambda v_I v_I^T; every conditioned rank-one-core cross term is parallel to v_I, so the transverse affine coefficient is exactly D_ij/||v_I||. The source-pinned physical pair theorem QFORM-RANK1-PAIR-TRANSVERSE-AFFINE-v1 therefore gives, whenever D_ij!=0,

||p_Qaff||inf <= 6 |lambda|^(-1/3)|D_ij|^(-2/3).                (E4)

Since Q_aff has interval ratio >=rho/4,

|D_ij| <= (24/rho)^(3/2)|lambda|^(-1/2)                         (E5)

for every pair i<j in H (zero pairs satisfy this trivially).

Now use the exact exterior identity

W^2:=sum_(i<j) D_ij^2
 = ||v_H||_2^2 ||g_H||_2^2-(v_H^T g_H)^2
 = q^2 dist_2(g_H,span(v_H))^2, q=||v_H||_2.                   (E6)

If q>0, take the L2 projection alpha_2=(v_H^Tg_H)/q^2. Cauchy-Schwarz gives

Gamma <= sqrt(S_kappa) dist_2(g_H,span(v_H))
       = sqrt(S_kappa) W/q.                                     (E7)

Under the small-remainder branch, S_kappa < p/[128(C_D+C_u/rho)]. Combining (E3),(E7) gives the aggregate lower bound

W^2 > q^2 p(C_D+C_u/rho)/(128 K_core^2).                        (E8)

Thus high density forces a genuine diffuse affine-wedge packet: every individual physical pair area is O(rho^(-3/2)) by (E5), but their total squared area is bounded below by (E8). Quantitatively, if lambda*q !=0,

N_eff := W^2/(max_(i<j)|D_ij|^2)
 > |lambda| q^2 p rho^3(C_D+C_u/rho)/(1,769,472 K_core^2).      (E9)

Since W^2 is a sum of pair squares, at least N_eff physical pair modes must be nonzero (in the obvious ceiling sense when N_eff>1).

This is a new aggregate-before-inversion compiler. It does not select one minor, rotate the random variables, discard F, or assume connected supports. The remaining analytic gap is an aggregate receiver for a rank-one grouped core whose transverse affine wedge is spread across many tiny physical pairs.
