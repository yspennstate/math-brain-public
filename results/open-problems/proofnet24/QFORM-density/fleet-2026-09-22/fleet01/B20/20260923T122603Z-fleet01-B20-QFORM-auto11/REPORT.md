# fleet01/B20 — strengthened N3 two-scale closure compiler

**Status:** `ESSENTIAL_STEP_APPLIED`. The full QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN** separately. Execution label: `WITHOUT_VERIFIED_BRAIN`.

Run id: `20260923T122603Z-fleet01-B20-QFORM-auto11`.

## 1. Exact target and source discipline

Target: for arbitrary independent real `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with a universal finite constant, or give a valid counterexample. Continuity is tracked separately.

No Gaussianity, moments, iid assumption, compact support, log-concavity, or post-rotation independence is used. The known false uniform pointwise quadratic oscillatory-decay route is not used. Small spectral tails are not deleted from the random quadratic form.

Fresh designated completed partner actually consumed: fleet02/B20, canonical mathematics `yspennstate/math-open-problems@19327f690f815425717fcbd07854302df2090970`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T112426Z-fleet02-B20-QFORM-auto11/REPORT.md`; source-pinned brain handoff was read from its committed fleet02/B20 handoff. Its N3 compiler supplies, in particular, the source-valid inequality

`(A^2)_hh >= (P_0)_hh`,  where `P_0 = 1_{|A|>=1}`,

and keeps the arbitrary extra spectrum rather than truncating the law. I apply that inequality below at the actual new threshold `1/60`.

Prior own compiler: `yspennstate/math-open-problems@0a22623e8aa296bfdb618b8952fbd186c670c55c`, fleet01/B20 run `20260923T114521Z-fleet01-B20-QFORM-auto11`. It paid the N3 star branch above leverage `1/32` unless a four-direction leaf packet survived, and paid the spectral-window branch at threshold `1/64` under leverage `5/128`.

