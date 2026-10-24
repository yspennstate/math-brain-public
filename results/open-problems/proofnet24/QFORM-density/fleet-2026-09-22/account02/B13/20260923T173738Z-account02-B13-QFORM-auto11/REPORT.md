SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-23T17:37:38Z.
attacking: the latest partner's diagonal-plus-rank-eight / small-Frobenius-twist survivor by an exact slab-pair residual-energy inequality, while keeping arbitrary fragmentation and the genuine twist.

# account02/B13 — exact residual-energy pair counting after the rank-eight Frobenius reduction

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Role: extremal product laws / complementary constructions.  
Designated partner: account03/B13.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: **NEW SUPPORTING TARGET-LEVEL IMPLICATIONS / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

All random coordinates below are ORIGINAL physical coordinates. Deterministic spectral decompositions are used only on coefficient matrices. No moment, support, connectedness, log-concavity, centered-uniform, post-rotation-independence, or perturbative deletion assumption is introduced.

## 0. First unpaid implication

The first remaining B13 implication after this report is

`QFORM-SCALEFREE-FROBENIUS-TWIST-GLUE-v1`:

> In the latest partner's high-ratio decomposition `A=D+R+E`, `rank R<=8`, `||E||_F=O(rho^-1)`, close the branches in which either `rank R<=2`, the range of `R` has a physical leverage above `1/2`, or the nonzero determinant scale of `R` is `O(rho^-1)`; and in the complementary diffuse/nondegenerate branch exploit the exact residual-energy pair separation proved below rather than assuming a support diameter or deleting `E`. Otherwise construct a genuine unit-product-indicator counterexample sequence whose slab-conditioned pairs have the forced scale-free separation while every physical fifth exterior volume simultaneously collapses.

The point is that the partner's former vague “large core spread” alternative is converted below into a precise two-copy inequality in the **actual residual quadratic energy**. Euclidean spread is only a corollary, so exact null directions are not falsely charged.

## 1. Fresh source-pinned inputs actually used

### 1.1 Latest completed compatible designated partner: aggregate E3 and rank-eight Frobenius reduction

Account03/B13 r30, canonical source

`yspennstate/math-open-problems@feda06c104c0d8c62661daf01eed33c10f55fa99`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T173317Z-account03-B13-qform-r30/REPORT.md`.

It proves, conditional on the source-pinned grouped projected-crossing receiver inherited from r29, that every slab witness of ratio

`rho = P{X^T A X in J}/|J|`

satisfies for every disjoint physical cross block `B=A[L,R]`

`e_3(B^T B) <= (C3/rho)^6`, `C3=9 sqrt(3e)`,                       (1.1)

and, if `rho>C0+2` with `C0=128*2^(1/4)`, admits

`boxed: A=D+R+E,   rank R<=8,   ||E||_F<=K0/rho,`                  (1.2)

where `D` is diagonal, `E` is zero-diagonal and

`K0=72 C3^3=1,222,316.3743601379...`.                              (1.3)

Its sharper Case B gives

`rank R<=4,   ||E||_F<6/rho`                                      (1.4)

when `V_2(A)<rho^-4<=V_1(A)`. The partner explicitly leaves (1.2) as a genuine twist: it is not deleted on unbounded product laws.

The r30 report states its dependency status precisely: the aggregate-E3/rank-eight theorem still inherits the not-yet-independently-reviewed grouped projected-crossing receiver. I preserve that condition rather than upgrading its review status.

### 1.2 Exact diffuse range-curvature receiver with arbitrary diagonal twists

Account01/B13,

`yspennstate/math-open-problems@9d9e2369ad137664a48b1b7c6d682ddaed62bcad`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T125929Z-account01-B13-qform-auto23/FRESNEL_RANGE_ADDENDUM.md`.

If `R` is symmetric of rank `d>=3`, its range projection `P_R` obeys

