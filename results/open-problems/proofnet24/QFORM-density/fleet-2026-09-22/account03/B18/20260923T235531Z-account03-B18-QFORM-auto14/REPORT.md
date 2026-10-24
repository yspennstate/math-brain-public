SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T23:55:31Z.
attacking: source-valid one-sided cross-bank plus independent scalar-square smoothing, with arbitrary same-side curvature and outside affine terms retained.

# account03/B18 auto14 — one-sided cross plus square Lp receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T235531Z-account03-B18-QFORM-auto14`  
Status: `NEW SUPPORTING THEOREM / TARGET-VALID FAMILY CLOSED / FULL QFORM OPEN`.

## 1. Statement

Let
- `X=(X_1,...,X_m)` and `Y=(Y_1,...,Y_n)` be two disjoint original-coordinate banks;
- `W` be one more original coordinate, disjoint from both banks;
- all coordinates be mutually independent and have probability densities bounded by one;
- `M` be a nonzero real `m x n` matrix and `sigma=||M||_op>0`;
- `alpha in R^m`, `a != 0`, `d,c in R`;
- `G:R^n -> R` be arbitrary measurable.

Define

`T = X^T M Y + alpha^T X + G(Y) + a W^2 + d W + c`.

Then for every `1<q<2`, with `p=q/(q-1)`, `T` has a continuous density vanishing at infinity and

\[
 \boxed{
 \|p_T\|_\infty\le
 \frac{q}{q-1}
 2^{1+1/q}(2-q)^{-1/q}
 \sigma^{-1/q}|a|^{-(q-1)/q}.}
 \tag{1.1}
\]

In particular at `q=3/2`,

\[
 \boxed{
 \|p_T\|_\infty\le
 12\,2^{1/3} (|a|\sigma^2)^{-1/3}.}
 \tag{1.2}
\]

Call this supporting result `QFORM-ONE-SIDED-CROSS-SQUARE-LP-v1`.

The theorem permits arbitrary quadratic/affine curvature inside the `Y` bank through `G(Y)`. It does **not** permit an `X`-side quadratic term or a coupling of `W` back into `X` or `Y`. Arbitrary coordinates outside the displayed principal pattern may nevertheless be conditioned: their couplings become the allowed affine terms `alpha`, `d`, and additions to `G`.

## 2. Primary-source transfer: sharp density of linear forms

The source-valid external input is Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2. For independent real random variables with densities bounded by `K` and coefficients `r_j` with `sum r_j^2=1`, the density of `sum r_j X_j` is bounded by `sqrt(2) K` a.e. The theorem has no Gaussian, log-concavity, moment, support, iid, centering, symmetry, or smoothness assumption.

This is applied only to genuine original-coordinate product banks. No rotated spectral coordinates are declared independent.

A second primary-source scope check is Hu--Paouris, *Small Ball Probabilities for Simple Random Tensors*, arXiv:2403.20192. Their bounded-coordinate tensor theorem gives the expected logarithmic small-ball behavior in the bilinear/tensor setting. It is consistent with the mandatory rank-two hyperbolic logarithm, but its displayed centered tensor small-ball theorem is not used here as a translation-uniform density theorem.

## 3. Cross-bank `L^p` density estimate

Set

\[
R=X^TMY+\alpha^TX+G(Y).
\]

For fixed `Y=y`, put `c(y)=My+alpha`. Conditional on `Y=y`,

\[
R=c(y)^TX+G(y).
\]

Whenever `c(y) != 0`, Rudelson--Vershynin gives

\[
\|p_{R\mid Y=y}\|_\infty\le {\sqrt2\over\|c(y)\|_2}.
\tag{3.1}
\]

Since this conditional density has total mass one,

\[
\|p_{R\mid Y=y}\|_p
 \le \left({\sqrt2\over\|c(y)\|_2}\right)^{1-1/p}
 = \left({\sqrt2\over\|c(y)\|_2}\right)^{1/q}.
\tag{3.2}
\]

Choose unit left/right singular vectors `u,v` for the top singular value, so

\[
u^TM=\sigma v^T.
\]

Therefore

