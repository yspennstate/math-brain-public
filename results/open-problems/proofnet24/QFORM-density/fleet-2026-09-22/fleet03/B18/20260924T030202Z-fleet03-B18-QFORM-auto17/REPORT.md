SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-24T03:02:02Z.
attacking: the endpoint Lorentz interpolation between a rough cross-bank density and an independent scalar square, replacing the q<2 loss at the square endpoint.

# fleet03/B18 auto17 — endpoint Lorentz cross-plus-square receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T030202Z-fleet03-B18-QFORM-auto17`  
Status: **NEW SUPPORTING THEOREM / CONTINUOUS-DENSITY BRANCH / FULL QFORM OPEN**.  
Native brain status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact theorem

Let
- `X=(X_1,...,X_m)` and `Y=(Y_1,...,Y_n)` be disjoint original-coordinate banks;
- `W` be one more original coordinate, disjoint from both banks;
- all coordinates be mutually independent with probability densities bounded by one;
- `M` be a nonzero real `m x n` matrix, with `sigma=||M||_op>0`;
- `alpha in R^m`, `a!=0`, `d,c in R`;
- `G:R^n -> R` be arbitrary measurable.

Put

`R = X^T M Y + alpha^T X + G(Y)`

and

`T = R + a W^2 + dW + c`.

Then `T` has a continuous density vanishing at infinity and

\[
\boxed{\|p_T\|_\infty\le {16\over\sqrt{|a|\,\sigma}}.}\tag{1.1}
\]

Call this result `QFORM-CROSS-SQUARE-LORENTZ-ENDPOINT-v1`.

This is the endpoint companion to this slot's earlier `QFORM-ONE-SIDED-CROSS-SQUARE-LP-v1`, whose strong-`L^q` proof required `q<2` because a scalar square density is generally not in strong `L^2`. The present result reaches the missing square endpoint through the exact pair `L^{2,1}` and weak `L^{2,\infty}`.

The theorem retains arbitrary same-bank curvature through `G(Y)`. It does not allow an `X`-side quadratic term or a coupling of `W` back into the retained `X,Y` banks. Arbitrary coordinates outside this retained pattern can be conditioned, provided their couplings become only the displayed affine terms/additions to `G`.

## 2. Primary-source transfer and literature match

The external anti-concentration input is Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2. If independent real variables have densities bounded by `K` and the coefficient vector has Euclidean norm one, the resulting scalar linear form has density bounded by `sqrt(2) K`. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, centering, symmetry, or smoothness assumption is present.

Source: https://arxiv.org/abs/1402.4492 ; published version IMRN 2015(19), 9594--9617.

The endpoint convolution language is the classical Lorentz-space setting of Richard O'Neil, *Convolution operators and L(p,q) spaces*, Duke Math. J. 30 (1963), 129--142, DOI `10.1215/S0012-7094-63-03015-1`. To avoid any normalization ambiguity in Lorentz quasi-norm conventions, the needed endpoint inequality is rederived below directly from decreasing rearrangements rather than quoted with a black-box constant.

No quadratic-form paper found in the current source check supplies the owner's full arbitrary-rough, arbitrary-non-iid theorem; this report makes no novelty claim about the general Lorentz machinery.

## 3. A Lorentz `L^{2,1}` bound for the cross-bank density

For fixed `Y=y`, define

\[
c_y=My+\alpha.
\]

Except on a null set identified below, conditioning on the genuine original-coordinate bank `Y` gives

\[
R=c_y^T X+G(y),
\]

so Rudelson--Vershynin gives

\[
\|p_{R\mid Y=y}\|_\infty\le {\sqrt2\over\|c_y\|_2}.\tag{3.1}
\]

Choose unit left/right singular vectors `u,v` for `sigma`, so

\[
u^TM=\sigma v^T.
\]

Set

\[
Z=\sigma v^TY+u^T\alpha.
\]

Then

\[
\|c_Y\|_2\ge |u^Tc_Y|=|Z|.\tag{3.2}
\]

A second application of Rudelson--Vershynin to the original `Y` coordinates gives

\[
\|p_Z\|_\infty\le {\sqrt2\over\sigma}.\tag{3.3}
\]

In particular `P(Z=0)=0`; hence (3.1) supplies a conditional density almost surely, and averaging gives a density `p_R`.

Define the random conditional cap

\[
K(Y)={\sqrt2\over\|c_Y\|_2}.
\]

By (3.2)--(3.3), for every `s>0`,

