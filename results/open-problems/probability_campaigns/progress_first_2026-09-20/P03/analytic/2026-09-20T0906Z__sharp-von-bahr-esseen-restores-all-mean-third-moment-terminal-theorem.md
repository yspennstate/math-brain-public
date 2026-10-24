Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — sharp von Bahr–Esseen constant restores the all-mean finite-third-moment terminal theorem

**Status:** PROVED PARTIAL / CORRECTED THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains unresolved. This report supplies a valid proof of the all-mean finite-third-moment terminal monotonicity statement that the `0800Z` report intended but did not prove. The `0800Z` proof itself remains withdrawn because its von Bahr–Esseen constant was wrong; the present report does not rewrite that history.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role. Old D0047 history and P03-B files are untouched.

**Captured master immediately before write:** `0054f815e38f0df56d29ad7cfbd0c85208174ffe`.

**Inherited checkpoints:**

* `2026-09-20T0800Z__third-moment-terminal-monotonicity.md`: all-mean third-moment claim withdrawn because it used an invalid constant-one von Bahr–Esseen bound.
* `2026-09-20T0810Z__third-moment-contraction-correction-and-high-mean-theorem.md`: corrected the inequality with a coarse universal factor and proved terminal monotonicity only for `m>(3+sqrt(5))/2`, while preserving the exact branch-addition/cubic-moment part of the argument.
* P03-B latest complementary checkpoint: `P03/coupling/2026-09-20T0813Z__local-history-filter-and-dangerous-tail.md`, which treats path-history/coupling effects and is not duplicated here.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The intermediate obligation **does move**: the artificial high-mean condition from the `0810Z` correction is removed completely. Under a finite third offspring moment, the terminal monotonicity interval now follows for **every supercritical mean `m>1`**.

## 1. Source convention and current broad benchmark

Let `nu` be the offspring variable of a supercritical Galton–Watson tree without leaves:

\[
P(\nu=0)=0,\qquad m:=E\nu>1.
\]

The original outward-bias convention `beta` has, at a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac{1}{1+\beta k},\qquad
P_\beta(x,x_i)=\frac{\beta}{1+\beta k}.
\]

I use the reciprocal **parent-bias** parameter

\[
\lambda=\beta^{-1},
\]

so

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac{1}{\lambda+k}.
\tag{1.1}
\]

The transient interval is `0<=lambda<m`. The LPP conjecture is that the speed `ell_lambda` is nonincreasing in `lambda` (equivalently nondecreasing in outward bias `beta`).

Primary partial-result source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865.

The strongest broad low-parent-bias theorem checked for this campaign remains H. Song, L. Wang and K. Xiang, *J. Appl. Probab.* 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, then

\[
\ell_\lambda\text{ is strictly decreasing for }
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability in the appropriate ballistic/CLT regime; their later arXiv:2006.03433 gives analyticity in the ballistic regime. Those regularity results do not by themselves supply the global sign.

The Song–Wang–Xiang paper also points out that the Einstein relation yields monotonicity near `lambda=m` under stronger integrability assumptions; the classical argument assumes an exponential offspring moment. Therefore the existence of *some* terminal monotonicity neighborhood is not claimed here as a new phenomenon. The contribution of this route is the much weaker tail hypothesis `E nu^3<infinity` together with a direct recursive proof. A bounded current search did not locate a checked published theorem under exactly this finite-third-moment assumption; that is negative evidence, not a novelty certificate.

## 2. Normalized critical recursion

Let `B_lambda` be the escape probability from a child-root never to hit its artificial parent. With iid copies `B_i`,

\[
B_\lambda\stackrel d=\frac{S_\nu}{\lambda+S_\nu},
\qquad S_n=\sum_{i=1}^n B_i.
\tag{2.1}
\]

Put

\[
\delta=m-\lambda,\qquad
e_\delta=E B_{m-\delta},\qquad
r_\delta=\frac{e_\delta}{\delta},\qquad
X_\delta=\frac{B_{m-\delta}}{e_\delta},
\tag{2.2}
\]

so `E X_delta=1`, and let

\[
Y_\delta=\sum_{i=1}^{\nu}X_{\delta,i}.
\]

Then exactly

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}{m-\delta+\delta r_\delta Y_\delta}.}
\tag{2.3}
\]

Under `E nu^3<infinity`, the inherited moment recursion gives, for sufficiently small positive `delta`,

\[
\sup E X_\delta^2<\infty,
\qquad
\sup E X_\delta^3<\infty,
\tag{2.4}
\]

