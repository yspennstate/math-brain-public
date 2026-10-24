# QFORM-FIXED-MULTIPLICITY-9-2510-v1

Run: `20260924T141332Z-account01-B04-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **proved constant sharpening conditional only on the already-complete nine-direction replacement proof; new arithmetic sharpening pending independent review**.  
Baseline manuscript: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, let `b in R^n`, `c in R`, and assume

` s_9(A) >= s > 0.`

Then the complete nine-direction replacement proof already in the repository admits the sharpened universal height

`boxed: ||p_(X^T A X+b^T X+c)||_(infinity,ess) < 2510 K^2/s.`

No Gaussian, log-concavity, moment, compact-support, connected-support, signature, exact-rank, diagonal-basis, or post-rotation-independence assumption is added. The unrestricted three-eigenvalue conjecture remains open. The threshold eight universal-height problem also remains open.

The only change from the independently reviewed `<2582 K^2/s` proof is a sharper rigorous evaluation of the quarter-power constant entering the nested scalar-pivot branch. All structural parts of the nine-direction proof are unchanged.

## 1. Source-pinned structural proof being sharpened

The complete threshold-nine proof is account03/B04, blob `054facef834d29927713c5d42a1f09a541c5644b`, at

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.

It proves, in normalized variables `K=s=1`:

- no physical pivot: `<2400` by order-three disjoint volume plus the marginal-free `E_3` product-Fourier receiver;
- scalar physical pivot: outer square profile times a full half-potential bound for the Schur remainder;
- definite pair pivot: `<32`;
- indefinite pair pivot: `<251`.

Account01/B16 commit `54ec2a651d854563f8db0d92c4c3426f76551786` independently reconstructed the replacement proof and reported PASS. Account03/B14 independently audited it and sharpened the previous scalar-pivot arithmetic to `<2582`. The present run independently reread the complete threshold-nine mechanism after completing the baseline audit and also reports PASS. This file does not self-award owner-level validation.

## 2. Exact quarter-power coefficient

The baseline quarter-power concentration lemma uses the exact coefficient

`C_q = 2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8).`                    (2.1)

The earlier `<2582` audit bounded this coefficient by a deliberately loose rational. We can do materially better with a standard explicit Gamma inequality.

NIST DLMF equation 5.6.1 states, for every `x>0`,

`Gamma(x) < sqrt(2 pi) x^(x-1/2) exp(-x+1/(12x)).`               (2.2)

Use the recurrence twice:

`Gamma(3/8) = (64/33) Gamma(19/8).`                              (2.3)

Applying (2.2) at `x=19/8` and substituting into (2.1) gives, after cancellation,

`C_q < [2^(3/2)/33] 19^(15/8) pi^(1/4) exp(-112/57).`           (2.4)

Raising to the eighth power,

`C_q^8 < [4096*19^15*pi^2/33^8] exp(-896/57).`                  (2.5)

I now certify the simple rational bound

`boxed: C_q < 7993/2000 = 3.9965.`                              (2.6)

This is a finite rational check. Put `x=896/57` and

`S_33 = sum_(k=0)^33 x^k/k!`.

All Taylor terms are positive, hence `e^x>S_33`. Also use the classical rational upper bound `pi<22/7`. Therefore (2.5) is strictly smaller than `(7993/2000)^8` once

`[4096*19^15*(22/7)^2/33^8] < (7993/2000)^8 S_33`.              (2.7)

Equation (2.7) is an exact rational inequality; the accompanying `CHECKS.py` evaluates it with `fractions.Fraction` and returns PASS. Numerically, only for orientation,

`S_33 = 6710977.895890062...`,

while the rational threshold on the left after division by `(7993/2000)^8` is

`6710628.336846249...`.

No floating-point comparison is needed for the certificate.

## 3. Rigorous logarithm bounds

Two elementary logarithm upper bounds suffice.

First,

`log 2 < 1733/2500 = 0.6932.`                                   (3.1)

Indeed the positive Taylor partial sum through degree six satisfies

`sum_(k=0)^6 (1733/2500)^k/k! > 2`.

Second, from (2.6),

`log C_q < log(7993/2000) < 2771/2000 = 1.3855.`                (3.2)

The second strict inequality follows because the positive Taylor partial sum through degree eight satisfies

`sum_(k=0)^8 (2771/2000)^k/k! > 7993/2000`.

Again the companion exact-rational check records both inequalities. For reference, the exact positive margin in the degree-eight comparison is

`2722603209183783919743667361 / 10321920000000000000000000000000`.

## 4. Scalar-pivot half-potential with the improved constant

The independently audited account03/B14 convolution calculation gives, for

`J(d)=int_(-1)^1 |x|^(-1/2)|x-d|^(-1/2) dx`,

the uniform estimate

`J(d) <= pi+4 log 2 + 2 log_+(1/|d|).`                           (4.1)

The quarter-power small-ball estimate with coefficient `C_q` gives the logarithmic potential

`L_log <= 4+4 log C_q`.                                         (4.2)

With the manuscript's `eta=1/100`, the inner scalar-pivot truncated half-potential is therefore

`H_trunc
 < 10 [ pi+4 log2 + 2(4+4 log C_q) ].`                         (4.3)

Adding the tail `|R-a|>1` costs at most one:

`H_full
 < 10 [ pi+4 log2+8+8 log C_q ] +1.`                           (4.4)

The **outer** scalar pivot in the threshold-nine theorem costs another factor `eta^(-1/2)=10`. Thus its normalized density height is strictly below

`C_scalar
 = 810 + 100 pi + 400 log2 + 800 log C_q.`                       (4.5)

Use `pi<22/7`, (3.1), and (3.2):

`C_scalar
 < 810 +100*(22/7)+400*(1733/2500)+800*(2771/2000)
 = 439244/175
 = 2509.965714285714...`                                        (4.6)

and

`2510 - 439244/175 = 6/175 >0.`                                 (4.7)

Hence the scalar-pivot branch is `<2510`.

## 5. Complete normalized case split

Nothing else in the threshold-nine proof changes.

- **No pivot:** `<2400`.
- **Scalar pivot:** `<2510` by (4.6)--(4.7).
- **Definite pair pivot:** `<32`.
- **Indefinite pair pivot:** `<251`.

Therefore for cap-one inputs and `s_9(A)>=1`,

`boxed: ||p_Q||_(infinity,ess) <2510.`                           (5.1)

For general cap `K` and spectral scale `s`, put

`Y=KX`, `A'=A/s`, `b'=(K/s)b`, `c'=(K^2/s)c`.

