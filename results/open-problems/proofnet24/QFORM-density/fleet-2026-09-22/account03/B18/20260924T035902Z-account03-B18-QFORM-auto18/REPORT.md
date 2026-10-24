# account03/B18 auto18 — Rudelson–Vershynin spectral-tail transfer and the Hilbert–Schmidt rank-two collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T035902Z-account03-B18-QFORM-auto18`  
**Role:** literature-to-proof transfer  
**Status:** `PROVED SUPPORTING TARGET-LEVEL REDUCTION / FULL QFORM OPEN`  
**Continuity:** not proved by the new generic theorem.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-24T03:59:02Z.  
attacking: the near-rank-two cross collar left by account04/B18; use the published Rudelson–Vershynin spectral-tail small-ball estimate to spend aggregate Hilbert–Schmidt cross energy without deleting any small singular direction.

## 1. Exact scope and correction discipline

The owner target remains open: for arbitrary independent real original coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free bound on the density of `X^T A X`, or give a counterexample. No moments, support restriction, iid hypothesis, symmetry, centering, log-concavity, smoothness, or post-rotation independence is assumed.

This report does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, conditional-density-cap-as-independence, deletion of a small nonzero coefficient, a forced fixed good principal minor, or independence after a spectral rotation. All conditioning below is on disjoint ORIGINAL-coordinate banks.

## 2. Primary source: the spectral-tail estimate hidden inside Rudelson–Vershynin Theorem 8.1

The primary source is M. Rudelson and R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492v2 / IMRN 2015.

Two statements are used exactly at their published hypotheses.

1. **Theorem 1.2 (densities of sums).** If independent scalar random variables have densities bounded by `K`, then every normalized linear combination has density bounded by `sqrt(2) K`. In particular, for a coefficient vector `a != 0` and cap-one independent coordinates,

   `||p_(a·X)||_infinity <= sqrt(2)/||a||_2`.                                  (2.1)

2. In the proof of **Theorem 8.1**, equation (8.4), the authors define

   `S_r(M)^2 = sum_{j=r+1}^infinity s_j(M)^2`                                  (2.2)

   and prove, for every integer `r>=0`,

   `L(MY, M0 t S_r(M)) <= (C_RV M0 p)^r`,                                    (2.3)

   when the independent coordinates of `Y` satisfy `L(Y_i,t)<=p`; `C_RV` is an absolute constant. For continuous cap-one coordinates, the paper's continuous specialization absorbs the one-dimensional convention into the same absolute constant. Taking `M0=1`, translation invariance of the concentration function gives the following cap-one consequence for every deterministic shift `alpha`:

   `P{ ||MY+alpha||_2 <= u } <= min{1,(C_RV u/S_r(M))^r}`.                    (2.4)

Equation (8.4), unlike the usual floored stable-rank corollary, permits an arbitrary integer `r`. This is the point of the transfer: choosing `r=2` measures the **entire Hilbert–Schmidt tail beyond the best rank-two approximation**, even when every individual tail singular value is tiny.

By Eckart–Young,

`S_r(M) = dist_HS(M,{rank <= r})`.                                             (2.5)

No Gaussian, moment, support, iid, log-concavity, or smoothness hypothesis is present in these source statements.

## 3. New theorem: spectral-tail cross density

### `QFORM-RV-SPECTRAL-TAIL-CROSS-v1`

Let `X in R^m` and `Y in R^n` be independent ORIGINAL-coordinate product banks, all coordinate densities bounded by one. Let `M` be a real `m x n` matrix, let `alpha in R^m`, and let `G(Y)` be an arbitrary measurable real function. Define

`R = X^T M Y + alpha^T X + G(Y)`.                                             (3.1)

For every integer `r>=2` with `S_r(M)>0`, the law of `R` has a density and

`||p_R||_infinity <= sqrt(2) C_RV [r/(r-1)] / S_r(M)`.                         (3.2)

In particular,

`boxed: ||p_R||_infinity <= 2 sqrt(2) C_RV / S_2(M).`                          (3.3)

This is an essential-supremum statement. Generic continuity is not asserted.

### Proof

Set

`Z = ||MY+alpha||_2`.                                                          (3.4)

From (2.4), for `S=S_r(M)>0`,

