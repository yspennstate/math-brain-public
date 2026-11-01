# fleet03/B09 — full bilinear-block absorption by mixed-Hessian Plancherel

**Run:** `20260922T130227Z-fleet03-B09-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Bilinear block mechanism`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full conjecture remains **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and corrections enforced

The active target is the full universal statement: for every dimension, every independent real coordinate law with one-dimensional densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a dimension- and law-independent `L^infinity` bound for the density of `Q=X^T A X`, or give a genuine counterexample.

This report keeps the original coordinate independence and all signs. It does not rotate the random vector into an eigenbasis, use the refuted law-uniform one-dimensional Fresnel estimate, or take a spectral-fiber supremum. The pointwise estimate below is a different, valid estimate forced by an invertible **mixed coordinate Hessian** and proved by an `L^2` Fourier-operator identity.

The named partner `fleet04/B09` still had no completed current-programme handoff at the fresh source read, so no partner result is fabricated or awaited. A completed compatible same-role result was substantively consumed instead: `fleet02/B09`, run `20260922T115241Z-fleet02-B09-QFORM-r1`, canonical commit `fa592b592c61bd1597aa8cf3270c3c9f58f410bf`. That result proves the exact `m/(m-1)|det B|^{-1/m}` density bound when one pivot-side principal block vanishes, and supplies an explicit logarithmic counterexample showing that an invertible `2x2` cross block alone does **not** control arbitrary within-block curvature. The new theorem below removes the vanishing-principal-block condition once the mixed block has dimension at least three.

## 2. Main theorem — arbitrary within-block absorption

