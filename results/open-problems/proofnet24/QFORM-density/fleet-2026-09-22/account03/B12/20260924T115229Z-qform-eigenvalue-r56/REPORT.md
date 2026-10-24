SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T11:52:29.055723Z.
attacking: lower the finite-large-spectrum closure threshold from 189 by replacing the heavy five-mode endpoint with the completed four-mode square-energy compiler while preserving arbitrary additional signed spectrum.

# account03/B12 r56 — 141-large-eigenvalue closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T115229Z-qform-eigenvalue-r56`  
Role: Additional eigenvalue control  
Status: **PROVED TARGET-SCOPE SUBTHEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and source-valid inputs

The owner target is unchanged. The inputs are independent ORIGINAL coordinates with arbitrary one-dimensional probability densities `0<=f_i<=1`; `A=A^T` is arbitrary. No moment, centering, compact-support, connected-support, Gaussian, log-concavity, iid, or post-rotation independence hypothesis is introduced. No spectral quadratic remainder is ever treated as independent convolution noise.

The live correction inbox was refreshed before publication. In particular, this report does not use law-uniform pointwise van-der-Corput decay, an arbitrary-joint coarea cap, conditional-density caps after non-product changes of variables, a dimension-free fiber supremum, or a uniformly good single physical minor.

The completed inputs used at their stated scopes are:

1. **Four-mode physical square-energy compiler** `QFORM-FOUR-MODE-SPECTRAL-SQUARE-CARRIER-v1`, account03/B12 r40, available at immutable commit `fdcb2e5ac7ce86f617c79cbeaae2d33aafd25a7a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T194742Z-qform-eigenvalue-r40/REPORT.md`. If `s_3(A)>=s`, `H` is a literal ORIGINAL-coordinate carrier of size `m>=4`, and there is `0<=G<=A^2` with `lambda_4(G[H,H])>=g^2`, then the full quadratic form has an essentially bounded density, with the explicit five-term bound recalled in Section 3 below. All spectrum of the final `A` is retained.

2. **One-scale ridge theorem and two-part MSS frame application**, source-pinned in `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, path `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. For a literal ORIGINAL-coordinate cross block `B=A[I,J]`, `gamma>0`, `K=BB^T(gamma^2 I+BB^T)^{-1}`, `theta=tr K`, if `max_i K_ii<=q/2` and `theta>2q`, `1<=q<=2`, then the full form has a continuous `C_0` density and the stated ridge height bound. The same source gives the two-part MSS consequence: a Parseval frame with row squared norms at most `alpha` has a partition whose two frame operators are at least `delta I`, where `delta=1/2-alpha-sqrt(2 alpha)`.

3. **Fixed-matrix rough-input regularity**, `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`: for every fixed real symmetric matrix of rank at least three and every cap-one product input, the output has an instance-dependent bounded `C_0` density. This input supplies continuity only; the universal height below is proved independently of it.

4. **Designated partner account04/B12 r9**, `yspennstate/math-open-problems@71b7db02d3bd2f5cb6bf07e800caa6bd13a1a3e5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260924T021341Z-account04-B12-resonance-repair-r9/REPORT.md`. Its exact-resonance six-coordinate carrier has six mutually orthogonal final carrier columns of norm `2`, despite an exactly singular relative-gain matrix.

## 2. Main theorem

### Theorem 2.1 — `QFORM-141-LARGE-EIGENVALUE-CLOSURE-v1`

Let

`r_1 = #{j: |lambda_j(A)|>=1}`.

If `r_1>=141`, then for every independent cap-one product input `X`, the law of `Q=X^TAX` has an essentially bounded density satisfying

`boxed: ||p_Q||_(infinity,ess) < 1,588,901,662,443.`

No restriction is imposed on any remaining eigenvalue: additional eigenvalues may have either sign, arbitrary multiplicity, arbitrary magnitude below or above intermediate scales, and arbitrarily oriented eigenvectors in the ORIGINAL coordinates.

Combining the height estimate with the completed fixed-matrix regularity theorem gives a continuous `C_0(R)` representative on this entire `r_1>=141` sector, with the same pointwise height bound. Thus the unresolved universal-height problem reduces to

`boxed: 3 <= r_1 <= 140.`

The full three-large-eigenvalue conjecture remains open.

## 3. Constants and the heavy-coordinate branch

Fix

`m=35`,
`alpha=42869/500000=0.085738`,
`tau=1/6144=0.00016276041666666666...`.

Define

`delta = 1/2-alpha-sqrt(2 alpha)
       = 0.0001653929141655075...`,

so

`sigma=delta-tau=2.632497498840841e-6 >0`.

The positivity is exact. Since `1/2-alpha=207131/500000`,

`(207131/500000-1/6144)^2 - 2 alpha
 = 20092939729/9216000000000000 >0`,

and the left side before squaring is positive. Hence `delta>tau`.

Let `P=1_{|A|>=tau}` be the spectral projector onto the complete `tau`-high spectral space and write `P=UU^T` with orthonormal columns. Put

`ell_i=P_ii=||u_i||^2`,
`S={i: ell_i>alpha}`, `h=|S|`.

