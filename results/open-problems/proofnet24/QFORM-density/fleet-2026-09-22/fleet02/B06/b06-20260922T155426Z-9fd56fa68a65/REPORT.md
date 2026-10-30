# fleet02/B06 — weighted affine fibers, a same-sign rank-two theorem, and a minority-pivot branch

**Run:** `b06-20260922T155426Z-9fd56fa68a65`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Curved fiber integration` / pathway `GEOMETRY`  
**Classification:** `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; full target **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport was used, not verified native learned-memory retrieval.

## 0. Scope, controls, corrections, and source pins

The sole target is the full arbitrary-dimension statement: independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and a real symmetric matrix `A` with at least three eigenvalues of modulus at least one; prove one universal essential bound for the density of `X^T A X`, or give a valid target counterexample. No moment, support, sign, diagonal-basis, or post-rotation-independence assumption is introduced.

Fresh control at the beginning was `yspennstate/math-research-brain@f18013218feca9ecaf9d62b4c462aa9f490d1bf7`; the pre-publication refresh reached `3675656d1533e3b20ac84be5b7cc71e38c99a0da`. The owner revision remained `2026-09-22.5`, with QFORM as the sole research target and no later applicable B06 stop. Required corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, and `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, together with the live correction inbox through the pre-publication snapshot. In particular, this report does not use unrestricted fiber suprema, post-rotation independence, conditional cap claims created by a change of variables, or a fixed-good-minor assertion.

Own predecessor consumed: fleet02/B06, `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`. It established the exact same-sign Pluecker determinant mass and an exact Hadamard delocalization obstruction, leaving `QFORM-WEIGHTED-CURVED-FIBER-AGGREGATION-v1` as the first unpaid implication.

The designated partner result actually consumed is fleet03/B06, run `20260922T151714Z-fleet03-B06-qform-r12`, canonical mathematics `yspennstate/math-open-problems@8624700dc9342807bbdf427e271fffcc518a0315`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T151714Z-fleet03-B06-qform-r12/REPORT.md`. Its `QFORM-RANK3-TWO-PIVOT-ENDPOINT-v1` gives, for exact rank three and a paid physical pair `(i,k)`,

`||p_Q||_infinity <= 94.356 [|a| |d|^2 |det Lambda| Delta_ik]^(-1/8)`

with `a=A_ii`, `d=A_ii A_kk-A_ik^2`, and `Delta_ik=||r_i wedge r_k||^2`. More importantly for the new inequality below, that completed report supplies the original-coordinate physical square-completion / one-sided square-kernel framework (source-pinned there to fleet04/B18) without manufacturing independence after rotation.

I also use the standard geometric rank-one Brascamp--Lieb inequality in the exact form already source-recorded in fleet02/B08, `yspennstate/math-open-problems@0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/B08-20260922T113624Z-qform11/REPORT.md`.

## 1. A weighted product-structure replacement for fiber suprema

The first unpaid implication can be partly repaired more cleanly than by pairwise reciprocal-minor averaging. The correct weights live on the **orthogonal complement of the spectral fiber** and enter before any supremum is taken.

### Theorem 1 — `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`

Let `X=(X_1,...,X_n)` have independent coordinates with probability densities `f_i<=1`. Let `R` be an `n x k` real matrix with orthonormal columns, and write `r_i` for row `i`,

`ell_i=||r_i||^2`,  `0<=ell_i<=1`.

Then the spectral projection

`Y=R^T X in R^k`

has an essentially bounded density `g`, and

`||g||_infinity <= product_{i:ell_i<1} (1-ell_i)^(-(1-ell_i)/2) <= exp(k/2)`.       (1.1)

Rows with `ell_i=1` contribute the factor `1` by convention.

This statement is dimension-free. It keeps the original product measure active on every affine fiber and therefore does **not** perform the refuted operation of integrating an unrestricted fiber supremum.

### Proof

Put `E=ker(R^T)`, so `dim E=n-k`, and let `P_E=I-RR^T`. Since `R^T R=I_k`, the linear coarea Jacobian of `R^T:R^n->R^k` equals one. For almost every `y`, choosing any `x_0` with `R^T x_0=y`,

`g(y)=int_E product_i f_i(x_{0,i}+<P_E e_i,z>) dz`.                    (1.2)

Set

`v_i=P_E e_i`,  `c_i=||v_i||^2=1-ell_i`.                              (1.3)

