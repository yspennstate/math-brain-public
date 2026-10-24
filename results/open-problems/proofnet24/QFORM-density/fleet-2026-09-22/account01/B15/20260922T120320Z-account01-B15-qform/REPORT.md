# account01/B15 — absolute continuity and instancewise bounded density for every rank >= 3 quadratic form

**Run:** `20260922T120320Z-account01-B15-qform`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
**Assignment:** `Absolute continuity and regularity`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-SUPPORTING-THEOREM / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source state

The live owner target is: for every `n`, independent real `X_i` with densities `0 <= f_i <= 1`, and real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a valid counterexample.

The pointwise law-uniform oscillatory-decay route is refuted by phase-aligned densities, and fixed fiber-supremum estimates can lose dimension. Neither premise is used here. The full universal-constant conjecture remains open.

The named partner result actually consumed is:

`yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

Its Theorem 2.1 proves the following exact three-coordinate statement: if `B` is an invertible symmetric `3 x 3` matrix, `kappa=sigma_min(B)`, and `Y_1,Y_2,Y_3` are independent with densities bounded by `1`, then every affine quadratic

`Y^T B Y + 2 b^T Y + c`

has a density with

`||p||_infinity <= (2*pi + 3*sqrt(3))/kappa`.

I extend that mechanism to four original coordinates and combine it with an elementary principal-block lemma. The result is that **every individual rank >= 3 instance already has some bounded density**; only uniformity of the constant over `A` remains.

---

## 2. Absolute continuity needs no rank-three hypothesis

### Theorem 2.1 — `QFORM-NONZERO-AC-v1`

Let `X` be any `R^n`-valued random vector with a Lebesgue density `F in L^1`, and let

`P(x)=x^T A x + 2 b^T x + c`

with real symmetric `A != 0`. Then `P(X)` is absolutely continuous with respect to one-dimensional Lebesgue measure.

### Proof

The critical set is

`C={x: Ax=-b}`.

It is either empty or an affine subspace of codimension at least `1`, hence has `n`-dimensional Lebesgue measure zero.

Let `N subset R` have one-dimensional Lebesgue measure zero. For integers `m>=1`, define

`E_m={x in B(0,m): P(x) in N, |grad P(x)| >= 1/m}`.

On each ball, `P` is Lipschitz, so the coarea formula gives

`int_{E_m} |grad P(x)| dx = int_N H^{n-1}(E_m cap P^{-1}(y)) dy = 0`.

Since `|grad P|>=1/m` on `E_m`, `|E_m|=0`. Every point of `P^{-1}(N)\C` lies in some `E_m`, so `P^{-1}(N)` is null. Therefore

`P(P(X) in N)=int_{P^{-1}(N)} F(x) dx=0`.

Thus the pushforward law is absolutely continuous. `QED`.

**Consequence.** In the owner problem, absolute continuity is not the hard part: it already holds for every nonzero quadratic form under the much weaker assumption that the joint input law has a density. The hard assertion is the uniform `L^infinity` bound.

---

## 3. Four-coordinate affine quadratic theorem

### Theorem 3.1 — `QFORM-4VAR-AFFINE-v1`

Let `Y_1,...,Y_4` be independent real random variables with densities bounded by `1`. Let `B` be a real symmetric invertible `4 x 4` matrix and

`kappa=sigma_min(B)>0`.

For every `b in R^4` and `c in R`, the affine quadratic

`Z=Y^T B Y + 2 b^T Y + c`

has an essentially bounded density satisfying

`||p_Z||_infinity <= C_4/kappa`,

where

`C_4 = 4*pi + 8 < 20.57`.

### Proof

Complete the square and translate the four independent coordinates:

`Y^T B Y + 2 b^T Y + c = (Y+B^{-1}b)^T B (Y+B^{-1}b) + c-b^TB^{-1}b`.

Translation preserves independence and the density upper bounds. By scaling `B`, it is enough to prove the interval small-ball estimate with `kappa=1`:

`P(Y^TBY in J) <= (4*pi+8)|J|`

for every interval `J`.

Write `F(y)=prod_i f_i(y_i)`, so `0<=F<=1`. Split into

`N={y: |By|<=1}`

and `N^c`.

#### Near region

Write `B=S|B|`, where `S=sign(B)` is symmetric orthogonal, and put

`z=|B|^{1/2}y`.

Then

`y^T B y = z^T S z`,

`dy=(det |B|)^(-1/2) dz <= dz`,

and

`|By|^2 = z^T |B| z >= |z|^2`.

Therefore the near contribution is bounded by

`|{z: |z|<=1, z^T S z in J}|`.

Orthogonal diagonalization of `S` leaves the unit ball and Lebesgue measure unchanged. There are three signature types up to sign.

* Definite `(4,0)`: for `t=|z|^2`, the four-ball volume is `(pi^2/2)t^2`, so the `t`-density is `pi^2 t <= pi^2 < 4*pi` on `[0,1]`.
* Signature `(3,1)`: write `z=(u,v)` with `u in R^3`, `v in R`. For fixed `v`, the three-ball volume as a function of `t=|u|^2` has derivative `2*pi*sqrt(t)<=2*pi`. An interval of `q=|u|^2-v^2` of length `eta` therefore cuts at most `2*pi*eta` of `u`-volume. Integrating over `v in[-1,1]` gives at most `4*pi*eta`.
* Signature `(2,2)`: write `z=(u,v)` with `u,v in R^2`. For fixed `v`, planar area has constant density `pi` in `t=|u|^2`; integrating over the unit `v`-disk gives at most `pi^2*eta < 4*pi*eta`.

Hence

`P(N, Y^TBY in J) <= 4*pi |J|`.

#### Far region

On `N^c`, `|By|>1`, so for some original coordinate `i`,

`|(By)_i| > 1/2`.

For each `i`, let

`E_i={Y^TBY in J, |(By)_i|>1/2}`.

Condition on the other three original independent coordinates. As a function `g(t)` of `t=y_i`,

`g'(t)=2(By)_i`.

