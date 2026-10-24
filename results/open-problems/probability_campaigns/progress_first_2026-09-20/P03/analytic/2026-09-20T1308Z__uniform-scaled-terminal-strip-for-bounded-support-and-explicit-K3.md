Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested, but no authenticated model-effort selector or guaranteed full-hour execution is exposed here, so I do not claim it.

# P03-A analytic proof report — a uniform scaled terminal strip for bounded offspring support, with an explicit full `{1,2,3}` simplex theorem

**Status:** PROVED PARTIAL / NEW RESTRICTED THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was already checked on assignment and is not changed here. P03-B retains regeneration/coupling/path-score work; I checked its latest `2026-09-20T1215Z__two-sided-return-elasticity-and-fresh-child-charge.md` for continuity and do not duplicate its return-score analysis. Old D0047 history is untouched.

**Captured master immediately before this write:** `1981f87465beed04c7ac89b7f71b99dc426a6c8f`.

**Inherited P03-A checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1158Z__explicit-two-coordinate-terminal-strip-for-balanced-one-two-three-law.md`.

That report treated only the balanced law on `{1,2,3}`. This run removes the mixture restriction over the entire supercritical `{1,2,3}` simplex and, more structurally, proves a uniform scaled terminal theorem for every fixed bounded offspring support `{1,...,K}`.

The fixed source-level metric remains

`R_full: 1 -> 1`.

The intermediate obligation moves: the critical-edge interval is now uniform over all laws with a fixed support bound, rather than law-by-law or one selected finite family.

---

## 1. Bias convention and current external benchmark

At a non-root vertex with `k` children I use reciprocal **parent bias** `lambda`:

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Thus the original outward child-bias parameter is `beta=1/lambda`. Increasing `lambda` weakens the outward bias. If `m=E nu`, the transient interval is `0<=lambda<m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing in `lambda` throughout that interval.

Primary partial source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. Their outward-bias result gives increasing speed for sufficiently large `beta` (historically `beta>=717`, with the minimum-degree refinement in the paper).

A fresh bounded source check on 20 September 2026 again found the broad later theorem of He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\]

Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, prove differentiability / analyticity in the corresponding ballistic regimes but do not supply the missing sign. The bounded search did not surface a full-source resolution. This is negative evidence only, not a novelty certificate.

---

## 2. New theorem statements

### Theorem 2.1 — uniform scaled terminal strip for every fixed bounded support

Fix an integer `K>=2`. There exists a constant `c_K>0`, depending only on `K`, such that for every offspring law satisfying

\[
P(1\le\nu\le K)=1,\qquad m:=E\nu>1,
\]

the parent-bias speed is strictly decreasing on

\[
\boxed{
 m-c_K(m-1)<\lambda<m.}
\tag{2.1}
\]

Moreover `c_K` may be chosen uniformly over the entire supercritical probability simplex on `{1,...,K}`. In particular the terminal width cannot collapse faster than a fixed multiple of `m-1` as the law approaches the degenerate critical vertex `P(nu=1)=1`.

This is stronger than the inherited qualitative finite-third-moment terminal theorem, whose `epsilon` was law-dependent.

### Theorem 2.2 — completely explicit full `{1,2,3}` simplex certificate

Let

\[
P(\nu=i)=p_i,\qquad i=1,2,3,
\qquad p_1+p_2+p_3=1,
\]

and assume

\[
a:=m-1=p_2+2p_3>0.
\]

Then the speed is strictly decreasing throughout

\[
\boxed{
 m-10^{-6}(m-1)\le\lambda<m.}
\tag{2.2}
\]

More quantitatively, whenever

\[
m-10^{-6}(m-1)\le\lambda_1<\lambda_2<m,
\]

one has

\[
\boxed{
\ell_{\lambda_1}-\ell_{\lambda_2}
>0.04\,(\lambda_2-\lambda_1).}
\tag{2.3}
\]

The constant is deliberately conservative. The gain over the `1158Z` report is that (2.2) covers **every** supercritical law on `{1,2,3}`, including arbitrarily small total mass away from degree `1`, rather than only the balanced point. On the `{1,2}` face the earlier `1106Z` theorem has the much wider `p/10000` strip; the present theorem is a two-dimensional simplex result.

---

## 3. Normalized critical recursion and support-uniform moment control

Write

\[
\delta:=m-\lambda,
\qquad e_\delta:=E B_{m-\delta},
\qquad r_\delta:=\frac{e_\delta}{\delta},
\qquad X_\delta:=\frac{B_{m-\delta}}{e_\delta},
\]