When `c_i=0`, the `i`th coordinate is constant along the fiber and its density factor is at most one, so omit it. For `c_i>0`, put `u_i=v_i/sqrt(c_i)`. Restricted to `E`,

`sum_i c_i u_i u_i^T = sum_i v_i v_i^T = I_E`.                        (1.4)

For the fixed fiber define

`h_i(s)=f_i(x_{0,i}+sqrt(c_i)s)^(1/c_i)`.                              (1.5)

Then the integrand in (1.2) is exactly

`product_i h_i(<u_i,z>)^(c_i)`.                                       (1.6)

Because `0<=f_i<=1`, `int f_i=1`, and `1/c_i>=1`,

`int_R h_i(s) ds
 = c_i^(-1/2) int_R f_i(x)^(1/c_i) dx
 <= c_i^(-1/2)`.                                                       (1.7)

Apply geometric Brascamp--Lieb to (1.4)--(1.7):

`g(y)<=product_i (int h_i)^(c_i)
      <=product_i c_i^(-c_i/2)`.                                      (1.8)

This is uniform in `y`. Finally, for `0<c<=1`,

`c log(1/c)<=1-c`.                                                     (1.9)

Hence

`log product_i c_i^(-c_i/2)
 <= (1/2) sum_i (1-c_i)
 = (1/2) sum_i ell_i
 = k/2`,                                                               (1.10)

because `sum_i ell_i=tr(RR^T)=k`. This proves (1.1). `QED`

### Interpretation

The repaired fiber mechanism is an exact weighted integral, not a maximum. The complement leverages `c_i=1-ell_i` are precisely the Brascamp--Lieb exponents needed to integrate the original product density along the affine spectral fiber. In particular, even if a spectral plane is completely delocalized over `n` coordinates, the whole projected two-dimensional density remains uniformly bounded; no factor of `n` appears.

## 2. Same-sign rank-two quadratic forms in arbitrary rotated physical coordinates

Theorem 1 immediately turns the ellipse geometry from the previous B06 run into a rotation-safe result.

### Corollary 2 — `QFORM-ROTATED-DEFINITE-RANK2-v1`

Let `S` be a real symmetric matrix of exact rank two with its two nonzero eigenvalues `beta_1,beta_2` of the same sign. For independent cap-one input coordinates,

`||p_(X^T S X)||_infinity <= pi e / sqrt(|beta_1 beta_2|)`.            (2.1)

### Proof

Write `S=R diag(beta_1,beta_2) R^T` with `R^T R=I_2`, and put `Y=R^T X`. Theorem 1 with `k=2` gives a joint density `g_Y<=e` without asserting that the two coordinates of `Y` are independent. For a positive-definite pair, coarea in `R^2` gives

`int_{R^2} delta(t-beta_1 y_1^2-beta_2 y_2^2)dy
 = pi/sqrt(beta_1 beta_2)`                                             (2.2)

on the supported side of the level. Multiplying by the cap `e` yields (2.1). The negative-definite case follows by reflection. `QED`

This is a genuine curved-fiber theorem: the projected law may be highly dependent, but its full two-dimensional density cap is obtained from the original product structure before the ellipse is integrated.

## 3. Applying the partner square-kernel mechanism: a one-pivot exact-rank-three branch

The previous theorem can now be paid inside a physical Schur complement.

### Theorem 3 — `QFORM-MINORITY-PIVOT-CURVED-FIBER-v1`

Assume `A=R Lambda R^T` has exact rank three, `R^T R=I_3`, and all three nonzero eigenvalues satisfy `|lambda_j|>=1`. Suppose the signature is `(2,1)` or `(1,2)`. Let `i` be a physical coordinate with

`a=A_ii !=0`,  `ell_i=||r_i||^2>0`,                                  (3.1)

and suppose `a` has the **minority sign** of the inertia of `A`. Then `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity
 <= 2 sqrt(2 pi e) [ |a| |det Lambda| ell_i ]^(-1/4)`.                 (3.2)

Numerically `2 sqrt(2 pi e)<8.266`. Since `|det Lambda|>=1`, a branch with `|a| ell_i>=eta` has the explicit bound `8.266 eta^(-1/4)`.

### Proof

Write the physical block decomposition around coordinate `i` as

`A=[[a,b^T],[b,C]]`.

Completing the square only in the original independent coordinate `X_i` gives

`Q=a(X_i+a^(-1)b^T Z)^2 + Z^T S_i Z`,
`S_i=C-bb^T/a`.                                                       (3.3)

