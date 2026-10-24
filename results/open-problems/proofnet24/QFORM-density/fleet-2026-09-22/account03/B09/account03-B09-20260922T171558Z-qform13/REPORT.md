# QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1

Run: `account03-B09-20260922T171558Z-qform13`  
Worker: `account03/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh start control: `yspennstate/math-research-brain@b5ddc3ce7894270ed6dcf4648cb96baea7dbc251`, OWNER CONTROL revision `2026-09-22.8`  
Status: **proved supporting theorem; full conjecture remains OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`

## 1. Contribution and why this run changes mechanism

The full target is to prove a universal constant `C` such that for every dimension, every product law of independent real coordinates with densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one,

`P(X^T A X in L) <= C |L|`

for every interval `L`, or to give a genuine counterexample.

Earlier B09 runs used a **nonzero scalar square pivot** and a Schur cross block. The current corrections show that one scalar pivot / one local rank-two cross minor is not structurally forced. This run therefore changes mechanism to an **indefinite two-coordinate physical pivot**. No square-root small-ball decoupling is used.

The main new result is a conditional end-to-end density theorem for an invertible physical `3x3` block whose first `2x2` principal block is indefinite. It is particularly useful in the previously unpaid case where the whole `3x3` block has zero diagonal: the scalar-pivot method is then unavailable, but a genuine bilinear pivot is automatic.

The argument has two ingredients:

1. a new universal logarithmic envelope for the product of two independent cap-one variables, uniform under arbitrary translations;
2. the already proved weak-`L^2` quadratic-ridge estimate from `account03/B16`, which turns that logarithmic singularity into a finite `L^infinity` output bound after the third independent coordinate is integrated.

This establishes an `O(|L|)` interval estimate directly. It proves essential boundedness in the stated branch, not continuity of the output density.

## 2. Source-pinned dependencies and corrections

Fresh control and state were read from `yspennstate/math-research-brain@b5ddc3ce7894270ed6dcf4648cb96baea7dbc251`, including `scheduled_tasks/README.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, the QFORM manifest/current research/claims/correction inbox/memory protocol, and `assignments/account03/B09.json`.

The only mathematical dependency used below is the weak-`L^2` logarithmic ridge estimate proved in

`yspennstate/math-open-problems@1defc84f1bfd79994a103a6d683c887d9dead1e7`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/B16-20260922T135620Z-r11/REPORT.md`.

In the notation

`Psi(s)=1+log(1/|s|)` for `0<|s|<=1`, and `Psi(s)=|s|^(-1/4)` for `|s|>=1`,

that source proves, uniformly in `a in R`,

`||Psi(a+z^2)||_{L^{2,infinity}(dz)} <= sqrt(15)`.

Consequently, after scaling, for every cap-one probability density `g` and every `delta>0`,

`integral g(z) Psi(a +/- delta z^2) dz <= 2 sqrt(15) delta^(-1/4)`.   (2.1)

The sign is irrelevant because `Psi` is even.

Relevant live corrections consumed before derivation include: law-uniform pointwise quadratic van-der-Corput decay is false; post-rotation coordinates are not independent; a bounded conditional density does not replace product provenance; one fixed cross minor / one exact rank-two Schur extraction is not forced by the three-large-eigenvalue hypothesis; and local principal-minor selection may lose dimension. None of those refuted premises is used here.

The designated partner is `account04/B09`. At the fresh source check there was no `account04/B09` QFORM directory in the canonical QFORM archive and no current shared handoff directory for that slot. Therefore there was no completed named-partner result that could honestly be applied in this invocation. The run proceeds asynchronously, as ordered, and does not fabricate partner consumption.

## 3. New elementary lemma: translated product laws have only a logarithmic singularity

### Lemma 3.1 — cap-one product density envelope

Let `U,V` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Translations of `U,V` are allowed. Then `W=UV` is absolutely continuous away from zero, with an a.e. density satisfying

`p_W(s) <= 2 Psi(s)`                                                   (3.1)

for every `s!=0`, where `Psi` is the function in Section 2. In particular, for every `beta!=0`,

`p_{2 beta UV}(s) <= |beta|^(-1) Psi(s/(2 beta))`.                     (3.2)

The estimates are uniform in the two input laws and in independent translations of the two variables.

### Proof

For `s!=0`, the standard product-density formula gives

`p_W(s)=integral_R f(x) g(s/x) dx/|x|`.

First suppose `0<|s|<=1`. Split the integral into

`|x|<|s|`, `|s|<=|x|<=1`, and `|x|>1`.

On `|x|<|s|`, make the change of variables `y=s/x`. Then `|y|>1` and

`integral_{|x|<|s|} f(x)g(s/x) dx/|x|`
` = integral_{|y|>1} f(s/y)g(y) dy/|y| <=1`,

using `f<=1`, `1/|y|<=1`, and `integral g=1`.

On `|s|<=|x|<=1`, use only `f,g<=1`:

`integral dx/|x| = 2 log(1/|s|)`.

