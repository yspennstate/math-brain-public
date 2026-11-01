SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B17, 2026-09-24T04:45:51.001591Z.
attacking: robustness and near-sharpness of the dense-bank 3 sqrt(2) witness under almost-sure remote fragmentation, with a maximal admissible satellite-gap scaling law.

# QFORM-NEARROOTM-SATELLITE-SHARP-WITNESS-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet02/B17`  
Run: `20260924T044551Z-fleet02-B17-QFORM-auto11`  
Status: **PROVED SUPPORTING SHARP-WITNESS THEOREM / FULL TARGET OPEN**

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a source-valid lower-bound obstruction for the universal constant. It strengthens the latest designated-partner `fleet03/B17` almost-sure-satellite construction: the remote support gap may grow as `sqrt(m)/L_m` for **any** auxiliary sequence `L_m -> infinity` with `L_m=o(sqrt(m))`, while the probability that at least one of the `3m` physical coordinates visits a satellite interval still tends to one and the cone-tip density still converges to the sharp known obstruction `3 sqrt(2)`.

Thus a proof cannot gain any strict improvement below `3 sqrt(2)` by assuming that sharp witnesses effectively live in one bounded component, by charging only the all-main product cell, or by discarding support pieces merely because their gap grows almost on the central-limit scale. This is a supporting witness theorem, not a QFORM counterexample.

No moment, bounded-support, log-concavity, connected-support, post-rotation independence, or Gaussian assumption is imposed on the finite inputs. The finite laws are explicit cap-one indicator densities. Continuity is not used as a full-target reduction.

## 1. Exact dense target matrices

Let

\[
n={1\over\sqrt{14}}(1,2,3)^T,
\qquad
\alpha_m=2+{1\over m},
\qquad
B_m=I_3-\alpha_m nn^T.
\]

Let `T_m` be the `3m x 3` synthesis matrix having, in bank `j`, `m` copies of `e_j/sqrt(m)`. Then

\[
T_m^TT_m=I_3,
\qquad
A_m=T_mB_mT_m^T.
\]

Because `nn^T` is the orthogonal projection onto `span(n)`,

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)
=\operatorname{spec}(B_m)
=\left\{1,1,-\left(1+{1\over m}\right)\right\}.}
\tag{1.1}
\]

Hence every finite matrix is an exact target instance. Moreover every entry of `B_m` is nonzero. Explicitly,

\[
(B_m)_{11}={12m-1\over14m}>0,
\quad
(B_m)_{22}={3m-2\over7m}>0,
\quad
(B_m)_{33}=-{4m+9\over14m}<0,
\]

and every off-diagonal entry is `-alpha_m n_i n_j != 0`. Therefore every physical entry of `A_m` is nonzero: the matrix is entrywise dense.

This exact matrix is the completed dense strict-slack family used in the latest compatible designated-partner theorem `fleet03/B17`, run `20260924T040702Z-fleet03-B17-QFORM-r11`, scientific commit `8eae5b3f9d8ebacc998d7091608a8308cdbe1cad`. The partner proved the same sharp limit for one particular pair of exponents. The new work below derives the full near-`sqrt(m)` gap envelope.

## 2. A one-parameter family with nearly root-m support gaps

Let `L_m` be **any** positive sequence satisfying

\[
\boxed{L_m\longrightarrow\infty,
\qquad {L_m\over\sqrt m}\longrightarrow0.}
\tag{2.1}
\]

Define

\[
\varepsilon_m={\sqrt{L_m}\over m},
\qquad
\ell_m=1-\varepsilon_m,
\qquad
R_m={\sqrt m\over L_m}.
\tag{2.2}
\]

For all sufficiently large `m`, put on every one of the `3m` original physical coordinates the probability density

\[
\boxed{
f_m(x)=
\mathbf 1_{[-\ell_m/2,\,\ell_m/2]}(x)
+\mathbf 1_{[R_m,\,R_m+\varepsilon_m]}(x).
}
\tag{2.3}
\]