On `E_i`, `|g'|>1`. Since `g'` is affine, the set `|g'|>1` has at most two monotonic branches for the quadratic `g`; on each branch the preimage of an interval of length `eta` has length at most `eta`. Thus the total allowed `t`-length is at most `2 eta`. Since `f_i<=1`,

`P(E_i | Y_{hat i}) <= 2 eta`.

Summing the four coordinates gives

`P(N^c, Y^TBY in J) <= 8 eta`.

Combining near and far regions proves

`P(Y^TBY in J) <= (4*pi+8)|J|`.

Interval domination implies domination of the pushforward measure by `(4*pi+8)Leb`, hence a density with that essential-supremum bound. Scaling restores the factor `1/kappa`. `QED`.

---

## 4. A symmetric rank >= 3 matrix always has an invertible principal block of order 3 or 4

### Lemma 4.1 — `QFORM-PRINCIPAL-3OR4-v1`

If a real symmetric matrix `A` has `rank(A)>=3`, then there exists a principal index set `I` with

`|I| in {3,4}`

such that `A_{I,I}` is invertible.

### Proof

Use the following extension step. Suppose `A_{I,I}=B` is invertible and `|I|<rank(A)`. After permuting coordinates,

`A = [[B,C],[C^T,D]]`.

Its Schur complement

`S=D-C^T B^{-1}C`

is nonzero because

`rank(A)=|I|+rank(S)>|I|`.

If some diagonal entry `S_jj` is nonzero, then

`det A_{I union {j}, I union {j}} = det(B) S_jj != 0`,

so the principal block extends by one coordinate.

If every diagonal entry of `S` is zero, then because `S!=0` there are `j!=k` with `S_jk!=0`, and

`det [[0,S_jk],[S_jk,0]] = -S_jk^2 !=0`.

Thus `I` extends by two coordinates.

Now start as follows.

* If some `A_ii!=0`, begin with a nonsingular `1 x 1` principal block. Since `rank(A)>=3`, applying the extension step once or twice reaches a nonsingular block of size `3` or `4`.
* If all diagonal entries vanish, `A` is not zero, so some `A_ij!=0`; then the principal block `[[0,A_ij],[A_ij,0]]` is invertible. One extension step reaches size `3` or `4`.

This proves the lemma. `QED`.

---

## 5. New target-level consequence: every individual rank >= 3 instance already has a bounded density

