# Bilateral-preference degrees: a non-Gaussian fluctuation candidate

Status: private author-checked candidate for the growing-degree regime in the degree-distribution question on PDF page 3 of Dabirian and Subramanian, *Connectivity of a Family of Bilateral Preference Random Graphs*, arXiv:2209.05677v3, 8 July 2025. No independent review or novelty certification. This packet does not settle every growth regime in the source's broadly stated question. The related simultaneous-concentration estimate is a sufficient condition, not an optimal characterization. Both remain partial in the campaign ledger.

The model is exactly the source model: assign independent uniform $(0,1)$ weights to all undirected edges of the complete graph on $n$ vertices. An edge survives in $LK(n,k)$ precisely when it is among the $k$ smallest incident weights at both endpoints. Let $D$ be the degree of a specified vertex; symmetry gives the same law for a uniformly chosen vertex. Ties have probability zero.

## Candidate theorem and meaning

Suppose $k=k(n)\to\infty$ and $k=o(n^{2/5})$. Let $Z$ be standard normal and write

$$g(z)=\phi(z)+z\Phi(z),\qquad v=\frac13+\frac{\sqrt3-2}{2\pi}>0.$$

The candidate conclusion is convergence in distribution and of the first two moments:

$$\frac{k-D}{\sqrt{k}}\ \Longrightarrow\ g(Z).$$

Consequently,

$$\frac{\operatorname{Var}(D)}{k}\longrightarrow v,\qquad
\frac{D-\mathbb ED}{\sqrt{\operatorname{Var}(D)}}\ \Longrightarrow\
\frac{1/\sqrt\pi-g(Z)}{\sqrt v}.$$

This includes the source's $k=o(n^{1/3})$ regime for its detailed mean asymptotic. The limiting distribution is not normal: $g$ is strictly increasing, positive, and has range $(0,\infty)$, so the standardized degree limit has a finite upper endpoint. Its negative skew is consistent with the deterministic ceiling $D\le k$.

## Exact finite-graph comparison

Fix the root $0$. Let $S$ be its $k$ preferred neighbors, let $O$ be the other $n-k-1$ vertices, and let $X$ be the root's $(k+1)$st smallest incident weight. Then

$$X\sim\operatorname{Beta}(k+1,n-k-1),\quad
\mathbb EX=\frac{k+1}{n},\quad
\mathbb EX^2=\frac{(k+1)(k+2)}{n(n+1)}.$$

Conditional on $X$ and the selected label set $S$, the $k$ unordered root-to-$S$ weights are independent uniforms on $(0,X)$. All edges not incident to the root retain their independent uniform laws. This conditional statement follows directly from the joint density of independent uniform order statistics; no independence of actual degrees is asserted.

Temporarily ignore edges whose two endpoints lie in $S$ when deciding whether a selected neighbor also prefers the root. Let $D^0$ count the resulting accepted root edges. Removing competitors can only help acceptance, so $D^0\ge D$.

Let $J$ count edges internal to $S$ with weight below $X$, and put $M=\binom{k}{2}$. If a neighbor's acceptance changes, it must touch such an edge: every root-to-$S$ weight is below $X$. Therefore

$$0\le D^0-D\le2J,\qquad J\mid X\sim\operatorname{Bin}(M,X).$$

In particular,

$$\mathbb E\frac{(D^0-D)^2}{k}
\le\frac4k\left(M\frac{k+1}{n}
+M(M-1)\frac{(k+1)(k+2)}{n(n+1)}\right)
=O\left(\frac{k^2}{n}+\frac{k^5}{n^2}\right)=o(1).$$

The last step is exactly where the sufficient restriction $k=o(n^{2/5})$ is used. This is an $L^2$ comparison; a bound only on the probability of a discrepancy would not by itself justify the variance conclusion.

There are $m=n-k-1$ outside edges at each selected neighbor. The outside-edge arrays for different selected neighbors are disjoint sets of independent edge variables. Conditional on $X$ and $S$, after also averaging over their independent root weights, the ideal acceptance indicators are thus independent and identically distributed. For large $n$, $m\ge k$. If $T$ is the $k$th order statistic of $m$ independent uniforms, independent of $X$, then

