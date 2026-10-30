# fleet01/B03 — decoupled time integral via a mixed coordinate minor

**Run:** `B03-20260922T115130Z-qform-decoupled-time`  
**Assignment:** `Decoupled time integral`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_SUPPORTING_LEMMA / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Exact target and source pins

The live target is the full arbitrary-dimensional conjecture: independent real `X_i` with densities `0<=f_i<=1`, arbitrary real symmetric `A`, and at least three eigenvalues of `A` with absolute value at least one; prove a dimension- and law-independent `L^infinity` bound for the density of `Q=X^TAX`, or give a valid counterexample.

Control/source snapshot used at the start of the proof:

- same commit, `CLAIMS.json`, `MEMORY_PROTOCOL.md`, `ORDER.md`, `PATHWAYS.md` and `assignments/fleet01/B03.json`;
- fresh `CORRECTION_INBOX.json` was empty at the checked source snapshot.

The named partner result actually consumed and applied is:

- `yspennstate/math-open-problems@b4736d3226c5ffb46bda90b98c1a7b0ac28454b3:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T114427Z-b03-qform-a11/REPORT.md`, blob `363519157d63781d00966b0ff1dd1733d3681a49`.

That report proves two facts used below: (i) the sum/difference variables in the independent-copy identity are dependent and must retain their exact joint density, and (ii) scalar one-copy small-ball symmetrization cannot recover linear scaling. The present proof uses those corrections and replaces the failed scalar route by a block `L^2`/Plancherel decoupling that gives an integrable time tail whenever a `3 x 3` mixed coordinate minor is nonsingular.

A fresh later correction event from fleet02/B09 was also checked before publication:


It refutes a *two-by-two* cross-minor-only density claim. The theorem below starts exactly at block size three; the `m=2` estimate is only `|t|^{-1}` and is deliberately not promoted to a density bound, so the correction is respected.

## 1. Exact independent-copy identity with the dependence retained

Let `X'` be an independent copy of `X` and write

`U=X-X'`, `V=X+X'`.

Then, exactly,

`Q(X)-Q(X') = U^T A V`,

so

`|phi_Q(t)|^2 = E exp(i t U^T A V)`.

For each original coordinate,

`(U_i,V_i)=(X_i-X_i',X_i+X_i')`

has joint density

`h_i(u,v)=(1/2) f_i((v+u)/2) f_i((v-u)/2)`.

The pairs `(U_i,V_i)` are independent across `i`, but `U_i` and `V_i` are generally dependent within a pair. In particular, no step below replaces `h_i` by the product of its marginals. This is exactly the correction emphasized by the partner report.

The partner report also proves that if a scalar output `Z` has a nonzero `L^2` density, then

`P(|Z-Z'|<=eps)=2 eps ||p_Z||_2^2+o(eps)`.

Thus the elementary inequality `P(Z in I)^2 <= P(|Z-Z'|<=|I|)` can give at best square-root scaling from a linear small-ball bound for `Z-Z'`. The next theorem therefore extracts decay before taking such a square root.

## 2. Main theorem: a nonsingular mixed `m x m` coordinate block

### Theorem 2.1 — `QFORM-MIXED-MINOR-L2-v1`

Let `I,J` be disjoint coordinate sets of the same size `m>=3`. Put

`C=A[I,J]`.

Assume `C` is invertible and write `delta=|det C|`. Under the full input assumptions `0<=f_i<=1`, `int f_i=1`, the characteristic function of `Q=X^TAX` obeys

`|phi_Q(t)| <= min(1, pi^(m/2) delta^(-1/2) |t|^(-m/2)).`      (2.1)

Consequently `phi_Q in L^1(R)`, the law of `Q` has a bounded uniformly continuous density, and

`||p_Q||_infinity <= [m/(m-2)] delta^(-1/m).`                    (2.2)

In particular, for a disjoint nonsingular `3 x 3` mixed minor,

`boxed{ ||p_Q||_infinity <= 3 |det A[I,J]|^(-1/3). }`            (2.3)

No condition is imposed on the principal blocks `A[I,I]` or `A[J,J]`, on the signs of the spectrum, on the remaining coordinates, or on the remaining eigenvalues.

### Proof

Condition on every coordinate outside `I union J`. Independence leaves the selected coordinates with their original product densities. Write

`y=X_I in R^m`, `z=X_J in R^m`.

For the fixed outside configuration the quadratic polynomial has the form

`q(y,z)=y^T B y + 2 y^T C z + z^T D z + 2 alpha^T y + 2 beta^T z + c`,

where `B=A[I,I]`, `D=A[J,J]`, and `alpha,beta,c` depend only on the conditioned variables.

Let

`a(y)=prod_{i in I} f_i(y_i)`, `b(z)=prod_{j in J} f_j(z_j)`.

Because every `f_i<=1` and has mass one,

`||a||_2<=1`, `||b||_2<=1`.

For fixed `t!=0`, absorb all terms except the mixed block into unimodular amplitudes:

`A_t(y)=a(y) exp(i t[y^T B y+2 alpha^T y])`,

`B_t(z)=b(z) exp(i t[z^T D z+2 beta^T z])`.

Then the conditional characteristic function is, up to the harmless factor `exp(itc)`,

`Phi(t)=int int A_t(y) B_t(z) exp(i 2t y^T C z) dy dz`.

With Fourier convention

`hat B_t(xi)=int exp(-i xi^T z) B_t(z) dz`,

we have

`Phi(t)=int A_t(y) hat B_t(-2t C^T y) dy`.

