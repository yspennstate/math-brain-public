SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T00:32:32Z.
attacking: a strict-N3 near-null hub in which the two projected leaf coordinates are genuinely dependent; preserve the original product factorization through the mixed-Fresnel curved pushforward and compare it with the singular Schur-pivot route.

# QFORM r21 — same-bank null-hub interpolation inside N3

## Status

**PROVED SUPPORTING THEOREM + EXPLICIT ROUTE OBSTRUCTION.** The full quadratic-form conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This run gives a target-valid exact-rank-three family lying inside the strict no-pivot class N3, with one leverage-one physical coordinate and a genuinely dependent two-dimensional product projection on the remaining coordinates. The completed Claude mixed-Fresnel theorem gives a uniform global density bound across a scalar pivot passing through zero, while the scalar-Schur/half-Riesz certificate diverges like a negative power of that pivot. This is a mechanism result, not a full-target proof.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Authenticated repository retrieval was used, but no native learned-memory receiver ingestion was established.

## Pinned sources actually consumed


Required newest-Claude package:
- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
- same commit/path `FOURIER_ROUTE_REPORT.md`
- same commit/path `COUNTEREXAMPLE_SEARCH.md`

The source result used quantitatively is `FOURIER_ROUTE_REPORT` Theorem MF. In its notation, for heavy coordinates H, leaf block `A_LL=D_L+S Lambda S^T`, cross block `C=A_LH`, augmented leaf rows `w_l=(C_{l,.},s(l))`, and `Gamma=sum_l w_l w_l^T`, if `Gamma` is invertible and every augmented leverage is at most `1/2`, then

`|phi_Q(t)| <= (4 pi)^(|H|+r/2) 2^(-|H|) |t|^(-(|H|+r/2)) prod_k |lambda_k|^(-1/2) det(Gamma)^(-1/2)`.

No condition is imposed on `A_HH`, the diagonal leaf twist, or affine terms. This is crucial below.

The source `COUNTEREXAMPLE_SEARCH.md` also proves the rough-law ruled one-sheet estimate for exact rank-three signature `(2,1)`, using the cap-two two-dimensional marginal theorem without asserting projected independence.

Newest designated-partner result actually applied: fleet03/B16 handoff `20260923T000300Z-fleet03-B16-QFORM-r20`, canonical mathematics `yspennstate/math-open-problems@bf4ea19e3c7e327cd53615128f4daaeee0e53811`. It proves that bounded joint projection density, even together with bounded coordinate marginals, is insufficient receiver-side data at a nonzero pivot, and records the valid scalar-square plus rank-two half-Riesz replacement. The comparison in Section 6 below applies that replacement to the present family.

Corrections preserved: no independence after spectral rotation; no arbitrary-joint rank-three coarea; no normalized conditional-density supremum; no law-uniform one-dimensional Fresnel decay; no fixed physical pair/triple extraction from spectrum alone.

## 1. A same-bank exact-rank-three family

Fix an even integer `m>=4`. Choose signs `epsilon_j in {+1,-1}`, `j=1,...,m`, with

`sum_j epsilon_j = 0`.

Let

`a = m^(-1/2) (1,...,1)`,
`b = m^(-1/2) (epsilon_1,...,epsilon_m)`.

Then `a,b` are orthonormal vectors in `R^m`. Let `X_0,X_1,...,X_m` be independent real random variables with arbitrary probability densities bounded by one. Put

`Y = a.X = m^(-1/2) sum_j X_j`,
`Z = b.X = m^(-1/2) sum_j epsilon_j X_j`.

For a real parameter `delta`, define

`c_delta = sqrt(1+|delta|)`

and

`Q_{m,delta} = delta X_0^2 + 2 c_delta X_0 Y + Z^2`.          (1.1)

The physical matrix is

`A_{m,delta} = [[delta, c_delta a^T], [c_delta a, b b^T]]`.    (1.2)

The three physical-space vectors `e_0,a,b` are orthonormal. On their span, `A_{m,delta}` is represented by

`M_delta = [[delta,c_delta,0],[c_delta,0,0],[0,0,1]]`.        (1.3)

It vanishes on the orthogonal complement. Hence it has exact rank three.

The two eigenvalues of the leading `2x2` block are

`(delta +/- sqrt(delta^2+4 c_delta^2))/2`.

Because `c_delta^2=1+|delta|`, this simplifies exactly:
- if `delta>=0`, the two values are `1+delta` and `-1`;
- if `delta<=0`, the two values are `1` and `-(1+|delta|)`.