$$T\sim\operatorname{Beta}(k,n-2k),\qquad
D^0\mid X\sim\operatorname{Bin}(k,1-q_n(X)),\qquad
q_n(X)=\frac{\mathbb E[(X-T)_+\mid X]}{X}.$$

Indeed, for a root edge of weight $u$, acceptance means that at most $k-1$ outside edges have weight below $u$, equivalently $u<T$. Integrating $u$ uniformly over $(0,X)$ gives the displayed formula. These are conditional laws of the comparison variable, not of $D$.

## Fluctuation and moment limits

Set

$$A=nX,\quad B=nT,\quad U_n=\frac{A-k}{\sqrt k},\quad V_n=\frac{B-k}{\sqrt k}.$$

Both $U_n$ and $V_n$ converge to standard normal variables in their marginal laws, and their fourth moments are uniformly bounded. Here are the needed checks. Represent a beta variable as a ratio of independent gamma variables. For $X$, the numerator is $\operatorname{Gamma}(k+1,1)$ and the denominator has shape $n$; the denominator replacement error after scaling by $\sqrt k$ is $O_P(\sqrt{k/n})$. For $T$, the numerator has shape $k$ and the denominator has shape $n-k$; the additional centering error is $k^{3/2}/(n-k)=o(1)$. The gamma central limit theorem then applies. The moment assertion also follows directly from the beta moments $\mathbb E X^j=(k+1)^{\overline j}/n^{\overline j}$ and $\mathbb E T^j=k^{\overline j}/(n-k)^{\overline j}$ for $j\le4$. Equivalently, the beta variance and kurtosis formulas show bounded fourth moments after this centering and scaling. No exponentially growing degree moment is being assumed.

Define

$$g_n(u)=\mathbb E[(u-V_n)_+].$$

Convergence in law of $V_n$ and uniform integrability of $|V_n|$ give convergence to normal in Wasserstein distance of order one. Since the positive-part function is one-Lipschitz,

$$\sup_{u\in\mathbb R}|g_n(u)-g(u)|\longrightarrow0,\qquad
g(u)=\mathbb E[(u-Z)_+]=\phi(u)+u\Phi(u).$$

The conditional mean of the scaled degree deficit is

$$C_n:=\frac{kq_n(X)}{\sqrt k}=\frac{k}{A}g_n(U_n).$$

Since $k/A\to1$ in probability, the preceding facts imply $C_n\Longrightarrow g(Z)$.

To justify moments, split according to $A\ge k/2$. On that event,

$$C_n\le2\bigl(|U_n|+\mathbb E|V_n|\bigr).$$

On its complement, $C_n\le\sqrt k$ because $0\le q_n\le1$. Furthermore, the order-statistic/binomial identity and a Chernoff bound give

$$\mathbb P(A<k/2)
\le\mathbb P\{\operatorname{Bin}(n-1,k/(2n))\ge k\}
\le e^{-(\log2-1/2)k}.$$

For the last inequality, apply Markov's inequality to $2^{\operatorname{Bin}}$ and use that the binomial mean is at most $k/2$. Thus $\sup_n\mathbb E C_n^4<\infty$ along the asymptotic sequence. It follows that the first two moments of $C_n$ converge to those of $g(Z)$.

The remaining conditional binomial noise has vanishing second moment:

$$\mathbb E\left[\left(\frac{k-D^0}{\sqrt k}-C_n\right)^2\right]
=\mathbb E[q_n(X)(1-q_n(X))]
\le\frac{\mathbb EC_n}{\sqrt k}\longrightarrow0.$$

Combining this with the earlier $L^2$ comparison from $D^0$ to $D$ proves the candidate distribution and moment conclusions.

## Two independent calculations of the constants

Let $Z,Z_1,Z_2$ be independent standard normal variables. Conditioning on $Z$ gives