On `|x|>1`, use `g<=1` and `1/|x|<=1`, giving at most `integral f=1`. Therefore

`p_W(s)<=2+2log(1/|s|)=2 Psi(s)`.

For `|s|>=1`, Cauchy--Schwarz gives the sharper estimate

`p_W(s)^2`
` <= [integral f(x)g(s/x) dx] [integral f(x)g(s/x) dx/x^2]`
` <= 1 * integral g(s/x) dx/x^2`
` = |s|^(-1) integral g(y)dy = |s|^(-1)`.

Here the first integral is at most `integral f=1`, and in the second we dropped `f<=1` before substituting `y=s/x`. Thus

`p_W(s)<=|s|^(-1/2)<=|s|^(-1/4)=Psi(s)<=2Psi(s)`.

Scaling by `2 beta` gives (3.2). Translating the two inputs merely replaces `f,g` by translated cap-one probability densities, so the same proof applies. QED.

**Why this lemma matters.** The generic Cauchy bound `|s|^(-1/2)` is too singular to combine at the critical point with a third square. The logarithmic bound near zero is the correct gain: a logarithm is integrable against the third-coordinate square ridge, and (2.1) quantifies that integration uniformly.

## 4. Density envelope for a physical indefinite two-coordinate block

Let

`H=[[r,s],[s,t]]`

be a real symmetric invertible **indefinite** `2x2` matrix, and put

`D=|det H|=s^2-rt>0`.

Let `X,Y` be independent cap-one variables; arbitrary deterministic translations are allowed.

### Lemma 4.1 — nonzero diagonal case

If `r!=0`, then the density of

`R=(X,Y) H (X,Y)^T`

satisfies

`p_R(u) <= 8 D^(-1/2) Psi(r u/D)`                                    (4.1)

for a.e. `u`. The same statement holds with `r` replaced by `t` if `t!=0`.

### Proof

Complete the square in the **original** coordinate `X`:

`R=r(X+(s/r)Y)^2 -(D/r)Y^2`.

Condition on `Y=y`. The translated variable `X+(s/r)y` still has a probability density at most one. The pushforward under `r Z^2` has density bounded by

`|r|^(-1/2)|v|^(-1/2)`

on the appropriate half-line. Hence

`p_R(u) <= |r|^(-1/2) integral g(y) |u+(D/r)y^2|^(-1/2)dy`.

Factor `D/|r|` from the absolute value. The remaining integral is exactly of the translated quadratic-kernel type bounded in the source B16 report by `8 Psi`; signs are absorbed by the evenness of `Psi`. The prefactors cancel to `D^(-1/2)`, giving (4.1). No rotated coordinate is declared independent. QED.

### Lemma 4.2 — pure bilinear case

If `r=t=0`, then `H=[[0,s],[s,0]]`, `D=s^2`, and Lemma 3.1 gives

`p_R(u) <= |s|^(-1) Psi(u/(2s))`.                                    (4.2)

This is the endpoint that remains well behaved when every scalar diagonal pivot vanishes.

## 5. Main theorem: indefinite pair plus one Schur coordinate

Take three **original independent coordinates** and write their physical principal block as

`B=[[H,v],[v^T,c]]`,                                                  (5.1)

where `H` is an invertible indefinite `2x2` matrix and `det B!=0`. Let an arbitrary ambient symmetric matrix contain this block. All coefficients outside the triple and all cross couplings to outside coordinates are unrestricted.

Condition on every outside original coordinate. The triple remains a product of the same three cap-one marginals; outside couplings become only affine terms plus a constant.

For fixed third coordinate `z` and fixed outside variables, complete the affine terms in the first two variables by translating them by `H^(-1)` times an affine vector. This translation may depend on `z` and on the outside variables, but conditional on those values it translates the two independent one-dimensional densities separately and preserves their cap-one property. The exact Schur identity gives

`Q = U_z^T H U_z + d z^2 + e z + k`,                                  (5.2)

where

`d=c-v^T H^(-1)v = det B/det H`,                                      (5.3)

and `e,k` may depend on the outside variables. Since `det B` and `det H` are nonzero, `d!=0`.

### Theorem 5.1 — QFORM-INDEFINITE-PAIR-SCHUR-SMOOTHING-v1

Under (5.1):

**(a) If a diagonal coefficient of `H` is nonzero**, say `r=H_11!=0`, then the full ambient quadratic form has an essentially bounded density satisfying

`||p_Q||_infinity <= 16 sqrt(15) (|r det B|)^(-1/4)`.                  (5.4)

The same bound with `t=H_22` holds if that diagonal is used instead.

**(b) If both diagonals of `H` vanish**, so `H=[[0,s],[s,0]]`, then

`||p_Q||_infinity <= 2^(5/4) sqrt(15) (|s det B|)^(-1/4)`.             (5.5)

Consequently every interval `L` obeys the corresponding linear estimate

`P(Q in L) <= ||p_Q||_infinity |L|`.                                  (5.6)

