SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-23T11:45:17Z.
attacking: the exact-null physical-hub endpoint of the rank-three coupled case; identify the mixed-Fresnel augmented leverage exactly with the B10 transverse leverage and close the full r23 null-hub survivor before returning to the nonzero near-null collar.

# account03/B10 r24 — null-hub transverse-leverage closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW QUANTITATIVE COROLLARY / R23 NULL-HUB SURVIVOR CLOSED / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary

Fresh source control was read from `yspennstate/math-research-brain@c0983c9ed4f61a9f45c8335fc2b3b8f808645117`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The full target and unrestricted continuity claim remain open in the canonical claims ledger.

The immediate B10 predecessor is

`yspennstate/math-open-problems@be74f28001070ca45728f51da989c89335e2803c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260923T101459Z-account03-B10-QFORM-r23/REPORT.md`.

Its remaining exact-null state has an exact-rank-three Parseval representation

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>=1`,

and one ORIGINAL physical coordinate `0` whose spectral row is

`u_0=sqrt(h) r`, `||r||=1`, `h>55/64`, `r^T M r=0`,               (1.1)

while every complementary row satisfies

`||P_(r^perp) u_j||^2 <=1/2`.                                      (1.2)

The analytic input used below is the completed mixed-hub/Fresnel theorem in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

and its exact-null rank-three shear corollary as written out independently in

`yspennstate/math-open-problems@d3e2179df26d8808f17ec506a480fa4ca0e1f099`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T000427Z-account02-B01-qform-r30/REPORT.md`.

For a physical null hub `A_00=0`, write the hub coupling vector to the leaves as `g`, `gamma=||g||`, and write the rank-one residual after the exact hub shear as `lambda beta beta^T`, `||beta||_2=1`, `beta perp g`. If the augmented leaf leverage

`beta_j^2+g_j^2/gamma^2 <=1/2`                                    (1.3)

for every leaf, the cited mixed-Fresnel argument gives

`|phi_Q(t)| <=4 pi^(3/2) |lambda|^(-1/2) gamma^(-1) |t|^(-3/2)`   (1.4)

and hence a continuous density with

`||p_Q||_infinity <=3*2^(4/3)(|lambda| gamma^2)^(-1/3)`.           (1.5)

This is a joint original-product Fourier estimate. It is not the refuted assertion of law-uniform one-dimensional quadratic-phase decay.

## 2. Exact spectral-to-physical identification

The point of this run is that, in the B10 state (1.1)-(1.2), every quantity in (1.3)-(1.5) can be identified exactly with the already-controlled spectral geometry.

Put

`s=||M r||`.

Since `M` is invertible, `s>0`; and because `r^T M r=0`, the vector `M r` is perpendicular to `r`. Set

`v=(M r)/s`

and choose the unit vector `q` so that `(r,v,q)` is an orthonormal basis of `R^3`. In this basis symmetry forces

`M = [[0,s,0],[s,b,c],[0,c,d]]`.                                  (2.1)

Its determinant is

`det M=-s^2 d`, hence

`d!=0`, `D=s^2 |d|`.                                               (2.2)

For every leaf row write

`u_j=t_j r+alpha_j v+beta_j q`.                                   (2.3)

Parseval, after removing `u_0 u_0^T=h rr^T`, gives in particular

`sum_j alpha_j^2=1`, `sum_j beta_j^2=1`, `sum_j alpha_j beta_j=0`. (2.4)

The physical hub-leaf coefficient is

`g_j=A_0j=u_0^T M u_j=sqrt(h) s alpha_j`.                          (2.5)

Therefore

`gamma^2=sum_j g_j^2=h s^2`.                                      (2.6)

Now define

`ell_j=h^(-1/2)[ t_j +(b/(2s))alpha_j +(c/s)beta_j ]`.             (2.7)

A direct expansion of (2.1) gives the ENTIRE leaf block, with no deletion or perturbation,

`A_jk=g_j ell_k+ell_j g_k+d beta_j beta_k`.                        (2.8)

Consequently the full quadratic form has the exact original-coordinate shear representation

`Q=2 X_0 (g.X_L)+X_L^T A_LL X_L`
` =2 (X_0+ell.X_L)(g.X_L)+d(beta.X_L)^2`.                          (2.9)

The dependence between the translated hub variable and the leaves is not discarded. In the mixed-Fresnel proof, translating the hub density by `ell.X_L` only produces leafwise unit-modulus linear twists after Fourier transformation, so the original leaf product amplitude is preserved. This is precisely the shear-stable scope of the cited null-hub theorem.

Most importantly, the normalized augmented leverage in (1.3) is exactly

`beta_j^2 + g_j^2/gamma^2
 =beta_j^2+alpha_j^2
 =||P_(r^perp)u_j||^2`.                                           (2.10)

Thus B10's existing gate (1.2) is not merely analogous to the mixed-Fresnel gate; it is IDENTICAL to it.

Finally, by (2.2) and (2.6),

`|lambda| gamma^2=|d| h s^2=hD`.                                  (2.11)

## 3. Main corollary

