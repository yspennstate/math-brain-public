# account01/B19 — universal assembly: low-offdiagonal threshold pushed to 3/10

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260922T165145Z-b19-qform-r11`.
Control used at publication refresh: owner control revision `2026-09-22.8`.
Status: `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL-BRANCH-PROVED / FULL CONJECTURE OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction boundary

Let `X=(X_1,...,X_n)` have independent real coordinates, each with a probability density bounded by one, and let `A` be real symmetric with at least three eigenvalues of modulus at least one. The target is a dimension-, law-, sign-, and matrix-independent finite bound on the essential supremum of the density of `Q=X^T A X`. Continuity is tracked separately.

No rotation of the product law, no pointwise law-uniform van der Corput estimate, no conditional-cap-implies-independence step, no fixed-good-minor assertion, and no fictitious independent convolution is used here. All pivots are physical original-coordinate pivots.

## 2. Completed peer inputs used

### 2.1 Designated partner account02/B19 r15

Source: `yspennstate/math-open-problems@48841f2d72a1faf741d5a75f6569107537221e7e`, account02/B19 run `20260922T151209Z-account02-B19-qform-r15` and its ridge addendum.

The partner proved the structural ridge-or-physical-resource implication at the `|lambda|>=1/64` spectral window: if the ridge-window diffuse hypothesis does not hold, then some physical coordinate `i` satisfies

`|A_ii| >= 1/512`  or  `||A_{i,-i}||_2 > 1/512`.

The elementary inequality used there is

`(A^2)_ii = A_ii^2 + ||A_{i,-i}||_2^2`,

combined with `A^2 >= P/4096` for the spectral projection `P` onto `|lambda(A)|>=1/64`.

I apply this result in Section 7 to the actual remaining branch rather than merely citing it.

### 2.2 account03/B19 physical indefinite-pivot quarter kernel

Source: `yspennstate/math-open-problems@7291482e652c4cb47efc44c1656c0af46fa0f45e`, account03/B19 run `20260922T160316Z-account03-B19-QFORM-r14`.

For a physical pivot

`B = [[a,c],[c,-b]]`,  `a,b>=m>0`,  `Delta=ab+c^2`,

and exact Schur complement `S`, conditioning on the outside original coordinates gives a density kernel

`h_z(t) <= 2 Delta^(-1/4) m^(-1/4) |t-z^T S z|^(-1/4)`.

This statement permits arbitrary outside couplings and arbitrary independent cap-one input laws.

### 2.3 account03/B11 one-eigenvalue quarter-Riesz theorem

Source: `yspennstate/math-open-problems@841766055688a7534c8621fc06eb99d227e58aca`, account03/B11 run `20260922T161210Z-account03-B11-QFORM-r13`.

For every symmetric `S` with `s_1(S)>=sigma>0` and arbitrary independent cap-one coordinates `Z`,

`sup_t E |t-Z^T S Z|^(-1/4) <= 25 sigma^(-1/4)`.

No sign, moment, support, rank, or diagonal-basis hypothesis is imposed.

## 3. New splice: every quantitative opposite-sign physical pair is paid

### Lemma 3.1 — `QFORM-OPPOSITE-DIAGONAL-PAIR-v1`

Assume two original coordinates `i,j` satisfy, after possibly replacing `A` by `-A`,

`A_ii=a>=m`,  `A_jj=-b<=-m`,  `m>0`.

Then for arbitrary independent cap-one input laws,

`||p_Q||_infinity <= 50 m^(-3/4)`.

#### Proof

Write `A` in the block form

`A = [[B,K],[K^T,C]]`,

with the two-coordinate pivot `B=[[a,c],[c,-b]]`. It is automatically invertible and indefinite, with

`Delta=ab+c^2 >= m^2`.

Let

`S=C-K^T B^(-1)K`

be its exact Schur complement. The block identity

`A - diag(0_2,S)
 = [I_2; K^T B^(-1)] B [I_2, B^(-1)K]`

has rank at most two. Hence the rank-two singular-value interlacing inequality gives

`s_3(A) <= s_1(S)`.

Under the owner target, `s_3(A)>=1`, so

`s_1(S)>=1`.                                                     (3.1)

Apply the account03/B19 conditional pivot kernel and average over the outside product law:

