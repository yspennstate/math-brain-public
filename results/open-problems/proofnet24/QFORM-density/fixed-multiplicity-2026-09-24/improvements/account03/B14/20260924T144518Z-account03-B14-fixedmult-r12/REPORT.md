# account03/B14 r12 — Fejer/diagonal interpolation sharpening to 2506, with zero-loss rough-law localization

Run: `20260924T144518Z-account03-B14-fixedmult-r12`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Logical assignment: translations and localization  
Execution: `WITHOUT_VERIFIED_BRAIN`  

## 1. Result

This run independently rechecked the current nine-direction proof architecture and the newest Fejer sharpening, then improves the numerical endpoint.

### Theorem `QFORM-NINE-FEJER-2506-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T`, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then

`Q=X^TAX+b^TX+c`

has a density satisfying

`boxed: ||p_Q||_(infinity,ess) < 2506 K^2/s.`

Using the separately completed fixed-instance affine regularity theorem, the density may in fact be taken in `C_0(R)` with the **same** height bound. No law-uniform modulus of continuity is claimed.

No Gaussianity, moment bound, compact support, connected support, log-concavity, sign restriction, exact-rank assumption, diagonal-basis assumption, or independence after rotation is introduced.

The threshold `9` is not new here. The new content is the `2511 -> 2506` constant sharpening and its localization/continuity closure. Multiplicity `8` and the unrestricted three-eigenvalue conjecture remain open.

## 2. Sources actually consumed

1. Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`. I reread the complete proof by its proof-map ranges.
2. New Fejer source: snapshot `yspennstate/math-open-problems@0aa54bd634644b2922e9faecd003692d7f29e61e`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B10/20260924T140550Z-account01-B10-fixedmult-r13/IMPROVEMENT.md`, blob `8ea4eeb1ed6a72d3c15afe1fd697a68a072f3587`.
3. Same-height `C_0` nine-direction compiler: same snapshot, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B15/20260924T140459Z-account03-B15-fixedmult-continuity-r13/REPORT.md`, blob `8af7e1a48ea703e6c9acf1cf37ed28428ac53aed`.
4. Underlying affine fixed-instance `C_0` theorem: `yspennstate/math-open-problems@26ef4e7b08ecc3336e8ee7fcfdf0445e868745c5`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T092642Z-account03-B15-qform-auto11/REPORT.md`, blob `c34fa9208db4ed7e771148511e6574cef63d4ebd`.
5. Designated partner account04/B14 compact-completion theorem: snapshot `yspennstate/math-open-problems@0aa54bd634644b2922e9faecd003692d7f29e61e`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T171953Z-account04-B14-QFORM-r2/REPORT.md`, blob `bd0013b917741a9202c5462ed4317629ceb0b158`.

A repository search before publication found the visible current `2511` source but no matching `2506 K^2/s` theorem. This is therefore recorded as a new constant sharpening pending independent review, not owner-level release status.

## 3. The missed diagonal interpolation gain

Write `L=||S||` and

`R=X^TSX+d^TX+e`.

The existing quarter-power lemma splits into a diagonal case and a cross-block case.

If some `|S_ii|>=L/2`, conditioning on the other original coordinates and using the scalar-square inverse-image estimate gives

`P{|R-a|<rho} <= min(1, 4 sqrt(rho/L)).`

The current Fejer source relaxed this directly to `4(rho/L)^(1/4)`. One can instead interpolate with the trivial probability bound first. For every `u>0`,

`min(1,4 sqrt(u)) <= 2 u^(1/4).`                                  (3.1)

Indeed, for `u<=1/16` this is `4u^(1/2)<=2u^(1/4)`, while for `u>=1/16` it is `1<=2u^(1/4)`. Thus the diagonal branch costs only the quarter-power coefficient `2`, not `4`.

This makes the cross-block Fejer coefficient the controlling coefficient and allows its actual value to enter the logarithmic potential.

## 4. Sharpening the cross-block Fejer coefficient

In the complementary case the audited sign partition gives an original-coordinate crossing block with operator norm at least `L/4`, and the regularized determinant theorem gives

`|phi_R(t)| <= (4 pi e/(L|t|))^(1/4).`                            (4.1)

Take

`K_U(x)=(sin(Ux)/(Ux))^2,    U=3/(5 rho).`

Under the manuscript Fourier convention,

`hat K_U(t)=(pi/U)(1-|t|/(2U))_+.`

For `|x|<=rho`, the alternating sine series gives the exact lower bound

`sin(3/5) > 3/5-(3/5)^3/6+(3/5)^5/120-(3/5)^7/5040
           = 24703107/43750000.`                                  (4.2)

Therefore

`1_{|x|<rho} <= c_0 K_U(x),`

where

`c_0 <= ((3/5)/(24703107/43750000))^2.`

Fourier inversion, (4.1), and

`int_{-2U}^{2U}(1-|t|/(2U))|t|^(-1/4)dt
 = (32/21)(2U)^(3/4)`

give

`P{|R-a|<rho} <= C_F (rho/L)^(1/4),`

with

`C_F = c_0 (16/21) 2^(3/4) (5/3)^(1/4) (4 pi e)^(1/4).`           (4.3)

For a fully rational certificate, first

`e = sum_{k=0}^6 1/k! + sum_{k>=7}1/k!
   < 1957/720 + 1/4410
   = 31967/11760
   < 27183/10000,`                                                (4.4)

where the tail is bounded by a geometric series with ratio `1/8`; the final margin is exactly `13/735000`. Together with `pi<22/7`, (4.2)--(4.4) yield

`C_F^4 < U_0`

with

`U_0 = 2988387500000000000000000000000000000000000000000000000000
       /11972685640355754882277405939298717746123001311953679647
     = 249.6004313290567... .`                                    (4.5)

Now let `q=69/50`. The positive Taylor partial sum through order 16 satisfies

`sum_{k=0}^{16} (138/25)^k/k! - U_0 > 0`;                         (4.6)

its exact positive numerator and denominator are recorded in `CHECKS.json`. Since the full exponential series is larger than its positive partial sum,

`exp(4q)>U_0>C_F^4`,

so

`log C_F < q=69/50.`                                              (4.7)

Combining (3.1) with the cross-block result therefore gives the uniform quarter-power concentration

`P{|R-a|<rho} <= min(1, C (rho/L)^(1/4))`

for some `C<exp(69/50)`. Layer cake, for `L>=1`, then gives

`sup_a E log_+(1/|R-a|) < 4+4(69/50)=238/25.`                    (4.8)

No pointwise van-der-Corput estimate is used; the cross estimate is the existing integrated product-measure determinant estimate.

## 5. New pivot constant

Use the exact singular-convolution estimate already checked in the current Fejer source,

`J(d)<=pi+4log2+2log_+(1/|d|),`

and the existing rational certificate

`log2<1733/2500.`

At an `eta=1/100` scalar pivot, (4.8) gives truncated half potential

`H_scalar
 <10[22/7 +4(1733/2500)+2(238/25)]
 =218362/875
 =249.556571428571... .`                                         (5.1)

Adding the region `|Q-a|>1`, where the half-Riesz kernel is at most one,

`sup_a E|Q-a|^(-1/2) <219237/875
                         =250.556571428571... .`                  (5.2)

The definite-pair and optimized indefinite-pair pivot branches remain strictly smaller. Therefore the half-potential proposition needed by the outer scalar pivot may use (5.2).

## 6. Nine directions with constant 2506

Normalize `K=s=1` and retain the manuscript parameters `eta=1/100`, `kappa=1/80^2`.

- No pivot: the independently reconstructed order-three crossing compiler gives density `<2400`.
- Scalar pivot: Schur leaves at least eight unit directions. If the Schur remainder has a pivot, apply (5.2); if it has no pivot, the existing order-two crossing receiver gives the smaller full half-potential bound. The outer scalar-square profile costs `eta^(-1/2)=10`, hence

`||p_Q||_infinity
 <10*(219237/875)
 =438474/175
 =2505.565714285714... <2506,`                                    (6.1)

with exact margin `76/175`.
- Definite pair: `<32`.
- Indefinite pair: `<251`.

Thus every normalized branch is `<2506`. For general `K,s`, set `Y=KX` and use the quadratic matrix `A/s`; the scalar density change of variables gives

`boxed: ||p_Q||_(infinity,ess) <2506 K^2/s.`                     (6.2)

The proof retains arbitrary deterministic affine terms throughout.

## 7. B14 localization and translations: actual partner application

The completed account04/B14 compact-completion theorem says that every cap-one marginal can be approximated in total variation by compactly supported cap-one marginals, with product TV controlled by the sum and deterministic pushforward contracting TV. Mollification then gives smooth compact cap-one marginals. Consequently any uniform interval estimate proved on that core passes to arbitrary rough, fragmented, unbounded-support laws with **exactly the same constant**.

Apply this to (6.2), including arbitrary deterministic translations. For every `t in R^n`,

`(X+t)^TA(X+t)=X^TAX+2(At)^TX+t^TAt,`

so translation is exactly an allowed affine perturbation. Therefore

`boxed: sup_t ||p_((X+t)^TA(X+t))||_(infinity,ess)
        <2506 K^2/s,   whenever s_9(A)>=s.`                       (7.1)

There is no support-radius, translation-size, fragment-count, fragment-separation, tail-rate, or moment cost.

The partner localization by itself does not transfer continuity. Continuity is supplied separately by the fixed-instance affine theorem: since `s_9(A)>0` forces `rank(A)>=9`, each fixed affine instance has a canonical `C_0` density. Combining that qualitative theorem with the interval inequality (6.2) forces the same continuous representative to obey the identical `<2506 K^2/s` pointwise height bound. Thus the nine-direction theorem has same-constant `C_0` closure, while no uniform modulus of continuity is asserted.

## 8. Status

- Baseline `s_17` manuscript: no new defect found in this reread.
- Threshold `9`: already supported by independent reconstructions; this run changes only the constant/regularity ledger.
- New constant `<2506 K^2/s`: proved here; pending independent review as a new sharpening.
- Nine-direction continuity: `C_0` with the same `<2506 K^2/s` height by the separately proved fixed-instance compiler, rechecked for scope here.
- Multiplicity `8`: OPEN. Fresh repository search still shows only terminal-collar/overlap and half-potential progress, not a dimension-free linear interval bound.
- Full three-eigenvalue conjecture: OPEN / not proved / not disproved.
- Full-target continuous-density conclusion: OPEN.

The next structural debt is still the `9 -> 8` endpoint receiver in the no-pivot collar; tails and translations are not the obstruction.
