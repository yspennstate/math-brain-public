SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T18:17:45Z.
attacking: rank-two disjoint cross-bank smoothing with an exactly zero internal bank, avoiding local-minor and conditional-spectral-sup losses.

# QFORM-ZEROINTERNAL-BANK-WEDGE-v1

Run: `20260922T181745Z-account02-B09-QFORM-r6`  
Worker: `account02/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh prepublication owner control: revision `2026-09-22.11` at `yspennstate/math-research-brain@1dabd8516681f9f2c43318ab858b337d8d6f8cae`  
Classification: **ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING THEOREM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target remains open: for arbitrary independent real coordinates with densities bounded by one and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal density bound for `X^T A X`, or give a target-valid counterexample.

## 1. First unpaid implication attacked in this run

The previous B09 ledger had reached an aggregate-before-inversion obstruction: fixed small minors and a single scalar Schur pivot can be arbitrarily bad on diffuse bank families. The latest partner correction also rules out paying the full-rank problem by conditioning on all complementary spectral coordinates and taking a conditional spectral `L^infinity` norm.

This run attacks the following product-preserving structural bridge early:

**`QFORM-ZEROINTERNAL-WEDGE-OR-GROUPED-ROUTING-v1`.** Before paying any reciprocal local minor, find a disjoint original-coordinate split with one internally flat bank and two aggregate cross singular directions, or route the matrix into an already-paid pivot/ridge/three-bank branch. If the internally flat branch occurs, prove a direct `O(|L|)` interval estimate depending only on the two aggregate singular values, not on any physical entry or selected `3x3` minor.

The theorem below completely pays the analytic part of the internally flat branch. The structural extraction from the bare three-large-eigenvalue hypothesis remains unpaid.

## 2. Sources and corrections actually used

1. **Livshyts--Paouris--Pivovarov marginal-density theorem.** I use the source-valid consequence recorded in `yspennstate/math-open-problems@58cde0caae66f5236332d48a1022fa7c5d12a1f7`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260922T153407Z-qform-lit/REPORT.md`: for a product density with each one-dimensional factor at most one, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. Only `k=1,2` are used here. No moment, support, smoothness, centering or identical-law assumption is introduced.
2. **Named partner account03/B09.** The positive theorem actually applied below is `QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1`, canonical source `yspennstate/math-open-problems@f510cd96f4505202fa369a8ac74b9d016b72ae14`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T171558Z-qform13/REPORT.md`.
3. **Latest partner correction.** `QFORM-CONDITIONAL-THREEPROJ-2OVER3-MOMENT-FALSE-v1`, canonical source `yspennstate/math-open-problems@60b3f717b1a0e336406bc2acdfc1eaf951906fca`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T174618Z-account03-B09-QFORM-r14/REPORT.md`, proves that the positive conditional spectral projection moment proposed by an earlier owner message diverges even in a target-valid cube family. I do not use that interface.
4. Fresh `CURRENT_RESEARCH` also records the stronger interactive corrections that an arbitrary-joint rank-three coarea cap and the positive conditional-projection moment are false. This proof never invokes either statement.

## 3. Main theorem: two aggregate cross directions suffice when one bank is internally flat

### Theorem — `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`

Let the original independent coordinates be partitioned into disjoint sets `I,J,K`, where `K` may be empty. Let `A` be any real symmetric matrix satisfying

`A[I,I]=0`.

Write `B=A[I,J]`, and suppose `B` has at least two nonzero singular values

`s_1 >= s_2 > 0`.

No restriction is placed on `A[J,J]`, `A[K,K]`, `A[I,K]`, `A[J,K]`, on the rank of `A`, or on any additional eigenvalues. Then for every permitted product input law,

`boxed( ||p_(X^T A X)||_infinity <= 2 sqrt(pi) / sqrt(s_1 s_2). )`     (3.1)

Consequently every interval `L` satisfies the direct linear small-ball estimate

`boxed( P{X^T A X in L} <= [2 sqrt(pi)/sqrt(s_1 s_2)] |L|. )`          (3.2)

This uses no Cauchy--Schwarz decoupling, no resampling, and no square-root loss in `|L|`.

### Proof

