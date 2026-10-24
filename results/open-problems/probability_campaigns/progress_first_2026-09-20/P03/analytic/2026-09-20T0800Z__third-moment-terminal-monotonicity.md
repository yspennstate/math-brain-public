Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — finite-third-moment terminal monotonicity via a W_{3/2} escape contraction

**Status:** PROVED PARTIAL / NEW REPOSITORY THEOREM CANDIDATE. Not independently audited. No claim of exhaustive external novelty. The full Lyons–Pemantle–Peres conjecture remains unresolved.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Old D0047 history is preserved. Canonical ownership was checked at assignment and is not reopened.

**Captured master before this write:** `fb3fcf58da39da755d2cffaff73ae5aa4e97169e`.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0705Z__terminal-critical-monotonicity-by-normalized-contraction.md` plus its immutable TeX erratum `2026-09-20T0712Z__terminal-critical-monotonicity-erratum.md`.

**Complementary P03-B checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0715Z__common-spine-occupation-debt.md`. Its new common-spine occupation lemma concerns the coupling route `beta d>1`; this report stays on the independent escape-recursion route at the recurrent edge.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The intermediate obligation **does move**: the previous P03-A terminal-interval theorem assumed `E nu^4 < infinity`. This report lowers that hypothesis to the strictly weaker `E nu^3 < infinity`, and gives a direct exact mechanism explaining why the third moment is enough.

## 1. Source convention and a literature correction that matters

Let `nu` be the offspring variable of a supercritical Galton-Watson tree without leaves:

\[
P(\nu=0)=0,\qquad m:=E\nu>1.
\]

Use the reciprocal parent-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+\nu(x)},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)}.
\tag{1.1}
\]

Thus `0<=lambda<m` is the transient interval and the LPP conjecture says that the speed `ell_lambda` is nonincreasing in `lambda`.

The checked broad low-bias theorem remains Song--Wang--Xiang, *J. Appl. Probab.* 62 (2025), 1044--1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, then

\[
\ell_\lambda\text{ is strictly decreasing for }
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime, and arXiv:2006.03433 proves analyticity in the ballistic regime; neither gives the missing global sign.

A correction to the framing in the preceding P03-A report is important. The 2025 Song--Wang--Xiang paper explicitly notes that the Ben Arous--Hu--Olla--Zeitouni Einstein relation already implies the LPP monotonicity problem in a neighborhood of `lambda=m` under that paper's integrability assumptions. The original Einstein-relation paper assumes an **exponential offspring moment**, namely `sum b^k p_k<infinity` for some `b>1`. Therefore the terminal neighborhood itself is not new. The meaningful advance pursued here is a substantially weaker tail hypothesis and a direct discrete-time speed argument.

A bounded 20 September 2026 search did not locate a checked terminal-neighborhood theorem under only a finite third offspring moment. That is negative evidence, not a novelty certificate.

## 2. Exact speed representation and normalized critical variables

Let `B_lambda` be the escape probability from a child-root to never hit its artificial parent. With iid copies `B_1,B_2,...`,

\[
B_\lambda\stackrel d=
\frac{S_\nu}{\lambda+S_\nu},
\qquad S_n:=\sum_{i=1}^n B_i.
\tag{2.1}
\]

Aidekon's exact speed representation can be written as follows. Let `B_0,B_1,...` be iid copies of `B_lambda`, independent of `nu`, and define

\[
c_n(\lambda):=
E\left[\frac{B_0}{\lambda-1+\sum_{i=0}^{n}B_i}\right],
\qquad
M(\lambda):=
\frac{E[\nu c_\nu(\lambda)]}{E[c_\nu(\lambda)]}.
\tag{2.2}
\]

Then

\[
\boxed{
\ell_\lambda=\frac{M(\lambda)-\lambda}{M(\lambda)+\lambda}.
}
\tag{2.3}
\]

Put

\[
\delta:=m-\lambda,\qquad
e_\delta:=E B_{m-\delta},\qquad
r_\delta:=\frac{e_\delta}{\delta},\qquad
X_\delta:=\frac{B_{m-\delta}}{e_\delta}.
\tag{2.4}
\]

Thus `E X_delta=1`. If

\[
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i},
\]

then exactly

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}
{m-\delta+\delta r_\delta Y_\delta}.
}
\tag{2.5}
\]