so `E X_delta=1`. If

\[
Y_\delta=\sum_{i=1}^{\nu}X_{\delta,i},
\]

then the inherited exact escape recursion and companion mean identity are

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}{m-\delta+\delta r_\delta Y_\delta},
}
\tag{3.1}
\]

\[
\boxed{
\frac1{r_\delta}
=E\frac{Y_\delta^2}{m-\delta+\delta r_\delta Y_\delta}.
}
\tag{3.2}
\]

The inherited Jensen bound gives `0<r_delta<=1/m<=1`. Put

\[
f_2=E[\nu(\nu-1)].
\]

The previously proved critical limit is

\[
\boxed{
r_\delta\longrightarrow r_0:=\frac{m-1}{f_2}}
\qquad(\delta\downarrow0).
\tag{3.3}
\]

For `1<=nu<=K`, with `a=m-1`,

\[
2a\le f_2\le Ka,
\qquad
\frac1K\le r_0\le\frac12.
\tag{3.4}
\]

The inequalities follow degreewise from

\[
2(n-1)\le n(n-1)\le K(n-1),\qquad1\le n\le K.
\]

Now restrict temporarily to `0<delta<=c a`, with `c>0` small depending only on `K`. If

\[
s_2=EX_\delta^2,\qquad s_3=EX_\delta^3,
\]

then from (3.1)

\[
s_2\le
\frac{m s_2+f_2}{(m-\delta)^2},
\]

and hence

\[
s_2\le
\frac{f_2}{(m-\delta)^2-m}.
\tag{3.5}
\]

Because

\[
(m-\delta)^2-m\ge ma(1-2c),
\]

(3.4) gives a bound `s_2<=C_2(K)` uniform over the whole simplex.

Similarly

\[
EY_\delta^3=m s_3+3f_2s_2+f_3,
\qquad
f_3=E[\nu(\nu-1)(\nu-2)],
\]

and

\[
f_3\le K(K-2)a.
\]

Since `(m-delta)^3-m` is bounded below by a positive `K`-dependent multiple of `ma` once `c=c(K)` is small, one obtains

\[
\boxed{
EX_\delta^2+EX_\delta^3+EY_\delta^2+EY_\delta^3\le C_3(K)
}
\tag{3.6}
\]

uniformly over all source laws with support in `{1,...,K}` and `0<delta<=ca`.

This uniformity is the first ingredient that was missing from the law-by-law terminal theorem.

---

## 4. Uniform `W_{3/2}` contraction at scale `m-1`

Let

\[
C_*:=\sqrt{1+1/\sqrt2}<1.307
\]

be the sharp `p=3/2` von Bahr–Esseen constant inherited from the `0906Z` proof (Pinelis, arXiv:1008.5350). For an optimal centered coupling of two normalized laws and iid coupled child copies,

\[
\left\|Y_\delta-Y_\eta\right\|_{3/2}
\le
\alpha_a\,W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\]

where

\[
\alpha_a=(1+C_*a)^{2/3}.
\tag{4.1}
\]

By concavity,

\[
\alpha_a\le1+\frac{2C_*}{3}a.
\]

Because `2C_*/3<1`, and `m=1+a<=K`, there is `gamma_K>0` such that, after reducing `c_K` if necessary,

\[
\boxed{
\frac{\alpha_a}{m-\delta}\le1-\gamma_K a.}
\tag{4.2}
\]

For

\[
F_{\delta,r}(y)=\frac{y}{m-\delta+\delta r y},
\]

one has

\[
|\partial_yF|\le\frac1{m-\delta},
\]

\[
|\partial_\delta F|
\le \frac{y+r y^2}{(m-\delta)^2},
\qquad
|\partial_rF|
\le\frac{\delta y^2}{(m-\delta)^2}.
\]

The moment bounds (3.6) therefore imply, with

\[
w=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\quad h=|\delta-\eta|,
\quad R=|r_\delta-r_\eta|,
\]

a uniform estimate

\[
w\le(1-\gamma_Ka)w+C_Kh+C_KcaR.
\tag{4.3}
\]

For

\[
\psi_{\delta,r}(y)=\frac{y^2}{m-\delta+\delta r y},
\]

its derivative in `y` satisfies the useful inequality

\[
0\le\psi'(y)
=\frac{y\{2(m-\delta)+\delta r y\}}
{(m-\delta+\delta r y)^2}
\le\frac{2y}{m-\delta}.
\tag{4.4}
\]

