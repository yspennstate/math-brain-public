# account02/B10 — heavy-isotropic leakage: an independent-leakage closure and a sharp conditional-cap falsifier

**Run:** `20260922T130225Z-b10-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Rank-three coupled case`  
**Classification:** `ESSENTIAL_STEP_APPLIED` plus local `CANDIDATE_REFUTED`; full target remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target, source state, and first unpaid implication

The target is the rank-exactly-three part of the owner conjecture: for independent real physical coordinates with densities at most one and a real symmetric rank-three matrix whose three nonzero eigenvalues have modulus at least one, prove a universal density bound for `X^T A X`, with arbitrary orientation and without declaring spectral projections independent.

Fresh controls were read at `math-research-brain@4bf9804d245be3c4d815483093f6d49d7df5408d` and refreshed before publication at `ecc0bbc3635222f0ba0f1c0ee593059e07bf7809`. The live corrections include the failure of law-uniform pointwise oscillatory decay, loss from naive fiber suprema, non-independence after rotation, the cross-minor-only falsifier, the generic X-ray falsifier, the conditional sum/difference cap failure, and the new `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` event. None of those invalid mechanisms is used below.

The named partner result actually consumed is account03/B10, `math-open-problems@c1af196adade03e07456c8f6e783f952b0fa0e8d`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/account03-B10-20260922T121625Z-qform-r11/REPORT.md`. Its Theorem 2.1 proves the dependence-tolerant hyperbolic-square estimate when one scalar variable remains genuinely independent of the possibly dependent projected pair. The two-dimensional projection cap used there is source-pinned in account03/B09 at `math-open-problems@41fc39eccdd44a0dcae6619676bf41f5ea21bb3e`.

The first unpaid implication from the partner is the heavy isotropic leakage state

`Q = 2B( sqrt(c) X_i + T )Y + rY^2 + 2sYZ + tau Z^2`,

with `c in (1/2,1)`, `B^2|tau|>=1`, where `T` is a residual linear form dependent on `(Y,Z)`. A tempting next step is to replace the missing independence by the facts that `(Y,Z)` has bounded joint density and `sqrt(c)X_i+T` has a bounded conditional density given `(Y,Z)`. This run tests that implication first and shows it is false in the strongest possible way.

## 2. Partner theorem with a nonunit independent density cap

The partner theorem scales immediately as follows.

### Lemma 2.1 — scaled dependent-pair hyperbolic-square theorem

Let `W` be independent of `(Y,Z)`, with `||p_W||_infinity<=K`. Let `(Y,Z)` have joint density at most `H`. For nonzero `a,b` and arbitrary measurable `F,theta`, set

`T0 = 2aWY + F(Y) + b(Z+theta(Y))^2`.

Then

`||p_T0||_infinity <= 3*2^(2/3) H^(2/3) K^(2/3) |a|^(-2/3)|b|^(-1/3)`.      (2.1)

**Proof.** Put `W'=KW`. Then `W'` has density at most one, remains independent of `(Y,Z)`, and `2aWY=2(a/K)W'Y`. Apply account03/B10 Theorem 2.1 with coefficient `a/K`. QED.

This is an actual use of the named partner theorem, not a restatement of the assignment.

## 3. Heavy isotropic coordinates and an independent-leakage closure

Use the partner's exact heavy-row normalization. Write

`A=U Lambda U^T`, `U^T U=I_3`, `|lambda_j(Lambda)|>=1`,

choose a physical row `u_i=sqrt(c)e` with `c>1/2`, and suppose

`alpha=e^T Lambda e=0`.

Choose an orthonormal spectral basis `(e,f,g)` in which

`Lambda = [[0,B,0],[B,r,s],[0,s,tau]]`,

so

`B^2 |tau| = |det Lambda| >=1`.                                          (3.1)

For every residual physical row write

`u_j = s_j e + y_j f + z_j g`.

The Parseval identities are

`sum s_j^2=1-c`, `sum y_j^2=sum z_j^2=1`,

`sum s_j y_j=sum s_j z_j=sum y_j z_j=0`.                                (3.2)