The two interval lengths sum to one, so `0<=f_m<=1` and `int f_m=1` exactly.

The support gap obeys

\[
\operatorname{gap}(\operatorname{supp}f_m)
\ge R_m-{1\over2}
={\sqrt m\over L_m}-{1\over2}
\longrightarrow\infty.
\tag{2.4}
\]

Let `S_m` be the event that at least one of all `3m` coordinates lands in the satellite interval. Since a single coordinate lands there with probability `epsilon_m`,

\[
\mathbb P(S_m^c)
=(1-\varepsilon_m)^{3m}
=\exp\{-3\sqrt{L_m}+o(1)\},
\]

and hence

\[
\boxed{\mathbb P(S_m)\longrightarrow1.}
\tag{2.5}
\]

So the sharp limit below is **not** carried by a positive-probability all-main cell. Indeed the expected number of satellite coordinates is `3 sqrt(L_m) -> infinity`.

The scale (2.4) is close to the CLT scale in a strong sense: since `L_m` may diverge arbitrarily slowly, one may take, for example,

\[
R_m={\sqrt m\over\log\log m}
\]

(up to the harmless usual modification for small `m`).

## 3. Exact moment accounting

Let `X_m` have density (2.3). Its mean is

\[
\mu_m=R_m\varepsilon_m+{\varepsilon_m^2\over2}.
\]

Therefore the mean of the normalized bank sum has the exact scale

\[
\boxed{
\sqrt m\,\mu_m
={1\over\sqrt{L_m}}
+{L_m\over2m^{3/2}}
\longrightarrow0.}
\tag{3.1}
\]

The raw second moment is

\[
\mathbb E X_m^2
={\ell_m^3\over12}
+R_m^2\varepsilon_m
+R_m\varepsilon_m^2
+{\varepsilon_m^3\over3}.
\]

The leading satellite correction is exactly

\[
\boxed{\varepsilon_mR_m^2=L_m^{-3/2}\longrightarrow0.}
\tag{3.2}
\]

Consequently, with `sigma_m^2=Var(X_m)`,

\[
\boxed{\sigma_m^2\longrightarrow{1\over12}.}
\tag{3.3}
\]

For the local CLT the relevant Lyapunov quantity is even smaller. The satellite contribution to the third absolute moment, divided by `sqrt(m)`, satisfies

\[
{\varepsilon_m(R_m+1)^3\over\sqrt m}
=O\!\left(L_m^{-5/2}\right)+o(1),
\]

because the leading term is exactly

\[
\boxed{{\varepsilon_mR_m^3\over\sqrt m}=L_m^{-5/2}.}
\tag{3.4}
\]

Thus

\[
{\mathbb E|X_m-\mu_m|^3\over\sqrt m}\longrightarrow0.
\tag{3.5}
\]

Notice what (3.1)--(3.4) accomplish simultaneously: the product sample uses remote pieces with probability tending one, yet their aggregate contribution to the normalized bank mean, variance, and Lyapunov error vanishes.

## 4. Self-contained triangular local CLT for the two-interval laws

Let `X_{m,1},...,X_{m,m}` be iid with density `f_m`, and define one bank variable

\[
Y_m={1\over\sqrt m}\sum_{k=1}^mX_{m,k}.
\tag{4.1}
\]

Write `phi_m(s)=E exp(isX_m)`. The exact interval form gives

\[
\phi_m(s)
=\int_{-\ell_m/2}^{\ell_m/2}e^{isx}\,dx
+\int_{R_m}^{R_m+\varepsilon_m}e^{isx}\,dx.
\tag{4.2}
\]

The satellite location affects only a phase, not the elementary modulus bounds. In particular,

\[
|\phi_m(s)|
\le
\ell_m\left|\operatorname{sinc}{(s\ell_m/2)}\right|
+\min\{\varepsilon_m,2/|s|\}.
\tag{4.3}
\]

