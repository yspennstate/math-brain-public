SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-24T09:55:29Z.
attacking: the critical 2+1 cross-hub endpoint — extract the one-sided two-slope positive-half time budget despite an arbitrary deterministic U-V cross term, then splice it with the completed fleet02/B03 negative-half fresh-hub estimate to obtain an L1 characteristic function and linear small-ball scaling.

# Critical 2+1 cross-hub positive-half theorem

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **new supporting integrated-time theorem / designated fleet02-B03 theorem applied at an actual inequality / exact target family / full QFORM OPEN / unrestricted continuity OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First missing implication

The preceding fleet01/B03 run proved a cross-coupled marginal-Plancherel theorem for two physical hub groups. In total physical hub dimension `d=3`, its symmetric geometric-mean estimate gives only the endpoint decay

`|phi(t)|^2 = O(|t|^(-3/2))`,

which is not enough by itself to make `phi` integrable. The first missing implication was whether the critical `2+1` split retains a *positive-half integrated time budget* strong enough to splice with one complementary negative-half packet.

It does. The key is not to geometric-average the two one-sided estimates. In a `2+1` split, the two-dimensional side alone has enough Plancherel strength to pay the entire `+1/2` time weight. The scalar slope on the other side can be arbitrarily dependent on the two-dimensional slope and in fact needs no density bound at all.

This is exactly the kind of endpoint statement that survives the live corrections: no pointwise van-der-Corput estimate, no conditional slope-density cap, no mixed `L1_t L2_fiber` norm, and no rotation of physical product coordinates is used.

## 2. Main theorem

### Theorem — `QFORM-CROSS-HUB-2PLUS1-POSHALF-v1`

Let

- `U=(U_1,U_2)` have a probability density `f_U` on `R^2` with `0<=f_U<=1`;
- `V` be a real random variable with probability density at most one;
- `Y` be an arbitrary random object independent of `(U,V)`;
- `L=L(Y) in R^2` have a Lebesgue density with `||p_L||_infinity <= K_2`;
- `M=M(Y)` be an arbitrary measurable real variable. **No density bound and no independence between `M` and `L` are assumed**;
- `C` be any symmetric `2 x 2` matrix, `d` any real number, `E in R^2` any deterministic cross vector, and `R(Y)` any measurable real phase.

Set

`T = U^T C U + d V^2 + 2 V E^T U + 2 U^T L(Y) + 2 V M(Y) + R(Y).`

Then

`boxed: |phi_T(t)|^2 <= min{1, pi^2 K_2 |t|^(-2)}.`                    (2.1)

Consequently the positive-half integrated time budget satisfies

`boxed: A_+(T):=int_R |t|^(1/2)|phi_T(t)|^2 dt`
`                 <= (16/3) pi^(3/2) K_2^(3/4).`                       (2.2)

The estimate is uniform in `C,d,E,R` and in the law of `M`.

For two original independent cap-one coordinates, their joint product density satisfies the hypothesis `f_U<=1`, so the theorem is directly product-valid.

### Proof

For fixed `t`, define the two-dimensional hub transform

`F_t(z)=E_U exp{i t[U^T C U+2U^T z]}.`

For fixed slope values `(l,m)`, integrate the scalar hub `V` only after the `U`-transform has been formed:

`K_t(l,m)`
` = E_V[ exp{i t(dV^2+2Vm)} F_t(l+EV) ].`                              (2.3)

Cauchy--Schwarz with respect to the probability law of `V` gives

`|K_t(l,m)|^2 <= H_t(l),`

where

`H_t(l)=E_V |F_t(l+EV)|^2.`                                               (2.4)

This is the decisive one-sided inequality: the arbitrary scalar slope `m` has disappeared before any density assumption is requested.

Now

`phi_T(t)=E_Y[ exp(i t R(Y)) K_t(L(Y),M(Y)) ].`

Jensen and (2.4) yield

`|phi_T(t)|^2 <= E_Y H_t(L(Y))`
`              = E_(L,V)|F_t(L+EV)|^2.`                                  (2.5)

Since `L` is independent of `V`, conditioning on `V=v` only translates its density. Hence

`E_(L,V)|F_t(L+EV)|^2`
` <= K_2 int_(R^2) |F_t(z)|^2 dz.`                                       (2.6)

Put

`h_t(u)=f_U(u) exp(i t u^T C u).`