Define

`T=sum s_jX_j`, `Y=sum y_jX_j`, `Z=sum z_jX_j`, `W=sqrt(c)X_i+T`.

Then exactly

`Q=2BWY+rY^2+2sYZ+tau Z^2`

` =2BWY +(r-s^2/tau)Y^2 + tau(Z+(s/tau)Y)^2`.                           (3.3)

### Theorem 3.1 — `QFORM-HEAVY-ISOTROPIC-INDEPENDENT-LEAKAGE-v1`

In the state above, assume additionally that `T` is independent of `(Y,Z)`. A concrete sufficient original-coordinate condition is

`supp(s) cap (supp(y) union supp(z)) = empty`.                           (3.4)

Then

`||p_Q||_infinity <= 3*2^(4/3)c^(-1/3) < 3*2^(5/3) < 9.525`.             (3.5)

**Proof.** Since `X_i` is independent of all residual coordinates and `T` is independent of `(Y,Z)`, `W=sqrt(c)X_i+T` is independent of `(Y,Z)`. The scaled variable `sqrt(c)X_i` has density at most `c^(-1/2)`, and convolution with independent `T` cannot increase the `L^infinity` norm, hence

`||p_W||_infinity <= c^(-1/2)`.                                         (3.6)

The coefficient vectors `(y_j)` and `(z_j)` are orthonormal by (3.2). The Livshyts--Paouris--Pivovarov two-dimensional product-marginal theorem, in the source-valid form used and proved into the account03/B09 report, gives

`||p_(Y,Z)||_infinity <=2`.                                              (3.7)

Apply Lemma 2.1 to (3.3) with `K=c^(-1/2)`, `H=2`, `a=B`, `b=tau`. Using (3.1),

`||p_Q||_infinity`

` <=3*2^(2/3) 2^(2/3)c^(-1/3)|B|^(-2/3)|tau|^(-1/3)`

` =3*2^(4/3)c^(-1/3)(B^2|tau|)^(-1/3)`

` <=3*2^(4/3)c^(-1/3)`.

Because `c>1/2`, this is strictly below `3*2^(5/3)=9.524406...`. QED.

This strictly extends the partner's `c=1` isotropic closure to every heavy `c>1/2` state in which the leakage is genuinely independent of the transverse projected pair. It is a supporting branch, not a closure of arbitrary orientation.

## 4. What arbitrary heavy leakage still gives for free

Even without independence between `T` and `(Y,Z)`, the heavy isotropic state has two strong distributional caps.

First, (3.7) remains true: `(Y,Z)` is a two-dimensional orthogonal projection of the residual product law.

Second, the conditional law of `W=sqrt(c)X_i+T` given `(Y,Z)` has density at most `c^(-1/2)`. Indeed, conditioned on `(Y,Z)`, the variable `T` has some regular conditional law `mu_{y,z}`, while `X_i` is independent of `(T,Y,Z)`. Hence

`p_{W|Y,Z}(w|y,z)`

` = int c^(-1/2) f_i((w-t)/sqrt(c)) d mu_{y,z}(t)`

` <= c^(-1/2)`.                                                         (4.1)

It is therefore natural to ask whether partner Theorem 2.1 remains true if genuine independence of `W` from `(Y,Z)` is replaced by the pair of conditions

`||p_(Y,Z)||_infinity <=H`,

`||p_{W|Y,Z}( . |y,z)||_infinity <=K` a.e.                              (4.2)

If this were true with a universal function of `H,K,a,b`, the heavy isotropic leakage branch would close immediately using `H=2`, `K=c^(-1/2)`.

The next section gives an exact counterexample.

## 5. Exact falsifier: conditional density caps do not replace independence

### Proposition 5.1 — `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`

For every `delta in (0,1)` there is a three-dimensional probability density `p(s,y,z)` such that

1. `||p||_infinity=1`;
2. the pair `(Y,Z)` has joint density bounded by one;
3. the conditional law of `S` given `(Y,Z)` has density bounded by one for every `(y,z)` in the support;
4. nevertheless `2SY+Z^2` has an unbounded density.

