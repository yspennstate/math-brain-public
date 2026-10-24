# account02/B09 — multi-pivot bilinear small-ball theorem

**Run:** `20260922T115241Z-account02-B09-QFORM-r1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Bilinear block mechanism`  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full target **OPEN / NOT PROVED / NOT DISPROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Live target and corrections consumed

The later owner control supersedes the stale FEI prompt. The active target is: for independent real coordinates with probability densities at most one and a real symmetric matrix having at least three eigenvalues of magnitude at least one, prove a universal bound on the density of `Q=X^T A X`, or produce a genuine counterexample.

The following live corrections are enforced:

1. law-uniform pointwise Fresnel decay is false for arbitrary densities bounded by one;
2. taking unrestricted suprema over spectral fibers can lose a factor growing with dimension;
3. diagonalizing `A` does not preserve independence.

Accordingly the proof below is a direct interval/small-ball argument in the original independent coordinates. It uses no Fourier pointwise decay and no rotated-coordinate independence.

## 2. Sources actually consumed

- `account03/B17`, math-open-problems commit `c64fcff680b0a252a3c92002c60eedba02bbb9ec`: exact refutation of law-uniform pointwise Fresnel decay and diagonal `C=pi` theorem.
- **OTHER-account result applied:** `account03/B01`, shared handoff commit `47dc94f0d2e847cd4d89bf4c8ec45816fb042324`, canonical report commit `c7a1ce265139092705e86c5a577523798291b964`: common product envelope and a three-coordinate non-diagonal block theorem with density `<= C0 |det A_S|^{-1/3}`, `C0<7.90`.
- `account02/B07`, shared handoff commit `a333185e6a76510285063e4db1d20801b904b852`: exterior-power determinant-mass identities and the Walsh delocalization obstruction to fixed coordinate-minor selection.
- `account02/B10`, canonical report commit `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`: hyperbolic-square smoothing and a quantitative Pluecker reciprocal-loss obstruction.

The assigned partner `account03/B09` had no completed current-programme handoff at the checked source path, so no partner theorem is fabricated or awaited.

## 3. Main theorem: direct multi-pivot linearization

### Theorem 3.1 — `QFORM-MULTIPIVOT-BILINEAR-SMALLBALL-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i<=1`. Let `A` be real symmetric. Suppose there are disjoint coordinate sets `I,J` with

- `|I|=|J|=m>=2`,
- the whole pivot principal block vanishes: `A[I,I]=0`,
- the square cross block `B=A[I,J]` is invertible.

Then for every interval `L` of length `ell`,

`P{X^T A X in L} <= [m/(m-1)] |det B|^{-1/m} ell`.

Consequently `Q=X^T A X` is absolutely continuous and has a version of its density satisfying

`||p_Q||_infinity <= [m/(m-1)] |det B|^{-1/m}`.

In particular for a two-pivot packet,

`||p_Q||_infinity <= 2 / sqrt(|det A[I,J]|)`.

This is dimension-free and law-independent.

### Proof

Condition on every coordinate outside `I union J`. Write `x=X_I`, `y=X_J`. Because `A[I,I]=0`, all dependence on `x` is linear:

`Q = 2 x^T (B y + d) + H(y)`,

where `d` is a deterministic vector under the conditioning and `H` is an arbitrary measurable quadratic/affine expression in `y` (plus the conditioned coordinates). No assumption on `A[J,J]` is needed.

Fix `y`. Put `c=2(By+d)`. The variables `x_i`, `i in I`, remain independent and each has density at most one. If `c_k!=0`, the scaled variable `c_k x_k` has density with `L^infinity` norm at most `1/|c_k|`. Convolution with the remaining independent summands cannot increase `L^infinity`; therefore the conditional density of `c^T x` satisfies

`||p_{c^T x | y}||_infinity <= 1/max_k |c_k| = 1/[2 ||By+d||_infinity]`.

The exceptional event `By+d=0` has probability zero because `B` is invertible and `y` has a joint density.

It remains to average the reciprocal coefficient without paying a square-root decoupling loss. Let

`Z=By+d`.

Since `y` has joint density `prod_{j in J} f_j(y_j)<=1`, the variable `Z` has a probability density `h` satisfying

`0<=h(z)<=M:=|det B|^{-1}`.

For `R=||Z||_infinity`, the cube volume bound gives for every `r>0`

`P{R<r} <= min(1, M (2r)^m)`.

By layer cake,

`E R^{-1} = integral_0^infinity P{R<t^{-1}} dt`

`<= integral_0^infinity min(1, 2^m M t^{-m}) dt`.

The two terms meet at `t0=2 M^{1/m}`. Since `m>=2`,

`E R^{-1}`
`<= t0 + 2^m M integral_{t0}^infinity t^{-m} dt`
`= 2 M^{1/m} + [2/(m-1)] M^{1/m}`
`= [2m/(m-1)] M^{1/m}`.

Therefore, still under the outside conditioning,

`P{Q in L}`
`<= (ell/2) E R^{-1}`
`<= [m/(m-1)] |det B|^{-1/m} ell`.

The bound is independent of the conditioned coordinates, so averaging them preserves it. A finite measure satisfying `mu(L)<=C|L|` for every interval is absolutely continuous with Radon-Nikodym derivative at most `C` almost everywhere. This proves the theorem. `QED`