The earlier critical-edge report, under `E nu^3<infinity`, proved

\[
\boxed{
r_\delta\to r_0:=\frac{m-1}{f_2}},
\qquad
f_2:=E[\nu(\nu-1)].
\tag{2.6}
\]

The problem left by the previous run was to obtain enough **pairwise** regularity in `delta` to turn this first-order limit into monotonicity on a whole interval without the fourth moment.

## 3. Uniform third moments are enough

Assume from now on

\[
\boxed{E\nu^3<\infty.}
\tag{3.1}
\]

Choose `delta_0>0` so that `lambda_0=m-delta_0` satisfies

\[
\lambda_0^2>m,\qquad \lambda_0^3>m.
\tag{3.2}
\]

This is possible because `m>1`.

Since `B<=S_nu/lambda`, with `e=EB`,

\[
EB^2\le\frac{mEB^2+f_2e^2}{\lambda^2},
\tag{3.3}
\]

and

\[
EB^3\le
\frac{mEB^3+3f_2(EB^2)e+f_3e^3}{\lambda^3},
\qquad f_3:=E[(\nu)_3].
\tag{3.4}
\]

Therefore, uniformly for `0<delta<=delta_0`,

\[
\boxed{
\sup E X_\delta^2<\infty,
\qquad
\sup E X_\delta^3<\infty.
}
\tag{3.5}
\]

The same deterministic escape-scale bounds used in the preceding report require only the second moment:

\[
\frac{\lambda^2-m}{f_2\lambda}
\le r_\delta\le \frac1m
\tag{3.6}
\]

for `delta` sufficiently small. In particular `r_delta` is uniformly bounded above and away from zero.

## 4. The new contraction: use W_{3/2}, not W_2

The fourth moment in the preceding run entered only because it measured the normalized fixed point in `W_2`; the parameter derivative of (2.5) grows quadratically in `Y`, forcing an `L^4` bound. The natural replacement is

\[
p:=\frac32.
\]

At the critical fixed point, the branching smoothing map contracts `W_p` by

\[
m^{1/p-1}=m^{-1/3}<1.
\]

### Lemma 4.1 — finite-third-moment pairwise critical contraction

There exist `delta_*>0` and `C<infinity`, depending only on the offspring law, such that for all `0<eta,delta<=delta_*`,

\[
\boxed{
W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta))
+|r_\delta-r_\eta|
\le C|\delta-\eta|.
}
\tag{4.1}
\]

#### Proof

Write

\[
w:=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\quad h:=|\delta-\eta|,
\quad \bar\delta:=\max(\delta,\eta).
\]

Couple iid child pairs optimally and use the same offspring variable `nu`. Every child difference has mean zero because both normalized variables have mean one. Conditional on `nu`, the von Bahr--Esseen inequality for `1<=p<=2` gives

\[
E\left|\sum_{i=1}^{\nu}
(X_{\delta,i}-X_{\eta,i})\right|^{3/2}
\le
E\left[\nu\right]w^{3/2}.
\]

Hence

\[
\boxed{
\|Y_\delta-Y_\eta\|_{3/2}
\le m^{2/3}w.
}
\tag{4.2}
\]

For

\[
F_{\delta,r}(y):=
\frac{y}{m-\delta+\delta r y},
\]

we have

\[
|\partial_yF_{\delta,r}(y)|
\le\frac1{m-\delta},
\tag{4.3}
\]

and

\[
|\partial_\delta F_{\delta,r}(y)|
\le C(y+y^2),
\qquad
|\partial_rF_{\delta,r}(y)|
\le C\delta y^2.
\tag{4.4}
\]

Because `2p=3`, the uniform third-moment bound (3.5) makes the right-hand side of (4.4) uniformly `L^{3/2}`. Thus, after choosing `delta_*` small enough that

\[
q:=\frac{m^{2/3}}{m-\delta_*}<1,
\tag{4.5}
\]

comparison of the two fixed-point equations gives

\[
\boxed{
w\le q w+Ch+C\bar\delta|r_\delta-r_\eta|.}
\tag{4.6}
\]

To control `r`, use the exact scalar identity inherited from the previous report. If

\[
D_{\delta,r}(y):=m-\delta+\delta r y,
\]

then taking means in (2.5) gives

