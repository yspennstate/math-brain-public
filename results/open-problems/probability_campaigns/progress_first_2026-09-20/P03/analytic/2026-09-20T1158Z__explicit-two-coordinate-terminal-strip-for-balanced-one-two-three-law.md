Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. GPT-6 / maximum reasoning was requested, but no authenticated model-effort selector or full-hour guarantee is exposed here, so I do not claim it.

# P03-A analytic proof report — explicit two-coordinate terminal strip for the balanced `{1,2,3}` law

**Status:** PROVED PARTIAL / EXPLICIT RESTRICTED THEOREM CANDIDATE. Not independently audited. The full Lyons–Pemantle–Peres conjecture remains open.

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`. Canonical ownership was already checked on assignment and is not changed here. P03-B retains the distinct regeneration/coupling/path-score role. I consumed its latest `2026-09-20T1120Z__revisit-only-score-decomposition-and-four-step-obstruction.md` only for continuity; none of its path-score work is duplicated below. Old D0047 history is untouched.

**Captured master immediately before this write:** `a1b2b3226fc44f4094a8b4d128a06e5419060c7d`.

**Inherited analytic checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T1106Z__uniform-explicit-terminal-strip-for-all-one-two-mixtures.md`.

That report made the terminal interval explicit for every `{1,2}` mixture. The new obligation was to replace the one branch-addition coordinate by the first genuinely two-coordinate system. This run does that for the balanced three-degree law and obtains a completely explicit terminal interval and secant margin.

The fixed source-level metric remains

`R_full: 1 -> 1`.

The intermediate obligation does move: explicit terminal monotonicity now covers a law with three offspring values and two independent branch-addition coordinates, rather than only a two-point family.

---

## 1. Convention and current source benchmark

At a non-root vertex with `k` children I use reciprocal **parent bias** `lambda`,

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+k}.
\]

Thus the original outward child-bias parameter is `beta=1/lambda`; increasing `lambda` means weaker outward bias. If `m=E nu`, the transient interval is `0<=lambda<m`, and the LPP conjecture asks that the speed `ell_lambda` be nonincreasing in `lambda` throughout that interval.

Primary partial-result source: G. Ben Arous, A. Fribergh and V. Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865.

A bounded current source check on 20 September 2026 again recovered He Song, Longmin Wang and Kainan Xiang, *The speed of a biased walk on a Galton-Watson tree without leaves is monotonic for low values of bias*, J. Appl. Probab. 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: when the minimum offspring is `d>=2`, strict decrease holds for

\[
0\le\lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\]

That theorem does not cover the minimum-offspring-one law treated here. Bowditch–Tokushige, arXiv:1906.07913 and arXiv:2006.03433, prove differentiability / analyticity in the corresponding ballistic regimes but do not supply the missing sign. The bounded search did not surface a source-wide resolution. This is negative evidence only, not a novelty certificate.

---

## 2. New theorem

Consider the genuinely three-degree law

\[
\boxed{
P(\nu=1)=P(\nu=2)=P(\nu=3)=\frac13.}
\tag{2.1}
\]

Then

\[
m=E\nu=2,\qquad
f_2=E[\nu(\nu-1)]=\frac83,\qquad
f_3=E[\nu(\nu-1)(\nu-2)]=2.
\tag{2.2}
\]

### Theorem 2.1 — explicit terminal strip for the balanced `{1,2,3}` law

For (2.1), the parent-bias speed is strictly decreasing throughout

\[
\boxed{
\frac{1999}{1000}\le\lambda<2.}
\tag{2.3}
\]

More quantitatively, whenever

\[
\frac{1999}{1000}\le\lambda_1<\lambda_2<2,
\]

one has

\[
\boxed{
\ell_{\lambda_1}-\ell_{\lambda_2}
>0.17\,(\lambda_2-\lambda_1).}
\tag{2.4}
\]

Hence at every differentiability point in the strip,

\[
\ell'_\lambda<-0.17.
\tag{2.5}
\]

The width `10^{-3}` is conservative. The mathematical gain is structural: unlike the `{1,2}` proof, the Aidekon tilt now has two genuinely independent branch-addition coordinates, and the exact speed sign survives their joint variation.

---

## 3. Normalized escape recursion and explicit moments