Also let `A_H` be the exact spectral truncation of `A` to `Ran P` and `E=A-A_H`. Then

`||E||_op<tau`.                                                   (3.1)

Suppose first that `h>=35`, and select any literal ORIGINAL-coordinate subset `H subset S` of cardinality 35. Let

`kappa_1>=...>=kappa_35>=0`

be the eigenvalues of `P[H,H]`. Since `P` is a projection, every `kappa_j<=1`, while

`sum kappa_j = sum_{i in H} ell_i >35 alpha
 =3+83/100000`.                                                   (3.2)

The top three eigenvalues contribute at most `3`. Therefore

`sum_{j=4}^{35} kappa_j >83/100000`.

There are 32 terms in this tail, so

`boxed: kappa_4 > beta:=83/3200000
                    =2.59375e-5.`                                (3.3)

Because `A^2>=tau^2 P` spectrally, the PSD certificate

`G=tau^2 P`

satisfies `0<=G<=A^2`, and

`lambda_4(G[H,H]) > g^2`,
`g=tau sqrt(beta)=8.289204421982161e-7`.                           (3.4)

Now apply the completed four-mode compiler with `s=1`, `m=35` and the admissible parameter choice

`c=(19/20)g`,
`b=(19/20)c/m`,
`a=(9/10)b/binom(35,2)`.                                         (3.5)

These obey `0<a<b/binom(m,2)`, `0<b<c/m`, `0<c<g`. The five explicit compiler terms are respectively

`1.5889016624427961e12`,
`8.745302215480340e11`,
`7.614862101963689e10`,
`7.089343773871708e7`,
`5.696136172843642e9`.                                           (3.6)

Thus the heavy branch obeys

`boxed: ||p_Q||_(infinity,ess) <1,588,901,662,443.`               (3.7)

This step is a square-order argument on the FINAL deterministic matrix. No omitted spectral term is declared independent.

## 4. The light-coordinate branch

Assume now `h<=34` and put `L=S^c`. Work in the high-spectral coordinate space `R^r`, `r=rank P`. Let

`W=ker(U_S)`

and let `R` denote orthogonal projection onto `W`. Since `U_S` has at most `h` rows,

`codim W<=h`.                                                     (4.1)

For every `i in L`, set `w_i=R u_i`. For `x in W`, `U_Sx=0`, hence

`sum_{i in L}<w_i,x>^2
 =sum_{i in L}<u_i,x>^2
 =||Ux||^2=||x||^2`.                                              (4.2)

Thus the `w_i` form a Parseval frame on `W`, and

`||w_i||^2<=ell_i<=alpha`.                                       (4.3)

The two-part MSS consequence supplies a partition

`L=I disjoint_union J`

such that on `W`

`M_I:=sum_{i in I}w_iw_i^T >=delta I_W`,
`M_J:=sum_{j in J}w_jw_j^T >=delta I_W`.                          (4.4)

Let `Lambda` be the signed diagonal of all eigenvalues in the `tau`-high spectral space, and let `E_1` be the span of its coordinate axes with actual `|lambda|>=1`; `dim E_1=r_1>=141`. Define

`C=R Lambda R |_W`.                                               (4.5)

Consider

`V=E_1 intersect W intersect Lambda^{-1}W`.                       (4.6)

Both `W` and `Lambda^{-1}W` have codimension at most `h`, because `Lambda` is invertible on the `tau`-window. Hence

`dim V>=r_1-2h`.                                                  (4.7)

For `x in V`, `Rx=x` and `Lambda x in W`, so

`Cx=Lambda x`,
`||Cx||>=||x||`.                                                  (4.8)

The singular-value min-max principle yields

`s_{r_1-2h}(C)>=1`.                                               (4.9)

At the worst allowed `h=34`,

`5+2h=73`,
`r_1-2h>=141-68=73`.

Therefore in every light case

`boxed: s_{5+2h}(C)>=1.`                                         (4.10)

Form the projected physical crossing

`G=U_I R Lambda R U_J^T`.                                        (4.11)

By (4.4), both outer maps have least singular value at least `sqrt(delta)`, so

`s_{5+2h}(G)>=delta s_{5+2h}(C)>=delta`.                          (4.12)

The actual high-spectral cross block is

`B_H=A_H[I,J]=U_I Lambda U_J^T`.

With `Q=I-R`,

`Lambda-R Lambda R = Q Lambda + R Lambda Q`,

so

`rank(B_H-G)<=2 rank Q<=2h`.                                     (4.13)

Rank-`2h` singular-value interlacing and (4.12) give

`boxed: s_5(B_H)>=delta.`                                        (4.14)

Restoring the entire low spectral tail from (3.1), the actual cross block `B=A[I,J]` satisfies rectangular Weyl:

`boxed: s_5(B)>delta-tau=sigma
                 =2.632497498840841e-6.`                         (4.15)

This is the dependence-safe additional-spectrum step: all lower spectral modes, with arbitrary signs and orientations, are retained through one deterministic operator-norm tail estimate; the random quadratic remainder is never separated probabilistically.

Apply the one-scale ridge theorem with

`q=2`, `gamma=sigma/3`.                                          (4.16)

