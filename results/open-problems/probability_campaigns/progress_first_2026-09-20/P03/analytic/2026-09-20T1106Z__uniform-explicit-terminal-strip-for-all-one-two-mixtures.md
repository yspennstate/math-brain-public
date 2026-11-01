Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — a uniform explicit terminal strip for every nondegenerate `{1,2}` offspring mixture

**Status:** PROVED PARTIAL / EXPLICIT RESTRICTED THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role. The current registry was already checked on assignment. P03-B retains the distinct regeneration/coupling/path-score role; its latest `2026-09-20T1020Z__finite-path-fisher-history-and-return-budget.md` was consumed only for continuity. Old D0047 history is untouched.

**Captured master immediately before this write:** `910deb3fb7287fe172f7a19c0af8c853ee33beef`.

**Inherited analytic checkpoints:**

- `2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md`: qualitative law-dependent terminal monotonicity for every no-leaf finite-third-moment law;
- `2026-09-20T1011Z__explicit-terminal-width-for-balanced-one-two-law.md`: explicit width `1/200` for the single balanced law `P(nu=1)=P(nu=2)=1/2`.

This run removes the **mixture-weight restriction** from that explicit-width program. It gives one explicit terminal strip for every supercritical law supported on `{1,2}`, including arbitrarily small positive mass at degree `2`.

The fixed source-level metric remains

`R_full: 1 -> 1`.

The intermediate obligation does move: explicit terminal monotonicity is now uniform over the full one-parameter `{1,2}` family rather than one mixture weight.

---

## 1. Source convention and current benchmark

