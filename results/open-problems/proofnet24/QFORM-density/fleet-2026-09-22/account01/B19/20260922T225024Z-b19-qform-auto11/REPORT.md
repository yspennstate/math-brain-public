SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-22T22:50:24Z.
attacking: the heavy-null near-unit / high-normalized-leverage branch; convert partner r20's large normalized complement leverage into a direct physical scalar-square or two-pivot payment before reciprocal local-minor selection.

# account01/B19 — direct linear-square smoothing closes the entire exact null-coloop branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control at start/prepublication:** revision `2026-09-22.15`  
**Run:** `20260922T225024Z-b19-qform-auto11`  
**Assignment:** Universal proof assembly  
**Outcome:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL BRANCH CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The owner target remains unrestricted: independent original-coordinate real inputs with marginal densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moment/support/log-concavity hypothesis, and no independence after spectral rotation. Essential boundedness is the target; continuity is tracked separately.

This report proves a new direct integration theorem which eliminates the residual-determinant singularity in the exact null-coloop branch. In particular, it replaces the preceding `D^{-1/8}` and `sqrt(log(e/D))` bounds by one bound independent of the residual determinant `D`, including `D=0`.

## 1. Source-valid inputs actually consumed

### 1.1 Named assigned partner: account02/B19 r20

Canonical source:

`yspennstate/math-open-problems@4a4682f27ee74da65f62c20fc4520e81b48bece6`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T221019Z-account02-B19-qform-r20/REPORT.md`.

Its theorem `QFORM-NEARSPAN-NORMALIZED-COMPLEMENT-MSS-v1` treats the exact-rank-three heavy-null state

`A=RMR^T`, `R^TR=I_3`, `u_0=sqrt(c)r`, `r^TMr=0`, `D_M=|det M|>=1/2`.

For `c<=61/64`, if the normalized complement frame is diffuse (`max ell_j<=1/16`), it produces an original-coordinate rank-three cross cut and the continuous bound `<339.450`. Its remaining near-span branch contains the genuinely near-unit alternative `c>61/64`, including the endpoint `c=1`.

The theorem proved below is applied to that actual endpoint `c=1`: it pays it uniformly, with no residual determinant or leverage assumption. Thus the partner's near-unit alternative is reduced from `c>61/64` to the punctured range `61/64<c<1` on this route.

### 1.2 Product-projection density theorem

I use account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `R` has `k` orthonormal columns and `Y=R^TX` for independent cap-one coordinates, then

`||p_Y||_infinity <= exp(k/2)`.

For `k=2` this gives the cap `e`. The proof is a genuine affine-fiber Brascamp--Lieb integral in the original product coordinates, not a post-rotation independence claim.

### 1.3 Predecessor comparison

account04/B19 r2, canonical

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

proved in the residual-diffuse exact null-coloop normal form a continuous bound `<34 sqrt(log(e/D))` for `0<D<=1`, while the exact singular endpoint `D=0` was separately bounded. The present theorem removes `D` altogether, at the cost of proving essential boundedness rather than continuity.

The live corrections are respected: no arbitrary-joint rank-three coarea bound, no positive conditional projection-density moment, no conditional-cap-as-independence step, no pointwise quadratic-phase decay, no fixed good physical minor, and no coefficient-small perturbative deletion is used.

## 2. New analytic theorem: independent linear direction plus one square

### Theorem 2.1 — `QFORM-INDEPENDENT-LINEAR-SQUARE-SMOOTHING-v1`

Let `X` be a real random variable with density `0<=f_X<=1`. Let `(Y,Z)` be a real random pair, independent of `X`, with a joint probability density `g` satisfying

`||g||_infinity <= H`.

Let `s,f` be nonzero real numbers and let `a` be arbitrary. Put

`T = 2sXY + aY^2 + fZ^2`.

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 6 H^(2/3) |s^2 f|^(-1/3).
`

All signs are allowed. No independence between `Y` and `Z` is assumed. The same estimate is unchanged by additive constants, by arbitrary terms depending only on `Y`, and after determinant-one shears/translations of the `(Y,Z)` pair that preserve the displayed normal form.

### Proof

Write

`p_Y(y)=int_R g(y,z) dz`.

For almost every fixed `y!=0`, let `k_y(t)` denote the density contribution at target `t` from the slice with that `Y=y`:

`k_y(t)=int_R int_R f_X(x) g(y,z)
         delta(t-2syx-a y^2-fz^2) dx dz`.

Two different exact integrations give complementary bounds.

#### Bound A: spend the original independent linear coordinate

Integrate in `x` first. Since `f_X<=1`,

`k_y(t)
 <= [1/(2|s y|)] int_R g(y,z) dz
 = p_Y(y)/(2|s y|).`                                      (2.1)

