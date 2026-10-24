SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T10:29:30Z.
attacking: extremal product laws, then an exterior-energy ladder that turns a high slab ratio into a dimension-free operator-norm low-rank skeleton without rotating the product source.

# account01/B13 auto20 — exact barycentric purification and an exterior-ratio operator-norm skeleton

Status: **ESSENTIAL STEP APPLIED / PROVED SUPPORTING REDUCTION + PROVED TARGET-LEVEL STRUCTURAL CONSEQUENCE / FULL QFORM OPEN / CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

The full target remains open. Nothing below asserts a universal density constant for every admissible matrix. The new structural theorem is useful because it replaces the preceding entrywise-small residual by an **operator-norm-small residual**, with fixed rank and fixed physical core, for every sufficiently high-output-density witness. It does not perturbatively delete that residual on arbitrary translated/fragmented product supports.

## 1. Current source pins and corrections

Fresh owner control before publication remained QFORM-only, revision `2026-09-22.15`. The live programme continues to mark the full conjecture OPEN and separately marks continuity OPEN.

The designated partner result actually applied is `account02/B13` r24:

- `yspennstate/math-open-problems@cc40e95933db0262eddb6e679211145a84dca081`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T085705Z-account02-B13-extremal-r24/REPORT.md`.

Its cut-free higher exterior theorem states that, for

`D_r^perp(A) = sum_{P,Q: |P|=|Q|=r, P cap Q=empty} det(A[P,Q])^2`,

and every integer `r>=5`,

`||p_Q||_infinity <= C_r [D_r^perp(A)]^(-1/(2r))`,
`C_r = 2 sqrt(2e) r/(r-4)`.

In particular

`C_5 = 10 sqrt(2e) = 23.316439815971...`,

so an actual slab ratio `rho=P(Q in J)/|J|` forces

`D_5^perp(A) <= (C_5/rho)^10`.                                    (1.1)

The rank-three physical-principal-block receiver used below is the orientation-free rank-two/rank-three synthesis:

- `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`
- `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

For an invertible original-coordinate `3 x 3` principal block `M`, and a chosen coordinate in that block with `a=M_ii!=0`, the full ambient quadratic form, with arbitrary outside coefficients and couplings, satisfies

`||p_Q||_infinity <= 128 [ |a| |det M| ]^(-1/4)`.                (1.2)

Here the spectral frame inside the three-coordinate block is the identity, so the row-leverage factor in the general source theorem is one.

The proof below respects the live corrections: no pointwise quadratic oscillatory decay, no independence after a physical-coordinate rotation, no arbitrary-joint coarea estimate, no conditional projection-density cap, no bounded support diameter, no fixed fragment count, and no one-good-minor implication from the bare three-eigenvalue hypothesis.

## 2. Exact barycentric purification of one cap-one law

The previous fleet results gave equality of suprema and finite-family approximation by bounded finite-union indicators. For the geometric formulation it is useful to have an exact law-level barycentric identity.

### Theorem 2.1 — `QFORM-EXACT-BARYCENTRIC-PRODUCT-PURIFICATION-v1`

Let `f:R-> [0,1]` be measurable with `int_R f=1`. There is a probability mixture of measurable sets `E subset R`, each satisfying `|E|=1`, such that, as finite measures,

`f(x) dx = integral 1_E(x) dx dPi(E)`.                             (2.1)

Equivalently, for every nonnegative measurable `h`,

`int h(x) f(x) dx = integral [ int_E h(x) dx ] dPi(E)`.          (2.2)

Consequently, for finitely many marginals `f_1,...,f_n`, one may take the product of the corresponding mixing laws. For every nonnegative measurable kernel `K:R^n->[0,infinity]`,

`int K(x) prod_i f_i(x_i) dx`
` = integral ... integral [ int_{prod_i E_i} K(x) dx ] prod_i dPi_i(E_i)`.    (2.3)

In particular, for every fixed symmetric `A` and interval `J`,

`P_f{X^T A X in J}`
` = E_E |{x in prod_i E_i : x^T A x in J}|`.                    (2.4)

Thus every strict slab violation by arbitrary cap-one product laws is witnessed, with **no loss at all**, by some tuple of arbitrary measurable unit-measure product sets. This theorem does **not** assert a single interval, centered uniform law, bounded diameter, finite fragment count, or attained global optimizer in a restricted class.