### Theorem (`QFORM-FULL-BLOCK-BILINEAR-ABSORPTION-v1`)

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`, and let `A` be any real symmetric matrix. Suppose there are disjoint coordinate sets `I,J` with

- `|I|=|J|=m>=3`, and
- the square cross block `B=A[I,J]` is invertible.

No condition is imposed on `A[I,I]`, `A[J,J]`, the remaining rows and columns, or the signs of `A`.

Then `Q=X^T A X` has a bounded continuous density, vanishing at infinity, and

`||p_Q||_infinity <= [m/(m-2)] |det B|^{-1/m}.`                 (2.1)

In particular, for a disjoint `3x3` mixed block,

`||p_Q||_infinity <= 3 |det A[I,J]|^{-1/3}.`                    (2.2)

This is a direct `O(interval length)` theorem. There is no square-root/fourth-root decoupling loss.

### Proof

Condition on every coordinate outside `I union J`. Write `u=X_I`, `v=X_J`. Under this conditioning the coordinates of `u` and `v` are still mutually independent and retain their original one-dimensional densities. The conditional quadratic polynomial has the form

`q(u,v)=u^T C u + 2u^T Bv + v^T Dv + a^T u + b^T v + c`,        (2.3)

where `C,D,a,b,c` may depend on the conditioned outside coordinates. Crucially, the mixed block `B` does not change.

Fix `t!=0` and define

`F_t(u)= [prod_{i in I} f_i(u_i)] exp(i t[u^T C u+a^T u])`,

`G_t(v)= [prod_{j in J} f_j(v_j)] exp(i t[v^T D v+b^T v])`.

The arbitrary same-side quadratic and linear terms are now merely unit-modulus factors. Because `0<=f_i<=1` and each `f_i` integrates to one,

`||F_t||_2^2 = prod_{i in I} int f_i^2 <=1`,
`||G_t||_2^2 = prod_{j in J} int f_j^2 <=1`.                    (2.4)

The conditional characteristic function is

`psi(t)=e^{itc} int F_t(u) [int exp(i 2t u^T Bv) G_t(v) dv] du`. (2.5)

Use the Fourier convention

`Ghat(xi)=int exp(-i xi^T v) G(v) dv`.

The inner bracket in (2.5) is `Ghat_t(-2t B^T u)`. Cauchy-Schwarz followed by Plancherel and the invertible change of variables `xi=-2tB^T u` gives

`|psi(t)|
 <= ||F_t||_2 (int |Ghat_t(-2tB^Tu)|^2 du)^{1/2}`

`= ||F_t||_2 [(2pi)^m / ((2|t|)^m |det B|)]^{1/2} ||G_t||_2`

`<= pi^{m/2} |t|^{-m/2} |det B|^{-1/2}.`                       (2.6)

Of course `|psi(t)|<=1`, so uniformly in all conditioned outside values,

`|psi(t)| <= min(1, a |t|^{-m/2}),`
`a=pi^{m/2}|det B|^{-1/2}.`                                    (2.7)

Averaging over the outside coordinates preserves the same upper bound for the unconditional characteristic function `phi_Q(t)`.

For `m>2` the majorant is integrable. Set

`t0=a^{2/m}=pi |det B|^{-1/m}`.                                 (2.8)

Then on the positive half-line,

`int_0^infinity min(1,a t^{-m/2}) dt`
`= t0 + a int_{t0}^infinity t^{-m/2} dt`
`= t0 + [2/(m-2)] t0`
`= [m/(m-2)] t0`.                                                (2.9)

Therefore

`int_R |phi_Q(t)| dt <= [2m/(m-2)] pi |det B|^{-1/m}.`           (2.10)

The standard `L^1` Fourier inversion theorem for characteristic functions now gives a bounded continuous density tending to zero at infinity, and

`||p_Q||_infinity
 <= (1/(2pi)) int_R |phi_Q(t)| dt
 <= [m/(m-2)] |det B|^{-1/m}.`

This proves (2.1). `QED`

## 3. Why this does not resurrect the refuted pointwise-decay claim

The live correction says that for arbitrary one-dimensional `f<=1` there is no law-uniform power decay of `int exp(itx^2)f(x)dx`: fragmented supports can be phase-aligned. The present proof never uses such a statement.

Its cancellation comes from the nondegenerate **mixed** phase `2u^T Bv`. The map `v -> 2tB^Tu` turns the inner integral into a genuine Fourier transform, and Plancherel controls its `L^2` norm regardless of the same-side phases. In particular, the argument is immune to phase-aligned supports in either block because multiplying by those phases does not change the `L^2` norms in (2.4).

The threshold `m>=3` is also intrinsic to this exact Fourier-inversion mechanism: `m=2` gives only `|t|^{-1}`, whose integral diverges logarithmically. This matches the completed `fleet02/B09` counterexample: a nonsingular `2x2` cross block with curvature on both sides can still have a logarithmically unbounded output density. Thus the peer result is used here as the sharp low-dimensional endpoint/control, not merely cited.

Combining the two results gives the following source-valid block dictionary:

- arbitrary principal blocks + invertible square cross block of size `m>=3`:
  `||p_Q||_infinity <= [m/(m-2)] |det B|^{-1/m}` (this report);
- a one-sided linear pivot packet of size `m>=2`:
  `||p_Q||_infinity <= [m/(m-1)] |det B|^{-1/m}` (`fleet02/B09`);
- an arbitrary `2x2` cross block with both-side curvature: no universal conclusion from that datum alone (`fleet02/B09` logarithmic control example).

This closes a substantial part of the previous fleet03/B09 unpaid implication `QFORM-BILINEAR-BLOCK-ABSORPTION-v1`: **all** within-block quadratic curvature can be absorbed once three independent mixed coordinate directions are present.

## 4. Exact interval consequence

For every interval `L`, (2.1) immediately yields

`P{X^TAX in L} <= [m/(m-2)] |det A[I,J]|^{-1/m} |L|`.            (4.1)

This is the linear small-ball scale required by the owner target. No resampling exponent is lost.

The statement is stable under arbitrary outside couplings because the proof conditions on all outside coordinates and its constant is independent of their realized values.

## 5. What remains unpaid for the full three-eigenvalue theorem

The spectral hypothesis alone does not yet provide a dimension-free lower bound for one fixed original-coordinate cross determinant. In diffuse examples, exterior/minor mass can be spread over many tiny packets; diagonal matrices have every disjoint cross block equal to zero and are instead handled by the already-proved diagonal theorem. Thus selecting a largest `3x3` cross minor and paying its reciprocal determinant is not a valid universal bridge.

The first remaining B09 implication is now narrower:

> **`QFORM-MIXED-HESSIAN-AGGREGATION-v1` (OPEN).** Starting from the three-large-eigenvalue hypothesis in original coordinates, aggregate mixed-coordinate curvature before paying the reciprocal determinant cost, or prove a product-preserving dichotomy that sends every matrix either to (i) a quantitatively usable mixed packet covered by Theorem 2, or (ii) an already source-valid diagonal/diffuse/localized smoother.

A fixed-minor selection argument is explicitly insufficient. The next useful mechanism should average/aggregate the determinant mass at the oscillatory-operator level, not choose a tiny minor and invert it.

## 6. Status

**New proved supporting theorem:** `QFORM-FULL-BLOCK-BILINEAR-ABSORPTION-v1`, equations (2.1)-(2.10), including arbitrary signs, arbitrary within-block quadratic terms, arbitrary outside couplings, continuous density, and a sharp-for-this-integrability-threshold distinction between mixed dimension 2 and 3.

**Applied compatible result:** `fleet02/B09` `QFORM-MULTIPIVOT-BILINEAR-SMALLBALL-v1` plus its exact `2x2` curvature counterexample; this supplies the low-dimensional endpoint and rules out an invalid extension of the new theorem to `m=2`.

**Full universal conjecture:** OPEN. No target-level counterexample is produced here.

**Next step:** prove or refute `QFORM-MIXED-HESSIAN-AGGREGATION-v1` without rotating the input law, taking a fiber supremum, or paying a single diffuse coordinate minor.
