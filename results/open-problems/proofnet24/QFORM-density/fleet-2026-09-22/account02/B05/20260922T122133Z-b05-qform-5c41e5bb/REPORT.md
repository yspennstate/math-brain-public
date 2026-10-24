# account02/B05 — binary gradient-box coarea and scalar-Schur closure

**Run:** `20260922T122133Z-b05-qform-5c41e5bb`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` for native learned-memory purposes; authenticated repository retrieval was used, but repository transport alone is not evidence of native brain ingestion.

## 1. Exact target, assignment, and corrections consumed

The target remains the full arbitrary-product-law statement: for every dimension, every independent real inputs with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moment, support, sign, diagonal-basis, or post-rotation-independence assumption is introduced here.

This B05 assignment is the direct coarea/small-interval route. The live corrections consumed before the proof include:

- law-uniform pointwise one-dimensional Fresnel decay is false;
- unrestricted spectral-fiber suprema can lose a dimension-dependent factor;
- rotating to the eigenbasis does not preserve independence;
- a cross minor alone is not a complete target certificate;
- the generic two-sheet X-ray cap alone does not bound the quadratic trace.

Accordingly, the proof below works in original independent coordinates and retains both the product density cap and one-dimensional section masses. It never replaces the curved fiber by an unrestricted fiber supremum.

## 2. Peer results actually applied

### Named partner `account03/B05`

Canonical report: `yspennstate/math-open-problems@c828d2ee2f8acef5eb96892bc8a9a25594db0f51`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T113800Z-account03-B05-qform-r11/REPORT.md`.

For a rank-`r>=3` form `A=R^T Lambda R` whose active spectral projector `P=R^T R` has `max_j ||P e_j||_2<=1/2`, the partner combines the Rudelson--Vershynin Fourier--Brascamp--Lieb estimate with the exact Fresnel transform to obtain

`||p_{X^TAX}||_infinity <= [B^2/(4 pi^2 D)] r/(r-2)`,  
`D=(prod |lambda_k|)^(1/r)`.

In particular, when `D>=1`, this is a universal delocalized bound. The remaining partner debt is spectral truncation when only three eigenvalues are large and tiny complementary eigenvalues are present. This run supplies the complementary original-coordinate localized/coarea mechanism.

### `account03/B01`

