# r22 addendum — one-sided half-Riesz sharpening and predecessor reconciliation

This addendum is part of the immutable r22 record. It does not rewrite `REPORT.md`; it records a later same-run source discovery and a stronger constant.

## 1. Predecessor reconciliation

After the first r22 report was committed, a fresh source search found the already-completed fleet02/B13 run

`yspennstate/math-open-problems@6fb28b3e367d9cd8bf1dff3a4ca05b500d5d32c8`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T025607Z-fleet02-B13-extreme-cf3f0909/REPORT.md`.

That report had already combined the fleet03/B13 r21 cross-three-volume `L3` theorem with a scalar Schur peel and obtained the same qualitative certificate, with constant `20.870`; it also recorded the anchored four-volume identity

`W_i(I,J)=A_ii^2 e_3(M^T M)`.

Therefore r22 does **not** claim priority for the qualitative scalar-Schur/cross-three-volume gluing mechanism. The genuinely new contributions retained here are:

1. the direct three-quarter cross-three-volume slab estimate `<14.486 Z3^(-1/8)|J|^(3/4)` from the entropic/six-hub dichotomy; and
2. the sharper one-sided half-Riesz transducer below, which improves the scalar-Schur density constant substantially.

A second completed source found in the refresh is fleet03/B06 r24,

`yspennstate/math-open-problems@6fb28b3e367d9cd8bf1dff3a4ca05b500d5d32c8`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T011959Z-fleet03-B06-qform-r24/REPORT.md`.

Its Lemma 5.1 already proved a one-sided `L3` half-Riesz transducer with constant `8/3^(3/4)=3.50953...`. The calculation below sharpens that constant; it does not duplicate the lemma unchanged.

## 2. Sharper one-sided half-Riesz inequality

### Lemma — `QFORM-L3-ONESIDED-HALF-RIESZ-SHARP-v1`

If `p` is a probability density on `R` with `||p||_3<=M`, then

`boxed:
 sup_t int_0^infinity p(t-u) u^(-1/2) du
 <= C_+ M^(3/4),
 C_+=2 sqrt(pi/sqrt(3))
    =2.693547374177197... .}`                                      (2.1)

The reflected kernel `int_0^infinity p(t+u)u^(-1/2)du` obeys the same bound.

### Proof

Fix `lambda>0`. For `u>0`,

`u^(-1/2) <= lambda + (u^(-1/2)-lambda)_+`.

Hence, using only `int p=1` for the first term and Holder `(3,3/2)` for the second,

`int_0^infinity p(t-u)u^(-1/2)du`

`<= lambda
 + M ||(u^(-1/2)-lambda)_+||_{L^(3/2)(0,infinity)}.`              (2.2)

The exact kernel integral is

`int_0^infinity (u^(-1/2)-lambda)_+^(3/2) du
 = (3pi/4) lambda^(-1/2).`                                        (2.3)

Indeed the support is `0<u<lambda^(-2)`; setting `x=lambda sqrt(u)` reduces the integral to

`2 lambda^(-1/2) B(1/2,5/2)=3pi/4 lambda^(-1/2)`.

Thus (2.2) is

`<= lambda + M (3pi/4)^(2/3) lambda^(-1/3)`.

The minimum occurs at

`lambda=[M(3pi/4)^(2/3)/3]^(3/4)`,

and the minimum value is

`4 [M(3pi/4)^(2/3)/3]^(3/4)
 =2 sqrt(pi/sqrt(3)) M^(3/4)`.

This proves (2.1). QED.

This improves the split-at-radius constant in fleet03/B06 r24 from `3.5095307012...` to `2.6935473742...` while preserving exactly the same hypotheses.

## 3. Sharpened scalar-Schur cross-three-volume theorem

Use the dependence-safe square kernel already pinned in fleet03/B06 r24 / fleet04/B18. After completing one ORIGINAL scalar square with coefficient `a!=0`,

`p_Q(t)
 <= |a|^(-1/2)
    int_0^infinity p_R(t-sgn(a)u)u^(-1/2)du`.                      (3.1)

For a residual Schur cross block `M` with

`Z3=e_3(M^TM)>0`,

fleet03/B13 r21 gives the safe bound

`||p_R||_3 < 6.787 Z3^(-1/9)`.

Insert this into (2.1) and (3.1):

`boxed:
 ||p_Q||_infinity
 <11.327 |a|^(-1/2) Z3^(-1/12).}`                                (3.2)

The evaluated constant is

`2 sqrt(pi/sqrt(3)) * 6.787^(3/4)
 =11.326168157432749...`.

Using the unrounded r21 branch constant `6.786385992671971...` gives `11.325399655639595...`, but (3.2) deliberately uses the safe public `6.787` theorem statement.

Equivalently, with the anchored bordered four-volume of fleet02/B13,

`W_i(I,J)=a^2 Z3`,

one obtains the original-matrix certificate

`boxed:
 ||p_Q||_infinity
 <11.327 (|A_ii|^4 W_i(I,J))^(-1/12).}`                           (3.3)

If `s_3(M)>=sigma`, then `Z3>=sigma^6` and

`||p_Q||_infinity <11.327 (|a| sigma)^(-1/2)`.                    (3.4)

All same-side Schur curvature, arbitrary extra cross singular directions, outside couplings, affine terms, signs, and arbitrary fragmented/unbounded cap-one marginals remain allowed.

## 4. Designated partner application remains zero-loss

For bounded finite-union unit product indicators, (3.2) gives the slab inequality

`P(Q in J) <11.327 |a|^(-1/2) Z3^(-1/12)|J|`.

Apply the designated fleet04/B13 no-attainment product purification (`math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`) to the bounded kernel `1_{Q in J}`. The same inequality transfers to every independent cap-one product law with zero constant loss. No optimizer, interval extremality, support-radius bound, or fragment-count bound is assumed.

This proves essential boundedness in the stated branch. Continuity is not established by the one-sided square transducer or by the mixture transfer.

## 5. Remaining gap

Full QFORM remains OPEN. The sharpened theorem forces every divergent no-pivot candidate sequence to have

`|A_ii|^4 W_i(I,J) ->0`

for every nonzero original scalar pivot `i` and every residual disjoint physical cut `(I,J)` along the divergent subsequence, unless an already-paid branch applies. The unpaid implication is to convert simultaneous collapse of all these anchored aggregate four-volume currencies into the exact/near-null coloop, low-cross-rank tube, grouped-bank, hub/Fresnel, or diffuse volume-stability exits without deleting small coefficients on unbounded product supports.
