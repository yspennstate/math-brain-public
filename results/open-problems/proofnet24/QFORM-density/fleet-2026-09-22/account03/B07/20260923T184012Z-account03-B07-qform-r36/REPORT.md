SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-23T18:40:12Z.
attacking: the r35 low-E3 rank-two interface survivor — sharpen the determinant-weighted heavy-marginal geometry, then pay an exact flat-side rank-two crossing branch without discarding the interface tail.

# account03/B07 r36 — E2 heavy marginals force rank one or a quantitatively nondegenerate rank-two carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Run: `20260923T184012Z-account03-B07-qform-r36`  
Initial fresh brain main: `fa7daf47cc710d11bf732d922f29c4c5b7f26b2a`  
Pre-publication brain main: `d26e91fa027fd3a6a369b1d41a198d0ccdad7c95`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Execution: `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
Status: **NEW SUPPORTING DETERMINANT-WEIGHTED DICHOTOMY + NEW FLAT-SIDE ANALYTIC RECEIVER / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

The unrestricted conjecture is not proved or disproved here. No Gaussian, log-concave, moment, compact-support, connected-support, iid, post-rotation-independence, pointwise van-der-Corput, arbitrary-joint coarea, fiber-supremum, or deletion-of-a-small-quadratic-tail hypothesis is used. All coefficient blocks are on literal original-coordinate banks.

## 1. Source-pinned incoming state

The previous B07 report is

`yspennstate/math-open-problems@3a3334245375f0d72687f3cb482b4478d51f3188`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260923T173750Z-account03-B07-qform-r35/REPORT.md`.

Its incoming branch has disjoint original-coordinate banks `L,R` and

`K=A[L,R]`,

with

`Z:=e_2(KK^T)>Z_0 h^4`,

`Z_0=854675.100194511`,

`h=(2sqrt(2)-1)/1572864=1.1624826588606455e-6`.

For any column extension `T=[K Y]` on the same physical row bank, put

`V=e_3(TT^T)`.

The r35 two-compound defect argument produces a spectral projection `P` spanned by the singular directions of `K` whose natural E2 inclusion marginal is larger than `2/3`, with

`rank(P)<=2`,

and

`||(I-P)T||_F^2 <= 9V/Z`.                                        (1.1)

Applied to the full physical interfaces

`T_L=A[L,L^c]`, `T_R=A[R,R^c]`,

the branch `V<h^6` therefore has retained Frobenius tail below

`3/sqrt(Z_0) h <0.003245045040 h`.                                (1.2)

If instead either interface has `V>=h^6`, the completed account03/B02 marginal-free E3 theorem at

`yspennstate/math-open-problems@52cef3abd27c641ae6666d6ee3bbc25d90cb4813`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`

already gives the full ambient law a continuous `C_0` density with

`||p_Q||_infinity <=10.550168831164775/h <9.076e6`.               (1.3)

The designated partner result used quantitatively below is account04/B07 r1,

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T091740Z-account04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

At the actual strict-N3 threshold it supplies the literal physical coefficient cap

`|A_ij|<=h/8`                                                     (1.4)

on the relevant off-diagonal coefficients. The newer account04/B07 coordinate-core report at commit `dab16464e87c939cc0cf3fd01d070045290192fa` was also refreshed. Its diagonal-plus-rank payment requires large physical diagonals and is not silently applied in this tiny-diagonal chamber.

For the analytic lemma in Section 3 I use only the standard orthonormal product-projection bound explicitly recorded in the current projected-crossing proof

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`:

a rank-r orthonormal projection of independent scalar cap-one inputs has density at most `2^(r/2)`.

## 2. Sharpening the r35 heavy-marginal alternative

Let the positive squared singular values of `K` be `x_1,x_2,...`; set

`S=sum_r x_r`,

`Z=sum_{p<q}x_p x_q=e_2(KK^T)`,

and define the natural E2 inclusion marginals

`alpha_r=x_r(S-x_r)/Z`.                                          (2.1)

Every pair `x_p x_q` is counted twice, hence

`sum_r alpha_r=2`.                                                (2.2)

Let `P` be the span of those singular vectors with `alpha_r>2/3`. Equation (2.2) gives `rank(P)<=2`.

### Theorem 2.1 — `QFORM-E2-INTERFACE-R1-OR-NONDEGENERATE-R2-v1`

For every physical extension `T=[K Y]`, one of the following holds.

1. `rank(P)<=1`, and

   `dist_F(T,{rank<=1}) <= 3 sqrt(V/Z)`.                          (2.3)

2. `rank(P)=2`, and simultaneously

   `dist_F(T,{rank<=2}) <= 3 sqrt(V/Z)`,                          (2.4)

   `s_1(T)s_2(T) > sqrt(Z/3)`.                                   (2.5)