### Theorem — `QFORM-NULL-HUB-TRANSVERSE-LEVERAGE-CLOSURE-v1`

Let `A=RMR^T` have exact rank three, `R^T R=I_3`, and let `D=|det M|`. Suppose one ORIGINAL coordinate has physical spectral row `u_0=sqrt(h)r`, `h>0`, with

`r^T M r=0`,

and suppose every other physical spectral row satisfies

`||P_(r^perp)u_j||^2<=1/2`.

For arbitrary independent original-coordinate input laws with densities at most one, the law of `Q=X^TAX` has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <=3*2^(4/3)(hD)^(-1/3).`                  (3.1)

Proof. Sections 2.1-2.11 verify every hypothesis and identify the determinant currency of the cited mixed-Fresnel theorem. Equation (1.4) becomes

`|phi_Q(t)| <= K |t|^(-3/2)`,
`K=4 pi^(3/2)(hD)^(-1/2)`.                                        (3.2)

Together with `|phi_Q|<=1`,

`int_R min(1,K|t|^(-3/2)) dt=6K^(2/3)`.                           (3.3)

Fourier inversion gives

`||p_Q||_infinity <=(1/(2pi))*6K^(2/3)
 =3*2^(4/3)(hD)^(-1/3)`.                                          (3.4)

The integrable characteristic-function envelope also gives a continuous representative vanishing at infinity. QED.

No post-rotation independence, conditional projection-density cap, arbitrary-joint coarea estimate, moment assumption, compact support, connected support, Gaussianity, or perturbative deletion occurs.

## 4. Closure of the r23 exact-null survivor

In r23, `h>55/64`, `D>=1`, and (1.2) holds. Therefore (3.1) gives

`boxed: ||p_Q||_infinity
 <3*2^(4/3)(64/55)^(1/3)
 =7.9512182993270875... <7.952.`                                  (4.1)

This pays the entire exact-null single-hub survivor from r22/r23 and proves continuity there. In particular, the previous square-root small-ball estimate and quarter-Riesz star currency are no longer the endpoint on this branch: the mixed-Fresnel augmented frame converts the same geometry directly into an integrable `|t|^(-3/2)` envelope.

## 5. Designated partner account04/B10 applied at an actual inequality

The completed designated partner theorem is

`QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`,

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B10/20260923T061725Z-account04-B10-QFORM-r4/REPORT.md`.

Apply it to the same complement (2.3). Here the full transverse Gram is `I_2`, the global regression vector is zero by Parseval, the residuals are exactly `e_j=t_j`, and

`rho=sum_j t_j^2=1-h`.

It supplies disjoint ORIGINAL-coordinate banks `S,Y,Z` with

`rho_S M(G_Y,G_Z) >=(2/81)rho`.                                   (5.1)

Because `rho_S<=rho` and the total transverse pair-volume is one,

`M(G_Y,G_Z)>=2/81`, `rho_S>=(2/81)rho`.                            (5.2)

Thus the actual fixed-hub principal-triple packet in those partner banks obeys

`sum_(j in Y,k in Z)|det A_{0jk}|
 =D h M(G_Y,G_Z)
 >55/2592`.                                                        (5.3)

This is an actual inequality-level use of the designated partner result. The new closure (4.1) is stronger and does not need to select or invert any member of this packet, but (5.3) remains a valid product-preserving curvature certificate for the neighboring nonzero-pivot collar.

## 6. What remains

This run does NOT prove arbitrary exact rank three and does NOT prove full QFORM. It closes the exact-zero-pivot endpoint under the transverse-diffuse gate that survived r22/r23.

The next B10 obstruction is the genuinely nonzero near-null/near-coloop collar isolated before the exact-null specialization: the hub has small but nonzero Rayleigh coefficient, and after the already-paid moderate-mixed-transverse branch the residual geometry is a high-slope cancellation bank. The first next implication is therefore

`QFORM-NEARNULL-NONZERO-HUB-HIGHSLOPE-PAYMENT-v1`:

obtain a universal endpoint through the punctured collar `0<|r^TMr|<<1` without paying a negative power of that scalar pivot and without treating the small longitudinal coefficients as a perturbative random error. The newly completed mixed-basis triple-Fresnel theorem of account01/B03 (`math-open-problems@3d991ad3ab91593155b0b465007f4938968a14bf`) is directly relevant to that next step, but its disjoint-basis collision parameter is not automatically bounded below in the concentrated high-slope survivor, so no full collar closure is claimed here.

Full exact-rank-three theorem: OPEN / NOT PROVED.  
Full owner conjecture: OPEN / NOT PROVED.  
Continuity: PROVED in theorem (3.1) and r23 survivor (4.1), still OPEN globally.

## 7. Deterministic algebra regression

A deterministic numerical regression generated 2000 random orthonormal physical frames, imposed the null-hub spectral normal form (2.1), and checked (2.8), (2.2)/(2.11), (2.6), and (2.10). Maximum absolute discrepancies were respectively

`1.11e-15`, `8.88e-15`, `1.78e-15`, `1.11e-15`.

These computations are regression checks only. The proof is the exact algebra above.