Since `0<=K<=I`, the leverage requirement is automatic:

`max_i K_ii<=1=q/2`.                                             (4.17)

The five singular values in (4.15) contribute at least `9/10` each to `theta=tr K`, so

`theta>=9/2>4=2q`.                                               (4.18)

Hence

`||p_Q||_infinity
 <= 27 sqrt(e)/(2 sigma)
 =8,454,988.9085... <8,454,989`.                                 (4.19)

This branch is continuous `C_0` directly from the ridge theorem.

Combining (3.7) and (4.19) proves Theorem 2.1.

## 5. Why 141 is the natural endpoint of this exact mechanism

The improvement over r55 is from **189 to 141** because the heavy branch now needs four physical square modes rather than five.

For the same two-part MSS mechanism, positivity requires

`alpha < alpha_*=(1-1/sqrt(2))^2=0.0857864376...`.                (5.1)

To force a fourth eigenvalue of an `m`-row projector compression by trace alone, one needs

`m alpha>3`.                                                      (5.2)

No `m<=34` can satisfy both (5.1) and (5.2), while `m=35` can. Thus 35 is the smallest heavy-set size available to this four-mode/MSS proof architecture. Consequently the light case has `h<=34`; retaining five ridge modes through the two codimension losses and the rank-`2h` restoration requires

`r_1>=5+4h`,                                                      (5.3)

whose worst case is exactly

`5+4*34=141`.                                                     (5.4)

So further reduction below 141 needs a genuinely new light-branch accounting or a receiver needing fewer than five ridge directions; it cannot come merely from retuning the constants in this mechanism.

## 6. Designated partner applied at an actual inequality

Use account04/B12 r9's exact-resonance physical carrier. Let `P_H` embed its six ORIGINAL carrier coordinates and let `A_res` be the partner's final resonant matrix at the exact repair point. The partner proves

`boxed: s_6(A_res P_H)=2`.                                       (6.1)

Now add an arbitrary real symmetric signed packet `F` satisfying only

`rank(FP_H)<=2`,                                                  (6.2)

with no bound on its nonzero eigenvalue magnitudes, signs, global rank away from the carrier, or complement spectrum. Rank-two singular-value interlacing gives

`s_4((A_res+F)P_H)>=s_6(A_resP_H)=2`.                             (6.3)

Add one more arbitrary symmetric matrix `T` satisfying only the local carrier bound

`||TP_H||_op<=1/4`;                                               (6.4)

its global operator norm and complement spectrum may be arbitrarily large. Weyl yields

`boxed: s_4((A_res+F+T)P_H)>=7/4.`                               (6.5)

Hence the FINAL matrix `A=A_res+F+T` has

`s_3(A)>=7/4`,
`lambda_4((A^2)[H,H])>=49/16`.                                   (6.6)

Apply the completed four-mode compiler to this actual inequality with `m=6`, `s=g=7/4` and

`c=0.9g`, `b=0.9c/6`, `a=0.9b/binom(6,2)`.                       (6.7)

Its five terms are

`1500.4901`, `1994.6621`, `4360.8162`, `9.1635`, `243.4605`,

so

`boxed: ||p_Q||_(infinity,ess) <4361.`                            (6.8)

This is an explicit extension of the partner's exact-resonance family by arbitrarily large signed carrier-rank-two spectrum plus a dense local tail. By the fixed-matrix regularity theorem, this branch also has a continuous `C_0` representative. No added quadratic term is treated as independent noise.

## 7. Rigorous computation / sanity checks

The theorem itself is analytic. Finite computations were used only as consistency checks, never as evidence of universality.

- Exact arithmetic verifies the heavy trace surplus `35 alpha-3=83/100000`, hence `beta=83/3200000`.
- Exact arithmetic verifies `delta>tau` through the positive rational difference displayed before (3.1).
- A fixed-seed 10,000-instance random matrix check of rank-two singular-value interlacing found zero violations; the smallest observed margin in `s_4(M+R)-s_6(M)` was `0.19712789998387947`.
- A fixed-seed 2,000-instance check of the signed compression lemma `s_{r-2h}(R Lambda R|_W)>=1` in random finite analogues found zero violations; the smallest observed numerical margin was `0.0002733718103105076`.

These checks do not substitute for the min-max, rank, and MSS arguments above.

## 8. Remaining gap

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** This run lowers the finite-large-spectrum reduction from `r_1<=188` to

`boxed: 3<=r_1<=140`.

The next B12 target is therefore structural rather than a perturbation-size issue: in the finite-large-spectrum sector, replace the five-direction light ridge endpoint by a four-or-three-resource receiver, or prove that failure of such a receiver forces one of the already-paid grouped-hub, projected-crossing, rank-two common-plane, Schur, pair, or Pluecker-volume mechanisms. Any such step must preserve ORIGINAL-coordinate product provenance and arbitrary signs of all additional spectrum.

Continuity status is recorded separately: the light ridge branch is directly `C_0`; the heavy and partner branches obtain `C_0` from the source-pinned fixed-matrix rank>=3 theorem. The universal height conjecture for `3<=r_1<=140` remains open.