Together with the third eigenvalue `1`, every `A_{m,delta}` has three eigenvalues of modulus at least one. Thus (1.1) is genuinely inside the full QFORM target for every real `delta`.

## 2. The family lies in the strict N3 no-pivot class near delta=0

The physical entries are

`A_00=delta`,
`A_jj=1/m`,
`A_0j=c_delta/sqrt(m)`,
`A_jk=epsilon_j epsilon_k/m` for leaf indices `j,k`.

For a hub-leaf pair,

`det A[{0,j},{0,j}] = (delta-c_delta^2)/m`.                    (2.1)

Hence its absolute value is `1/m` for `delta>=0`, and `(1+2|delta|)/m` for `delta<0`. For two leaves `j!=k`,

`det A[{j,k},{j,k}] = 1/m^2 - (epsilon_j epsilon_k/m)^2 = 0`. (2.2)

Fix any `tau in (0,1]`. Choose `|delta|<tau/2` and an even `m` so large that

`m > (1+tau)/tau`.

Then all physical diagonal entries have magnitude `<tau` and every physical `2x2` principal determinant has magnitude `<tau`. Thus this is an explicit one-parameter family **inside N3(tau)** that crosses the null pivot `delta=0` while keeping the full three-large-eigenvalue hypothesis.

This already blocks one tempting N3 shortcut: the no-pivot assumptions do not force every spectral-row leverage to be small. The rank-three spectral subspace is `span{e_0,a,b}`; its leverage at the hub is exactly one, while each leaf leverage is `2/m`. Therefore the diffuse-frame hypothesis `max leverage <=1/2` fails maximally at the hub.

Two other completed structural currencies are also blind here. For every coordinate cut, the off-diagonal cross block is the sum of the split hub-star part (rank at most one) and the split rank-one leaf square `b b^T` (rank at most one), so every cross block has rank at most two. Hence every D'/D5 three- or five-volume certificate is zero. Also, every nonzero rank-three Pluecker triple must contain the hub coordinate 0, because the leaf rows span only the two-dimensional `a,b` plane. Therefore the disjoint-Pluecker mass from the previous B16 two-bank route is exactly zero.

So this family is simultaneously strict-no-pivot, high-leverage, cross-volume-blind, and two-full-bank-blind.

## 3. The two projected leaf coordinates need not be independent

The pair `(Y,Z)` is an orthogonal two-dimensional projection of the original leaf product law. The LPP/Ball product-marginal theorem used in the Claude source therefore gives a joint density cap

`||rho_{Y,Z}||_infinity <= 2`.                                (3.1)

But this is **not** an independence statement, and independence is false for perfectly admissible examples.

For example, let `m=4`, choose signs `(+,+,-,-)`, and take the four leaf inputs iid `Unif[0,1]`. Writing

`S_+=X_1+X_2`, `S_-=X_3+X_4`,

we have

`Y=(S_++S_-)/2`, `Z=(S_+-S_-)/2`.

The joint support is the parallelogram defined by

`0<=Y+Z<=2`, `0<=Y-Z<=2`,

whereas the product of the marginal supports is a strictly larger rectangle. Hence `Y` and `Z` are not independent. This is exactly the projection-product interface assigned to B16: the useful object is a dependent product **projection**, not a pair of independent rotated coordinates.

## 4. Mixed Fresnel pays the entire same-bank family

Apply the completed source Theorem MF with

`H={0}`, `L={1,...,m}`, `D_L=0`, `r=1`, `S=b`, `Lambda=[1]`,

and cross column

`C=c_delta a`.

For leaf `j`, the augmented row is

`w_j=(c_delta/sqrt(m), epsilon_j/sqrt(m))`.

Since the signs are balanced,

`Gamma = sum_j w_j w_j^T = diag(c_delta^2,1)`.                 (4.1)

Thus `det Gamma=c_delta^2`. Moreover every augmented leverage is exactly

`w_j^T Gamma^(-1) w_j = 1/m+1/m = 2/m <=1/2`.               (4.2)

Theorem MF therefore gives, uniformly over all cap-one input densities and all `delta`,

`|phi_{Q_{m,delta}}(t)| <= K_delta |t|^(-3/2)`,               (4.3)

where

`K_delta = 4 pi^(3/2) / c_delta`.                             (4.4)

This application retains the original leaf product factorization. It never treats `Y,Z` as independent.

Combining (4.3) with the trivial `|phi|<=1`,