Condition on the original coordinates `X_K`. Product provenance is preserved: `X_I` and `X_J` remain independent product vectors with the original cap-one marginals. Since the entire physical `I x I` block is zero, the conditional form has the exact shape

`Q = 2 X_I^T (B X_J + d) + H(X_J)`,                                  (3.3)

where `d` is deterministic under the conditioning and `H` is an arbitrary measurable quadratic-affine function of `X_J`. Thus all `J`-side self-curvature and all conditioned outside couplings remain present rather than being discarded.

Fix `X_J=y` and put

`c(y)=B y+d`.

For `c(y) !=0`, the one-dimensional LPP bound applied to the normalized original-coordinate linear form gives

`||p_(<c(y),X_I>)||_infinity <= sqrt(2)/||c(y)||_2`.

The random term in (3.3) is twice this linear form, so

`||p_(Q | X_J=y,X_K)||_infinity <= 1/[sqrt(2)||B y+d||_2]`.            (3.4)

Let `p_1,p_2` and `r_1,r_2` be left and right singular vectors of `B` corresponding to `s_1,s_2`. Define

`Z=(<r_1,X_J>, <r_2,X_J>)`.

This is a two-dimensional orthogonal marginal of the original product law on `J`, hence it has a density `rho_Z` with

`||rho_Z||_infinity <= 2`.                                           (3.5)

Let

`W=(s_1 Z_1,s_2 Z_2)`.

Then `W` has a two-dimensional density bounded by

`M := 2/(s_1 s_2)`.                                                   (3.6)

Projecting `By+d` onto `span{p_1,p_2}` only decreases its norm, so for a deterministic shift `delta in R^2`,

`||B y+d||_2 >= ||W+delta||_2`.                                      (3.7)

The exceptional equation `B X_J+d=0` has probability zero: (3.7) forces `W=-delta`, and `W` has a two-dimensional density.

It remains to average one inverse radius. For every `R^2` random vector with density at most `M` and every shift `delta`, put `R=||W+delta||_2`. Then

`P{R<=r} <= min(1, M pi r^2)`.

Layer cake, with `t_0=sqrt(M pi)`, gives the translation-uniform estimate

`E R^(-1)`
` = int_0^infinity P{R<1/t} dt`
` <= t_0 + int_(t_0)^infinity M pi t^(-2) dt`
` = 2 sqrt(M pi)`.                                                    (3.8)

Average (3.4), use (3.7)-(3.8), and substitute (3.6):

`||p_(Q | X_K)||_infinity`
` <= (1/sqrt(2)) 2 sqrt(M pi)`
` <= 2 sqrt(pi)/sqrt(s_1 s_2)`.                                      (3.9)

The bound is uniform in the conditioned value of `X_K`, so averaging the conditional laws proves (3.1). Equation (3.2) follows immediately. QED.

### What the theorem preserves

The singular vectors are used only to take a low-dimensional marginal **inside the original independent bank `J`**. The variables `Z_1,Z_2` are not declared independent; only their genuine two-dimensional marginal-density cap is used. The whole opposite-side quadratic phase `H(X_J)` is retained as a shift after conditioning. Thus the argument is compatible with the no-post-rotation-independence correction and with the latest failure of conditional spectral `L^infinity` moments.

The theorem also uses the actual top two singular directions of the full physical cross block. It does not pay the determinant of a selected `2x2` or `3x3` coordinate minor and is insensitive to how diffuse those singular vectors are.

## 4. A target-valid diffuse family where aggregate payment removes a local-minor loss

Let `m>=4` be even. On `R^m`, define the orthonormal Walsh-type vectors

`u=m^(-1/2)(1,...,1)`,

`v=m^(-1/2)(1,...,1,-1,...,-1)`,

with `m/2` plus signs and `m/2` minus signs in `v`, and put

`P=u u^T+v v^T`.

Thus `P` is a rank-two orthogonal projection. On two disjoint physical banks `I,J`, each of size `m`, set

`A_m = [[0, 2P], [2P, D]]`,                                         (4.1)

where `D=e_1 e_1^T` is the rank-one physical square on the first `J` coordinate.

