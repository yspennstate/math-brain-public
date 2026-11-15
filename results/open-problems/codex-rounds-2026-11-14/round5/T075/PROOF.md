# Arbitrarily long small-cap prefixes at singular parameters

For $1/2<\lambda<1$, put $R=(1-\lambda)^{-1}$ and let $u_\lambda$
be the uniform probability measure on $[-R,R]$. Define
\[
 T_\lambda\rho=\tfrac12(g_+)_*\rho+\tfrac12(g_-)_*\rho,
 \qquad g_\pm(x)=\lambda x\pm1,
 \qquad \mu_n=T_\lambda^n u_\lambda.
\]
Thus $\mu_n$ is the law of the first $n$ signs plus an independent
uniform tail on $[-R\lambda^n,R\lambda^n]$, as in the preceding reports.
Set
\[
 A_n(\delta)=\sup_{|E|\leq\delta}\mu_n(E),\qquad
 d(\lambda)=\frac{(2\lambda-1)(1-\lambda)}{\lambda}.
\]
The supremum is over Lebesgue measurable sets. Write
$\|\rho-\sigma\|_{\rm TV}=\sup_E|\rho(E)-\sigma(E)|$ for probability
measures. For densities this is half their $L^1$ distance.

**Proposition.** For every $n\geq0$ and $\delta>0$,
\[
 \|\mu_n-u_\lambda\|_{\rm TV}\leq n d(\lambda),
 \tag{1}
\]
and consequently
\[
 A_n(\delta)\leq
 \min\left\{1,\frac{\delta(1-\lambda)}2+n d(\lambda)\right\}
 \leq \min\left\{1,\frac\delta4+n(2\lambda-1)\right\}.
 \tag{2}
\]

**Theorem.** Let $\delta>0$ and $\delta/4<\theta<1$. For every
integer $N\geq1$ there is an algebraic $\lambda\in(1/2,1)$ such that
$\nu_\lambda$ is singular and
\[
 A_n(\delta)<\theta\quad(0\leq n\leq N),
 \qquad \lim_{n\to\infty}A_n(\delta)=1.
 \tag{3}
\]
An explicit choice is $\lambda=\lambda_k=\beta_k^{-1}$, where
\[
 P_k(z)=z^k-z^{k-1}-\cdots-z-1,\qquad k\geq2,
\]
$\beta_k$ is its positive root in $(1,2)$, and $k$ is any integer with
\[
 N2^{-k}<\theta-\delta/4.
 \tag{4}
\]
These parameters satisfy
\[
 \frac12<\lambda_k<\frac12+2^{-(k+1)},\qquad
 A_n(\delta)<\frac\delta4+n2^{-k}\quad(n\geq1).
 \tag{5}
\]

The theorem rules out replacing an infinite-subsequence cap bound by a
fixed finite initial segment, uniformly over all real parameters in
$(1/2,1)$. It does not rule out a propagation argument with additional
hypotheses, and it supplies no singular transcendental parameter.

## 1. The uniform law has a small one-step defect

Let $a=2\lambda-1\in(0,1)$. The images of $[-R,R]$ under $g_-$ and
$g_+$ are $[-R,aR]$ and $[-aR,R]$. Each branch contributes density
$(1-\lambda)/(4\lambda)$. Consequently the density $v$ of
$T_\lambda u_\lambda$ equals
\[
 v(x)=
 \begin{cases}
 (1-\lambda)/(2\lambda),& |x|<aR,\\
 (1-\lambda)/(4\lambda),& aR<|x|<R,\\
 0,& |x|>R.
 \end{cases}
\]
The density of $u_\lambda$ is $(1-\lambda)/2$ on this support. Hence
$v-u_\lambda$ is positive on the central interval and negative on its
complement in the support. The positive mass is
\[
 2aR\left(\frac{1-\lambda}{2\lambda}-\frac{1-\lambda}{2}\right)
 =\frac{a(1-\lambda)}\lambda=d(\lambda).
 \tag{6}
\]
Independently, the two outer intervals have total length
$2R(1-a)=4$. Their negative mass is
\[
 4\left(\frac{1-\lambda}{2}-\frac{1-\lambda}{4\lambda}\right)
 =\frac{a(1-\lambda)}\lambda.
 \tag{7}
\]
Thus the one-step total variation distance is exactly $d(\lambda)$.

