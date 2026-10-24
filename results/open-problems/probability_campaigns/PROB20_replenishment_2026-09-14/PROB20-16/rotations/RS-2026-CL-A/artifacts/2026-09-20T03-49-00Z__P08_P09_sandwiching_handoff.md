# RS-2026-CL-A handoff to P08/P09 — variance-sensitive sandwiching transfer

Source ownership remains RS-2026-CL-A / native `6aa7b4b639a08191b893e2b7dd6cdf59`. This is a reusable lemma, not a transfer of the Randomstrasse claim.

## Reusable theorem

Let `Q` be stationary for a Markov operator `T`, let `P_{<=D}` be the source polynomial/Hermite filtration, and assume

`Adv_Q^{<=D}(P,Q) <= A`.

For a target statistic `f`, suppose there are `g,a in P_{<=D}` such that pointwise

`a>=0`, `|Tf-g|<=a`.

Then

`|E_{PT}f-E_Qf| <= A sqrt(Var_Q f) + (2+2A)||a||_{L2(Q)}`.

The proof uses only stationarity/L2 contraction, the source LDA inequality on `g` and on the nonnegative envelope `a`, and `|Tf-g|<=a`.

Equivalently define

`Sand_D(Tf;Q)=inf ||a||_2`

over such degree-`D` pairs. Then

`|E_{PT}f-E_Qf| <= A sqrt(Var_Qf)+(2+2A)Sand_D(Tf;Q)`.

For `[0,1]` decision tests with `E_Q f ->0`, bounded source LDA plus `Sand_D(Tf;Q)->0` rules out strong distinction. No global planted `L2`, Renyi, smoothed-likelihood-tail, or frame-conditioning hypothesis is required.

## Gaussian / OU specialization

Take `Q=gamma_m` and `T=U_t` the Ornstein--Uhlenbeck operator. If a bounded phase-retrieval or tensor decision statistic `f` admits Hermite-degree-`D` polynomials `g,a` with

`a>=0`, `|U_t f-g|<=a`, `||a||_{L2(gamma_m)}=o(1)`,

then any planted law with bounded Hermite LDA through degree `D` cannot strongly distinguish through `f` after OU noise, regardless of the planted law's full Hermite tail.

This suggests a proof architecture different from bounding the entire planted likelihood:

1. smooth the target decision statistic by OU;
2. approximate the smoothed statistic on its bulk by a low Hermite degree polynomial;
3. build a **nonnegative low-degree polynomial envelope/guard** for the approximation error, including the Gaussian tail region;
4. bound the guard's `L2(gamma_m)` norm.

For a Gaussian-process or tensor statistic, any concentration lemma that yields such a polynomial guard is immediately reusable by the theorem above.

## Exact-moment endpoint and prior art warning

If `A=0`, classical degree-`D` sandwiching polynomials `p_-<=Tf<=p_+` give directly

`|E_{PT}f-E_Qf| <= E_Q[p_+-p_-]`.

Sandwiching polynomials are established pseudorandomness/learning machinery; do not claim that concept as new. The RS-2026-CL-A contribution is the variance-sensitive bounded-LDA extension and its use to separate test-side and likelihood-side obstructions.

## Mao calibration

For Mao arXiv:2607.20318, source LDA is exactly zero through `D_n`, yet a noised rank-test indicator has expectation gap `1-o(1)`. Therefore its degree-`D_n` sandwiching defect satisfies

`Sand_{D_n}(T f_n;Q_n) >= 1/2-o(1)`.

Any proposed Gaussian/tensor analogue that would purport to cover arbitrary tests should be stress-tested against an analogous macroscopic sandwiching defect.