\[
\|c(Y)\|_2\ge |u^Tc(Y)|
 =|\sigma v^TY+u^T\alpha|.
\tag{3.3}
\]

The scalar

\[
Z=\sigma v^TY+u^T\alpha
\]

has density cap `K=sqrt(2)/sigma`, again by the same primary theorem. In particular `P(Z=0)=0`, so (3.1)--(3.3) hold almost surely for the purpose of the following average.

For `0<theta<1`, every probability density `h<=K` obeys the sharp bathtub estimate

\[
\int |z|^{-\theta}h(z)\,dz
\le { (2K)^\theta\over1-\theta}.
\tag{3.4}
\]

Indeed the decreasing weight is maximized by `h=K` on the centered interval of length `1/K`.
With `theta=1/q`, (3.4) and Minkowski yield

\[
\begin{aligned}
\|p_R\|_p
&\le \mathbb E\|p_{R\mid Y}\|_p\\
&\le 2^{1/(2q)}\mathbb E |Z|^{-1/q}\\
&\le {q\over q-1}\left({4\over\sigma}\right)^{1/q}.
\end{aligned}
\tag{3.5}
\]

This step retains the full arbitrary function `G(Y)` because it only translates each conditional linear density.

## 4. Translation-uniform square `L^q` estimate

Complete the square:

\[
aW^2+dW=a(W+d/(2a))^2-d^2/(4a).
\]

Translation preserves the cap-one property. For completeness, let `U=W+d/(2a)` and let

\[
r(t)=f_U(t)+f_U(-t),\qquad t>0.
\]

Then `0<=r<=2` and `int_0^infty r(t)dt=1`. The density of `|a|U^2` satisfies, under `y=|a|t^2`,

\[
\int p(y)^qdy
=(2|a|)^{1-q}\int_0^\infty r(t)^q t^{1-q}dt.
\tag{4.1}
\]

Because `t^(1-q)` is decreasing and `0<=r<=2` with mass one, bathtub rearrangement gives

\[
\int_0^\infty r(t)^q t^{1-q}dt
\le 2^q\int_0^{1/2}t^{1-q}dt
={2^{2q-2}\over2-q}.
\]

Consequently

\[
\boxed{
\|p_{aW^2+dW}\|_q
\le
\left({2^{q-1}\over2-q}\right)^{1/q}|a|^{-1+1/q}.}
\tag{4.2}
\]

This independently reproduces the corrected translation-uniform square estimate recorded by account03/B15 after its nonzero-slope shortcut was refuted. In particular, no affine slope is credited with artificial smoothing.

## 5. Convolution and continuity

`R` depends only on the original `X,Y` banks and is genuinely independent of `W`. Young/Hölder convolution with `1/p+1/q=1` gives

\[
\|p_T\|_\infty\le\|p_R\|_p\|p_{aW^2+dW}\|_q.
\]

Substituting (3.5) and (4.2) is exactly (1.1).
At `q=3/2`, the constant simplifies to (1.2).

Moreover `p_R in L^p` and the square density is in `L^q`, with finite conjugate exponents. Hence their convolution has a continuous representative vanishing at infinity: translation continuity in `L^q` gives continuity by Holder, and compactly-supported `L^p/L^q` approximation gives vanishing at infinity. Thus this theorem proves `C_0` regularity, not only essential boundedness.

## 6. Target-valid physical form and pseudodeterminant scale

Take three original independent coordinates `U,V,W` and

\[
Q_b=2bUV+aW^2+\text{arbitrary affine terms allowed by the theorem},
\qquad b\ne0,\ a\ne0.
\]

Here `sigma=2|b|`, while the symmetric quadratic matrix has eigenvalues

\[
\{b,-b,a\}
\]

and

\[
D=|\operatorname{pdet}A|=|a|b^2.
\]

Therefore (1.2) becomes the invariant estimate

\[
\boxed{
\|p_{Q_b}\|_\infty
\le {12\over2^{1/3}}D^{-1/3}
=9.524406311809196\ldots\,D^{-1/3}.}
\tag{6.1}
\]

If `|a|>=1` and `|b|>=1`, this is an actual instance of the owner's three-large-eigenvalue target and gives a continuous density bounded by `9.525`.