#### Proof

Partition the line into unit intervals `I_m=[m,m+1)`, `m in Z`, and put

`alpha_m = int_{I_m} f`, so `0<=alpha_m<=1` and `sum_m alpha_m=1`.

For each `m`, consider the convex set

`K_m={g in L^infinity(I_m): 0<=g<=1, int_{I_m}g=alpha_m}`.       (2.5)

On the weak-* topology `sigma(L^infinity,L^1)`, `K_m` is compact and metrizable because `L^1(I_m)` is separable. Its extreme points are precisely the indicator classes `1_F` with measurable `F subset I_m` and `|F|=alpha_m`.

Indeed, an indicator is extreme. Conversely, if `g` is not zero-one almost everywhere, then for some `epsilon>0` the set `{epsilon<g<1-epsilon}` has positive measure. By nonatomicity split a positive-measure part into equal-measure sets `U,V`; for sufficiently small `delta>0`, both

`g +/- delta(1_U-1_V)`

still belong to `K_m` and are distinct, so `g` is not extreme.

By the metrizable Choquet theorem, the restriction `f|_{I_m}` is the barycenter of a probability measure `Pi_m` supported on those extreme points. Therefore, for every `h in L^1(I_m)`,

`int_{I_m} h f = integral [int_F h] dPi_m(F)`.                  (2.6)

Take the countable product of the `Pi_m`, choose one `F_m subset I_m` from each factor, and put `E=union_m F_m`. Since `|F_m|=alpha_m` deterministically,

`|E|=sum_m alpha_m=1`.                                            (2.7)

Summing (2.6) over `m`, first for nonnegative simple `h` and then by monotone convergence, proves (2.2). Tensoring the finite collection of marginal barycenters and applying Tonelli proves (2.3). Equation (2.4) is the special case `K=1_{x^T A x in J}`. QED.

Remark. The previously proved finite-union approximation remains useful for finite computational witnesses, but the exact identity above naturally lives on arbitrary measurable unit sets, exactly as required by the corrected scope.

## 3. Exterior-ratio Frobenius/operator-norm skeleton

The preceding B13 max-volume skeleton controlled a residual entry-by-entry. The next theorem instead averages over **all** disjoint base minors and obtains a dimension-free Frobenius, hence operator-norm, remainder.

### Theorem 3.1 — `QFORM-EXTERIOR-RATIO-FROBENIUS-SKELETON-v1`

Let `A` be a finite real symmetric matrix and let `r>=1`. If

`D_r^perp(A)>0`,

then there are a diagonal matrix `D`, a symmetric matrix `R`, a symmetric matrix `E`, and disjoint physical sets `P,Q` with `|P|=|Q|=r`, such that, with `S=P union Q`,

`A=D+R+E`,                                                        (3.1)
`rank R <= 4r`,                                                   (3.2)
`E_ii=0`,                                                         (3.3)
`E_ij=0` whenever `i in S` or `j in S`,                           (3.4)

and

`||E||_op <= ||E||_F`
` <= (r+1) sqrt( D_{r+1}^perp(A) / D_r^perp(A) )`.              (3.5)

In particular, if `D_{r+1}^perp(A)=0`, then `E=0` and

`A = diagonal + symmetric rank <=4r`.                             (3.6)

#### Proof

For a disjoint base pair `(P,Q)` with `|P|=|Q|=r` and invertible

`B=A[P,Q]`, `beta=det B`,

let `K=(P union Q)^c`. For distinct `k,l in K`, define the directed Schur residual

`delta_{kl}^{P,Q}`
` = A_kl - A[k,Q] B^{-1} A[P,l]`.                                (3.7)

The block determinant identity gives exactly

`det A[P union {k}, Q union {l}] = beta delta_{kl}^{P,Q}`.       (3.8)

Hence, writing

`G(P,Q)=sum_{k,l in K, k!=l} det A[P union{k},Q union{l}]^2`,

we have

`G(P,Q)=beta^2 sum_{k!=l} (delta_{kl}^{P,Q})^2`.                 (3.9)

Now sum `G(P,Q)` over all disjoint base pairs. Each disjoint `(r+1)x(r+1)` minor `A[P',Q']` is counted exactly `(r+1)^2` times: choose which row of `P'` and which column of `Q'` were added last. Therefore

