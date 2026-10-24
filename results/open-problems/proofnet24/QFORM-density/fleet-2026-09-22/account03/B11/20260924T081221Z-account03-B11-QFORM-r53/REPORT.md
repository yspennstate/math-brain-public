SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T08:12:21Z.
attacking: the punctured indefinite collar through the independent-copy difference law: convert the exploding rank-two Schur pseudovolume into a source-valid two-dimensional frequency-density and reciprocal-frequency bound.

# account03/B11 r53 — Schur-difference flattening in the punctured indefinite collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: genuinely rotated indefinite signatures `(2,1)` and `(1,2)`  
Status: **NEW SUPPORTING THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by this run**.

Fresh control was read from `yspennstate/math-research-brain` main. At the prepublication refresh the control commit was `ff6c8cb4dcd0709a8630c9dec58942a202597b44`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no later stop or B11 reassignment observed. The full conjecture and full continuous-density conclusion remain open.

This run changes mechanism from the preceding two-chart coarea work to the independent-copy product law. It does not use law-uniform pointwise van der Corput decay, arbitrary-joint rank-three coarea, conditional density caps after the sum/difference transform, X-ray-only control, fiber suprema, moments, support regularity, or independence after a spectral rotation.

## 1. Exact product source after independent-copy differencing

Let the original coordinates be independent, with probability densities `0<=f_j<=1`. Let `X'` be an independent copy and put

`U_j=X_j-X'_j`.

Then the `U_j` are independent and have densities

`mu_j(u)=int_R f_j(x) f_j(x-u) dx`.                              (1.1)

They are again cap-one probability densities:

`0<=mu_j(u)<=int f_j=1`, and `int mu_j=1`.                       (1.2)

Thus the independent-copy difference vector is itself a legitimate original-coordinate product source for every product-projection theorem used below. This avoids the false assertion that the conjugate sums are conditionally cap-one.

For reference, the exact unnormalised sum/difference Fourier kernel is

`F_j(u,t)=int_R f_j(x)f_j(x-u) exp(it(2x-u)) dx`.                (1.3)

The already-completed Moyal identity gives

`int_R2 |F_j(u,t)|^2 du dt = pi (int f_j^2)^2 <= pi`.            (1.4)

I do not claim (1.4) as new; it is recalled only to identify the product-provenance interface. The new theorem below concerns the Schur image of the *difference* vector itself.

## 2. Rank-two Schur image of the difference product

Let an exact-rank-three target be written

`A=R M R^T`, `R^T R=I_3`,                                      (2.1)

and set

`s=min_k |lambda_k(M)|>0`, `D=|det M|`.                         (2.2)

Fix an ORIGINAL physical coordinate `h` with nonzero scalar pivot

`alpha=A_hh !=0`,                                                (2.3)

and leverage

`q=||R^T e_h||^2`.                                               (2.4)

Write `I=h^c`, `c=A[I,h]`, `B=A[I,I]`, and form the physical Schur complement

`S_h=B-cc^T/alpha`.                                              (2.5)

For exact rank three, `S_h` has rank at most two. In the nondegenerate branch relevant here it has rank exactly two. Let `E` be any `(n-1) x 2` matrix with orthonormal columns spanning `range(S_h)`, and define the two-dimensional **Schur difference frequency**

`Z=E^T S_h U_I`.                                                 (2.6)

This is a deterministic linear image of independent cap-one ORIGINAL difference coordinates.

### Theorem 2.1 — `QFORM-SCHUR-DIFFERENCE-FLATTENING-v1`

Let

`Delta_2(S_h)=sigma_1(S_h)sigma_2(S_h)`                          (2.7)

be the product of its two nonzero singular values. Then `Z` has a two-dimensional density and

`boxed: ||p_Z||_infinity <= 2/Delta_2(S_h).`                     (2.8)

Consequently, for every `r>0`,

`boxed: P(||Z-z0||<=r) <= min(1, 2 pi r^2/Delta_2(S_h))}`        (2.9)

uniformly in the center `z0`, and

`boxed: E ||Z-z0||^(-1) <= 2 sqrt(2 pi/Delta_2(S_h)).}`          (2.10)

No independence between the two coordinates of `Z` is asserted or needed.

#### Proof

Put

`L=E^T S_h`,                                                     (2.11)

so `Z=L U_I`. Since `E` spans the range of the symmetric rank-two matrix `S_h`,

`L L^T=E^T S_h^2 E`.                                            (2.12)

Its two eigenvalues are `sigma_1(S_h)^2` and `sigma_2(S_h)^2`; hence

`sqrt(det(L L^T))=Delta_2(S_h)`.                                (2.13)

Polar-normalize the coefficient map:

`P=(L L^T)^(-1/2)L`,                                             (2.14)

so `P P^T=I_2` and

`Z=(L L^T)^(1/2)(P U_I)`.                                       (2.15)

The completed two-dimensional product-projection theorem gives

`||p_(P U_I)||_infinity <=2`,                                   (2.16)

because the `U_j` are independent cap-one coordinates by (1.2). Scaling (2.15) divides density height by `sqrt(det LL^T)`, proving (2.8).

Equation (2.9) is the density-cap bound on a disk. For (2.10), put `K=2/Delta_2(S_h)`. Layer cake gives

`E ||Z-z0||^(-1)
 <= int_0^infinity min(1, pi K t^(-2)) dt
 =2 sqrt(pi K)
 =2 sqrt(2pi/Delta_2(S_h)).`                                    (2.17)