Thus comparing (3.2) at two parameters costs only third moments, not sixth moments. Using Holder and (3.6),

\[
R\le C_K w+C_Kh+C_KcaR.
\tag{4.5}
\]

Choosing `c_K` small enough to absorb the final terms in (4.3)–(4.5) gives

\[
\boxed{
w\le\frac{C_K}{a}h,
\qquad
R\le\frac{C_K}{a}h.}
\tag{4.6}
\]

Letting `eta downarrow0` and using (3.3),

\[
|r_\delta-r_0|\le C_K\frac\delta a\le C_Kc_K.
\tag{4.7}
\]

This is the key scaling fact: although the contraction gap vanishes linearly as `m downarrow1`, the allowed terminal width is also taken proportional to `m-1`, and the two losses cancel.

---

## 5. New exact branch-vector identity for arbitrary bounded support

This is the main structural lemma of the run.

For `n>=1` write

\[
D_{n,\delta}
:=a-\delta+\delta r_\delta\sum_{i=0}^{n}X_{\delta,i},
\]

\[
h_n(\delta):=E\frac{X_{\delta,0}}{D_{n,\delta}},
\]

and for `1<=j<=K-1`,

\[
g_j(\delta)
:=E\frac{X_{\delta,0}X_{\delta,j+1}}
{D_{j,\delta}D_{j+1,\delta}}.
\]

Adding one branch gives exactly

\[
\boxed{h_j-h_{j+1}=e_\delta g_j.}
\tag{5.1}
\]

Define

\[
\boxed{x_j:=\frac{e_\delta g_j}{h_1}.}
\tag{5.2}
\]

Then

\[
\frac{h_n}{h_1}=1-\sum_{j=1}^{n-1}x_j.
\tag{5.3}
\]

Let `p_n=P(nu=n)` and define the tail coefficients

\[
T_j:=P(\nu>j),
\qquad
A_j:=E[(\nu-m)\mathbf 1_{\{\nu>j\}}].
\tag{5.4}
\]

The `A_j` are nonnegative because they equal a tail mass times the gap between the conditional tail mean and the global mean. Aidekon's escape-tilted effective offspring mean

\[
M_\delta=
\frac{\sum_n n p_n h_n}{\sum_n p_n h_n}
\]

therefore satisfies the exact finite-vector identity

\[
\boxed{
q_\delta:=m-M_\delta
=
\frac{\sum_{j=1}^{K-1}A_jx_j}
{1-\sum_{j=1}^{K-1}T_jx_j}.}
\tag{5.5}
\]

Two sums collapse completely:

\[
\boxed{
\sum_{j=1}^{K-1}T_j=E(\nu-1)=a,}
\tag{5.6}
\]

and

\[
\boxed{
\sum_{j=1}^{K-1}A_j
=E[(\nu-m)(\nu-1)]
=\operatorname{Var}(\nu).}
\tag{5.7}
\]

Equation (5.7) is the new algebraic reason the many-coordinate problem still has only one first-order critical obstruction: every branch-addition coordinate has the same leading slope, and the coefficients sum to exactly the offspring variance.

For `K=3`, (5.5) reduces to the formula inherited from `1158Z`:

\[
q_\delta=
\frac{p_1(p_2+2p_3)x_1+p_3(2p_1+p_2)x_2}
{1-(p_2+p_3)x_1-p_3x_2}.
\]

---

## 6. Common critical secant slope of all branch coordinates

Put

\[
t=\frac\delta a,
\qquad
A_{n,\delta}:=\frac{D_{n,\delta}}a
=1-t+t r_\delta\sum_{i=0}^{n}X_{\delta,i}.
\]

Then

\[
a h_1=E\frac{X_0}{A_{1,\delta}},
\qquad
a^2g_j=E\frac{X_0X_{j+1}}{A_{j,\delta}A_{j+1,\delta}}.
\]

Using `A_{n,delta}>=1-t`, the moment bounds and (4.6), uniformly in `j<=K-1`,

\[
a h_1=1+O_K(c_K),
\qquad
a^2g_j=1+O_K(c_K),
\tag{6.1}
\]

and, for two parameters,

\[
\left|a h_1(\delta)-a h_1(\eta)\right|
\le C_K\frac{|\delta-\eta|}{a},
\]

\[
\left|a^2g_j(\delta)-a^2g_j(\eta)\right|
\le C_K\frac{|\delta-\eta|}{a}.
\tag{6.2}
\]