## 4. Why this avoids the forbidden square-root loss

A one-copy resampling argument gives bounds of the form

`P(Q in L)^2 <= P(Q-Q' in L-L)`

and therefore turns an `O(ell)` bound for the difference into only `O(sqrt(ell))` for `Q`. The theorem above never applies Cauchy-Schwarz or resampling. It conditions directly on a disjoint coefficient packet and integrates the exact reciprocal linear coefficient.

The dimension threshold in that reciprocal integral is sharp for this mechanism. For `m=1`,

`integral_0^infinity min(1,2Mt^{-1}) dt = infinity`.

This is not an artefact: `Q=2XY` with independent `Uniform[-1/2,1/2]` inputs has the familiar logarithmically unbounded product density. With two pivots, the singularity becomes `1/||(z1,z2)||`, which is integrable in the two-dimensional coefficient packet, giving an exact `O(ell)` bound.

## 5. A target-level family closed by the theorem

Take four independent coordinates and

`A = [[0,0,1,0],
      [0,0,0,1],
      [1,0,0,0],
      [0,1,0,0]]`.

Then

`Q=2(X1 X3 + X2 X4)`

and `spec(A)={1,1,-1,-1}`. Thus it is a genuine indefinite member of the owner's target class. Every `3x3` principal minor is singular, so a fixed nonsingular-three-coordinate theorem such as the account03/B01 or account02/B15 route does not apply directly. The present theorem uses `I={1,2}`, `J={3,4}`, `B=I_2` and gives the universal bound

`||p_Q||_infinity <= 2`.

This is a genuinely complementary block mechanism.

## 6. Counterexample to an overstrong cross-minor claim

A tempting but false strengthening is: "an invertible `2x2` cross block by itself forces bounded density, even when the pivot side has quadratic curvature." This is false, and the failure occurs at the sharp two-large-eigenvalue obstruction.

Let `X1,Y1,X2,Y2` be independent `Uniform[-1/2,1/2]` variables and set

`Q=(X1+Y1)^2-(X2+Y2)^2`.

With the partition `x=(X1,X2)`, `y=(Y1,Y2)`, the cross block is `B=diag(1,-1)`, so `|det B|=1`. However the full matrix has eigenvalues `{2,-2,0,0}` only.

Put `U=X1+Y1` and `V=X2+Y2`. They are independent with triangular density

`g(u)=1-|u|` on `[-1,1]`.

For `S=U^2`, the density on `(0,1)` is

`h(s)=s^{-1/2}-1`.

Hence the density of `Q=S1-S2` is unbounded at zero. More quantitatively, for `0<z<1/8` and `s in [2z,1/4]`,

`h(s)>=1/(2 sqrt(s))`,
`h(s-z)>=1/(2 sqrt(s))`,

so

`p_Q(z) >= (1/4) integral_{2z}^{1/4} ds/s = (1/4) log(1/(8z)) -> infinity`.

Thus `det A[I,J] !=0` is not enough: the exact linear-pivot condition `A[I,I]=0` (or a different genuine smoothing mechanism such as account02/B10's square term) is mathematically substantive.

This is a counterexample to the intermediate mechanism only, not to the owner conjecture.

## 7. Relation to other source-backed mechanisms

The account03/B01 theorem controls a nonsingular three-coordinate block by a product-envelope / square smoother and pays `|det|^{-1/3}`. The present theorem controls a disjoint linear-pivot packet and pays `|det B|^{-1/m}`. The pure four-coordinate hyperbolic block in Section 5 is invisible to every `3x3` principal determinant but is solved by the present packet.

Account02/B07 proves that the spectral hypothesis supplies dimension-free *total* exterior-minor mass, while flat Walsh frames can spread that mass over many tiny coordinate minors. Account02/B10 independently verifies that paying reciprocal local minor constants before aggregation can lose a factor growing with dimension. Therefore the new theorem should not be combined with spectral determinant mass by selecting one largest minor; the aggregation must happen before the reciprocal determinant cost is paid.

## 8. First essential missing implication

`QFORM-CURVATURE-OR-MULTIPIVOT-AGGREGATION-v1`:

Starting only from at least three eigenvalues with magnitude at least one, produce a product-preserving decomposition/aggregation which, with universal quantitative constants, yields at least one of the already source-valid local smoothers:

1. a definite physical `2x2` block (beta/coarea route);
2. a nonsingular three-coordinate block with controlled conditioning (account03/B01 / account02/B15);
3. a hyperbolic-square triangular triple (account02/B10); or
4. a disjoint `m>=2` linear-pivot packet from Theorem 3.1 with `|det B|^{1/m}` bounded below after aggregation.

The Walsh/Pluecker stress tests show that fixed-minor selection is not a valid bridge. The unpaid step is an aggregation theorem that keeps the original product law rather than rotating to the eigenbasis or taking fiber suprema.

## 9. Verification and status

No numerical computation is used as evidence for Theorem 3.1 or the counterexample; both are exact analytic derivations. The counterexample's matrix spectrum follows from two rank-one `2x2` blocks `[[1,1],[1,1]]` and `[[-1,-1],[-1,-1]]`.

**Status:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN`.
