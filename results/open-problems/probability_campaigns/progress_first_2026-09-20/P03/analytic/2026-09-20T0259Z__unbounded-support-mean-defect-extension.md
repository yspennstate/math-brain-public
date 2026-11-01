Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — escape-tilt stochastic domination and an unbounded-support mean-defect extension

**Status:** PROVED PARTIAL (new repository theorem candidate, not independently audited; no claim of external novelty; the full Lyons–Pemantle–Peres conjecture remains open).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, complementary analytic recursive/derivative role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `29285fe940b1721fbc836b152519a888f8cd29ee`.

## 1. Source convention, assumptions, current baseline, and inherited work

Let `nu` be the Galton–Watson offspring variable. The source problem assumes a supercritical Galton–Watson tree without leaves,

\[
P(\nu=0)=0,
\]

and asks for monotonicity of the speed throughout the transient regime. Ben Arous–Fribergh–Sidoravicius use the outward child-bias `beta`,

\[
P_\beta(x,x^*)=\frac1{1+\beta\nu(x)},\qquad
P_\beta(x,x_i)=\frac\beta{1+\beta\nu(x)}.
\]

I use the reciprocal parent-bias parameter

\[
\lambda=1/\beta,
\]

so

\[
P_\lambda(x,x^*)=\frac\lambda{\lambda+\nu(x)},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)}.
\]

The conjectural direction is that the speed `ell_lambda` is nonincreasing as `lambda` grows.

Primary references checked for continuity are:

* Ben Arous, Fribergh and Sidoravicius, arXiv:1111.5865, proving the old high-outward-bias result `beta>=717`;
* Bowditch and Tokushige, arXiv:1906.07913 and arXiv:2006.03433, proving differentiability / analyticity in ballistic regimes but not the derivative sign;
* Song, Wang and Xiang, *Journal of Applied Probability* 62 (2025), DOI `10.1017/jpr.2024.113`, currently the source-uniform monotonicity baseline used here: if the minimum offspring is `d>=2`, then strict parent-bias decrease holds for

\[
0\le\lambda\le
\theta_d:=\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.1}
\]

A fresh bounded literature check on 20 September 2026 did not surface a later source-wide resolution. This is bounded negative evidence, not a novelty certificate.

Repository continuity used rather than re-derived:

* previous P03-A `2026-09-20T0207Z__gini-covariance-and-three-degree-extension.md` proved arbitrary `{2,3,4}` mixtures through `lambda=7/4` and arbitrary `{2,3,4,5}` mixtures through `31/20`, using the exact effective-degree derivative identity and a Gini covariance decomposition;
* P03-B `2026-09-20T0217Z__occupation-debt-and-interface-obstruction.md` develops the distinct coupling/occupation route and proves that a naive pointwise response-sign mechanism is false; I do not duplicate it;
* NM13-05 `2026-09-20T02-34-00Z__rare-extra-child-nearcritical-d3.md` gives a complementary rare-defect `{3,4}` theorem near `lambda=3`, based on branch-addition and endpoint-mixture compression.

The fixed full-source metric remains

`R_full: 1 -> 1`.

The goal of this run is different from the preceding bounded-support results: **remove the upper-support restriction entirely** for a quantitative near-regular class.

## 2. Inherited exact speed derivative identity

Assume for this report that

\[
\nu\ge d\quad\text{a.s.},\qquad d\ge2,
\tag{2.1}
\]

and initially fix `1<=lambda<d`.

Let `B` denote the escape probability from a vertex before hitting its parent. Conditional on the current vertex having `n` children, let `B_0,...,B_n` be iid copies of `B`, put

\[
S_n=\sum_{i=0}^n B_i,
\qquad A_n=\lambda-1+S_n,
\]

and define

\[
c_n(\lambda)
:=E\left[\frac{S_n}{(n+1)A_n}\right].
\tag{2.2}
\]

Writing `p_n=P(nu=n)`, define the escape-tilted offspring law