Since

\[
x_j
=\delta\,\frac{r_\delta}{a}
\frac{a^2g_j}{a h_1},
\]

(4.7) and (6.1)–(6.2) imply the uniform secant expansion

\[
\boxed{
 x_j(\delta)-x_j(\eta)
=\frac{r_0}{a}(\delta-\eta)
+O_K(c_K)\frac{\delta-\eta}{a}.}
\tag{6.3}
\]

This is stronger than merely knowing `x_j(delta)=delta r_0/a+o(delta)`: the error is controlled on **all secants** in the scaled strip.

Substituting (6.3) into the exact vector formula (5.5), using (5.6)–(5.7), gives

\[
\boxed{
 q_\delta-q_\eta
=rac{\operatorname{Var}(\nu)}{f_2}(\delta-\eta)
+O_K(c_K)(\delta-\eta).}
\tag{6.4}
\]

The critical coefficient has a uniform gap from `1`:

\[
1-\frac{\operatorname{Var}(\nu)}{f_2}
=rac{m(m-1)}{f_2}
\ge\frac1K,
\tag{6.5}
\]

because `f_2<=Ka` and `m>=1`.

Choose `c_K` so that the absolute error coefficient in (6.4) is at most `1/(2K)`. Then

\[
(\delta-q_\delta)-(\eta-q_\eta)
\ge\frac1{2K}(\delta-\eta)>0.
\tag{6.6}
\]

Aidekon's symmetrized speed formula is

\[
\ell_{m-\delta}
=\frac{M_\delta-(m-\delta)}{M_\delta+(m-\delta)}
=\frac{\delta-q_\delta}{2m-\delta-q_\delta}.
\tag{6.7}
\]

The numerator is nonnegative and increasing by (6.6), while the denominator decreases after `c_K` is reduced once more if necessary. Since it is at most `2m<=2K`,

\[
\boxed{
\ell_{m-\delta}-\ell_{m-\eta}
\ge\frac1{4K^2}(\delta-\eta),
\qquad0\le\eta<\delta\le c_Ka.}
\tag{6.8}
\]

This proves Theorem 2.1.

---

## 7. Explicit constants for the full `{1,2,3}` simplex

Now set `K=3` and take

\[
\boxed{c=10^{-6}.}
\]

Here

\[
a=p_2+2p_3,
\qquad
f_2=2p_2+6p_3,
\qquad
\frac13\le r_0=\frac a{f_2}\le\frac12.
\tag{7.1}
\]

Also

\[
f_2\le3a,\qquad f_3=6p_3\le3a.
\]

The estimates in Section 3 become, with outward rounding,

\[
EX_\delta^2<3.001,
\qquad
EX_\delta^3<15.1,
\]

\[
EY_\delta^2<15.1,
\qquad
EY_\delta^3<106.
\tag{7.2}
\]

For the child-sum coupling, `(1+C_*a)^{2/3}/(m-delta)` is bounded by `1-0.042a` after the small `delta r` perturbation is separated. The parameter derivatives of `F` are bounded in `L^{3/2}` by `27` and `22.4 delta`, while (4.4) and (7.2) give the scalar companion estimate

\[
R\le24w+123h.
\]

Absorbing the `delta R` term yields the explicit pair

\[
\boxed{
w<\frac{650}{a}h,
\qquad
R<\frac{16000}{a}h.}
\tag{7.3}
\]

Letting `eta downarrow0`,

\[
\boxed{|r_\delta-r_0|<0.016,\qquad r_\delta<0.517.}
\tag{7.4}
\]

For the dimensionless branch weights

\[
H:=a h_1,
\qquad
G_j:=a^2 g_j,
\qquad j=1,2,
\]

the denominators satisfy `A_n>=1-c`. Direct use of (7.2) and (7.4) gives

\[
|H-1|<3.1c,
\qquad
|G_j-1|<8.8c.
\tag{7.5}
\]

Under the coupled laws, with `tau=h/a`, coordinate differentiation gives

\[
|H(\delta)-H(\eta)|<660\tau,
\qquad
|G_j(\delta)-G_j(\eta)|<1320\tau.
\tag{7.6}
\]

Therefore, for

\[
J_j:=\frac{G_j}{H},
\]

\[
|J_j-1|<12.2c,
\qquad
|J_j(\delta)-J_j(\eta)|<2000\tau.
\tag{7.7}
\]

Writing

\[
u_j(\delta):=\frac{r_\delta J_j(\delta)}a,
\qquad x_j(\delta)=\delta u_j(\delta),
\]