`integral_R min(1,K_delta |t|^(-3/2)) dt = 6 K_delta^(2/3)`.

Fourier inversion therefore yields the global essential density bound

`||p_{Q_{m,delta}}||_infinity
 <= 3 K_delta^(2/3)/pi
 = 3*2^(4/3) c_delta^(-2/3)
 = 3*2^(4/3) (1+|delta|)^(-1/3)
 <= 3*2^(4/3)
 = 7.559526299369239...`.                                    (4.5)

This is a genuine full-output bound, not a one-sided or conditional estimate. It is uniform in the dimension parameter `m`, in the pivot `delta`, and in all admissible one-dimensional input laws.

Call this supporting theorem

`QFORM-SAME-BANK-NULL-HUB-MIXED-FRESNEL-v1`.

## 5. Relation to the two-dimensional curved marginal theorem

The family has signature `(2,1)`. The ruled one-sheet theorem from the required `COUNTEREXAMPLE_SEARCH.md` applies directly to the exact rank-three product projection and gives

`p_{Q_{m,delta}}(s) <= pi sqrt(2)`                              (5.1)

on the majority-sign one-sheet side `s>=0` (in the interval-domination / essential-density sense appropriate to rough input laws), because all three nonzero eigenvalues have modulus at least one.

The estimate (5.1) uses only the source-valid two-dimensional product-marginal geometry along real rulings. It does not control the two-sheet side. Equation (4.5) is therefore a concrete mechanism extension: in this null-hub geometry the original product factorization, retained through Theorem MF, closes the opposite curved side as well even though the projected coordinates `Y,Z` are dependent.

This is the exact distinction required by the live corrections. A bounded joint projection density by itself is not being substituted for source provenance.

## 6. Designated-partner comparison: Schur completion loses the null limit

For `delta!=0`, scalar completion gives the exact identity

`Q_{m,delta}
 = delta (X_0 + (c_delta/delta)Y)^2
   + Z^2 - (c_delta^2/delta)Y^2`.                              (6.1)

Conditioned on the leaves, the shifted scalar `X_0+(c_delta/delta)Y` still has density cap one because `X_0` is an original coordinate independent of the leaves. The rank-two residual in the orthonormal projected coordinates `(Y,Z)` has determinant magnitude

`c_delta^2/|delta|`.

Applying the valid square-peel plus the designated partner's in-range rank-two half-Riesz bound gives the source-valid certificate

`||p_{Q_{m,delta}}||_infinity
 <= 16 sqrt(30) |delta|^(-1/2)
      (c_delta^2/|delta|)^(-1/4)
 = 16 sqrt(30) |delta|^(-1/4) c_delta^(-1/2)`.                (6.2)

The right side diverges as `delta ->0`. This is exactly the loss highlighted by fleet03/B16 r20: scalar Schur completion separates quantities whose geometry is favorable only jointly.

By contrast, the mixed-Fresnel estimate (4.5) is continuous through `delta=0` and in fact improves as `|delta|` grows. Theorem MF can do this because its hypothesis and conclusion are uniform in the heavy-heavy block `A_HH`; it integrates the physical hub against its original density **before** destroying the leaf-product amplitude.

The partner's cap-only counterexample remains fully relevant: it shows that one cannot recover this interpolation merely from a bounded joint density for a projected receiver. The successful interpolation here is source-valid precisely because the full original-coordinate product factorization survives in the augmented rows `(c_delta a_j,b_j)`.

## 7. First unpaid implication after this run

The surviving full-target debt is not the exact same-bank packet above; that packet is paid uniformly by (4.5). The next structural bridge is:

`QFORM-N3-APPROXIMATE-SAME-BANK-HUB-ROUTING-v1`.

In the strict N3 class, show that a leverage-heavy near-null physical coordinate whose pair minors are individually tiny either

1. generates, on a large original-coordinate leaf set, a quantitatively nondegenerate augmented Gram matrix for the **actual** hub-coupling vector together with one residual square/direction, so Theorem MF applies before any Schur completion; or
2. routes into an already-paid determinant-pair, D'/D5, finite-core, or grouped-bank branch.

The proof must tolerate overlap of the two projected leaf directions, as (1.1) demonstrates; disjoint source banks are not necessary and cannot be assumed. It also must not shear `X_0` by a leaf linear form and then pretend the new variable is independent. The designated partner's r20 obstruction shows that replacing this product-linear provenance by a receiver-side joint-density cap cannot close the interpolation.

This is a narrower and source-compatible N3 routing problem. Full QFORM remains OPEN.