Thus no theorem depending only on a bounded `(Y,Z)` density and a bounded conditional `S|(Y,Z)` density can replace the genuine independence premise in the account03/B10 hyperbolic-square theorem.

### Construction and exact calculation

Let

`Y ~ Uniform(0,delta)`,

`Z ~ Uniform(0,1/delta)`,

`U ~ Uniform(0,1)`

be independent, and set

`S = -Z^2/(2Y) + U`.                                                     (5.1)

Because the rectangle `(0,delta)x(0,1/delta)` has area one, `(Y,Z)` has joint density exactly one there. The map `(u,y,z) -> (s,y,z)` in (5.1) has Jacobian one, so `(S,Y,Z)` has density one on

`E_delta = {0<y<delta, 0<z<1/delta, -z^2/(2y)<s<-z^2/(2y)+1}`,           (5.2)

which has volume one. In particular the full joint density cap is also one. For each fixed `(y,z)`, the conditional `S`-section is a unit interval, so `p_{S|Y,Z}<=1` exactly.

But the designed cancellation gives

`2SY+Z^2 = 2YU`.                                                        (5.3)

The marginal density of `Y` is `1/delta` on `(0,delta)`. Therefore for `0<q<2delta`, the product transformation gives

`p_{2YU}(q)`

` = int_{q/2}^{delta} (1/delta) * 1 * (1/(2y)) dy`

` = (1/(2delta)) log(2delta/q)`,                                       (5.4)

which diverges as `q downarrow0`.

This is an exact probability-density counterexample, not a histogram or asymptotic guess. It is **not** a counterexample to the owner QFORM theorem, because the specially correlated `(S,Y,Z)` law in (5.2) has not been represented as an orthogonal projection of an original-coordinate product measure. Its role is narrower and decisive: it kills the conditional-cap shortcut that would otherwise seem to close the partner's heavy-isotropic leakage residual.

## 6. Consequence for the rank-three programme

The heavy isotropic residual is now split cleanly:

* if the leakage is genuinely independent of `(Y,Z)`, Theorem 3.1 closes it with constant `<9.525` by an actual application of the named account03/B10 theorem;
* in the arbitrary product-origin case, one still has the strong caps (3.7) and (4.1), but Proposition 5.1 proves that those caps alone are mathematically insufficient;
* therefore the next theorem must exploit an invariant that distinguishes **linear images of product measures with the Parseval identities (3.2)** from arbitrary three-dimensional densities satisfying the same low-dimensional caps.

A precise first unpaid implication is:

**`QFORM-ISOTROPIC-PRODUCT-PROVENANCE-TRACE-v1`.** In the heavy isotropic normal form (3.1)--(3.3), prove a uniform bound for

`2B( sqrt(c)X_i + sum s_jX_j )(sum y_jX_j) + rY^2+2sYZ+tau Z^2`

using the original independent coordinates and the exact orthogonality relations (3.2), without collapsing first to only `p_(Y,Z)` and `p_{W|Y,Z}`. Equivalently, one needs a product-origin curved-trace estimate that forbids the nonlinear cancellation geometry (5.1)--(5.2).

This residual is consistent with the live `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` correction: the hard target family can have no useful single Schur-cross pivot, so the new estimate must permit high-cardinality aggregation before paying local reciprocal constants.

## 7. Status and provenance

- `QFORM-HEAVY-ISOTROPIC-INDEPENDENT-LEAKAGE-v1`: **PROVED SUPPORTING THEOREM**.
- `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: **EXACT COUNTEREXAMPLE TO AN INTERMEDIATE MECHANISM**.
- arbitrary heavy isotropic leakage: **OPEN**.
- arbitrary rank-three orientation: **OPEN**.
- full owner target with additional spectrum: **OPEN**.

No finite census is used. No post-rotation independence is assumed. No moment, support, continuity, or log-concavity assumption is added. The logarithmic divergence in (5.4) is exact. No code or numerical experiment is needed for the mathematical claims in this report.
