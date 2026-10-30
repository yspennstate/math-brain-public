# fleet02/B08 — diffuse Hadamard global-ridge payment

**Run:** `B08-20260922T173452Z-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM`; full QFORM remains OPEN.  
**Result name:** `QFORM-DIFFUSE-HADAMARD-GLOBAL-RIDGE-v1`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and first unpaid implication

The target is the full uniform-cube quadratic-form density conjecture: for independent real coordinates with arbitrary probability densities bounded by one and real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite density bound for `X^T A X`, or give a genuine counterexample.

The preceding B08 run refuted extraction of an approximate physical block decomposition as an exhaustive diffuse mechanism. Its remaining question was whether delocalized large eigenvectors can instead force either a local original-coordinate smoothing object or a global ridge/cross-bank payment. The current proof-first owner continuation sharpens this to an exhaustive product-preserving ridge-or-grouped-coordinate reduction.

This run changes mechanism. It gives an exact global ridge-cut theorem, an explicit full-spectrum Hadamard stress family with three genuinely delocalized large eigenvectors but no fixed-size nondegenerate principal block, and a literal application of the named partner fleet03/B08 theorem below the direct ridge `L^infinity` endpoint. The full dichotomy is still unpaid.

## 2. Source theorems actually used

### 2.1 Direct one-scale ridge theorem

Source: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B`, scale `gamma>0`, define

`K = B B^T (gamma^2 I + B B^T)^(-1)`,
`theta=tr K`,
`D=det(I+B B^T/gamma^2)`.

If for some `q in [1,2]`,

`max_i K_ii <= q/2`, `theta>2q`,

then, with arbitrary self blocks, outside coordinates, and outside couplings retained, the full quadratic form has a continuous `C_0` density and

`||p||_infinity <= e/(sqrt(2q) gamma) * theta/(theta-2q) * D^(-1/(2theta))`.

The proof preserves the original-coordinate product law; no spectral-coordinate independence, moment, or support assumption is used.

### 2.2 Named partner theorem actually applied

Named partner source: fleet03/B08 `QFORM-PIVOT-PLUS-RIDGE-LP-v1`, canonical mathematics
`yspennstate/math-open-problems@f0a31a05a227ca671ffb22f6d7ed62954ce48c73`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T162359Z-fleet03-B08-qform-diffuse-r13/REPORT.md`.

After an ORIGINAL physical pivot `a != 0`, let the Schur residual admit a cross block with the same ridge quantities. Put

`beta=theta/(2q)`,
`t0=pi e sqrt(2/q)/(2 gamma) D^(-1/(2theta))`.

For `s in (1,2)` satisfying `theta s>2q`, the partner theorem proves essential boundedness with

`||p_Q||_infinity <= (2/sqrt(pi)) |a|^(-1/2) (1-s/2)^(-1/2) C_s^(s/2)
                       [t0 beta s/(beta s-1)]^(1/2)`,

where `C_s<=1` is the sharp Hausdorff--Young constant. Thus one genuine original-coordinate square lowers the ridge threshold from `theta>2q` to `theta>q`. Continuity is not claimed by this hybrid theorem.

## 3. Exact scalar-orthogonal cross-block theorem

### Theorem 3.1 — `QFORM-SCALAR-ORTHOGONAL-CROSSBLOCK-v1`

Let a quadratic form on independent cap-one coordinates have an original-coordinate cut `I|J` whose cross block is square `m x m` and obeys

`B B^T = sigma^2 I_m`

for some `sigma>0`. All self blocks, all other coordinates, and all other couplings are arbitrary. If `m>4`, then `X^T A X` has a continuous density vanishing at infinity and

`boxed(||p_Q||_infinity <= [e sqrt(2)/(4 sigma)] * m/(m-4)).`       (3.1)

#### Proof

Apply the source ridge theorem with `q=1` and `gamma=sigma`. Then exactly

`K = (1/2) I_m`,
`theta=m/2`,
`D=2^m`.

Hence `max diag K=1/2=q/2`, and `theta>2` iff `m>4`. Also