Write

\[
\delta:=2-\lambda,\qquad 0<\delta\le\varepsilon:=10^{-3}.
\tag{3.1}
\]

Let `B_lambda` be the child-root escape probability from its artificial parent and put

\[
e_\delta:=E B_{2-\delta},\qquad
r_\delta:=\frac{e_\delta}{\delta},\qquad
X_\delta:=\frac{B_{2-\delta}}{e_\delta},
\tag{3.2}
\]

so `E X_delta=1`. With iid copies and

\[
Y_\delta:=\sum_{i=1}^{\nu}X_{\delta,i},
\]

the inherited exact normalized recursion is

\[
\boxed{
X_\delta\stackrel d=
\frac{Y_\delta}{2-\delta+\delta r_\delta Y_\delta}.}
\tag{3.3}
\]

The companion mean identity is

\[
\boxed{
\frac1{r_\delta}
=E\frac{Y_\delta^2}{2-\delta+\delta r_\delta Y_\delta}.}
\tag{3.4}
\]

Concavity gives `e_delta<=delta/m`, hence

\[
0<r_\delta\le\frac12.
\tag{3.5}
\]

The inherited critical-edge theorem gives

\[
\boxed{r_\delta\to\frac{m-1}{f_2}=\frac38}
\qquad(\delta\downarrow0).
\tag{3.6}
\]

Let

\[
s_2=EX_\delta^2,\qquad s_3=EX_\delta^3.
\]

Since the denominator in (3.3) is at least `2-delta>=1.999`,

\[
s_2\le\frac{2s_2+8/3}{(2-\delta)^2},
\]

so

\[
\boxed{s_2<1.337.}
\tag{3.7}
\]

For a random sum of iid mean-one variables,

\[
EY_\delta^3=2s_3+3f_2s_2+f_3
=2s_3+8s_2+2.
\]

Therefore

\[
s_3\le\frac{8s_2+2}{(2-\delta)^3-2},
\]

which, together with (3.7), yields

\[
\boxed{s_3<2.120.}
\tag{3.8}
\]

Consequently, throughout the strip,

\[
\boxed{EY_\delta^2<5.341,\qquad EY_\delta^3<16.94.}
\tag{3.9}
\]

---

## 4. Explicit normalized `W_{3/2}` contraction

Let

\[
C_*:=\sqrt{1+1/\sqrt2}<1.307
\]

be the sharp Pinelis von Bahr–Esseen constant used in the preceding P03-A terminal theorem. For an optimal centered coupling of `X_delta-X_eta`, repeated independently across children, the random-child-sum inequality gives

\[
\|Y_\delta-Y_\eta\|_{3/2}
\le \alpha w,
\qquad
\alpha=(1+C_*)^{2/3}<1.746,
\tag{4.1}
\]

where

\[
w:=W_{3/2}(\mathcal L(X_\delta),\mathcal L(X_\eta)).
\]

Indeed one may write the random sum as its first centered increment plus the remaining stopped martingale differences; because `E nu=2`, Pinelis gives the factor `1+C_*` at the `3/2`-moment level.

Put `h=|delta-eta|` and `R=|r_delta-r_eta|`. For

\[
F_{\delta,r}(y)=\frac{y}{2-\delta+\delta r y},
\]

(3.9), `r<=1/2`, and `2-delta>=1.999` give the outward-rounded estimates

\[
\frac{\alpha}{2-\delta}<0.874,
\]

\[
\|\partial_\delta F(Y)\|_{3/2}<1.470,
\qquad
\|\partial_rF(Y)\|_{3/2}<0.00166.
\]

Hence

\[
\boxed{
w\le0.874w+1.470h+0.00166R.}
\tag{4.2}
\]

For

\[
\psi_{\delta,r}(y)=\frac{y^2}{2-\delta+\delta r y},
\]

one has

\[
|\psi(y)-\psi(z)|
\le\frac{(y+z)|y-z|}{1.999}.
\]

Using (3.9), (4.1), and the exact parameter derivatives gives

\[
|E\psi(Y_\delta)-E\psi(Y_\eta)|
<4.49w+3.46h+0.00425R.
\]

Since `r_delta r_eta<=1/4`, the scalar identity (3.4) implies

