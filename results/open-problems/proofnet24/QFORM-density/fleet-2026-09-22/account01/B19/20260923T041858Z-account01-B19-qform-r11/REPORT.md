SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B19, 2026-09-23T04:18:58Z.
attacking: co-heavy aggregate routing: replace the now-refuted fixed-second-gradient selector by an exact three-independent-scalar theorem and use it to pay arbitrary curvature on a three-line bank endpoint.

# B19 r11 — three independent scalars are universally paid; arbitrary curved three-line banks are paid

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

Fresh prepublication control: `yspennstate/math-research-brain@f36917932cd48ad857c3293a596e44b3e44a8498`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction inbox was reread. No invalid arbitrary-joint coarea, conditional-cap-as-independence, post-rotation independence, coefficient deletion, or reciprocal single-minor selector is used below.

## Source-pinned peer inputs actually used

1. **Latest designated partner account02/B19 r26.** Handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B19/20260923T041017Z-account02-B19-QFORM-r26.md`, blob `880e609e974fa8d329ddf882f9cb435b644c0ee8`; canonical mathematics `yspennstate/math-open-problems@d294539dec9f048e8da354542b37cc9ac664f020`. It proves the pure-bipartite target branch

   `A=[[0,C],[C^T,0]], s_2(C)>=1  =>  ||p_Q||_infinity <= e sqrt(pi) < 4.819`,

   and gives a target-valid family showing that N3 aggregate curvature cannot in general be converted first into one fixed physical second-gradient area. Its first synthesis debt is `QFORM-N3-CURVED-AGGREGATE-THIRD-SOURCE-v1`.

2. **Rank-two affine half-Riesz theorem.** Source `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, report blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`. For independent cap-one inputs and an invertible symmetric two-dimensional quadratic part `S`, arbitrary affine terms satisfy

   `sup_t E|Z^T S Z + ell^T Z - t|^(-1/2) <= 128 |det S|^(-1/4)`;

   when the affine term lies in the quadratic range the constant improves to `16 sqrt(30)`. In dimension two the range is all of `R^2`, so the improved constant applies below.

3. **Pair-log theorem.** Source `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `PAIR_LOG_THEOREM.md`. For an exact-rank-three original-coordinate form with nonzero eigenvalue magnitudes at least `s`, any invertible indefinite physical pair `B`, with `D=|det B|` and `kappa=sigma_min(B)`, gives

   `||p_Q||_infinity <= 8 sqrt(5) (D kappa s)^(-1/4)`.

4. **Weighted affine-fiber BL.** account02/B06, canonical `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, report blob `dfdbbc3b74ad0cf0d56eae0f75e0cab8c742f38e`. A normalized one-dimensional product projection has density cap at most `sqrt(e)`.

These are used at their stated scopes only.

---

## 1. New theorem: arbitrary symmetric quadratic form of three independent scalars

### `QFORM-3SCALAR-UNIVERSAL-v1`

Let `Y=(Y1,Y2,Y3)` have independent coordinates, each with density at most one. Let `M=M^T` be `3x3` with

`singular_min(M) >= s > 0`.

For every affine vector `d` and constant `c`, the random variable

`Q=Y^T M Y + d^T Y + c`

has an essentially bounded density and

`boxed: ||p_Q||_infinity < 105/s.`

All signatures and all degeneracies of individual entries of `M` are allowed; only invertibility at scale `s` is used.

### Proof

Split at the physical diagonal threshold `s/2`.

#### Case A: some physical diagonal is large

After relabeling,

`M=[[a,b^T],[b,C]]`, with `|a|>=s/2`, `Z=(Y2,Y3)`.

Include the affine term and complete the `Y1` square. For a deterministic function `h(Z)`,

`Q=a(Y1+h(Z))^2 + Z^T S Z + ell^T Z + c0`,

where

`S=C-b b^T/a`, and `det S = det M / a`.

Conditioning on `Z`, translation of `Y1` preserves the cap one. The density of `a(Y1+h)^2` is bounded by

`|a|^(-1/2) |u|^(-1/2)`

at displacement `u`. Hence

`p_Q(t) <= |a|^(-1/2) E|Z^T S Z + ell^T Z + c0-t|^(-1/2)`.

Because `det M !=0`, also `det S!=0`. Apply the completed rank-two affine half-Riesz theorem with its in-range constant `16 sqrt(30)`:

`||p_Q||_infinity`
`<=16 sqrt(30) |a|^(-1/2)|det S|^(-1/4)`
`=16 sqrt(30) |a|^(-1/4)|det M|^(-1/4)`.

Since `|det M|>=s^3` and `|a|>=s/2`,

`||p_Q||_infinity <=16 sqrt(30) 2^(1/4) / s`
`=104.216889989.../s <105/s`.

No rotated independence is used: the only conditioning is on the other two original independent scalar coordinates.

#### Case B: all physical diagonals are small

Assume `|M_ii|<s/2` for all `i`. Since `||M e_i||>=s`, for any column `i` the two off-diagonal squares sum to more than `3s^2/4`. Hence for some `j!=i`,

`|M_ij| >= sqrt(3/8) s`.

Take that physical pair

`B=[[a,b],[b,c]]`.

Then `|a|,|c|<s/2` and `|b|>=sqrt(3/8)s`, so

`det B = ac-b^2 <0`,

`D:=|det B| >= (3/8-1/4)s^2 = s^2/8`.

Also, viewing `B=[[0,b],[b,0]]+diag(a,c)` and using the singular-value perturbation inequality,

`kappa:=sigma_min(B) >= |b|-s/2`
`>= (sqrt(3/8)-1/2)s = ((sqrt(6)-2)/4)s`.

Thus the pair is genuinely indefinite and the pair-log theorem applies to the full three-coordinate form, including the arbitrary affine term:

`||p_Q||_infinity`
`<=8 sqrt(5) [ (s^2/8) (((sqrt(6)-2)/4)s) s ]^(-1/4)`
`=8 sqrt(5) [32/(sqrt(6)-2)]^(1/4) /s`
`=51.96160262.../s <105/s`.

The two cases exhaust every symmetric invertible `3x3` matrix. This proves the theorem.

---

## 2. Repaired localized physical-triple theorem

### `QFORM-LOCALIZED-3PHYSICAL-REPAIRED-v1`

For the full owner target in arbitrary dimension, suppose there is a set `I` of three **original coordinates** such that

`sigma_min(A[I,I]) >= s >0`.

Condition on all coordinates outside `I`. The remaining conditional form in `X_I` is exactly

`X_I^T A[I,I] X_I + d(outside)^T X_I + c(outside)`.

The three coordinates in `I` remain independent and cap one. Applying `QFORM-3SCALAR-UNIVERSAL-v1` conditionally gives the same bound for every outside realization. Averaging yields

`boxed: ||p_(X^T A X)||_infinity <105/s.`

This is a source-valid localized theorem that does **not** use the refuted arbitrary-joint rank-three coarea lemma. It also tolerates arbitrary outside quadratic curvature and cross-couplings because those become only an affine term after the outside coordinates are fixed.

---

## 3. Exact curved three-line bank endpoint

### `QFORM-THREE-LINE-FRAME-PAID-v1`

Let an exact-rank-three core be

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `sigma_min(M)>=1`.

Assume every row of the Parseval frame `R` lies on one of three one-dimensional subspaces spanning `R^3`. Then

`boxed: ||p_(X^T A X)||_infinity <105 e <286.`

This allows **arbitrary diagonal and off-diagonal entries of `M`**, hence arbitrary signs and arbitrary same-line rank-one self curvature. It strictly extends the prior B19 zero-diagonal three-bank endpoint.

### Proof

First, the three support lines are automatically orthogonal. Let their unit directions be `v1,v2,v3` and let `alpha_j` be the total squared row mass on line `vj`. Parseval gives

`sum_j alpha_j v_j v_j^T=I_3`.

Set `W=[sqrt(alpha_1)v1, sqrt(alpha_2)v2, sqrt(alpha_3)v3]`. Then `WW^T=I_3`; since `W` is square, it is orthogonal. Therefore `alpha_j=1` and the three line directions form an orthonormal basis.

Group original coordinates by those three lines and define

`Z_j=sum_(i in I_j) r_ij X_i`.

The banks `I_1,I_2,I_3` are disjoint, so `Z_1,Z_2,Z_3` are genuinely independent. Their coefficient vectors all have Euclidean norm one. Apply account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` at `k=1`:

`||p_(Z_j)||_infinity <= sqrt(e)`.

Now set `W_j=sqrt(e) Z_j`. The `W_j` are independent cap-one variables and

`X^T A X = Z^T M Z = W^T (M/e) W`.

Since `sigma_min(M/e)>=1/e`, the three-scalar theorem gives

`||p_(X^TAX)||_infinity <105 e =285.419591988...<286`.

No post-rotation independence is asserted: independence comes only from the three **disjoint original-coordinate banks**.

---

## 4. Application to the latest partner and the conditional proof graph

The latest designated partner r26 changes the immediate target. It already proves two facts that are both used here:

* the exact pure-bipartite node is paid by `<4.819`;
* a fixed physical second-gradient extraction is false even in target-valid N3 families, so a universal proof must accept a genuinely aggregate receiver.

The new three-line theorem pays a complementary **curved aggregate** endpoint: once the surviving rank-three source is carried by three disjoint one-dimensional original-coordinate banks, *all* `3x3` self/cross curvature on those three bank aggregates is harmless, with one explicit universal constant `<286`. Thus the old B19 zero-diagonal restriction is removed at this endpoint.

A compact conditional end-to-end route is now:

1. if a quantitative original-coordinate physical triple exists, `QFORM-LOCALIZED-3PHYSICAL-REPAIRED-v1` pays it by `<105/s`;
2. the partner's pure-bipartite endpoint is paid by `<4.819`;
3. existing scalar-pivot, pair-log, ridge/diffuse, and legitimate aggregate-E2 nodes remain available in their source-pinned scopes;
4. if the N3/co-heavy residual collapses product-preservingly onto exactly three one-dimensional source banks, `QFORM-THREE-LINE-FRAME-PAID-v1` pays it by `<286` without any single local minor.

Therefore the first essential missing implication on this route is now

`QFORM-N3-CURVED-AGGREGATE-TO-THREEBANK-OR-PAID-v1`:

> Starting from the partner r26 N3 survivor with aggregate rank-two cross currency and the unavoidable third source, prove **without deleting the nonzero within-bank curvature** that either (a) a physical three-coordinate block has `sigma_min>=c0`, (b) a currently paid pure-bipartite/ridge/scalar-pair node occurs, or (c) the product source can be represented exactly by three disjoint one-dimensional banks (or by a stronger bank receiver that contains this case).

The exact three-line endpoint is now fully paid for arbitrary curvature. What remains is the nonperturbative routing/stability step: near-line coefficients cannot simply be dropped, because law-uniform coefficient-perturbation continuity is one of the live corrections.

Arbitrary extra spectrum beyond the exact rank-three core remains a separate full-target debt wherever the current global reduction has not already removed it.

## Scope / continuity

This report proves essential boundedness on the stated branches. It does **not** prove continuity of the resulting density, and it does not claim the unrestricted owner target is solved. Full QFORM remains `OPEN / NOT PROVED`.