For a signed measure $\eta$, the full variation norm satisfies
$\|T_\lambda\eta\|\leq\|\eta\|$: pushforward does not increase
variation, and the two coefficients sum to one. For differences of
probability measures this gives contraction in the TV convention above.
The identity
\[
 T_\lambda^n u_\lambda-u_\lambda
 =\sum_{j=0}^{n-1}T_\lambda^j(T_\lambda u_\lambda-u_\lambda)
\]
proves (1). For $|E|\leq\delta$, it follows that
\[
 \mu_n(E)\leq u_\lambda(E)+n d(\lambda)
 \leq\frac{\delta(1-\lambda)}2+n d(\lambda).
\]
The bound by one is automatic. Finally $(1-\lambda)/2<1/4$ and
$d(\lambda)<2\lambda-1$, giving (2).

## 2. Multinacci roots and the parameter bound

The function $\sum_{j=1}^k x^{-j}$ is strictly decreasing for $x>0$,
is $k>1$ at $x=1$, and is $1-2^{-k}<1$ at $x=2$. It has exactly one
root of the equation $\sum_{j=1}^k x^{-j}=1$ in $(1,2)$, namely
$\beta_k$. Equivalently, $\lambda_k$ is the unique positive root of
\[
 \sum_{j=1}^k\lambda^j=1.
 \tag{8}
\]
At $\lambda=1/2$, the left side is $1-2^{-k}<1$, so $\lambda_k>1/2$.

Put $t=1/2+2^{-(k+1)}$. For $0<x<1$, the identity
\[
 (1-x)\left(\sum_{j=1}^k x^j-1\right)=2x-1-x^{k+1}
 \tag{9}
\]
shows that $\lambda_k<t$ if
\[
 (1+2^{-k})^{k+1}<2.
 \tag{10}
\]
Indeed $2t-1=2^{-k}$ and
$t^{k+1}=2^{-(k+1)}(1+2^{-k})^{k+1}$.
For $k=2$, (10) is $125/64<2$. For $k\geq3$, put $m=k+1$ and
$u=2^{-k}$. Then $mu\leq1/2$: equality holds at $k=3$, and the
ratio of consecutive values is $(k+2)/(2k+2)<1$. The binomial expansion
and $\binom mj\leq m^j$ give
\[
 (1+u)^m=\sum_{j=0}^m\binom mj u^j
 <\sum_{j=0}^\infty (mu)^j=\frac1{1-mu}\leq2.
\]
The inequality is strict because the infinite series has positive terms
beyond $m$. This proves (5)'s parameter bound and $2\lambda_k-1<2^{-k}$.
Together with (2) it proves the cap bound in (5).

## 3. The other conjugates lie inside the unit circle

The polynomial identity
\[
 (z-1)P_k(z)=z^{k+1}-2z^k+1
\]
shows that the roots of $Q_k(z)=z^k(2-z)-1$ are those of $P_k$ together
with $1$. For $r>1$ sufficiently close to one,
\[
 r<\min\{\beta_k,2\},\qquad r^k(2-r)>1.
\]
The latter follows because $r^k(2-r)$ equals one at $r=1$ and has
derivative $k-1>0$ there. On $|z|=r$,
\[
 |z^k(2-z)|\geq r^k(2-r)>1.
\]
Rouché's theorem applied to $z^k(2-z)$ and $Q_k$ therefore gives
exactly $k$ roots of $Q_k$ inside $|z|<r$, counted with multiplicity.
The comparison polynomial has $k$ roots at zero and its other root at
$2$, outside the circle. The degree of $Q_k$ is $k+1$, and $\beta_k>r$
is a root, so every root other than $\beta_k$ lies in $|z|<r$.
Letting such radii decrease to one puts all those roots in $|z|\leq1$.

If $|z|=1$ and $Q_k(z)=0$, then $|2-z|=1$, forcing $z=1$.
But $P_k(1)=1-k\ne0$. Thus every root of $P_k$ other than $\beta_k$
lies strictly inside the unit circle.

The number $\beta_k$ is an algebraic integer. It is irrational, since
a rational algebraic integer is an integer and $1<\beta_k<2$.
Let its distinct algebraic conjugates be $\beta_k,\alpha_2,\ldots,
\alpha_d$; they are among the roots of $P_k$, so
$\rho=\max_{i\geq2}|\alpha_i|<1$. For $m\geq1$ the power sum
\[
 s_m=\beta_k^m+\sum_{i=2}^d\alpha_i^m
\]
is an integer. This follows from Newton's identities for the monic
minimal polynomial with integer coefficients: they give the first $d$
power sums as integers and then an integer linear recurrence for the
remaining sums. Consequently
\[
 \operatorname{dist}(\beta_k^m,\mathbb Z)\leq(d-1)\rho^m.
 \tag{11}
\]
No positive power $\beta_k^m$ is rational: it would be an integer, while
the corresponding conjugate $\alpha_2^m$ would be the same integer and
have modulus less than one, contradicting $\beta_k^m>1$. No negative
power is rational either, by inversion.

## 4. Fourier nondecay and singularity

