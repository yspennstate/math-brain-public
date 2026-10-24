# account01/B10 r14 improvement — Fejer factor correction and `2422` nine-direction constant

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T144911Z-account01-B10-fixedmult-r14`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **NEW SAME-THRESHOLD CONSTANT SHARPENING; NOT SELF-AWARDED INDEPENDENT VALIDATION.** The threshold `9` was already established in separate source-backed replacement proofs and reviewed independently elsewhere in this root. This report only sharpens its constant and strengthens the exact `r=2` diagnostic at the `s_8` frontier. Multiplicity eight remains open.

## Theorem candidate `QFORM-NINE-2422-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, `b in R^n`, `c in R`, and suppose

` s_9(A) >= s > 0.`

Then `Q=X^TAX+b^TX+c` has an essentially bounded density and

`boxed: ||p_Q||_infinity < 2422 K^2/s.`

No Gaussian, log-concavity, moment, support, sign, exact-rank, leverage, connected-support, or diagonal-basis assumption is introduced. Global continuity is not claimed; the no-pivot Fourier branch is continuous.

The only new analytic observation is that the preceding B10 Fejer calculation contained a harmless factor-two overestimate. Correcting it improves the quarter-power small-ball constant from `<4` to `<2`; after exact hyperbolic bookkeeping the global nine-direction constant becomes `<2422`.

## 1. Correct Fejer calculation: quarter-power constant `<2`

Let `S=S^T !=0`,

`R=X^T S X+b^T X+c`,

with independent coordinate densities bounded by one, and let `L=||S||>0`.

The diagonal branch of the baseline quarter-power lemma already gives

`P{|R-a|<rho} <=4 sqrt(rho/L)`,

which is at most `2(rho/L)^(1/4)` only when `rho/L` is sufficiently small, so retain the baseline diagonal argument separately. For the off-diagonal branch, the baseline sign-cut and determinant theorem give a literal original-coordinate cross block with

`|phi_R(t)| <= (4 pi e/(L |t|))^(1/4)`.                      (1.1)

Put

`K_U(x)=(sin(Ux)/(Ux))^2`, `U=3/(5 rho)`.

Under the manuscript Fourier convention,

`hat K_U(t)=(pi/U)(1-|t|/(2U))_+`.

For `|x|<=rho`, `|Ux|<=3/5` and

`sin y/y >=1-y^2/6 >=47/50`,

hence

`1_{|x|<rho} <=(2500/2209)K_U(x)`.                            (1.2)

Fourier inversion, (1.1), and

`int_{-2U}^{2U}(1-|t|/(2U))|t|^(-1/4)dt=(32/21)(2U)^(3/4)`

give

```
P{|R-a|<rho}
 <= C_F (rho/L)^(1/4),
C_F=(2500/2209)(16/21)(5/6)^(1/4)(4 pi e)^(1/4).              (1.3)
```

The previous report inserted an extra factor `2`; (1.3) is the direct simplification of `(1/(2U))*(32/21)*(2U)^(3/4)`.

Raise (1.3) to the fourth power and use `pi<22/7`, `e<11/4`:

```
C_F^4
 < (2500/2209)^4 (16/21)^4 (5/6) (242/7)
 =1548800000000000000000 / 97247699666584761861
 <16.
```

The exact rational margin is

`16-C_F^4 >7163194665356189776 / 97247699666584761861 >0`.

Therefore the off-diagonal branch has coefficient `<2`.

For the full quarter-power lemma we may combine the diagonal branch and this off-diagonal branch as follows. If `rho>=L/16`, the trivial bound `1` is at most `2(rho/L)^(1/4)`. If `rho<L/16`, the diagonal estimate gives

`4 sqrt(rho/L) <=2(rho/L)^(1/4)`.

Thus **both branches** satisfy

`boxed: P{|R-a|<rho} <= min{1,2(rho/L)^(1/4)}.`                (1.4)

This is strictly stronger than the baseline constant `16` and the preceding B10 constant `4`.

If `L>=1`, layer cake now gives

```
sup_a E log_+(1/|R-a|)
 <= int_0^infinity min(1,2e^(-u/4))du
 =4+4 log2.                                                   (1.5)
```

## 2. Exact logarithm bounds used below

For `0<z<1`,

`log((1+z)/(1-z))=2 sum_{k>=0} z^(2k+1)/(2k+1)`.

After truncation at `m`, the tail is bounded by

`2 z^(2m+3)/((2m+3)(1-z^2))`.

Thus, using `z=1/3,m=2` and `z=1/2,m=4`, respectively,

`log2 <23581/34020`,

`log3 <487259/443520`.                                        (2.1)

These are purely rational upper bounds.

## 3. Scalar pivot half-potential becomes `<196`

Reuse the exact singular-convolution kernel proved in the preceding B10 report:

`J(d) <= pi+4 log2+2 log_+(1/|d|)` for `d!=0`.

At a scalar pivot with `|A_ii|>=eta=1/100`, the Schur remainder has one unit spectral direction whenever the pivot proposition is invoked. Combining the square profile, (1.5), and the kernel estimate gives the truncated half potential

