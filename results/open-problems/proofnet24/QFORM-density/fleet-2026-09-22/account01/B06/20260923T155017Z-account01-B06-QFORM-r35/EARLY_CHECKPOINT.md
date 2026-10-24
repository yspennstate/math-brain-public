SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T15:50:17Z.
attacking: non-null scalar/dependent-pair interpolation — integrate the scalar quadratic oscillation against the full product-derived two-plane Fresnel transform before any curved-fiber supremum.

# Early substantive checkpoint

Status: useful partial derivation; full QFORM remains OPEN. Execution label: WITHOUT_VERIFIED_BRAIN.

## Candidate theorem under active proof

Let X be an independent cap-one scalar. Let Z have independent cap-one coordinates and let V be an m x 2 matrix with orthonormal columns whose row leverages satisfy max_j ||v_j||^2 <= 1/2. Set Y=V^T Z. For a symmetric invertible 3 x 3 block

B = [[a,b^T],[b,C]],

with C invertible symmetric 2 x 2, consider

Q = a X^2 + 2 X b^T Y + Y^T C Y.

The working derivation gives

||p_Q||_infinity <= C_IF |det C|^(-1/8)|det B|^(-1/4),
C_IF = (2/(3 pi)) 6^(1/4) [pi e 2^(4/3)(2pi)^(1/3)5^(2/3)]^(3/4)
     = 11.7473500925...,

and in fact an L1 characteristic function, hence a continuous density.

The key exact identity after Fourier inversion of the 2D projected density is

|phi_Q(t)| <= (4pi)^(-1)|t|^(-1)|det C|^(-1/2)
              int |hat g(xi)| |F_{b^T C^(-1)xi}(t)| dxi,

where

F_eta(t)=int f(x) exp(i t s x^2-i eta x) dx,
s=a-b^T C^(-1)b=det B/det C.

Product structure is retained through the projection-Fourier estimate

||hat g||_1 <= (2pi)^2 e

when the two-plane row leverages are <=1/2. For every eta,

||F_eta||_3 <= (2pi)^(1/3)5^(2/3)|s|^(-1/3),

because the complex pushforward of f(x)e^{-i eta x} under x -> s x^2 is dominated by the positive square pushforward h_s and

int h_s^(3/2) <= 5 |s|^(-1/2).

Therefore, for T>0,

int_{|t|>T}|phi_Q(t)|dt
 <= K0 |det C|^(-1/6)|det B|^(-1/3) T^(-1/3),
K0=pi e 2^(4/3)(2pi)^(1/3)5^(2/3)=116.1067961106... .

Adding the trivial low-frequency contribution 2T and optimizing at T=(A/6)^(3/4) gives the stated constant.

## Exact rank-one light-curvature endpoint from newest-Claude MF

If instead C has rank one, write C=lambda ss^T and decompose b=beta s+gamma q with q perpendicular to s. Invertibility of B forces gamma !=0 and

|det B|=|lambda| gamma^2.

The newest-Claude mixed-Fresnel theorem applies with one heavy scalar and one light square direction. Its Gram determinant is gamma^2, so

||p_Q||_infinity <= 3*4^(2/3)|det B|^(-1/3)=7.5595262994... |det B|^(-1/3),

with a continuous density. This holds for arbitrary scalar pivot a, so it genuinely extends the already-paid exact-null scalar endpoint in this rank-one-light regime.

## Partner account02/B06 actual inequality

The latest designated partner theorem gives, for an exact physical null bank and cross matrix M with top singular values s1>=s2>0,

||p_Q||_infinity <=2 sqrt(pi)/sqrt(s1 s2).

Thus any occurrence in the current reduction with a null product bank and s1 s2 >= eta^2 is immediately paid by 2 sqrt(pi)/eta. This is retained as a branch exit, while the main new calculation attacks the non-null coupled scalar/two-plane regime.

## Current first gap

After the two results above, the diffuse-coloop interpolation is paid at the exact rank-one light-curvature endpoint and for invertible C bounded away from rank one. The remaining analytic seam is the near-rank-one nonzero indefinite light curvature: 0<|det C|<<1. The new bound blows only as |det C|^(-1/8), while the exact endpoint is bounded by mixed Fresnel. The next target is a product-preserving stability/interpolation that bridges those estimates without treating a small matrix coefficient as a small random quadratic perturbation.