(7.3)–(7.7) imply

\[
\left|u_j(\delta)-\frac{r_0}{a}\right|
<\frac{0.0161}{a},
\]

\[
|u_j(\delta)-u_j(\eta)|
<\frac{17100}{a^2}h.
\]

Hence, for `delta>eta`, because `eta<=ca`,

\[
\boxed{
\left|
(x_j(\delta)-x_j(\eta))
-\frac{r_0}{a}(\delta-\eta)
\right|
<\frac{0.034}{a}(\delta-\eta),
\quad j=1,2.}
\tag{7.8}
\]

Also `0<=x_j<5.2*10^{-7}` throughout the strip.

For `{1,2,3}` the numerator coefficients in (5.5) are

\[
A_1=p_1(p_2+2p_3),
\qquad
A_2=p_3(2p_1+p_2),
\]

and

\[
A_1+A_2=\operatorname{Var}(\nu)\le2a.
\tag{7.9}
\]

The denominator coefficients sum to

\[
(p_2+p_3)+p_3=a.
\]

Using (7.8), the tiny bound on `x_j`, and the exact rational formula gives the quantitative secant estimate

\[
\boxed{
\left|
(q_\delta-q_\eta)
-\frac{\operatorname{Var}(\nu)}{f_2}(\delta-\eta)
\right|
<0.069(\delta-\eta).}
\tag{7.10}
\]

(The direct numerator error is `<0.068 h`; all denominator corrections together are `<10^{-5}h`, so `0.069` leaves visible slack.)

Finally,

\[
1-\frac{\operatorname{Var}(\nu)}{f_2}
=\frac{ma}{f_2}
\ge\frac13.
\]

Thus

\[
(\delta-q_\delta)-(\eta-q_\eta)
>\left(\frac13-0.069\right)(\delta-\eta)
>0.264(\delta-\eta).
\tag{7.11}
\]

Moreover `q_delta-q_eta>-0.069(delta-eta)`, so `2m-delta-q_delta` decreases with `delta`; and (7.11) from `eta=0` shows the speed numerator is positive. Since `2m<=6`, (6.7) gives

\[
\ell_{m-\delta}-\ell_{m-\eta}
>\frac{0.264}{6}(\delta-\eta)
>0.04(\delta-\eta).
\]

This proves Theorem 2.2.

---

## 8. What changed, and what remains open

### New proved content in this run

1. **Exact arbitrary finite-support branch-vector identity** (5.5), with the two collapse identities
   \[
   \sum T_j=m-1,
   \qquad
   \sum A_j=\operatorname{Var}(\nu).
   \]
   This is the structural reason all branch-addition coordinates share a single first-order obstruction.

2. **Uniform scaled terminal theorem for every fixed support bound `K`**: there is `c_K>0` valid simultaneously for all supercritical laws on `{1,...,K}`.

3. **Explicit whole-simplex `{1,2,3}` theorem**: width `(m-1)/10^6` and secant speed margin `0.04`.

The new theorem is still only a terminal interval. It does **not** prove the full LPP conjecture, and it does not close the middle-bias region.

### Exact remaining gap

The current analytic program now has two complementary regions:

- source-wide / low-parent-bias results for minimum offspring at least two, together with the earlier P03-A extensions;
- terminal parent-bias intervals near `lambda=m`, now uniform over each bounded-support class and explicit over `{1,2,3}`.

The principal missing implication is to make the terminal control **support-free** with a quantitative width that depends on a low-order tail statistic rather than a hard cutoff `K`, and then connect it to the low/intermediate certificates. The obstacle in Section 6 is not the exact algebra: (5.5) already generalizes. It is obtaining uniform branch-coordinate secant control when arbitrarily many offspring values contribute.

### Next concrete analytic attack

Use (5.5) with a core-tail split at degree `K` rather than truncating the law outright. The coefficient identities suggest charging the tail by

\[
\sum_{j\ge K}A_j
=E[(\nu-m)(\nu-K)_+]
\]

and

\[
\sum_{j\ge K}T_j=E[(\nu-K)_+],
\]

while the low coordinates retain the common critical slope. The target is a support-free terminal theorem under a finite third moment with an explicit width controlled by a normalized tail quantity, then a passage from bounded support to arbitrary no-leaf laws without reintroducing the minimum-degree singularity at `lambda=d`.

No email, Drive, publication, force-push, historical overwrite, peer overwrite, or permission change is part of this report.