`sum_{all base P,Q} G(P,Q) = (r+1)^2 D_{r+1}^perp(A)`.           (3.10)

Restricting the nonnegative left side to the invertible bases can only decrease it. Meanwhile

`sum_{invertible base P,Q} beta^2 = D_r^perp(A)`,                (3.11)

because singular bases contribute zero to `D_r^perp`. Thus a weighted-average argument gives at least one invertible disjoint base `(P,Q)` for which

`sum_{k!=l}(delta_{kl}^{P,Q})^2`
` <= (r+1)^2 D_{r+1}^perp(A)/D_r^perp(A)`.                      (3.12)

Fix that base. Use the symmetric Nyström completion already established in the earlier B13 skeleton. On the `2r`-coordinate core `S=P union Q`, put

`H = [[0,2B],[2B^T,0]]`,

and let `C=A[S,K]`. Define the symmetric rank-`2r` matrix `R_1` by

`(R_1)_{SS}=H`, `(R_1)_{SK}=C`, `(R_1)_{KS}=C^T`,
`(R_1)_{KK}=C^T H^{-1}C`.                                       (3.13)

Its Schur complement in the core is zero, so `rank R_1=2r`. Add a symmetric correction `R_2` supported on `S x S`, with zero diagonal, so that `R_1+R_2` matches every off-diagonal entry of `A` inside the core. Then `rank R_2<=2r`. Put `R=R_1+R_2`, let `D` be the diagonal part of `A-R`, and set `E=A-D-R`. This gives (3.1)-(3.4) and `rank R<=4r`.

For distinct `k,l in K`, the `KK` entry of (3.13) is the average of the two directed Nyström predictions, hence, by symmetry of `A`,

`E_kl = (delta_{kl}^{P,Q}+delta_{lk}^{P,Q})/2`.                  (3.14)

Therefore

`sum_{k!=l} E_kl^2`
` <= sum_{k!=l} (delta_{kl}^{P,Q})^2`,                            (3.15)

by `(u+v)^2/4 <= (u^2+v^2)/2` and summing the ordered pairs. Equations (3.12) and (3.15) give

`||E||_F <= (r+1)sqrt(D_{r+1}^perp/D_r^perp)`,

and `||E||_op<=||E||_F`. QED.

This theorem is inverse-free in its final remainder bound. A selected base minor may be poorly conditioned; the determinant cancels through the weighted exterior-energy average before any reciprocal coefficient is paid.

## 4. A low-off-diagonal-energy branch is already paid

Define

`D_1^perp(A)=sum_{i!=j} A_ij^2`.                                  (4.1)

### Lemma 4.1 — `QFORM-LOW-OFFDIAG-FROBENIUS-PAID-v1`

Under the target spectral hypothesis `s_3(A)>=1`, if

`D_1^perp(A) <= 1/16`,                                            (4.2)

then the full ambient quadratic form has an essentially bounded density with

`||p_Q||_infinity`
` <= 128 (3/32)^(-1/4)`
` = 231.322112924...`.                                            (4.3)

#### Proof

Write `A=D_0+H`, where `D_0=diag(A)` and `H` has zero diagonal. From (4.2),

`||H||_op <= ||H||_F <= 1/4`.                                    (4.4)

Singular-value perturbation and `s_3(A)>=1` give

`s_3(D_0)>=3/4`.                                                   (4.5)

Hence there are three original coordinates `S` for which every selected diagonal coefficient obeys `|A_ii|>=3/4`. On the principal block `M=A[S,S]`,

`s_min(M) >= 3/4-||H[S,S]||_op >=1/2`,                            (4.6)

so

`|det M|>=1/8`.                                                    (4.7)

Choose any coordinate in `S`. Its scalar coefficient has magnitude at least `3/4`. Apply the source theorem (1.2), which permits arbitrary outside coefficients/couplings. This gives

`||p_Q||_infinity <=128[(3/4)(1/8)]^(-1/4)=128(3/32)^(-1/4)`. QED.

The result is only an essential-supremum statement; no continuity conclusion is imported from this receiver.

## 5. Actual application of the designated partner: high slab ratio forces rank <=16 plus an operator-small tail

### Theorem 5.1 — `QFORM-HIGHRATIO-RANK16-OPNORM-SKELETON-v1`

