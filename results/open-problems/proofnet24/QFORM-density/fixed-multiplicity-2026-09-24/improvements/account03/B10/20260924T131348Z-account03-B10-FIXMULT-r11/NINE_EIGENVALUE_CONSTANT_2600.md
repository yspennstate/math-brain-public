# QFORM-FIXED-MULTIPLICITY-9-CONSTANT-2600-v1

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Nine-direction source: account03/B04 candidate at `8ff490c177d0cd7d6f33130f1431785e312a9d10`, independently reconstructed by account01/B16 (`54ec2a651d854563f8db0d92c4c3426f76551786`), account03/B08 (`c02a08f19d010e508578695a5906744fdbcfcd70`), and independently again in account03/B10 audit commit `62504c6e976c8b45ae373b8141b111cc31507a1d`.

## Theorem

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by `K`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

\[
s_9(A)\ge s>0,
\]

then `Q=X^TAX+b^TX+c` has an essentially bounded density and

\[
\boxed{\ \|p_Q\|_\infty<2600\,K^2/s.\ }
\]

No support, moment, log-concavity, sign, diagonal-basis, exact-rank, leverage, smoothness, or post-rotation-independence assumption is added. Global continuity is not asserted.

## Constant ledger in the normalized case

Take `K=s=1`, `eta=1/100`, `kappa=1/80^2`.

1. **No pivot.** The nine-direction spectral-to-volume theorem gives `V_3>=kappa^3`; a fair coordinate cut gives `E_3>=4^-3 kappa^3`. The marginal-free third-volume receiver gives a continuous bounded density. Even the self-contained grouped compiler has coefficient `<15`, hence
   \[
   \|p_Q\|_\infty<15\cdot160=2400.
   \]

2. **Scalar pivot.** The Schur complement retains at least eight unit spectral directions. If it has a pivot, the sharpened pivot theorem below gives full half potential `<260`. If it has no pivot, then `s_5>=1`; the order-two spectral-to-volume theorem plus fair cut gives `E_2^{-1/8}=sqrt(160)`, while the marginal-free two-volume receiver gives coefficient `<13`, hence full half potential `<13sqrt(160)<169<260`. The square profile therefore gives
   \[
   \|p_Q\|_\infty<10\cdot260=2600.
   \]

3. **Definite pair pivot.** Direct density bound `<10pi<40`.

4. **Indefinite pair pivot.** The Schur complement keeps at least seven unit directions, hence the manuscript hyperbolic/log-potential density estimate is `<251`.

Thus `2600` dominates all normalized branches.

## Sharpened pivot theorem

For the singular convolution kernel

\[
J(d)=\int_{-1}^1|x|^{-1/2}|x-d|^{-1/2}dx,
\]

direct exact integration gives

\[
J(d)<6+2\log_+(1/|d|).
\]

The manuscript quarter-power Gaussian coefficient satisfies the exact rational certificate

\[
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<35/8,
\]

and `log(35/8)<119/80`. Therefore one surviving unit spectral direction gives

\[
\sup_a E\log_+(1/|R-a|)<199/20.
\]

At a scalar pivot, the truncated half potential is then

\[
H<10\left(6+2\cdot199/20\right)=259.
\]

For an indefinite pair, optimize the original-coordinate hyperbolic tail proof with cancellation ratio `q=2/9`. If

\[
C_0=2\log3+\frac{37}{14}\log2,
\qquad B=\frac{36\sqrt2}{49},
\]

the conditional density satisfies

\[
p(z)\le D^{-1/2}\left(C_0+\log_+\frac{B\sqrt D}{|z-v|}\right).
\]

The manuscript logarithmic-kernel integral yields

\[
H_{\rm ind}(D)\le D^{-1/2}\left(4C_0+8+4\log_+(B\sqrt D)\right).
\]

For `D>=1/100` this is decreasing in `sqrt D`; since `B/10<1`, its maximum is `10(8+4C_0)`. The elementary bounds `log2<7/10`, `log3<11/10` imply `C_0<81/20`, hence

\[
H_{\rm ind}<242.
\]

The definite-pair branch is `<160`. Thus every pivot under the two-direction hypothesis has `H<259`, and adding the unit tail gives full half potential `<260`.

## Scaling

Set `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q.
\]

The coordinates of `Y` have density cap one and `s_9(A/s)>=1`. The normalized result and scalar density scaling give

\[
\|p_Q\|_\infty<2600K^2/s.
\]

## Scope

This improves the constant and uses the already completed nine-direction threshold reduction. It does not lower nine. Multiplicity eight and the unrestricted three-eigenvalue conjecture remain open. The no-pivot branch is `C_0`; global continuity is not proved by the pivot argument.