and `r_delta` is bounded above and away from zero. Also

\[
r_\delta\longrightarrow r_0:=\frac{m-1}{f_2},
\qquad f_2:=E[\nu(\nu-1)].
\tag{2.5}
\]

The remaining issue after `0810Z` was solely obtaining a strict pairwise contraction for all `m>1` without a fourth moment.

## 3. The missing inequality: use Pinelis's sharp von Bahr–Esseen constant

Iosif Pinelis, *Best possible bounds of the von Bahr–Esseen type*, Ann. Funct. Anal. 6(4):1–29 (2015), arXiv:1008.5350, proves for `1<p<=2` the sharp martingale-difference inequality

\[
E\left|\sum_{i=1}^n D_i\right|^p
\le E|D_1|^p+\widetilde C_p\sum_{i=2}^n E|D_i|^p
\tag{3.1}
\]

for independent zero-mean variables as a special case. Proposition 1.8 gives the exact value

\[
\boxed{
C_*:=\widetilde C_{3/2}
=\sqrt{1+\frac1{\sqrt2}}
\approx1.3065629648763766.}
\tag{3.2}
\]

This is the point missed in the `0810Z` correction. The crude bound `2-1/n` was valid but too expensive; the best constant is small enough to recover contraction for every supercritical mean.

Fix `p=3/2`. Optimally couple `X_delta` and `X_eta`, independently across children, and write

\[
w:=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\qquad
D_i:=X_{\delta,i}-X_{\eta,i}.
\]

Since both normalized variables have mean one,

\[
E D_i=0,
\qquad E|D_i|^{3/2}=w^{3/2}.
\]

Conditioning on `nu=n>=1`, (3.1) gives

\[
E\left[\left|\sum_{i=1}^{n}D_i\right|^{3/2}\mid\nu=n\right]
\le [1+C_*(n-1)]w^{3/2}.
\tag{3.3}
\]

Averaging over `nu` uses only `E nu=m` and the no-leaf fact `nu>=1`:

\[
\boxed{
E|Y_\delta-Y_\eta|^{3/2}
\le A_m w^{3/2},
\qquad
A_m:=1+C_*(m-1).}
\tag{3.4}
\]

Therefore

\[
\boxed{
\|Y_\delta-Y_\eta\|_{3/2}
\le A_m^{2/3}w.}
\tag{3.5}
\]

## 4. Exact algebra: the critical contraction is strict for every `m>1`

For

\[
F_{\delta,r}(y)=\frac{y}{m-\delta+\delta r y},
\]

we have

\[
|\partial_yF_{\delta,r}(y)|\le\frac1{m-\delta}.
\tag{4.1}
\]

Thus the critical law-change coefficient is

\[
q_0(m):=\frac{A_m^{2/3}}{m}.
\tag{4.2}
\]

The key point is

\[
\boxed{q_0(m)<1\quad\text{for every }m>1.}
\tag{4.3}
\]

Indeed, put `t=m-1>0`. Then

\[
\begin{aligned}
m^3-A_m^2
&=(1+t)^3-(1+C_*t)^2\\
&=t\Big[(3-2C_*)+(3-C_*^2)t+t^2\Big].
\end{aligned}
\tag{4.4}
\]

Now

\[
C_*<\frac32,
\qquad
C_*^2=1+\frac1{\sqrt2}<3,
\]

so every coefficient in the bracket is strictly positive. Hence `m^3>A_m^2`, which is exactly (4.3).

Define the explicit positive critical contraction gap

\[
\gamma_m:=m-A_m^{2/3}>0.
\tag{4.5}
\]

Any preliminary `delta_0<gamma_m` gives

\[
\frac{A_m^{2/3}}{m-\delta_0}<1.
\tag{4.6}
\]

Further shrinking `delta_0` below will absorb the scalar coupling terms.

## 5. Pairwise Lipschitz control now closes for all means

The parameter derivatives used in `0800Z/0810Z` are unchanged:

\[
|\partial_\delta F_{\delta,r}(y)|\le C(y+y^2),
\qquad
|\partial_rF_{\delta,r}(y)|\le C\delta y^2.
\tag{5.1}
\]

Because `2p=3`, the uniform third-moment bound (2.4) makes the right side uniformly `L^{3/2}`. Consequently, with `h=|delta-eta|` and `bar delta=max(delta,eta)`, (3.5) and the fixed-point equations give

\[
w\le q w+C_1h+C_2\bar\delta|r_\delta-r_\eta|,
\qquad q<1.
\tag{5.2}
\]

The exact scalar identity is

