# A sharper conditional integrability criterion on the line

Let $0<\lambda<1$, $R=(1-\lambda)^{-1}$ and $D=2R$. The signs
$\xi_j$ are independent and fair. Write
\[
 S_n=\sum_{j=0}^{n-1}\xi_j\lambda^j,\qquad r_n=R\lambda^n,
 \qquad \nu=\mathcal L\left(\sum_{j=0}^\infty\xi_j\lambda^j\right).
\]
Let $\mu_n$ be the law of $S_n+\lambda^n U$, where $U$ is independent
and uniform on $[-R,R]$. Its density and concentration function are
\[
 f_n(x)=\frac{1}{2^{n+1}r_n}
 \sum_{\sigma\in\{-1,1\}^n}
 1_{[s_\sigma-r_n,s_\sigma+r_n]}(x),
 \qquad
 A_n(\delta)=\sup_{|E|\leq\delta}\int_E f_n(x)\,dx.
\]
Here $s_\sigma=\sum_{j=0}^{n-1}\sigma_j\lambda^j$.
All small-set suprema are over Lebesgue measurable sets. Repeated prefix
sums retain their multiplicities. Endpoints of intervals do not affect
the densities.

**Theorem.** Suppose $0<\delta\leq D$ and
\[
 \liminf_{n\to\infty} A_n(\delta)<\theta<\frac14.
 \tag{1}
\]
Then $\nu$ is absolutely continuous. For every
\[
 c>\frac{1}{1-4\theta},\qquad
 \gamma=\frac{4c\theta}{c-1},\qquad
 H=\frac{4cD}{\delta\lambda},
 \tag{2}
\]
its density belongs to $L^p(\mathbb R)$ for every
\[
 1<p<1+\frac{\log(1/\gamma)}{\log H}.
 \tag{3}
\]
In particular, one admissible explicit choice is
\[
 p=1+
 \frac{\log((1+4\theta)/(8\theta))}
 {2\log(8D/(\delta\lambda(1-4\theta)))}.
 \tag{4}
\]
Under the simpler restriction $\theta<1/12$, another admissible choice is
\[
 p=1+\frac{\log(1/(12\theta))}
 {\log(8D/(\delta\lambda))}.
 \tag{5}
\]
For the range $\theta<1/18$ treated in the earlier report, (5) is strictly
larger than its exponent
$1+\log(1/(18\theta))/\log(72D/(\delta\lambda))$.

The hypothesis (1) is an infinite-subsequence condition. No finite-depth
condition and no absolute continuity result for a specified transcendental
parameter is asserted. The constants here are sufficient; their optimality
is not asserted.

## 1. Rechecking the passage from prefixes to the measure

Couple $X$ of law $\nu$ and $Z_n$ of law $\mu_n$ using the same first
$n$ signs. The remaining tails of both lie in $[-r_n,r_n]$, so
$|X-Z_n|\leq2r_n\to0$. Thus $\mu_n$ converges weakly to $\nu$.

For completeness, $\nu$ has pure Lebesgue type. Define
\[
 T\rho=\tfrac12(g_+)_*\rho+\tfrac12(g_-)_*\rho,
 \qquad g_\pm(x)=\lambda x\pm1.
\]
Both similarities preserve absolute continuity and singularity of positive
finite measures. Consequently, in the Lebesgue decomposition $\nu=a+s$,
the identity $T\nu=\nu$ implies $Ta=a$ and $Ts=s$ by uniqueness of that
decomposition. There is a unique invariant probability supported on
$[-R,R]$: couple two starting points by using the same signs for $k$
iterations. Their distance becomes at most $2R\lambda^k$, so invariant
laws agree on all bounded Lipschitz functions and hence agree as measures.
If $a(\mathbb R)>0$, then $a/a(\mathbb R)$ is such an invariant
probability and equals $\nu$. Thus $\nu$ is absolutely continuous;
otherwise $\nu$ is singular.

If $\nu$ is singular, for any $b<1$ there is a compact null set $F$
with $\nu(F)>b$. For every $\delta>0$ there is a bounded open
$G\supset F$ with $|G|<\delta$. The open-set inequality gives
\[
 b<\nu(G)\leq\liminf_n\mu_n(G)\leq\liminf_n A_n(\delta).
\]
Letting $b\uparrow1$ shows $A_n(\delta)\to1$. Hypothesis (1) excludes
this case, so $d\nu=f\,dx$ for an integrable nonnegative density $f$.

