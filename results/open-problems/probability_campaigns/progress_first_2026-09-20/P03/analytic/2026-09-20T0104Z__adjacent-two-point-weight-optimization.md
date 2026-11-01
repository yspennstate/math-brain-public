Model actually run: GPT-5.6 Sol; reasoning level UNVERIFIED. This was not GPT-6 at maximum, and I do not claim otherwise.

# P03-A analytic proof report — remove the small-mixture restriction and optimize adjacent two-point offspring laws

**Status:** PROVED PARTIAL (new repository theorem candidate, not independently audited; no claim of external novelty and not a full-source solution).

**Native role:** P03-A, `6aa7b398af30819181ca50ba3c4e6c33`, analytic recursive/derivative role under `operations/progress_first_2026-09-20/REGISTRY.md`.

**Captured master immediately before write:** `5414128ca3334011a57206342bb0d8854b103050`.

## 1. Continuity, source convention, and complementary ownership

The source problem is the Lyons–Pemantle–Peres monotonicity conjecture for biased random walk on a supercritical Galton–Watson tree without leaves. I use the parent/inward-bias convention

\[
P_\lambda(x,x^*)=\frac{\lambda}{\lambda+\nu(x)},\qquad
P_\lambda(x,x_i)=\frac1{\lambda+\nu(x)}.
\]

Thus larger `lambda` means stronger bias toward the root, and the conjecture asks that the speed `ell_lambda` be nonincreasing on the transient interval `0<=lambda<E nu` under `P(nu=0)=0`.

The strongest current source-uniform interval recovered remains Song--Wang--Xiang (J. Appl. Probab. 62 (2025), arXiv:1610.08151): if the minimum offspring is `d>=2`, then `ell_lambda` is strictly decreasing on

\[
0\le\lambda\le \theta_d:=\frac{d}{1+\sqrt{1-1/d}}.
\tag{1.1}
\]

Bowditch--Tokushige (arXiv:1906.07913; arXiv:2006.03433) supply differentiability/analyticity in the ballistic regime. Aidekon (arXiv:1111.4313) supplies the exact speed formula.

The current owner registry explicitly assigns P03-A and P03-B as complementary roles. I checked the current repository ownership/search state once this run: other P0066 workers exist, but no exclusive canonical claim is taken here. P03-B's current report proves a common-regeneration debt criterion and, importantly, rules out universal pathwise radial ordering for infinitesimal bias changes. I therefore do not repeat coupling work.

I also reused, rather than re-derived from scratch, the valid adjacent-two-point derivative bounds in `runs/prob10_2026-09-20/PROB10-06/20260920T0013Z_two_point_escape_derivative_bridge_4f6c2e91.md`. That report proves the needed one-sided ratios but loses sharpness in the last AM--GM step. The new mathematics below is the exact tilted-weight optimization that removes that loss and then a general all-mixture corollary.

The fixed full-source metric remains

`R_full = 1 -> 1`.

## 2. Inherited exact effective-degree reduction

Let `B` be the escape probability from a vertex before hitting its parent, and let `B_0,...,B_k` be iid copies. Put

\[
S_k=\sum_{i=0}^k B_i,
\qquad
D_k=\lambda-1+S_k,
\qquad
c_k(\lambda)=E\left[\frac1{k+1}\frac{S_k}{D_k}\right].
\tag{2.1}
\]

By exchangeability, `c_k` is exactly the previous P03-A quantity `a_k=E[B_0/D_k]`.

For an offspring law supported on two adjacent values

\[
P(\nu=d)=1-p,\qquad P(\nu=d+1)=p,
\qquad d\ge2,\quad 0\le p\le1,
\tag{2.2}
\]

define

\[
C=(1-p)c_d+pc_{d+1},
\qquad
\theta=\frac{pc_{d+1}}{C}.
\tag{2.3}
\]

Aidekon's formula then reduces exactly to

\[
M(\lambda)=\frac{d(1-p)c_d+(d+1)pc_{d+1}}{C}=d+\theta,
\tag{2.4}
\]

\[
\boxed{\ell_\lambda=\frac{M-\lambda}{M+\lambda}},
\qquad
\boxed{\ell_\lambda'=\frac{2(\lambda M'-M)}{(M+\lambda)^2}}.
\tag{2.5}
\]

Thus it is enough to prove `lambda M'<M`.

## 3. One-sided adjacent sensitivity bound

Write `U=-B'>=0`. For `1<=lambda<d`, the standard escape/derivative bounds used by Song--Wang--Xiang give

\[
1-\frac\lambda d\le B\le1-\frac\lambda{d+1},
\qquad
0\le U\le\frac{B}{d-\lambda}.
\tag{3.1}
\]

Differentiating (2.1) gives

\[
h_k:=-c_k'
=E\left[\frac1{k+1}
\frac{\sum_{i=0}^k(B_i+(\lambda-1)U_i)}{D_k^2}\right].
\tag{3.2}
\]