With Fourier convention `hat h(xi)=int h(u) exp(i xi^T u)du`, one has

`F_t(z)=hat h_t(2tz).`

Plancherel and the change of variables `xi=2tz` give

`int |F_t(z)|^2 dz`
` = (4t^2)^(-1)(2pi)^2 int |h_t(u)|^2du`
` <= pi^2 |t|^(-2),`                                                     (2.7)

because `int f_U^2 <= ||f_U||_infinity int f_U <=1`.

Combining (2.5)--(2.7) proves (2.1). Let

`T_0=pi K_2^(1/2)`

be the exact crossover. Then

`A_+(T)`
` <= 2[ int_0^(T_0) t^(1/2)dt`
`       + pi^2 K_2 int_(T_0)^infinity t^(-3/2)dt ]`
` = 2[(2/3)T_0^(3/2)+2T_0^(3/2)]`
` = (16/3) pi^(3/2) K_2^(3/4).`

QED.

## 3. Applying the completed fleet02/B03 result at an actual inequality

The designated partner result is fleet02/B03 r52:

`yspennstate/math-open-problems@54243d0668be2be7879ae467ed9cb6b962f24652`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260924T081949Z-fleet02-B03-QFORM-auto11-r52/REPORT.md`.

Its theorem `QFORM-CONDITIONAL-ENVIRONMENT-WEIGHTED-TIME-COMPILER-v1` says that, after conditioning on a physical environment `W`, if two source-disjoint fresh packets have conditional characteristic functions `F_w,G_w` and

`A_-(w)=int |t|^(-1/2)|F_w(t)|^2dt`,
`A_+(w)=int |t|^( 1/2)|G_w(t)|^2dt`,

then

`boxed: ||p_Q||_infinity <= (2pi)^(-1)(E A_-)^(1/2)(E A_+)^(1/2),`       (3.1)

and the resulting density is continuous and vanishes at infinity.

The same partner report records the fresh scalar-hub estimate

`A_-(w) <= 8 sqrt(pi M_-(w)/|gamma|)`                                     (3.2)

when the conditional random linear slope has density cap `M_-(w)`.

Apply (3.1) with the partner's fresh scalar packet on the negative side and Theorem 2.1 on the positive side. If, conditionally on `W`, the critical `2+1` packet has two-dimensional slope cap `K_2(w)`, then (2.2) gives

`A_+(w) <= (16/3)pi^(3/2)K_2(w)^(3/4).`                                  (3.3)

Therefore

`boxed: ||p_Q||_infinity`
` <= 4 sqrt(2/3)`
`    *[E sqrt(M_-(W)/|gamma|)]^(1/2)`
`    *[E K_2(W)^(3/4)]^(1/2).`                                           (3.4)

This is an equation-level application of the completed partner theorem, not a citation-only dependency.

Under uniform conditional caps `M_-<=1`, `K_2<=1`, `|gamma|>=1`,

`boxed: ||p_Q||_infinity <= 4 sqrt(2/3)`
`                         = 3.265986323710904... .`                        (3.5)

Thus the critical **three-hub** cross-coupled packet can now be paid by one complementary fresh negative-half packet. The previous run needed a four-hub cross packet to obtain the positive-half budget from the symmetric geometric-mean estimate; the one-sided argument above removes that extra hub dimension.

## 4. Exact owner-target family with maximal slope overlap and nonzero cross coupling

Take eight genuine independent cap-one coordinates

`H_0,Z,W,U_1,U_2,V,Y_1,Y_2`

and define

`Q_* = 2H_0(Z+W)`
`    + 2U_1(Y_1+W) + 2U_2Y_2`
`    + 2VY_1 + 2U_1V.`                                                     (4.1)

Condition on the original coordinate `W`.

The negative packet is

`S_W=2H_0(Z+W)`.

It has `gamma=1` and conditional slope density cap `M_-=1`, so the completed fleet02/B03 estimate gives

`A_-(W)<=8sqrt(pi).`                                                       (4.2)

The positive packet is

`T_W=2U_1(Y_1+W)+2U_2Y_2+2VY_1+2U_1V.`                                   (4.3)

Here

`U=(U_1,U_2)`,
`L_W=(Y_1+W,Y_2)`,
`M=Y_1`,
`E=(1,0)^T`.

The two-dimensional slope `L_W` has density cap one for every `W`, while the scalar slope `M` is literally a coordinate of the same source and is therefore maximally dependent on `L_W`. The deterministic physical cross term `2U_1V` is nonzero. Theorem 2.1 gives

`A_+(W)<=(16/3)pi^(3/2).`                                                  (4.4)

Equations (3.1), (4.2), and (4.4) yield

`boxed: ||p_(Q_*)||_infinity <=4sqrt(2/3)`
`                             =3.265986323710904... ,`                     (4.5)

so every interval `I` satisfies

`boxed: P(Q_* in I) <= 3.265986323710904... |I|.`                          (4.6)

The proof gives `phi_(Q_*) in L^1`, hence `Q_*` has a continuous `C_0` density.

This family is strictly inside the owner target. Delete the coordinate `W`. The resulting `7 x 7` principal matrix is the direct sum of

- the edge `(H_0,Z)`, with eigenvalues `{+1,-1}`, and
- the `5 x 5` matrix on `(U_1,U_2,V,Y_1,Y_2)`, whose spectrum is exactly `{2,1,-1,-1,-1}`.

Hence the principal submatrix has ordered spectrum

`{2,1,1,-1,-1,-1,-1}`.

By Cauchy interlacing, the full `8 x 8` coefficient matrix has at least three eigenvalues `>=1`. Thus (4.1) satisfies the exact target spectral quantifier without any diagonal-basis assumption.

## 5. Assignment-specific independent-copy integral

The independent-copy identity is retained only at the whole-output level:

`|phi_(Q_*)(t)|^2 = E exp(i t(Q_*-Q_*')).`                                (5.1)

No coordinatewise difference `X_i-X_i'` is separated from its conjugate sum, and no conditional cap is assigned to either member of such a pair.

For the exact family, Jensen and `|G_W(t)|<=1` give

`|phi_(Q_*)(t)|^2 <= E_W |F_W(t)|^2.`

Therefore the partner negative-half budget (4.2) implies directly

`boxed: int_R |t|^(-1/2)|phi_(Q_*)(t)|^2dt <=8sqrt(pi)`
`       =14.179630807244127... .`                                         (5.2)

Using the regularized one-dimensional Riesz identity

`int_R |t|^(-1/2)e^(itx)dt = sqrt(2pi)|x|^(-1/2),`

(5.1)--(5.2) give

`boxed: E|Q_*-Q_*'|^(-1/2) <=4sqrt(2)`
`       =5.656854249492381... .`                                          (5.3)

After the one-copy density bound (4.5) is known, convolution preserves that cap for `Q_*-Q_*'`; the sharp one-dimensional bathtub estimate improves this to

`E|Q_*-Q_*'|^(-1/2) <=2sqrt(2||p_(Q_*)||_infinity)`
`                    <=5.111544833970179... ,`                            (5.4)

or equivalently

`int |t|^(-1/2)|phi_(Q_*)|^2dt <=12.812742807873674... .`                  (5.5)

The logical direction is important: linear small-ball scaling comes from the complementary weighted `L^1_t` compiler (3.1), not from reversing the collision estimate.

## 6. Scope and remaining gap

This run settles the first integrated endpoint missing from the previous B03 run:

**an arbitrary deterministic cross term between a two-dimensional physical hub and a scalar physical hub does not destroy the two-slope `+1/2` time budget.** The scalar slope may be arbitrarily dependent on the two-dimensional slope and need not have any density bound.

What is still open is the standalone critical three-hub packet when no source-disjoint negative-half resource can be exposed. The full QFORM conjecture therefore remains **OPEN**, and unrestricted full-target continuity remains **OPEN**. The next structural/analytic debt is to prove that every survivor either exposes such a fresh negative-half packet (possibly after a product-valid conditioning cut) or falls into an already-paid grouped-carrier, principal-pair, ridge, or rank-three receiver; otherwise one needs a genuinely standalone critical `2+1` endpoint mechanism.

## 7. Correction and source ledger

Fresh owner/control state was read from `yspennstate/math-research-brain` main. The live correction corpus was respected, including the failures of uniform pointwise quadratic-phase decay, conditional projection-density caps, and the universal `L1_t L2_fiber` mixed norm. No Gaussian, log-concavity, moment, support, connected-support, diagonal-basis, rotated-independence, or conditional-density assumption is added.

Completed partner source actually used: fleet02/B03 r52 at commit `54243d0668be2be7879ae467ed9cb6b962f24652`, path stated in Section 3.