`max_j (P_R)jj <=1/2`,                                             (1.5)

and `D` is any diagonal matrix, then for independent cap-one original coordinates and every affine term,

`X^T(D+R)X + l^T X + c`

has a continuous density bounded by

`boxed: M_R = [4d/(d-2)] |pdet R|^(-1/d).`                         (1.6)

No transformed random coordinates are declared independent; the deterministic spectral range enters only in the Fourier/Fresnel calculation.

### 1.3 Required pinned Claude/Fourier D5 theorem

At the exact required immutable source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`,

the completed unconditional fifth-volume theorem says that for every disjoint ORIGINAL-coordinate physical cross block `B`,

`boxed: ||p_Q||_infty <= C5 e_5(B^T B)^(-1/10),`

`C5=5 sqrt(2e)=11.6582199079856...`,                               (1.7)

with no volume-marginal condition. The source's `RESULTS.md` and `COUNTEREXAMPLE_SEARCH.md` were also read; the numerical search reports no counterexample, but no numerical evidence is used below.

### 1.4 No-attainment extremal-product transfer

Account04/B13,

`yspennstate/math-open-problems@82f9b7e9372c2434f27fd1f5a65e7148663516a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`,

proves equality of the supremum of every nonnegative product functional over arbitrary cap-one mass-one marginals and over products of unit-measure indicator sets, without asserting attainment. For bounded slab kernels, measurable unit sets can in addition be approximated in measure by bounded finite unions of intervals. There is no common diameter, fragment-count, single-interval, or centered-uniform conclusion.

## 2. Abstract one-centre lemma: subtract the genuine residual around an arbitrary point

Let

`q(x)=x^T(B+E)x+l^T x+c`,                                         (2.1)

where `B,E` are symmetric. Suppose that for the given product law every affine perturbation of the base form

`x^T Bx+a^T x+b`                                                   (2.2)

has density at most `M`, uniformly in `a,b`.

For a deterministic centre `z`, define

`q_z(x)=q(x)-(x-z)^T E(x-z)`.                                     (2.3)

Expansion gives the exact identity

`boxed:
 q_z(x)=x^T Bx+(l+2Ez)^T x+c-z^T E z.
}`                                                                  (2.4)

Therefore (2.2) gives

`||p_(q_z(X))||_infty<=M`                                         (2.5)

**uniformly in the centre `z`**. No smallness of `E` is used in this step.

Let `J` be an interval of length `L>0`, put

`S={q(X) in J}`, `m=P(S)=rho L`.                                  (2.6)

For every `delta>=0`, on

`S intersect {|(X-z)^T E(X-z)|<=delta}`

we have `q_z(X) in J+[-delta,delta]`, an interval of length `L+2delta`. Hence

`boxed:
 P(S and |(X-z)^T E(X-z)|<=delta)
 <=M(L+2delta).
}`                                                                  (2.7)

This is already a support-free one-centre residual localization theorem. Importantly, the residual is measured by the actual quadratic action of `E`, not by a Euclidean radius.

## 3. Main new theorem: exact two-copy residual-energy pair count

Let `X'` be an independent copy of `X`. In (2.7), for each fixed `x'`, choose `z=x'`. Then

`(X-z)^T E(X-z)=(X-X')^T E(X-X')`.                                (3.1)

Integrate the bound (2.7) only over `x'` for which `q(x') in J`. The joint probability is at most

`m M(L+2delta)`.                                                   (3.2)

Dividing by `m^2` proves:

### Theorem 3.1 — `QFORM-AFFINE-UNIFORM-RESIDUAL-PAIR-COUNT-v1`

Under the uniform affine base-density hypothesis (2.2),

`boxed:
 P( |(X-X')^T E(X-X')|<=delta
    | q(X) in J, q(X') in J )
 <= (M/rho)(1+2delta/L).
}`                                                                  (3.3)

This is an exact two-copy inequality inside the bad slab. It has no moments, support radius or continuity assumption on the residual form.