\[
\boxed{
r_\delta^{-1}
=E\frac{Y_\delta^2}{D_{\delta,r_\delta}(Y_\delta)}.}
\tag{4.7}
\]

The derivative of

\[
\psi_{\delta,r}(y):=\frac{y^2}{D_{\delta,r}(y)}
\]

with respect to `y` obeys the useful **linear-growth** bound

\[
|\partial_y\psi_{\delta,r}(y)|
=\frac{y[2(m-\delta)+\delta r y]}
{(m-\delta+\delta r y)^2}
\le Cy.
\tag{4.8}
\]

Therefore the law-change term is controlled by Holder with conjugate exponents `3/2` and `3`:

\[
E[(Y_\delta+Y_\eta)|Y_\delta-Y_\eta|]
\le
C\|Y_\delta-Y_\eta\|_{3/2}.
\tag{4.9}
\]

The parameter derivatives of `psi` are bounded in expectation by constants times `E(Y^2+Y^3)`, again finite by (3.5) and `E nu^3<infinity`. Since `r_delta` stays bounded above and away from zero, (4.7) consequently yields

\[
|r_\delta-r_\eta|
\le Cw+Ch+C\bar\delta|r_\delta-r_\eta|.
\tag{4.10}
\]

Shrink `delta_*` to absorb the last term, substitute into (4.6), and shrink once more so the final coefficient of `w` is below one. This proves (4.1). QED.

### Why `3/2` is the natural exponent for this route

Two demands have to be met simultaneously:

1. the parameter derivative of `F` contains `Y^2`, so `W_p` requires a `2p` moment;
2. the scalar identity (4.7) has a `y`-derivative of order `y`, so Holder pairs `W_p` with the conjugate moment `p/(p-1)`.

The minimum of

\[
\max\left\{2p,\frac{p}{p-1}\right\},\qquad 1<p\le2,
\]

occurs at `p=3/2` and equals `3`. Thus the third moment is not an arbitrary cosmetic weakening; it is the exact balance point of this contraction argument.

## 5. Exact branch-addition identity for the effective-degree tilt

The previous fourth-moment proof obtained a second-order Taylor expansion degree by degree. Under only a third moment, that is unnecessarily expensive. An exact adjacent-degree identity avoids differentiating cubic remainders.

Put

\[
a:=m-1,
\qquad
T_{n+1,\delta}:=\sum_{i=0}^{n}X_{\delta,i},
\qquad
D_{n,\delta}:=a-\delta+e_\delta T_{n+1,\delta}.
\]

Define

\[
h_n(\delta):=\frac{c_n(m-\delta)}{e_\delta}
=E\left[\frac{X_{\delta,0}}{D_{n,\delta}}\right].
\tag{5.1}
\]

Adding one independent branch gives exactly

\[
\boxed{
h_n(\delta)-h_{n+1}(\delta)
=e_\delta g_n(\delta),}
\tag{5.2}
\]

where

\[
\boxed{
g_n(\delta):=
E\left[
\frac{X_{\delta,0}X_{\delta,n+1}}
{D_{n,\delta}D_{n+1,\delta}}
\right]>0.}
\tag{5.3}
\]

This is just `1/D_n-1/D_{n+1}=e X_{n+1}/(D_nD_{n+1})`; no approximation is involved.

Let `nu'` be an independent copy of `nu` and define

\[
\bar h_\delta:=E[h_\nu(\delta)],
\tag{5.4}
\]

\[
K_\delta:=
\frac12 E\left[
|\nu-\nu'|
\sum_{j=\min(\nu,\nu')}^{\max(\nu,\nu')-1}
 g_j(\delta)
\right].
\tag{5.5}
\]

The pairwise covariance identity and (5.2) give the exact formula

\[
\boxed{
M(m-\delta)=m-e_\delta\frac{K_\delta}{\bar h_\delta}.}
\tag{5.6}
\]

Indeed

\[
\operatorname{Cov}(\nu,h_\nu)
=\frac12E[(\nu-\nu')(h_\nu-h_{\nu'})]
=-e_\delta K_\delta,
\]

and `M-m=Cov(nu,h_nu)/E h_nu`.

At `delta=0`, every denominator equals `a`, so