QED.

## 3. Designated account04/B11 theorem applied at an actual inequality

The completed designated-partner theorem is account04/B11 `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1`, canonical mathematics

`yspennstate/math-open-problems@28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T041708Z-account04-B11-schur-pseudodet-r1/REPORT.md`.

It proves the exact identity

`boxed: Delta_2(S_h)=q D/|alpha|.`                               (3.1)

Combining (3.1) with Theorem 2.1 gives the **source-valid** estimates

`boxed: ||p_Z||_infinity <= 2 |alpha|/(qD),}`                    (3.2)

`boxed: P(||Z-z0||<=r) <= min(1,2pi |alpha| r^2/(qD)),}`         (3.3)

and

`boxed: E ||Z-z0||^(-1) <= 2 sqrt(2pi |alpha|/(qD)).}`           (3.4)

These improve as the physical pivot closes; the Schur frequency does not collapse.

In the live B11 near-coloop collar

`q>=63/64`, `0<|alpha|<=s/64`, `D>=s^3`,                        (3.5)

(3.1) yields the already-sharp actual partner inequality

`boxed: Delta_2(S_h)>=63 s^2`.                                  (3.6)

The new probabilistic consequences are therefore

`boxed: ||p_Z||_infinity <= 2/(63 s^2),}`                        (3.7)

`boxed: P(||Z-z0||<=r) <= min(1, 2pi r^2/(63s^2)),}`            (3.8)

and

`boxed: E ||Z-z0||^(-1) <= [2 sqrt(2pi/63)]/s
                         =0.631610956567.../s.}`                 (3.9)

This is a dimension-free reciprocal-frequency budget extracted from the exact ORIGINAL product difference law, not from an arbitrary dependent projected law.

## 4. Exact decoupled Schur phase identity

The reason `Z` is the correct quantity for the next Fourier step is algebraic. Block `A` as

`A=[[alpha,c^T],[c,B]]`.                                        (4.1)

For difference/sum vectors `U=(u_h,u)` and `V=(v_h,v)`, define

`u_tilde=u_h+c^T u/alpha`,
`v_tilde=v_h+c^T v/alpha`.                                      (4.2)

Then exactly

`boxed: U^T A V
 = alpha u_tilde v_tilde + u^T S_h v.`                          (4.3)

Since `S_h u=E Z`, if `Y=E^T v`,

`boxed: u^T S_h v=Z dot Y.`                                    (4.4)

Thus the independent-copy phase is a scalar pivot product plus a rank-two frequency pairing whose frequency `Z` obeys (3.2)-(3.9). The determinant blow-up from the partner theorem has become a genuine product-law flattening statement before any conditional sum-density normalization occurs.

The shears in (4.2) are **not** declared to preserve coordinate independence. Equations (4.3)-(4.4) are algebraic identities only; the probability estimate is placed entirely on `Z`, where product provenance is genuine.

## 5. Mandatory rank-two control and how the third direction appears

For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                        (5.1)

so opposite-sign rank two really has a logarithmic singularity.

The new viewpoint on the third direction is complementary to r52's two-chart coarea geometry. As the physical scalar pivot tends to zero, account04/B11 shows that the rank-two Schur pseudovolume grows like `1/|alpha|`; Theorem 2.1 converts that growth into a two-dimensional product-derived frequency law whose density height is `O(|alpha|)` and whose reciprocal first moment is `O(sqrt(|alpha|))` before the collar constants are frozen. Thus the third curvature is not merely geometrically transverse: in the independent-copy product source it forces the Schur frequency away from its rank-two singular origin in an averaged, dimension-free sense.

## 6. What remains unpaid

This is not yet the bounded-density theorem. The exact remaining compiler is now narrower:

`QFORM-SCHUR-DIFFERENCE-MOYAL-COMPILER-v1`:

> Starting from the unnormalised coordinate kernels `F_j(u,t)` and the exact phase decomposition (4.3), prove a time-integrable estimate whose conditional cost is at most a universal multiple of `1/||Z||`; then (3.9) closes the punctured exact-rank-three branch uniformly. The proof must aggregate the ORIGINAL sum/difference product kernels before normalization and may not replace their law by arbitrary joint/pair/scalar density caps.

The chronologically newer account02/B11 `QFORM-LDL-MARGINAL-CAPS-SUFFICIENT-FALSE-v1` and account01/B11 `QFORM-TWOJACOBIAN-TRANSVERSALITY-ONLY-FALSE-v1` explain why this distinction is essential: arbitrary dependent laws can have excellent marginal/Jacobian bounds and still have unbounded quadratic output. The present theorem survives those corrections because `Z` is explicitly a linear image of independent cap-one difference coordinates.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner theorem. No new continuity assertion is made.

## 7. Verification and source-match check

A deterministic 20,000-case floating regression checks, for random exact-rank-three indefinite matrices of both signatures, the partner identity (3.1) and the coefficient-area equality `sqrt(det(LL^T))=Delta_2(S_h)`. Maximum relative errors were below `5.1e-13` and `1.1e-13`, respectively. The identities themselves are proved above; the computation is only a regression.

A fresh repository search found the already-known Moyal identity and the standard two-dimensional product-projection/reciprocal-bathtub tools, but no source-matching statement converting account04/B11's exact Schur pseudodeterminant into the difference-product density cap (3.2) and reciprocal-frequency budget (3.4). This is not a literature novelty claim.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.