`p_Q(t)
 <= 2 Delta^(-1/4)m^(-1/4)
       E |t-Z^T S Z|^(-1/4)`.

Now apply the account03/B11 quarter-Riesz theorem to (3.1):

`p_Q(t) <= 50 Delta^(-1/4)m^(-1/4)
         <= 50 m^(-3/4)`.

This is uniform in `t`. All signs of the remaining spectrum, all eigenvalue coincidences, all outside degeneracies and all admissible input densities are allowed. QED.

This is the key new assembly step: after an indefinite physical two-pivot, the third large spectral direction is not hunted through a local Schur cross minor. Rank-two Schur inheritance leaves one large singular direction in the exact Schur complement, and the completed one-eigen quarter-Riesz theorem pays it globally.

## 4. Same-sign physical pair

### Lemma 4.1 — definite physical-pair bound

If two physical diagonal entries have the same sign and, after a global sign change,

`A_ii>=m`, `A_jj>=m`, `|A_ij|<=r<m`,

then

`||p_Q||_infinity <= pi / sqrt(m^2-r^2)`.                       (4.1)

#### Proof

Condition on all outside original coordinates. They create only an affine term in the two pivot variables. The physical `2 x 2` matrix is positive definite with determinant at least `m^2-r^2`. Completing the square translates its center. For an interval `I` of length `eps`, the inverse image of `I` under the translated definite quadratic has area at most

`pi eps / sqrt(det B)`.

The conditioned two-coordinate joint density is a product bounded pointwise by one. Thus the conditional interval probability is at most the same area, uniformly in the outside variables. Averaging and taking the Radon--Nikodym derivative gives (4.1). The negative-definite case follows by reflecting the output. QED.

No regularity of the input densities is needed.

## 5. New target-level branch theorem

Put

`D=diag(A)`, `H=A-D`.

### Theorem 5.1 — `QFORM-LOW-OFFDIAG-ONE-THIRD-BARRIER-v1`

Let `0<=tau<1/3`. Under the exact full target hypotheses, if

`s_2(H) <= tau`,