Then `Q=(s/K^2) Qtilde`, the coordinates of `Y` have density cap one, and `s_9(A')>=1`. Scaling (5.1) gives

`boxed: ||p_Q||_(infinity,ess) <2510 K^2/s.`                     (5.2)

## 6. Continuity status

The height proof above is self-contained relative to the already-complete threshold-nine replacement proof and yields essential boundedness. Separately, current fleet work contains a fixed-instance affine theorem giving a canonical `C_0` density for every fixed rank-at-least-three symmetric quadratic form under arbitrary cap-one product laws. Since `s_9(A)>0` implies `rank(A)>=9`, that theorem can be combined with the interval bound (5.2) to obtain a canonical `C_0` representative with the same `<2510 K^2/s` height. I do not relabel that separate continuity theorem as newly reproved here.

## 7. Eight-direction endpoint remains open

The current threshold-eight terminal theorem produces a quantitative no-pivot overlap-one/two-sided collar and a universal half-potential `<53.338`, hence square-root interval concentration, but no dimension-free linear interval estimate. The improvement above changes only the threshold-nine constant and does not pay that collar. Thus:

- multiplicity 9: complete candidate height theorem, now `<2510 K^2/s` after this arithmetic sharpening;
- multiplicity 8: universal-height theorem still open;
- unrestricted multiplicity 3: open.

The exact rational arithmetic for Sections 2--4 is recorded in `CHECKS.py` and `checks.json` in this run directory.
