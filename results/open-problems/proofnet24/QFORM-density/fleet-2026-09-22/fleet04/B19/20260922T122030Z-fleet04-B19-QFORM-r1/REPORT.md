# Universal assembly: compact product-set core and the exact remaining trace inequality

**Run:** `20260922T122030Z-fleet04-B19-QFORM-r1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet04/B19, universal proof assembly  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and corrections

The target is uniform in the dimension, the independent one-dimensional laws, and the real symmetric matrix: each input density is only assumed to satisfy `0<=f_i<=1`, and the matrix has at least three eigenvalues of modulus at least one. No moments, connected supports, compact supports, log-concavity, or independence after an eigenvector rotation are assumed.

This report consumes the current corrections. In particular, pointwise law-uniform quadratic Fourier decay is false; an unrestricted spectral-fiber supremum loses dimension; a bounded projected density alone does not control an indefinite quadratic pushforward; one cross minor alone is insufficient; and a probability density with a generic line-X-ray cap can still concentrate in a thin indefinite quadratic shell. The correction inbox also records that `C=pi` is false and every universal constant is at least `3 sqrt(2)`.

## 2. New target-level theorem: compact finite-union product sets are an exact testing core

Let

`D={f:R->[0,1] measurable : int f=1}`.

For a measurable map `Phi:R^n->R` define the concentration seminorm

`K(Phi)=sup_{f_1,...,f_n in D} sup_{I interval, |I|>0}
          [int 1_{Phi(x) in I} prod_i f_i(x_i) dx]/|I|.`

Let `U_fin` be the class of bounded finite unions of intervals in `R` having total measure one.

### Theorem `QFORM-FINITE-UNION-CORE-v1`

For every measurable `Phi`,

`K(Phi)=sup_{E_1,...,E_n in U_fin} sup_I
 |{x in prod_i E_i : Phi(x) in I}|/|I|.`

Consequently the full quadratic-form conjecture is equivalent, with exactly the same constant, to the geometric estimate

`|{x in prod_i E_i : x^T A x in I}| <= C |I|`

for every admissible `A`, interval `I`, and bounded finite unions `E_i` of total length one.

This statement has two important quantifier consequences.

1. Compact support may be used as a *testing core* without being silently assumed in the theorem.
2. If the conjecture is false, then for every proposed constant `C` there is a counterexample with every input density equal to the indicator of a bounded finite union of intervals. Thus a genuine counterexample never requires an irreducibly noncompact or non-bang-bang input law.

### Proof

The completed fleet01/B18 product-set theorem gives, for every fixed measurable event `B`,

`sup_{f_i in D} int 1_B prod_i f_i
 =sup_{|E_i|=1} |B intersect prod_i E_i|`,

where the sets on the right are arbitrary measurable sets of measure one. It follows by applying the bathtub principle in one coordinate at a time; no compactness or existence of a maximizer is needed because suprema are used.

It remains to replace arbitrary unit-measure sets by bounded finite unions. Fix measurable `E` with `|E|=1`. Lebesgue regularity gives bounded finite unions of intervals `F_m` with `|E triangle F_m|->0`. By trimming or adjoining one interval disjoint from the existing union, we may also impose `|F_m|=1` while retaining convergence in symmetric difference.

For product indicators, telescope one coordinate at a time:

`|| prod_i 1_{E_i} - prod_i 1_{F_i} ||_1
 <= sum_i |E_i triangle F_i|.`

Hence the probability of every fixed measurable event, in particular `{Phi in I}`, converges under simultaneous finite-union approximation. Therefore the supremum over arbitrary unit-measure product sets is no larger than the supremum over `U_fin`; the reverse inequality is immediate. Taking the supremum over intervals proves the theorem. `QED`

### Density consequence

If the common concentration seminorm is finite, the pushforward measure satisfies `mu(I)<=C|I|` for every interval. Outer regularity and interval coverings imply `mu(B)<=C|B|` for every Borel set, so `mu` has a Radon--Nikodym density bounded by `C`. This proves only an essentially bounded representative. Continuity requires an additional argument and is not claimed here.

## 3. Actual application of the curved-fiber theorem

Choose two same-sign eigenvalues among three large eigenvalues. Write their spectral plane as `V`, their magnitudes as `a,b>=1`, and the sign as `sigma`. For a finite-union product set `D=prod_i E_i`, put `F=1_D`. Thus `0<=F<=1`, `int F=1`, and no limiting or smoothness hypothesis is present.

Apply fleet03/B06's completed elliptic-energy compression theorem to

`H(z,s)=int_V delta(s-a u^2-b v^2) F(z+u e_1+v e_2) du dv.`

For every `1<=p<infinity`, this gives the actual inequality

`int_{V^perp} int_0^infinity H(z,s)^p ds dz
 <= pi^(p-1) (ab)^(-(p-1)/2) <= pi^(p-1).`

In particular,

`||H||_1=1,   ||H||_2^2<=pi,   ||H||_infinity<=pi.`

This is not a citation-only use: the finite-union reduction inserts the exact extremal input `F=1_D` into the peer theorem and shows that the entire arbitrary-density target reaches the same dimension-free energy budget by approximation.

Writing the remaining spectral quadratic as `q_perp`, the output density, when it exists, is the trace

`p_Q(t)=int_{V^perp} H(z, sigma(t-q_perp(z)))
                   1_{sigma(t-q_perp(z))>=0} dz.`

Therefore the full conjecture follows from the following single finite-union trace estimate:

### `QFORM-PRODUCT-ELLIPTIC-TRACE-v1` (open)

For every finite-union product indicator `F`, every spectral plane `V` coming from two same-sign eigenvalues `a,b>=1`, and every complementary quadratic form containing at least one eigenvalue of modulus at least one,

`sup_t int_{V^perp} H(z, sigma(t-q_perp(z)))
        1_{sigma(t-q_perp(z))>=0} dz <= C_tr`

with a universal constant.

The preceding theorem proves that it is enough to establish this trace inequality for compact finite-union rectangles. Passing to arbitrary measurable supports and then arbitrary bounded densities is automatic and constant-preserving.

## 4. Compact conditional end-to-end proof

For reference, the strongest current proof can now be stated without hidden quantifier gaps.

1. Reduce every interval probability exactly to product indicators of bounded finite unions by `QFORM-FINITE-UNION-CORE-v1`.
2. If `A` is diagonal in the physical independent coordinates, use the two-same-sign beta integral to obtain the sharp control `pi` for that branch.
3. If an original-coordinate nonsingular `3 x 3` block has least singular value `kappa`, condition outside it and use the proved bound `(2pi+3sqrt(3))/kappa`; the analogous `4 x 4` bound is `(pi^2+8)/kappa`.
4. If an original-coordinate partition has cross block of rank `r>2` and nonzero singular-value product `Delta`, use the proved cross-block Fourier theorem

   `||p_Q||_infinity <= [2r/(r-2)] Delta^(-1/r)`,

   which also gives a continuous density.
5. In exact rank three, if the eigenframe has maximum row leverage at most `1/12`, the proved partition argument gives `||p_Q||_infinity<=24`, continuously.
6. The newer fleet03/B19 spectral--Schur theorem strengthens the exact-rank-three assembly. It proves every definite rank-three form has density at most `3e`. For an indefinite rank-three form, if a physical row `v` of leverage `c=|v|^2` has nonzero Rayleigh pivot `a=v^T Lambda v` of the minority inertia sign, then

   `||p_Q||_infinity <= 2 sqrt(2pi) (|a|c|det Lambda|)^(-1/4)`.

   This follows from the exact identity `pdet(T)=c det(Lambda)/a` for the residual spectral Schur complement and the dependent square-smoothing theorem. It is a closed branch at every quantitatively nonisotropic minority pivot.
7. In every remaining case choose a same-sign spectral plane and invoke the exact energy bounds in Section 3. The sole universal analytic gap is `QFORM-PRODUCT-ELLIPTIC-TRACE-v1` (or a different estimate implying it). Already in pure rank three, its first concrete manifestation is the localized indefinite majority-pivot/near-isotropic branch. With `c>1/2`, the exact cross-energy identity gives

   `sum_{j!=i} A_ij^2=|Lambda v|^2-a^2 >= c-a^2`.

   Thus `|a|<=1/2` forces at least `1/4` total squared cross coupling, but converting this aggregate into a product-law density bound remains open. Arbitrary additional spectral directions create a separate interaction/truncation debt and are not discarded.

All signatures are included because three large eigenvalues always contain a same-sign pair. Repeated eigenvalues cause no degeneracy; zero and small remaining eigenvalues are absorbed into `q_perp`. Arbitrary additional eigenvalues and all cross terms remain present. Steps 2--6 are genuine closed branches at their stated hypotheses, not claims that every matrix satisfies those extra hypotheses.

## 5. Why the trace step is genuinely first

The ambient estimates `||H||_1=1`, `||H||_2^2<=pi`, and `||H||infinity<=pi` do not control restriction to a codimension-one graph for a generic function `H`. Likewise, the bounded three-dimensional spectral projection density from Livshyts--Paouris--Pivovarov cannot be substituted: explicit unit-volume densities may concentrate in arbitrarily thin indefinite quadratic shells. The needed estimate must retain that `H` is the circular/elliptic average of a product-set indicator in the original coordinates. The spectral--Schur theorem shows exactly where generic coarea stops being enough: after a localized majority-sign pivot the residual rank-two quadratic is indefinite; its level sets have infinite area, so its bounded two-dimensional projection density alone cannot pay the square-smoothing hypothesis.

The finite-union core sharpens this obligation: no tail truncation, smooth approximation, or moment estimate remains part of the missing implication. What is missing is purely a uniform product-geometric trace estimate on compact semialgebraic pieces, with the number and location of the one-dimensional components arbitrary.

## 6. Status

**Proved here:** `QFORM-FINITE-UNION-CORE-v1`, including the constant-preserving equivalence, the finite-union counterexample consequence, and the essentially-bounded-density deduction.

**Completed peer theorems actually applied:** fleet01/B18's exact product-set extremal reduction and fleet03/B06's elliptic-energy `L^p` compression, yielding the explicit `L^1/L^2/L^infinity` inequalities above for the extremal finite-union inputs; and fleet03/B19's spectral--Schur identity combined with dependent square smoothing in the localized rank-three branches. The designated fleet01/B19 partner had no completed QFORM report at the final prepublication check, so no start-only claim was borrowed.

**Not proved:** `QFORM-PRODUCT-ELLIPTIC-TRACE-v1`, continuity in the universal residual branch, or the full conjecture. The current universal lower bound is `3 sqrt(2)`; the earlier proposed universal value `pi` is false.

## 7. Source pins

- Owner control: `yspennstate/math-research-brain`, revision `2026-09-22.5`, README blob `433b2d57345823967480245b59a7c47d51019c37`.
- fleet01/B18 product-set reduction: `yspennstate/math-open-problems@a195041a2ae61f69a67c8dae86d56675b4b1374f`.
- fleet03/B06 elliptic-energy compression: `yspennstate/math-open-problems@18e6593354456a8d90385eafe61f205a9a9b956b`.
- fleet03/B19 localized spectral--Schur assembly: `yspennstate/math-open-problems@5a84b253fe14acc142ebdd26717d2e267dd95ebc`.
- Cross-block/diffuse/lower-bound assembly: `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`.
- Current correction inbox blob at final refresh: `1681679e291cfd73917b46a25dc5bc8584d40bec`.

No native brain retrieval was used. Repository transport and theorem application are recorded separately.