Assume the full QFORM hypotheses and suppose some interval `J` has slab ratio

`rho = P(X^T A X in J)/|J| > 231.323`.                            (5.1)

Then there is an integer `r in {1,2,3,4}` and a decomposition

`A=D+R+E`,                                                        (5.2)

where

- `D` is diagonal;
- `R` is symmetric with `rank R<=4r<=16`;
- `E` is symmetric and zero diagonal;
- `E` vanishes on every row and column of a physical core of size `2r<=8`;
- and either `E=0`, or

`||E||_op <= 5 sqrt(2) C_5^(5/4) rho^(-5/4)`
`          < 362.296 rho^(-5/4)`.                               (5.3)

Here `C_5=10sqrt(2e)` is exactly the designated partner constant.

#### Proof

By Lemma 4.1, (5.1) rules out `D_1^perp(A)<=1/16`. Thus

`D_1^perp(A)>1/16`.                                                (5.4)

Apply the partner's theorem to this **actual slab inequality**. Equation (1.1) gives

`D_5^perp(A) <= (C_5/rho)^10`.                                   (5.5)

If some `D_{r+1}^perp(A)=0` with `r in {1,2,3,4}` and `D_r^perp(A)>0`, Theorem 3.1 gives (5.2) with `E=0`. Positivity of a higher exterior order implies positivity of all lower orders, so this covers the zero case.

Otherwise `D_1^perp,...,D_5^perp` are all positive. Telescope:

`prod_{r=1}^4 [D_{r+1}^perp/D_r^perp]`
` = D_5^perp/D_1^perp`.                                         (5.6)

Therefore for some `r in {1,2,3,4}`,

`D_{r+1}^perp/D_r^perp`
` <= (D_5^perp/D_1^perp)^(1/4).                                 (5.7)

Theorem 3.1 and `r+1<=5` give

`||E||_op`
` <=5(D_5^perp/D_1^perp)^(1/8)`
` <5*16^(1/8)*(C_5/rho)^(10/8)`
` =5sqrt(2) C_5^(5/4) rho^(-5/4)`.                              (5.8)

Numerically the coefficient is `362.295383930...`. QED.

A useful scale marker, not a perturbative deletion argument, is that (5.3) is `<1/128` once `rho>5407.78`. The form `E` must still be retained in the probability estimate because arbitrary unit-measure product sets can have arbitrarily remote fragments.

### Geometric product-set version

By Theorem 2.1, every arbitrary-law slab ratio is an exact barycentric average of unit-product-set slab ratios. Conversely, any uniform geometric inequality for all measurable `|E_i|=1` immediately gives the arbitrary-law result. Thus Theorem 5.1 can be read directly as follows: every measurable unit-product-set witness with ratio `rho>231.323` forces the same fixed-core/rank-16/operator-tail decomposition of its coefficient matrix.

No single interval, centered uniform law, bounded diameter, or fixed fragment count appears.

## 6. What this changes and what remains unpaid

The previous B13 high-ratio skeleton gave a fixed-rank term plus a **max-norm** residual. That was insufficient in high dimension. The new exterior-ratio selection upgrades this to a **dimension-free operator-norm** residual:

`rank R<=16`, `core<=8`, `||E||_op=O(rho^(-5/4))`.               (6.1)

This is a genuine strengthening because it is obtained before choosing an ill-conditioned individual minor: all disjoint exterior energies are aggregated first.

It still does **not** prove full QFORM. The remaining implication is

`QFORM-DIAG-RANK16-OPNORM-TAIL-PRODUCT-CLOSURE-v1`:

> Starting from an actual high-ratio product witness and (5.2)-(5.3), control the zero-diagonal operator-small tail `E` together with the diagonal plus rank-16 skeleton, uniformly over arbitrary translated and fragmented cap-one product laws. One may use the existing ridge-window/diffuse-separable, physical-pair, grouped-bank, or no-pivot receivers, but must not simply delete `E` by support-sensitive continuity.

The natural next attack is to combine the operator-small tail with the existing spectral-window theorem: the diffuse large-spectral-projection branch is already paid, so only a high-leverage finite-coordinate obstruction should survive. In the no-pivot chamber this should be compared with the current three-bank/star packets before any reciprocal physical-minor selection.

No claim here has received two independent end-to-end reviews. Full target status: **OPEN**.
