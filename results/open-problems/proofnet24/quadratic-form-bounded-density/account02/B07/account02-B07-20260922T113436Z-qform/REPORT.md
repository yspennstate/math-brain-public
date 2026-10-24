# account02/B07 — pointwise-decay obstruction and an integrated L3 replacement

**Run:** `account02-B07-20260922T113436Z-qform`  
**Classification:** `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED`.  
**Full quadratic-form bounded-density conjecture:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and owner supersession

The active owner target at control commit `63d2a5aaeeb662e9630d01ce5ee20b68710ea347`, OWNER revision `2026-09-22.4`, is:

> For independent real random variables `X_1,...,X_n` with densities bounded by `1`, and every real symmetric quadratic form `Q(x)=x^T A x` having at least three eigenvalues with absolute value at least `1`, prove that the law of `Q(X)` has a density bounded by one universal constant, independent of `n`, the laws and `A`.

This later OWNER MESSAGE explicitly supersedes the earlier FEI assignment. No FEI mathematics is used below.

A compact end-to-end Fourier route would be: prove a universal bound

\[
\int_{\mathbb R}\left|\mathbb E e^{itQ(X)}\right|\,dt\le C_1,
\]

then Fourier inversion gives `||p_Q||_infty <= C_1/(2*pi)`. The first advertised substep in the owner note was a law-independent pointwise estimate `|E e^{isX^2}| \lesssim |s|^{-1/2}` for every density `f<=1`. That substep is false. The useful replacement is an **integrated `L^3` estimate**, which is exactly strong enough to prove the complete coordinate-diagonal three-large-eigenvalue case and also explains why two opposite-sign squares remain critical.

## 2. Refutation of the uniform pointwise one-dimensional decay claim

### Proposition 2.1
There is no function `rho(s)->0` such that

\[
\left|\int_{\mathbb R} e^{isx^2}f(x)\,dx\right|\le \rho(s)
\]

for every `s>=1` and every probability density `f` satisfying `0<=f<=1`.
In particular there is no universal `C` with the bound `C s^{-1/2}`.

### Proof
Fix `s>=1` and put

\[
G_s=\{x\in[12,24]:\cos(sx^2)\ge 1/2\}.
\]

The phase map `theta=sx^2` sends `[12,24]` monotonically onto an interval of length

\[
(24^2-12^2)s=432s,
\]

and has derivative at most `48s` there. Every full `2*pi` phase period contained in this image contains a good phase subinterval of length `2*pi/3`, and the inverse image of each such good subinterval therefore has `x`-length at least

\[
\frac{2\pi/3}{48s}=\frac{\pi}{72s}.
\]

Any interval of phase length `432s` contains at least `432s/(2*pi)-2` full periods. Hence

\[
|G_s|\ge \left(\frac{432s}{2\pi}-2\right)\frac{\pi}{72s}
=3-\frac{\pi}{36s}>1.
\]

Choose any measurable `E_s subset G_s` of Lebesgue measure `1` and set `f_s=1_{E_s}`. Then `f_s` is a probability density bounded by `1`, while

\[
\Re\int e^{isx^2}f_s(x)\,dx
=\int_{E_s}\cos(sx^2)\,dx\ge \frac12.
\]

Thus the modulus is at least `1/2` for every `s>=1`, after choosing a source-valid density depending on `s`. This refutes every universal decaying pointwise envelope. QED.

### Consequence for the advertised three-direction pointwise route
Taking three independent variables with this same density and `Q=x_1^2+x_2^2+x_3^2` gives

\[
|\phi_Q(s)|=\prod_{j=1}^3\left|\mathbb E e^{isX_j^2}\right|\ge 1/8.
\]

So a universal pointwise `|t|^{-3/2}` bound, uniform over all admissible laws, is also false even in the easiest diagonal positive-definite case. This does **not** refute the bounded-density conjecture; it refutes only that proposed proof mechanism.

## 3. Integrated replacement: a uniform L3 theorem for one square

Let `X` have density `f<=1`, and let `Y=X^2`. Its density on `(0,infinity)` is

\[
g(y)=\frac{f(\sqrt y)+f(-\sqrt y)}{2\sqrt y}.
\]

Therefore

\[
0\le g(y)\le y^{-1/2},\qquad \int_0^\infty g(y)\,dy=1.
\]

### Lemma 3.1
For every such `g`,

\[
\int_0^\infty g(y)^{3/2}\,dy\le 2\sqrt2.
\]

### Proof
Put `h(y)=y^{-1/2}`, `w(y)=h(y)^{1/2}=y^{-1/4}`, and `a=1/4`. Since

\[
\int_0^a h(y)\,dy=2\sqrt a=1,
\]

and `w` is decreasing, the bathtub comparison gives

\[
\int_0^\infty w(y)g(y)\,dy\le \int_0^a w(y)h(y)\,dy.
\]

Indeed the mass missing from `[0,a]` equals the mass placed in `[a,infinity)`, and its weight can only decrease when moved to the right. Since `g<=h`,

\[
g^{3/2}\le h^{1/2}g=wg,
\]

so

\[
\int g^{3/2}\le \int_0^{1/4}y^{-3/4}\,dy
=4(1/4)^{1/4}=2\sqrt2.
\]

QED.

Let

\[
\psi(t)=\mathbb E e^{itX^2}=\int_0^\infty e^{ity}g(y)\,dy.
\]

