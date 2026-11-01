# fleet03/B12 — exterior-power regularized determinant and additional-eigenvalue control

**Run:** `fleet03-B12-20260922T140131Z-r11-ext3`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  

## 1. Exact target and change of mechanism

The target remains: for every dimension `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal finite bound on the density of `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

This run deliberately changes mechanism from B12's previous small physical principal-block pair/triple argument. It uses the current regularized cross-block determinant theorem and exterior-power curvature. No spectral rotation is used to assert independence, no pointwise one-dimensional Fresnel decay is assumed, and no single large coordinate minor is extracted.

The source theorem consumed is the completed interactive report

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its needed statement is: for a physical cut with cross block `B=A[I,J]`, for `1<=q<2`, if the coordinate leverage of `range(B)` on the chosen physical side is at most `q/2`, then

`|phi_Q(t)| <= det(I + c_q t^2 B B^T)^(-1/(4q))`,

where

`c_q = 2q/(pi^2 e^2)`.

The estimate is uniform over all within-block quadratic phases, all outside coordinates and couplings, all input laws with density cap one, and all signs. Thus it is valid after conditioning only in the original independent coordinates.

At the prewrite source-bound check there was still no current QFORM artifact at the assigned partner path `fleet04/B12` in either the shared handoff tree or the canonical fleet04 QFORM archive. I therefore do **not** fabricate a partner result. The owner-supplied completed determinant theorem above is applied directly. Partner application remains an operationally unmet clause, not a mathematical premise.

## 2. Exterior-power density lemma

For a positive semidefinite matrix `M`, write

`e_m(M) = sum_{1<=i_1<...<i_m} mu_{i_1}...mu_{i_m}`

for the `m`th elementary symmetric polynomial of its eigenvalues. If the singular values of `B` are `s_1,s_2,...`, then

`e_m(BB^T) = sum_{i_1<...<i_m} s_{i_1}^2...s_{i_m}^2`.

### Theorem 2.1 — `QFORM-EXTERIOR-POWER-CROSSBLOCK-v1`

Let `A` be any real symmetric matrix and let `I,J` be disjoint sets of **original** coordinates. Set `B=A[I,J]`. Assume for some `1<=q<2` that

`max_i (P_range(B))_{ii} <= q/2`

on the physical side to which the regularized determinant theorem is applied. Let `m` be an integer with

`m > 2q`

and suppose `E_m := e_m(BB^T)>0`. Then, for arbitrary independent input coordinates with densities bounded by one, `Q=X^T A X` has a continuous density, vanishing at infinity, and

`||p_Q||_infinity <= K_{m,q} E_m^(-1/(2m))`,

where

`K_{m,q} = [e/(2m sqrt(2q))] B(1/(2m), 1/(4q)-1/(2m))`.

Here `B(a,b)` is the beta function. The same conclusion survives arbitrary measurable coordinate-separable real perturbations that are finite almost surely.

#### Proof

By the consumed determinant theorem,

`|phi_Q(t)| <= det(I + c_q t^2 BB^T)^(-1/(4q))`,

with `c_q=2q/(pi^2 e^2)`. Expanding the determinant into elementary symmetric polynomials of the nonnegative eigenvalues of `BB^T` gives

`det(I+c_q t^2 BB^T) >= 1 + c_q^m t^(2m) e_m(BB^T)`.

Hence

`|phi_Q(t)| <= (1+c_q^m E_m t^(2m))^(-1/(4q)).`                 (2.1)

Because `m>2q`, the exponent at infinity is `m/(2q)>1`, so (2.1) is integrable. Put

`u = c_q^(1/2) E_m^(1/(2m)) |t|`.

The beta integral gives

`int_0^infinity (1+u^(2m))^(-1/(4q)) du`

`= (1/(2m)) B(1/(2m), 1/(4q)-1/(2m)).`

Therefore Fourier inversion yields

`||p_Q||_infinity`

`<= (1/(2pi)) int_R |phi_Q(t)| dt`

`<= c_q^(-1/2) E_m^(-1/(2m)) /(2pi m)`