The same conclusion survives arbitrary outside spectrum/couplings after conditioning, provided the retained original-coordinate principal pattern still has: zero internal `X`-bank quadratic block, a nonzero `X-Y` cross block, an independent scalar square `aW^2`, and no retained `W-(X,Y)` cross edge. Outside couplings only generate affine terms.

## 7. Required application of account04/B18

The latest completed designated-partner result is account04/B18's
`QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1`, report commit
`84fa5922df082f90064dea4d22a600a60e799803`.
For an original-coordinate exact-rank-three `4x4` null-hub block with
`s<=|mu_j|<=L` and one hub edge at least `eta`, it proves

\[
\|p\|_\infty
\le576^{1/3}{L^{2/3}\over s\eta^{2/3}}.
\tag{7.1}
\]

Apply it to the literal four-coordinate block

\[
B_c=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&c&0\\
0&0&0&0
\end{pmatrix},\qquad c\ge1.
\]

Its nonzero spectrum is `{1,-1,c}`. Thus `s=1`, `L=c`, and `eta=1`, so the partner theorem gives

\[
\|p\|_\infty\le576^{1/3}c^{2/3}.
\tag{7.2}
\]

The new theorem applies to the same form as `2X_0X_1+cX_2^2` and gives

\[
\|p\|_\infty\le {12\over2^{1/3}}c^{-1/3}.
\tag{7.3}
\]

Hence an actual combined inequality is

\[
\boxed{
\|p\|_\infty\le
\min\{576^{1/3}c^{2/3},\; (12/2^{1/3})c^{-1/3}\}.}
\tag{7.4}
\]

The partner estimate is sharper near `c=1`; the new cross-square estimate is sharper for

\[
c> {12/2^{1/3}\over576^{1/3}}
=1.1447142425533319\ldots .
\]

At `c=64`, (7.2) is `133.1253646753...`, while (7.3) is `2.38110157795...`. This is a genuine application of the designated partner result at the same target-valid matrix, not merely a citation.

## 8. Literature scope and corrections

The argument consumes the live corrections as follows.

- No law-uniform pointwise quadratic van-der-Corput decay is used.
- No arbitrary-joint coarea bound is used.
- No conditional density cap is reinterpreted as independence.
- No random variable is rotated and then declared independent.
- No small nonzero coefficient is deleted.
- No uniformly good physical minor is asserted from `s_3(A)>=1`.
- The account03/B15 correction `QFORM-B15-NONZERO-SQUARE-AFFINE-SLOPE-RESCUE-FALSE-v1` is explicitly respected: the square estimate (4.2) is uniform in the translation/slope and does not improve as `|d|` grows.

Hu--Paouris' tensor small-ball theorem is recorded only as a scope comparison; it is not promoted to an arbitrary-center scalar density theorem. The exact proof above needs only Rudelson--Vershynin Theorem 1.2 plus elementary rearrangement and convolution.

## 9. Remaining connection to the full target

The unrestricted conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open.

The new receiver pays any branch in which original-coordinate algebra can expose simultaneously:
1. a cross bank with zero quadratic curvature on one side;
2. a disjoint nonzero scalar square; and
3. no retained cross edge from that scalar-square coordinate back into the two banks.

The bare hypothesis `s_3(A)>=1` does not currently force such a product-preserving pattern. The remaining compiler must either extract this geometry with a uniform scale, or route its failure into the already-paid ridge/grouped-cross/hub/volume mechanisms. Arbitrary fully source-entangled residual curvature remains the first essential missing implication.

## 10. Integrity / privacy / execution notes

Changed-file allowlist for this mathematical repository run is restricted to this immutable run directory. The content contains only abstract mathematics, public bibliographic metadata, and source commit identifiers; no credentials, private personal data, scheduler IDs, machine paths, signed URLs, trading/company/client data, or unrelated material are present. No installation, remote workflow, public release, paid API/model call, or permission expansion was performed.

Repository transport is not native mathematical-memory ingestion. Brain status remains `WITHOUT_VERIFIED_BRAIN` unless a genuine authenticated receiver retrieval/use is separately observed.
