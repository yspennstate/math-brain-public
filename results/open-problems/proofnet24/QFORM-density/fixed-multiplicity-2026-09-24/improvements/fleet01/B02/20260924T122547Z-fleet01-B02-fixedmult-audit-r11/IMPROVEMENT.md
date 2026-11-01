# B02 improvement: same 17-eigenvalue theorem with constant 4880

Source manuscript blob audited: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This note does **not** lower the multiplicity below 17. It gives a rigorous constant improvement under exactly the same hypotheses, and records why the obvious 16-direction endpoint does not follow from the present analytic inputs.

## Proposition

Under the hypotheses of the manuscript's main theorem,

`independent real X_i with densities <= K`, `A=A^T`, arbitrary `b,c`, and `s_17(A)>=s>0`,

the same proof yields

\[
\|p_{X^TAX+b^TX+c}\|_\infty < 4880\,\frac{K^2}{s}.
\]

No assumption is changed.

## Proof

Only the scalar-pivot constants need tightening.

### 1. Keep the actual coefficient already proved in the quarter-power lemma

In the proof of `lem:quarter`, before the manuscript rounds upward to 16, the Gaussian localization coefficient is
\[
C_*=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]
The manuscript itself proves
\[
\Gamma(3/8)\le 8/3+e^{-1}<10/3,
\]
and then uses the elementary bounds `2^(5/8)<2`, `e^(3/8)<2`, `pi^(-1/4)<1`. Therefore the proof already gives the strictly stronger explicit estimate
\[
C_*<40/3.
\]
Hence the quarter-power concentration statement may be retained as
\[
\Pr\{|R-a|<\rho\}\le
\min\left\{1,\frac{40}{3}(\rho/L)^{1/4}\right\}.
\]
For `L>=1`, layer cake then gives
\[
\sup_a E\log_+\frac1{|R-a|}
\le L_0':=4+4\log(40/3).
\]

### 2. Keep the exact far-region coefficient in the `J(d)` kernel

The proof of `lem:kernels` already shows that on `|x|>2|d|`,
\[
|x|^{-1/2}|x-d|^{-1/2}\le \sqrt2/|x|.
\]
Thus, instead of rounding `2 sqrt(2)` upward to 3, one has for all `d != 0`
\[
J(d)\le 8+2\sqrt2\,\log_+(1/|d|).
\]
(The near region is the same one bounded by 8 in the manuscript; if `2|d|>=1` the far region is empty.)

### 3. Improved scalar-pivot truncated half potential

At a scalar pivot `|a_ii|>=eta=1/100`, the same conditional/Tonelli argument therefore gives
\[
H(Q)\le10\left(8+2\sqrt2\,L_0'\right).
\]
This is less than 487. A completely elementary certificate is as follows:

- `sqrt(2)<14143/10000`, since `(14143/10000)^2>2`;
- `log(40/3)<2591/1000`: indeed the degree-9 positive Taylor partial sum for `exp(2591/1000)` already exceeds `40/3`.

Therefore
\[
L_0'<4+4(2591/1000)=14.364,
\]
and
\[
10\left(8+2\sqrt2 L_0'\right)
<486.301<487.
\]

The other pivot-half-potential branches remain below 487 without any modification: the definite branch is `<160`; the manuscript's indefinite estimate is `<444`.
Hence the proposition `pivot controls truncated half potentials` may be sharpened from `H(Q)<=600` to
\[
H(Q)<487.
\]

### 4. Improved nine-direction full half potential

If `s_9(A)>=1` and there is a pivot, the preceding estimate plus the tail `|Q-a|^{-1/2}<=1` outside `|Q-a|<=1` gives
\[
\sup_a E|Q-a|^{-1/2}<488.
\]
If there is no pivot, the manuscript already proves the stronger full bound `<200`. Thus the manuscript's `601` can be replaced by `488`.

### 5. Main theorem

At a scalar pivot in the 17-direction theorem, `|a_ii|^{-1/2}<=10`; hence
\[
\|p_Q\|_\infty<10\cdot488=4880.
\]
The other branches are already smaller: no-pivot `<2400`, definite pair `<40`, indefinite pair `<251`. Scaling `Y=KX` and `\widetilde Q=(K^2/s)Q` is unchanged. This proves the proposition.

## Multiplicity-lowering attempt

The present proof does **not** justify replacing 17 by 16. In the terminal `r=4` bad-volume-ratio chamber, `s_17>=1` and `rank R<=12` force five large entries of `D`, while `rank R[L,L]<=4`; a `5x5` diagonally dominant block contradicts rank four. With only `s_16>=1`, the same calculation forces exactly four large entries, and an invertible `4x4` block is compatible with rank four. Thus the current interpolation/rank count genuinely stops at 17.

Nor can one lower to 16 merely by replacing order five by the order-four Fourier endpoint plus the existing quarter-power concentration. An order-four crossing gives only `|phi(t)|=O(1/|t|)`. The probability density
\[
p(x)=\frac12\log(1/|x|)\,\mathbf 1_{|x|<1}
\]
is unbounded, but integration by parts gives
\[
\phi(t)=\frac{\operatorname{Si}(t)}{t}=O(1/|t|),
\]
and its worst interval small-ball mass is of order `rho(1+log(1/rho))`, hence is bounded by a constant times `rho^(1/4)`. Therefore those two analytic estimates alone do not imply bounded density. A valid 16-eigenvalue proof needs additional quadratic/product structure in the terminal `r=4` chamber (or a genuinely stronger endpoint theorem).

## Status

- Constant improvement to `<4880 K^2/s`: **proved in this note, pending separate review**.
- Multiplicity improvement 17 -> 16: **not proved**.
- Full three-eigenvalue conjecture: **not claimed**.
