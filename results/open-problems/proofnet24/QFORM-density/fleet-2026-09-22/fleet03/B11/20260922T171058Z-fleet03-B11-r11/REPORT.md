# fleet03/B11 — ruled-majority-sheet theorem for indefinite exact rank three

Run: `20260922T171058Z-fleet03-B11-r11`

Status: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM**. The full universal QFORM conjecture remains **OPEN / NOT PROVED**.

Execution status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not native learned-memory ingestion.

## 1. Scope and source-pinned premises

The full target is: for independent real coordinates `X_i` with probability densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension- and law-independent finite bound on the density of `Q=X^T A X`, or give a valid counterexample. Continuity is a separate requested conclusion.

This run stays on B11's genuinely indefinite signatures and changes mechanism from the preceding local-Pluecker selector to a global ruling/X-ray argument. It uses no post-rotation independence, no law-uniform pointwise Fresnel decay, no fiber-supremum estimate, and no moment/support/log-concavity assumptions.

The designated completed partner result actually applied is fleet04/B11:

`yspennstate/math-open-problems@44e7ab6750fbc3dccd77f1dd9e8bdba0bba2f0f5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T161514Z-b11-cone-trace-r1/REPORT.md`.

For a three-dimensional density `g` and

`q(u,v,w)=u^2+v^2-w^2`,                                       (1.1)

that report proves the exact a.e. cone-trace formula

`p_q(y) = (1/2) ∫_{w^2+y>0} ∫_0^{2π}`
`           g(sqrt(w^2+y) cos θ, sqrt(w^2+y) sin θ, w) dθ dw`. (1.2)