Choose a subsequence $n_j\to\infty$ such that $A_{n_j}(\delta)\leq\theta$.
If $F$ is compact and $|F|\leq\delta/2$, take a bounded open
$G\supset F$ with $|G|<\delta$. Then
\[
 \nu(F)\leq\nu(G)\leq\liminf_j\mu_{n_j}(G)\leq\theta.
\]
Inner regularity gives
\[
 \omega(\delta/2)\leq\theta,
 \qquad \omega(t)=\sup_{|E|\leq t}\nu(E).
 \tag{6}
\]
Lebesgue measurable sets may be replaced by Borel sets up to a null set
here, since absolute continuity has already been established.

## 2. Localization by cylinders

Let $B=(x-r,x+r)$ with $0<r<D$, and choose the least $k\geq1$
such that $D\lambda^k\leq r$. Then
\[
 \frac{\lambda r}{D}<\lambda^k\leq\frac rD.
\]
The interval $g_\sigma([-R,R])$, for
$g_\sigma(y)=s_\sigma+\lambda^ky$, has diameter at most $r$.
Every such interval meeting $B$ lies in $2B=(x-2r,x+2r)$.
For $E\subset B$,
\[
 |g_\sigma^{-1}E|=\lambda^{-k}|E|
 \leq\frac{2D}{\lambda}\frac{|E|}{|B|}.
\]
The non-strict inequality includes $|E|=0$. The level-$k$ self-similarity
identity, summing only over cylinders meeting $B$, therefore gives
\[
 \nu(E)\leq
 \omega\!\left(\frac{2D}{\lambda}\frac{|E|}{|B|}\right)
 \nu(2B).
 \tag{7}
\]
Indeed, the sum of the weights of these cylinders is at most $\nu(2B)$,
because their entire conditional measures are supported in $2B$.

Set
\[
 \varepsilon=\frac{\delta\lambda}{4D}\in(0,1).
 \tag{8}
\]
Equations (6) and (7) imply
\[
 |E|\leq\varepsilon|B|\quad\Longrightarrow\quad
 \nu(E)\leq\theta\nu(2B)
 \quad(E\subset B,\ 0<r<D).
 \tag{9}
\]
Rescaling by $D^{-1}$ makes the allowed radii less than one, preserving
$\varepsilon$ and $\theta$. Membership in $L^p$ is preserved by this
fixed rescaling. It remains to prove the following analytic lemma.

## 3. An interval covering lemma

Every finite family of open bounded intervals has a subfamily with the
same union and multiplicity at most two.

To see this, discard an interval whenever it is contained in the union
of the others. This finite procedure preserves the union. The remaining
family has no pair with one interval contained in the other. Suppose three
remaining intervals contain a point. Order their left endpoints as
$a_1<a_2<a_3$; absence of containment orders their right endpoints as
$b_1<b_2<b_3$. Their common point implies $a_3<b_1$, and hence
\[
 (a_2,b_2)\subset(a_1,b_1)\cup(a_3,b_3).
\]
The middle interval would have been removable, a contradiction. Thus no
point belongs to three remaining intervals.

## 4. A one-dimensional higher-integrability lemma

**Lemma.** Let $h\geq0$ be in $L^1(\mathbb R)$. Suppose that
$0<\varepsilon<1$, $0<\eta<1/4$, and for every open interval $B$ of
radius less than one and every measurable $E\subset B$,
\[
 |E|\leq\varepsilon|B|\quad\Longrightarrow\quad
 \int_Eh\leq\eta\int_{2B}h.
 \tag{10}
\]
For any $c>1/(1-4\eta)$, put
\[
 A=\frac c\varepsilon>1,\qquad
 \Gamma=\frac{4c\eta}{c-1}<1.
\]
Then $h\in L^p$ whenever $p>1$ and $\Gamma A^{p-1}<1$.

**Proof.** If $h=0$ almost everywhere there is nothing to prove. Put
\[
 F(t)=\int_{\{h>t\}}h.
\]
Fix $t>0$ and a Lebesgue point $x$ with $h(x)>At$. The centered
average of $h$ tends to $h(x)>ct$ at small radii and to zero at large
radii. As a function of positive radius the average is continuous.
It follows that there is a largest radius $r_x>0$ at which this average
is at least $ct$. For $B_x=(x-r_x,x+r_x)$,
\[
 \int_{B_x}h=ct|B_x|,\qquad
 \int_{aB_x}h\leq ct|aB_x|\quad(a>1).
 \tag{11}
\]
The equality follows by continuity and maximality. Also
$r_x\leq\|h\|_1/(2ct)$. For $t>\|h\|_1/(2c)$ every such $B_x$
has radius less than one, so (10) applies to it.