`   * B(1/(2m),1/(4q)-1/(2m))`

`= K_{m,q} E_m^(-1/(2m)).`

Since `phi_Q` is integrable, Fourier inversion supplies a continuous representative vanishing at infinity. QED.

### Why this is additional-eigenvalue control

The right side depends on one chosen exterior-power energy `e_m`, not on the product of **all** nonzero cross singular values. Adding any further cross singular values can only increase every `e_m`; arbitrarily tiny added singular values never create a reciprocal-small-singular-value penalty. This is a monotone statement at the level actually used by the proof. It does not claim that an arbitrary spectral perturbation of `A` preserves a fixed physical cross block.

For `m=3,q=1`,

`K_{3,1} = [e/(6 sqrt(2))] B(1/6,1/12)`

`= 5.6557637733872399...`.

Thus a leverage-`1/2` cut with `e_3(BB^T)>=eta` gives

`||p_Q||_infinity <= 5.655764 eta^(-1/6)`.

This is an aggregate three-direction criterion: it does not require three individually specified singular values to share one common lower bound.

## 3. Diffuse full-range theorem with arbitrary extra eigenvalues

The preceding lemma can be combined with the same MSS two-part frame partition used in the consumed report, but with a free leverage parameter and arbitrary exterior-power order.

Write the entire nonzero spectral decomposition as

`A = U Lambda U^T`,

where `U` has orthonormal columns spanning the **entire range** of `A`, and `Lambda` is invertible. Put

`rho = max_i ||u_i||^2`.

Define

`delta(rho) = 1/2 - sqrt(2 rho) - rho`.

Whenever `delta(rho)>0`, MSS gives a physical partition `I,J` for which

`delta I <= U_I^T U_I, U_J^T U_J <= (1-delta) I`.             (3.1)

For `B=A[I,J]=U_I Lambda U_J^T`, (3.1) implies:

1. `range(B)=range(U_I)`;
2. the leverage of `range(B)` is at most `rho/delta`;
3. every singular value satisfies `s_k(B)>=delta s_k(Lambda)`.

The third point follows by writing the nonzero singular values of `B` as those of

`(U_I^T U_I)^(1/2) Lambda (U_J^T U_J)^(1/2)`

and using the lower singular-value bound on both outer factors. Consequently, for every `m<=rank(A)`,

`e_m(BB^T) >= delta^(2m) e_m(Lambda^2)`.                      (3.2)

### Theorem 3.1 — `QFORM-DIFFUSE-EXTERIOR-POWER-v1`

Assume `delta(rho)>0`. Choose any `q` with

`max(1, 2rho/delta(rho)) <= q < 2`

and any integer `m<=rank(A)` satisfying

`m>2q`.

Then `X^T A X` has a continuous density, vanishing at infinity, and

`||p_Q||_infinity`

`<= [K_{m,q}/delta(rho)] e_m(Lambda^2)^(-1/(2m)).`             (3.3)

This permits **all** additional nonzero eigenvalues represented in `Lambda`: they may be arbitrarily small or large and have either sign. Their signs disappear only inside the legitimate squared spectral quantity `e_m(Lambda^2)`; no independence in the eigenbasis is asserted. Extra eigenvalues only increase the exterior-power energy appearing in (3.3).

#### Proof

The leverage bound in (3.1) is at most `rho/delta<=q/2`, so Theorem 2.1 applies to the physical cut. Insert (3.2) into its conclusion. QED.

## 4. Concrete strengthening of the current three-large-eigenvalue diffuse branch

Suppose only that at least three eigenvalues have absolute value at least one. Then

`e_3(Lambda^2)>=1`.

For a rank-three matrix (or when using only `m=3`), Theorem 3.1 needs some `q<3/2`. Taking the smallest permitted value

`q_rho = max(1, 2rho/delta(rho))`

works exactly when

`2rho/delta(rho) < 3/2`.

Solving the boundary equation gives

`rho < rho_3^* := (39-6 sqrt(30))/98`

`= 0.0626188423437758489...`.                                (4.1)