then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity
 <= max{
      50(1-tau)^(-3/4),
      pi / sqrt((1-tau)^2-4tau^2)
    }`.                                                        (5.1)

Equivalently the second denominator is

`(1-tau)^2-4tau^2=(1+tau)(1-3tau)>0`.

#### Proof

Choose a top-magnitude eigenpair `lambda,v` of the symmetric zero-diagonal matrix `H` and write

`H=lambda vv^T+R`,  `||R||op=s_2(H)<=tau`.                    (5.2)

Since `H_ii=0`,

`lambda v_i^2 + R_ii=0`,

so

`|lambda| v_i^2 <= tau` for every `i`.                         (5.3)

For `i!=j`,

`|H_ij|
 <= |lambda| |v_i v_j| + |R_ij|
 <= sqrt((|lambda|v_i^2)(|lambda|v_j^2))+tau
 <= 2tau`.                                                     (5.4)

Now set

`A_0=D+lambda vv^T=A-R`.

Weyl's singular-value inequality and `s_3(A)>=1` give

`s_3(A_0)>=1-tau=:m`.                                         (5.5)

A rank-one perturbation can increase singular-value counting by at most one, hence

`s_3(D+lambda vv^T)<=s_2(D)`,

and therefore

`s_2(D)>=m`.                                                   (5.6)

Thus there are two physical coordinates `i,j` with

`|A_ii|,|A_jj|>=m`.                                           (5.7)

If their signs are opposite, Lemma 3.1 gives

`||p_Q||_infinity <=50m^(-3/4)`.

If their signs agree, (5.4) gives `|A_ij|<=2tau`. Since `tau<1/3`,

`m=1-tau>2tau`,

so their physical block is definite and Lemma 4.1 gives

`||p_Q||_infinity
 <= pi / sqrt(m^2-4tau^2)`.

These cases exhaust all sign possibilities. QED.

### Corollary 5.2 — clean numerical branch

Taking `tau=3/10` gives `m=7/10` and

`m^2-4tau^2=13/100`.

Hence

`boxed: s_2(A-diag A)<=3/10  =>  ||p_Q||_infinity <66.`         (5.8)

Indeed

`50(10/7)^(3/4)=65.335087...`,

while

`10pi/sqrt(13)=8.713211...`.

This doubles the previously source-pinned `3/20` low-offdiagonal threshold and lowers the branch constant from `<700` to `<66` by replacing the former Schur cross-bank extraction with the direct quarter-Riesz Schur inheritance splice.

The theorem is intentionally stated for every fixed `tau<1/3`; no conclusion at the endpoint `tau=1/3` is claimed because the same-sign determinant lower bound vanishes there.

## 6. Why the 1/3 barrier is genuine for this argument

The proof mechanism has exactly one scalar obstruction at `tau=1/3`: the information (5.4)--(5.7) then permits a same-sign physical block with

`A_ii=A_jj=2/3`,  `|A_ij|=2/3`,

whose determinant is zero. Thus the present two-heavy-diagonal argument cannot cross `1/3` without additional aggregate information. This is a limitation of the mechanism, not a counterexample to QFORM.

## 7. Conditional end-to-end assembly and designated-partner application

Use the completed spectral-window ridge theorem at its stated scope: if the `|lambda(A)|>=1/64` spectral projection has maximum coordinate leverage at most `1/32`, the full form has a continuous density `<64`.

If that diffuse condition fails, apply the designated partner account02/B19 r15 ridge-or-physical-resource inequality. It gives an actual original-coordinate resource

`|A_ii|>=1/512` or `||A_{i,-i}||_2>1/512`.                    (7.1)

Now intersect with the new theorem:

* if `s_2(A-diag A)<=3/10`, (5.8) closes the form with density `<66`, independently of which alternative in (7.1) occurs;
* therefore every still-unpaid form must simultaneously satisfy

`max_i P_ii>1/32`,

`s_2(A-diag A)>3/10`,

and the partner's physical-resource alternative (7.1).        (7.2)

This is the designated partner result applied to the actual residual inequality, not just listed as background.

A second completed full-matrix reduction, account03/B07 `QFORM-THIRD-COMPOUND-OVERLAP-REDUCTION-v1`, further says that every such remaining matrix belongs to one of O0/O1/O2/O3 aggregate determinant classes; its O0 diffuse calibrated-ridge subbranch is already paid. Therefore a compact conditional full proof is now:

1. spectral-window diffuse -> paid (`<64`, continuous);
2. otherwise use (7.1);
3. low offdiagonal `s_2(H)<=3/10` -> paid by Theorem 5.1 (`<66`);
4. high offdiagonal `s_2(H)>3/10` -> prove one product-preserving aggregate payment for the surviving O0-heavy/O1/O2/O3 class while retaining (7.1).

Only item 4 is not presently proved.

## 8. First essential missing implication

The first remaining global inequality can now be stated without a local-minor fiction:

`QFORM-HIGH-OFFDIAG-OVERLAP-PAYMENT-v1`:

For matrices satisfying the full target, `s_2(A-diag A)>3/10`, and the partner physical-resource condition (7.1), prove that the aggregate third-compound alternative O0-heavy/O1/O2/O3 yields one already-supported product-coordinate smoothing packet with a universal quantitative constant.

The immediate subproblem is the O0-heavy case: at calibrated effective rank `theta=8/3`, a ridge row has leverage `>1/2`. One must convert that DPP-heavy original row into a grouped-coordinate rank-two-plus-square packet or transfer a fixed amount of third-compound mass into O1/O2/O3 without selecting a reciprocal tiny minor. The live corrections show why a fixed good triple or fixed cross minor cannot be demanded.

A useful structural target for the next run is to combine (7.1) with the O0 DPP-heavy row: if the two heavy physical rows coincide, condition it and use the completed one-heavy-row theorem; if they are separated, seek a two-row Gram determinant lower bound before whitening. Failure should force overlap mass into O1/O2.

## 9. Scope and continuity

* Theorem 5.1 is an essential-density theorem for arbitrary independent densities bounded by one, all dimensions, all signs and all additional eigenvalues.
* It makes no continuity claim. The spectral-window ridge branch separately has continuity.
* The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.
* No endpoint `tau=1/3` statement is claimed.
* No operational receipt is treated as mathematical validation; independent end-to-end review of this new splice is still needed before any full-proof promotion.