This keeps the actual marginal mass `p_Y(y)` and is useful away from `y=0`.

#### Bound B: spend the square before the linear critical point

For fixed `x,y`, integrate in `z`. The pushforward of a cap-`H` density under `z -> fz^2` obeys the pointwise square kernel

`int g(y,z) delta(w-fz^2) dz
 <= H / [sqrt(|f|) sqrt(|w|)]`                                (2.2)

for almost every `w` (and with the left side zero on the unsupported sign).

Therefore

`k_y(t)
 <= H |f|^(-1/2)
    int f_X(x) |t-a y^2-2syx|^(-1/2) dx.`                    (2.3)

For any probability density `0<=h<=1` and every `c`, the bathtub/rearrangement bound gives

`int h(x)|x-c|^(-1/2) dx
 <= int_(-1/2)^(1/2) |u|^(-1/2)du
 = 2sqrt(2).`                                                (2.4)

Scaling (2.4) by `2sy` in (2.3) yields

`k_y(t) <= 2H / sqrt(|f s y|).`                              (2.5)

This is integrable across the critical line `y=0`.

#### Split and optimize

For any `r>0`, use (2.5) on `|y|<=r` and (2.1) on `|y|>r`. Since `int p_Y=1`,

`p_T(t)
 <= [2H/sqrt(|fs|)] int_(|y|<=r)|y|^(-1/2)dy
    + [1/(2|s|)] int_(|y|>r) p_Y(y)|y|^(-1)dy`

` <= 8H sqrt(r)/sqrt(|fs|) + 1/(2|s|r).`                     (2.6)

The right side is independent of `t`. Its exact optimizer is

`r_* = [ sqrt(|f|/|s|)/(8H) ]^(2/3).`                         (2.7)

Substitution into (2.6) gives

`p_T(t)
 <=6 H^(2/3)|f|^(-1/3)|s|^(-2/3)
 =6H^(2/3)|s^2f|^(-1/3).`                                    (2.8)

The exceptional slice `y=0` has zero measure because `(Y,Z)` has a density. The integrable majorants above give an absolutely continuous mixture, proving the asserted essential density bound. QED.

### Why this is not the forbidden conditional-cap shortcut

The theorem uses **true independence of the original scalar `X` from the full pair `(Y,Z)`**. This is essential. A conditional cap by itself does not substitute for it.

Indeed, take `Y,Z,U` independent uniform variables on `[0,1]`, `[0,1]`, and `[-1/2,1/2]`, and define

`W=-Z^2/(2Y)+U` for `Y>0` (define it arbitrarily on the null event `Y=0`).

Then `(Y,Z)` has density cap one and the conditional density of `W|(Y,Z)` has cap one. Nevertheless

`2WY+Z^2 = 2UY`,

whose density has the usual logarithmic product singularity at zero. Thus a proof of the punctured near-unit branch may not replace the independent null-coloop scalar by a merely conditionally bounded effective scalar.

## 3. Target-level application: exact null coloop is completely paid

Consider the exact-rank-three null-coloop state from account01/B10/account04/B19:

`A=UMU^T`, `U^TU=I_3`, `sigma_min(M)>=1`,

and one genuine original-coordinate spectral row is a unit null vector `u_i=r`,

`r^TMr=0`, `||r||=1`.

Parseval forces every other spectral row into `r^perp`. Choose an orthonormal spectral basis `(r,e_1,e_2)` with

`Mr=s e_1`, `|s|>=1`.

Then

`M=[[0,s,0],[s,d,g],[0,g,f]]`,

with

`det M=-s^2 f`, and `f!=0` (indeed `|f|>=1`).                  (3.1)

Let

`(Y_1,Y_2)=W^T X_{-i}`

be the residual two-dimensional spectral projection. The columns of `W` are orthonormal. By `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, its joint density satisfies

`||p_(Y_1,Y_2)||_infinity <= e`.                               (3.2)

The genuine original coordinate `X_i` is independent of this whole pair.

The quadratic is exactly

`Q=2sX_iY_1+dY_1^2+2gY_1Y_2+fY_2^2`.                          (3.3)

Apply the determinant-one shear

`Z=Y_2+(g/f)Y_1`.

The joint density cap remains `e`, independence from `X_i` is unchanged, and

`Q=2sX_iY_1 + (d-g^2/f)Y_1^2 + fZ^2`.                         (3.4)

Theorem 2.1 with `H=e` gives

`boxed:
 ||p_Q||_infinity
 <=6 e^(2/3)|s^2f|^(-1/3)
 =6e^(2/3)|det M|^(-1/3)
 <=6e^(2/3)
 <11.687.