The base matrix with `D=0` has nonzero spectrum `{2,2,-2,-2}`. The perturbation `diag(0,D)` has operator norm one. Weyl's singular-value perturbation inequality therefore gives

`s_4(A_m)>=1`,                                                        (4.2)

so `A_m` has at least four eigenvalues of modulus at least one. This is an exact target-valid family, not merely a low-rank method test.

The cross block `2P` has two nonzero singular values `s_1=s_2=2`. The theorem therefore gives, uniformly in `m` and in every admissible product input law,

`boxed( ||p_(X^T A_m X)||_infinity <= sqrt(pi). )`                    (4.3)

Yet the individual physical cross coefficients are diffuse: since

`P_ab = 2/m` when `a,b` belong to the same Walsh half and `0` otherwise,

all nonzero entries of `2P` equal `4/m` and tend to zero.

## 5. Named partner result applied to the same family

Take an `I` coordinate `i` in the first Walsh half, the perturbed `J` coordinate `j_0=1`, and another `J` coordinate `k` in the same half. In the order `(j_0,i,k)`, the physical principal triple is

`C_m = [[1,4/m,0], [4/m,0,4/m], [0,4/m,0]]`.                         (5.1)

Its first physical pair

`H_m=[[1,4/m],[4/m,0]]`

is invertible indefinite, and

`det C_m = -16/m^2`.                                                  (5.2)

Apply the completed named-partner theorem `QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1` with the nonzero diagonal coefficient `r=1`. It gives the valid ambient inequality

`||p_(X^T A_m X)||_infinity`
` <=16 sqrt(15) (16/m^2)^(-1/4)`
` =8 sqrt(15) sqrt(m)`.                                               (5.3)

Equation (5.3) is not wrong; it is a local-triple payment. Comparing (4.3) with (5.3) shows exactly what the new bank theorem gains: it aggregates the two true singular directions before any reciprocal diffuse coordinate minor is paid, replacing a `sqrt(m)` local loss by the dimension-free `sqrt(pi)` bound.

## 6. Compatibility with the newest partner correction

The latest completed account03/B09 run proves that

`E ||rho_(Y|Z)||_infinity^(2/3)`

can grow linearly in the block size after conditioning on all complementary spectral coordinates. The theorem in Section 3 does not take such a conditional spectral supremum. It conditions only on disjoint **original** coordinate banks, applies the genuine two-dimensional LPP marginal bound before conditioning inside the bank, and integrates the translation-uniform inverse-radius kernel directly. Thus the partner correction is applied as a routing constraint, not ignored.

The partner's three-block counterexample is not automatically covered by Section 3 because its large-direction blocks have nonzero internal quadratic parts. No claim beyond the exact theorem hypotheses is made.

## 7. Sharpened remaining implication

The analytic debt for an exactly flat coefficient-side bank is now gone. The next structural obligation is

**`QFORM-ZEROINTERNAL-WEDGE-OR-CURVED-SELF-BANK-v1`.** Starting only from `s_3(A)>=1`, and after the already proved diffuse/ridge/pair reductions, force either

1. a disjoint original-coordinate bank `I` with `A[I,I]=0` and a cross block whose two leading singular values have product bounded below at universal scale, so Section 3 applies;
2. an existing full-matrix indefinite-pair, scalar-pivot/rank-two-half-Riesz, ridge-window, or exact three-bank certificate; or
3. a quantitatively defined **curved self-bank residual** in which every potentially useful two-direction cross wedge is accompanied by unavoidable same-bank quadratic curvature, and prove a translation-uniform extension there.

The last case is the genuine new residual for this mechanism. It must be attacked without the disproved conditional spectral supremum, without assuming one uniformly good coordinate minor, and without discarding extra spectrum.

## 8. Status

- `QFORM-ZEROINTERNAL-BANK-WEDGE-v1`: **PROVED in the stated arbitrary-rank scope**.
- Target-valid diffuse family (4.1): **uniformly closed by (4.3)**.
- Named partner account03/B09 theorem: **applied quantitatively** in (5.3).
- Latest account03/B09 conditional-moment correction: **consumed and enforced**.
- Full arbitrary-matrix QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: not claimed by the new theorem; essential boundedness is proved in its scope.