\[
\boxed{R<1.124w+0.867h.}
\tag{4.3}
\]

Substitution into (4.2) therefore yields the clean explicit pair

\[
\boxed{w<12h,\qquad R<14.4h.}
\tag{4.4}
\]

Letting `eta downarrow0` and using (3.6),

\[
\boxed{
0<r_\delta<\frac38+14.4(10^{-3})<0.39.}
\tag{4.5}
\]

This sharper bootstrap is used below.

---

## 5. Exact two-coordinate Aidekon tilt

Here `m-1=1`. For `n=1,2,3`, define

\[
D_{n,\delta}
:=1-\delta+\delta r_\delta\sum_{i=0}^{n}X_{\delta,i},
\qquad
h_n(\delta):=E\frac{X_{\delta,0}}{D_{n,\delta}}.
\tag{5.1}
\]

For `n=1,2`, put

\[
g_n(\delta)
:=E\frac{X_{\delta,0}X_{\delta,n+1}}
{D_{n,\delta}D_{n+1,\delta}}.
\tag{5.2}
\]

Adding one branch gives the exact telescoping identities

\[
\boxed{h_1-h_2=e_\delta g_1,\qquad h_2-h_3=e_\delta g_2.}
\tag{5.3}
\]

Define two branch-addition coordinates

\[
\boxed{
x_1:=\frac{e_\delta g_1}{h_1},\qquad
x_2:=\frac{e_\delta g_2}{h_1}.}
\tag{5.4}
\]

Then

\[
h_2=h_1(1-x_1),\qquad
h_3=h_1(1-x_1-x_2).
\tag{5.5}
\]

The inherited Aidekon speed representation uses the escape-tilted effective offspring mean

\[
M_\delta=
\frac{\sum_n n p_n h_n}{\sum_n p_n h_n}.
\]

For the balanced law (2.1), (5.5) simplifies exactly to

\[
\boxed{
M_\delta
=2-q_\delta,
\qquad
q_\delta=
\frac{x_1+x_2}
{3\left(1-\frac23x_1-\frac13x_2\right)}.}
\tag{5.6}
\]

This is the new structural reduction. The previous `{1,2}` family had only one scalar `x`; here the entire environment-seen-from-the-walk correction is an explicit rational function of two branch-addition coordinates.

---

## 6. Explicit Lipschitz control of both coordinates

Because `D_{n,delta}>=1-delta>=0.999`, (4.5) and (3.7) give

\[
\begin{aligned}
h_1
&\ge E\left[X_0\{1+\delta-\delta r(X_0+X_1)\}\right]\\
&=1+\delta-\delta r(s_2+1)\\
&>1.
\end{aligned}
\tag{6.1}
\]

Also independence of the newly added branch gives

\[
\boxed{0<g_1,g_2<\frac1{0.999^2}<1.003.}
\tag{6.2}
\]

Therefore

\[
\boxed{0\le x_1,x_2<0.000392.}
\tag{6.3}
\]

We now compare two parameters using the coordinatewise optimal coupling from Section 4.

For

\[
\Phi(x_0,x_1)=
\frac{x_0}{1-\delta+\delta r(x_0+x_1)},
\]

the coordinate derivatives, parameter derivatives, (3.7), (4.4), and (4.5) give

\[
|h_1(\delta)-h_1(\eta)|<14.1h.
\tag{6.4}
\]

The outward-rounded constants behind (6.4) are:

- law-change coefficient `<1.002` multiplying `w`;
- direct `delta` coefficient `<1.916`;
- `r` coefficient `<0.00235`.

Thus (4.4) gives less than `1.002*12+1.916+0.00235*14.4<14.1`.

For `g_n`, differentiate

\[
G_n=\frac{x_0x_{n+1}}{D_nD_{n+1}}.
\]

The two numerator coordinates contribute `<2.008 w`. All denominator-coordinate terms carry the small factor `delta r`; using `EX^3<2.120` keeps their total within the same bound. For the worst case `n=2`,

\[
E[X_0X_3(S_2+S_3)]
=3s_2+4<8.011.
\]

Hence the direct parameter bounds are `<5.14 h` and `<0.00804 R`. Therefore