With the Fourier convention `hat g(t)=int e^{ity}g(y)dy`, Hausdorff--Young (`p=3/2`, `q=3`) gives

\[
\|\psi\|_3\le (2\pi)^{1/3}\|g\|_{3/2}.
\]

Using Lemma 3.1,

\[
\int_{\mathbb R}|\psi(t)|^3\,dt
\le 2\pi\left(\int g^{3/2}\right)^2
\le 16\pi.
\tag{3.1}
\]

The same estimate holds for a shifted square `(X+c)^2`, since translating `X` preserves the density bound. Scaling gives

\[
\int_{\mathbb R}|\mathbb E e^{it\lambda X^2}|^3dt\le \frac{16\pi}{|\lambda|}
\qquad(\lambda\ne0).
\tag{3.2}
\]

This is a genuine law-independent integrated estimate; Proposition 2.1 shows that one must not replace it by a uniform pointwise decay statement.

## 4. Complete diagonal theorem with explicit constant 8

### Theorem 4.1
Suppose `X_1,...,X_n` are independent with densities bounded by `1`, and

\[
Q(X)=\sum_{j=1}^n \lambda_j X_j^2
\]

has at least three coefficients, say `lambda_1,lambda_2,lambda_3`, satisfying `|lambda_j|>=1`. Then the law of `Q(X)` has a bounded continuous density `p_Q` and

\[
\|p_Q\|_\infty\le 8.
\]

This includes arbitrary signs and arbitrary additional diagonal terms.

### Proof
Write

\[
\psi_j(t)=\mathbb E e^{it\lambda_jX_j^2}.
\]

Independence gives

\[
\phi_Q(t)=\prod_{j=1}^n\psi_j(t).
\]

All characteristic factors have modulus at most `1`. Hence by Holder with exponents `3,3,3` and (3.2),

\[
\begin{aligned}
\int_{\mathbb R}|\phi_Q(t)|dt
&\le \int |\psi_1(t)\psi_2(t)\psi_3(t)|dt\\
&\le \prod_{j=1}^3\|\psi_j\|_3\\
&\le 16\pi\,|\lambda_1\lambda_2\lambda_3|^{-1/3}\\
&\le16\pi.
\end{aligned}
\]

Thus `phi_Q in L^1`. Fourier inversion supplies a bounded continuous density and

\[
\|p_Q\|_\infty\le \frac1{2\pi}\|\phi_Q\|_1\le8.
\]

QED.

### Sharp-threshold interpretation of the method
The exponent `3` is not cosmetic. One square supplies a uniform `L^3` characteristic-function bound. Three independent square factors combine by Holder exactly into `L^1`, which is what density inversion needs. With only two factors the same argument yields only an `L^{3/2}` product bound, not `L^1`; this is consistent with the logarithmic singularity of `X_1^2-X_2^2` in the opposite-sign control case.

## 5. What remains for the full conjecture

The diagonal proof uses independence **after** the quadratic form is diagonalized. For a general symmetric matrix `A`, diagonalizing `A` rotates `X`; the spectral coordinates are then dependent, so the factorization in Theorem 4.1 disappears. The missing implication is therefore not a one-dimensional stationary-phase estimate (that statement is false), but a genuinely coupled integrated estimate.

A clean target formulation is:

> **QFORM-MIXED-L1.** There is a universal `C` such that for every symmetric `A` with third largest singular value at least `1` and every product density `F(x)=prod_i f_i(x_i)` with `0<=f_i<=1` and `int f_i=1`,
> \[
> \int_{\mathbb R}\left|\int_{\mathbb R^n}e^{itx^TAx}F(x)dx\right|dt\le C.
> \]

This implication would close the owner target immediately by Fourier inversion. It must exploit product structure across the original coordinates in an **integrated** way; no uniform pointwise decay can hold under only `f_i<=1`.

A plausible next mechanism is an oscillatory/entropic Brascamp--Lieb inequality or a squared bilinear form obtained from

\[
|\phi(t)|^2=\mathbb E\exp\{it(X-X')^TA(X+X')\},
\]

where the joint density still factors by coordinate pairs. The required estimate should preserve enough of that coordinate-pair product structure to recover three powers of time only after integration in `t`.

## 6. Source and verification record

- Active owner control: `yspennstate/math-research-brain`, commit `63d2a5aaeeb662e9630d01ce5ee20b68710ea347`, `scheduled_tasks/README.md`, OWNER revision `2026-09-22.4`.
- The proof above is self-contained apart from standard Hausdorff--Young and Fourier inversion.
- A web literature check for exact source-matching quadratic-form bounded-density theorems did not produce a theorem matching these quantifiers; this is not a novelty claim and not an exhaustive literature review.
- No numerical or symbolic computation was used in the mathematical proof, so there is no executable certificate to report for these claims.

## 7. Status

`CANDIDATE_REFUTED`: the advertised universal one-direction `|s|^{-1/2}` pointwise decay mechanism, and therefore the derived universal three-direction `|t|^{-3/2}` pointwise envelope, are false for arbitrary densities bounded by `1`.

`ESSENTIAL_STEP_APPLIED`: the uniform integrated `L^3` estimate (3.1) replaces the false pointwise step and gives the complete diagonal theorem with explicit constant `8`, including all sign patterns and extra diagonal terms.

The full rotated/coupled quadratic-form conjecture remains **OPEN**. The first unpaid implication is `QFORM-MIXED-L1` above.