\[
\boxed{
r_\delta^{-1}
=E\frac{Y_\delta^2}{m-\delta+\delta r_\delta Y_\delta}.}
\tag{5.3}
\]

For

\[
\psi_{\delta,r}(y)=\frac{y^2}{m-\delta+\delta r y},
\]

its `y` derivative has only linear growth,

\[
|\partial_y\psi_{\delta,r}(y)|\le Cy.
\tag{5.4}
\]

Hence Hölder with exponents `3/2` and `3`, together with (2.4), controls the law-change term. Parameter derivatives are controlled by `E(Y^2+Y^3)`. Since `r_delta` stays bounded above and below, (5.3) yields

\[
|r_\delta-r_\eta|
\le C_3w+C_4h+C_5\bar\delta|r_\delta-r_\eta|.
\tag{5.5}
\]

Shrink `delta_0` so that the last term is absorbed. Substitute (5.5) into (5.2). The additional coefficient multiplying `w` is `O(delta_0)`, so shrink once more while preserving (4.6). This proves

\[
\boxed{
W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta))
+|r_\delta-r_\eta|
\le C|\delta-\eta|}
\tag{5.6}
\]

for all sufficiently small positive `delta,eta`, **with no restriction on `m` beyond `m>1`**.

This is the exact missing input in the prior third-moment proof.

## 6. Exact escape-tilt identity and cubic bookkeeping

For completeness, retain the exact branch-addition route rather than hiding the rest behind the previous report. Let `a=m-1` and

\[
D_{n,\delta}=a-\delta+e_\delta\sum_{i=0}^{n}X_{\delta,i},
\]

\[
h_n(\delta)=E\left[\frac{X_{\delta,0}}{D_{n,\delta}}\right].
\]

Adding one independent branch gives the exact identity

\[
\boxed{
h_n-h_{n+1}=e_\delta g_n,}
\tag{6.1}
\]

where

\[
g_n=E\left[
\frac{X_{\delta,0}X_{\delta,n+1}}
{D_{n,\delta}D_{n+1,\delta}}
\right]>0.
\tag{6.2}
\]

For an iid copy `nu'`, define

\[
\bar h_\delta=E[h_\nu],
\]

\[
K_\delta=\frac12E\left[
|\nu-\nu'|
\sum_{j=\min(\nu,\nu')}^{\max(\nu,\nu')-1}g_j
\right].
\tag{6.3}
\]

The pairwise covariance identity gives exactly

\[
\boxed{
M(m-\delta)=m-e_\delta\frac{K_\delta}{\bar h_\delta}.}
\tag{6.4}
\]

At the critical edge,

\[
\bar h_0=\frac1{m-1},
\qquad
g_j(0)=\frac1{(m-1)^2},
\qquad
K_0=\frac{\operatorname{Var}(\nu)}{(m-1)^2}.
\tag{6.5}
\]

The pairwise law estimate (5.6) implies degreewise

\[
|g_j(\delta)-g_j(\eta)|
\le C(1+j)|\delta-\eta|.
\tag{6.6}
\]

The deterministic degree weight satisfies

\[
|n-k|\sum_{j=\min(n,k)}^{\max(n,k)-1}(1+j)
\le C(1+n^3+k^3),
\tag{6.7}
\]

so `E nu^3<infinity` is exactly enough to average (6.6). Hence

\[
|\bar h_\delta-\bar h_\eta|
+|K_\delta-K_\eta|
\le C|\delta-\eta|.
\tag{6.8}
\]

Combining (2.5), (6.4), (6.5), and (6.8) gives the increment-controlled expansion

\[
\boxed{
M(m-\delta)
=m-\frac{\operatorname{Var}(\nu)}{f_2}\delta
+O_{\rm Lip}(\delta^2).}
\tag{6.9}
\]

Here `R(delta)=O_Lip(delta^2)` means

\[
|R(\delta)-R(\eta)|
\le C\max(\delta,\eta)|\delta-\eta|.
\tag{6.10}
\]

## 7. All-mean finite-third-moment terminal theorem

Aïdékon's exact speed representation in this notation is

\[
\ell_\lambda
=\frac{M(\lambda)-\lambda}{M(\lambda)+\lambda}.
\tag{7.1}
\]

Using

\[
f_2-\operatorname{Var}(\nu)=m(m-1),
\]

(6.9) yields

\[
\boxed{
\ell_{m-\delta}
=\frac{m-1}{2f_2}\delta
+O_{\rm Lip}(\delta^2).}
\tag{7.2}
\]

The leading coefficient is strictly positive. Therefore there is `delta_*>0` such that for

