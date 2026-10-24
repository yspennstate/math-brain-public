Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic correction — the W_{3/2} constant and a valid finite-third-moment high-mean terminal theorem

**Status:** PROVED PARTIAL + IMMUTABLE CORRECTION. The all-mean finite-third-moment theorem asserted in `2026-09-20T0800Z__third-moment-terminal-monotonicity.md` is **NOT ESTABLISHED** by that report. The exact defect is identified below. A corrected finite-third-moment theorem is proved under an explicit mean condition, and a sharper law-specific criterion is isolated. The full Lyons–Pemantle–Peres conjecture remains unresolved.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`. Old D0047 history and peer files are untouched.

**Captured master immediately before this correction:** `677a112c02ccfaa672c6342ecdc15864eb3a291f`.

**Correction target:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0800Z__third-moment-terminal-monotonicity.md`, creation commit `f7ecfbfc6a8201beb354b60c2f0046fe6683185d`, read-back blob `8e3899a46b8ed33cb5058f5791217c6640ed7387`.

The fixed full-source metric remains

`R_full: 1 -> 1`.

## 1. Exact defect in the preceding report

The preceding report set `p=3/2` and, after coupling iid centered child differences `D_i`, used

\[
E\left|\sum_{i=1}^{\nu}D_i\right|^p
\le E\nu\,E|D_1|^p.
\tag{1.1 -- INVALID AS STATED}
\]

For general independent centered variables and `1<p<2`, the von Bahr--Esseen inequality carries a constant. One may use the classical bound

\[
E\left|\sum_{i=1}^{n}D_i\right|^p
\le c_{p,n}\sum_{i=1}^n E|D_i|^p,
\qquad c_{p,n}\le 2-\frac1n.
\tag{1.2}
\]

The constant cannot simply be replaced by one for arbitrary nonsymmetric centered child differences. Thus the claimed contraction factor `m^{-1/3}` in the 0800Z report was unjustified, and so was the resulting theorem for every `m>1`.

Everything in that report after the contraction lemma is conditional on having a strict `W_{3/2}` contraction. The exact branch-addition identity and the cubic-moment bookkeeping remain useful, but the unrestricted contraction claim must not be cited as proved.

## 2. Corrected W_{3/2} contraction coefficient

Retain the normalized variables

\[
\delta=m-\lambda,
\qquad e_\delta=EB_{m-\delta},
\qquad r_\delta=e_\delta/\delta,
\qquad X_\delta=B_{m-\delta}/e_\delta,
\]

and

\[
X_\delta\stackrel d=
\frac{Y_\delta}{m-\delta+\delta r_\delta Y_\delta},
\qquad
Y_\delta=\sum_{i=1}^{\nu}X_{\delta,i}.
\tag{2.1}
\]

Assume `E nu^3<infinity`. As in the 0800Z report, the normalized third moments are uniformly bounded near `delta=0`, and `r_delta` stays bounded above and away from zero.

Let `p=3/2`, optimally couple `X_delta,X_eta`, and put

\[
w=W_p(\mathcal L(X_\delta),\mathcal L(X_\eta)).
\]

Conditional on `nu=n`, the child differences are iid, centered, and have p-th moment `w^p`. Applying (1.2), then averaging over `nu>=1`, gives

\[
\begin{aligned}
E|Y_\delta-Y_\eta|^p
&\le E\bigl[c_{p,\nu}\nu\bigr]w^p\\
&\le E(2\nu-1)w^p\\
&=(2m-1)w^p.
\end{aligned}
\tag{2.2}
\]

Hence

\[
\boxed{
\|Y_\delta-Y_\eta\|_{3/2}
\le (2m-1)^{2/3}w.}
\tag{2.3}
\]

Since the derivative of the normalized escape map with respect to its input is at most `1/(m-delta)`, the law-change coefficient tends at criticality to

\[
\boxed{
q_0(m):=\frac{(2m-1)^{2/3}}{m}.}
\tag{2.4}
\]