For `0<eta<1`, define the `(1-eta)` lower quantile of residual pair energy by

`Delta_(E,eta)(S)
 =inf{delta>=0:
      P(|(X-X')^TE(X-X')|<=delta | X,X' in S)>=1-eta}.`            (3.4)

Then (3.3) implies

`boxed:
 Delta_(E,eta)(S)
 >= (L/2) ( ((1-eta)rho/M)-1 )_+.
}`                                                                  (3.5)

At the median (`eta=1/2`),

`boxed:
 Delta_(E,1/2)(S)
 >= (L/2) (rho/(2M)-1)_+.
}`                                                                  (3.6)

If `E=0`, the left side of (3.3) is one already at `delta=0`, so the theorem immediately returns the direct payment `rho<=M`. Thus no fictitious spread branch survives in the exact-base endpoint.

### Cross-law form

The same proof works for two possibly different cap-one product laws `mu,nu`. If their slab ratios are `rho_mu,rho_nu` and the same affine-uniform base bound `M` holds for both, then

`P_(mu x nu)( |(X-Y)^TE(X-Y)|<=delta | q(X),q(Y) in J )
 <= M(1+2delta/L)/max(rho_mu,rho_nu).`                              (3.7)

Indeed, conditioning first on `Y` gives the denominator `rho_mu`; swapping the laws gives `rho_nu`, and one takes the smaller upper bound. This version is useful when a no-attainment approximation is expanded into finite convex mixtures.

## 4. Apply the theorem to the latest partner's diagonal-plus-rank-eight survivor

Assume the r30 decomposition (1.2), and suppose

`d=rank R>=3`,
`max_j(P_R)jj<=1/2`.                                               (4.1)

Set

`Lambda_R=|pdet R|^(1/d)`.                                        (4.2)

The account01/B13 theorem (1.6) gives the affine-uniform base bound

`M_R=[4d/(d-2)] Lambda_R^-1 <=12 Lambda_R^-1`,                     (4.3)

because `d>=3`. Apply Theorem 3.1 with

`B=D+R` and residual `E`.

### Theorem 4.1 — `QFORM-RANK8-FROBENIUS-RESIDUAL-PAIR-COUNT-v1`

Subject to the partner r30 dependency and (4.1), every slab witness with `rho>C0+2` satisfies

`boxed:
 P( |(X-X')^TE(X-X')|<=delta | X,X' in S )
 <= (M_R/rho)(1+2delta/L).
}`                                                                  (4.4)

In particular,

`boxed:
 Delta_(E,1/2)(S)
 >= (L/2)(rho/(2M_R)-1)_+
 >= (L/2)(rho Lambda_R/24-1)_+.
}`                                                                  (4.5)

This is the exact residual-energy currency promised by the partner's unresolved “large core spread” branch.

## 5. Frobenius smallness turns residual action into scale-free slab-pair separation

For every vector `y`,

`|y^T E y| <= ||E||op ||y||_2^2 <= ||E||F ||y||_2^2`.             (5.1)

Combine (5.1), (4.5), and the partner bound `||E||F<=K0/rho`. If `r_(1/2)` denotes the median of `||X-X'||_2` conditional on both copies lying in the slab, then

`boxed:
 r_(1/2)/sqrt(L)
 >= [ rho/(2K0) * (rho/(2M_R)-1)_+ ]^(1/2)
 >= [ rho/(2K0) * (rho Lambda_R/24-1)_+ ]^(1/2).
}`                                                                  (5.2)

This statement is dimension-free. It does **not** infer useful residual action merely from Euclidean spread; rather, (4.5) first proves that the actual residual action is large, and (5.1) then forces Euclidean separation because the whole Frobenius norm of `E` is small.

A convenient scale-separated consequence is: if

`rho Lambda_R>=48`,                                                (5.3)

then

