# A prefix concentration criterion

Fix $0<\lambda<1$ and write $\nu=\nu_\lambda$. The signs below are independent and fair. Put $R=(1-\lambda)^{-1}$, $D=2R$, and
\[
 S_n=\sum_{j=0}^{n-1}\xi_j\lambda^j,
 \qquad r_n=R\lambda^n.
\]
Let $U$ be uniform on $[-R,R]$, independently of the signs. The law
$\mu_n=\mathcal L(S_n+\lambda^n U)$ has density
\[
 f_n(x)=\frac1{2^{n+1}r_n}
 \sum_{\sigma\in\{-1,1\}^n}
 1_{[s_\sigma-r_n,s_\sigma+r_n]}(x),
 \qquad s_\sigma=\sum_{j<n}\sigma_j\lambda^j.
\]
Repeated prefix sums are counted with multiplicity. Endpoints do not affect integrals. For $\delta>0$, define
\[
 A_n(\delta)=\sup_{|E|\leq\delta}\int_E f_n(x)\,dx,
\]
where the supremum is over Lebesgue measurable sets.

**Proposition.** The following are equivalent:

1. The Bernoulli convolution $\nu_\lambda$ is absolutely continuous.
2. For some $\delta>0$, $\liminf_{n\to\infty}A_n(\delta)<1$.
3. $\lim_{\delta\downarrow0}\sup_{n\geq1}A_n(\delta)=0$.

If the measure is singular, then $A_n(\delta)\to1$ for every $\delta>0$.

This is a reformulation of absolute continuity in finite-prefix terms, not a finite-depth test or a proof for any specified transcendental parameter.

## 1. Weak convergence and pure type

Write $X=S_n+\lambda^nY_n$, where $Y_n$ has law $\nu_\lambda$, is independent of $S_n$, and lies in $[-R,R]$. Coupling with the same prefix and an independent $U$ gives
\[
 |X-(S_n+\lambda^nU)|\leq2R\lambda^n\longrightarrow0.
\]
Thus $\mu_n$ converges weakly to $\nu_\lambda$. Both measures are supported on $[-R,R]$.

Here is a proof of pure type so that it need not be assumed. Define
\[
 T\rho=\tfrac12(g_+)_*\rho+\tfrac12(g_-)_*\rho,
 \qquad g_\pm(x)=\lambda x\pm1.
\]
These maps preserve absolute continuity and singularity of finite positive measures: similarities and their inverses preserve Lebesgue-null sets, and a finite union of null sets is null. In the Lebesgue decomposition $\nu=a+s$, uniqueness of that decomposition and $T\nu=\nu$ therefore give $Ta=a$ and $Ts=s$.

