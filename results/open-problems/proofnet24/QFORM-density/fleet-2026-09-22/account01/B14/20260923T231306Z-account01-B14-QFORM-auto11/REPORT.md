# account01/B14 — Schur zero-tax localization for translations

Run: `20260923T231306Z-account01-B14-QFORM-auto11`

Status: **supporting theorem proved; full QFORM remains OPEN.**

Execution context: `WITHOUT_VERIFIED_BRAIN`.

Control target: independent real coordinates with marginal density caps `<=1`; symmetric `A`; at least three eigenvalues with absolute value `>=1`; prove a universal density bound for `X^T A X` or a valid counterexample.

This run changed mechanism from the preceding Lp/fractional/heat-flow localization runs to an exact algebraic completion-of-squares / Schur-complement mechanism. No pointwise quadratic Fourier-decay claim is used.

## Source-pinned partner input

Designated partner: `account02/B14`.

Completed partner source used here:

- repository: `yspennstate/math-open-problems`
- source commit inspected: `7a0ffb7d9c4c6074cc6e13375db70828740e1bd4`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260923T220530Z-account02-B14-QFORM-auto11/REPORT.md`
- companion checks: `.../CHECKS.md`

The completed partner material verifies, among other items, the 3-dimensional target theorem used below: if `B` is a real symmetric `3 x 3` matrix whose three eigenvalues all have modulus at least `1`, then for independent cap-one coordinates the quadratic output, with arbitrary deterministic affine terms allowed, has density cap at most

`6 sqrt(pi)`.

Only that completed result is imported below. The new localization identities and ambient application are proved here.

---

## 1. Small-ball density functional

For a finite Borel measure `mu` on `R`, define

`Lambda(mu) := sup_{a<b} mu((a,b))/(b-a)`.

For a real random variable `S`, write `Lambda(S)` for the functional of its law.

If `Lambda(mu) <= C`, then `mu(I) <= C |I|` for every bounded interval `I`. By the standard interval outer-regularity / differentiation argument, `mu << dx` and its Radon–Nikodym density satisfies `||p_mu||_infty <= C`. Conversely a density cap `C` plainly implies `Lambda(mu) <= C`. Thus it is enough to establish interval small-ball bounds.

For a fixed symmetric `k x k` matrix `B`, define its pure product-law constant

`K(B) := sup Lambda(X^T B X)`,

where the supremum runs over independent real `X_1,...,X_k` with probability densities bounded by `1`. Extended value `+infty` is allowed in the definition.

Define similarly the affine constant

`K_aff(B) := sup Lambda(X^T B X + ell^T X + c)`,

where in addition `ell in R^k` and `c in R` are arbitrary deterministic parameters.

---

## 2. Exact pure-to-affine equality for invertible active blocks

### Theorem A — `QFORM-INVERTIBLE-PURE-TO-AFFINE-EQUALITY-v1`

If `B` is invertible and symmetric, then

`K_aff(B) = K(B)`.

In particular, arbitrary deterministic translations of the active coordinates cost exactly zero in the optimal density constant.

### Proof

For arbitrary `ell,c`, set

`z = (1/2) B^{-1} ell`.

Then exactly

`X^T B X + ell^T X + c
 = (X+z)^T B (X+z) + c - (1/4) ell^T B^{-1} ell`.

Translation by the deterministic vector `z` preserves independence of the coordinates and preserves each marginal `L^infty` density cap. The final scalar constant does not change `Lambda`. Therefore every affine instance is bounded by `K(B)`, so `K_aff(B) <= K(B)`. The reverse inequality follows by taking `ell=0,c=0`. QED.

This is exact: there is no factor depending on `||B^{-1}||`, `||ell||`, support radius, moments, fragment count, or the size of the translation. The shift can be arbitrarily large.

---

## 3. Ambient Schur localization with exactly the same constant

Let the ambient symmetric matrix be decomposed in original independent coordinates as

`A = [[B, C], [C^T, D]]`,

where `B` is `k x k` and invertible. Split the random vector as `(X,Y)`, with `X` the active `k` original coordinates and `Y` all remaining original coordinates. Then

`Q = X^T B X + 2 X^T C Y + Y^T D Y`.

### Theorem B — `QFORM-SCHUR-COMPLETE-SQUARE-ZERO-TAX-LOCALIZATION-v1`

For every invertible symmetric active block `B`,

`Lambda(Q) <= K(B)`.

This holds for arbitrary `C,D` and, in fact, for every probability law of `Y` independent of `X`; no density, support, tail, or moment assumption on `Y` is needed for the localization step itself.

### Proof

Condition on `Y=y`. Set `z_y=B^{-1} C y`. Then

`Q | (Y=y)
 = (X+z_y)^T B (X+z_y)
   + y^T (D - C^T B^{-1} C) y`.

For every fixed `y`, `X+z_y` is still a product vector of cap-one marginal densities. Therefore for every bounded interval `I`,

`P(Q in I | Y=y) <= K(B) |I|`.

Integrating over `y` gives

`P(Q in I) <= K(B)|I|`.

Taking the interval supremum proves the claim. QED.

### Translation/localization consequence

The random shift `B^{-1} C Y` may be arbitrarily large and may range over arbitrarily remote pieces. The Schur term `Y^T(D-C^T B^{-1}C)Y` may have unbounded support and arbitrarily large moments. None of those quantities enters the constant.

Thus arbitrary outside translations, distant fragments, unbounded supports, and no-moment laws are localized with **zero tax** once an invertible active block has a pure quadratic density certificate.

---

## 4. Exact countable-fragment mass homogeneity

The preceding theorem is stronger than a normalized-fragment argument. Let the outside probability measure be decomposed into any finite or countable positive sum

`P_Y = sum_j nu_j`,

where `nu_j` is a subprobability measure of mass `m_j` and `sum_j m_j=1`. Let `eta_j` be the unnormalized output measure obtained by integrating the conditional law of `Q` against `nu_j`.

For every interval `I`, the same fiber estimate gives

`eta_j(I) <= m_j K(B) |I|`.

Therefore

`sum_j eta_j(I) <= K(B)|I| sum_j m_j = K(B)|I|`.

So the localization ledger is exactly linear in fragment mass. There is no `sqrt(N)`, `N^(1/3)`, logarithmic, or other fragment-count loss, even for countably many arbitrarily remote pieces. Importantly, no fragment is normalized before paying the analytic estimate.

---

## 5. Singular blocks: exact range condition and the kernel-leakage obstruction

The invertibility hypothesis can be weakened exactly when the outside coupling does not inject into the kernel of the active quadratic block.

Let `B` be symmetric, possibly singular. Let `B^dagger` be its Moore–Penrose inverse and `P_0` the orthogonal projection onto `ker(B)`. For `r=Cy`, decompose

`r_0=P_0 r`,  `r_R=(I-P_0)r`,  `z=B^dagger r`.

Because `Range(B)=ker(B)^perp`, one has `Bz=r_R` and `r_0 perp z`. Hence

`x^T B x + 2 r^T x
 = (x+z)^T B(x+z)
   + 2 r_0^T(x+z)
   - z^T B z`.

Therefore:

### Theorem C — `QFORM-SINGULAR-RANGE-ZERO-TAX-v1`

If

`P_0 C = 0`,

or equivalently `Range(C) subset Range(B)`, then

`Q | (Y=y)
 = (X+B^dagger C y)^T B (X+B^dagger C y)
   + y^T(D-C^T B^dagger C)y`,

and consequently

`Lambda(Q) <= K(B)`.

If `P_0 C != 0`, exact completion removes every range component and leaves only

`2 (P_0 C y)^T X`

as the residual affine term. Thus **kernel leakage is the exact algebraic obstruction** to pure-to-affine zero-tax localization for a singular active block. This gives a precise interface for the structural workers: either arrange an invertible active block, arrange `Range(C) subset Range(B)`, or separately pay the kernel-leakage linear term.

---

## 6. Actual completed-partner application: a dense indefinite three-direction block

Take the dense original-coordinate block

`B_* = I_3 - (2/3) 1 1^T`

so explicitly

`B_* = [[ 1/3, -2/3, -2/3],
        [-2/3,  1/3, -2/3],
        [-2/3, -2/3,  1/3]]`.

This is a Householder reflection:

`B_*^2=I_3`,

with spectrum

`{1,1,-1}`.

It is therefore invertible, dense in the original coordinate basis, off-diagonal, and indefinite.

The completed `account02/B14` three-dimensional theorem yields

`K(B_*) <= 6 sqrt(pi)`.

Now allow an arbitrary number of additional independent cap-one coordinates `Y`, an arbitrary coupling matrix `C`, and an arbitrary symmetric outside block `D`. Set

`A = [[B_*, C], [C^T, D]]`,

`Q = X^T B_* X + 2X^T C Y + Y^T D Y`.

Since `B_*^{-1}=B_*`, Theorem B gives the exact conditional identity

`Q | (Y=y)
 = (X+B_* C y)^T B_* (X+B_* C y)
   + y^T(D-C^T B_* C)y`.

The partner theorem therefore applies on every fiber and yields the actual inequality

`||p_Q||_infty <= 6 sqrt(pi) = 10.6347231054...`.

This is uniform over dimension, `C`, `D`, all outside translations, all support geometry, and all moments.

### Verification that this is an exact-target family

Let the eigenvalues of the full `A` be sorted decreasingly. Since `B_*` is a principal `3 x 3` submatrix with eigenvalues `1,1,-1`, Cauchy interlacing gives

`lambda_2(A) >= 1`

and

`lambda_min(A) <= -1`.

Thus the full matrix has at least two eigenvalues `>=1` and at least one eigenvalue `<=-1`; in particular it has at least three eigenvalues of absolute value at least `1`.

So this is not a diagonal/projection-only toy case: it is a dense indefinite original-coordinate active block with arbitrary ambient couplings and arbitrary admissible product laws, and it lies exactly inside the owner's target.

---

## 7. What this resolves and what remains open

Resolved in this run:

1. **Arbitrary deterministic affine terms on an invertible active block cost exactly zero** relative to the pure quadratic density constant.
2. **Arbitrary outside random translations, tails, distant fragments, unbounded supports, and absent moments cost exactly zero** after conditioning on outside original coordinates.
3. The outside-fragment ledger is **exactly linear in unnormalized mass**, so finite/countable fragmentation causes no proof tax.
4. For singular active blocks, the exact remaining algebraic defect is the kernel component `P_0 C`; `Range(C) subset Range(B)` is the precise zero-tax condition.
5. Applying the completed partner theorem gives the concrete exact-target ambient inequality

   `||p_Q||_infty <= 6 sqrt(pi)`

   for every ambient extension of the dense reflection block `B_*` above.

Still open:

Barely knowing that the full symmetric matrix `A` has three eigenvalues with absolute value at least `1` does **not** presently force an original-coordinate principal block `B` to which one can apply the preceding certificate with universal parameters. The three spectral directions may be diffusely spread across many coordinates. This is the remaining matrix-structural bridge, and this report does not claim to solve it.

No counterexample to full QFORM was found in this run.