By Sylvester inertia under this congruence, because `a` has the unique minority sign, the rank-two Schur complement `S_i` is semidefinite of the majority sign and has exactly two nonzero eigenvalues of that sign.

We need its pseudodeterminant. For every two-set `J` of coordinates outside `i`, Schur's determinant identity gives

`det (S_i)_J = det A_{ {i} union J } / a`.                             (3.4)

For exact rank three,

`det A_K = det(Lambda) det(R_K)^2`                                    (3.5)

for every physical three-set `K`. Summing (3.4) over `|J|=2` and using Cauchy--Binet / the projection determinantal identity

`sum_{J:|J|=2, J not contains i} det(R_{ {i} union J })^2 = ell_i`,    (3.6)

we obtain

`pdet(S_i)=det(Lambda) ell_i / a`.                                    (3.7)

The signs agree in the minority-pivot branch, so this quantity is positive. Corollary 2 applied to the independent coordinates `Z` therefore gives the residual density `h` the cap

`M:=||h||_infinity
 <= pi e / sqrt(|pdet(S_i)|)`.                                        (3.8)

Now apply the physical square-kernel mechanism used in the completed partner report. Conditional on `Z`, the shifted variable

`V=X_i+a^(-1)b^T Z`                                                   (3.9)

has a translate of the original density of `X_i`, hence density at most one. Conditioning further on the residual value `Z^T S_i Z=r` only mixes such translates, so the conditional density of `V|r` is still at most one. Thus

`p_Q(t)<=|a|^(-1/2) int_0^infinity h(t +/- u) u^(-1/2)du`,             (3.10)

with the sign chosen according to `a`.

For any probability density `h<=M` and any `rho>0`,

`int_0^infinity h(t-u)u^(-1/2)du
 <= 2M sqrt(rho)+rho^(-1/2)`.                                         (3.11)

The first term uses the `L^infinity` cap; the second uses total mass one. Optimizing at `rho=(2M)^(-1)` yields

`<=2 sqrt(2M)`.                                                       (3.12)

Insert (3.8) and then (3.7) into (3.10)--(3.12):

`||p_Q||_infinity
 <=2 sqrt(2 pi e)|a|^(-1/2)|pdet(S_i)|^(-1/4)
 =2 sqrt(2 pi e)[|a||det Lambda|ell_i]^(-1/4)`.                        (3.13)

This proves (3.2). `QED`

### Relation to the named partner result

This theorem uses the partner's completed original-coordinate square-completion / one-sided square-kernel mechanism at an actual inequality. The payment is different: instead of needing a second physical pivot and the pair certificate `d`, the minority-sign condition makes the entire first Schur complement same-sign rank two, and Theorem 1 pays its rotated two-dimensional product density globally. Where both hypotheses are available, one may take the better of (3.2) and the partner's two-pivot endpoint bound.

## 4. Exact adversary: same-sign Pluecker mass and two-pivot support can be disjoint

A tempting next step would be to average the partner's pairwise two-pivot certificates using the same-sign Pluecker weights from the previous B06 run. That is false in the strongest possible support sense.

### Construction — `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`

Let `n=2^m`, take the first three normalized columns of a Sylvester--Hadamard matrix,

`r_i=(1,s_i,t_i)/sqrt(n)`,  `s_i,t_i in {+1,-1}`,

and let

`A=R diag(1,1,-1)R^T`.                                                (4.1)

This is an exact-rank-three target matrix with nonzero spectrum `{1,1,-1}`. For the same-sign positive plane spanned by the first two columns, the Pluecker weight on a physical pair is

`w_ij=det([[1,s_i],[1,s_j]])^2/n^2`,                                  (4.2)

so `w_ij>0` exactly when `s_i!=s_j`.

But in that case

`A_ii=1/n`,
`A_ij=(1+s_i s_j-t_i t_j)/n=-t_i t_j/n`,                              (4.3)

and therefore the **full** physical two-pivot determinant is

`d_ij=A_ii A_jj-A_ij^2=0`.                                            (4.4)

Thus every pair carrying positive same-sign spectral determinant mass has zero full two-pivot determinant. Directly weighting the partner reciprocal pair certificate by the same-sign Pluecker measure cannot work: its denominator is singular on the entire support of that measure.

Conversely, in the exact `n=16` checker, all 32 pairs with nonzero full determinant have `w_ij=0`; the two supports are disjoint. This is a route counterexample, not a counterexample to QFORM.

