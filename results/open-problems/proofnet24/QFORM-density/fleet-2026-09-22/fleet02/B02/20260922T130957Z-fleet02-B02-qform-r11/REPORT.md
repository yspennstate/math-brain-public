# fleet02/B02 — coupled 2x3 mixed-norm integrated Fourier theorem

**Run:** `20260922T130957Z-fleet02-B02-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Target, corrections, and the first unpaid implication attacked

The full target remains open: for arbitrary independent real coordinates whose densities are bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one dimension- and law-independent essential density bound for `Q=X^T A X`, or produce a valid target counterexample.

This run keeps the live corrections: no law-uniform pointwise Fresnel decay is assumed; no independence is asserted after an orthogonal change of variables; a fixed cross minor is not assumed to follow from the spectral hypothesis; bounded conditional density is not substituted for genuine independence; and the rank-two cross-block endpoint by itself is nonintegrable.

The named partner result actually consumed is fleet03/B02 `QFORM-RANK2-PLUS-PIVOT-FOURIER-v1`, canonical report `yspennstate/math-open-problems@ac57190328fc109873ebe3b17122d835abbc2c3a`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T121820Z-fleet03-B02-QFORM-r11/REPORT.md`, blob `cf1b7abb4f9bd91f991db6e54c0c36e92ad6125f`. That theorem closes a `2+1` Fourier configuration when the third physical pivot has **zero couplings** to both sides of an invertible `2x2` cross block. The first implication attacked here is removal of that exact decoupling condition while preserving original-coordinate product provenance.

## 2. New theorem: a fully coupled 2x3 physical block still closes the Fourier integral

### Theorem `QFORM-COUPLED-2x3-MIXED-FOURIER-v1`

Let `I,J` be disjoint sets of original coordinates with

`|I|=2`, `|J|=3`.

Let

`C=A[I,J]`

have rank two. Write its two nonzero singular values as `s_1,s_2` and put

`Delta=s_1 s_2>0`.

Let `n in R^J` be either unit vector spanning `ker C`, and define the null-direction curvature

`delta=n^T A[J,J] n`.

Assume `delta != 0`. There are **no other structural assumptions**: `A[I,I]` is arbitrary, `A[J,J]` may be fully coupled, all couplings to coordinates outside `I union J` are arbitrary, all additional eigenvalues are arbitrary, the dimension is arbitrary, and the input laws are arbitrary independent laws with densities at most one.

Then the characteristic function of `Q=X^T A X` belongs to `L^1(R)`, and

`||phi_Q||_1 <= pi * 2^(175/48) * 3^(-1/4) * Delta^(-3/8) * |delta|^(-1/4)`.   (2.1)

Consequently `Q` has a bounded continuous density, vanishing at infinity, with

`boxed( ||p_Q||_infinity <= 2^(127/48) * 3^(-1/4) * Delta^(-3/8) * |delta|^(-1/4) )`.   (2.2)

The numerical prefactor in `(2.2)` is about `4.75549`, so the clean bound

`||p_Q||_infinity < 5 Delta^(-3/8)|delta|^(-1/4)`

also holds.

The scaling is correct: under `A -> cA`, `Delta -> |c|^2 Delta` and `|delta| -> |c||delta|`, so the right side scales by `|c|^(-1)`.

### Relation to the partner theorem

If `J=J_0 union {k}`, `|J_0|=2`, the cross block is `[B,0]`, and the third coordinate is exactly decoupled from the selected cross block, then `n=e_k` and `delta=A_kk`. Thus the partner's structural configuration is contained in the present one. The partner theorem is quantitatively sharper in that exactly decoupled special case. The point here is qualitative and structural: **arbitrary couplings of the null direction to the two active `J` directions are allowed**.

## 3. Proof

Condition on every original coordinate outside `I union J`. The conditioned coordinates generate only linear terms and a constant on the five selected coordinates. All estimates below are uniform in those induced linear terms.

Take an SVD of the `2x3` cross block. Orthogonal changes of variables inside the exact two `I` coordinates and exact three `J` coordinates put the selected variables in the form

`x in R^2`, `(y,z_0) in R^2 x R`,

with cross term

`2 x^T S y`, `S=diag(s_1,s_2)`,