\[
\bar h_0=\frac1a,
\qquad
g_j(0)=\frac1{a^2},
\qquad
K_0=\frac{\operatorname{Var}(\nu)}{a^2}.
\tag{5.7}
\]

## 6. Third moments also make the exact tilt Lipschitz

### Lemma 6.1

For sufficiently small `delta,eta`,

\[
\boxed{
|\bar h_\delta-\bar h_\eta|
+|K_\delta-K_\eta|
\le C|\delta-\eta|.}
\tag{6.1}
\]

#### Proof

All denominators in Section 5 are at least `a/2` after shrinking the terminal interval.

For `h_n`, changing the parameters costs expectations of at most

\[
C X_0(1+T_{n+1}),
\]

while changing the normalized child law costs a first-order term plus `delta` times sums of terms `X_0|Delta X_i|`. Using (4.1), Holder `(3/2,3)`, independence across distinct child indices, and the uniform third moments gives after averaging over `nu`

\[
|\bar h_\delta-\bar h_\eta|\le Ch.
\tag{6.2}
\]

For `g_j`, parameter differentiation of (5.3) costs at most

\[
C X_0X_{j+1}(1+T_{j+2}),
\]

whose expectation is `O(1+j)` using only second moments. For the law change, decompose the change in the numerator and each denominator. The numerator terms are controlled by independence and `W_{3/2}`. The denominator term contains

\[
\delta X_0X_{j+1}|\Delta T|.
\]

If the changed summand is neither index `0` nor `j+1`, independence gives a factor `E|Delta X|`; for the two exceptional indices, Holder `(3/2,3)` uses the third moment. Consequently

\[
\boxed{
|g_j(\delta)-g_j(\eta)|
\le C(1+j)h.}
\tag{6.3}
\]

Insert (6.3) into (5.5). Since

\[
|n-k|\sum_{j=\min(n,k)}^{\max(n,k)-1}(1+j)
\le C(1+n^3+k^3),
\tag{6.4}
\]

`E nu^3<infinity` is exactly enough to average the bound. This proves the `K` estimate and hence (6.1). QED.

## 7. Terminal monotonicity under only E nu^3 < infinity

From (4.1), (5.6), and (6.1), the function

\[
H_\delta:=r_\delta\frac{K_\delta}{\bar h_\delta}
\]

is Lipschitz at zero. By (2.6) and (5.7),

\[
H_0
=\frac{m-1}{f_2}
\frac{\operatorname{Var}(\nu)/a^2}{1/a}
=\frac{\operatorname{Var}(\nu)}{f_2}.
\tag{7.1}
\]

Equation (5.6) therefore becomes the pairwise second-order expansion

\[
\boxed{
M(m-\delta)
=m-rac{\operatorname{Var}(\nu)}{f_2}\,\delta
+O_{\rm Lip}(\delta^2),}
\tag{7.2}
\]

where

\[
R=O_{\rm Lip}(\delta^2)
\quad\Longleftrightarrow\quad
|R(\delta)-R(\eta)|
\le C\max(\delta,\eta)|\delta-\eta|.
\tag{7.3}
\]

To verify (7.2) directly, write `M=m-delta H_delta`; since `H` is Lipschitz and `H_delta-H_0=O(delta)`, the remainder `-delta(H_delta-H_0)` has exactly the increment bound (7.3).

Now use (2.3). Since

\[
f_2-\operatorname{Var}(\nu)=m(m-1),
\tag{7.4}
\]

smooth expansion of the rational map gives

\[
\boxed{
\ell_{m-\delta}
=\frac{m-1}{2f_2}\,\delta
+O_{\rm Lip}(\delta^2).}
\tag{7.5}
\]

Set

\[
A:=\frac{m-1}{2f_2}>0.
\]

For `0<=eta<delta<=delta_1`, (7.5) gives

\[
\ell_{m-\delta}-\ell_{m-\eta}
\ge
[A-C\delta_1](\delta-\eta).
\]

Choose `delta_1>0` so small that `C delta_1<A/2`. Then

\[
\boxed{
\ell_{m-\delta}>\ell_{m-\eta}
\qquad(0\le\eta<\delta\le\delta_1).}
\tag{7.6}
\]

Equivalently:

### Theorem 7.1 — finite-third-moment terminal LPP monotonicity

If

