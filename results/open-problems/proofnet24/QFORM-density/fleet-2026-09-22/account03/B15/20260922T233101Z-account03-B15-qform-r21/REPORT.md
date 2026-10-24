# account03/B15 — rigorous rough-input bridge for the ruled one-sheet theorem

**Run:** `20260922T233101Z-account03-B15-qform-r21`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / RULED_ROUGH_INPUT_BRIDGE_PROVED`  
**Full universal QFORM theorem:** OPEN  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities
`0<=f_i<=1`. Let `r_1,r_2,r_3 in R^n` be orthonormal and let

\[
Q=\lambda_1\langle r_1,X\rangle^2+\lambda_2\langle r_2,X\rangle^2-\mu\langle r_3,X\rangle^2,
\qquad \lambda_1,\lambda_2,\mu\ge1.
\]

This is the exact-rank-three indefinite signature `(+,+,-)` case. The newest Claude-attributed source
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, file
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,
states the ruled one-sheet bound

\[
p_Q(s)\le
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}
\le \pi\sqrt2
\]

for the one-sheet side `s>=0`. The live continuation explicitly asks account03/B15 for an independent
check of the **rough-input bridge**, because an a.e. marginal-density cap cannot simply be evaluated on
a one-dimensional curve.

The result below supplies that missing justification without assuming continuity of the original `f_i`.
It proves the correct rough statement as an interval domination / essential-density bound. Continuity is
kept separate.

## 2. The theorem

### Theorem — `QFORM-RULED-ROUGH-INTERVAL-BRIDGE-v1`

Define the positive-side submeasure

\[
\mu_+(B)=\Pr(Q\in B\cap[0,\infty)).
\]

Then for every interval `I` contained in `[0,infinity)`,

\[
\boxed{
\Pr(Q\in I)
\le C_+(\lambda_1,\lambda_2,\mu)|I|,
}
\]

where

\[
\boxed{
C_+(\lambda_1,\lambda_2,\mu)=
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}
\frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}
\le \pi\sqrt2.
}
\]

Consequently `mu_+` is absolutely continuous and its Radon-Nikodym density satisfies

\[
\boxed{\|d\mu_+/ds\|_\infty\le\pi\sqrt2.}
\]

By sign reversal the identical statement holds on the majority-sign one-sheet side of signature
`(-,-,+)`.

This theorem does **not** claim that the rough-input density has a continuous representative. The central
`L^infinity` conclusion and the stronger continuity conclusion are separate.

## 3. Gaussian padding preserves the target class

Let `G_1,...,G_n` be independent standard Gaussians, independent of `X`, and set

\[
X_i^{(\varepsilon)}=X_i+\varepsilon G_i.
\]

Its density is

\[
f_i^{(\varepsilon)}=f_i*\gamma_\varepsilon.
\]

Because `gamma_epsilon` is a probability density,

\[
0\le f_i^{(\varepsilon)}\le\|f_i\|_\infty\le1,
\qquad \int f_i^{(\varepsilon)}=1.
\]

Thus the padded coordinates remain independent and cap-one. Also

\[
\|f_i^{(\varepsilon)}-f_i\|_1\to0.
\]

For the product laws,

\[
\left\|\bigotimes_{i=1}^n f_i^{(\varepsilon)}-
\bigotimes_{i=1}^n f_i\right\|_1
\le \sum_{i=1}^n\|f_i^{(\varepsilon)}-f_i\|_1\to0.
\]

Hence their pushforwards by the fixed measurable map `x -> x^T A x` converge in total variation.
In particular, for every Borel set `B`,

\[
\Pr(Q_\varepsilon\in B)\to\Pr(Q\in B).
\]

This will let us prove the interval inequality for smooth padded laws and pass it to the original rough
product law with no loss in the constant.

## 4. Smooth ruled formula with the trace issue removed

Write `R=[r_1 r_2 r_3]` and

\[
Y_\varepsilon=R^T X^{(\varepsilon)}.
\]

Since `R^T G` is a standard three-dimensional Gaussian,

\[
Y_\varepsilon=R^T X+\varepsilon Z_3
\]

has a `C^infinity` density `rho_epsilon` on `R^3`.

Put

\[
D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu),
\qquad Z_\varepsilon=DY_\varepsilon.
\]

Then

\[
Q_\varepsilon=Z_{\varepsilon,1}^2+Z_{\varepsilon,2}^2-Z_{\varepsilon,3}^2.
\]

For `s>0`, let

\[
e_\theta=(\cos\theta,\sin\theta,0),
\qquad e_\theta^\perp=(-\sin\theta,\cos\theta,0),
\qquad d_\theta=e_\theta^\perp+e_3,
\]

and define

\[
F(s,\theta,t)=\sqrt{s}\,e_\theta+t d_\theta.
\]

Then `q(F)=s` for `q(z)=z_1^2+z_2^2-z_3^2`. The map

\[
(0,\infty)\times[0,2\pi)\times\mathbb R\to\{z:q(z)>0\}
\]

is one-to-one modulo the harmless angular endpoint identification. Indeed, for `z` with `q(z)=s>0`,
`t=z_3` and the planar part is uniquely represented as

\[
(z_1,z_2)=\sqrt{s}\,e_\theta+t e_\theta^\perp.
\]

The Jacobian is exactly

\[
\left|\det\left(\partial_sF,\partial_\theta F,\partial_tF\right)\right|=\frac12.
\]

Therefore for every interval `I subset (0,infinity)`, ordinary change of variables gives

\[
\Pr(Q_\varepsilon\in I)
=\frac1{2\det D}
\int_I\int_0^{2\pi}\int_{\mathbb R}
\rho_\varepsilon\!\left(D^{-1}F(s,\theta,t)\right)
\,dt\,d\theta\,ds.
\]

This is a genuine three-dimensional integral identity. No pointwise trace of a merely `L^infinity`
representative has been used.

## 5. Exact use of the two-dimensional product-projection theorem

For fixed `theta`, define

\[
v_\theta=D^{-1}d_\theta
=\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
\frac{\cos\theta}{\sqrt{\lambda_2}},
\frac1{\sqrt\mu}\right).
\]

Choose an orthonormal basis `E_theta` of `v_theta^perp` in `R^3`. Then

\[
U_\theta=E_\theta^T Y_\varepsilon=(R E_\theta)^T X^{(\varepsilon)}.
\]

The two columns of `R E_theta` are orthonormal in `R^n`. The sharp
Livshyts-Paouris-Pivovarov product-marginal theorem therefore gives

\[
\|p_{U_\theta}\|_\infty\le2.
\]

Here there is no rough trace ambiguity: because of the independent Gaussian padding, `U_theta` is a
convolution with a nondegenerate two-dimensional Gaussian, so its density is continuous. The a.e.
projection bound is therefore a pointwise bound.

For

\[
y_0=D^{-1}(\sqrt{s}\,e_\theta),
\]

the fibre of the orthogonal projection onto `v_theta^perp` through `y_0` is the line
`y_0+R v_theta`. Hence

\[
\int_{\mathbb R}\rho_\varepsilon(y_0+t v_\theta)\,dt
=\frac1{|v_\theta|}
 p_{U_\theta}(E_\theta^T y_0)
\le \frac2{|v_\theta|}.
\]

Substitution into the ruled formula yields

\[
\Pr(Q_\varepsilon\in I)
\le
\frac{|I|}{\det D}
\int_0^{2\pi}\frac{d\theta}{|v_\theta|}
=C_+(\lambda_1,\lambda_2,\mu)|I|.
\]

The coefficient is exactly

\[
\frac1{\det D\,|v_\theta|}
=\frac1{\sqrt{
\lambda_2\mu\sin^2\theta+
\lambda_1\mu\cos^2\theta+
\lambda_1\lambda_2}}.
\]

Since all three parameters are at least one,

\[
\lambda_2\mu\sin^2\theta+\lambda_1\mu\cos^2\theta\ge1,
\qquad \lambda_1\lambda_2\ge1.
\]

Thus pointwise

\[
\frac1{\det D\,|v_\theta|}\le\frac1{\sqrt2},
\]

and therefore

\[
C_+\le\frac{2\pi}{\sqrt2}=\pi\sqrt2.
\]

This verifies both the Jacobian and the constant in the ruled theorem.

## 6. Passage back to arbitrary measurable cap-one marginals

The estimate above is uniform in `epsilon`:

\[
\Pr(Q_\varepsilon\in I)\le\pi\sqrt2\,|I|
\qquad(I\subset(0,\infty)).
\]

Total-variation convergence of the output laws gives

\[
\Pr(Q\in I)\le\pi\sqrt2\,|I|.
\]

There is no atom at zero: `Q(x)` is a nonzero polynomial and the full product law of `X` is absolutely
continuous with respect to `n`-dimensional Lebesgue measure, while the zero set of a nonzero polynomial
has Lebesgue measure zero. Hence the same interval inequality extends to intervals touching zero.

By the standard interval domination criterion, the positive-side submeasure `mu_+` is absolutely
continuous with density bounded essentially by `pi sqrt(2)`.

This is the precise rough-input conclusion. The original densities `f_i` need not be continuous,
compactly supported, log-concave, connected, centered, or identical.

## 7. Required application of completed partner account04/B15

Completed partner source:

- repository/commit: `yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260922T211430Z-account04-B15-heat-regularity-r4/REPORT.md`.

Its exact Gaussian heat-height theorem says, for every probability law `nu`,

\[
\sup_{\eta>0,y}(\nu*\gamma_\eta)(y)=\|p_\nu\|_\infty,
\]

with `+infinity` if no bounded density exists. By normalization and linearity, the identical formula holds
for finite positive subprobability measures.

Apply it to the just-proved positive-side measure `mu_+`. We obtain the actual inequality

\[
\boxed{
\sup_{\eta>0,y}
\int_{[0,\infty)}\gamma_\eta(s-y)\,d\mu_Q(s)
=\left\|\frac{d\mu_+}{ds}\right\|_\infty
\le C_+
\le\pi\sqrt2.
}
\]

Thus for every heat scale and center,

\[
(\mu_Q*\gamma_\eta)(y)
\le \pi\sqrt2
+\int_{(-\infty,0)}\gamma_\eta(s-y)\,d\mu_Q(s).
\]

So, in the exact-rank-three `(+,+,-)` case, the **entire one-sheet contribution is uniformly paid** in
the partner's positive heat formulation. Any remaining heat-height obstruction is confined to the
minority-sign/two-sheet submeasure. This is a concrete reduction, not a renamed density bound.

## 8. What is and is not closed

Closed in this run:

- the newest ruled-hyperboloid theorem's rough-input limiting step;
- the trace-on-a-curve issue noted by the live continuation;
- the exact constant and Jacobian check;
- an interval formulation valid for arbitrary measurable cap-one marginals;
- the corresponding all-scale positive heat bound via account04/B15.

Not closed:

- the two-sheet side `s<0` for signature `(+,+,-)`;
- definite exact-rank-three forms by this mechanism;
- higher-rank matrices with additional eigenvalues/couplings;
- the full matrix- and dimension-independent universal density constant;
- a continuous representative derived **from this theorem alone** for rough inputs.

The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is respected: bounded line/X-ray marginals alone do
not control the two-sheet side. The new theorem uses the special straight-line ruling that exists only on
the one-sheet side and therefore does not contradict that correction.

## 9. First unpaid implication

For exact rank three with signature `(+,+,-)`, prove a product-preserving bound on the two-sheet submeasure,
preferably directly in interval or positive-heat form, without replacing product provenance by an
arbitrary joint three-dimensional density. In the full matrix problem, a further structural reduction is
still needed to expose a uniformly controlled exact-rank-three or other already-paid component without
paying a reciprocal tiny physical minor.

This run changed mechanism from the previous tent-kernel averaging attack to ruled-level geometry plus
class-preserving Gaussian padding, as required after repeated regularization work.

## 10. Source pins

- Control source at run start: `yspennstate/math-research-brain@0978e6fe90234d8b545ec790fef99764d301dce4`.
- Pre-publication refreshed control observed: `yspennstate/math-research-brain@299087a96cac1db6a92973fe418e273a5e7d230e`, OWNER CONTROL revision `2026-09-22.15`.
- Newest Claude continuation: `scheduled_tasks/work/shared/qform-density-2026-09-22/requests/QFORM-CLAUDE-LATEST-20260922T225732Z.md`.
- Ruled source checked at the current math-open-problems master as well as source commit `e5f71d79eff325201dd0274053d20268ce65b837`; its file blob remained `d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc` at the pre-publication check.
- Product-marginal theorem transfer checked in account03/B18's literature report and the Claude source: every two-dimensional orthogonal projection of a cap-one product law has density at most `2`.
- Partner account04/B15 heat theorem: `ad7e5daa036cc8330b1432285ad40fec611d37dd`.

No refuted pointwise quadratic-phase decay, arbitrary-joint coarea bound, spectral-coordinate independence,
conditional density-cap moment, worst fibre-supremum, or universal single-minor assertion is used.