and no `x-z_0` cross term. These changes are only analytic coordinate changes. No independence after rotation is asserted. The joint density on the rotated `J` block is the original three-fold product density composed with an orthogonal map; it therefore still has mass one and is pointwise at most one.

Write the rotated `J` principal block as

`[[E,b],[b^T,delta]]`.

The induced linear term in `z_0` can be absorbed as well. Since `delta != 0`, complete the square by the unit-Jacobian shear

`z = z_0 + delta^(-1)(b^T y + beta)`

for the appropriate conditioned scalar `beta`. The phase is now

`q_I(x) + 2 x^T S y + q_J'(y) + delta z^2 + linear terms + constant`.   (3.1)

Let `H(y,z)` be the transformed nonnegative density on the `J` block after this shear. It has total mass one and remains pointwise at most one. Its `z` marginal also has a dimension-free cap. Indeed `z` is an affine linear functional of the three original independent `J` coordinates. The coefficient vector has Euclidean norm

`nu=sqrt(1+||b/delta||^2) >= 1`.

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures* (arXiv:1507.07949), prove that every one-dimensional marginal of a product density with coordinate densities bounded by one has density at most `sqrt(2)`. Scaling the linear functional therefore gives

`m(z):=int_{R^2} H(y,z)dy <= sqrt(2)/nu <= sqrt(2)`.   (3.2)

This use of a marginal theorem preserves the original product provenance; it is not a claim of conditional independence.

### 3.1 Rank-two Plancherel factor

Absorb every `x`-only quadratic and linear phase into the complex amplitude `F_t(x)`. Since the two `I` coordinates are original independent coordinates and each density is bounded by one,

`||F_t||_2 <= 1`.

Define

`A_t(y)=int_{R^2} F_t(x) exp(i 2t x^T S y) dx`.

Angular Fourier Plancherel and the change of variables `xi=2tSy` give, for `t!=0`,

`||A_t||_{L^2(dy)} <= pi Delta^(-1/2)|t|^(-1)`.   (3.3)

This is exactly the rank-two endpoint mechanism consumed from fleet03/B02/fleet02-B02, but here it will be paired with a **vector-valued** square credit rather than a pointwise scalar factorization.

### 3.2 Vector-valued square transform

Define

`h_t(y)=int_R exp(i t delta z^2) H(y,z) dz`

and put

`B(t)=||h_t||_{L^2(dy)}`.

The remaining `y`-only phase in `(3.1)` has modulus one and hence does not change `B(t)`.

We prove

`boxed( ||B||_{L^3(dt)} <= 3^(2/3) 2^(19/36) pi^(1/3) |delta|^(-1/3). )`   (3.4)

It is enough to take `delta>0`; reflection handles the other sign. For `r>0` set

`a(r)=||H(.,r)+H(.,-r)||_2`.

From `0<=H<=1` and the marginal cap `(3.2)`,

`a(r)^2 <= 2[m(r)+m(-r)] <= 4sqrt(2)`,

so

`M:=||a||_infinity <= 2*2^(1/4)`.   (3.5)

Also

`int_0^infinity a(r)^2 dr <= 2`,   (3.6)

because `(H_r+H_-r)^2 <= 2(H_r^2+H_-r^2) <= 2(H_r+H_-r)` and `H` has mass one.

The Hilbert-valued density in the square variable `s=delta r^2` is

`g(s,y)=[H(y,sqrt(s/delta))+H(y,-sqrt(s/delta))]/[2 sqrt(delta s)]`, `s>0`.

Thus

`int_0^infinity ||g(s,.)||_2^(3/2) ds
 = 2^(-1/2) delta^(-1/2) int_0^infinity a(r)^(3/2) r^(-1/2)dr`.   (3.7)

For any `R>0`, `(3.5)-(3.6)` give

`int_0^infinity a(r)^(3/2)r^(-1/2)dr
 <= 2 M^(3/2) R^(1/2) + (int a^2)^(3/4) R^(-1/4)`.

Optimizing in `R` gives

`int_0^infinity a(r)^(3/2)r^(-1/2)dr <= 3*2^(19/24)`.   (3.8)

Substitution into `(3.7)` yields

`||g||_{L^(3/2)(ds;L^2_y)} <= 3^(2/3) 2^(7/36)|delta|^(-1/3)`.   (3.9)