`boxed:
 r_(1/2)/sqrt(L)
 >= rho sqrt( Lambda_R/(96 K0) ).
}`                                                                  (5.4)

Thus if `Lambda_R` stays bounded below along a hypothetical sequence with `rho->infinity`, at least half of the slab-conditioned pairs become separated at a distance linear in `rho sqrt(L)`.

### Sharper partner Case B

If the partner's Case B (1.4) occurs, replace `K0` by `6` everywhere. Then

`boxed:
 r_(1/2)/sqrt(L)
 >= [ rho/12 * (rho Lambda_R/24-1)_+ ]^(1/2).
}`                                                                  (5.5)

When `rho Lambda_R>=48`, this simplifies to

`boxed:
 r_(1/2)/sqrt(L) >= rho sqrt(Lambda_R)/24.
}`                                                                  (5.6)

This is a substantially stronger necessary geometry for the rank-at-most-four Frobenius branch.

## 6. The required pinned D5 result gives a simultaneous global fifth-volume obstruction

Now use the owner-required pinned result (1.7) at a second actual inequality. For every disjoint original-coordinate cross block `B=A[L,R]`, either `e_5(B^TB)=0` or

`rho <= C5 e_5(B^TB)^(-1/10)`.

Thus, in all cases,

`boxed:
 e_5(A[L,R]^T A[L,R]) <= (C5/rho)^10.
}`                                                                  (6.1)

Define the global ordered disjoint fifth-minor currency

`V_5(A)=sum_{S cap T=empty, |S|=|T|=5} det A[S,T]^2`.              (6.2)

For a uniformly random Bernoulli partition of the physical coordinates into `(L,R)`, each ordered disjoint `(S,T)` lands with `S subset L`, `T subset R` with probability

`2^-10=4^-5=1/1024`.                                              (6.3)

Cauchy--Binet therefore gives

`E e_5(A[L,R]^T A[L,R])=V_5(A)/1024`.                             (6.4)

Since (6.1) holds for every cut,

### Theorem 6.1 — `QFORM-PINNED-D5-GLOBAL-V5-SLAB-v1`

`boxed:
 V_5(A) <= 1024 (5 sqrt(2e)/rho)^10.
}`                                                                  (6.5)

This theorem is unconditional on the partner r30 projected-crossing dependency: it follows directly from the required pinned D5 theorem and the random physical partition identity. In a hypothetical counterexample sequence `rho_m->infinity`, the complete ordered disjoint fifth exterior currency is therefore `O(rho_m^-10)`.

The pinned counterexample search reports no valid counterexample in the families it tested. I use none of those numerics as proof.

## 7. Extremal-product interpretation without an attained optimizer

The pair-count theorem was proved directly for arbitrary cap-one product laws, so it does not require an extremizer. For the complementary-construction role it is nevertheless useful to record the precise finite-union form.

Fix a strict slab witness with ratio `rho_0`. The account04/B13 no-attainment theorem produces, for every `epsilon>0`, a product of unit-measure indicator sets with the same matrix and slab and ratio at least `rho_0-epsilon`. A measurable unit-measure set on the line can be approximated in symmetric-difference measure by a bounded finite union of intervals; adjust the last interval by an arbitrarily small amount to keep total measure exactly one. Since the slab kernel is bounded by one,

`| int K prod_i 1_(E_i) - int K prod_i 1_(F_i) |
 <= sum_i |E_i triangle F_i|`.                                    (7.1)

For the two-copy bounded pair event the analogous error is at most twice the right side. Hence every strict slab-ratio / pair-energy violation transfers, with arbitrarily small loss, to bounded finite-union unit-product indicators.

This is an approximation statement, not an attained global bathtub optimizer. The support diameters and fragment counts may diverge with the approximation; separated and originally unbounded supports remain allowed. No singular Riesz kernel is passed through bare total variation.

For such a purified witness Theorem 4.1 becomes the geometric statement

