# fleet03/B10 r26 — substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status at checkpoint: supporting analytic theorem derived; full target OPEN; independent review pending.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First new calculation: triangular rank-two half-Riesz interpolation

Let `(W,Y)` admit regular conditional densities with

- `||p_Y||_infinity <= L`,
- `||p_{W|Y=y}||_infinity <= K` for a.e. `y`.

Let

`R=aW^2+2bWY+cY^2+dW+eY+f`,

and assume the quadratic determinant `Delta=ac-b^2` is nonzero. The candidate estimate is

`sup_t E |R-t|^(-1/2) <= 16 sqrt(2 K L) |Delta|^(-1/4).`    (1.1)

This is uniform as `a -> 0`; when `a=0`, the previously completed bilinear proof gives the sharper `4 sqrt(2KL)|b|^(-1/2)`.

For `a!=0`, complete the square only algebraically:

`R-t = a(W+h(Y))^2 + q_t(Y)`,

where `q_t` is a one-dimensional quadratic whose leading coefficient is

`kappa = c-b^2/a = Delta/a`.

For fixed `Y=y`, a bounded-density one-dimensional quadratic inverse-half estimate gives

`E(|R-t|^(-1/2)|Y=y)
 <= 4 sqrt(2K)|a|^(-1/4)|q_t(y)|^(-1/4)`                         (1.2)

outside the null set on which `q_t(y)=0`. The proof splits according to whether the completed scalar quadratic has two real roots or no real roots. In the real-root case, on the Voronoi cell of either root the other root is at least the half-separation away, and the standard inverse-half bound

`sup_h E|W-h|^(-1/2) <= 2 sqrt(2K)`

pays the local root. In the no-real-root case, `x^2+r^2 >= 2r|x|` reduces to the same inverse-half bound.

For any real quadratic polynomial `q(y)` with nonzero leading coefficient `kappa`, the universal sublevel estimate

`|{y: |q(y)|<eps}| <= 4 sqrt(eps/|kappa|)`                         (1.3)

implies, by layer cake and `p_Y<=L`,

`E|q(Y)|^(-1/4) <= 4 sqrt(L)|kappa|^(-1/4).`                       (1.4)

Combining (1.2)-(1.4), and using `|a kappa|=|Delta|`, proves (1.1).

This avoids scalar-pivot completion followed by a determinant-only rank-two estimate; that older route loses `|a|^(-1/4)` near a null hub. Here the singularity of the conditional quadratic in `W` is averaged against the original `Y` density before taking a worst fibre.

## 2. Near-null rank-three consequence with one genuine tangent innovation

In an exact-rank-three state choose a physical heavy row `r_0=sqrt(c)e`. Write the spectral matrix in `R e direct_sum e^perp` as

`Lambda = [[alpha, g^T],[g,T]]`.

Because `sigma_min(Lambda)>=1`, if `h in e^perp` is a unit vector perpendicular to `g`, then `Lambda h=T h` and hence `||T||op>=1`. Choose a unit eigenvector `z in e^perp` with

`tau=z^T Lambda z`, `|tau|=||T||op>=1`,

and let `y` be the other transverse eigenvector. In `(e,y,z)` coordinates,

`Lambda=[[alpha,beta,gamma],[beta,r,0],[gamma,0,tau]].`             (2.1)

For the spectral projections

`W=sqrt(c)X_0 + sum_{j!=0}s_jX_j`,
`Y=sum_{j!=0}y_jX_j`,
`Z=sum_{j!=0}z_jX_j`,

Parseval gives `sum y_j^2=sum z_j^2=1` and `sum s_j y_j=sum s_j z_j=0`.

Assume a disjoint ORIGINAL-coordinate bank `K_z` is a pure `z` innovation,

`r_k=z_k z` for `k in K_z`,  `zeta=sum_{k in K_z}z_k^2>0`.

Then

`||p_Y||infinity<=sqrt(2)`,
`||p_{W|Y}||infinity<=c^(-1/2)`,
`||p_{Z|W,Y}||infinity<=sqrt(2/zeta)`.                             (2.2)

The first is the one-dimensional product-projection bound. The second comes from convolution with the genuinely independent scaled physical scalar `sqrt(c)X_0`; the third comes from convolution with the genuinely independent pure-`z` bank.

Complete only the `Z` square:

`Q=R(W,Y)+tau[Z+(gamma/tau)W]^2`,

where the determinant of the `(W,Y)` quadratic part is exactly

`Delta_R=det(Lambda)/tau`.                                        (2.3)

Applying (1.1) followed by the conditional square kernel gives

`||p_Q||infinity
 <=16 sqrt(2/zeta) sqrt(2*c^(-1/2)*sqrt(2))
      |tau|^(-1/2)|Delta_R|^(-1/4)`
 `<=16*2^(5/4)c^(-1/4) zeta^(-1/2)|det Lambda|^(-1/4)`.           (2.4)

Thus this branch is uniform through `alpha=0` and through every nonzero near-null `alpha`; no `|alpha|^(-1/4)` remains. Continuity is not yet claimed at this checkpoint.

## 3. Designated partner fleet04/B10 applied at an actual inequality

The newest completed designated partner report is

`yspennstate/math-open-problems@5bfbad861ea24cd956f12fd00cb32b1514b64fc8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`.

Apply its `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` to the sole survivor of fleet03/B10 r24. There the mixed bank `M` obeys

`sum_(j in M) s_j w_j=0`,
`rho_M=sum_(j in M)s_j^2<1/64`,
`H_M=sum_(j in M) w_jw_j^T`,
`eta=lambda_max(H_M)>7/8`.

Whenever `H_M` is invertible the regression vector is exactly zero, so the partner theorem has residuals `e_j=s_j`, transverse Gram `G=H_M`, and gives a partition `M=S disjoint_union Y disjoint_union Z` with

`rho_S * M(G_Y,G_Z) >= (2/81) rho_M det(H_M)`.                    (3.1)

If `xi=lambda_min(H_M)>=1/8`, then `det H_M>7/64`, hence the normalized, near-coloop-scale-free packet satisfies

`boxed: (rho_S/rho_M) * M(G_Y,G_Z) > 7/2592.`                     (3.2)

If instead `xi<1/8`, combine the exact hub packet identity from fleet02/B10 with `c>63/64`:

`P_MT/c = eta(1-xi)+xi(1-eta) > (7/8)(7/8)=49/64`,

so

`boxed: P_MT > 3087/4096 >0.7536.`                                (3.3)

Thus the r24 high-slope survivor has a quantitative alternative: either a constant normalized three-source regression/transverse packet supplied by the exact partner theorem, or an even larger hub/mixed/pure-transverse Pluecker packet. This does not by itself close the no-pure-innovation chamber; it is a source-valid routing certificate for the next receiver.

## 4. Remaining obligation

The new analytic receiver closes the near-null/nonzero-coloop branch whenever a fixed positive pure innovation exists along a transverse eigenvector of the compression `P_(e^perp)Lambda P_(e^perp)`. The remaining B10 debt is the no-pure-innovation overlap chamber: every physical row carrying the needed tangent direction also carries one of the other active spectral directions. Equations (3.2)-(3.3) show that this chamber still has a constant aggregate product-coordinate packet, so the next mechanism must spend that packet before taking conditional-height suprema or selecting a tiny local minor.

Full exact rank three and full QFORM remain OPEN.