\[
\begin{aligned}
P\{K>s\}
&\le P\{|Z|<\sqrt2/s\}\\
&\le {\sqrt2\over\sigma}\,{2\sqrt2\over s}
={4\over\sigma s}.
\end{aligned}\tag{3.4}
\]

Write

\[
C={4\over\sigma}.\tag{3.5}
\]

Let `E` be any measurable subset of the line with Lebesgue measure `t`. Conditional on `Y`,

\[
P\{R\in E\mid Y\}\le \min\{1,tK\}.
\]

Using layer cake for `min(1,tK)`,

\[
\int_E p_R
\le t\int_0^{1/t}P\{K>s\}\,ds.
\tag{3.6}
\]

If `0<t<=1/C`, insert (3.4):

\[
\int_E p_R
\le Ct\left(1+\log {1\over Ct}\right).
\tag{3.7}
\]

For `t>=1/C` the probability bound `int_E p_R<=1` is enough.

Let `p_R^*` denote the decreasing rearrangement. Since

\[
\int_0^t p_R^*(s)ds=\sup_{|E|=t}\int_Ep_R
\]

and `p_R^*` is decreasing, (3.7) yields

\[
p_R^*(t)\le
\begin{cases}
C\left(1+\log {1\over Ct}\right),&0<t\le1/C,\\
1/t,&t\ge1/C.
\end{cases}\tag{3.8}
\]

Use the explicit Lorentz integral