The Fourier transform acts only in the scalar `s` variable with values in the Hilbert space `L^2_y`. Interpolating the vector-valued `L^1(H)->L^infinity(H)` triangle inequality with Hilbert-valued Plancherel gives angular Hausdorff--Young

`||hat g||_{L^3(dt;L^2_y)} <= (2pi)^(1/3)||g||_{L^(3/2)(ds;L^2_y)}`.

Since `hat g(t)=h_t`, this is `(3.4)`. No law-uniform pointwise Fresnel estimate occurs anywhere in this step.

### 3.3 Integrating the conditional characteristic function

The conditioned characteristic function `Phi(t)` satisfies, by Cauchy--Schwarz in `y` and `(3.3)`,

`|Phi(t)| <= pi Delta^(-1/2)|t|^(-1) B(t)`,

and of course `|Phi(t)|<=1`. Hence for every `T>0`, Holder with exponents `3` and `3/2` on `|t|>T` gives

`||Phi||_1
 <= 2T + pi Delta^(-1/2)||B||_3 (int_{|t|>T}|t|^(-3/2)dt)^(2/3)`
` <= 2T + C_0 Delta^(-1/2)|delta|^(-1/3) T^(-1/3)`,   (3.10)

where

`C_0=2^(67/36) 3^(2/3) pi^(4/3)`.

The minimizing choice is

`T=[C_0 Delta^(-1/2)|delta|^(-1/3)/6]^(3/4)`.

Substitution into `(3.10)` gives exactly `(2.1)`:

`||Phi||_1 <= pi 2^(175/48)3^(-1/4) Delta^(-3/8)|delta|^(-1/4)`.

This bound is uniform in all outside conditioned coordinates. Since

`phi_Q(t)=E[Phi(t) | outside]`

in the usual disintegration sense, Tonelli and Jensen/triangle inequality give the same `L^1` bound for `phi_Q`. Fourier inversion proves `(2.2)` and supplies a continuous representative vanishing at infinity.

For arithmetic checking only:

- the vector-valued square-transform prefactor in `(3.4)` is about `4.39212207946`;
- the `L^1` prefactor in `(2.1)` is about `29.8795980931`;
- dividing by `2pi` gives the density prefactor about `4.75548573411`.

These decimal values are not used in the proof.

## 4. What the theorem pays and what remains unpaid

This is a genuine extension of the partner's integrated `2+1` theorem: exact zero couplings of the third smoothing direction are no longer required. The third direction may be fully coupled to the two active directions on its side; the square smoothing is retained as an `L^3_t(L^2_y)` resource rather than forced into a scalar characteristic-function factor.

It does **not** prove the full conjecture and does not establish a target-wide uniform `L^1` characteristic-function bound. No counterexample to that stronger target-wide Fourier criterion was found in this run. The first remaining implication is now a product-preserving extraction/aggregation statement:

> From the sole hypothesis of three eigenvalues with modulus at least one, force or aggregate either an existing rank-three physical cross-block resource, or a `2x3` physical configuration for which `Delta^3 delta^2` is bounded below at a dimension-free scale; alternatively extend the mixed-norm argument to a high-cardinality aggregate null direction without paying a reciprocal fixed minor.

The fixed-small-minor version cannot be silently assumed: existing Walsh/Hadamard and hard-saddle families make every fixed physical minor small while remaining bounded through high-cardinality aggregation. Arbitrary additional spectral directions are a separate difficulty because they can cancel a cross block extracted from only three chosen eigendirections.

## 5. Source/correction ledger

Mathematics actually applied:

- fleet03/B02 `QFORM-RANK2-PLUS-PIVOT-FOURIER-v1`: `yspennstate/math-open-problems@ac57190328fc109873ebe3b17122d835abbc2c3a`, report blob `cf1b7abb4f9bd91f991db6e54c0c36e92ad6125f`;
- Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, specifically the bound `2^(k/2)` for a `k`-dimensional marginal of a product density with coordinate factors bounded by one;
- prior fleet02/B02 physical cross-block Plancherel mechanism: `yspennstate/math-open-problems@400f82c8b98fc5623f567581b6ccb0b4298974e8`.

Live correction state consumed before publication includes `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, and `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`. The present proof does not use any challenged premise.

Full QFORM target: **OPEN**.