Choose a fixed small `delta>0`. Since `ell_m ->1`, the quadratic drop of `sinc` at the origin implies that for all sufficiently large `m`,

\[
|\phi_m(s)|\le1-cs^2,
\qquad |s|\le\delta,
\tag{4.4}
\]

for an absolute `c>0`. This estimate is important: it comes from the length-`1-o(1)` central interval and does **not** require a uniform third moment.

For every fixed `0<delta<K`, the densities `f_m` differ in `L^1` from `1_{[-1/2,1/2]}` by at most `2 epsilon_m`, while their central interval lengths tend to one. Hence

\[
\sup_{\delta\le|s|\le K}|\phi_m(s)|\le\rho_{\delta,K}<1
\tag{4.5}
\]

for all sufficiently large `m`.

For `|s|>=K`, (4.3) yields

\[
|\phi_m(s)|\le {2\over|s|}+\varepsilon_m.
\tag{4.6}
\]

Choose fixed `K` sufficiently large. On `K<=|s|<=4/epsilon_m`, the right side is at most a fixed number below one for large `m`. For `|s|>=4/epsilon_m`, bounding both interval integrals by `2/|s|` gives

\[
|\phi_m(s)|\le{4\over|s|}.
\tag{4.7}
\]

The characteristic function of `Y_m` is

\[
\Phi_m(t)=\phi_m(t/\sqrt m)^m.
\]

Equations (4.4)--(4.7) imply an integrable four-zone majorization:

* on `|t|<=delta sqrt(m)`, `|Phi_m(t)|<=exp(-c t^2)`;
* on `delta sqrt(m)<=|t|<=K sqrt(m)`, the integral is `O(sqrt(m) rho^m)`;
* on `K sqrt(m)<=|t|<=4 sqrt(m)/epsilon_m`, the integral is at most a polynomial factor times `q^m`, `q<1`;
* beyond `4 sqrt(m)/epsilon_m`,
  \[
  \int_{4\sqrt m/\varepsilon_m}^{\infty}
  \left({4\sqrt m\over t}\right)^m dt
  ={4\sqrt m\over m-1}\,\varepsilon_m^{m-1},
  \tag{4.8}
  \]
  and similarly on the negative side.

On each fixed compact `t`-set, (3.1), (3.3), and (3.5) give the standard triangular-array characteristic-function expansion

\[
\phi_m(t/\sqrt m)^m
\longrightarrow
\exp(-t^2/24).
\tag{4.9}
\]

Combining (4.4)--(4.9) gives `L^1(dt)` convergence of characteristic functions. Fourier inversion therefore yields the **uniform local CLT**

\[
\boxed{
\|g_m-\gamma_{1/12}\|_\infty\longrightarrow0,
\qquad
\gamma_{1/12}(y)=\sqrt{6/\pi}\,e^{-6y^2},
}
\tag{4.10}
\]

where `g_m` is the density of `Y_m`. In particular,

\[
\boxed{\sup_m\|g_m\|_\infty<\infty}
\tag{4.11}
\]

for all sufficiently large `m`.

This local CLT is proved for the actual disconnected cap-one laws (2.3); no finite input is replaced by a Gaussian.

## 5. Cone-tip density for the exact rotated matrix

The three physical banks are disjoint, so the three bank sums `Y_{m,1},Y_{m,2},Y_{m,3}` are genuinely independent copies of `Y_m`. No independence after diagonalizing `B_m` is asserted.

Write

\[
q_m(y)=y^TB_my,
\qquad
\beta_m=1+1/m,
\qquad
\alpha_m=1+\beta_m=2+1/m.
\]

Let `e_1,e_2` be an orthonormal basis of `n^perp` and

\[
v(\theta)=\cos\theta\,e_1+\sin\theta\,e_2.
\]

The two null circles on `S^2` are