Therefore the existing full-spectrum diffuse-range branch extends from the previously stated `rho<=1/32=0.03125` to every

`rho < 0.06261884234377585`,

with an explicit finite constant supplied by (3.3). This is still an additional leverage hypothesis and is **not** the unrestricted conjecture.

A simple source-exact checkpoint is `rho=1/16=0.0625`. Then

`delta=(7-4 sqrt(2))/16 = 0.08394660940672623...`,

`q=2/(7-4 sqrt(2)) = 1.489041676410868... <3/2`.

Using only the three target eigenvalues gives a finite universal constant; the individual-three-singular-value envelope from the same determinant theorem gives about

`2562.663`.

The constant is large near the endpoint because the integrability exponent tends to the logarithmic boundary. The significance of (4.1) is scope, not constant optimization.

For the older `rho=1/32` point, `delta=7/32` and `q=1`. The aggregate formula is

`||p_Q||_infinity <= 25.854921 * e_3(Lambda^2)^(-1/6)`.

The consumed report's sharper individual-third-singular-value gamma integral can be smaller when only three eigenvalues matter. The new exterior-power formula becomes advantageous when many additional eigenvalues contribute enough aggregate `e_3` energy. No claim of a uniformly improved constant in every spectrum is made.

## 5. Four-or-more nonzero eigenvalues: a second leverage extension

If `rank(A)>=4`, take `m=4`. The integrability requirement is only `q<2`. Hence the same argument applies whenever

`2rho/delta(rho) < 2`,

i.e. `rho<delta(rho)`. The exact boundary is

`rho < rho_4^* := (2-sqrt(3))/4`

`= 0.0669872981077806766...`.                                (5.1)

The price is the factor `e_4(Lambda^2)^(-1/8)`. Thus a fourth eigenvalue that is nonzero but extremely small gives a finite but non-universal-in-that-eigenvalue numerical bound, while a quantitatively nontrivial fourth eigenvalue yields a correspondingly stronger certificate. This is the correct monotone behavior for an **additional-eigenvalue** theorem; it is not used to pretend that the original three-eigenvalue target has four large directions.

More generally Theorem 3.1 lets one select the smallest exterior-power order `m>2q`; it never multiplies reciprocals of every tiny eigenvalue.

## 6. Exact remaining implication to the full target

The full conjecture remains **OPEN**. The unpaid bridge is now more precise:

> Prove that every symmetric matrix with three eigenvalues of absolute value at least one either enters a physical local-curvature branch already covered by B12's prior principal-block theorem, or admits a physical partition with enough leverage-controlled exterior-power cross energy to invoke Theorem 2.1, or is controlled by a third heavy-coordinate aggregation mechanism.

The theorem here removes an artificial obstacle inside the diffuse branch: arbitrary additional spectral directions do not have to be discarded, and one need not pay the product of all of their sizes. What remains is the heavy-coordinate/nonseparable structural reduction.

A promising next attack is to classify the exact third exterior-power budget

`e_3(A^2)=sum_{|I|=|J|=3} det(A[I,J])^2 >=1`

by the overlap size `|I cap J|`. The four overlap channels (0,1,2,3) correspond respectively to fully disjoint cross smoothing, mixed pivot channels, and principal curvature. Because the identity is an aggregate sum of squares, it respects the known correction that no single coordinate minor need be dimension-independently large.

## 7. Status and source integrity

- Full QFORM: **OPEN / NOT PROVED**.
- Theorems 2.1 and 3.1: **PROVED**, conditional only on the cited completed regularized determinant theorem and the same MSS partition input already used there.
- Continuity: **PROVED within the stated theorem scopes** via `phi in L^1`; not proved for the unrestricted target.
- Partner fleet04/B12: no completed current QFORM artifact visible at the source-bound check; no result was fabricated or borrowed from stale FEI work.
- Native brain status: **WITHOUT_VERIFIED_BRAIN**; repository retrieval is not native receiver-context ingestion.
- No scheduler mutation, email, Drive action, public release, remote workflow, paid model/API/Codex call, credential access, or cross-account scheduler action was used.
