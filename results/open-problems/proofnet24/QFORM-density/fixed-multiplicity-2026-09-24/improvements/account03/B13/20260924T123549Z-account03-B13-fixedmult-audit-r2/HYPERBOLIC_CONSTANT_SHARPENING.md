# QFORM-FIXEDMULT-B13-CONSTANT-3110-v1

Source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

The same seventeen-eigenvalue proof admits the following replacements, with no hypothesis change:

1. Exact singular kernel:
   - `0<d<=1`: `J(d)=2 asinh(d^{-1/2})+pi+2 acosh(d^{-1/2})`;
   - `d>=1`: `J(d)=2 asinh(d^{-1/2})+2 asin(d^{-1/2})`.
   Hence `J(d)<7+2 log_+(1/|d|)`.
2. The exact Gaussian-smoothing coefficient in the quarter-power lemma satisfies
   `2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)<9/2`, using
   `Gamma(3/8)<11779489/4740120<5/2`. Thus
   `P{|R-a|<rho} <= min(1,(9/2)(rho/L)^(1/4))` and
   `sup_a E log_+(1/|R-a|) <= 4+4 log(9/2)` for `L>=1`.
3. The hyperbolic branch constant is retained exactly as `(15/2)log 2` instead of rounding to `6`.
4. With `eta=1/100`, every pivot under the manuscript's two-direction hypothesis therefore has truncated half-potential `<310`:
   - scalar pivot `<278`;
   - definite pair `<160`;
   - indefinite pair `<=10[8+30 log2+4 log(8/5)]<310`.
5. Hence under `s_9(A)>=1`, the full half-potential is `<311`. At the main scalar pivot, the square profile contributes at most `10`, giving density `<3110`. The no-pivot branch stays `<2400`; both pair branches are smaller.

Therefore, for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, and arbitrary affine `b,c`,

\[
\boxed{\quad s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty<3110\,K^2/s.\quad}
\]

This is a proved constant improvement only. It does not lower seventeen. The order-four route to thirteen still hits the `|t|^{-1}` absolute-Fourier endpoint and needs a new structural endpoint theorem.