```
H_scalar
 <=10 [pi+4log2+2(4+4log2)]
 =10 [pi+8+12log2].
```

Using `pi<22/7` and (2.1),

`H_scalar <110342/567 =194.6067019...`.

Therefore its full half potential is `<195.607<196`.

The definite-pair full half potential stays `<161`.

## 4. Indefinite pair: exact `<242.2` full half potential

Use the already derived original-coordinate hyperbola tail split with `q=2/9`. One branch has

`C0+log_+[(72 sqrt2/49)/(|delta| Lambda)]`,

where

`C0=2 log3+(37/14)log2`.

After `Lambda>=2/sqrt D`, the conditional density envelope is

`D^(-1/2)[C0+log_+((36 sqrt2/49)sqrt D/|z-v|)]`.

The manuscript logarithmic-kernel bound gives

`H_ind(D) <=D^(-1/2)[4C0+8+4log_+((36sqrt2/49)sqrt D)]`.       (4.1)

For `D>=eta=1/100`, (4.1) is decreasing in `sqrt D`: before the logarithm activates it is a positive constant divided by `sqrt D`; afterwards its derivative numerator is `4-(4C0+8)-4log(...)<0`. Also `(36sqrt2/49)/10<1`, e.g. from `sqrt2<3/2`. Therefore the maximum occurs at `D=1/100`, with the log term inactive:

`H_ind <=10(4C0+8)`.

From (2.1),

`C0 <168871687/41912640`.

Moreover

`403/100 -168871687/41912640 =181261/209563200>0`,

so `C0<4.03`. Hence

`boxed: H_ind <241.2,   full half potential <242.2=1211/5.`    (4.2)

The indefinite pair is therefore the largest pivot half-potential branch after the Fejer correction.

## 5. Nine eigenvalues: global constant `<2422`

Normalize `K=s=1`, keep `eta=1/100`, `kappa=1/80^2`.

### No physical pivot

The audited baseline spectral-to-volume theorem at `k=3` gives `V_3>=kappa^3`. A fair original-coordinate cut gives `E_3>=4^(-3)kappa^3`, hence `E_3^(-1/6)<=160`. The already source-backed marginal-free order-three grouped product-Fourier receiver gives a density `<2400` (indeed sharper reviewed constants exist). This branch is continuous.

### Physical scalar pivot

The outer square profile costs `eta^(-1/2)=10`. The Schur complement retains at least eight unit spectral directions.

- If that complement has a pivot, its full half potential is `<1211/5` by Sections 3–4 above; the indefinite pair controls the maximum.
- If it has no pivot, `s_5>=1`. The audited order-two spectral-to-volume step plus a fair cut and the source-backed marginal-free order-two half-Riesz receiver give full half potential `<13 sqrt(160)<169`, smaller than `1211/5`.

Therefore

`||p_Q||_infinity <10*(1211/5)=2422`.                          (5.1)

### Physical pair pivots

A definite pair gives `<10pi<32`. An indefinite pair leaves at least seven unit Schur directions, hence one, and the direct hyperbolic/log-potential density branch is `<251`; both are far below (5.1).

Thus the normalized nine-direction theorem has density `<2422`. For general `K,s`, set `Y=KX` and scale exactly as in the baseline manuscript to obtain

`boxed: ||p_Q||_infinity <2422 K^2/s.`

This is a complete constant refinement of the already established threshold-nine proof. The new `2422` number itself has not yet received two independent full reviews and must not be labeled independently validated from this report alone.

## 6. Multiplicity eight remains open; exact `r=2` rank sharpness

The current `s_8` terminal no-pivot chamber can reach the sampled order `r=2`, where the baseline completion only gives

`rank R<=6`, `rank R[L,L]<=2`.

The following exact no-pivot finite example shows **both bounds are simultaneously sharp already at `r=2`**:

```
A=(1/1000)*
 [[ 1, 1,-2, 0, 2, 1],
  [ 1, 1, 0, 1, 0, 2],
  [-2, 0,-1, 2,-1, 0],
  [ 0, 1, 2,-1,-2, 2],
  [ 2, 0,-1,-2, 0, 2],
  [ 1, 2, 0, 2, 2, 2]],
S={1,2}, T={3,4}, L={5,6}.
```

Here `det A[S,T]=-1/500000`, `max_i |A_ii|=1/500<eta`, and the largest principal `2x2` determinant has modulus `3/500000<eta`. The completion has

`rank R=6=3r`, `rank R[L,L]=2=r`.

Thus the eight-direction frontier cannot be closed merely by replacing the universal rank constants `3r` and `r` with smaller ones. This is a finite local sharpness diagnostic, not a counterexample to an `s_8` theorem. The remaining obligation is still an overlap-aware/product-preserving receiver for the terminal `r=2` collar (or a genuinely new structural decomposition).

## 7. Status

- Literal baseline `s_17` theorem: PASS in this run's separate full audit.
- Threshold `9`: already has complete replacement proofs/reviews in the repository; this run supplies a new candidate constant `<2422 K^2/s`.
- New constant `2422`: **pending independent review**.
- Threshold `8`: **OPEN**.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: not claimed.
