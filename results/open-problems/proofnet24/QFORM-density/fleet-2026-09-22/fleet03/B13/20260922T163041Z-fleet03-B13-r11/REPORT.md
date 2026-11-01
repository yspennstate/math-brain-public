# fleet03/B13 — affine-uniform two-pivot smoothing in exact rank three

**Run:** `20260922T163041Z-fleet03-B13-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW EXACT-RANK3 PRODUCT-LAW THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains **OPEN / NOT PROVED**. This report proves a new exact-rank-three branch that is uniform in arbitrary support translations and arbitrary tail-dependent affine shifts. It does not solve the pure light-cone case in which the relevant physical diagonal coefficients vanish, and it does not address arbitrary additional spectral directions.

## 1. Fresh control and source-valid premises

The run began from fresh brain main and was refreshed during the derivation. The later owner control is revision `2026-09-22.7`; the sole substantive target is unchanged: independent real physical coordinates with one-dimensional densities at most one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, or post-rotation independence assumption is used.

The live correction state rules out law-uniform pointwise quadratic Fresnel decay, unrestricted spectral-fiber suprema, replacement of product provenance by conditional density caps, fixed-minor dichotomies, bounded-diameter localization, fixed fragment count, and support-free operator-norm continuity. The theorem below is specifically designed to be insensitive to the translation obstruction from the latest B13 partner-side work.

The designated `fleet04/B13` current-QFORM artifact was still absent at the source check, so no result is fabricated or awaited. Compatible completed peer mathematics actually applied is:

1. **Exact product bang-bang reduction**, fleet02/B13, canonical source  
   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260922T115714Z-fleet02-B13-qform-480ba28b/REPORT.md`.  
   For every fixed slab kernel, the supremum over product densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over unit-measure product indicators. The same report proves the physical definite-pair slab bound `pi/sqrt(det C)` with arbitrary affine tilt.

2. **Weighted affine-fiber Brascamp--Lieb projection theorem**, fleet02/B06, canonical report  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.  
   A normalized original-coordinate linear aggregate `Z=sum a_k X_k`, `sum a_k^2=1`, has a density cap at most `sqrt(e)`. This is used below for the exact transverse aggregate.

