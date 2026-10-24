SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T20:38:19Z.
attacking: the near-coloop/near-planar exact-null-hub puncture via the latest account03/B18 private-bank theorem and a nonaligned private-bank Fresnel--Brascamp--Lieb aggregation.

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

## Early substantive implication

Work in the exact null-hub form

Q = 2 (X0 + ell.X_L)(g.X_L) + d (beta.X_L)^2,

with independent original-coordinate cap-one inputs, ||beta||_2=1, beta.g=0, gamma=||g||_2>0 and d!=0. Let L=J disjoint_union K be a literal source split with g_K=0 and rho=||beta_K||_2>0. Decompose

ell_K = a beta_K + r,   a=(ell_K.beta_K)/rho^2,   r perp beta_K,
eta=||r||_2.

For eta>0 put b=beta_K/rho and v=r/eta. Then b,v are orthonormal coefficient vectors on the original K bank. If every K-coordinate satisfies

b_k^2 + v_k^2 <= 1/2,

then the following Fourier calculation is source-valid and does not infer independence of b.X_K and v.X_K.

Write G=g_J.X_J, C=beta_J.X_J and S=X0+ell_J.X_J. Exact completion gives

Q = R_J + d rho^2 (b.X_K + c_J)^2 + 2 eta G (v.X_K),

where c_J=(C+aG/d)/rho and R_J=2SG-2aCG-a^2G^2/d depends only on the outside source block. For fixed J, Fresnel linearisation of the square and product factorisation on K give

|phi_Q(t)|
 <= (4 pi |t d| rho^2)^(-1/2)
    E_J int_R prod_{k in K} |psi_k(b_k u + 2t eta G v_k)| du.

If M_G=||p_G||_infinity, change y=2t eta G and drop all outside phases:

|phi_Q(t)|
 <= (4 pi |t d| rho^2)^(-1/2) [M_G/(2|t|eta)]
    int_{R^2} prod_{k in K}|psi_k(b_k u+v_k y)| du dy.

The rows (b_k,v_k) form a Parseval frame in R^2. With c_k=b_k^2+v_k^2<=1/2, the normalized geometric Brascamp--Lieb inequality plus the pinned e5f L^p estimate int |psi_k|^p <=4pi/sqrt(p), p>=2, gives the exact bound

int_{R^2} prod_k |psi_k(b_k u+v_k y)| du dy <= (4pi)^2.

Therefore

|phi_Q(t)| <= 4 pi^(3/2) M_G [rho eta sqrt(|d|)]^(-1) |t|^(-3/2).

Integrating min(1,B|t|^(-3/2)) and Fourier inverting yields

||p_Q||_infinity
 <= 3*2^(4/3) M_G^(2/3) (rho^2 eta^2 |d|)^(-1/3).

Livshyts--Paouris--Pivovarov Theorem 1.1 applies to the genuine J-product source and gives M_G<=sqrt(2)/gamma, hence

||p_Q||_infinity
 <= 3*2^(5/3) [|d| gamma^2 rho^2 eta^2]^(-1/3).

Moreover phi_Q is integrable, so this branch has a continuous C_0 density. This is the nonaligned/diffuse complement to account03/B18 r34: r34 pays eta=0 (alignment) through a random-centre square; the calculation above aggregates a diffuse source-private K bank when eta>0 without selecting one tiny coordinate.

A strict quantitative stress family will use beta=(1,...,1)/sqrt(m) and a unit v with distinct coordinate ratios v_j/beta_j and max_j(beta_j^2+v_j^2)<=1/2. Then every r34-aligned private subbank is a singleton and its rho is 1/sqrt(m), whereas the aggregate bound above is dimension-free.