This is strictly below one exactly when

\[
(2m-1)^2<m^3.
\]

For `m>1`,

\[
m^3-(2m-1)^2=(m-1)(m^2-3m+1),
\]
so the clean sufficient range is

\[
\boxed{
m>m_\star:=\frac{3+\sqrt5}{2}\approx2.61803398875.}
\tag{2.5}
\]

For every fixed law satisfying (2.5), choose `delta_*` small enough that

\[
q:=\frac{(2m-1)^{2/3}}{m-\delta_*}<1.
\tag{2.6}
\]

The rest of the coupled fixed-point estimate from the 0800Z report is then valid: the parameter derivatives are controlled in `L^{3/2}` by the uniform third moment, while the exact scalar identity

\[
r_\delta^{-1}
=E\frac{Y_\delta^2}{m-\delta+\delta r_\delta Y_\delta}
\tag{2.7}
\]

has a law derivative of only linear growth in `Y`. Consequently

\[
\boxed{
W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta))
+|r_\delta-r_\eta|
\le C|\delta-\eta|}
\tag{2.8}
\]

for `0<delta,eta<=delta_*` whenever (2.5) holds.

### Sharper law-specific criterion

The bound `2m-1` in (2.2) is only a universal simplification. If a valid von Bahr--Esseen constant `c_{3/2,n}` is retained degree by degree, the same proof works whenever

\[
\boxed{
\kappa_{3/2}:=
\frac{\left(E[c_{3/2,\nu}\nu]\right)^{2/3}}{m}<1.}
\tag{2.9}
\]

Thus (2.5) is sufficient, not asserted optimal.

## 3. Exact effective-degree identity remains valid

The exact algebra from the 0800Z report does not use the false constant. Let

\[
a=m-1,
\qquad
D_{n,\delta}=a-\delta+e_\delta\sum_{i=0}^n X_{\delta,i},
\]

\[
h_n(\delta)
=E\left[\frac{X_{\delta,0}}{D_{n,\delta}}\right].
\]

Adding one branch gives

\[
\boxed{
h_n-h_{n+1}=e_\delta g_n,}
\tag{3.1}
\]

with

\[
g_n=E\left[
\frac{X_{\delta,0}X_{\delta,n+1}}
{D_{n,\delta}D_{n+1,\delta}}
\right].
\tag{3.2}
\]

If `nu'` is an iid copy of `nu`, define

\[
\bar h_\delta=E[h_\nu],
\]

\[
K_\delta=
\frac12E\left[
|\nu-\nu'|
\sum_{j=\min(\nu,\nu')}^{\max(\nu,\nu')-1}g_j
\right].
\tag{3.3}
\]

The pairwise covariance identity gives exactly

\[
\boxed{
M(m-\delta)
=m-e_\delta\frac{K_\delta}{\bar h_\delta}.}
\tag{3.4}
\]

At criticality,

\[
\bar h_0=\frac1{m-1},
\qquad
g_j(0)=\frac1{(m-1)^2},
\qquad
K_0=\frac{\operatorname{Var}(\nu)}{(m-1)^2}.
\tag{3.5}
\]

Under `E nu^3<infinity`, (2.8) implies the same Lipschitz estimates

\[
|\bar h_\delta-\bar h_\eta|
+|K_\delta-K_\eta|
\le C|\delta-\eta|.
\tag{3.6}
\]

The cubic moment is enough because the degreewise difference obeys

\[
|g_j(\delta)-g_j(\eta)|\le C(1+j)|\delta-\eta|
\]

and

\[
|n-k|\sum_{j=\min(n,k)}^{\max(n,k)-1}(1+j)
\le C(1+n^3+k^3).
\tag{3.7}
\]

## 4. Corrected theorem

The earlier critical-edge calculation gives

\[
r_\delta\to\frac{m-1}{f_2},
\qquad f_2=E[\nu(\nu-1)].
\tag{4.1}
\]