3. **Weak-L2 logarithmic-ridge theorem**, fleet03/B16, canonical report  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/B16-20260922T135620Z-r11/REPORT.md`.  
   With
   `Psi(u)=1+log(1/|u|)` for `0<|u|<=1`, and `Psi(u)=|u|^(-1/4)` for `|u|>=1`, it proves
   `||Psi(a+z^2)||_(L^{2,infinity}(dz)) <= sqrt(15)` uniformly in `a`, and the scaled version with coefficient `delta>0` costs `delta^(-1/4)`.

The exact operator-norm continuity falsifier from fleet02/B13 (`20260922T155613Z-fleet02-B13-productset-r12`) is also enforced: small spectral leakage is never discarded. Instead all leakage is absorbed algebraically into affine shifts and one exact scalar square.

## 2. Exact two-pivot spectral decomposition

Assume first that `A` has **exact rank three**:

`A=R Lambda R^T`, `R^T R=I_3`,

where `Lambda=diag(lambda_1,lambda_2,lambda_3)` is invertible. Let `r_k^T` denote row `k` of `R`.

Choose two physical coordinates `i,j` whose spectral rows are linearly independent. Put

`Delta_ij := ||r_i wedge r_j||^2 > 0`,

and let

`C := A[{i,j},{i,j}]`

be their physical `2 x 2` compression. Assume for now `det C != 0`. Choose a unit spectral vector `v` perpendicular to `span{r_i,r_j}`.

For the tail coordinates `T=[n]\{i,j}`, define

`Z := sum_{k in T} <r_k,v> X_k`.                                      (2.1)

Because `sum_k r_k r_k^T=I_3` and `<r_i,v>=<r_j,v>=0`,

`sum_{k in T}<r_k,v>^2 = 1`.                                         (2.2)

Thus `Z` is a normalized linear aggregate of the **original independent tail coordinates**. In particular the fleet02/B06 affine-fiber theorem gives

`||p_Z||_infinity <= sqrt(e)`.                                       (2.3)

Let `Y_T=sum_{k in T} r_k X_k` be the tail spectral vector. Write its orthogonal decomposition as

`Y_T = m_1 r_i + m_2 r_j + Z v`,                                     (2.4)

where `m_1,m_2` are linear forms of the original tail coordinates. Set

`H=[r_i, r_j, v]`

with these vectors as columns. Then the total spectral vector is

`R^T X = H ( X_i+m_1, X_j+m_2, Z )^T`.                               (2.5)

Write

`H^T Lambda H = [[C,k],[k^T,gamma]]`.                                (2.6)

Since `C` is invertible, complete the square only in the first two coordinates:

`Q=X^TAX`
` = (x+L(X_T))^T C (x+L(X_T)) + s Z^2`,                              (2.7)

where `x=(X_i,X_j)^T`,

`L=(m_1,m_2)^T + C^(-1)k Z`,                                        (2.8)

and

`s=gamma-k^T C^(-1)k`.                                               (2.9)

This is an **exact identity**. All arbitrarily small planar leakage of the tail is retained in the affine shift `L`; no support radius or moment is needed.

The scalar coefficient has an exact invariant formula. By the Schur determinant identity,

`det(H^T Lambda H)=det(C) s`.                                        (2.10)

On the other hand

`det(H^T Lambda H)=det(H)^2 det(Lambda)`.                            (2.11)

Since `v` is unit and perpendicular to the first two columns,

`det(H)^2 = Delta_ij`.                                                (2.12)

Therefore

`boxed( s = det(Lambda) Delta_ij / det(C) ).`                         (2.13)

In particular

`boxed( |det C| |s| = |det Lambda| Delta_ij ).`                       (2.14)

This exact curvature tradeoff is the key cancellation below.

## 3. A translation-uniform pointwise envelope for a two-variable quadratic

Let `U,V` be independent variables with densities bounded by one, and let

`C=[[a,b],[b,d]]`

be any invertible real symmetric `2 x 2` matrix with `a!=0`. Put

`D=|det C|`.

For arbitrary deterministic translations `u_0,v_0`, let

`Y=(U+u_0,V+v_0)^T C (U+u_0,V+v_0)`.

### Lemma 3.1 — `QFORM-2D-AFFINE-LOG-ENVELOPE-v1`

`Y` has a density `h` satisfying, for almost every `y`,

`boxed( h(y) <= 8 D^(-1/2) Psi( a y / D ) ).`                         (3.1)

The bound is uniform in both translations and in the individual input laws.

### Proof

Complete the square in the first physical variable:

`Y = a W^2 + (det C/a)(V+v_0)^2`,                                    (3.2)

where `W=U+u_0+(b/a)(V+v_0)`. Conditional on `V`, `W` is a translate of `U`, so its conditional density is at most one. The pushforward by `aW^2` therefore gives

`h(y) <= |a|^(-1/2) int f_V(v)
 |y-(det C/a)(v+v_0)^2|^(-1/2) dv`.                                  (3.3)

After translating `v`, factor out `|a|` and put

`delta=D/a^2`, `A=y/a`.

Then

`h(y) <= |a|^(-1)
 sup_{0<=f<=1, int f=1} int f(v)|A +/- delta v^2|^(-1/2)dv`.          (3.4)

If `W_delta=sqrt(delta)V`, its density cap is `delta^(-1/2)`. Rescale once more by this cap to return to the unit-cap class in the fleet03/B16 bathtub kernel. This gives

`sup_f int f(v)|A +/- delta v^2|^(-1/2)dv`
` <= delta^(-1/2) J_*(A/delta)`                                     (3.5)

and the B16 bound `J_*(u)<=8 Psi(u)` yields

`h(y) <= 8 |a|^(-1) delta^(-1/2) Psi(A/delta)`
`      = 8 D^(-1/2) Psi(ay/D)`.                                     (3.6)

The sign in (3.4) is harmless because `Psi` depends only on absolute value. QED.

The important point is that the singularity is pinned to the **quadratic critical value** and the envelope is completely independent of the affine translation. This is exactly the feature missing from a naive operator-norm continuity argument.

## 4. New theorem: the determinant of the physical pair cancels completely

Return to the exact-rank-three decomposition (2.7). Assume `det C!=0` and at least one diagonal entry of `C` is nonzero. Relabel the pair so

`a:=A_ii!=0`.

Let

`D=|det C|`, `D_3=|det Lambda|`, `Delta=Delta_ij`.

Conditional on all tail coordinates, `(X_i,X_j)` remain independent with their original unit density caps; the shift `L(X_T)` is deterministic. Lemma 3.1 therefore gives

`p_{Q|X_T}(t|X_T)`
` <= 8 D^(-1/2)
       Psi( (a/D)(t-s Z^2) )`.                                      (4.1)

Crucially the right side depends on the tail only through `Z`, not through the other affine shift. Averaging over the tail is therefore legitimate even though `Z` may be strongly correlated with the shift `L`.

Let

`delta = |a s|/D`.                                                    (4.2)

The fleet03/B16 weak-`L^2` ridge theorem and scaling give, uniformly in `t`,

`|| z -> Psi((a/D)(t-sz^2)) ||_(L^{2,infinity}(dz))`
` <= sqrt(15) delta^(-1/4)`.                                         (4.3)

If a probability density `g` has cap `H`, the elementary layer-cake pairing with weak `L^2` gives

`int g(z) F(z) dz <= 2 H^(1/2) ||F||_(2,infinity)`.                   (4.4)

Using the actual peer bound `H=sqrt(e)` from (2.3), (4.1)--(4.4) yield

`||p_Q||_infinity`
` <= 16 sqrt(15) e^(1/4) D^(-1/2) delta^(-1/4)`.                     (4.5)

Now insert the exact Schur coefficient (2.13):

`|s|=D_3 Delta/D`,

so

`delta=|a| D_3 Delta / D^2`.                                         (4.6)

The entire physical-pair determinant cancels:

### Theorem 4.1 — `QFORM-RANK3-AFFINE-TWOPIVOT-SQUARE-SMOOTHING-v1`

For every exact-rank-three target matrix and every physical pair `i,j` satisfying

- `r_i,r_j` linearly independent,
- `det A[{i,j},{i,j}] !=0`, and
- `A_ii!=0` after possibly swapping `i,j`,

one has, for arbitrary independent cap-one one-dimensional input laws,

`boxed(
 ||p_Q||_infinity
 <= 16 sqrt(15) e^(1/4)
    ( |A_ii| |det Lambda| Delta_ij )^(-1/4).
)`                                                                    (4.7)

Numerically

`16 sqrt(15) e^(1/4) = 79.5681448790...`.                            (4.8)

The theorem proves an essentially bounded density. A continuous representative is **not proved here**.

The same estimate with `A_jj` in place of `A_ii` holds after swapping the two coordinates. Thus the better of the two physical diagonal pivots may be used.

### Why (4.7) is structurally useful

The estimate is completely independent of:

- `det C`, even as the physical pair approaches singularity;
- the sign pattern of the two-dimensional compression;
- support location, support diameter, fragment count, or moments;
- arbitrary tail-dependent translations generated by tiny spectral leakage.

The compensation is exact: a small `|det C|` makes the residual square coefficient `|s|` proportionally large through (2.14), and the weak-`L^2` logarithmic-ridge estimate spends that extra curvature.

## 5. Product-indicator geometric consequence

By the exact fleet02/B13 bang-bang theorem, the same constant is an exact slab constant for arbitrary unit-measure product sets. Namely, under the hypotheses of Theorem 4.1, every interval `J` and every measurable `E_k subset R` with `|E_k|=1` satisfy

`boxed(
 |{x in prod_k E_k : x^T A x in J}|
 <= 16 sqrt(15) e^(1/4)
    ( |A_ii| |det Lambda| Delta_ij )^(-1/4) |J|.
)`                                                                    (5.1)

No single-interval or centered-uniform extremality is used.

## 6. Application to the current four-direction stability collar

The previous B13 profile-overlap theorem reduces the non-leverage-one nested-heavy exact-rank-three obstruction to rows

`r_i=sqrt(c)e_1`,

`r_j=rho e_1+sqrt(h)e_2`,

with `c,h>1/2`. Hence

`Delta_ij=||r_i wedge r_j||^2 = c h > 1/4`.                           (6.1)

Therefore whenever their physical `2 x 2` compression is invertible and either diagonal pivot obeys `|A_ii|>=tau` or `|A_jj|>=tau`, Theorem 4.1 gives the explicit collar bound

`boxed(
 ||p_Q||_infinity
 < 16 sqrt(15)e^(1/4)(tau/4)^(-1/4)
 = 16 sqrt(30)e^(1/4) tau^(-1/4).
)`                                                                    (6.2)

Under the target normalization `D_3>=1`, no additional factor appears.

This is a genuinely **affine-uniform** payment of the collar: the planar leakage may be arbitrarily small, its source supports may be arbitrarily far away, and the induced affine shift may be arbitrarily large. The fleet02/B13 operator-norm counterexample therefore does not affect (6.2).

The surviving terminal obstruction is now explicitly the light-cone regime in which the heavy physical rows have vanishing diagonal Rayleigh coefficients. This is consistent with the independent fleet01/B03 nonisotropic-heavy-pivot theorem; the new content is the exact two-pivot decomposition and cancellation of the pair determinant, which removes a second source of degeneration from this branch.

If `det C=0`, the present two-pivot completion is not used. The completed one-pivot fractional-trace theorem remains available for every nonzero diagonal pivot. If both diagonal entries tend to zero, one reaches the genuine heavy-isotropic/product-provenance problem identified by the live corrections rather than a physical-pair determinant problem.

## 7. Deterministic exact check

Use the tetrahedral Parseval frame

`R=(1/2)*[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]`

and

`Lambda=diag(2,3,-1)`.

Then `R^TR=I_3` and

`A=R Lambda R^T`
` = [[1,0,1/2,-3/2], [0,1,-3/2,1/2], [1/2,-3/2,1,0], [-3/2,1/2,0,1]]`.

For the pair `(i,j)=(1,2)` in one-based indexing,

`C=I_2`, `Delta_ij=1/2`, `det Lambda=-6`.

A unit vector perpendicular to the two selected rows is

`v=(0,1,-1)/sqrt(2)`,

and the two tail coefficients of `Z` are `+1/sqrt(2),-1/sqrt(2)`, so their squared sum is exactly one. Formula (2.13) gives

`s=(-6)(1/2)/1=-3`.

The accompanying checker verifies these identities and the numerical constant (4.8). It is diagnostic; the proof is analytic.

## 8. Status and next unpaid implication

**Proved here:**

- exact affine-uniform two-pivot decomposition (2.7)--(2.14);
- translation-uniform two-variable logarithmic density envelope (3.1);
- `QFORM-RANK3-AFFINE-TWOPIVOT-SQUARE-SMOOTHING-v1`, equation (4.7);
- its zero-loss product-indicator slab consequence (5.1).

**Not proved:**

- the heavy pure/near-light-cone branch where all useful physical diagonal Rayleigh coefficients vanish;
- the rank-three collar when its only surviving curvature is hyperbolic and the leakage must be paid through original product-linear provenance;
- arbitrary additional spectral directions;
- the full owner conjecture;
- continuity for the new branch.

The first B13 unpaid implication is therefore sharpened to:

> **`QFORM-RANK3-AFFINE-HYPERBOLIC-LIGHTCONE-PROVENANCE-v1` (OPEN).** In the exact-rank-three collar, treat the case where two quantitatively independent heavy spectral rows have physical diagonal Rayleigh coefficients tending to zero. One must exploit that the leakage and transverse variable are simultaneous linear images of the original independent tail coordinates; bounded receiver densities or support-free coefficient perturbation are insufficient. The new theorem shows that no separate degeneration of the physical pair determinant needs to be paid once one diagonal pivot is nonzero.

Full QFORM remains **OPEN / NOT PROVED**.