Canonical report: `yspennstate/math-open-problems@c7a1ce265139092705e86c5a577523798291b964`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T113140Z-account03-B01-qform-r1/REPORT.md`.

It proves a common `L^3` envelope for products and, in particular, the target-level block theorem for

`[[0,b,d],[b,0,e],[d,e,c]]`, `b!=0`, `det!=0`,

with arbitrary outside couplings:

`||p_Q||_infinity < 7.90 |det B|^(-1/3)`.

This will close the all-zero-diagonal local triple left outside the scalar-pivot theorem below.

## 3. First unpaid implication attacked

The preceding B05 run reduced a scalar-pivot coarea argument to the generic binary Schur residual

`R(Y,Z)=beta Y^2+2 gamma YZ+delta Z^2+linear+constant`.

The exact-product case `beta=delta=0` was closed there. The first unpaid implication was a dimension-free bound on

`sup_t E |t-R|^(-1/2)`

under arbitrary independent densities bounded by one. This run closes that implication whenever the binary quadratic matrix is nonsingular, with no sign restriction.

## 4. Binary gradient-box small-ball lemma

### Lemma 4.1 — `QFORM-BINARY-GRADIENT-BOX-v1`

Let `Y,Z` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let

`R(y,z)=beta y^2+2 gamma yz+delta z^2+l1 y+l2 z+c`,

and put

`Delta=beta delta-gamma^2`.

Assume `Delta!=0`. Then, for every `t in R`, `r>0`, and `s>0`,

`P(|R-t|<r) <= 8 r/s + s^2/|Delta|`.                    (4.1)

Consequently, with

`C0=3*2^(4/3)`,

`P(|R-t|<r) <= min(1, C0 r^(2/3)|Delta|^(-1/3)).`       (4.2)

#### Proof

The gradient map is affine:

`(d_y R,d_z R)=2 [[beta,gamma],[gamma,delta]] (y,z)^T +(l1,l2)`.

Its Jacobian determinant has absolute value `4|Delta|`. Define the critical gradient box

`G_s={|d_y R|<s, |d_z R|<s}`.

The image box has area `4s^2`, hence

`Leb(G_s)=s^2/|Delta|`.

Because the joint density is exactly the original-coordinate product `f(y)g(z)<=1`,

`P((Y,Z) in G_s)<=s^2/|Delta|`.                          (4.3)

Outside `G_s`, at least one partial derivative has magnitude at least `s`. Fix `z`. The map `y -> R(y,z)` is a polynomial of degree at most two. On each of its at most two monotonic branches, the inverse derivative is at most `1/s` on the set `|d_y R|>=s`; therefore the preimage of `(t-r,t+r)` on one branch has length at most `2r/s`, and the total `y`-length is at most `4r/s`. Since `f<=1`, integrating against the probability density `g(z)` gives

`P(|R-t|<r, |d_y R|>=s)<=4r/s`.                         (4.4)

The symmetric argument gives the same bound with `z`. Combining (4.3)--(4.4) proves (4.1).

Optimizing `8r/s+s^2/|Delta|` at `s=(4r|Delta|)^(1/3)` yields (4.2). QED.

### Why this is dimension-free

Two different pieces of the product structure are used and neither is replaceable by a spectral-fiber supremum:

1. the joint pointwise cap `f(y)g(z)<=1` controls the two-dimensional critical set;
2. the one-dimensional cap plus the unit mass of the other coordinate controls each transverse section.

This is precisely the averaging that the known cube-projection counterexample destroys if one takes an unrestricted fiber maximum first.

## 5. Half-Riesz closure of the generic binary Schur residual

### Theorem 5.1 — `QFORM-BINARY-HALF-RIESZ-v1`

Under the hypotheses of Lemma 4.1,

`sup_t E |t-R(Y,Z)|^(-1/2) <= K |Delta|^(-1/4)`,          (5.1)

where

`K=8*3^(3/4) < 18.237`.

#### Proof

For every nonnegative random variable of the form `|t-R|^(-1/2)`, layer cake gives

`E |t-R|^(-1/2)`
` = (1/2) integral_0^infinity r^(-3/2) P(|t-R|<r) dr`.    (5.2)

Use (4.2). The crossover where `C0 r^(2/3)|Delta|^(-1/3)=1` is

`r0=|Delta|^(1/2) C0^(-3/2)`.

Splitting (5.2) at `r0` gives

`(1/2) C0 |Delta|^(-1/3) integral_0^r0 r^(-5/6)dr`
` +(1/2) integral_r0^infinity r^(-3/2)dr`
` =3 C0^(3/4)|Delta|^(-1/4)+C0^(3/4)|Delta|^(-1/4)`
` =8*3^(3/4)|Delta|^(-1/4)`.

QED.

This does not claim that the binary residual itself has bounded density. Rank-two opposite-sign examples retain their logarithmic singularity; the theorem proves exactly the half-order smoothing quantity required by the third scalar square.

## 6. Scalar-Schur coarea theorem

### Theorem 6.1 — `QFORM-SCALAR-SCHUR-COAREA-v1`

Let `X_1,...,X_n` be independent with densities bounded by one, and let `Q=X^T A X` with `A` real symmetric. Suppose an original-coordinate principal triple `I={i,j,k}` has nonsingular coefficient block `B=A_I`, and for some pivot `i in I`

`a=B_ii !=0`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= K |a det B|^(-1/4)`,                (6.1)

with `K=8*3^(3/4)<18.237`. All couplings to coordinates outside `I` are arbitrary.

#### Proof

Condition on every outside coordinate. This converts outside couplings into affine terms in the selected three original coordinates and does not alter their independence or density caps.

Relabel the pivot variable as `X` and the other two as `Y,Z`. Completing the square only in the original coordinate `X` gives

`Q = a (X+m(Y,Z))^2 + R(Y,Z)`,                           (6.2)