The adjacent-two-point estimate already established elsewhere in the repository is

\[
\frac{h_d}{c_d}
\le
\frac{d-1}{(d-\lambda)(d-\lambda/d)},
\tag{3.3}
\]

\[
\frac{h_{d+1}}{c_{d+1}}
\ge
\frac1{d+1-\lambda/(d+1)}.
\tag{3.4}
\]

For completeness, the mechanism is short: (3.3) uses the lower escape bound in `D_d` and `B+(lambda-1)U <= B(d-1)/(d-lambda)`; (3.4) uses `U>=0` and the upper escape bound to upper-bound `D_{d+1}`.

Define the one-sided adjacent log-sensitivity budget

\[
a_d(\lambda):=
\frac{d-1}{(d-\lambda)(d-\lambda/d)}
-
\frac1{d+1-\lambda/(d+1)}.
\tag{3.5}
\]

Since

\[
(\log c_{d+1}-\log c_d)'
=\frac{h_d}{c_d}-\frac{h_{d+1}}{c_{d+1}},
\]

(3.3)--(3.5) imply

\[
(\log c_{d+1}-\log c_d)'\le a_d(\lambda).
\tag{3.6}
\]

The logistic derivative in (2.3) is exact:

\[
\theta'
=\theta(1-\theta)
(\log c_{d+1}-\log c_d)'.
\tag{3.7}
\]

Therefore

\[
\boxed{M'=\theta'\le a_d(\lambda)\theta(1-\theta)}.
\tag{3.8}
\]

This is the point where the previous adjacent-family report used `theta(1-theta)<=1/4` and `M>=d` separately. That loses the correlation between the same `theta` appearing in both sides of the desired inequality.

## 4. New exact tilted-weight optimization

For `0<theta<1`, (2.4) and (3.8) give

\[
\lambda M'-M
\le
\lambda a_d(\lambda)\theta(1-\theta)-(d+\theta).
\tag{4.1}
\]

The exact threshold is therefore

\[
K_d:=\min_{0< t<1}\frac{d+t}{t(1-t)}.
\tag{4.2}
\]

Differentiating the right-hand side shows that the minimizer is

\[
t_d=\sqrt{d(d+1)}-d,
\]

and direct substitution gives

\[
\boxed{K_d=2d+1+2\sqrt{d(d+1)}}.
\tag{4.3}
\]

Hence:

### Theorem 4.1 — adjacent two-point analytic criterion

For the offspring law (2.2), if `1<=lambda<d` and

\[
\boxed{\lambda a_d(\lambda)<K_d},
\tag{4.4}
\]

then `ell'_lambda<0`, uniformly for **every** mixture weight `0<=p<=1`.

For `p=0` or `p=1`, `theta` is an endpoint and `M'=0`, so the conclusion is immediate. For `0<p<1`, (4.1)--(4.3) make the numerator in (2.5) strictly negative.

The old AM--GM sufficient condition was `lambda a_d<4d`. Since

\[
K_d-4d=1-2d+2\sqrt{d(d+1)}>0
\]

(the square difference is `4d(d+1)-(2d-1)^2=8d-1>0`), (4.4) is a strictly stronger criterion for every `d>=2`.

## 5. New broad corollary: all adjacent mixtures through `d-1/4`

The criterion yields a clean source-faithful theorem without any small-mixture assumption.

For `1<=lambda<=d-1/4`, discard the favorable second term in (3.5):

\[
\lambda a_d(\lambda)
<
\frac{\lambda(d-1)}{(d-\lambda)(d-\lambda/d)}.
\tag{5.1}
\]

Using

\[
\lambda\le d-\frac14,
\quad
d-\lambda\ge\frac14,
\quad
d-\frac\lambda d\ge d-1+\frac1{4d},
\]

gives

\[
\lambda a_d(\lambda)
<
\frac{4(d-1/4)(d-1)}{d-1+1/(4d)}
<4d<K_d.
\tag{5.2}
\]

The middle strict inequality is equivalent to

\[
(d-1/4)(d-1)<d(d-1)+1/4,
\]

whose right-minus-left difference is exactly `d/4>0`.

Therefore Theorem 4.1 proves strict decrease on `[1,d-1/4]`. The published source-uniform theorem (1.1) overlaps this interval because `theta_d>1`, and in fact `theta_d<d-1/4` for every `d>=2`.

### Theorem 5.1 — all adjacent two-point offspring mixtures

For every integer `d>=2` and every `0<=p<=1`, if

\[
P(\nu=d)=1-p,\qquad P(\nu=d+1)=p,
\]

then the biased-walk speed is strictly decreasing on

\[
\boxed{0\le\lambda\le d-\frac14}.
\tag{5.3}
\]

For `0<p<1` this is a genuinely random Galton--Watson family. It is a restricted-family theorem, not the full LPP conjecture.

## 6. Sharpening the `{2,3}` family to `lambda=46/25`

For `d=2`, (3.5) simplifies to