\[
\boxed{|g_n(\delta)-g_n(\eta)|<29.5h,
\qquad n=1,2.}
\tag{6.5}
\]

Finally

\[
|\delta r_\delta-\eta r_\eta|
\le0.39h+10^{-3}R<0.405h.
\]

Using (6.1)–(6.5) in `x_n=delta r g_n/h_1` yields, for each coordinate,

\[
\boxed{|x_n(\delta)-x_n(\eta)|<0.423h,
\qquad n=1,2.}
\tag{6.6}
\]

The important point is that the two coordinates do not introduce a singular factor: both have a uniform slope substantially below one.

---

## 7. Speed sign with an explicit margin

Set

\[
Z:=1-\frac23x_1-\frac13x_2.
\]

By (6.3),

\[
Z>0.999608,
\qquad
0\le q_\delta<0.000261.
\tag{7.1}
\]

Differentiating the rational function in (5.6) with respect to its two coordinates gives

\[
\frac{\partial q}{\partial x_1}
=\frac{Z+\frac23(x_1+x_2)}{3Z^2},
\qquad
\frac{\partial q}{\partial x_2}
=\frac{Z+\frac13(x_1+x_2)}{3Z^2}.
\]

On the present rectangle each derivative is `<0.334`. Therefore (6.6) implies

\[
\boxed{|q_\delta-q_\eta|<0.283|\delta-\eta|.}
\tag{7.2}
\]

Aidekon's exact speed formula is

\[
\ell_{2-\delta}
=\frac{M_\delta-(2-\delta)}{M_\delta+(2-\delta)}
=\frac{\delta-q_\delta}{4-\delta-q_\delta}.
\tag{7.3}
\]

For the two-variable function

\[
L(\delta,q)=\frac{\delta-q}{4-\delta-q},
\]

(7.1) gives throughout the strip

\[
\frac{\partial L}{\partial\delta}>0.24996,
\qquad
\left|\frac{\partial L}{\partial q}\right|<0.25017.
\tag{7.4}
\]

Hence, for `0<eta<delta<=10^{-3}`,

\[
\begin{aligned}
\ell_{2-\delta}-\ell_{2-\eta}
&\ge 0.24996(\delta-\eta)
 -0.25017|q_\delta-q_\eta|\\
&>\left(0.24996-0.25017\cdot0.283\right)(\delta-\eta)\\
&>0.17(\delta-\eta).
\end{aligned}
\tag{7.5}
\]

This proves Theorem 2.1.

---

## 8. What changed and what remains

### New proved intermediate obligation

The terminal critical-edge program now handles a genuinely three-degree minimum-offspring-one law with an explicit width and derivative/secant margin:

\[
P(\nu=1)=P(\nu=2)=P(\nu=3)=1/3,
\qquad
1.999\le\lambda<2.
\]

The reduction (5.6) is reusable: for a general law on `{1,2,3}`, the same two branch-addition coordinates satisfy

\[
M=m-
\frac{p_1(p_2+2p_3)x_1+p_3(2p_1+p_2)x_2}
{1-(p_2+p_3)x_1-p_3x_2}.
\tag{8.1}
\]

Thus the next generalization is not conceptually blocked by a new formula; it is a matter of making the contraction and coordinate constants uniform as the probabilities approach faces of the simplex. On the `{1,2}` face, the previous `1106Z` theorem already supplies the needed scaled width.

### Full-source gap

The full-source metric remains

`R_full: 1 -> 1`.

This report proves only a terminal interval for one three-degree law. It does **not** prove the whole transient interval, arbitrary `{1,2,3}` mixtures, arbitrary no-leaf laws, or the full LPP conjecture. For the balanced law there remains a large middle interval between inherited low-bias results and `lambda=1.999`.

### Next attack

Use the exact general formula (8.1) to cover a compact simplex, for example

\[
p_i\ge1/5,\qquad p_1+p_2+p_3=1,
\]

with one uniform explicit terminal width. Then combine that compact-simplex theorem with the existing `{1,2}` face scaling and analogous `{1,3}` / `{2,3}` face estimates. The objective is an explicit terminal width for **every** nondegenerate law supported on `{1,2,3}` before introducing an unbounded tail.

No email, Drive, publication action, force-push, historical overwrite, or peer overwrite is part of this report.