At a non-root vertex with `k` children I use reciprocal **parent bias** `lambda`,

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Thus the original outward child-bias parameter is `beta=1/lambda`; increasing `lambda` means weaker outward bias. For offspring mean `m=E nu`, the transient interval is `0<=lambda<m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing in `lambda` throughout that interval.

Primary partial-result source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865.

A bounded current source check on 20 September 2026 again found the strongest broad later low-parent-bias theorem to be He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\]

That theorem does not cover the minimum-offspring-one family below. Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, give differentiability/analyticity in the appropriate ballistic regimes but not the missing global sign. The bounded search did not surface a later source-wide solution. This is negative evidence only, not a novelty certificate.

---

## 2. New theorem

Fix

\[
\boxed{
P(\nu=1)=1-p,\qquad P(\nu=2)=p,\qquad 0<p\le1.}
\tag{2.1}
\]

Then

\[
m=E\nu=1+p,
\qquad
f_2=E[\nu(\nu-1)]=2p.
\]

### Theorem 2.1 — explicit terminal strip for all mixture weights

For every `0<p<=1`, the parent-bias speed is strictly decreasing on

\[
\boxed{
1+p-\frac{p}{10000}
\le \lambda <1+p.}
\tag{2.2}
\]

More quantitatively, if

\[
1+p-\frac p{10000}\le\lambda_1<\lambda_2<1+p,
\]

then

\[
\boxed{
\ell_{\lambda_1}-\ell_{\lambda_2}
>0.07\,(\lambda_2-\lambda_1).}
\tag{2.3}
\]

Hence, at every differentiability point in this strip,

\[
\ell'_\lambda<-0.07.
\tag{2.4}
\]

The width `p/10000` is deliberately conservative. At `p=1/2` it is much smaller than the sharper `1/200` width proved in the `1011Z` report. The gain here is not a better balanced-law constant; it is removal of the mixture restriction all the way down to arbitrarily small `p>0`.

In outward-bias notation `beta=1/lambda`, the same statement gives strict increase of speed on the reciprocal interval immediately above the critical value `1/(1+p)`.

---

## 3. Exact normalized escape recursion

Write

\[
\delta:=m-\lambda,
\qquad
0<\delta\le c p,
\qquad
c:=10^{-4}.
\tag{3.1}
\]

Let `B_lambda` be the child-root escape probability from the artificial parent. Put

\[
e_\delta:=E B_{m-\delta},
\qquad
r_\delta:=\frac{e_\delta}{\delta},
\qquad
X_\delta:=\frac{B_{m-\delta}}{e_\delta},
\tag{3.2}
\]

so `E X_delta=1`. If

\[
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i},
\]

then the escape recursion is exactly

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}{m-\delta+\delta r_\delta Y_\delta}.}
\tag{3.3}
\]

The companion mean identity is

\[
\boxed{
\frac1{r_\delta}
=E\frac{Y_\delta^2}{m-\delta+\delta r_\delta Y_\delta}.}
\tag{3.4}
\]

The standard Jensen/concavity estimate gives

\[
e_\delta\le\frac\delta m,
\qquad
0<r_\delta\le\frac1m\le1.
\tag{3.5}
\]

The inherited critical-edge theorem gives

\[
\boxed{r_\delta\longrightarrow\frac12\quad(\delta\downarrow0)}
\tag{3.6}
\]

for every law (2.1), because its critical coefficient is

\[
\frac{m-1}{f_2}=\frac{p}{2p}=\frac12.
\]

The argument below first obtains a coarse Lipschitz estimate using only `r<=1`, and then feeds (3.6) back in to obtain the sharp enough bound `r<0.59` on the whole explicit strip.

---

## 4. Uniform second- and third-moment bounds

Set

\[
s_2:=EX_\delta^2,
\qquad
s_3:=EX_\delta^3.
\]

Since the denominator in (3.3) is at least `m-delta`,

\[
s_2\le\frac{EY_\delta^2}{(m-\delta)^2}
=\frac{m s_2+2p}{(m-\delta)^2}.
\]

Because `delta<=cp`,

\[
(m-\delta)^2-m
=pm-2m\delta+\delta^2
\ge pm(1-2c).
\]

Therefore

\[
\boxed{
s_2\le\frac{2}{m(1-2c)}<2.001.}
\tag{4.1}
\]

Similarly, for the `{1,2}` law,

\[
EY_\delta^3=m s_3+6p s_2.
\]

Moreover

\[
\begin{aligned}
(m-\delta)^3-m
&=pm(2+p)-3m^2\delta+3m\delta^2-\delta^3\\
&\ge pm(2+p)(1-2c),
\end{aligned}
\]

because `3m<=2(2+p)` for `0<p<=1`. Hence

\[
\boxed{
s_3
\le\frac{12}{m^2(2+p)(1-2c)^2}
<6.003.}
\tag{4.2}
\]

Consequently

\[
\boxed{EY_\delta^2<4.001.}
\tag{4.3}
\]

For the cubic child-sum moment, use

\[
EY_\delta^3
\le
\frac{12}{m(2+p)(1-2c)^2}
+
\frac{12p}{m(1-2c)}.
\tag{4.4}
\]

If `p<=1/2`, the two terms are respectively below `6.003` and `4.001`; if `p>=1/2`, they are below `3.202` and `6.002`. Thus throughout the full family and strip,

\[
\boxed{EY_\delta^3<10.01.}
\tag{4.5}
\]

These uniform moment bounds are the reason the endpoint width can be made explicit simultaneously for every `p>0`.

---

## 5. Quantitative `W_{3/2}` contraction uniformly in `p`

Let

\[
C_*:=\sqrt{1+\frac1{\sqrt2}}<1.307
\]

be the sharp Pinelis von Bahr–Esseen constant used in the `0906Z` report. For an optimal centered coupling of `X_delta-X_eta`, independent across children, the child-sum estimate is

\[
\|Y_\delta-Y_\eta\|_{3/2}
\le \alpha_p\,w,
\qquad
\alpha_p:=(1+C_*p)^{2/3},
\tag{5.1}
\]

where

\[
w:=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)).
\]

By concavity of `u^(2/3)`,

\[
\alpha_p\le1+\frac{2C_*}{3}p.
\]

Since `1-2C_*/3>0.1286` and `m=1+p<=2`,

\[
\frac{\alpha_p}{m}<1-0.0643p.
\]

Also `delta/m<=cp<=10^{-4}`, so

\[
\boxed{
\frac{\alpha_p}{m-\delta}
<1-0.064p.}
\tag{5.2}
\]

Now put

\[
F_{\delta,r}(y)=\frac{y}{m-\delta+\delta r y}.
\]

From (4.3)-(4.5), `r<=1`, and `m-delta>1`,

\[
\|\partial_\delta F(Y)\|_{3/2}<6.7,
\qquad
\|\partial_rF(Y)\|_{3/2}<0.000468\,p.
\]

Therefore, writing `h:=|delta-eta|` and `R:=|r_delta-r_eta|`,

\[
\boxed{
w\le(1-0.064p)w+6.7h+0.000468pR.}
\tag{5.3}
\]

For the scalar identity (3.4), set

\[
\psi_{\delta,r}(y)=\frac{y^2}{m-\delta+\delta r y}.
\]

Since

\[
|\psi(y)-\psi(z)|
\le (y+z)|y-z|
\]

on the present domain, Holder together with (4.5) and (5.1) gives a law-change coefficient below `7.6`. The parameter derivatives satisfy

\[
E|\partial_\delta\psi(Y)|<14.2,
\qquad
E|\partial_r\psi(Y)|<0.00101p.
\]

Using `r_delta r_eta<=1`,

\[
R\le7.6w+14.2h+0.00101pR,
\]

hence

\[
\boxed{R<7.61w+14.22h.}
\tag{5.4}
\]

Substituting (5.4) into (5.3) leaves the coefficient of `w` below

\[
1-(0.064-0.000468\cdot7.61)p
<1-0.0604p.
\]

The `h` term is below `6.707h`. Thus

\[
\boxed{
w<\frac{112}{p}h,}
\tag{5.5}
\]

and then

\[
\boxed{
R<\frac{867}{p}h.}
\tag{5.6}
\]

Now let `eta downarrow0` and use (3.6). Since `delta<=10^{-4}p`,

\[
\left|r_\delta-\frac12\right|
\le867\frac\delta p
\le0.0867.
\]

Therefore on the whole strip,

\[
\boxed{0<r_\delta<0.587<0.59.}
\tag{5.7}
\]

This bootstrap from coarse contraction to the critical value `1/2` is the step that makes a single width work even when `p` is arbitrarily small.

---

## 6. Exact one-coordinate formula for the Aidekon offspring tilt

For this family `a:=m-1=p`. Define

\[
D_{n,\delta}
:=p-\delta+\delta r_\delta\sum_{i=0}^{n}X_{\delta,i},
\]

\[
h_n(\delta):=E\frac{X_{\delta,0}}{D_{n,\delta}},
\qquad n=1,2,
\]

and

\[
g_1(\delta)
:=E\frac{X_{\delta,0}X_{\delta,2}}
{D_{1,\delta}D_{2,\delta}}.
\]

Adding the third branch gives the exact identity

\[
\boxed{h_1-h_2=e_\delta g_1.}
\tag{6.1}
\]

Define

\[
\boxed{x_\delta:=\frac{e_\delta g_1}{h_1}
=\frac{\delta r_\delta g_1}{h_1}.}
\tag{6.2}
\]

Then `h_2=h_1(1-x_delta)`. Since the original offspring probabilities are `1-p` and `p`, Aidekon's exact escape-tilted effective offspring mean becomes

\[
\boxed{
M_\delta
=\frac{(1-p)h_1+2ph_2}{(1-p)h_1+ph_2}
=\frac{m-2px_\delta}{1-px_\delta}.}
\tag{6.3}
\]

Equivalently,

\[
\boxed{
m-M_\delta
=\frac{p(1-p)x_\delta}{1-px_\delta}.}
\tag{6.4}
\]

Thus the full mixture dependence has been compressed into the scalar `x_delta`.

---

## 7. Uniform scale and Lipschitz bound for `x_delta`

Because `delta<=cp` and (5.7) holds,

\[
D_{n,\delta}\ge p-\delta\ge p(1-c).
\]

For `h_1`, use

\[
\frac1{p+u}\ge\frac1p-\frac{u}{p^2},\qquad u\ge0,
\]

and the fact that dropping the `-delta` term only increases the comparison denominator. Since `EX_0(X_0+X_1)=s_2+1<3.001`,

\[
\boxed{
h_1>\frac{0.9998}{p}.}
\tag{7.1}
\]

Independence of `X_0,X_2` gives

\[
\boxed{
g_1<\frac{1.0003}{p^2}.}
\tag{7.2}
\]

Therefore

\[
\boxed{
\frac{r_\delta g_1}{h_1}<\frac{0.5903}{p},
\qquad
0\le x_\delta<5.903\times10^{-5}.}
\tag{7.3}
\]

We next control changes in `x_delta`. Use the same independent coordinatewise optimal couplings as in Section 5.

For

\[
\Phi_{\delta,r}(x_0,x_1)
=\frac{x_0}{p-\delta+\delta r(x_0+x_1)},
\]

the coordinate derivatives, (5.5), and the parameter derivatives give

\[
\boxed{
|h_1(\delta)-h_1(\eta)|
<\frac{116}{p^2}h.}
\tag{7.4}
\]

The ingredients are explicit:

- the coordinate coefficient is below `1.0002/p`, hence contributes less than `112.1 h/p^2`;
- the direct `delta` coefficient is below `2.772/p^2`;
- the `r` coefficient times (5.6) contributes less than `0.27/p^2`.

For

\[
G_{\delta,r}(x_0,x_1,x_2)
=\frac{x_0x_2}{D_1D_2},
\]

telescoping one coordinate at a time, using `s_3<6.003`, yields a coordinate coefficient below `2.002/p^2`. The direct `delta` derivative contributes below `6.724/p^3`, and the `r` derivative together with (5.6) contributes below `0.70/p^3`. Hence

\[
\boxed{
|g_1(\delta)-g_1(\eta)|
<\frac{232}{p^3}h.}
\tag{7.5}
\]

Put

\[
A_\delta:=\frac{r_\delta g_1(\delta)}{h_1(\delta)},
\qquad x_\delta=\delta A_\delta.
\]

From (5.6), (7.1), (7.2), (7.4), and (7.5), quotient telescoping gives

\[
\boxed{
|A_\delta-A_\eta|
<\frac{1080}{p^2}h.}
\tag{7.6}
\]

Indeed the three contributions are respectively less than `868/p^2`, `137/p^2`, and `69/p^2`, leaving room under `1080/p^2` after outward rounding.

Finally,

\[
\begin{aligned}
|x_\delta-x_\eta|
&\le |\delta-\eta|\sup A
+\max(\delta,\eta)|A_\delta-A_\eta|\\
&<\left(\frac{0.5903}{p}
+10^{-4}p\frac{1080}{p^2}\right)h.
\end{aligned}
\]

Therefore

\[
\boxed{
|x_\delta-x_\eta|<\frac{0.70}{p}|\delta-\eta|.}
\tag{7.7}
\]

This is the central new estimate of the run. The apparent `1/p` divergence is exactly cancelled by the factor `p` in the offspring-tilt defect (6.4).

---

## 8. Speed secant inequality

Define

\[
a_p(x):=m-M=\frac{p(1-p)x}{1-px}.
\tag{8.1}
\]

Aidekon's speed formula in this notation is

\[
\ell_{m-\delta}
=\frac{M-(m-\delta)}{M+(m-\delta)}
=\frac{\delta-a_p(x_\delta)}{2m-\delta-a_p(x_\delta)}.
\tag{8.2}
\]

Let

\[
L_p(\delta,x)
:=\frac{\delta-a_p(x)}{2m-\delta-a_p(x)}.
\]

From (7.3), `px<5.903e-5`, hence

\[
0\le a_p(x)<6\times10^{-5}.
\tag{8.3}
\]

At fixed `x`,

\[
\partial_\delta L_p
=\frac{2(m-a_p(x))}{(2m-\delta-a_p(x))^2}
>\frac{0.99994}{2m}.
\tag{8.4}
\]

Also

\[
a_p'(x)=\frac{p(1-p)}{(1-px)^2}
<1.00012\,p(1-p).
\]

Since `delta+a_p(x)<1.6e-4`,

\[
\boxed{
|\partial_xL_p|
<\frac{1.0003\,p(1-p)}{2m}.}
\tag{8.5}
\]

Take `0<=eta<delta<=cp`. Using (7.7), (8.4), and (8.5),

\[
\begin{aligned}
L_p(\delta,x_\delta)-L_p(\eta,x_\eta)
&>\frac{1}{2m}
\left[0.99994
-1.0003\,p(1-p)\frac{0.70}{p}\right](\delta-\eta)\\
&\ge\frac{0.2997}{2m}(\delta-\eta).
\end{aligned}
\]

Since `m<=2`,

\[
\boxed{
L_p(\delta,x_\delta)-L_p(\eta,x_\eta)
>0.07(\delta-\eta).}
\tag{8.6}
\]

Because `lambda=m-delta`, (8.6) is exactly (2.3), proving Theorem 2.1.

---

## 9. What changed, what did not

### New proved partial result

The explicit critical-edge program now covers **every** supercritical `{1,2}` mixture:

\[
P(\nu=1)=1-p,
\quad P(\nu=2)=p,
\quad 0<p\le1,
\]

with one closed-form width

\[
\varepsilon_p=\frac{p}{10000}.
\]

The previous `1011Z` theorem was explicit only at `p=1/2`. This run removes that restriction.

### Full-source metric

`R_full: 1 -> 1`.

This is not the full LPP conjecture. Even within the `{1,2}` family, a large middle interval remains between currently certified low-bias information and this near-critical strip.

### Why the restriction can now be removed

The key mechanism is the exact cancellation of scales:

1. the critical contraction gap is of order `p` as `p downarrow0`, so the normalized-law Lipschitz constant is of order `1/p`;
2. the branch-addition coordinate obeys `|x_delta-x_eta|=O(|delta-eta|/p)`;
3. the effective offspring defect contains the compensating factor `p(1-p)`:

\[
m-M=\frac{p(1-p)x}{1-px}.
\]

Thus the speed sign remains uniformly positive after choosing `delta<=10^{-4}p`.

---

## 10. Exact remaining gap and next attack

The present theorem still uses the two-degree structure heavily through the scalar identity (6.3). The next analytic bottleneck is to replace that one-coordinate collapse by a finite-dimensional adjacent-branch system for

\[
P(\nu\in\{1,2,3\})=1.
\]

The exact branch-addition identities already available in earlier P03-A reports suggest defining

\[
x_1=\frac{e g_1}{h_1},
\qquad
x_2=\frac{e g_2}{h_2},
\]

so that `h_2/h_1=1-x_1` and `h_3/h_2=1-x_2`. The next useful theorem would be an explicit terminal strip, uniform over a nontrivial two-dimensional simplex of `{1,2,3}` mixture weights, followed by a compact-tail truncation argument. The point is to preserve the cancellation between small mixture masses and the corresponding escape-tilt defects rather than taking a worst-degree covariance envelope.

A second route is to combine the P03-B finite-path Fisher/history decomposition with the present critical contraction: near `lambda=m`, the continuation/return budget may provide a direct sign certificate whose constants depend on factorial moments rather than finite support. That would be the cleaner path toward removing the finite-support restriction altogether.

No publication, email, Drive output, force-push, peer overwrite, or historical overwrite was performed.