### Proof of (a)

By (4.1), conditional on `z` and the outside variables, the first-two-coordinate contribution has density at most

`8 D^(-1/2) Psi(r w/D)`

at displacement `w`, where `D=|det H|`.

Average this envelope over the third cap-one coordinate. Complete the square in `d z^2+e z`. The argument of `Psi` has quadratic coefficient

`delta=|r| |d|/D = |r det B|/D^2`,                                    (5.7)

using (5.3). Apply (2.1):

`p_{Q | outside}(y)`
` <= 8 D^(-1/2) * 2 sqrt(15) delta^(-1/4)`
` =16 sqrt(15) (|r det B|)^(-1/4)`.

The bound is independent of the conditioned outside coordinates. Averaging the conditional laws therefore preserves the same `L^infinity` bound, proving (5.4).

### Proof of (b)

Now `D=s^2`, and (4.2) gives the conditional first-two-coordinate density envelope

`|s|^(-1) Psi(w/(2s))`.

By (5.3),

`|d|=|det B|/s^2`.

After completing the square in the third coordinate, the coefficient inside `Psi` is

`delta=|d|/(2|s|)=|det B|/(2|s|^3)`.

Equation (2.1) yields

`p_{Q | outside}(y)`
` <= |s|^(-1) * 2 sqrt(15) * [2|s|^3/|det B|]^(1/4)`
` =2^(5/4) sqrt(15) (|s det B|)^(-1/4)`.

Again the estimate is uniform in the outside variables, so averaging proves (5.5). Absolute continuity and (5.6) follow. QED.

## 6. Exact closure of the all-zero-diagonal invertible physical triple

Suppose an invertible physical principal triple has zero diagonal:

`B=[[0,a,b],[a,0,c],[b,c,0]]`.

Then

`det B=2abc`.

Invertibility forces `a,b,c` all nonzero. Pick any edge as the bilinear pivot; for example `H=[[0,a],[a,0]]`. Theorem 5.1(b) gives

`||p_Q||_infinity <= 2^(5/4) sqrt(15) (|a det B|)^(-1/4)`.             (6.1)

Choosing the largest edge `e=max(|a|,|b|,|c|)` gives

`||p_Q||_infinity <= 2^(5/4) sqrt(15) (e |det B|)^(-1/4)`.             (6.2)

This closes exactly the all-zero-diagonal invertible-triple branch left open in Section 7 of the source B16 report. Together with B16 Theorem 5.1, **every invertible physical `3x3` principal block now has a conditional analytic payment**: a nonzero scalar diagonal uses the B16 scalar-Schur theorem, while an all-zero diagonal uses the present bilinear-pair theorem. The remaining global obstruction is no longer the local sign/pivot analysis; it is the dimension-free extraction/aggregation of such payments from the bare three-large-eigenvalue hypothesis.

As a clean control, if this zero-diagonal `3x3` block itself has all three eigenvalues of modulus at least one, then

`|det B|>=1`,

and

`2(a^2+b^2+c^2)=tr(B^2)=sum_j lambda_j^2>=3`.

Hence `e>=1/sqrt(2)`, and (6.2) yields the universal numerical bound

`||p_Q||_infinity <= 2^(11/8) sqrt(15) < 10.046`.                      (6.3)

This is a genuine target-normalized local branch for arbitrary independent cap-one laws, not a Gaussian or compact-support calculation.

## 7. What is and is not solved

**Solved here.** An indefinite physical `2x2` pivot plus one nondegenerate Schur coordinate gives a direct `O(|L|)` bound, with arbitrary outside quadratic terms and couplings. In particular, the previously unpaid all-zero-diagonal invertible physical triple is completely controlled. The proof works in original independent coordinates and does not take a square root of a small-ball estimate.

**Not solved.** The full conjecture still requires turning the spectral assumption “at least three eigenvalues have modulus at least one” into a dimension-free aggregate of local payments. Existing corrections rule out forcing one uniformly good physical triple/minor. The next structural implication should therefore be an aggregate/multiscale selection theorem rather than another single-minor lemma. A plausible receiver is a determinant-weighted mixture in which (5.4)/(5.5) are paid only after aggregating compatible physical triples.

**Continuity.** This proof establishes absolute continuity and an essentially bounded density in its scope. It does not establish a continuous representative for arbitrary merely measurable input densities; continuity remains a separate open request.

## 8. Partner and provenance status

The required named partner is `account04/B09`. No completed current-QFORM artifact for that slot was visible in either canonical location at the start of this run, so there was no partner theorem available to apply. This is recorded as an unavailable dependency, not silently replaced by another account04 slot. The completed account03/B16 weak-`L^2` ridge theorem was applied concretely in equations (5.7)--(5.5).

No scheduler state, notification setting, external workflow, email, Drive, paid API/model, credentials, repository visibility, or cross-account authentication was modified. Repository transport was used, but no authenticated native brain receiver/retrieval occurred; status remains `WITHOUT_VERIFIED_BRAIN`.