\[
C=\sum_{n\ge d}p_n c_n,
\qquad
\pi_n=\frac{p_n c_n}{C},
\qquad
M=\sum_{n\ge d}n\pi_n.
\tag{2.3}
\]

Aïdékon's symmetrized speed representation reduces to

\[
\boxed{
\ell_\lambda=\frac{M-\lambda}{M+\lambda}
},
\qquad
\boxed{
\ell_\lambda'=
\frac{2(\lambda M'-M)}{(M+\lambda)^2}
}.
\tag{2.4}
\]

If

\[
g_n:=-\frac{d}{d\lambda}\log c_n,
\tag{2.5}
\]

then differentiating the tilt gives

\[
\boxed{
M'=
-\operatorname{Cov}_\pi(\nu,g_\nu)
=
\sum_{n<m}\pi_n\pi_m(m-n)(g_n-g_m).
}
\tag{2.6}
\]

The previous P03-A reports established, using the standard escape derivative estimate, the uniform bound

\[
0\le g_n\le
\frac{d-1}
{(d-\lambda)\,[\lambda-1+(n+1)(1-\lambda/d)]}.
\tag{2.7}
\]

In particular

\[
0\le g_n\le U_d(\lambda),
\qquad
U_d(\lambda):=
\frac{d-1}{(d-\lambda)(d-\lambda/d)}.
\tag{2.8}
\]

The new work starts by exploiting a structural fact about the weights `c_n` that had only been used locally in two-point families.

## 3. New lemma: the escape tilt stochastically lowers offspring degree

For `lambda>1`, define

\[
\phi_\lambda(s)=\frac{s}{\lambda-1+s},\qquad s\ge0.
\tag{3.1}
\]

This function is increasing, concave, and satisfies `phi_lambda(0)=0`. If `S_r=B_1+...+B_r`, then

\[
c_n=\frac1{n+1}E\phi_\lambda(S_{n+1}).
\tag{3.2}
\]

### Lemma 3.1 — branch-addition ratio for every degree

For every `n>=d`,

\[
\boxed{
\frac{n+1}{n+2}
\le
\frac{c_{n+1}}{c_n}
\le1.
}
\tag{3.3}
\]

#### Proof

Because `phi_lambda` is increasing and `S_{n+2}>=S_{n+1}` under the natural iid coupling,

\[
E\phi_\lambda(S_{n+2})
\ge E\phi_\lambda(S_{n+1}),
\]

which gives the lower ratio in (3.3).

For the upper ratio, fix nonnegative `x_1,...,x_{n+2}` with total `S>0`. Concavity and `phi(0)=0` imply

\[
\phi(S-x_i)
\ge \left(1-\frac{x_i}{S}\right)\phi(S).
\]

Summing over `i=1,...,n+2` gives

\[
\sum_{i=1}^{n+2}\phi(S-x_i)
\ge(n+1)\phi(S).
\]

For iid `B_i`, every leave-one-out sum has the law of `S_{n+1}`. Hence

\[
(n+2)E\phi(S_{n+1})
\ge(n+1)E\phi(S_{n+2}),
\]

which is exactly `c_{n+1}<=c_n`.

At `lambda=1`, because `d>=2` and `lambda<d`, escape is positive and `phi_1(S_r)=1`; thus `c_n=1/(n+1)`, so (3.3) holds by continuity (indeed with equality at the lower bound). QED.

### Corollary 3.2 — stochastic domination of the tilted degree

Because `n -> c_n` is nonincreasing, the likelihood ratio `pi_n/p_n` is nonincreasing. Therefore the escape-tilted offspring variable `N~pi` is stochastically dominated by the original offspring variable `nu~p`.

More explicitly, for every increasing function `f` for which the expectations exist,

\[
\boxed{
E_\pi f(N)\le E f(\nu).
}
\tag{3.4}
\]

Indeed, if `nu,nu'` are iid under `p`, then

\[
2\operatorname{Cov}_p(f(\nu),c_\nu)
=
E[(f(\nu)-f(\nu'))(c_\nu-c_{\nu'})]\le0,
\]

because `f` increases while `c_n` decreases. Dividing by `Ec_\nu` gives (3.4).

In particular, if

\[
\mu:=E\nu<\infty,
\tag{3.5}
\]

then

\[
\boxed{d\le M\le\mu.}
\tag{3.6}
\]

This is the first main mechanism of the run. High-degree vertices are not amplified by Aïdékon's escape tilt; they are systematically downweighted.

## 4. New unbounded-support covariance bound

Define the tilted Gini dispersion

\[
G(\pi)=\sum_{n<m}\pi_n\pi_m(m-n)
=\frac12E|N-N'|,
\tag{4.1}
\]

where `N,N'` are iid under `pi`.

No upper support bound is needed for the following estimate. Since `n>=d`, for each pair `n<m`,

\[
m-n\le m-d.
\]

Therefore

\[
\boxed{
G(\pi)
\le
\sum_m\pi_m(m-d)
\sum_{n<m}\pi_n
\le M-d.
}
\tag{4.2}
\]

Using (2.6), `g_m>=0`, and `g_n<=U_d(lambda)`,

\[
M'
\le U_d(\lambda)G(\pi)
\le U_d(\lambda)(M-d).
\tag{4.3}
\]

Set

\[
a_d(\lambda)
:=\lambda U_d(\lambda)
=
\frac{\lambda(d-1)}{(d-\lambda)(d-\lambda/d)}.
\tag{4.4}
\]

Then

\[
\boxed{
\lambda M'-M
\le
(a_d(\lambda)-1)M-a_d(\lambda)d.
}
\tag{4.5}
\]

This inequality is the second main mechanism of the run. It turns the full derivative sign into a one-dimensional comparison involving only minimum degree and the escape-tilted mean.

### Analytic legitimacy for unbounded support

The preceding formula is not merely a formal extension from finite support. On any compact interval `1<=lambda<=L<d`, (2.8) gives a uniform constant `U_d(L)`. Also, since `0<phi_lambda<=1`,

\[
0<c_n\le\frac1{n+1},
\]

and from `-c_n'=c_ng_n`,

\[
|c_n'|\le\frac{U_d(L)}{n+1}.
\]

Hence

\[
\sum_n p_n|c_n'|<\infty,
\qquad
\sum_n p_n n|c_n'|\le U_d(L)<\infty.
\]

Thus the numerator and denominator defining `M` may be differentiated termwise by dominated convergence on compact subintervals of `[1,d)`, even when the offspring support is unbounded. The covariance series in (2.6) is absolutely controlled by (4.2)--(4.3) once `M<infty`; under (3.5), `M<=mu<infty` by Corollary 3.2.

## 5. Main new theorem: finite-mean laws get an explicit extension beyond the source-uniform cutoff

The function `a_d(lambda)` is strictly increasing on `[1,d)`. Its equation

\[
a_d(\lambda)=1
\]

has its smaller root exactly at

\[
\lambda=\theta_d
=\frac{d}{1+\sqrt{1-1/d}},
\tag{5.1}
\]

which is the Song--Wang--Xiang source-uniform endpoint.

This shows that the published cutoff is precisely the point at which the crude source-uniform estimate (4.5) loses sign if no information beyond `M>=d` is used. Corollary 3.2 supplies the missing extra information `M<=mu`.

### Theorem 5.1 — unbounded-support near-regular mean criterion

Assume

\[
P(\nu\ge d)=1,\qquad d\ge2,\qquad \mu=E\nu<\infty.
\tag{5.2}
\]

Fix `L` with

\[
1<L<d.
\]

Let

\[
A:=a_d(L)
=
\frac{L(d-1)}{(d-L)(d-L/d)}.
\tag{5.3}
\]

If `A<=1`, then (4.5) already has negative right-hand side for all tilted means `M>=d`.

If `A>1` and

\[
\boxed{
\mu<\mu_{\rm crit}(d,L)
:=\frac{dA}{A-1}
=
\frac{L d^2(d-1)}{2Ld^2-L^2-d^3},
}
\tag{5.4}
\]

then

\[
\boxed{
\ell_\lambda'<0
\quad\text{for every }1\le\lambda\le L.
}
\tag{5.5}
\]

Combining with the published theorem (1.1) yields strict monotonicity on the whole interval

\[
\boxed{0\le\lambda\le L.}
\tag{5.6}
\]

#### Proof

Because `a_d(lambda)` increases,

\[
a_d(\lambda)\le A
\qquad(1\le\lambda\le L).
\]

If `A<=1`, then from (4.5), using `M>=d`,

\[
\lambda M'-M
\le(A-1)M-Ad
\le(A-1)d-Ad=-d<0.
\]

Now suppose `A>1`. Corollary 3.2 gives `M<=mu`, so

\[
\lambda M'-M
\le(A-1)M-Ad
\le(A-1)\mu-Ad.
\]

The last quantity is strictly negative exactly under (5.4). Equation (2.4) then gives `ell'_lambda<0` on `[1,L]`. The interval `[0,theta_d]` is supplied by Song--Wang--Xiang; since `theta_d>1` for `d>=2`, the intervals overlap. QED.

### Corollary 5.2 — every finite-mean minimum-degree law gets some strict extension

Let `d>=2` and `mu<infty`. If `mu=d`, the law is deterministic `d`-regular and the speed is explicitly monotone throughout `lambda<d`.

If `mu>d`, then

\[
\mu_{\rm crit}(d,L)\to\infty
\qquad\text{as }L\downarrow\theta_d.
\]

Hence there exists an explicit `epsilon(d,mu)>0` such that

\[
\boxed{
\ell_\lambda\text{ is strictly decreasing on }
[0,\theta_d+\epsilon(d,\mu)].
}
\tag{5.7}
\]

Thus the source-uniform 2025 endpoint is not an endpoint for any fixed finite-mean offspring law with minimum degree at least two: the analytic escape tilt supplies a positive law-dependent extension without any finite-support assumption.

For `mu>d`, the maximal endpoint certified by this argument is the smaller root `L_*(d,mu)` of

\[
a_d(L)=\frac\mu{\mu-d},
\]

namely

\[
\boxed{
L_*(d,\mu)=
\frac{
 d^2(2\mu-d+1)
-
\sqrt{d^4(2\mu-d+1)^2-4\mu^2d^3}
}{2\mu}.
}
\tag{5.8}
\]

The theorem proves strict decrease for every `L<L_*(d,mu)`.

## 6. Explicit unbounded-support corollaries

These examples have **no upper offspring cutoff**.

### Corollary 6.1 — minimum degree 2, mean at most 9/4

Take

\[
d=2,\qquad L=\frac95.
\]

Then

\[
A=a_2(9/5)=\frac{90}{11},
\]

so

\[
\mu_{\rm crit}(2,9/5)
=\frac{180}{79}
\approx2.278481.
\]

Therefore every offspring law satisfying

\[
\boxed{
\nu\ge2\text{ a.s.},\qquad E\nu\le\frac94
}
\tag{6.1}
\]

— with arbitrary finite or infinite support — has strictly decreasing speed on

\[
\boxed{0\le\lambda\le\frac95=1.8.}
\tag{6.2}
\]

In the original child-bias convention this gives strict increase for

\[
\beta\ge\frac59.
\]

The published minimum-degree-2 source-uniform endpoint is `4-2sqrt(2)≈1.17157`, so this is a substantial extension for a broad unbounded-support class.

### Corollary 6.2 — minimum degree 2, mean at most 21/10

Take

\[
d=2,\qquad L=\frac{19}{10}.
\]

Then

\[
A=\frac{380}{21},
\qquad
\mu_{\rm crit}(2,19/10)=\frac{760}{359}
\approx2.11699.
\]

Hence every offspring law with

\[
\boxed{
\nu\ge2\text{ a.s.},\qquad E\nu\le\frac{21}{10}
}
\tag{6.3}
\]

has strictly decreasing speed throughout

\[
\boxed{0\le\lambda\le\frac{19}{10}=1.9.}
\tag{6.4}
\]

Again there is no support-width assumption.

### Corollary 6.3 — minimum degree 3, mean at most 31/10

Take

\[
d=3,\qquad L=\frac{29}{10}.
\]

Then

\[
A=\frac{1740}{61},
\qquad
\mu_{\rm crit}(3,29/10)=\frac{5220}{1679}
\approx3.10899.
\]

Therefore every offspring law satisfying

\[
\boxed{
\nu\ge3\text{ a.s.},\qquad E\nu\le\frac{31}{10}
}
\tag{6.5}
\]

has strictly decreasing speed on

\[
\boxed{0\le\lambda\le\frac{29}{10}=2.9.}
\tag{6.6}
\]

This complements NM13-05's near-`3` rare-defect `{3,4}` result: the present theorem allows **arbitrarily large offspring values** and uses only the first moment, at the price of stopping at `2.9` for the displayed clean mean bound.

## 7. Why this is genuine progress but not the full conjecture

The previous P03-A theorems removed mixture restrictions while retaining bounded support. Theorem 5.1 removes the upper-support restriction entirely and replaces it by a transparent mean-defect condition.

The structural advance is not a decimal endpoint. It is the combination

\[
\boxed{
\text{escape tilt lowers degree stochastically}
\quad+\quad
G(\pi)\le M-d
\quad+\quad
M\le E\nu,
}
\]

which turns the covariance obstruction into a one-parameter mean criterion.

The full source problem remains open for at least three reasons:

1. the theorem assumes minimum offspring `d>=2`, while the original no-leaf problem allows degree one;
2. for fixed `d>=2` and a large mean defect, the bound loses sign well before `lambda=d`;
3. even when `lambda>d`, the inherited escape derivative estimate `(d-lambda)^{-1}` is unavailable, so a qualitatively different argument is required to traverse the rest of the transient interval `lambda<E nu` when the mean exceeds the minimum degree.

The full-source metric therefore remains

`R_full: 1 -> 1`.

The intermediate obligation **did** move: bounded support is no longer needed for an explicit nontrivial extension beyond the current source-uniform interval.

## 8. Failed / deliberately avoided routes and what they teach

* **Do not use a global maximum degree `D`.** That would merely repeat the preceding bounded-support Gini theorem. The new proof avoids `D` completely.
* **Do not try pointwise positivity of the finite-horizon coupling response.** P03-B has already produced a valid source cylinder where that response is negative.
* **Do not replace `M` by the original mean before proving tilt order.** The key inequality `M<=mu` is not formal; it follows from the new monotone-likelihood-ratio property of `c_n`.
* **Do not claim the original degree-one case.** The present derivative cone is built on `lambda<d`, so `d=1` requires a different mechanism.

## 9. Exact remaining gap and next analytic attack

The strongest useful next step is to replace the coarse factor

\[
M'\le U_d(\lambda)(M-d)
\]

by a **degree-conditioned transport inequality** that retains the decay

\[
g_n\lesssim
\frac1{\lambda-1+(n+1)(1-\lambda/d)}
\]

inside the pairwise covariance sum. The present proof uses only the worst value `U_d` at degree `d`; for a heavy upper tail this is wasteful because the same escape tilt that suppresses high degrees also makes their logarithmic sensitivity small.

A concrete next target is to prove an inequality of the schematic form

\[
M'
\le
\sum_{j\ge d}
\alpha_j(\lambda)\,F_j(1-F_j),
\qquad
\alpha_j(\lambda)\downarrow0,
\]

with `F_j=P_pi(N<=j)`, and then use the stochastic domination `pi<=st p` to control the weighted tail sum by one or two ordinary moments of `nu`. That would enlarge the allowable mean defect and may permit controlled laws beyond `lambda=d` only if paired with a new escape-sensitivity estimate not singular at `d`.

The degree-one source case and the full interval remain open; no full solution is claimed.