where the quadratic coefficient matrix of `R` is the Schur complement

`C=B_{YZ,YZ}-B_{YZ,X} B_{X,YZ}/a`.

Thus

`det C = det B/a !=0`.                                   (6.3)

For each fixed `(Y,Z)`, the translated variable `X+m(Y,Z)` still has a conditional density bounded by one because `X` is independent of `(Y,Z)` before the translation. The pushforward through `a u^2` has density bounded by

`|a|^(-1/2) |v|^(-1/2)`

on the appropriate half-line. Therefore

`p_Q(t) <= |a|^(-1/2) E |t-R(Y,Z)|^(-1/2)`.              (6.4)

Apply Theorem 5.1 and (6.3):

`||p_Q||_infinity`
` <= K |a|^(-1/2) |det B/a|^(-1/4)`
` = K |a det B|^(-1/4)`.

The bound is uniform in the conditioned outside variables, so mixing restores the same bound in the full dimension. QED.

## 7. Complete local nonsingular-triple interface

The scalar-pivot theorem covers every nonsingular original-coordinate `3x3` principal block having at least one nonzero diagonal entry. If all three diagonal entries vanish, nonsingularity forces the three off-diagonal entries to be nonzero because

`det [[0,b,d],[b,0,e],[d,e,0]]=2bde`.

That remaining case is exactly inside the account03/B01 zero-diagonal-pair block theorem. Therefore:

> **Every fixed nonsingular original-coordinate principal triple admits a finite arbitrary-law density bound with arbitrary outside couplings.**

The quantitative certificate is either `|B_ii det B|` for a nonzero diagonal pivot, via (6.1), or `|det B|` in the all-zero-diagonal case via the B01 theorem.

This closes the previous B05 generic Schur-residual debt completely at the local three-coordinate level.

## 8. Source-valid obstruction to promoting the local theorem directly to the full spectral target

The matrix

`B0=[[0,1,1],[1,0,1],[1,1,0]]`

has eigenvalues `2,-1,-1`, determinant `2`, and every diagonal pivot is zero. Thus a claim that three large eigenvalues force a usable scalar diagonal pivot is false. B01's zero-diagonal theorem handles this exact example, showing the obstruction is to the pivot choice rather than to bounded density.

More importantly, the named partner's rank-three Walsh family shows why **one quantitative principal triple cannot be the entire full proof**. For its rank-three projector `A_n`, every coordinate leverage is `3/n`. Hence each diagonal entry is `3/n`; by Hadamard, every `3x3` principal determinant is at most `(3/n)^3`. Therefore every scalar local certificate satisfies

`|A_ii det A_I| <= (3/n)^4 = 81/n^4`.                    (8.1)

The bound (6.1) can consequently deteriorate linearly in `n`, even though the partner's global Fresnel--Brascamp--Lieb theorem gives a universal density bound on the same delocalized family. This is a source-valid mechanism counterexample to a proof that selects one principal triple and stops.

## 9. First unpaid implication after this run

`QFORM-LOCAL-DELLOCALIZED-AGGREGATION-v1`:

Combine the now-complete local nonsingular-triple interface with the named partner's delocalized spectral-subspace theorem in a dimension-free dichotomy that survives arbitrary tiny complementary eigenvalues. Equivalently, prove that failure of a uniformly strong original-coordinate local certificate forces enough selected large-eigenspace delocalization to run a **spectrally truncated** Wiener/Fresnel estimate, without paying the determinant of the tiny complementary spectrum; or construct a valid product-density counterexample to that weighted estimate.

The local curved-fiber factor is no longer missing: it is quantified by `|Delta|^(-1/4)` in (5.1). The remaining missing factor is global aggregation/extraction, not the generic binary Schur residual.

## 10. Integrity and computation

No numerical simulation or finite search is used as mathematical evidence. The constants are exact symbolic consequences of the optimization and layer-cake integrals above. The proof does not use the refuted pointwise oscillatory-decay claim, post-rotation independence, or a fiber supremum. The full conjecture remains open and no universal full-target constant is claimed.