\[
\omega_m^\pm(\theta)
=\pm{n\over\sqrt{\alpha_m}}
+\sqrt{\beta_m\over\alpha_m}\,v(\theta).
\tag{5.1}
\]

The latest designated-partner report proves the exact spherical coarea identity

\[
\boxed{
p_m(0)=
{1\over2\sqrt{\alpha_m}}
\sum_{\pm}\int_0^{2\pi}\int_0^\infty
\rho_m(r\omega_m^\pm(\theta))\,dr\,d\theta,
}
\tag{5.2}
\]

where

\[
\rho_m(y)=g_m(y_1)g_m(y_2)g_m(y_3).
\]

The passage from (4.10) to (5.2) is uniform in the radial tail. Indeed every unit vector `omega` has a coordinate `|omega_j|>=1/sqrt(3)`. Using (4.11),

\[
\int_M^\infty\rho_m(r\omega)dr
\le C^2\sqrt3\,
\mathbb P\{|Y_m|\ge M/\sqrt3\}.
\tag{5.3}
\]

By (3.1) and (3.3), `sup_m E Y_m^2<infinity`; Chebyshev makes the right side of (5.3) `O(M^{-2})` uniformly in `m,omega`.

Hence (4.10), (5.2), and (5.3) allow passage to the Gaussian comparator **on the same finite-m null cone**. Because the Gaussian density of covariance `(1/12)I_3` is radial, its cone-tip integral is explicit:

\[
{1\over2\sqrt{\alpha_m}}\cdot2\cdot2\pi
(2\pi v)^{-3/2}
\int_0^\infty e^{-r^2/(2v)}dr
={1\over2v\sqrt{\alpha_m}}
={6\over\sqrt{\alpha_m}},
\quad v={1\over12}.
\]

Therefore

\[
\boxed{
p_m(0)
={6\over\sqrt{2+1/m}}+o(1)
\longrightarrow3\sqrt2.}
\tag{5.4}
\]

Consequently every admissible universal QFORM constant satisfies

\[
\boxed{C_*\ge3\sqrt2.}
\tag{5.5}
\]

The novelty is the support geometry under which (5.4) is now witnessed: the all-main cell has probability tending zero, the expected number of remote visits diverges, and the satellite gap can be `sqrt(m)/L_m` with `L_m` arbitrarily slowly divergent.

## 6. Required pinned source applied to a real inequality