`                                                                    (3.5)

This bound is uniform in the residual determinant

`D=|df-g^2|`.

It treats simultaneously `D=0`, arbitrarily small nonzero `D`, and large `D`. It also requires **no residual leverage/diffuseness assumption**. Hence the entire exact null-coloop branch is paid by one direct argument.

This supersedes, for essential boundedness in this exact branch, both the earlier singular-Witt `<5.844` / nonsingular `D^(-1/8)` split and account04/B19's adaptive `<34 sqrt(log(e/D))` bridge. Those Fourier arguments remain useful because they also prove continuity; (3.5) by itself only proves essential boundedness.

## 4. Actual application of named partner account02/B19 r20

The partner's current near-span dichotomy leaves:

(A) `c<=61/64` with high normalized complement leverage, or

(B) `c>61/64` (the near-unit heavy-null endpoint family),

modulo already-paid packets.

At `c=1`, the heavy null row is exactly a null **coloop** and Parseval forces all other rows into `r^perp`. Equation (3.5) therefore applies to the actual partner state and proves

`boxed: c=1 => ||p_Q||_infinity<11.687,`

with no condition on the residual determinant, no normalized-complement leverage condition, and no residual-diffuse split.

Thus the partner's alternative (B) is sharpened to the genuinely punctured regime

`boxed: 61/64 < c < 1.`                                         (4.1)

In particular, there is no longer any separate exact-endpoint debt at `c=1`.

## 5. Compact conditional universal assembly after this run

A correction-safe proof route can now be stated as follows.

1. Existing ridge / diffuse spectral-window branches, definite physical pairs, sequential quantitative two-pivot packets, exact cross-rank packets, grouped-square packets, and the low-offdiagonal branch remain paid in their stated scopes.
2. account02/B19 r20 pays the `c<=61/64` near-span chamber whenever the normalized complement frame is MSS-diffuse, by a genuine original-coordinate rank-three cross cut.
3. account02/B19 r19 pays the exact local-span boundary and every leakage residual bounded quantitatively away from zero.
4. account03/B10 r19 proves that the small-positive-leakage limit still carries constant O3 aggregate curvature; no reciprocal leakage loss is structurally necessary.
5. **This run pays the entire exact null-coloop endpoint `c=1`, uniformly across the residual determinant and across residual leverage patterns.**

What remains on this line is not a singular residual determinant. It is the loss of genuine independence when `c<1`: the complement carries a nonzero longitudinal random form which can correlate with the two transverse projections.

## 6. First essential missing implication after the new payment

### `QFORM-NEARUNIT-PRODUCT-PROVENANCE-STABILITY-v1` — OPEN

In the exact-rank-three heavy-null state

`u_0=sqrt(c)r`, `r^TMr=0`, `61/64<c<1`,

write the complement spectral coordinates as

`alpha=(alpha_j)`, `beta=(beta_j)`, `gamma=(gamma_j)`,

so Parseval gives

`||alpha||^2=1-c`, `alpha dot beta=alpha dot gamma=0`,
`||beta||=||gamma||=1`, `beta dot gamma=0`.

The effective null-direction variable is

`R=sqrt(c)X_0 + alpha dot X_{-0}`,

and the transverse pair is

`Y=beta dot X_{-0}`, `Z=gamma dot X_{-0}`.

The next theorem must obtain a density bound uniform as `c up to 1` while retaining the original-product provenance of the jointly distributed triple `(alpha dot X, Y, Z)`. It may **not**:

- delete `alpha dot X` merely because `||alpha||=sqrt(1-c)` is small (supports are unrestricted);
- replace the effective `R` by an independent scalar;
- infer independence from a bounded conditional density;
- take a worst conditional projection-height moment.

A valid closure could use the existing J/K product-bank partition to expose one genuinely independent longitudinal packet, or an aggregate trace inequality that couples the longitudinal and transverse product projections before taking any reciprocal critical kernel.

The explicit cancellation example in Section 2 shows why a theorem stated only in terms of a joint pair cap plus a conditional effective-scalar cap cannot suffice.

The high-normalized-leverage subcase of partner r20 for `c<=61/64` remains a separate structural residual, as does the arbitrary-additional-spectrum descent in the full owner conjecture.

## 7. Status and continuity

- `QFORM-INDEPENDENT-LINEAR-SQUARE-SMOOTHING-v1`: **PROVED**.
- Exact-rank-three exact null-coloop branch: **CLOSED for essential boundedness**, with universal bound `<11.687`.
- account04/B19 punctured residual-determinant debt at exact null coloop: **REMOVED for essential boundedness**.
- Full exact-rank-three QFORM: **OPEN**.
- Full arbitrary-matrix QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**. The new direct argument does not by itself provide a continuous representative; the preceding Fourier arguments do in their stated subbranches.
