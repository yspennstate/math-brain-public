Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — an explicit terminal monotonicity width for the balanced `{1,2}` law

**Status:** PROVED PARTIAL / EXPLICIT RESTRICTED THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role. The current registry was checked once. P03-B retains the distinct coupling/path-score role; I consumed its latest `2026-09-20T0904Z__annealed-score-and-continuation-energy.md` only for continuity and did not duplicate its path-coupling work. Old D0047 history is untouched.

**Captured master before this write:** `ab1c4bd3b662dfe712acae1193e41d2f102dddb1`.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0906Z__sharp-von-bahr-esseen-restores-all-mean-third-moment-terminal-theorem.md`.

That report proved a qualitative law-dependent terminal interval `(m-epsilon,m)` for every no-leaf law with finite third moment. Its next obligation was to make the width explicit for the family

\[
P(\nu=1)=1-p,\qquad P(\nu=2)=p,
\]
starting with `p=1/2`.

The fixed source-level metric remains

`R_full: 1 -> 1`.

The intermediate obligation **does move**: for the first genuinely random minimum-offspring-one law in this terminal program, the terminal width is now explicit and comes with a quantitative secant/derivative margin.

---

## 1. Source convention and present benchmark

The source problem is the Lyons–Pemantle–Peres monotonicity conjecture for biased random walk on a supercritical Galton–Watson tree without leaves. In the original outward child-bias parameter `beta`, at a non-root vertex with `k` children,

\[
P_\beta(x,x^*)=\frac{1}{1+\beta k},\qquad
P_\beta(x,x_i)=\frac{\beta}{1+\beta k}.
\]

I use reciprocal **parent bias**

\[
\lambda=\beta^{-1},
\]

so

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\tag{1.1}
\]

The conjectured sign is that the speed `ell_lambda` is nonincreasing in `lambda` on the full transient interval `0<=lambda<m=E nu`.

Primary partial-result source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865.

The strongest broad low-parent-bias theorem rechecked for this campaign is He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: if the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

That theorem does not cover the minimum-offspring-one law treated below. Aidekon's earlier source-uniform work yields the familiar `lambda<=1/2` baseline for no-leaf laws. Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, provide differentiability/analyticity in the relevant ballistic regimes but not the missing global derivative sign.

A bounded current search on 20 September 2026 found no later source-wide resolution. This is negative evidence only, not a novelty certificate.

---

## 2. New theorem

Consider the balanced nondegenerate offspring law

\[
\boxed{
P(\nu=1)=P(\nu=2)=\frac12.}
\tag{2.1}
\]

Then

\[
m=E\nu=\frac32,
\qquad
f_2=E[\nu(\nu-1)]=1.
\]

### Theorem 2.1 — explicit terminal interval

For the law (2.1), the parent-bias speed is strictly decreasing on

\[
\boxed{
\frac{299}{200}\le \lambda<\frac32.}
\tag{2.2}
\]

More quantitatively, whenever

\[
\frac{299}{200}\le \lambda_1<\lambda_2<\frac32,
\]

one has the secant bound

\[
\boxed{
\ell_{\lambda_1}-\ell_{\lambda_2}
>0.062\,(\lambda_2-\lambda_1).}
\tag{2.3}
\]

Consequently, at every point of differentiability in this interval,

\[
\boxed{\ell'_\lambda<-0.062.}
\tag{2.4}
\]

The width `1/200=0.005` is deliberately conservative; I did not optimize the constants after obtaining a clean positive margin.

---

## 3. Normalized critical recursion with explicit moments

Write

\[
\delta:=\frac32-\lambda,
\qquad 0<\delta\le\varepsilon:=\frac1{200}.
\tag{3.1}
\]

Let `B_lambda` be the escape probability from a child-root never to hit its artificial parent. Put

\[
e_\delta:=E B_{3/2-\delta},
\qquad
r_\delta:=\frac{e_\delta}{\delta},
\qquad
X_\delta:=\frac{B_{3/2-\delta}}{e_\delta},
\tag{3.2}
\]

so `E X_delta=1`. With iid copies and

\[
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i},
\]

the exact normalized recursion inherited from the terminal theorem is

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}
{\frac32-\delta+\delta r_\delta Y_\delta}.}
\tag{3.3}
\]

Also, concavity of `x/(lambda+x)` gives the inherited deterministic upper bound

\[
e_\delta\le\frac\delta m=\frac{2\delta}{3},
\qquad
\boxed{0<r_\delta\le\frac23.}
\tag{3.4}
\]

Set

\[
s_2(\delta)=EX_\delta^2,
\qquad
s_3(\delta)=EX_\delta^3.
\]

Because the denominator in (3.3) is at least `3/2-delta`,

\[
s_2
\le\frac{E Y_\delta^2}{(3/2-\delta)^2}
=\frac{(3/2)s_2+1}{(3/2-\delta)^2},
\tag{3.5}
\]

where `E Y^2=(3/2)s_2+1` uses `f_2=1`. Since `3/2-delta>=299/200`,

\[
\boxed{
s_2\le
\frac{1}{(299/200)^2-3/2}
=\frac{40000}{29401}<1.361.}
\tag{3.6}
\]

Similarly, because `nu<=2`, `f_3=0` and

\[
E Y^3=\frac32 s_3+3s_2.
\]

Hence

\[
s_3
\le
\frac{3s_2}{(299/200)^3-3/2}
<2.217.
\tag{3.7}
\]

Thus throughout the entire strip (3.1),

\[
\boxed{
E Y^2<3.042,
\qquad
E Y^3<7.409.}
\tag{3.8}
\]

These explicit moment bounds are the quantitative replacement for the qualitative uniform-integrability step in the `0906Z` theorem.

---

## 4. Explicit `W_{3/2}` contraction and escape-scale Lipschitz constant

Use the sharp Pinelis von Bahr–Esseen constant at exponent `3/2`,

\[
C_*:=\sqrt{1+\frac1{\sqrt2}}<1.307.
\]

For this law, the child-sum coefficient is

\[
\alpha:=\left(1+\frac{C_*}{2}\right)^{2/3}<1.399.
\tag{4.1}
\]

For two parameters `delta,eta` in `(0,1/200]`, optimally couple `X_delta,X_eta` and independently repeat the coupling across children. Put

\[
w:=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)),
\qquad
h:=|\delta-\eta|,
\qquad
R:=|r_\delta-r_\eta|.
\]

The sharp centered-sum inequality gives

\[
\|Y_\delta-Y_\eta\|_{3/2}\le \alpha w.
\tag{4.2}
\]

Let

\[
F_{\delta,r}(y)=\frac{y}{3/2-\delta+\delta r y}.
\]

Since `3/2-delta>=1.495`,

\[
|\partial_yF|\le\frac1{1.495}.
\]

Using (3.8), `r<=2/3`, and the exact parameter derivatives gives the outward-rounded bounds

\[
\|\partial_\delta F(Y)\|_{3/2}<1.915,
\qquad
\|\partial_rF(Y)\|_{3/2}<0.00851.
\]

Therefore

\[
\boxed{
w\le 0.936\,w+1.915\,h+0.00851\,R.}
\tag{4.3}
\]

The exact scalar identity is

\[
\boxed{
\frac1{r_\delta}
=E\frac{Y_\delta^2}
{3/2-\delta+\delta r_\delta Y_\delta}.}
\tag{4.4}
\]

For

\[
\psi_{\delta,r}(y)=
\frac{y^2}{3/2-\delta+\delta r y},
\]

one has

\[
|\partial_y\psi(y)|
\le \frac{2y}{1.495}.
\]

Integrating this derivative between two child sums and applying Holder with exponents `3` and `3/2`, (3.8) and (4.2) give a law-change coefficient below `3.65`. The parameter derivatives give the outward-rounded bounds

\[
E|\partial_\delta\psi(Y)|<3.572,
\qquad
E|\partial_r\psi(Y)|<0.01658.
\]

Since `r_delta,r_eta<=2/3`,

\[
R
\le\frac49\,\left|r_\delta^{-1}-r_\eta^{-1}\right|,
\]

so, after absorbing the `R` term,

\[
\boxed{
R\le1.635\,w+1.600\,h.}
\tag{4.5}
\]

Substituting (4.5) into (4.3), the coefficient of `w` is below `0.950`. Hence

\[
\boxed{
w<38.6\,h,}
\tag{4.6}
\]

and then

\[
\boxed{
R<64.6\,h.}
\tag{4.7}
\]

Thus the qualitative normalized contraction from `0906Z` has an explicit constant on the entire strip `0<delta<=1/200`.

---

## 5. Exact two-degree branch-addition coordinate

For this law it is better not to differentiate the full Aidekon tilt directly. Put

\[
a:=m-1=\frac12,
\]

and, for `n=1,2`,

\[
D_{n,\delta}
:=a-\delta+\delta r_\delta
\sum_{i=0}^{n}X_{\delta,i},
\qquad
h_n(\delta):=E\frac{X_{\delta,0}}{D_{n,\delta}}.
\tag{5.1}
\]

Adding the third branch gives exactly

\[
\boxed{
h_1-h_2=e_\delta g_1,}
\tag{5.2}
\]

where

\[
g_1(\delta)
:=E\frac{X_{\delta,0}X_{\delta,2}}
{D_{1,\delta}D_{2,\delta}}>0.
\tag{5.3}
\]

Define the scalar branch-addition coordinate

\[
\boxed{
x_\delta:=\frac{e_\delta g_1}{h_1}
=\frac{\delta r_\delta g_1}{h_1}.}
\tag{5.4}
\]

Then

\[
h_2=h_1(1-x_\delta).
\]

Because the two offspring weights are equal, the Aidekon effective offspring mean is therefore **exactly**

\[
\boxed{
M_\delta
=\frac{h_1+2h_2}{h_1+h_2}
=\frac{3-2x_\delta}{2-x_\delta}.}
\tag{5.5}
\]

This reduces the whole terminal sign problem to controlling one scalar `x_delta`.

---

## 6. Explicit bounds for `h_1`, `g_1`, and the Lipschitz slope of `x_delta`

Throughout the strip,

\[
a-\delta\ge0.495.
\]

First, using

\[
\frac1{a+u}\ge\frac1a-\frac{u}{a^2},
\]

(3.4) and (3.6),

\[
\begin{aligned}
h_1
&\ge 2-4\delta r_\delta E[X_0(X_0+X_1)]\\
&\ge2-4\left(\frac1{200}\right)\left(\frac23\right)(1.361+1)
>1.968.
\end{aligned}
\tag{6.1}
\]

Also, independence of `X_0,X_2` gives

\[
\boxed{
g_1\le \frac1{0.495^2}<4.082.}
\tag{6.2}
\]

Consequently

\[
\boxed{0\le x_\delta<0.007.}
\tag{6.3}
\]

Now compare two parameters using the same coordinatewise optimal couplings as in Section 4. For

\[
\Phi(x_0,x_1)=
\frac{x_0}{a-\delta+\delta r(x_0+x_1)},
\]

the coordinate and parameter derivative bounds, together with (3.6), (4.6), and (4.7), give

\[
\boxed{|h_1(\delta)-h_1(\eta)|<92.2\,h.}
\tag{6.4}
\]

For completeness, the rounded constants used here are

\[
|\partial_{x_0}\Phi|\le 0.495^{-1},
\]

and after averaging the `x_1`, `delta`, and `r` derivatives their coefficients are respectively below

\[
0.0137,\qquad10.51,\qquad0.0482.
\]

Next consider

\[
\Psi(x_0,x_1,x_2)
=\frac{x_0x_2}{D_1D_2}.
\]

The three coordinate derivatives have total `L^3` coefficient below `10.88`; the `delta` and `r` derivative expectations are below `50` and `0.251`, respectively. These bounds use only `EX^3<2.217` and the denominator floor `0.495`. Combining with (4.6)–(4.7) yields

\[
\boxed{|g_1(\delta)-g_1(\eta)|<487\,h.}
\tag{6.5}
\]

Finally apply the product/quotient decomposition to

\[
x_\delta=\delta r_\delta g_1(\delta)/h_1(\delta).
\]

Using (3.4), (6.1), (6.2), (4.7), (6.4), and (6.5),

\[
\begin{aligned}
|x_\delta-x_\eta|
&\le h\,\frac{(2/3)4.082}{1.968}
+\frac1{200}(64.6)h\,\frac{4.082}{1.968}\\
&\quad+\frac1{200}\frac23(487)h\,\frac1{1.968}
+\frac1{200}\frac23(4.082)(92.2)h\,\frac1{1.968^2}\\
&<3.202\,h.
\end{aligned}
\tag{6.6}
\]

Hence

\[
\boxed{
|x_\delta-x_\eta|<3.202|\delta-\eta|.}
\tag{6.7}
\]

This is the quantitative scalar control that the preceding qualitative terminal theorem did not provide.

---

## 7. Speed monotonicity with a numerical margin

By Aidekon's exact speed representation,

\[
\ell_{3/2-\delta}
=\frac{M_\delta-(3/2-\delta)}
{M_\delta+(3/2-\delta)},
\tag{7.1}
\]

with `M_delta` given by (5.5). Regard the right side as a smooth function `L(delta,x)` on

\[
0<\delta\le1/200,
\qquad 0\le x<0.007.
\]

From (5.5),

\[
M(x)=\frac{3-2x}{2-x},
\qquad
M'(x)=-\frac1{(2-x)^2}.
\]

The bounds `x<0.007` imply

\[
M(x)>1.498.
\tag{7.2}
\]

At fixed `x`,

\[
\partial_\delta L
=\frac{2M}{(M+\lambda)^2}
>\frac{2(1.498)}{3^2}
>0.3328.
\tag{7.3}
\]

At fixed `delta`,

\[
|\partial_xL|
=\frac{2\lambda}{(M+\lambda)^2(2-x)^2}.
\]

Here

\[
\lambda\le1.5,
\quad
M+\lambda>1.498+1.495=2.993,
\quad
2-x>1.993,
\]

so

\[
\boxed{|\partial_xL|<0.08432.}
\tag{7.4}
\]

Take `0<delta_1<delta_2<=1/200`. Use the rectangle decomposition in `(delta,x)` and (6.7):

\[
\begin{aligned}
L(\delta_2,x_{\delta_2})-L(\delta_1,x_{\delta_1})
&\ge 0.3328(\delta_2-\delta_1)
-0.08432|x_{\delta_2}-x_{\delta_1}|\\
&>\bigl(0.3328-0.08432\cdot3.202\bigr)
(\delta_2-\delta_1)\\
&>0.062(\delta_2-\delta_1).
\end{aligned}
\tag{7.5}
\]

Because `lambda=3/2-delta`, (7.5) is exactly (2.3). This proves Theorem 2.1.

No differentiation of an uncontrolled `o(delta)` remainder is used anywhere in this final sign argument.

---

## 8. What changed, what did not, and next attack

### New proved partial result

The prior terminal theorem said only that some law-dependent `epsilon>0` exists. For the balanced `{1,2}` law, this run proves the explicit interval

\[
\boxed{1.495\le\lambda<1.5}
\]

with a uniform secant margin greater than `0.062`.

This is a genuine minimum-offspring-one result in a parent-bias region far above the old source-uniform `lambda<=1/2` baseline. It does **not** close the large middle gap.

### Full-source status

`R_full: 1 -> 1`.

The full conjecture is not solved. This theorem is for one fixed nondegenerate offspring law and only a terminal subinterval.

### Exact remaining gap for this law

For

\[
P(\nu=1)=P(\nu=2)=1/2,
\]

the present repository certificates now include the broad old low-bias baseline through `lambda=1/2` and the explicit terminal strip `[299/200,3/2)`. The unresolved middle interval is therefore still substantial:

\[
\boxed{\frac12<\lambda<\frac{299}{200}.}
\]

### Next analytic attack

The calculation above was intentionally organized so that the only law-specific inputs are `m`, the first three offspring factorial moments, the Pinelis child-sum coefficient, and the two degree weights in the final Aidekon tilt. The next useful step is therefore **not** another qualitative critical theorem. It is to keep `p` symbolic for

\[
P(\nu=1)=1-p,
\qquad P(\nu=2)=p,
\]

and obtain a uniform explicit terminal width for a nontrivial interval of mixture weights, for example `2/5<=p<=3/5`. After that, combine the symbolic branch-addition coordinate with the minimum-one low-bias score inequalities already present elsewhere in the repository, rather than duplicating P03-B's coupling route.

If that uniformization fails twice because the constants explode at an endpoint, the productive pivot is to replace the crude coordinatewise `g_1` derivative bound by the exact same-law covariance of `g_1/h_1`; that is where most of the current numerical loss enters.

---

## 9. Delivery note

This report is intended as an immutable P03-A proof checkpoint under the owner-directed progress-first policy. It preserves prior reports and claims no publication, public posting, email, Drive delivery, force-push, or overwrite of peer history.