I read the pinned source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`, and also checked the later `master` revision of those files. The completed ruled-level-set **Theorem C** in `COUNTEREXAMPLE_SEARCH.md` applies directly to the actual `3m` independent physical coordinates here. The nonzero spectral magnitudes are

\[
\lambda_1=1,
\qquad
\lambda_2=1,
\qquad
\mu=1+1/m.
\]

Thus, for every `s>=0`,

\[
\begin{aligned}
p_m(s)
&\le
\mu^{-1/2}
\int_0^{2\pi}
{d\theta\over\sqrt{\sin^2\theta+\cos^2\theta+1/\mu}}\\
&=\boxed{{2\pi\over\sqrt{2+1/m}}}.
\end{aligned}
\tag{6.1}
\]

This is a real finite-stage one-sheet inequality for the fragmented witness, with no post-rotation independence assumption.

Comparing (5.4) with (6.1),

\[
\boxed{
{p_m(0)\over 2\pi/\sqrt{2+1/m}}
\longrightarrow{3\over\pi}
=0.9549296585\ldots .}
\tag{6.2}
\]

The proof of Theorem C obtains (6.1) by bounding each relevant two-dimensional product-measure marginal along a ruling by `2`. Before that last cap, its `(1,1,-1)` identity is

\[
p(0)={\pi\over\sqrt2}\operatorname{avg}_\theta\rho_\theta(0).
\]

Accordingly (5.4) forces the corresponding angular average in this asymptotically sharp product family to approach

\[
\boxed{{6\over\pi}=1.9098593171\ldots .}
\tag{6.3}
\]

Hence any proof mechanism that tries to improve Theorem C solely by replacing the generic marginal cap `2` with one smaller universal number cannot use a value below `6/pi`. The generic cap has only the relative slack

\[
1-{3\over\pi}=0.0450703414\ldots
\tag{6.4}
\]

against this witness. This is a quantitative obstruction to a proof constant/mechanism, not a counterexample to QFORM.

## 7. Relation to the latest designated-partner theorem

Latest compatible partner consumed:

`fleet03/B17`, run `20260924T040702Z-fleet03-B17-QFORM-r11`,
scientific commit `8eae5b3f9d8ebacc998d7091608a8308cdbe1cad`.

That report takes

\[
\varepsilon_m=m^{-3/4},
\qquad
R_m=m^{1/8},
\]

and proves almost-sure satellite use together with `p_m(0)->3 sqrt(2)`. The present theorem keeps the exact partner matrix and its valid spherical-coarea receiver, but replaces the special exponents by (2.1)--(2.3). The new Fourier split in Section 4 is what permits the larger support gap.

For example, choosing `L_m=log log m` gives

\[
\varepsilon_m={\sqrt{\log\log m}\over m},
\qquad
R_m={\sqrt m\over\log\log m},
\]

so the gap is `m^{1/2-o(1)}`, while

\[
\mathbb P(S_m^c)
=\exp\{-3\sqrt{\log\log m}+o(1)\}\to0,
\]

and still `p_m(0)->3 sqrt(2)`.

Thus the partner's phenomenon is not tied to the exponents `3/4` and `1/8`; it persists almost up to the root-`m` scale.

## 8. What this rules out, and what remains open

This theorem rules out a broad class of localization-based sharp-constant arguments. In particular, none of the following facts can by itself force a uniform improvement below `3 sqrt(2)`:

1. the physical input law has only two interval components;
2. the support gap tends to infinity;
3. the support gap is as large as `sqrt(m)/L_m` with `L_m` arbitrarily slowly divergent;
4. the all-main product cell has probability tending zero;
5. the expected number of satellite-coordinate visits tends to infinity;
6. the physical matrix is entrywise dense and has strict negative spectral slack.

The surviving full-target gap is not fixed-dimensional: the current later source has proved `n=3` and, more generally, every fixed dimension with dimension-dependent constants. The unrestricted universal problem remains the dimension-growing rough no-pivot/hub and related coupled configurations described in the current continuation. The present witness says that any universal proof in that regime must retain product aggregation across remote components; it cannot pay for sharpness by a bounded-diameter or positive-main-cell reduction.

A finite example with density above `3 sqrt(2)` would refute only the proposed **sharp constant**. A genuine counterexample to QFORM must make the essential density escape every finite universal bound. Nothing here does that.

## 9. Compact theorem statement

**Theorem.** Let `L_m -> infinity` and `L_m=o(sqrt(m))`. For each sufficiently large integer `m`, let `3m` independent physical coordinates have the cap-one density (2.3), and let `A_m=T_mB_mT_m^T` be the exact dense matrix of Section 1. Then

\[
\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\},
\]

\[
\operatorname{gap}(\operatorname{supp}f_m)
\ge\sqrt m/L_m-1/2\to\infty,
\]

\[
\mathbb P(\hbox{at least one satellite among the }3m\hbox{ inputs})\to1,
\]

and

\[
\boxed{
p_{X^TA_mX}(0)
={6\over\sqrt{2+1/m}}+o(1)
\to3\sqrt2.}
\]

On the majority-sign one-sheet side, the completed pinned Theorem C also gives

\[
\boxed{\sup_{s\ge0}p_{X^TA_mX}(s)
\le {2\pi\over\sqrt{2+1/m}}.}
\]

Therefore the ruled-marginal proof constant is asymptotically saturated to the fraction `3/pi`, while the sharp known QFORM lower obstruction survives near-root-`m` remote fragmentation with overwhelming satellite usage.