`P{Z<=u} <= min{1,(C_RV u/S)^r}`.                                             (3.5)

In particular `P{Z=0}=0`. Layer cake for the negative first moment gives

`E Z^(-1) = integral_0^infinity P{Z<=u} du/u^2`.                              (3.6)

Split at `u0=S/C_RV`. Then

`integral_0^u0 (C_RV u/S)^r du/u^2
 = (C_RV/S)/(r-1)`,                                                           (3.7)

while

`integral_u0^infinity du/u^2 = C_RV/S`.                                      (3.8)

Therefore

`E Z^(-1) <= (C_RV/S) r/(r-1)`.                                               (3.9)

Condition now on the genuine original `Y`-bank. For almost every `y`, `My+alpha !=0`; by Rudelson–Vershynin Theorem 1.2, (2.1),

`||p_(R|Y=y)||_infinity <= sqrt(2)/||My+alpha||_2`.                            (3.10)

Averaging the conditional densities and using (3.9) proves (3.2). This simultaneously proves absolute continuity. No independence is asserted among spectral coordinates of `MY`; only the original `X` and `Y` banks are independent. `square`

## 4. Full-ambient quadratic corollary

Split the ORIGINAL coordinates as `I disjoint_union J disjoint_union K`, and suppose only that the physical `I-I` block vanishes:

`A_II = 0`, `B=A_IJ`.                                                         (4.1)

All other blocks `A_JJ,A_IK,A_JK,A_KK` are arbitrary, and therefore arbitrary additional spectrum and signs are allowed.

Condition on `X_K`. The full quadratic form becomes

`Q = 2 X_I^T B X_J + alpha_K^T X_I + G_K(X_J) + c_K`,                         (4.2)

with `G_K` arbitrary. Applying (3.2) with `M=2B`, then averaging over `X_K`, yields for every `r>=2` with `S_r(B)>0`

`boxed: ||p_Q||_infinity <= (C_RV/sqrt(2)) [r/(r-1)] / S_r(B).`                (4.3)

For `r=2`,

`boxed: ||p_Q||_infinity <= sqrt(2) C_RV / dist_HS(B,{rank<=2}).`              (4.4)

Thus a zero-self cross block is automatically paid whenever its **aggregate** tail beyond rank two has nontrivial Hilbert–Schmidt mass, regardless of how tiny each individual tail singular value is. This is strictly different from a largest-singular-value or fixed-minor payment.

## 5. Equation-level application of the designated account04/B18 result

The newest completed designated-partner theorem is account04/B18 r6,