`D^(-1/(2theta))=(2^m)^(-1/m)=1/2`.

Substitution in the source theorem gives

`||p_Q||_infinity
 <= e/(sqrt(2) sigma) * (m/2)/(m/2-2) * 1/2
 = [e sqrt(2)/(4 sigma)] * m/(m-4)`.

All conditioning and Fourier estimates in the source theorem occur in the original coordinates, so arbitrary self blocks and outside couplings are retained. QED.

The equivalent characteristic-function calculation is exact: `beta=m/4` and `t0=pi e sqrt(2)/(4sigma)`, so

`(2pi)^(-1) int |phi(t)|dt <= (t0/pi) beta/(beta-1)`,

which is exactly (3.1).

## 4. A delocalized full-spectrum family paid globally, not locally

Let

`H = 2^(-1/2) [[1,1],[1,-1]]`,
`A_k = H^(tensor k)`,
`n=2^k`, `k>=4`.

Then `A_k` is real symmetric orthogonal. Therefore **every** eigenvalue has modulus one, so the target spectral hypothesis holds with maximal slack.

Partition coordinates according to the first tensor bit. With `m=n/2`,

`A_k = 2^(-1/2) [[A_(k-1), A_(k-1)], [A_(k-1), -A_(k-1)]].`

Thus the physical cross block is

`B=2^(-1/2) A_(k-1)`,

and because `A_(k-1)` is orthogonal,

`B B^T=(1/2)I_m`.

Theorem 3.1 with `sigma=1/sqrt(2)` gives the source-valid uniform bound

`boxed(||p_{X^T A_k X}||_infinity <= (e/2) m/(m-4)
                                      = e n/[2(n-8)] <= e)`          (4.1)

for every `n>=16`, every independent input law with densities at most one, and with no moment/support/regularity assumptions. The output density is continuous and `C_0`. The bound tends to `e/2` along the family.

### 4.1 Three explicit delocalized large eigenvectors

Let

`v_+=(cos(pi/8), sin(pi/8))`,
`v_-=(sin(pi/8), -cos(pi/8))`.

These are orthonormal eigenvectors of `H` with eigenvalues `+1,-1`. For `k>=3`, the following tensor vectors are orthonormal `+1` eigenvectors of `A_k`:

`u1=v_+ tensor ... tensor v_+`,
`u2=v_- tensor v_- tensor v_+ tensor ... tensor v_+`,
`u3=v_- tensor v_+ tensor v_- tensor v_+ tensor ... tensor v_+`.

Put

`a=cos^2(pi/8)=(2+sqrt(2))/4`,
`b0=7/16+5sqrt(2)/32`.

A direct maximization over the first three coordinate bits gives the **exact** maximum row leverage of this selected three-frame:

`delta_k = a^(k-3) b0`.                                           (4.2)

Indeed all tensor positions after the first three are common `v_+` factors, whose squared coordinate is maximized by `a`; among the eight patterns on the first three bits the maximum sum of the three squared tensor coefficients is exactly `b0`.

Since

`a^k=n^(-kappa)`, `kappa=-log_2 a=0.228446696836388...`,

we have `delta_k ->0`. Thus the family contains a genuinely delocalized three-large-eigenvector frame while the full matrix remains full rank and maximally nonseparable.

### 4.2 No bounded-size nondegenerate principal block

Every entry of `A_k` has modulus `n^(-1/2)`. Hence every `r x r` physical principal block `P` satisfies

`||P||op <= ||P||F <= r/sqrt(n)`.                                 (4.3)

For every fixed `r`, its entire physical curvature scale therefore tends to zero as `n->infinity`; in particular `|A_ii|=n^(-1/2)`. Any reduction requiring a fixed bounded-size principal block with a dimension-free nonzero spectral scale is therefore false even inside a selected-eigenvector-delocalized target family.

This is **not** a counterexample to QFORM. Equation (4.1) shows that the same family is uniformly controlled by a growing global original-coordinate ridge cut. The correction is structural: diffuse selected eigenvectors may demand aggregate global payment rather than fixed local principal payment.