\[
P(\nu=0)=0,\qquad E\nu=m>1,\qquad E\nu^3<\infty,
\]

then there exists a law-dependent `epsilon>0` such that

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }
(m-\epsilon,m).}
\tag{7.7}
\]

Moreover the terminal speed has the quantitative pairwise expansion (7.5).

This strictly improves the previous P03-A theorem's fourth-moment hypothesis. It also reaches offspring laws outside the exponential-moment assumption used in the 2013 Einstein-relation paper.

## 8. A concrete heavy-tail family newly covered by this proof route

For example let

\[
P(\nu=n)=\frac{n^{-9/2}}{\zeta(9/2)},
\qquad n=1,2,3,\ldots.
\tag{8.1}
\]

Then

\[
P(\nu=0)=0,
\qquad
m=\frac{\zeta(7/2)}{\zeta(9/2)}>1,
\]

\[
E\nu^3=\frac{\zeta(3/2)}{\zeta(9/2)}<\infty,
\qquad
E\nu^4=\infty,
\]

and there is no finite exponential moment. Thus the preceding fourth-moment terminal theorem and the 2013 exponential-moment Einstein-relation hypothesis do not apply directly, while Theorem 7.1 does.

Numerically,

\[
m\approx1.0682903609,
\]

and the critical linear coefficient in (7.5) is approximately `0.1676955`. No explicit width `epsilon` is claimed in this run.

## 9. What failed, what changed, and the exact remaining gap

### Failed / superseded route

Trying to repeat the `W_2` proof with only a third moment fails at the correct place: the `L^2` norm of the parameter derivative contains `Y^2`, hence needs `E Y^4`. Merely truncating that term would lose the pairwise `O_Lip(delta^2)` control needed for monotonicity.

The successful pivot was twofold:

1. change the contraction space from `W_2` to `W_{3/2}` so the quadratic parameter derivative needs only a third moment;
2. replace degreewise second-order Taylor remainders by the exact branch-addition identity (5.2), so the effective-degree tilt only requires a cubic offspring average.

### Exact remaining gap

This is still not the full LPP conjecture. The source metric remains `R_full=1`. The open analytic obligations are now:

* lower the terminal tail assumption below the third moment, or identify a genuine obstruction;
* make the terminal width quantitative for concrete laws, especially `{1,2}` mixtures;
* join the terminal interval to the low/intermediate intervals already proved for restricted families;
* ultimately control the central bias gap for general no-leaf laws, where neither the minimum-degree low-bias argument nor the critical smoothing contraction is by itself sufficient.

The present `W_p`/Holder scheme has a structural third-moment barrier because `max{2p,p/(p-1)}` is minimized at `3`; beating it requires a different estimate, not a different choice of `p`.

## 10. Next analytic attack

The next useful target is **quantitative width for the `{1,2}` family**, beginning with `P(nu=1)=P(nu=2)=1/2`. The normalized recursion has bounded offspring and the constants in Sections 3--6 can then be made explicit. The goal is an explicit `epsilon` in

\[
\ell_\lambda\downarrow
\quad\text{on}\quad
(3/2-\epsilon,3/2),
\]

followed by an overlap test against any source-valid lower/intermediate interval. If the constants are too weak to overlap, the next pivot is a direct two-type moment closure for the escape law rather than another generic contraction estimate.

## 11. Self-checks

1. **Regular-tree check.** If `Var(nu)=0`, then (7.2) gives `M=m` exactly to first order, consistent with the regular-tree formula `(m-lambda)/(m+lambda)`.
2. **Coefficient check.** `f_2-Var(nu)=m(m-1)`, so the coefficient in (7.5) is exactly `(m-1)/(2f_2)>0`.
3. **Moment check.** Every place in the new proof uses at most a cubic offspring average: uniform `X^3`, Holder `(3/2,3)`, or the cubic bound (6.4). No fourth moment is hidden in the displayed argument.
4. **Prior-art check.** Terminal monotonicity under stronger exponential-moment assumptions is prior art through the Einstein relation and is explicitly acknowledged by the 2025 monotonicity paper. The result claimed here is the weaker finite-third-moment tail hypothesis plus the direct `W_{3/2}`/branch-addition proof route.
5. **No metric substitution.** The theorem is a restricted tail-assumption result near one endpoint and does not solve the full conjecture.