The repair is conceptual and concrete: **aggregate the product law on the same-sign spectral plane before adding the cancelling third eigendirection.** Theorem 1 performs exactly that operation. Only after the plane has been paid by an affine-fiber Brascamp--Lieb cap should one use the remaining curvature (for example through the minority physical pivot of Theorem 3).

## 5. Exact checker and reproducibility

A deterministic exact-arithmetic checker was executed. It verifies both the Hadamard support-disjoint identity and a nontrivial minority-pivot pseudodeterminant instance.

For `n=16` it verifies:

- 64 physical pairs have positive same-sign Pluecker weight;
- their total Pluecker weight is exactly `1`;
- every one of those 64 pairs has full physical two-pivot determinant zero;
- all 32 nonzero full physical pair determinants occur at zero same-sign Pluecker weight;
- for the explicit orthogonal frame
  `[(5/13,0,12/13),(0,1,0),(-12/13,0,5/13)]`
  and `Lambda=diag(2,1,-1)`, the first physical pivot has `a=-94/169`, leverage `ell=1`, positive rank-two Schur pseudodeterminant `169/47`, exactly equal to `det(Lambda)ell/a`;
- the universal constant `2 sqrt(2 pi e)=8.265462708244986`.

Checker SHA-256: `f5375228abb6310aab2ca5dbb0d32a33e63aa058becccc41cbadeeee8303b0f1`.  
Output SHA-256: `3ba7218e490ac9d46b7112d20bdadeb9a1b7d018e35601498048fe8173602d14`.  
Status: `PASS`.

The exact checker and exact output are stored beside this report.

## 6. Compact conditional route and first unpaid implication

The current geometry route can now be stated more sharply.

1. A `k`-dimensional spectral projection of an arbitrary cap-one product law has a dimension-free density cap `e^(k/2)` by Theorem 1. This is the requested product-structure-preserving replacement for the dimension-losing affine-fiber supremum.
2. Consequently every rotated same-sign rank-two form has density at most `pi e / sqrt(|beta_1 beta_2|)`.
3. In exact rank three, any sufficiently paid minority-sign physical diagonal closes immediately by Theorem 3.
4. Independently, the named partner closes any sufficiently paid two-pivot pair by its `J_ik` endpoint certificate.
5. One may **not** force these pair certificates by averaging against the same-sign Pluecker weights; Construction 4 makes the supports disjoint.
6. The already-completed diffuse exact-rank-three theorem (fleet02/B08) closes the regime of maximum rank-three row leverage at most `1/2` by a different Fourier--Brascamp--Lieb argument.

Therefore the first exact-rank-three unpaid geometry implication is now:

### `QFORM-MAJORITY-HEAVY-OR-ISOTROPIC-AGGREGATE-v1`

In the high-leverage exact-rank-three regime not paid by Theorem 3, prove that either a majority-sign physical pivot admits a quantitatively paid partner two-pivot certificate, or the finitely many high-leverage rows can be reduced to a product-preserving indefinite/light-cone aggregate without reciprocal inversion of a single physical minor. Any proof must allow the possibility that all physical diagonals have the majority sign and must not pair same-sign Pluecker mass directly with full pair determinants.

After exact rank three is closed, an additional full-target debt remains: arbitrary smaller nonzero spectral components cannot be discarded as independent noise. The current ridge-window supporting theorem covers one diffuse high-spectral-window regime with arbitrary small nonseparable tails, but its window hypothesis is not automatic. Thus no full target proof or continuity theorem is claimed here.

## 7. Status

**PROVED / supporting:** `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`; `QFORM-ROTATED-DEFINITE-RANK2-v1`; `QFORM-MINORITY-PIVOT-CURVED-FIBER-v1` in exact rank three; the one-pivot pseudodeterminant identity used there.

**CANDIDATE_REFUTED:** direct averaging of the named partner's full two-pivot certificate against the same-sign Pluecker determinant-mass weights.

**OPEN:** `QFORM-MAJORITY-HEAVY-OR-ISOTROPIC-AGGREGATE-v1`, the extra-spectrum bridge outside completed supporting branches, and the full universal QFORM conjecture.

## 8. Privacy / provenance check

Before publication I reviewed the changed-file allowlist for this run and ran a narrow generated-content lexical fallback scan for credentials, signed links, scheduler identifiers, private unrelated material, and machine paths. No such content is included. This limited generated-file scan is not a repository-wide secret scanner and is recorded as such.