There is only one invariant probability measure supported on $[-R,R]$. Indeed, for two such measures $\rho,\rho'$, couple their initial variables $Z,Z'$ arbitrarily and apply the same independent signs for $n$ steps. The resulting variables differ by $\lambda^n(Z-Z')$, of magnitude at most $2R\lambda^n$. If both laws are invariant, the expectations of every bounded Lipschitz function under the two laws differ by at most its Lipschitz constant times $2R\lambda^n$. Letting $n\to\infty$ proves equality of the laws.

If $a(\mathbb R)>0$, the probability $a/a(\mathbb R)$ is invariant and supported on $[-R,R]$, hence equals $\nu$. It follows that $\nu$ is absolutely continuous. Otherwise $\nu=s$ is singular. This proves the dichotomy.

## 2. Singular measures force concentration of the prefix densities

Suppose $\nu$ is singular. Given $b<1$, regularity supplies a compact Lebesgue-null set $F$ with $\nu(F)>b$. Given $\delta>0$, choose a bounded open neighborhood $G\supset F$ with $|G|\leq\delta$. Weak convergence and the open-set inequality give
\[
 b<\nu(G)\leq\liminf_n\mu_n(G)
 \leq\liminf_n A_n(\delta)\leq1.
\]
Letting $b\uparrow1$ proves $A_n(\delta)\to1$. Consequently assertion 2 rules out singularity, and pure type implies assertion 1.

## 3. Absolute continuity controls every prefix density

Suppose $d\nu=f\,dx$. Write
\[
 \omega_\nu(t)=\sup_{|E|\leq t}\nu(E).
\]
The absolute continuity of the integral gives $\omega_\nu(t)\to0$ as $t\downarrow0$.

Let $u_{2r}(x)=(4r)^{-1}1_{[-2r,2r]}(x)$. Conditioning on $S_n=s$, the true remaining tail lies in $[-r_n,r_n]$. If $|x-s|<r_n$, then $|x-s-y|<2r_n$ for every such tail value $y$. Hence, for almost every $x$,
\[
 (\nu*u_{2r_n})(x)\geq
 \frac1{4r_n}\,2^{-n}\sum_\sigma
 1_{(s_\sigma-r_n,s_\sigma+r_n)}(x)
 =\tfrac12 f_n(x).
\]
For any set $E$ of length at most $\delta$, Tonelli's theorem gives
\[
 \int_E (\nu*u_{2r_n})(x)\,dx
 =\int u_{2r_n}(y)\nu(E-y)\,dy
 \leq\omega_\nu(\delta).
\]
It follows that
\[
 A_n(\delta)\leq2\omega_\nu(\delta)\quad(n\geq1).
\]
This proves assertion 3. Assertion 3 immediately gives assertion 2, completing the proof.

## 4. A quantitative consequence

Suppose $0<\delta\leq D$ and
\[
 \liminf_n A_n(\delta)<\theta<1/18.
\]
Then $\nu$ has a density in $L^p(\mathbb R)$, where
\[
 \boxed{p=1+\frac{\log(1/(18\theta))}
 {\log(72D/(\delta\lambda))}>1.}
\]

To verify the constants, pass to a subsequence with $A_n(\delta)\leq\theta$. For any compact $F$ with $|F|\leq\delta/2$, there is an open neighborhood $G$ of length at most $\delta$. The open-set inequality along this subsequence shows $\nu(F)\leq\theta$. Inner regularity then gives
\[
 \omega_\nu(\delta/2)\leq\theta.
\]
The proposition has already proved absolute continuity here.

Let $B=(x-r,x+r)$ with $0<r<D$. Choose the least $k\geq1$ with $D\lambda^k\leq r$. Minimality gives
\[
 \lambda r/D<\lambda^k\leq r/D.
\]
The level $k$ cylinders are the images of $[-R,R]$ by maps $g_\sigma(y)=s_\sigma+\lambda^ky$; each has diameter at most $r$. Any cylinder meeting $B$ lies in $2B=(x-2r,x+2r)$. Its whole probability weight therefore contributes to $\nu(2B)$. For $E\subset B$,
\[
 |g_\sigma^{-1}E|=\lambda^{-k}|E|
 \leq\frac{2D}{\lambda}\frac{|E|}{|B|}.
\]
Using the level $k$ self-similarity identity and summing just the cylinders meeting $B$ yields
\[
 \nu(E)\leq
 \omega_\nu\!\left(\frac{2D}{\lambda}\frac{|E|}{|B|}\right)
 \nu(2B).
\]
In particular, with $\varepsilon=\delta\lambda/(4D)\in(0,1)$,
\[
 |E|\leq\varepsilon|B|
 \quad\Longrightarrow\quad
 \nu(E)\leq\theta\nu(2B).
\]
Rescale the real line by $D^{-1}$. Balls with $r<D$ become balls of radius less than one, and the last implication is unchanged. Apply Lemma 2.1, in dimension one, of Samuel Kittle and Constantin Kogler, *On L^p density of self-similar measures and Bernoulli convolutions*, [arXiv:2611.17277v1](https://arxiv.org/html/2611.17277v1). Its constant is $18$, so its exponent is
\[
 1+\frac{\log(1/(18\theta))}{\log(18/\varepsilon)}.
\]
Since $18/\varepsilon=72D/(\delta\lambda)$, this is the displayed value. Scaling back preserves membership in $L^p$.

## 5. Computing the statistic exactly

Between consecutive distinct endpoints $s_\sigma\pm r_n$, the density is constant. Let the resulting positive-density segments have lengths $\ell_j$ and overlap counts $c_j$. Sort the segments in decreasing order of $c_j$. Set $b=(2^{n+1}r_n)^{-1}$, $L_0=0$, and $L_j=\sum_{i=1}^j\ell_i$. Then
\[
 A_n(\delta)=b\sum_j c_j\min\{\ell_j,(\delta-L_{j-1})_+\}.
\]
To prove this formula, transfer any selected length from a lower-density segment to an unselected part of a higher-density segment. This never decreases mass and increases it when the densities differ. Filling segments in the indicated order is therefore optimal. Lebesgue measure has no atoms, so a segment may be filled to any requested partial length. Once all positive-density segments are filled the mass is one.

For rational $\lambda,\delta$, all endpoints and all terms in this formula are rational. The accompanying script uses exact fractions and aggregates coincident endpoint events. It verifies finite depths only. None of the equivalences above permits replacing an infinite subsequence by a finite set of depths.

For the control cases $0<\lambda\leq1/2$, the level-one hull intervals have disjoint interiors: their centers are $-1,1$ and their radii are $\lambda R\leq1$. Iteration shows that all level-$n$ hull intervals have disjoint interiors. Their total length is
\[
 L_n=2^n(2R\lambda^n)=D(2\lambda)^n.
\]
Each interval has the same density $1/L_n$, so
\[
 A_n(\delta)=\min\{\delta/L_n,1\}.
\]
At $\lambda=1/2$, the intervals tile the full support and $L_n=4$. At $\lambda=1/3$, $L_n=3(2/3)^n$ tends to zero, so $A_n(\delta)$ eventually equals one. Singularity in the latter case also follows directly: the measure is supported on every level-$n$ union, whose length tends to zero.