Define

`kappa_{3,4}(A) = max{ sigma_min(A_{I,I}) : |I| in {3,4}, det(A_{I,I}) != 0 }`.

By Lemma 4.1 this number is strictly positive whenever `rank(A)>=3`.

### Theorem 5.1 — `QFORM-RANK3-INSTANCEWISE-LINFINITY-v1`

Let `X_1,...,X_n` be independent real variables with densities bounded by `1`, and let `A` be any real symmetric matrix with `rank(A)>=3`. Then `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity <= (4*pi+8)/kappa_{3,4}(A)`.

### Proof

Choose an index set `I` attaining `kappa_{3,4}(A)` and condition on all coordinates outside `I`. The conditional polynomial in the original independent coordinates `X_I` is

`X_I^T A_{I,I} X_I + 2 b(X_{I^c})^T X_I + c(X_{I^c})`.

If `|I|=3`, apply the consumed account02/B15 theorem, whose constant `2*pi+3*sqrt(3)` is smaller than `4*pi+8`. If `|I|=4`, apply Theorem 3.1 above. In both cases every conditional output law is dominated by

`((4*pi+8)/kappa_{3,4}(A)) Leb`.

Averaging the conditional measures preserves this domination. `QED`.

### What this closes, and what it does not

The owner assumption of at least three eigenvalues with `|lambda|>=1` implies `rank(A)>=3`. Therefore every target instance has a bounded density. There is no remaining existence/absolute-continuity pathology for a fixed matrix `A`.

However, `kappa_{3,4}(A)` can go to zero along valid target matrices, so this theorem does **not** prove a universal constant independent of `A` or `n`. The full conjecture remains open.

For the flat rank-three projectors already isolated by account02/B15, every fixed principal triple can have singular scale `O(1/n)`, so the present theorem reproduces only a dimension-dependent bound there. Aggregate-minor or delocalized geometry is still needed.

---

## 6. Four coordinates are genuinely necessary for this local structural closure

Consider

`A_* = [[0,0,1,0],
        [0,0,0,1],
        [1,0,0,0],
        [0,1,0,0]]`.

Then `A_*` has eigenvalues `1,1,-1,-1`, so it lies inside the owner's spectral regime. Every `3 x 3` principal submatrix is singular: after deleting one coordinate, the induced bipartite block has parts of sizes `2` and `1`, hence rank at most `2`. But the full `4 x 4` block is invertible with `sigma_min(A_*)=1`.

Thus a theorem using only invertible principal triples cannot even cover all fixed target matrices. The four-variable extension above is not cosmetic; it closes this exact structural hole.

---

## 7. Regularity ledger

* **Absolute continuity:** proved for every nonzero quadratic form under any absolutely continuous joint input law (Theorem 2.1).
* **Bounded density for every fixed target instance:** proved uniformly over all input laws with coordinate densities <=1, with an explicit matrix-dependent constant (Theorem 5.1).
* **Universal constant independent of `A,n`:** still open.
* **Continuous representative:** still separate in the fully rotated case. The consumed account02/B15 result proves uniform continuity on the complete diagonal branch, but neither interval domination nor the present principal-block argument alone supplies a uniform continuity modulus for arbitrary rotated forms with merely measurable input densities.

The new first unpaid implication is therefore purely **uniform**: replace the dependence on `1/kappa_{3,4}(A)` by a dimension-free aggregate mechanism exploiting the full three-large-eigenvalue resource. Flat rank-three frames show that choosing one principal block cannot do this.

## 8. Correction and dependency closure

Consumed current corrections:

* `QFORM-POINTWISE-DECAY-FALSE` — not used.
* `QFORM-FIBER-SUP-DIMENSION-LOSS` — no unrestricted fiber supremum is used.
* `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` — conditioning is always in the original independent coordinates; no rotated coordinates are treated as independent.
* `QFORM-CROSSMINOR-ALONE-FALSE` — no cross-minor-only inference is used.

Primary external fleet dependency: account02/B15 Theorem 2.1 at the exact commit/path pinned in Section 1. The four-variable theorem, principal-block lemma, and rank-three corollary are derived here.

No novelty or publication-priority claim is made. Full universal bounded density remains OPEN.