Let $E_t=\{h>At\}$ and let $K$ be a compact subset of its Lebesgue
points. A finite collection of these $B_x$ covers $K$. Apply section 3
to obtain a subcover $B_1,\ldots,B_m$ of multiplicity at most two.
Chebyshev's inequality and (11) give
\[
 |E_t\cap B_i|\leq\frac{1}{At}\int_{B_i}h
 =\frac cA|B_i|=\varepsilon|B_i|.
\]
Thus (10) and (11), using $|2B_i|=2|B_i|$, imply
\[
 \int_Kh\leq\sum_i\int_{E_t\cap B_i}h
 \leq\eta\sum_i\int_{2B_i}h
 \leq2c\eta t\sum_i|B_i|.
 \tag{12}
\]
On the other hand,
\[
 ct|B_i|=\int_{B_i}h
 \leq t|B_i|+\int_{B_i\cap\{h>t\}}h.
\]
Summing, and using the multiplicity bound only for $B_i$ rather than
for $2B_i$, gives
\[
 (c-1)t\sum_i|B_i|\leq2F(t).
 \tag{13}
\]
Equations (12) and (13), followed by inner regularity and the Lebesgue
differentiation theorem, yield the recurrence
\[
 F(At)\leq\Gamma F(t),\qquad
 \Gamma=\frac{4c\eta}{c-1},
 \quad t>\frac{\|h\|_1}{2c}.
 \tag{14}
\]

Take $T>\|h\|_1/(2c)$ and a $p>1$ with $q=\Gamma A^{p-1}<1$.
For $M\geq AT$, put $J(M)=\int_T^M t^{p-2}F(t)\,dt$.
Changing variables $t=Au$ in the part from $AT$ to $M$ gives
\[
 \begin{aligned}
 J(M)&\leq J(AT)+\Gamma A^{p-1}J(M/A)\\
 &\leq J(AT)+qJ(M).
 \end{aligned}
\]
Therefore $J(M)\leq J(AT)/(1-q)$ uniformly in $M$. Since
$F(t)\leq\|h\|_1$, the integral from zero to $T$ is finite as well.
Tonelli's theorem now gives
\[
 \int_0^\infty t^{p-2}F(t)\,dt
 =\frac{1}{p-1}\int_{\mathbb R}h(x)^p\,dx<\infty.
\]
This proves the lemma. The strict condition $q<1$ is essential to this
argument; it makes no assertion at the endpoint exponent. $\square$

## 5. Exponents and comparison with the earlier result

Apply the lemma to the rescaled density using (9), with $\eta=\theta$
and (8). Its $A$ is $c/\varepsilon=4cD/(\delta\lambda)=H$.
The inequality $\gamma H^{p-1}<1$ is exactly (3). This proves the
main assertion.

For (4), take
\[
 c=\frac{2}{1-4\theta},\qquad
 \gamma=\frac{8\theta}{1+4\theta},\qquad
 H=\frac{8D}{\delta\lambda(1-4\theta)}.
\]
The displayed exponent satisfies $\gamma H^{p-1}=\sqrt\gamma<1$.
For (5), take $c=2$. Then $\gamma=8\theta$ and
$H=8D/(\delta\lambda)$, and its exponent satisfies
\[
 \gamma H^{p-1}=8\theta\frac1{12\theta}=\frac23<1.
\]
When $\theta<1/18$, the numerator in (5) is larger than the earlier
positive numerator, while its positive denominator is smaller. Hence
the asserted strict improvement follows.

For the earlier arithmetic example $\lambda=2/3$, $\delta=1/64$,
$\theta=1/36$, one obtains
\[
 D=6,\quad\varepsilon=1/2304,\quad
 H=4608,\quad\gamma=2/9,
 \quad p=1+\frac{\log3}{\log4608}
 \tag{15}
\]
from (5). These are conditional exponents, not a proof of the
hypothesis for $\lambda=2/3$.

## 6. Scope and source

The qualitative concentration criterion and the localization (7) were
proved in the round-3 folder and are re-derived here. The new ingredient
is the multiplicity-two interval cover in the higher-integrability
argument, giving (14), the threshold $1/4$, and (3)--(5).
The method is a one-dimensional modification of the proof of Lemma 2.1
in Samuel Kittle and Constantin Kogler, *On L^p density of self similar
measures and Bernoulli Convolutions*,
[arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1).
The proof above includes all analytic steps and does not use that lemma
as a black box. No claim of priority over the wider reverse-Hölder
literature is made.

The missing estimate remains an upper bound for $A_n(\delta)$ along an
unbounded sequence at a specified transcendental parameter. Dimension
one alone supplies no such estimate here. T075 remains open.