Cauchy-Schwarz, the linear change of variables `xi=-2t C^T y`, and Plancherel give

`|Phi(t)|`
`<= ||A_t||_2 [int |hat B_t(-2t C^T y)|^2 dy]^(1/2)`
`= ||a||_2 |det(2t C)|^(-1/2) ||hat B_t||_2`
`= ||a||_2 |2t|^(-m/2) delta^(-1/2) (2pi)^(m/2) ||b||_2`
`<= pi^(m/2) delta^(-1/2) |t|^(-m/2).`

This bound is uniform in the conditioned outside coordinates, so averaging the conditional characteristic functions preserves it. Together with `|phi_Q(t)|<=1`, this proves (2.1).

Set

`K=pi^(m/2) delta^(-1/2)`, `t0=K^(2/m)=pi delta^(-1/m)`.

Then

`int_R |phi_Q(t)| dt`
`<=2[t0 + K int_(t0)^infinity t^(-m/2) dt]`
`=2 t0 [1+2/(m-2)]`
`=2 pi [m/(m-2)] delta^(-1/m).`

Fourier inversion therefore gives a bounded uniformly continuous density and

`||p_Q||_infinity <= (1/(2pi)) ||phi_Q||_1`
`<= [m/(m-2)] delta^(-1/m).`

This proves (2.2) and (2.3). `QED`.

## 3. Explicit integrated tail and linear small-ball consequence

The proof gives the genuine time-integrated estimate

`int_{|t|>=T} |phi_Q(t)| dt`
`<= [4 pi^(m/2)/(m-2)] delta^(-1/2) T^(1-m/2)`                 (3.1)

for every `T>0` in the range where the power bound is used. At `m=3` this is

`int_{|t|>=T} |phi_Q(t)| dt <= 4 pi^(3/2) delta^(-1/2) T^(-1/2).`

More importantly, (2.2) yields the desired *linear* interval small-ball scaling on this structural branch:

`P(Q in J0) <= [m/(m-2)] delta^(-1/m) |J0|`                   (3.2)

for every interval `J0`.

Thus the partner's scalar-difference obstruction is not merely restated: it is actively bypassed by keeping a genuinely multivariate mixed block until the Cauchy-Plancherel step has produced the full `m/2` time-decay exponent.

## 4. Why the threshold `m=3` is exact for this mechanism

For `m=2`, the same proof gives only

`|phi_Q(t)| <= pi delta^(-1/2) |t|^(-1)`,

whose absolute time integral diverges logarithmically. Therefore this argument makes **no** bounded-density claim from an arbitrary nonsingular `2 x 2` mixed block alone.

This is consistent with the fleet02/B09 correction event: for independent centered unit-interval inputs,

`Q=(X1+Y1)^2-(X2+Y2)^2`

has a nonsingular `2 x 2` mixed block but an unbounded logarithmic density at zero. The event does not challenge Theorem 2.1; it confirms that the integrability threshold in the present proof is the right one for this route.

When additional structure such as a vanishing pivot-side principal block is available, fleet02/B09 obtains a stronger pure-bilinear theorem. The present result is complementary: at block size at least three it removes any hypothesis on either principal block.

## 5. Relation to the partner's cubic square estimate

The partner fleet02/B03 proves an exact `L^3_t` estimate for one shifted square and an `L^1_t` estimate for three independent shifted squares. Theorem 2.1 is the mixed-coordinate analogue:

- partner mechanism: three independent *one-dimensional quadratic* smoothing directions, combined by Holder in time;
- present mechanism: three *bilinearly coupled coordinate pairs*, combined by one `m`-dimensional Plancherel step.

Both mechanisms turn on exactly at three directions and both survive arbitrary bounded input densities despite the refuted law-uniform pointwise one-dimensional Fresnel estimate.

## 6. What this does and does not close

This is a target-level implication, not a proof of the full conjecture. The spectral assumption "at least three eigenvalues with absolute value at least one" does **not** force one disjoint mixed `3 x 3` coordinate minor to have determinant bounded below by a universal constant.

For a rank-three representation `A=U Lambda U^T`,

`det A[I,J]=det(U_I) det(Lambda) det(U_J)`

for disjoint triples `I,J`. In flat/delocalized frames the individual minors can all be of order `n^(-3)` even though Cauchy-Binet keeps total determinant mass at order one. Selecting the largest single mixed minor therefore loses dimension, just as selecting one principal triple does in the flat-projector stress family.

The first unpaid implication is consequently:

> **QFORM-AGGREGATED-MIXED-MINOR-L1:** replace the single-minor selection in Theorem 2.1 by a determinant-weighted or Brascamp-Lieb aggregation over many coordinate triples, preserving the original product law, so that the Cauchy-Binet determinant mass yields an `L^1_t` bound without an `n`-dependent maximum-minor loss.

Any valid closure must still handle extra nonzero spectral directions and all sign patterns. No independence after spectral rotation may be assumed.

## 7. Status ledger

- `QFORM-FULL`: **OPEN**.
- `QFORM-MIXED-MINOR-L2-v1`: **PROVED** in the exact scope of Theorem 2.1.
- `QFORM-AGGREGATED-MIXED-MINOR-L1`: **OPEN / first unpaid implication**.
- Partner dependence `(U_i,V_i)` correction: **APPLIED**.
- Partner scalar one-difference small-ball shortcut: **REJECTED AS INSUFFICIENT**, per the partner's proved obstruction.
- Fleet02/B09 `m=2` cross-minor correction: **APPLIED**; the theorem starts at `m>=3` and makes no `m=2` density claim.

No full-proof status is claimed.