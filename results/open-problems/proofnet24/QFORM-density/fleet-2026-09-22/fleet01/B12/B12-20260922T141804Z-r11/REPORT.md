# fleet01/B12 — cancellation-resistant control of arbitrary extra eigenvalue directions

**Run:** `B12-20260922T141804Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** Additional eigenvalue control  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

The unrestricted conjecture remains **OPEN**. The results below control two concrete ways of adding arbitrarily small or arbitrarily large eigenvalues, of either sign, without ever rotating the independent coordinates.

## 1. Exact sources consumed

The current target is: for independent real coordinates with densities bounded by one and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal bound for the density of `X^T A X`; continuity is tracked separately.

I use two source-valid completed results.

1. **Regularized cross-block determinant theorem.** Canonical proof:

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For every original-coordinate cut `I,J`, with `B=A[I,J]`, it proves unconditionally

`|phi_A(t)| <= det(I + 4 t^2 B B^T/(pi^2 e^2))^(-1/8)`.          (1.1)

The two self blocks, all outside couplings, signs, and arbitrary measurable self phases are already absorbed by the proof. Hence if `B` has `r>4` singular values at least `sigma`,

`||p_A||_infinity <= C_r/sigma`,                                  (1.2)

where

`C_r = (e sqrt(pi)/4) Gamma(r/8-1/2)/Gamma(r/8)`                  (1.3)

and, more simply,

`C_r <= e r/[2(r-4)]`.                                            (1.4)

The resulting density is continuous and vanishes at infinity.

The same source gives a stronger `q=1` estimate when the relevant cross-block range leverage is at most `1/2`: three cross singular values `>=sigma` then give

`||p_A||_infinity <= 3e/(sqrt(2) sigma)`.                          (1.5)

Its MSS corollary says that if a base matrix `A0=U Lambda U^T` has its entire range frame satisfying `max_i ||u_i||^2<=1/32`, then there is a physical partition `I,J` for which

`s_j(A0[I,J]) >= (7/32) s_j(Lambda)` for every j,                 (1.6)

and the cross-range leverage is at most `1/7`.

2. **Named partner `fleet02/B12`.** Canonical proof:

`yspennstate/math-open-problems@5924039504a3f27bdfa9079c4d054422a26baaf2:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`.

If a physical `m x m` symmetric block (`m>=4`) has at least `m-1` eigenvalues all `>=L` or all `<=-L`, while the remaining eigenvalue is arbitrary, then independent density-`<=1` coordinates plus every affine tilt have density

`||p||_infinity <= C_same/L < 24.193/L`.                           (1.7)

I apply (1.7) in Section 5 below to an actual arbitrary-magnitude rank-one spectral addition.

## 2. New theorem A: block-diagonal spectral additions are free across a certified cut

### Theorem A — `QFORM-CROSS-CERTIFICATE-BLOCK-DIAGONAL-STABILITY-v1`

Let `A0` be any real symmetric matrix and let `I,J` be disjoint original-coordinate sets. Suppose its cross block

`B0=A0[I,J]`

has at least three singular values at least `sigma>0`, and suppose the range projection on one physical side has coordinate diagonal at most `1/2` (the exact leverage hypothesis of the `q=1` source theorem).

Let `R` be **any** real symmetric perturbation satisfying only

`R[I,J]=0`.                                                       (2.1)

There is no restriction on `rank(R)`, `||R||`, its signs, its number of nonzero eigenvalues, or its eigenvalue magnitudes. Then for

`A=A0+R`

the law of `X^T A X` has a continuous density vanishing at infinity and

`||p_A||_infinity <= 3e/(sqrt(2) sigma)`.                          (2.2)

#### Proof

Across the same original-coordinate cut,

`A[I,J]=A0[I,J]+R[I,J]=B0`.

Thus both the cross singular values and the cross-range leverage are exactly unchanged. The regularized determinant theorem is explicitly uniform over the two self quadratic phases and over all outside couplings. Therefore the entire perturbation `R` is absorbed into those arbitrary self/outside phases and (1.5) applies verbatim. QED.

This is a true additional-eigenvalue theorem: an arbitrary number of extra eigenvalues, arbitrarily small or arbitrarily large and of either sign, may be inserted as long as their aggregate perturbation is block diagonal with respect to one already-certified physical cut. No convolution or independence of spectral coordinates is asserted.

### Diffuse-base corollary

Let `A0=U Lambda U^T` satisfy the full-range leverage condition `max_i ||u_i||^2<=1/32`, and suppose `A0` has three eigenvalues of magnitude at least `L`. Take the MSS partition from (1.6). For **every** symmetric `R` with `R[I,J]=0`, regardless of its rank or spectrum,

`||p_{X^T(A0+R)X}||_infinity <= 96e/(7 sqrt(2) L) < 27/L`.        (2.3)

The density is continuous and vanishes at infinity.

So the new determinant proof is stable under fully dense within-bank quadratic additions, not merely coordinate-separable diagonal additions.

## 3. New theorem B: arbitrary rank-k cross additions spend at most k cross singular directions

The next statement removes even the zero-cross condition at the price of a finite cancellation budget.

### Lemma 3.1 — singular-value cancellation budget

For arbitrary rectangular matrices `B0,E` with `rank(E)<=k`,

`s_j(B0+E) >= s_{j+k}(B0)`                                      (3.1)

for every admissible `j`.

#### Proof

The standard singular-value Weyl inequality gives

`s_{j+k}(B0) <= s_j(B0+E) + s_{k+1}(-E)`.

Since `rank(E)<=k`, `s_{k+1}(E)=0`, proving (3.1). Equivalently, a rank-`k` perturbation can cancel at most `k` singular directions above any fixed threshold. QED.

### Theorem B — `QFORM-ARBITRARY-RANKK-ADDITION-CANCELLATION-BUDGET-v1`

Let `A0` be real symmetric. Suppose there is an original-coordinate cut `I,J` such that

`s_{r+k}(A0[I,J]) >= sigma>0`                                    (3.2)

for some integers `k>=0` and `r>=5`.

Let `R` be **any** real symmetric matrix of rank at most `k`, with no restriction on its nonzero eigenvalue sizes or signs, and put `A=A0+R`. Then

`||p_{X^T A X}||_infinity <= C_r/sigma`,                          (3.3)

with `C_r` from (1.3), hence also

`||p_{X^T A X}||_infinity <= [e r/(2(r-4))]/sigma`.               (3.4)

The density is continuous and vanishes at infinity.

#### Proof

Set `B0=A0[I,J]` and `E=R[I,J]`. Restriction cannot increase matrix rank, so `rank(E)<=rank(R)<=k`. By Lemma 3.1,

`s_r(A[I,J]) = s_r(B0+E) >= s_{r+k}(B0) >= sigma`.                (3.5)

Thus the final cross block still has at least `r>=5` singular values at least `sigma`, regardless of how large or oppositely signed the added eigenvalues of `R` are. Apply the unconditional `q=2` regularized determinant estimate (1.1) and Fourier inversion. This proves (3.3), continuity and vanishing at infinity. QED.

For the minimal robust case `r=5`,

`C_5 = (e sqrt(pi)/4) Gamma(1/8)/Gamma(5/8)
     = 6.3259450841...`,                                         (3.6)

while the elementary bound gives `C_5<=5e/2=6.7957045711...`.

The important point is qualitative as well as quantitative: **arbitrary magnitude does not matter; only cross-rank cancellation matters.** Each arbitrary added eigenvalue direction costs at most one pre-existing certified cross singular direction.

## 4. Concrete spectral-addition corollary from the diffuse full-range theorem

### Corollary 4.1 — `QFORM-DIFFUSE-BASE-PLUS-ARBITRARY-RANKK-v1`

Let

`A0=U Lambda U^T`

with `U^T U=I`, and assume the entire range leverage satisfies

`max_i ||u_i||^2 <= 1/32`.                                      (4.1)

Suppose `A0` has at least `k+5` eigenvalues of absolute value at least `L>0`. Let `R` be any real symmetric rank-`k` matrix; its nonzero eigenvalues may be arbitrarily small, arbitrarily large, positive or negative. Then for `A=A0+R`,

`||p_{X^T A X}||_infinity
 <= (32/(7L)) C_5
 = 28.9186060989.../L`,                                          (4.2)

and in particular

`||p_{X^T A X}||_infinity <= 80e/(7L) = 31.0660780395.../L`.      (4.3)

The density is continuous and vanishes at infinity.

#### Proof

Use the MSS partition supplied by the source theorem. By (1.6), the base cross block has at least `k+5` singular values at least `7L/32`. Apply Theorem B with `r=5` and `sigma=7L/32`. No condition at all is imposed on the final matrix's range leverage: the proof switches to the unconditional `q=2` determinant bound after spending the `k` cancellation directions. QED.

This is stronger than simply requiring the *final* entire range to be diffuse. A rank-`k` perturbation may create highly concentrated or even coordinate-supported new eigendirections and may make the final entire-range leverage equal to one; (4.2) still holds.

## 5. Actual application of the named fleet02/B12 partner theorem

The partner result yields a complementary stability statement that handles one arbitrary spectral addition without any cross-richness assumption.

### Theorem C — `QFORM-DEFINITE-PHYSICAL-BLOCK-PLUS-ARBITRARY-RANKONE-v1`

Let `I` be an original-coordinate block of size `m>=4`. Suppose a symmetric matrix `D` on that block satisfies either

`D >= L I_m`                                                     (5.1)

or

`D <= -L I_m`                                                    (5.2)

for some `L>0`. Let `E` be any symmetric rank-one matrix on that block, with completely arbitrary sign and magnitude. Let the full ambient matrix `A` have principal block

`A[I,I]=D+E`,                                                     (5.3)

with **no restrictions whatsoever** on all coefficients outside `I x I`.

Then

`||p_{X^T A X}||_infinity < 24.193/L`.                            (5.4)

#### Proof

Assume (5.1); the negative case follows by reflection. Since `rank(E)<=1`, its kernel has dimension at least `m-1`. On `ker(E)`,

`x^T(D+E)x=x^T D x >= L ||x||^2`.

By the Courant--Fischer min-max principle, `D+E` therefore has at least `m-1` eigenvalues at least `L`; its remaining eigenvalue may be arbitrary. This is exactly the hypothesis of the completed `fleet02/B12` theorem (1.7). Condition on every original coordinate outside `I`. The outside couplings become only an affine tilt on `X_I`, and the partner theorem is uniform over all such tilts. Averaging the conditional densities gives (5.4). QED.

Thus a definite physical smoothing block is completely stable under **one arbitrary added eigenvalue direction**, even if that added eigenvalue is much larger than `L` and has the opposite sign. This is a direct mathematical use of the named partner result, not a citation-only dependency.

The partner theorem supplies an essentially bounded density at this scope. I do not upgrade Theorem C to continuity because the partner source does not establish that stronger conclusion.

## 6. What has changed, and what remains unpaid

### New mathematical change

This run establishes two cancellation ledgers for additional spectral directions:

1. **zero-cross additions cost zero:** any number of arbitrary eigenvalues can be added inside the two self banks of a certified cut with exactly no loss in the cross certificate (Theorem A);
2. **rank-k arbitrary additions cost at most k cross singular directions:** if the base cut has `r+k` certified directions, the final form retains `r` of them no matter how large or oppositely signed the new eigenvalues are (Theorem B);
3. **one arbitrary eigenvalue costs zero inside a definite physical block:** the named partner theorem plus rank-one min-max gives Theorem C.

These results directly address the assignment's warning that a quadratic remainder is dependent after rotation: no independent-convolution step is used anywhere.

### Exact unpaid implication

The full owner hypothesis supplies only **three** large eigenvalues. It does not imply a cut carrying five cross singular directions, a block-diagonal remainder relative to a three-direction cut, or a definite physical block plus only one exceptional direction. The live correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` explicitly rules out a naive uniformly good local-block-or-rank-three-cut dichotomy.

Therefore the full target remains OPEN. The next useful implication for this assignment is an **exhaustive heavy/light reduction that preserves a three-direction certificate while routing concentrated extra eigendirections into self blocks or a bounded-rank cancellation budget**. Theorems A--C give exact prices for such a reduction once it is constructed.

## 7. Corrections respected

This proof does not use:

- law-uniform pointwise van-der-Corput decay;
- independence after spectral rotation;
- naive fiber-supremum integration;
- a cross minor by itself;
- conditional density caps as a replacement for independence;
- single-Schur rank-two extraction;
- bounded-diameter localization;
- fiberwise indefinite trace control;
- the absolute phase-Wiener interface.

All cuts and conditionings are in original coordinates. The only spectral perturbation input is the exact rank bound and min-max/singular-value interlacing.

**Status:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`. No full-solution, novelty, or publication-priority claim is made.