Thus the only genuinely rank-two low-E3 survivor has a quantitatively nondegenerate two-dimensional carrier; it cannot be an arbitrarily ill-conditioned rank-two approximation.

### Proof

The distance statements follow immediately from (1.1): `PT` has rank at most `rank(P)`.

It remains to prove (2.5). Suppose `rank(P)=2`, with heavy squared singular values `x_p,x_q`. Put

`B=x_p+x_q`,

`T_0=sum_{r notin {p,q}}x_r`,

`E_0=sum_{r<s; r,s notin {p,q}}x_r x_s`.

Then

`Z=x_p x_q+B T_0+E_0`.                                            (2.6)

Moreover

`alpha_p+alpha_q
 =(2x_p x_q+B T_0)/Z
 >4/3`.                                                           (2.7)

Multiplying (2.7) by `3Z` and using (2.6) gives

`2x_p x_q > B T_0+4E_0`.                                         (2.8)

In particular

`Z=x_p x_q+B T_0+E_0 <3x_p x_q`,                                 (2.9)

so

`x_p x_q>Z/3`.                                                    (2.10)

The two largest squared singular values of `K` have product at least `x_p x_q`. Also

`TT^T=KK^T+YY^T >= KK^T`

in Loewner order, so each ordered eigenvalue of `TT^T` is at least the corresponding eigenvalue of `KK^T`. Hence

`s_1(T)^2 s_2(T)^2 >= x_p x_q>Z/3`,

which is (2.5). QED.

### Current numerical packet

On the r35 low-E3 branch `V<h^6`, (2.3)-(2.5) become the explicit alternative

`dist_F(T,{rank<=1})<0.003245045040 h`,                            (2.11)

or

`dist_F(T,{rank<=2})<0.003245045040 h`,

`s_1(T)s_2(T)>sqrt(Z_0/3)h^2
              =533.7524707810138 h^2`.                            (2.12)

This applies separately to `T_L` and `T_R`. The nonzero tails remain part of the actual coefficient matrix; they are not deleted.

## 3. A direct analytic receiver for a flat physical side

The remaining r35 debt is analytic: arbitrary internal curvature on the selected bank can interact with the rank-two crossing carrier. Before attempting that full curvature problem, the following exact flat-side branch can be paid end-to-end while retaining the *entire* cross block, including its nonzero tail.

### Theorem 3.1 — `QFORM-FLAT-SIDE-R2-CROSS-SMALLBALL-v1`

Let `X=(X_i)_{i in L}` and `Y=(Y_j)_{j in R}` be independent groups of independent scalar random variables, every scalar density bounded by one. Let `C` be a real `|L| x |R|` matrix with

`s_1(C)s_2(C)>0`.

For any fixed vector `a` and any measurable real `G(Y)`, define

`Q=a^T X+2X^T C Y+G(Y)`.                                         (3.1)

Then the law of `Q` is absolutely continuous and

`boxed: ||p_Q||_infinity <= 2 sqrt(pi/(s_1(C)s_2(C))).`           (3.2)

Continuity is not claimed.

### Proof

Fix `Y=y`. With

`b(y)=a+2Cy`,

(3.1) is a translate of the one-dimensional linear projection `b(y)^T X`. The rank-one product-projection bound gives, for every interval `I`,

`P(Q in I |Y=y) <= sqrt(2)|I|/||b(y)||`                           (3.3)

whenever `b(y)!=0`.

Let `u_1,u_2` and `v_1,v_2` be the top two left/right singular vectors of `C`, and let

`Sigma=diag(s_1(C),s_2(C))`,

`Z_2=(v_1^T Y,v_2^T Y)`.

The two-dimensional product-projection theorem gives a Lebesgue density for `Z_2` bounded by `2`. Projecting `b(Y)` onto `span{u_1,u_2}` yields

`||b(Y)|| >= ||a'+2 Sigma Z_2||`,                                (3.4)

where `a'=(u_1^T a,u_2^T a)`.

Set `W=a'+2Sigma Z_2`. Since the linear map `z -> a'+2Sigma z` has determinant `4s_1s_2`, `W` has a two-dimensional density bounded by

`N=1/(2s_1s_2)`.                                                  (3.5)

For any two-dimensional probability density `q<=N`, uniformly in its translation,

`E[1/|W|]
 =integral_0^infinity P(|W|<1/t) dt
 <=integral_0^infinity min(1,N pi/t^2) dt
 =2sqrt(pi N).`                                                   (3.6)

Therefore

`E[1/||b(Y)||]
 <=sqrt(2pi/(s_1s_2)).`                                          (3.7)