\[
0\le\eta<\delta\le\delta_*,
\]

\[
\ell_{m-\delta}-\ell_{m-\eta}
\ge
\frac{m-1}{4f_2}(\delta-\eta)>0.
\tag{7.3}
\]

Equivalently:

### Theorem 7.1 — finite-third-moment terminal monotonicity for every supercritical mean

Assume

\[
\boxed{
P(\nu=0)=0,\qquad m=E\nu>1,\qquad E\nu^3<\infty.}
\tag{7.4}
\]

Then there exists a law-dependent `epsilon>0` such that

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }(m-\epsilon,m).}
\tag{7.5}
\]

No minimum-offspring-two assumption is needed; `P(nu=1)>0` is allowed. In outward bias `beta=1/lambda`, the speed is strictly increasing on the corresponding interval immediately above `1/m`.

This is a terminal-interval theorem only. It does **not** prove the full LPP conjecture.

## 8. A low-mean heavy-tail example newly covered by the corrected argument

Let `N` have

\[
P(N=n)=\frac{n^{-9/2}}{\zeta(9/2)},\qquad n\ge1,
\]

and define `nu` by

\[
P(\nu=1)=\frac12,
\qquad
P(\nu=1+N\mid\nu>1)=1,
\]

with the second branch chosen with probability `1/2`. Equivalently, `nu=1` with probability `1/2` and `nu=1+N` with probability `1/2`.

Then

\[
m=1+\frac12\frac{\zeta(7/2)}{\zeta(9/2)}
\approx1.53414518045,
\tag{8.1}
\]

well below the `0810Z` cutoff `(3+sqrt(5))/2`. The polynomial tail gives

\[
E\nu^3<\infty,
\qquad E\nu^4=\infty,
\]

and no positive exponential moment. Thus this law is outside both the earlier repository `E nu^4` terminal proof and the `0810Z` high-mean third-moment theorem, while the present theorem applies.

Moreover

\[
f_2
=\frac12 E[N(N+1)]
\approx1.17009744379,
\]

so the critical linear coefficient is

\[
\boxed{
\frac{m-1}{2f_2}
\approx0.22824816142.}
\tag{8.2}
\]

No explicit terminal width is claimed for this example in the present run.

## 9. What changed, what did not, and the next attack

### Genuine progress

The exact best von Bahr–Esseen constant removes the only obstruction that forced the `0810Z` theorem to assume

\[
m>\frac{3+\sqrt5}{2}.
\]

The corrected terminal theorem now holds under `E nu^3<infinity` for every `m>1`. In particular, it covers minimum-offspring-one and low-mean heavy-tailed laws that the prior P03-A terminal theorems did not cover.

The Zolotarev-metric pivot proposed in `0810Z` is no longer necessary to remove the high-mean condition. It may still be useful for weakening the moment assumption below three, but that is no longer the immediate bottleneck.

### What remains open

* `R_full: 1 -> 1`: the full LPP monotonicity conjecture is still unresolved.
* The terminal width `epsilon` is qualitative because the contraction and remainder constants have not yet been optimized explicitly.
* The theorem covers only a neighborhood of `lambda=m`; it does not bridge that neighborhood to the known low/intermediate-bias intervals.
* Finite third moment is sufficient for this proof, not shown necessary. Lowering the moment requirement remains open.

### Next analytic attack

Make the contraction/remainder constants explicit for the two-point minimum-offspring-one family

\[
P(\nu=1)=1-p,\qquad P(\nu=2)=p,
\]

starting with `p=1/2`. In this family `m=1+p`, `f_2=2p`, and the critical speed coefficient is exactly `1/4`. The Pinelis margin

\[
\gamma_m=m-[1+C_*(m-1)]^{2/3}
\]

is explicit, and all moments are bounded. The concrete goal is an explicit `epsilon_p`, followed by a check whether that terminal interval overlaps any independent low/intermediate-bias certificate. If it does not, the remaining uncovered interval becomes a precise finite target rather than a qualitative gap.

## 10. Honest ledger

* Full-source metric: `R_full: 1 -> 1`.
* `0800Z` proof: remains **WITHDRAWN** as written because it used a false constant-one von Bahr–Esseen inequality.
* `0810Z` correction: remains valid but is now superseded in strength on the mean assumption.
* New result: **PROVED PARTIAL** — finite third offspring moment plus no leaves and `m>1` implies strict terminal monotonicity on a law-dependent interval `(m-epsilon,m)`.
* Independent audit: not yet performed; research continues without freezing this slot.