## 5. Literal named-partner application below the direct ridge endpoint

Take the exact real Householder matrix

`O = I_3 - (2/3) 1 1^T`,

so `O^T O=I_3`. Let

`S = [[0,O],[O^T,0]]`

on six original coordinates and let

`A_tilde = diag(1,S)`

on seven coordinates. Every eigenvalue of `A_tilde` has modulus one. Use the first original coordinate as the physical pivot: `a=1`, `b=0`, so the Schur residual is exactly `S`. Across its natural `3|3` cut, `B=O`.

Choose `q=1`, `gamma=1`. Then exactly

`K=(1/2)I_3`, `theta=3/2`, `D=8`.

The direct ridge density theorem does **not** apply because `theta=3/2 <=2q`.

Now apply the named partner theorem with `s=3/2`. We have

`beta=theta/(2q)=3/4`,
`beta s=9/8>1`,
`beta s/(beta s-1)=9`,
`t0=pi e sqrt(2)/4`.

Using `C_(3/2)<=1`, the partner bound becomes

`||p||_infinity
 <= (4/sqrt(pi)) sqrt(9 pi e sqrt(2)/4)
 = boxed(6 sqrt(e sqrt(2)))
 = 11.7640263946... .`                                           (5.1)

Thus the named partner result is applied to a genuine target matrix at a parameter point strictly below the direct ridge `L^infinity` threshold. This establishes essential boundedness for every admissible product input on this example. No post-rotation independence is used.

## 6. What is refuted, what is proved, and what remains

### Proved

1. The exact scalar-orthogonal cross-block theorem (3.1), retaining arbitrary self blocks and outside couplings.
2. The Sylvester-Hadamard family (4.1): a full-spectrum target family with an explicit three-frame whose leverage tends to zero, uniformly controlled by a global physical ridge cut with density bound at most `e` for `n>=16`.
3. The named partner theorem closes the explicit seven-dimensional target matrix (5.1) even though the direct ridge endpoint fails.

### Refuted intermediate mechanism

`QFORM-DIFFUSE-FIXED-LOCAL-PRINCIPAL-ONLY-FALSE-v1`: delocalization of three large eigenvectors does **not** force a uniformly nondegenerate principal block of any fixed bounded size. The Hadamard family has `||A[J,J]||op<=|J|/sqrt(n)` for every fixed-size physical set `J`, while its global ridge cut is uniformly excellent.

This refutes only that intermediate reduction. It does not refute localized conditioning in combination with global/grouped payment and it does not refute QFORM.

### First unpaid implication

`QFORM-DIFFUSE-MSS-LOCAL-OR-GLOBAL-RIDGE-v1`:

Given only a delocalized selected three-large-eigenvector frame and an arbitrary complementary spectrum, prove an exhaustive original-coordinate alternative, after conditioning a bounded amount of selected-frame mass:

- either a localized physical smoothing certificate (scalar pivot, definite principal pair, or grouped-coordinate bank) has a dimension-free usable scale;
- or some physical cut has ridge parameters with `max diag K<=q/2` and `theta>2q`; with one usable physical pivot it suffices, by fleet03/B08, to reach the weaker `theta>q` threshold.

The implication must retain arbitrary extra eigenvalues and survive the existing singleton-plus-two-banks and small-principal-minor corrections. The Hadamard family shows why the global-ridge alternative is genuinely necessary; the preceding three-bank construction shows why a local/grouped alternative is also genuinely necessary. No proof of this exhaustive dichotomy is supplied here.

## 7. Corrections and provenance

Consumed corrections include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and the preceding B08 `QFORM-DIFFUSE-APPROX-BLOCK-EXTRACTION-ALONE-FALSE-v1`. None of the refuted premises is used.

The source ridge theorem is a completed supporting proof with its own review status; the named partner theorem is used at its exact stated scope. Operational receipts are not mathematical proof. Full QFORM remains OPEN and no novelty claim beyond this private programme is made.