It also proves that a mere `L^infinity` cap on `g` cannot control this trace. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` likewise warns that generic X-ray control does not pay the minority-sign two-sheet trace. The theorem below deliberately controls only the majority-sign one-sheet side, where a new exact ruling identity is available.

A second completed input is the two-dimensional product-projection theorem from fleet02/B11:

`yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`.

If independent cap-one coordinates are mapped by an `n x 2` matrix `C` with `C^T C=I_2`, then the resulting two-dimensional density is bounded by `e`.

## 2. Abstract theorem: bounded 2D marginals control the one-sheet trace

### Theorem 2.1 — RULED-MAJORITY-SHEET

Let `Y=(Y_1,Y_2,Y_3)` be an arbitrary random vector in `R^3`. Assume that for every `3 x 2` matrix `U` with `U^T U=I_2`, the orthogonal two-dimensional projection `U^T Y` has a density bounded by the same constant `K`.

Put

`S=Y_1^2+Y_2^2-Y_3^2`.

Then the restriction of the law of `S` to `(0,infinity)` is absolutely continuous and its density satisfies

`||p_S||_{L^infinity(0,infinity)} <= π K / sqrt(2)`.          (2.1)

No three-dimensional density cap for `Y` is assumed.

### Proof for a smooth density

First suppose `Y` has a smooth density `g`. Fix `s=a^2>0`, `a>0`. Applying the designated partner identity (1.2),

`p_S(a^2)`
` = (1/2) ∫_R ∫_0^{2π}`
`      g(sqrt(a^2+t^2) cos θ, sqrt(a^2+t^2) sin θ, t) dθ dt`. (2.2)

For each `phi` define the affine line

`F_{a,phi}(t)`
` = (a cos phi - t sin phi, a sin phi + t cos phi, t)`.       (2.3)

Two exact identities drive the proof:

`q(F_{a,phi}(t))=a^2`,                                       (2.4)

and

`|dF_{a,phi}/dt|=sqrt(2)`.                                   (2.5)

For fixed `t`, the first two coordinates of (2.3) have radius `sqrt(a^2+t^2)` and polar angle

`theta = phi + arctan(t/a)` modulo `2π`.

Hence `dtheta=dphi`, and (2.2) becomes

`p_S(a^2)`
` = (1/2) ∫_0^{2π} ∫_R g(F_{a,phi}(t)) dt dphi`.              (2.6)

For fixed `phi`, the line direction is

`v_phi=(-sin phi, cos phi, 1)`, `|v_phi|=sqrt(2)`.            (2.7)

Let `P_phi` denote orthogonal projection onto `v_phi^perp`. The arclength integral of `g` over the line (2.3) is exactly one value of the density of `P_phi Y`. By hypothesis that density is at most `K`. Since arclength is `sqrt(2) dt`,

`∫_R g(F_{a,phi}(t)) dt <= K/sqrt(2)`.                        (2.8)

Substitution in (2.6) gives

`p_S(a^2) <= (1/2)(2π) K/sqrt(2) = πK/sqrt(2)`,              (2.9)

uniformly in `a>0`.

### Removal of smoothness

Let `G~N(0,I_3)` be independent and put `Y_epsilon=Y+epsilon G`. Every orthogonal two-dimensional projection of `Y_epsilon` is the convolution of the corresponding projection density of `Y` with a probability Gaussian density, so its `L^infinity` norm is still at most `K`.

The vector `Y_epsilon` has a smooth density, hence (2.9) applies to `S_epsilon=q(Y_epsilon)`. For every nonnegative `psi in C_c((0,infinity))`,

`E psi(S_epsilon) <= (πK/sqrt(2)) ∫ psi(s) ds`.               (2.10)

As `epsilon ->0`, `S_epsilon ->S` almost surely, so bounded convergence gives the same inequality for `S`. By measure domination, the restriction of the law of `S` to `(0,infinity)` has a density bounded by `πK/sqrt(2)`. This proves (2.1). QED.

### Why this does not contradict the two-sheet correction

For `s>0`, the level `u^2+v^2-w^2=s` is a one-sheet hyperboloid and is ruled by the straight lines (2.3). The proof converts its cone trace exactly into an angular average of line X-rays.

For `s<0`, the level is a two-sheet hyperboloid. There is no real straight-line ruling of the same type, and the live correction supplies examples showing that an X-ray cap by itself does not control that trace. The theorem therefore makes no minority-side claim.

## 3. Exact-rank-three QFORM consequence

### Theorem 3.1 — majority-sign half-line is universally bounded

Let `A` have exact rank three,

`A=R Lambda R^T`, `R^T R=I_3`,                               (3.1)

and suppose its three nonzero eigenvalues have signature `(+,+,-)` with

`lambda_1>=1`, `lambda_2>=1`, `lambda_3<=-1`.                 (3.2)

For arbitrary independent real `X_i` with densities at most one, let `Q=X^T A X`. Then

`||p_Q||_{L^infinity(0,infinity)} <= π e / sqrt(2)`
`                                      < 6.039`.              (3.3)

For signature `(+,-,-)`, the reflected statement holds:

`||p_Q||_{L^infinity(-infinity,0)} <= π e / sqrt(2)`.         (3.4)

Thus the entire half-line having the **majority eigenvalue sign** is controlled for every rotation, every dimension, and every admissible product input law. No leverage, Pluecker localization, or good physical minor is required.

### Proof

In the `(+,+,-)` case define

`D=diag(sqrt(lambda_1), sqrt(lambda_2), sqrt(-lambda_3))`,
`Y=D R^T X`.                                                   (3.5)

Then

`Q=Y_1^2+Y_2^2-Y_3^2`.                                        (3.6)

It remains to verify Theorem 2.1 with `K=e`. Let `U` be any `3 x 2` orthonormal frame and set

`B=R D U`, `G_U=B^T B=U^T D^2 U`.                             (3.7)

Since every diagonal entry of `D^2` is at least one,

`G_U >= I_2`, hence `det G_U>=1`.                              (3.8)

Whiten in the two-dimensional **target plane only**:

`C=B G_U^{-1/2}`.                                              (3.9)

Then `C^T C=I_2`. The completed two-dimensional product-projection theorem therefore gives

`||p_{C^T X}||_infinity <= e`.                                (3.10)

But

`U^T Y = B^T X = G_U^{1/2} C^T X`,                            (3.11)

so change of variables yields

`||p_{U^T Y}||_infinity`
` <= e / sqrt(det G_U) <= e`.                                 (3.12)

This establishes the hypothesis of Theorem 2.1 with `K=e`. Equation (3.3) follows. Replacing `A` by `-A` proves (3.4). QED.

Numerically,

`π e / sqrt(2) = 6.038503978383308...`.                        (3.13)

## 4. Actual application of the designated partner result

The fleet04/B11 cone-trace identity (1.2) is not cited merely as context: equation (2.2) is that exact identity at the positive level `y=a^2`. The new ruling substitution turns the partner's curved trace into

`p_q(a^2)`
` = (1/2) ∫_0^{2π} [one line-X-ray of g]/sqrt(2) dphi,         (4.1)