`|{(x,y) in S_B x S_B:
    |(x-y)^T E(x-y)|<=delta}| / |S_B|^2
 <= (M_R/rho_B)(1+2delta/L)`,                                     (7.2)

where

`S_B={x in prod_i E_i: x^T A x in J}`,
`|S_B|=rho_B L`.                                                   (7.3)

Thus the surviving product-set problem is now explicit: a high-ratio finite-union slab must have low residual additive energy at every scale below (4.5), while (6.5) simultaneously kills all global physical fifth exterior volume.

## 8. A source-valid obstruction for every diverging counterexample sequence

Subject to the single partner r30 dependency stated in Section 1.1, any target-valid sequence with slab ratios `rho_m->infinity` has

`A_m=D_m+R_m+E_m`,
`rank R_m<=8`,
`||E_m||F=O(rho_m^-1)`,                                           (8.1)

and also, unconditionally from pinned D5,

`V_5(A_m)=O(rho_m^-10)`.                                          (8.2)

Whenever along a subsequence

`rank R_m>=3`,
`max_j(P_(R_m))jj<=1/2`,
`Lambda_(R_m) rho_m ->infinity`,                                  (8.3)

the slab-conditioned pair energy obeys

`Delta_(E_m,1/2)/|J_m| ->infinity`,                               (8.4)

and more quantitatively the Euclidean pair scale obeys (5.2). If `Lambda_(R_m)` stays bounded below, then

`median(||X_m-X'_m||_2 | both in slab)/sqrt(|J_m|)=Omega(rho_m)`. (8.5)

Therefore any genuine counterexample sequence must escape the diffuse/nondegenerate low-rank model through at least one of the following mechanisms:

- rank of `R_m` eventually at most two;
- a physical coordinate has range leverage `>1/2`;
- `Lambda_(R_m)=O(rho_m^-1)` (or otherwise small enough that the affine-uniform receiver becomes weak);
- or the purified product slabs exhibit the quantitatively forced residual-energy / pair-separation geometry (4.5)--(5.2).

This is a reduction, not a proof of the full theorem. The last bullet cannot be ruled out by imposing a hidden support diameter; it is exactly where fragmented/unbounded product geometry must now be used.

## 9. Why this improves the previous B13 max-norm-twist obstruction

The preceding B13 run produced an at-most-four-hub, rank-at-most-four skeleton with an entrywise twist of size `O(rho^-1)` (and `O(rho^-3/2)` when a physical off-diagonal scale stayed fixed). That was useful algebraically but still left a dimension factor if one tried to convert coefficient smallness into a quadratic-error estimate.

The newest partner r30 supplies the stronger global Frobenius bound (1.2). Equation (5.1) therefore pays the residual quadratic error with **no dimension factor**. The present pair-count argument uses this only after proving the exact affine-uniform identity (2.4); it never erases `E`. The rough-support obstruction has consequently been narrowed from “small coefficients might be amplified” to the explicit low-additive-energy condition (7.2).

## 10. Scope and integrity

The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Full continuity remains separate. The partner rank-eight reduction is carried with its stated conditional dependency on the grouped projected-crossing receiver. The global D5 obstruction (6.5) is independent of that dependency.

No arbitrary-joint coarea bound, conditional-density supremum shortcut, post-rotation independence, pointwise law-uniform quadratic oscillatory decay, moment, support, log-concavity, interval extremality, uniform fragment count, or perturbative deletion of the Frobenius-small twist is used.

The next mathematics should attack `QFORM-SCALEFREE-FROBENIUS-TWIST-GLUE-v1`, preferably by converting (7.2) plus `V_5=O(rho^-10)` into a product-geometric contradiction or into a concrete finite-union counterexample sequence. The rank-`<=2`, high-leverage and small-`Lambda_R` exits must be routed through the existing physical hub/pivot receivers rather than hidden by a spectral rotation.