$$\mathbb E g(Z)=\mathbb E(Z-Z_1)_+=\frac1{\sqrt\pi},$$

and

$$\mathbb E g(Z)^2=\mathbb E[(Z-Z_1)_+(Z-Z_2)_+]
=\frac13+\frac{\sqrt3}{2\pi}.$$

For the last equality, the two differences have variances two and correlation $1/2$. Write them as $\sqrt2 R\cos\theta$ and $\sqrt2 R\cos(\theta-\pi/3)$ in polar coordinates of two independent standard normals. The angle is uniform, $\mathbb ER^2=2$, and the positive overlap is $(-\pi/6,\pi/2)$. Integrating the product of cosines on this interval gives $1/3+\sqrt3/(2\pi)$. Subtracting $1/\pi$ gives $v$ above, approximately $0.29068789486043867$.

A separate consistency calculation starts with the fixed-$k$ Erlang weighted tree root law in Moharrami et al. Its root threshold has law $\operatorname{Gamma}(k+1,1)$, and its conditional degree is binomial with retention probability $\mathbb E\min(\operatorname{Gamma}(k,1),X)/X$. Applying the gamma central limit theorem as $k\to\infty$ gives the same $g(Z)$ limit. This second lane does not replace the exact finite-$n$ comparison above: a sequential local limit alone would not prove the triangular-array theorem.

## A separate sufficient condition for simultaneous concentration

The same source asks for conditions under which degrees concentrate around their mean. A simple sufficient regime is $k/\log n\to\infty$. This uses the source's existing Erdős-Rényi sandwich idea; no novelty is claimed.

Let $\delta=\sqrt{6k\log n}$ and suppose $k>2\delta$. Threshold every uniform edge weight at $t=(k-\delta)/(n-1)$. Write $B_v$ for the resulting degree at vertex $v$, so $B_v\sim\operatorname{Bin}(n-1,t)$ and $\mathbb EB_v=k-\delta$. Chernoff bounds give, for each vertex,

$$\mathbb P(B_v>k)\le n^{-3},\qquad
\mathbb P(B_v<k-2\delta)\le n^{-3}.$$

The upper-tail exponent is at least $\delta^2/(2(k-\delta)+2\delta/3)\ge3\log n$; the lower-tail exponent is at least $\delta^2/(2(k-\delta))\ge3\log n$. A union bound, requiring no independence between vertex degrees, now shows that all threshold degrees lie in $[k-2\delta,k]$ with probability at least $1-2/n^2$.

On this event every threshold edge is among the $k$ preferred edges at both its endpoints. Hence the threshold graph is a subgraph of $LK(n,k)$ and

$$k-2\sqrt{6k\log n}\le D_v\le k\quad\hbox{for every vertex }v.$$

This proves simultaneous relative concentration when $k/\log n\to\infty$. It does not determine optimal tails or the critical logarithmic regime; below the connectivity threshold, isolated vertices already obstruct simultaneous concentration near $k$.

## Checks and remaining limits

An exhaustive independent rank enumeration of all $6!=720$ edge orders on four vertices, for $k=1,2$, found no violation of $D\le D^0\le D+2J$. The degree histograms were $(288,432,0,0)$ and $(48,192,480,0)$, giving means $3/5$ and $8/5$. These means also follow from direct two-endpoint ranking probabilities: a root's nearest edge is mutual with probability $3/5$, while for $k=2$ a given edge is kept with probability $1-2/3+1/5=8/15$. These finite controls are not a proof of the asymptotic theorem.

The fragile steps are the root's $k+1$ order statistic, the outside beta parameter $n-2k$, the $L^2$ rather than mere probability comparison, and moment convergence before standardization. They are exposed explicitly above. Bounded-degree regimes, larger growth regimes, optimal concentration, independent review, and novelty remain unresolved here. No original solution is promoted. The exact enumeration receipt and a retained proof plan are in `bilateral_degree_exact_checks.json` and `bilateral_degree_proof_plan.json`.