and the product-projection theorem pays each bracket by `e` after the spectral scaling/whitening in (3.7)-(3.12). Thus the completed partner result enters the actual numerical inequality

`p_Q(s) <= π e/sqrt(2),  s>0`,                                (4.2)

rather than only motivating the argument.

This also explains why the partner's arbitrary bounded-density cone tube is not a counterexample to (4.2): the present proof uses the much stronger genuine-product fact that **every relevant two-dimensional linear marginal** has a universal density cap.

## 5. Why the third direction removes the rank-two logarithm on this side

For independent `X,Y~Unif[-1/2,1/2]`, the rank-two saddle `2XY` has

`p_{2XY}(z)=log(1/(2|z|)),  0<|z|<1/2`,                       (5.1)

so the opposite-sign rank-two logarithmic singularity is retained exactly.

In three dimensions, the majority-sign level set is not merely a thickened hyperbola: it becomes a ruled one-sheet hyperboloid. The extra direction turns the coarea trace into a one-parameter average of complete straight-line fibers. Original-coordinate product structure controls each such line fiber through the two-dimensional projection-density theorem. There is no remaining scale-by-scale logarithmic accumulation on this side.

This is a different mechanism from the preceding B11 Pluecker theorem: no single physical triple is selected and no reciprocal minor is paid.

## 6. Regression computation

`VERIFY.py` beside this report checks, with standard-library arithmetic:

1. `q(F_{a,phi}(t))=a^2` numerically over 5,000 seeded points;
2. the ruling direction has squared speed exactly `2` up to floating error;
3. for 10,000 random orthonormal two-frames and random `D^2>=I`, the compressed matrix `G_U=U^T D^2 U` satisfies the two-dimensional PSD test `G_U-I>=0` and `det G_U>=1`;
4. the reported constant `πe/sqrt(2)=6.038503978383308...`.

The check terminates `QFORM_RULED_MAJORITY_SHEET_CHECK_PASS`. This is regression only; the proof is Sections 2-3.

## 7. Remaining first implication

The full conjecture is not closed. The new theorem removes one complete sign half-line in every genuinely rotated **exact-rank-three** indefinite target. The first remaining B11 implication is now sharply asymmetric:

**MINORITY TWO-SHEET PRODUCT TRACE.** For signature `(+,+,-)`, control `p_Q(s)` uniformly for `s<0` using more product provenance than the bare X-ray norm; equivalently, find a product-valid replacement for the missing straight-line ruling of the two-sheet hyperboloid. For `(+,-,-)` the unpaid side is `s>0`.

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction proves that one cannot simply repeat the present X-ray argument there. Candidate next mechanisms are translation-uniform half-Riesz synthesis, parabolic smoothing in a null chart, or an aggregate shear/ridge decomposition retaining original-coordinate product provenance.

A separate full-target debt remains when `A` has additional nonzero spectral directions: an exact-rank-three spectral truncation and the remaining quadratic term are generally dependent in the original product coordinates, so one cannot convolve the present rank-three bound with the remainder.

## 8. Continuity and integrity status

- New result: essential bounded density on the majority-sign open half-line, constant `πe/sqrt(2)`.
- Continuity of that density for arbitrary measurable cap-one input densities: **NOT PROVED** here.
- Minority-sign half-line: **OPEN** in this theorem.
- Exact-rank-three full density: **OPEN** because of that minority side.
- Arbitrary additional spectrum: **OPEN**.
- Full universal conjecture: **OPEN / NOT PROVED**.
- Designated partner fleet04/B11: **consumed and applied to equation (4.2)**.
- Opposite-sign rank-two logarithmic control: **retained**.
- Execution: **WITHOUT_VERIFIED_BRAIN**.

Narrow privacy review: this report contains only mathematical statements, repository source pins, the logical account/slot label, and a nonsecret run identifier. It contains no credentials, scheduler identifiers, machine paths, unrelated private transcripts, or public-release action.