\[
a_2(\lambda)
=
\frac{2}{(2-\lambda)(4-\lambda)}
-
\frac3{9-\lambda}.
\tag{6.1}
\]

The first term has derivative

\[
\frac{4(3-\lambda)}{(2-\lambda)^2(4-\lambda)^2}\ge\frac49
\]

on `[1,2)`, whereas the derivative of `3/(9-lambda)` is at most `3/49`. Hence `a_2` is strictly increasing there; since `a_2>0`, so is `lambda a_2(lambda)`.

At the exact rational endpoint

\[
\lambda_0=\frac{46}{25}=1.84,
\]

we have

\[
Q=(2-\lambda_0)(2-\lambda_0/2)=\frac{108}{625},
\qquad
V=3-\lambda_0/3=\frac{179}{75},
\]

and therefore

\[
\lambda_0 a_2(\lambda_0)=\frac{95473}{9666}.
\tag{6.2}
\]

For `d=2`, the exact weight threshold is

\[
K_2=5+2\sqrt6.
\]

The inequality in (4.4) holds at `lambda_0` because

\[
6-\left(\frac{47143}{19332}\right)^2
=\frac{19894895}{373726224}>0,
\]

which is exactly the squared verification that

\[
\frac{95473}{9666}<5+2\sqrt6.
\]

Thus every `{2,3}` mixture, with **no restriction on `p`**, satisfies

\[
\boxed{\ell'_\lambda<0\quad\text{for }0\le\lambda\le\frac{46}{25}}.
\tag{6.3}
\]

This improves two earlier repository checkpoints simultaneously: P03-A's first run required `p<0.093254...` and reached `lambda=3/2`, while PROB10-06 removed the `p` restriction but its coarse AM--GM threshold stopped at approximately `1.811`.

There is also an exact limiting criterion: since `lambda a_2(lambda)` is strictly increasing from `7/24` at `lambda=1` to `+infinity` as `lambda up 2`, there is a unique `Lambda_2 in (1,2)` satisfying

\[
\Lambda_2 a_2(\Lambda_2)=5+2\sqrt6.
\tag{6.4}
\]

Numerical self-check: `Lambda_2 = 1.8402833144...`. The proof therefore covers every `lambda<Lambda_2`; (6.3) is the clean closed rational interval asserted without relying on that decimal.

### Exact uniform derivative margin on the closed interval

Let

\[
A_*:=\frac{95473}{9666}.
\]

For `theta in [0,1]`,

\[
2+\theta-A_*\theta(1-\theta)
\ge
2-\frac{(A_*-1)^2}{4A_*}
=
\frac{19894895}{3691368072}.
\tag{6.5}
\]

Since `M+lambda<=3+46/25=121/25`, (2.5) yields the explicit uniform sign certificate

\[
\boxed{
\ell'_\lambda
\le
-\frac{12434309375}{27022659971076}
< -4.60\times10^{-4}
}
\tag{6.6}
\]

for every `p in [0,1]` and every `1<=lambda<=46/25`.

## 7. What changed and what remains open

**Full-source metric:** `R_full: 1 -> 1`.

**Intermediate obligations:**

* `O1` source convention/current source-uniform range: DONE.
* `O2` effective-degree reduction: DONE in prior P03-A.
* `O3` one genuinely random `{2,3}` subfamily past the published cutoff: DONE in prior P03-A.
* `O4` remove the small-`p` restriction for `{2,3}`: **DONE on a much larger interval**, now all `p` through `lambda=46/25`, with the analytic limiting threshold `Lambda_2≈1.8402833`.
* `O4b` adjacent two-point laws `{d,d+1}`: **NEW PROVED PARTIAL**, all mixture weights through `lambda=d-1/4`, plus the sharper pointwise criterion (4.4).
* `O5` arbitrary finite support with `min nu>=2`: OPEN.
* `O6` minimum offspring 1 and all no-leaf laws: OPEN.

## 8. Exact remaining gap and next attack

The natural next analytic identity is

\[
M'(\lambda)
=\operatorname{Cov}_{\pi_\lambda}\!\left(\nu,(\log c_\nu)'\right),
\qquad
\pi_\lambda(k)\propto P(\nu=k)c_k(\lambda).
\tag{8.1}
\]

For two adjacent support points, (3.6) completely controls this covariance. For broader finite support the next useful step is a pairwise decomposition

\[
\operatorname{Cov}_{\pi}(X,Y)
=\frac12 E_{\pi\otimes\pi}[(X-X')(Y-Y')]
\tag{8.2}
\]

combined with telescoping adjacent bounds on `(log c_{k+1})'-(log c_k)'`. The objective is to retain the analogue of the exact `d+theta` weight optimization instead of reverting to a support-diameter/Gruss bound. That is distinct from P03-B's regeneration-debt program and should be capable of extending Theorem 5.1 from adjacent support to arbitrary narrow finite support.

No old D0047 file, peer report, canonical claim, or history was modified in this run.