The exceptional event `b(Y)=0` has probability zero: it forces the absolutely continuous two-dimensional projection `Z_2` to equal one fixed point. Averaging (3.3) and using (3.7) gives

`P(Q in I)
 <=2 sqrt(pi/(s_1s_2)) |I|`.                                     (3.8)

The interval small-ball inequality implies absolute continuity and the essential density bound (3.2) by the Radon--Nikodym theorem/Lebesgue differentiation. QED.

This proof conditions only on original-coordinate groups. It does not diagonalize the random vector, and `G` may contain arbitrary quadratic curvature and couplings on the entire `Y` side.

## 4. Paid subbranch of the actual r35 interface packet

Apply Theorem 3.1 to the literal partition `L union L^c=[n]` when the physical self block on the selected side is exactly flat:

`A[L,L]=0`.                                                       (4.1)

Then

`X^TAX=2X_L^T T_L X_{L^c}+X_{L^c}^T A[L^c,L^c]X_{L^c}`,

so Theorem 3.1 applies with `C=T_L`, `a=0`, and arbitrary complement curvature retained.

If the low-E3 branch of Theorem 2.1 is in its two-heavy case, (2.12) gives

`s_1(T_L)s_2(T_L)>533.7524707810138 h^2`.

Consequently the full ambient law satisfies

`boxed:
||p_Q||_infinity
 < 2sqrt(pi)/(sqrt(533.7524707810138) h)
 =131992.27054475868.
`                                                                    (4.2)

This is an **essential bounded-density** conclusion for the exact flat-side subbranch; continuity is not established by this small-ball proof.

If instead the E2-heavy space has dimension at most one, the same low-E3 packet is sharpened from the r35 rank-two tube to the rank-one tube (2.11). Thus the unpaid geometry is now strictly smaller: either genuine internal curvature must interact with a nondegenerate two-direction crossing carrier, or the whole interface is quantitatively rank one.

## 5. Required designated-partner application at an actual inequality

Use the completed account04/B07 cap (1.4) on the actual off-diagonal entries of `T_L`. In the nondegenerate rank-two branch,

`||T_L||_F^2 >=s_1(T_L)^2+s_2(T_L)^2
              >=2s_1(T_L)s_2(T_L)
              >1067.5049415620276 h^2`.                           (5.1)

Every nonzero physical interface entry contributes at most `h^2/64` to the Frobenius square. Hence, if `N` is the number of nonzero literal physical entries in `T_L`,

`N h^2/64 >1067.5049415620276 h^2`,

so

`boxed: N>=68321.`                                                (5.2)

This is an equation-level application of the designated account04/B07 result. It shows that the surviving nondegenerate rank-two interface is necessarily highly diffuse under the actual strict-N3 coefficient cap; the count itself is structural currency, not a density proof.

## 6. Relation to same-hour aggregate-minor work

The same-hour account01/B07 report at

`yspennstate/math-open-problems@4e714d23f0673acdf71809b29fc99b469b2944aa`

proves a complementary spectral extension theorem: arbitrary determinant-weighted physical E2 packets lift to fractional E3 currency under `s_3(A)>=1` before any reciprocal minor selection. That theorem does not pay the current low-E3 rank-two-interface curvature branch, and I do not use it as a premise here. It reinforces that aggregate determinant weight, rather than a single selected minor, is the correct currency.

## 7. Remaining implication

The first B07 debt is now

`QFORM-NONDEGENERATE-R2-INTERFACE-WITH-CURVATURE-RECEIVER-v1`:

> Starting from a literal original-coordinate interface `T=A[L,L^c]` satisfying the retained-tail estimate
> `dist_F(T,rank<=2)<0.003245045040 h`
> and the carrier lower bound
> `s_1(T)s_2(T)>533.7524707810138 h^2`,
> pay the full ambient quadratic form when `A[L,L]` is arbitrary rather than exactly zero, without deleting the nonzero interface tail or using moments. Alternatively show that arbitrary same-bank curvature forces a new physical E3 packet or a bounded physical principal core.

The companion rank-one-interface branch remains a separate lower-complexity debt. The r34 hub/12-bank and 12-by-2-grid siblings also remain separate branches.

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** The previously paid E3 branch is continuous; the new exact flat-side branch proves essential boundedness only.

## 8. Regression checks

`CHECKS.py` and `CHECKS.txt` sit beside this report. They test 18,000 positive singular-value spectra for the heavy-marginal algebra, including 14,417 two-heavy cases, and verify the propagated constants and the integer `68321` diffusion count. The captured output ends `STATUS=PASS`.

Those finite computations are regression evidence only. The proofs above are the algebraic and measure-theoretic arguments in Sections 2-5.