\[
\|f\|_{2,1}^{\#}:=\int_0^\infty t^{-1/2}f^*(t)\,dt.
\]

Equation (3.8) gives

\[
\begin{aligned}
\|p_R\|_{2,1}^{\#}
&\le C\int_0^{1/C}t^{-1/2}\left(1+\log{1\over Ct}\right)dt
+\int_{1/C}^\infty t^{-3/2}dt\\
&=\sqrt C\left[\int_0^1u^{-1/2}du+
\int_0^1u^{-1/2}\log(1/u)du\right]+2\sqrt C\\
&=\sqrt C(2+4)+2\sqrt C
=8\sqrt C
={16\over\sqrt\sigma}.
\end{aligned}\tag{3.9}
\]

This is the endpoint gain: the cross-bank density need not be bounded uniformly, but its logarithmic concentration profile belongs to `L^{2,1}` with a scale-exact norm.

## 4. The scalar square is weak `L^2`, uniformly in translation

Complete the square:

\[
aW^2+dW=a\left(W+{d\over2a}\right)^2-{d^2\over4a}.
\]

Let `U=W+d/(2a)`. Translation preserves the density cap `<=1`. Up to reflection and an irrelevant output translation, the square variable is `|a|U^2`. Its density satisfies for `r>0`

\[
g(r)=
{f_U(\sqrt{r/|a|})+f_U(-\sqrt{r/|a|})
\over2\sqrt{|a|r}}
\le {1\over\sqrt{|a|r}}.
\tag{4.1}
\]

Therefore for every `lambda>0`,

\[
|\{g>\lambda\}|\le {1\over |a|\lambda^2},
\]

and consequently

\[
\boxed{g^*(t)\le {1\over\sqrt{|a|t}}.}\tag{4.2}
\]

Thus the translated square density is uniformly in weak `L^2`; importantly, no large affine slope is credited with fictitious extra smoothing.

## 5. Endpoint convolution, boundedness, and continuity

The random variables `R` and `aW^2+dW` are genuinely independent because `W` is a disjoint original coordinate. Hardy--Littlewood rearrangement gives, for every `x`,

\[
\begin{aligned}
(p_R*g)(x)
&\le\int_0^\infty p_R^*(t)g^*(t)dt\\
&\le |a|^{-1/2}
\int_0^\infty t^{-1/2}p_R^*(t)dt\\
&\le {16\over\sqrt{|a|\sigma}},
\end{aligned}\tag{5.1}
\]

which proves (1.1).

Continuity is also available. Since `p_R in L^{2,1}` and the Lorentz second index is finite, bounded compactly supported functions can approximate `p_R` in `L^{2,1}`; then smooth compactly supported functions can be used as approximants. If `f_j -> p_R` in the norm (3.9), the same rearrangement inequality and (4.2) imply

\[
\|(f_j-p_R)*g\|_\infty
\le |a|^{-1/2}\|f_j-p_R\|_{2,1}^{\#}\to0.
\]

Each `f_j*g` is continuous and vanishes at infinity because `f_j` is continuous compactly supported and `g in L^1`. Uniform convergence proves that `p_T=p_R*g` has a continuous representative in `C_0(R)`.

## 6. Relation to the earlier strong-`L^q` receiver

At `q=3/2`, the earlier result from this slot gives

\[
\|p_T\|_\infty
\le 12\,2^{1/3}(|a|\sigma^2)^{-1/3}.
\tag{6.1}
\]

Combining (1.1) and (6.1),

\[
\boxed{
\|p_T\|_\infty
\le
\min\left\{
{16\over\sqrt{|a|\sigma}},
12\,2^{1/3}(|a|\sigma^2)^{-1/3}
\right\}.}
\tag{6.2}
\]

The new endpoint is strictly sharper when

\[
{|a|\over\sigma}>
\left({16\over12\,2^{1/3}}\right)^6
=1.4046639231824423\ldots .
\tag{6.3}
\]

Thus this is not a restatement of the preceding `q<2` family: it removes its endpoint blow-up and quantitatively pays the square-dominant anisotropic regime.

For the physical three-coordinate form

\[
Q=2bUV+aW^2,
\]

one has `sigma=2|b|` and hence

\[
\boxed{
\|p_Q\|_\infty\le {8\sqrt2\over\sqrt{|ab|}}.}
\tag{6.4}
\]

If `|a|,|b|>=1`, this is a literal instance of the owner target, with continuous density and the universal numerical bound `8 sqrt(2)=11.313708498984761...`. The endpoint improves the prior `q=3/2` estimate on this family exactly when `|a|/|b|>2.8093278463648845...`.

## 7. Required equation-level application of fleet04/B18

The designated partner result is fleet04/B18 r5, `QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1`, canonical report

`yspennstate/math-open-problems@84fa5922df082f90064dea4d22a600a60e799803`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T221534Z-fleet04-B18-QFORM-r5/REPORT.md`.

For an original-coordinate exact-rank-three `4x4` null-hub core with `s<=|mu_j|<=L` and one hub edge at least `eta`, it proves

\[
\|p_Q\|_\infty\le576^{1/3}{L^{2/3}\over s\eta^{2/3}}.
\tag{7.1}
\]

Apply both (7.1) and the new theorem to the literal target-valid block

\[
B_c=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&c&0\\
0&0&0&0
\end{pmatrix},\qquad c\ge1.
\tag{7.2}
\]

Its nonzero spectrum is `{1,-1,c}`. The partner theorem has `s=1`, `L=c`, `eta=1`, so

\[
\|p\|_\infty\le576^{1/3}c^{2/3}.
\tag{7.3}
\]

The new theorem sees the same form as `2X_0X_1+cX_2^2`, hence `sigma=2`, `|a|=c`, and gives

\[
\|p\|_\infty\le8\sqrt2\,c^{-1/2}.
\tag{7.4}
\]

Therefore the actual combined inequality is

\[
\boxed{
\|p\|_\infty\le
\min\left\{576^{1/3}c^{2/3},\,8\sqrt2\,c^{-1/2}\right\}.}
\tag{7.5}
\]

The new endpoint becomes sharper than the partner window estimate for

\[
c>1.3013611842445794\ldots .
\]

At `c=64`, the partner bound is `133.12536467532183...`, the prior strong-`L^{3/2}` bound is `2.381101577952299...`, and the new Lorentz endpoint is

\[
\boxed{\sqrt2=1.4142135623730951\ldots}.\tag{7.6}
\]

This is a direct application of the designated partner theorem to the same matrix, not merely a bibliographic citation.

## 8. Corrections respected and remaining connection to the full target

The proof never rotates random variables and then asserts independence. It uses the projection-density theorem only for genuine linear forms of original-coordinate product banks, then supplies the nonlinear square smoothing separately. It does not use law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, a conditional density cap as independence, a fixed-good-minor assertion, a small-coefficient deletion, a moment assumption, or Monte Carlo evidence.

The unrestricted quadratic-form conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open. The new receiver closes a quantitative endpoint inside a product-preserving cross-plus-private-square geometry; the bare hypothesis `s_3(A)>=1` still does not force this geometry. The global compiler must force a target-scale cross/square decomposition or route its failure into the already-paid E3 product-Fourier, ridge, grouped-hub, pair-log, or other product-preserving branches while retaining arbitrary extra spectrum.

## 9. Integrity / execution notes

Only abstract mathematics, public bibliographic metadata, logical fleet labels, and nonsecret commit hashes are present. No unrelated personal/company/trading/client material, credentials, scheduler identifiers, signed URLs, machine paths, public release, paid model/API call, remote workflow, installation, permission expansion, email, or push action is involved. Repository transport is not native mathematical-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