Completed analytic receiver used here: the ridge-leverage density theorem at `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. For a physical cross block `B`, ridge scale `gamma`, and `q=1`, if `max_i K_gamma,ii<=1/2` and `theta=tr K_gamma>2`, then the full ambient form has a continuous `C_0` density and

`||p_Q||_infinity <= sqrt(e)/(sqrt(2) gamma) * theta/(theta-2)`.

The unrestricted fifth-volume receiver `D_5` used below is the previously completed theorem

`||p_Q||_infinity <= 5 sqrt(2e) e_5(N^T N)^(-1/10)`

for any genuine original-coordinate cross block `N`, with same-side blocks and outside couplings retained.

## 2. N3 setup

Let `tau=1/64` and assume the current partner state lies in `N3(tau)`:

1. `s_3(A)>=1`;
2. `|A_ii|<tau` for every physical coordinate;
3. `|A_ii A_jj-A_ij^2|<tau` for every `i!=j`.

Then every physical edge obeys

`A_ij^2 < tau+tau^2 = 65/4096`.                                      (2.1)

Indeed `A_ij^2 <= |A_iiA_jj-A_ij^2|+|A_iiA_jj|`.

## 3. New theorem: high spectral leverage `1/60` already forces the balanced-star packet

### Theorem 3.1 — `QFORM-N3-1OVER60-STAR-BALANCED-CUT-v1`

Let `P_0=1_{|A|>=1}`. If some original physical coordinate `h` satisfies

`(P_0)_hh >= 1/60`,                                                   (3.1)

then there is a physical partition of the leaves

`h^c = J disjoint_union K`

such that

`sum_{j in J} A_hj^2 > 17/61440`,

`sum_{k in K} A_hk^2 > 17/61440`,                                    (3.2)

and

`||A[J,K]||_F^2 > 3969/16384`.                                       (3.3)

#### Proof

The completed fleet02/B20 inequality gives

`(A^2)_hh >= (P_0)_hh >=1/60`.

Hence, with `w_j=A_hj^2` and `S=sum_{j!=h}w_j`, the N3 diagonal bound gives

`S=(A^2)_hh-A_hh^2 > 1/60-1/4096 =1009/61440`.                       (3.4)

By (2.1), every atom has

`w_j<65/4096`.                                                        (3.5)

Sort the weights decreasingly, append one zero if necessary, pair consecutive weights, and orient each pair so exactly one endpoint is in `J` and the other in `K`. For every orientation the star discrepancy is bounded by

`|sum_J w_j-sum_K w_j| <= (w_1-w_2)+(w_3-w_4)+... <=w_1<65/4096`.

Together with (3.4), each bank therefore receives more than

`(1009/61440-65/4096)/2 =17/61440`,

which proves (3.2), independently of how the pair orientations are chosen.

Now let `B=A[h^c,h^c]`. If `p` eigenvalues of `A` are at least one and `q` are at most minus one, `p+q>=3`. Cauchy interlacing after deleting coordinate `h` leaves at least

`max(p-1,0)+max(q-1,0)>=1`

eigenvalue of `B` with modulus at least one. Thus `||B||_op>=1`. Write `B=D+Z`, with `D=diag B` and `Z` zero diagonal. Since `||D||_op<1/64`,

`||Z||_op>63/64`, and therefore

`||Z||_F^2>3969/4096`.                                                (3.6)

Randomly and independently orient the consecutive pairs above. For every ordered pair of distinct leaves `(j,k)`, the probability of `j in J, k in K` is at least `1/4` (it is `1/2` if `j,k` form one paired block). Consequently

`E ||A[J,K]||_F^2 >= (1/4)||Z||_F^2 >3969/16384`.

Some orientation attains this expectation, while (3.2) held for every orientation. QED.

This strictly lowers the previous fleet01/B20 useful `P_0` leverage threshold from `1/32` to `1/60`.

## 4. Fifth-volume payment remains valid at the lower star threshold

For `N=A[J,K]`, let `x_r=s_r(N)^2` and `E_1=sum_r x_r=||N||_F^2`. If

`sum_{r<=4}x_r <=(63/64)E_1`,

then five iid draws from the probability weights `p_r=x_r/E_1` are all distinct with probability at least `(1/64)^4`: after at most four distinct indices have appeared, their total mass is at most the mass of the four largest atoms, namely at most `63/64`. Since the probability of five distinct draws is `5! e_5(p)`,

`e_5(N^TN) >= (1/64)^4 E_1^5/120`.

Using (3.3) in the completed unrestricted `D_5` theorem gives

`||p_Q||_infinity`
` <=5 sqrt(2e) [120/((1/64)^4(3969/16384)^5)]^(1/10)`
` =201.786346662743... <201.787`.                                    (4.1)

This paid branch has a continuous `C_0` density.

Thus every unpaid state satisfying (3.1) has one physical hub and one physical partition `J,K` with

`sum_{J}A_hj^2>17/61440`,

`sum_{K}A_hk^2>17/61440`,

`||A[J,K]||_F^2>3969/16384`,

and

`sum_{r<=4}s_r(A[J,K])^2 >(63/64)||A[J,K]||_F^2`
`                         >250047/1048576`.                          (4.2)

The remaining singular tail is retained; (4.2) is not replaced by an exact rank-four assertion.

## 5. New theorem: a higher spectral window `[1/16,infinity)` is paid at leverage `1/50`

### Theorem 5.1 — `QFORM-SPECTRAL-WINDOW-1OVER16-1OVER50-v1`

Let `A` be any real symmetric matrix with at least three eigenvalues of modulus at least one and put

`P_16 = 1_{|A|>=1/16}`.

If

`max_i (P_16)_ii <=1/50`,                                            (5.1)

then for arbitrary independent cap-one coordinate densities, `Q=X^TAX` has a continuous `C_0` density and

`||p_Q||_infinity <= 5400 sqrt(e)/(29 sqrt(2))`
`                  =217.084094838352... <217.085`.                   (5.2)

#### Proof

Write `A=A_H+E`, where `A_H=U Lambda U^T` is the spectral truncation to `|lambda|>=1/16`. Thus `||E||_op<eta=1/16`, `U^TU=I`, and each physical row `u_i` of `U` satisfies `||u_i||^2<=epsilon=1/50`.

The two-part MSS frame partition gives physical banks `I,J` for which both partial Gram matrices are bounded below by

`delta I`, where

`delta=1-(1/sqrt(2)+sqrt(epsilon))^2`
`     =1/2-sqrt(2/50)-1/50`
`     =7/25`.                                                         (5.3)

Let `B_0=A_H[I,J]=U_I Lambda U_J^T`. Both `U_I` and `U_J` have least singular value at least `sqrt(delta)`. Since `Lambda` has at least three singular values at least one,

`s_3(B_0)>=delta=7/25`.                                               (5.4)

Moreover `range(B_0)=range(U_I)`, and its physical range-projection leverage is bounded by

`max_i (P_range(B_0))_ii <= epsilon/delta =1/14`.                    (5.5)

Restore the full spectral tail `F=E[I,J]`, with `||F||_op<=eta=1/16`. Weyl gives, for the actual physical cross block `B=A[I,J]`,

`s_3(B)>=sigma:=delta-eta=87/400`.                                   (5.6)

Choose the ridge scale

`gamma=(2/3)sigma=29/200`.                                           (5.7)

The completed ridge-stability lemma applied to `B=B_0+F` and (5.5) gives

`max_i (K_gamma)_ii`
` <= (1/sqrt(14)+(1/16)/(29/200))^2`
` = (1/sqrt(14)+25/58)^2`
` <1/2`.                                                             (5.8)

For completeness the final strict inequality has a rational proof: `1/sqrt(2)>7/10`, `1/sqrt(14)<15/56`, and

`7/10-15/56=121/280>25/58`

because `7018>7000`. Thus `1/sqrt(14)+25/58<1/sqrt(2)`.

The three singular values in (5.6) imply ridge effective dimension

`theta=tr K_gamma >=3 sigma^2/(gamma^2+sigma^2)`
`                    =3/(1+4/9)=27/13>2`.                           (5.9)

Apply the completed ridge density theorem with `q=1`. Since `theta/(theta-2)` decreases for `theta>2`, (5.9) yields

`||p_Q||_infinity`
` <= sqrt(e)/(sqrt(2) gamma) * 27`
` =5400 sqrt(e)/(29 sqrt(2))<217.085`.

The receiver also supplies continuity and vanishing at infinity. All banks are original-coordinate banks; no independence after the spectral decomposition is asserted. QED.

## 6. New exhaustive N3 two-scale compiler

Combine Sections 3–5. Every N3 state produced by the completed fleet02/B20 reduction satisfies at least one of the following.

**(A) Paid fifth-volume star branch:** `||p_Q||_infinity<201.787`, continuously.

**(B) Expanded physical star/four-direction packet:** there are a physical hub `h` and a partition `h^c=J disjoint_union K` for which

`sum_J A_hj^2>17/61440`, `sum_K A_hk^2>17/61440`,

`||A[J,K]||_F^2>3969/16384`, and

`sum_{r<=4}s_r(A[J,K])^2>250047/1048576`.

**(C) Paid `1/16` spectral-window branch:** `||p_Q||_infinity<217.085`, continuously.

**(D) Higher annular-leverage packet:** there is an original physical coordinate `h` for which

`(P_0)_hh<1/60`, `(P_16)_hh>1/50`.

Indeed, if (A)/(B) do not occur, no coordinate can have `(P_0)_hh>=1/60`. If (C) also does not occur, some coordinate has `(P_16)_hh>1/50`. At that same coordinate, with

`R_16=1_{1/16<=|A|<1}=P_16-P_0`,

one has

`(R_16)_hh >1/50-1/60 =1/300`.                                      (6.1)

Since every spectral value on `R_16` has modulus at least `1/16`,

`((A R_16)^2)_hh >= (1/16)^2 (R_16)_hh >1/76800`.                   (6.2)

This is a strict strengthening of the preceding fleet01/B20 survivor, which only forced fixed leverage/energy in the wider `[1/64,1)` annulus. The current obstruction is pushed to the higher `[1/16,1)` spectral band and the high-`P_0` threshold is lowered at the same time.

## 7. First unpaid implication

The first remaining implication is now

`QFORM-N3-R16-OR-STAR4DIR-PAYMENT-v1`.

It suffices to pay either:

1. the expanded physical star/four-direction packet (B), retaining its small singular tail; or
2. the higher annular packet (D), with `(R_16)_hh>1/300` and `((A R_16)^2)_hh>1/76800`, by converting this deterministic spectral energy into a product-preserving physical bank/pivot/ridge/volume receiver.

Crucially, `R_16 X` is **not** an independent random coordinate and may not be conditioned on as if spectral rotation preserved the product law.

## 8. Corrections and scope

No step uses uniform pointwise quadratic Fourier decay for arbitrary cap-one densities; that statement is known false. No step assumes independence after orthogonal rotation, applies arbitrary-joint 3D coarea, deletes a small quadratic term, takes a worst-fiber conditional supremum as a global bound, or converts aggregate determinant/energy mass into one good coefficient without a proved selection mechanism.

The full theorem is therefore not claimed. What is proved is the two new supporting theorems and the explicit N3 compiler above. Continuity is proved only on the paid fifth-volume/ridge branches, while the full-target continuity question remains open.

## 9. Arithmetic self-check

`checks.py` in this immutable run directory verifies the rational constants and numerical density bounds. `check_results.txt` records the executed output and ends `STATUS=PASS`. This is a self-check, not an independent audit.