Write $\beta=\beta_k$ and $\lambda=\beta^{-1}$. Independence and
convergence of the random series give
\[
 \widehat\nu_\lambda(t)=\prod_{j=0}^\infty\cos(t\lambda^j).
 \tag{12}
\]
For example this follows first for finite prefixes and then by dominated
convergence, since the series converges uniformly over all choices of
signs.

Every factor $|\cos(2\pi\beta^\ell)|$, $\ell\in\mathbb Z$, is
nonzero. A zero would require $\beta^\ell$ to be an odd integer divided
by four; nonzero powers are irrational and the zeroth power is one.
For $\ell\to+\infty$, (11) and $1-|\cos(2\pi x)|\leq
1-\cos(2\pi x)\leq2\pi^2\operatorname{dist}(x,\mathbb Z)^2$ imply
summable deficits. For $\ell\to-\infty$, the inequality
$1-|\cos(2\pi x)|\leq2\pi^2 x^2$ gives the same conclusion.
Hence
\[
 C=\prod_{\ell\in\mathbb Z}|\cos(2\pi\beta^\ell)|>0.
 \tag{13}
\]
To justify positivity, discard finitely many factors so that all remaining
ones exceed $1/2$, and use $-\log a\leq2(1-a)$ for $1/2\leq a\leq1$.
The remaining logarithms are summable, and the discarded factors are
strictly positive.

At $t_m=2\pi\beta^m\to\infty$, (12) gives
\[
 |\widehat\nu_\lambda(t_m)|
 =\prod_{\ell=-\infty}^m|\cos(2\pi\beta^\ell)|\geq C.
 \tag{14}
\]
Thus $\nu_\lambda$ is not absolutely continuous. Indeed, the Fourier
transform of an $L^1$ density tends to zero: approximate the density in
$L^1$ by finite linear combinations of bounded-interval indicators,
whose Fourier transforms tend to zero by direct integration.

For completeness, the invariant measure has pure Lebesgue type. Both
similarities preserve absolute continuity and singularity, so uniqueness
of Lebesgue decomposition makes the absolutely continuous and singular
parts of $\nu_\lambda$ separately $T_\lambda$-invariant. There is a
unique invariant probability supported on $[-R,R]$: under the same
sequence of signs, any two starting variables in this interval differ
after $j$ steps by at most $2R\lambda^j$. Their expectations against any
bounded Lipschitz function therefore converge to each other. If the
absolutely continuous part had positive mass, its normalization would
be this unique invariant probability, forcing $\nu_\lambda$ itself to
be absolutely continuous. This contradicts (14). It follows that
$\nu_\lambda$ is singular.

## 5. Eventual concentration and the finite-depth obstruction

Couple $\mu_n$ with $\nu_\lambda$ using the same first $n$ signs.
Their tails each lie in $[-R\lambda^n,R\lambda^n]$, so the coupled
variables differ by at most $2R\lambda^n$. Thus $\mu_n$ converges
weakly to $\nu_\lambda$. If $b<1$, singularity supplies a compact null
set $F$ with $\nu_\lambda(F)>b$. Choose a bounded open $G\supset F$
with $|G|<\delta$. The open-set inequality for weak convergence gives
\[
 b<\nu_\lambda(G)\leq\liminf_n\mu_n(G)
 \leq\liminf_n A_n(\delta)\leq1.
\]
Let $b$ increase to one. This proves the limit in (3).

Choose $k$ satisfying (4). For $1\leq n\leq N$, (5) gives
$A_n(\delta)<\delta/4+N2^{-k}<\theta$. At $n=0$,
$A_0(\delta)\leq\delta(1-\lambda_k)/2<\delta/4<\theta$.
This completes the theorem.

For the previous reports' values $\delta=1/64$ and $\theta=1/36$,
the margin is
\[
 \theta-\delta/4=\frac{55}{2304}.
\]
At $k=20$, one may take $N=25031$, since
\[
 \frac1{36}-\left(\frac1{256}+\frac{25031}{2^{20}}\right)
 =\frac1{9437184}>0.
 \tag{15}
\]
Thus the singular parameter $\lambda_{20}$ passes all these cap tests
through depth $25031$. This is an analytic bound; it requires no
enumeration of $2^{25031}$ prefixes. The parameter satisfies
$1/2<\lambda_{20}<1/2+2^{-21}$.

The preceding round's conditional $L^p$ theorem remains valid. The
present obstruction concerns how its infinite-subsequence hypothesis
could be established. The underlying Pisot singularity mechanism is
classical; the contribution here is its explicit quantitative application
to the prefix caps. No claim of priority is made. Absolute continuity at
every transcendental parameter remains open in the bounded literature
check recorded in LOG.md.