- scientific commit `48c914d1bd070cad090d6d5deac743bd8465bc15`,
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`,
- theorem `QFORM-TWOSIDED-ANCHOR-PAY-OR-RANK2-COLLAR-v1`.

For the physical packet

`A_S = [[0,C,r],[C^T,B,h],[r^T,h^T,a]]`,                                     (5.1)

write `D=[C r]` and let `c1>=c2` be the top two singular values of `P_r C`. The partner proves, for `theta>0`,

`c1 c2 >= theta  =>  ||p_Q||_infinity <= 2 sqrt(2 pi)/sqrt(theta)`,            (5.2)

while failure forces

`dist_op(D,{rank<=2}) < sqrt(theta)`.                                         (5.3)

Take the live scale `theta=2^-12`. Partner r6 gives

`||p_Q||_infinity <= 128 sqrt(2 pi) = 320.848419152768...`                    (5.4)

unless `c1 c2<2^-12`.

In the latter branch, apply (4.4) to the **same packet**, treating `(Y,W)` as the right original-coordinate bank. If

`dist_HS(D,{rank<=2}) = S_2(D) >= 1/64`,                                     (5.5)

then

`||p_Q||_infinity <= 64 sqrt(2) C_RV`.                                       (5.6)

Hence the combination gives the exhaustive paid-or-survivor reduction

`boxed: either ||p_Q||_infinity <= max{128 sqrt(2 pi),64 sqrt(2) C_RV},`
`       or c1 c2<2^-12 and dist_HS(D,{rank<=2})<1/64.}`                        (5.7)

This is a genuine sharpening of the partner's remaining operator-norm collar: a high-dimensional cloud of individually tiny cross singular values can lie in the operator collar while having large Hilbert–Schmidt tail, and is now paid. The remaining collar is Hilbert–Schmidt-close to rank two, not merely operator-close.

A literal equation-level partner application is obtained by `r=0`, `C=diag(1,1)`, and zero same-side curvature. Then `c1 c2=1`, so account04/B18 itself gives

`||p_Q||_infinity <= 2 sqrt(2 pi) = 5.013256549262...`.                       (5.8)

The associated pure cross quadratic matrix has eigenvalues `{1,1,-1,-1}` and is already inside the owner target.

## 6. A target-valid diffuse-tail family paid only after the new transfer

Let

`delta = 2^-13`, `N=16385`,

and let `D_N` have singular values

`1, delta, delta, ..., delta`                                                 (6.1)

with `N` copies of `delta`. Form

`A_N = [[0,D_N],[D_N^T,0]] direct_sum [1]`.                                   (6.2)

Its spectrum consists of `+/-1`, `N` copies each of `+/-delta`, and one additional `+1`. Therefore it has exactly three eigenvalues of modulus at least one and is a literal owner-target matrix.

For the partner packet with `r=0`,

`c1 c2 = delta = 2^-13 < 2^-12`,                                              (6.3)

so the partner's transverse-volume gate does not pay; it only records the small operator tail `s3(D_N)=delta<1/64`.

But

`S_2(D_N) = delta sqrt(N-1)
          = 2^-13 * 2^7
          = 1/64`.                                                            (6.4)

Thus the new source transfer gives the dimension-free bound

`boxed: ||p_(X^T A_N X)||_infinity <= 64 sqrt(2) C_RV`                        (6.5)

for every cap-one product input law, uniformly in this diffuse high-dimensional realization. This example is exactly why the Hilbert–Schmidt tail currency is useful inside an operator-norm low-rank collar.

## 7. Literature scope checks

- **Livshyts–Paouris–Pivovarov**, arXiv:1507.07949 / Israel J. Math. 216 (2016), gives sharp bounded densities of linear marginals of product measures. It remains a linear projection theorem; by itself it does not control an indefinite quadratic pushforward.
- **Herry–Malicet–Poly**, arXiv:2303.09488, studies quadratic-form regularity under substantially narrower iid / smooth Gaussian-functional hypotheses and does not match the arbitrary rough non-iid cap-one owner target.
- **Hu–Paouris**, arXiv:2403.20192 / JFA 290 (2026) 111309, gives small-ball bounds for simple random tensors; the available tensor profile does not itself yield an all-center linear-in-epsilon density bound for the present arbitrary quadratic form.
- **Kwan–Sauermann**, arXiv:2312.13826 / Compos. Math. 161 (2025/online 2026), resolves a quadratic Littlewood–Offord point-concentration problem under robust dependence. Point concentration for discrete/arbitrary laws is not the scale-linear continuous density statement required here.

No exact published theorem matching all owner quantifiers was found in this targeted check. This is a scope statement only, not a novelty claim.

## 8. What remains

The unrestricted conjecture is **OPEN / NOT PROVED**, and unrestricted continuity remains open.

The new implication materially narrows one live obstruction. In the account04/B18 two-sided-anchor geometry, after the partner's transverse-volume payment and the new spectral-tail payment, the first survivor satisfies simultaneously

`c1 c2 < 2^-12`,                                                              (8.1)

and

`dist_HS([C r],{rank<=2}) < 1/64`.                                            (8.2)

A future argument must retain this genuinely Hilbert–Schmidt-small cross tail exactly; arbitrary unbounded inputs forbid simply deleting it. The natural successor is a source-valid receiver for an exact/near rank-two carrier with same-side curvature, or a structural route from this collar into an already-paid active-plane, ridge, grouped-hub, or pair-log branch.

## 9. Source pins

- Rudelson–Vershynin primary source: arXiv:1402.4492v2, Theorem 1.2 and Theorem 8.1 proof equation (8.4).
- Designated partner: `yspennstate/math-open-problems@48c914d1bd070cad090d6d5deac743bd8465bc15`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260924T032058Z-account04-B18-QFORM-r6/REPORT.md`.
- Current brain programme/control at startup: `yspennstate/math-research-brain@09c764e74095f6305fa8606a11a53a56431fa0b8`, OWNER CONTROL revision `2026-09-22.15`.
