# account03/B08 — fractional-ridge extension of the diffuse selected-eigenspace branch

**Run:** `20260922T154922Z-account03-B08-qform-diffuse-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full target remains open: for every dimension, every independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of magnitude at least one, prove a single universal bound for the density of `Q=X^TAX`, or give a valid counterexample. Continuity is a separate desired conclusion.

This run does not use the refuted law-uniform pointwise quadratic-phase decay, does not rotate the product law and declare the eigen-coordinates independent, and does not use an unrestricted fiber supremum. It also does not infer a universal fixed cross-rank-three cut from the spectral hypothesis.

The analytic engine is the complete one-scale ridge theorem `QFORM-RIDGE-DENSITY-v1` at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

path

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an original-coordinate cross block `B=A[I,J]`, ridge scale `gamma>0`,

`K=B B^T (gamma^2 I+B B^T)^(-1)`, `theta=tr K`,

if `1<=q<=2`, `max_i K_ii<=q/2`, and `theta>2q`, then the full quadratic form, with arbitrary self blocks and outside couplings, has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.

Its perturbation lemma says: if `B=B0+F`, `||F||<=eta`, and the range projection of `B0` has diagonal at most `ell`, then

`max_i K_ii <= [sqrt(ell)+eta/gamma]^2`.

The fresh account01/B08 report `QFORM-ROBUST-SEPARATOR-RIDGE-v1` at the current archive proves the corresponding selected-frame separator mechanism with the endpoint choice `q=1`. The present run changes mechanism by using the **fractional exponent `q>1`** to open a quantitatively larger selected-eigenspace leverage region which the `q=1` perturbative criterion cannot certify.

The designated partner `account04/B08` still has no completed current-QFORM handoff on the fresh shared path, so no theorem is attributed to that worker. To satisfy asynchronous mathematical reuse rather than wait, Section 5 also applies the completed account04/B16 theorem `QFORM-CONDITIONAL-HEAVY-RAYLEIGH-HALF-v1`, source `yspennstate/math-open-problems@d6150b6de22e898de442e821e42c2ddc09604a0d`, to an explicit complementary rank-three branch.

## 2. Elementary signed partition lemma

Let `R` be an `n x r` real matrix with orthonormal columns, rows `r_i^T`, and

`mu=max_i ||r_i||^2`.

Assume `r mu<1`. Then there is a partition of the **original physical coordinates** into `I union J` such that

`R_I^T R_I >= alpha I_r`, `R_J^T R_J >= alpha I_r`,

where

`alpha=(1-sqrt(r mu))/2`.

### Proof

Let `epsilon_i` be independent Rademacher signs and

`S=sum_i epsilon_i r_i r_i^T`.

Then

`E ||S||_F^2 = sum_i ||r_i r_i^T||_F^2 = sum_i ||r_i||^4 <= mu sum_i ||r_i||^2 = r mu`.

Hence one sign realization satisfies `||S||op<=||S||F<=sqrt(r mu)`. Let `I={i:epsilon_i=+1}`, `J={i:epsilon_i=-1}`. Since `sum_i r_i r_i^T=I_r`,

`R_I^T R_I=(I_r+S)/2`, `R_J^T R_J=(I_r-S)/2`,

so both are at least `alpha I_r`. QED.

This proof is finite-dimensional, product-structure preserving, and uses no probabilistic assumption on the input variables.

## 3. General fractional-ridge selected-subspace theorem

### Theorem — `QFORM-FRACTIONAL-RIDGE-DIFFUSE-SPECTRAL-GAP-v1`

Let

`A = R Lambda R^T + E`,

where `R^T R=I_r`, `r>=3`, `Lambda` is real symmetric with every singular value at least one, and `||E||op<=eta`. In the spectral application, `R` spans an invariant spectral subspace with `|lambda|>=1` and `E` is the orthogonal spectral remainder. Put

`mu=max_i ||r_i||^2`,
`alpha=(1-sqrt(r mu))/2`,
`sigma=alpha-eta`.

Assume `r mu<1` and `sigma>0`. Define

`kappa = [sqrt(mu/alpha) + sqrt(6) eta/sigma]^2`.

If there exists `q in [1,2]` such that

`kappa <= q/2`,
`6r/7 > 2q`,

then for every admissible independent cap-one product law, `Q=X^TAX` has a bounded continuous `C_0` density satisfying

`||p_Q||_infinity
 <= [3r/(3r-7q)] * sqrt(3e/q) / sigma`.                         (3.1)

No moment, support, sign, or post-rotation independence assumption is used.

### Proof

Choose the physical partition `I|J` from Section 2 and set

`G_I=R_I^T R_I`, `G_J=R_J^T R_J`.

Both are at least `alpha I_r`. The selected cross block is

`B0=R_I Lambda R_J^T`.

Write `R_I=Q_I G_I^(1/2)` and `R_J=Q_J G_J^(1/2)`, where `Q_I,Q_J` have orthonormal columns. The nonzero singular values of `B0` are the singular values of

`G_I^(1/2) Lambda G_J^(1/2)`.

Therefore

`s_r(B0)>=alpha`.

Moreover, because the middle factor is invertible,

`range(B0)=range(R_I)`.

The diagonal leverage of this range at coordinate `i in I` is

`r_i^T G_I^(-1) r_i <= mu/alpha`.

The actual full cross block is

`B=A[I,J]=B0+F`, `F=E[I,J]`,

and `||F||op<=eta`. Weyl's singular-value perturbation inequality gives

`s_r(B)>=alpha-eta=sigma`.

Set

`gamma=sigma/sqrt(6)`.

The ridge perturbation lemma gives

`max_i K_ii <= [sqrt(mu/alpha)+eta/gamma]^2 = kappa <= q/2`.

Also, since `B` has at least `r` singular values at least `sigma`,

`theta=tr K
 >= r sigma^2/(gamma^2+sigma^2)
 =6r/7 >2q`.

The one-scale ridge theorem therefore applies. Using its coarse determinant-free estimate,

`||p_Q||infinity
 <= sqrt(e)/(sqrt(2q) gamma) * theta/(theta-2q)`.

The function `x/(x-2q)` decreases for `x>2q`, so substituting `theta>=6r/7` and `gamma=sigma/sqrt(6)` gives

`||p_Q||infinity
 <= sqrt(3e/q)/sigma * [6r/(6r-14q)]
 = [3r/(3r-7q)] sqrt(3e/q)/sigma`,

which is (3.1). The source ridge theorem supplies the `L^1` characteristic-function majorant, hence continuity and vanishing at infinity. QED.

## 4. New explicit branch beyond the q=1 perturbative frontier

Take `r=3` and assume

`||E||op <= 1/64`,
`max_i ||r_i||^2 <= 169/1875`.

Because

`sqrt(3*(169/1875)) = 13/25`,

we have

`alpha >= (1-13/25)/2 = 6/25`,
`sigma >= 6/25 - 1/64 = 359/1600`,
`mu/alpha <= 169/450`.

Set `q=5/4`. Then

`kappa
 <= [13/(15 sqrt(2)) + 25 sqrt(6)/359]^2
 = 169/450 + 3750/128881 + 130 sqrt(3)/1077`.

Using `sqrt(3)<7/4`,

`kappa
 < 169/450 + 3750/128881 + 455/2154
 = 17859632/28998225
 < 5/8 = q/2`.

The last strict gap is

`5/8 - 17859632/28998225
 = 2114069/231985800 >0`.

Also

`theta >= 18/7 > 5/2 = 2q`.

Thus (3.1) gives the explicit continuous-density estimate

`||p_Q||infinity
 <= (57600/359) sqrt(12e/5)
 = 409.8084383... <410`.                                            (4.1)

This is a genuine fractional-`q` extension of the prior `q=1` perturbative mechanism. Indeed, in the same worst-case parameter corner, any `q=1` rank-three application requires `tau<1/sqrt(2)` in `gamma=tau sigma` to keep `theta>2`. Even at the best limiting value `tau -> 1/sqrt(2)`, its leverage upper bound has square root strictly larger than `1/sqrt(2)` because

`13/(15 sqrt(2)) + 25 sqrt(2)/359
 = sqrt(2) [13/30 + 25/359]
 = sqrt(2) [1/2 + 16/5385]
 >1/sqrt(2)`.

Hence the `q=1` perturbative criterion cannot certify this endpoint, while `q=5/4` does. The mechanism change is therefore mathematical rather than a relabeling of the previous run.

Interpretation: if the three selected `|lambda|>=1` eigenvectors are delocalized to row leverage at most about `0.09013`, and every complementary eigenvalue has magnitude at most `1/64`, then the exact universal target conclusion holds on this branch with a continuous density and explicit constant `<410`, regardless of signs, dimension, or input supports.

## 5. Applying completed account04 mathematics: a complementary rank-three branch

For comparison, suppose `E=0` and `r=3`, so `A` itself has rank exactly three with all three nonzero eigenvalues of magnitude at least one. The completed account04/B16 theorem applies when there is a physical row `i` whose range leverage `c=||r_i||^2` is the unique leverage above `1/2` and whose physical diagonal obeys `|A_ii|>=1/4`. It yields directly

`||p_Q||infinity <= 2^(13/4) sqrt(e) <15.69`,

with essential boundedness (continuity is not asserted by that theorem).

Combining the two proven inequalities gives a concrete rank-three phase map:

* diffuse rows `max_i ||r_i||^2 <=169/1875` are covered continuously by the fractional-ridge mechanism (with the sharper `E=0` constants obtainable from (3.1));
* a unique strongly localized row `c>1/2` with `|A_ii|>=1/4` is covered by the account04/B16 square/half-order mechanism.

The unresolved rank-three region is therefore concentrated in intermediate/multi-heavy leverage configurations and heavy near-isotropic rows with small physical Rayleigh value. This is not a full rank-three proof and is not claimed as one.

## 6. What remains for the full conjecture

The new theorem still assumes a spectral-gap/small-remainder branch. In the unrestricted target, the complement of the three selected large eigenvectors may itself contain arbitrarily many eigenvalues of arbitrary magnitude and sign. Treating that complement only as an adversarial operator-norm perturbation cannot close the theorem.

The next B08 mechanism should exploit the ridge theorem without paying the full remainder norm: at a physical cut, a large remainder can only be harmful to selected-space leverage if it also contributes ridge effective dimension. The desired next dichotomy is therefore:

`QFORM-LARGE-DEFECT-RIDGE-CHARGE-v1` — either the actual cross block already has `theta_gamma>2q` with admissible ridge diagonal and closes by the ridge theorem, or the failure of that certificate yields a quantitatively low-effective-dimension remainder which can be passed to an aggregate bank/star or localized-coordinate mechanism.

The full universal QFORM conjecture remains **OPEN / NOT PROVED**.

## 7. Verification scope

The companion checker verifies the exact rational/radical inequalities in Section 4 and the constant in (4.1). It is regression evidence for arithmetic only; the analytic proof is the argument above plus the cited complete ridge theorem.