Combining (3.4)--(3.6) with (4.1) yields

\[
M(m-\delta)
=m-rac{\operatorname{Var}(\nu)}{f_2}\delta
+O_{\rm Lip}(\delta^2).
\tag{4.2}
\]

Aidekon's exact speed formula

\[
\ell_\lambda=\frac{M(\lambda)-\lambda}{M(\lambda)+\lambda}
\tag{4.3}
\]

and `f_2-Var(nu)=m(m-1)` therefore give

\[
\boxed{
\ell_{m-\delta}
=\frac{m-1}{2f_2}\delta
+O_{\rm Lip}(\delta^2).}
\tag{4.4}
\]

The pairwise remainder implies a strictly positive slope in `delta` for all sufficiently small `delta`. Hence:

### Theorem 4.1 — valid finite-third-moment terminal theorem in the high-mean range

Assume

\[
P(\nu=0)=0,
\qquad m=E\nu>\frac{3+\sqrt5}{2},
\qquad E\nu^3<\infty.
\tag{4.5}
\]

Then there exists a law-dependent `epsilon>0` such that

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }
(m-\epsilon,m).}
\tag{4.6}
\]

More generally, the same conclusion follows from the law-specific strict-contraction criterion (2.9).

This remains only a terminal-interval theorem and does not solve the full conjecture.

## 5. A heavy-tail example not covered by exponential-moment arguments or the prior E nu^4 report

Let `N` have

\[
P(N=n)=\frac{n^{-9/2}}{\zeta(9/2)},\qquad n\ge1,
\]

and put

\[
\nu=N+2.
\tag{5.1}
\]

Then `P(nu=0)=0`, there is no positive exponential moment, and

\[
E\nu
=2+\frac{\zeta(7/2)}{\zeta(9/2)}
\approx3.0682903609
>\frac{3+\sqrt5}{2}.
\]

Moreover

\[
E\nu^3<\infty,
\qquad E\nu^4=\infty.
\]

Therefore Theorem 4.1 applies, whereas the preceding P03-A `E nu^4` terminal proof and the exponential-moment hypothesis in the classical Einstein-relation paper do not apply directly. For this law,

\[
f_2\approx6.4767756094,
\qquad
\frac{m-1}{2f_2}\approx0.1596697559.
\]

No explicit terminal width is claimed.

## 6. Exact remaining obstruction and next attack

The corrected proof shows precisely why the naive `W_{3/2}` route does not yet cover means close to one: the available centered-sum inequality introduces a constant that destroys the strict contraction. This is a mathematical obstruction of the chosen metric estimate, not evidence that monotonicity fails.

The most promising next analytic attack is to replace `W_{3/2}` by an **ideal Zolotarev metric of order 3/2**. Such metrics have the exact independent-sum and scaling properties needed for the critical branching smoothing map, whose formal contraction factor is `m^{1-3/2}=m^{-1/2}<1` for every `m>1`, without the von Bahr--Esseen constant. The remaining work is to control the nonlinear perturbation

\[
y\mapsto\frac{y}{m-\delta+\delta r y}
\]

in that ideal metric strongly enough to recover the Lipschitz estimates for `r_delta`, `K_delta`, and the speed remainder. If that succeeds, the finite-third-moment theorem should extend to all `m>1`; until then, the all-mean claim is withdrawn.

## 7. Honest ledger

* `R_full: 1 -> 1`.
* 0800Z all-mean `E nu^3` theorem: **WITHDRAWN / NOT PROVED** due to missing von Bahr--Esseen constant.
* Exact branch-addition identity and cubic bookkeeping from 0800Z: **VALID and reused**.
* New corrected result: **PROVED PARTIAL**, finite third moment plus `m>(3+sqrt5)/2`, or the sharper law-specific criterion (2.9), implies a terminal monotonicity interval.
* Next attack: Zolotarev-ideal contraction to remove the high-mean restriction.
