# Entropy concavity on every kernel line through a diagonal contraction

Status: parent-derived complete argument, awaiting an independent adversarial audit. This note is not yet promoted into the principal proof packet. The unrestricted Lyons conjecture remains open. No historical priority or formal verification is claimed.

## Theorem

Let \(D=\operatorname{diag}(d_1,\ldots,d_n)\), with \(0<d_i<1\), and let \(A\) be any Hermitian matrix. On the entire closed feasible interval
\[
I=\{s\in\mathbb R:0\preceq D+sA\preceq I_n\},
\]
the Shannon entropy of the determinantal subset law \(P_{D+sA}\) is concave. It is strictly concave if \(A\ne0\). There is no restriction on the dimension, the rank of \(A\), its diagonal, or its complex phases.

In particular, every line through \(I_n/2\) is covered, as is every complement interpolation between \(K\) and \(I_n-K\). The result includes endpoints with zero atom probabilities by continuity. It concerns lines through a diagonal kernel; it does not imply concavity on arbitrary lines between two nondiagonal kernels.

## 1. A product-resampling entropy lemma

Let \(\mu\) be a product of Bernoulli laws with parameters in \((0,1)\), and let \(f\ge0\) be any density relative to \(\mu\), with \(\mathbb E_\mu f=1\). Let \(E_i\) average over coordinate \(i\) using its Bernoulli marginal, and put \(D_i=I-E_i\). These commuting operators satisfy \(D_i^2=D_i\). Define
\[
N_t=\prod_{i=1}^n(E_i+tD_i),\qquad f_t=N_tf,\qquad 0\le t\le1.
\]
This retains each input coordinate with probability \(t\), and independently redraws it from its reference marginal otherwise. The operators act on densities because they are reversible with respect to \(\mu\).

**Lemma.** The relative entropy
\[
F(t)=\mathbb E_\mu[f_t\log f_t]
\]
is convex on \([0,1]\), and \(F''(t)>0\) for \(0<t<1\) unless \(f=1\).

To prove this, let \(L=\sum_iD_i\). The product expansion in joint eigenspaces gives, for \(t>0\),
\[
t f_t'=Lf_t,\qquad t^2f_t''=(L^2-L)f_t.
\]
For \(t<1\), every density value is positive, since the event of redrawing all coordinates has probability \((1-t)^n>0\). Differentiating the finite entropy sum, and writing \(g=f_t\), gives
\[
\begin{aligned}
t^2F''(t)
={}&\sum_i\mathbb E_\mu\frac{(D_ig)^2}{g}\\
&+2\sum_{i<j}\left[
\mathbb E_\mu\frac{D_igD_jg}{g}
+\mathbb E_\mu(D_iD_jg)\log g\right].
\tag{1}
\end{aligned}
\]
The diagonal terms of \(L^2-L\) vanish by idempotence; its off-diagonal terms are exactly twice the unordered pair sum. No second-derivative term has been discarded.

We verify each bracket in (1) is nonnegative. Condition on every coordinate except \(i,j\), let their Bernoulli parameters be \(p,q\), and denote the four positive density values by
\[
a=g(0,0),\quad b=g(0,1),\quad c=g(1,0),\quad d=g(1,1).
\]
Direct expansion of the two conditional averages gives the bracket, on this fiber, as \(p(1-p)q(1-q)\) times
\[
\frac{bc}{a}+\frac{ad}{b}+\frac{ad}{c}+\frac{bc}{d}
-(a+b+c+d)+(a+d-b-c)\log\frac{ad}{bc}.
\tag{2}
\]
For explicit verification, the first four fractional terms minus the sum are obtained by expanding
\[
\frac{(a-c)(a-b)}a+rac{(b-d)(b-a)}b
+\frac{(c-a)(c-d)}c+rac{(d-b)(d-c)}d.
\]
The log term follows because the four weighted values of \(D_iD_jg\) have common magnitude \(p(1-p)q(1-q)(a-b-c+d)\) and alternating signs.

Set \(r=ad/(bc)\), \(X=a+d\), \(Y=b+c\). Expression (2) is exactly
\[
X(r^{-1}-1+\log r)+Y(r-1-\log r)\ge0.
\tag{3}
\]
Both scalar factors are nonnegative by \(\log u\le u-1\), applied to \(u=r\) and \(u=1/r\). Thus (1) is nonnegative. If it vanishes, every single-coordinate square term vanishes, so \(D_ig=0\) for all \(i\). A function independent of every coordinate is constant, and normalization makes it one. Since \(N_t\) is invertible for \(t>0\), this forces \(f=1\). Otherwise \(F''(t)>0\). Continuity of the finite entropy sum extends convexity to both endpoints and proves the lemma.

## 2. Product resampling acts affinely on a DPP kernel

Fix any Hermitian contraction \(K\). Let \(X\) have law \(P_K\), and independently retain or redraw coordinates as above, with reference \(\mu=P_D\). Call the resulting set \(Y_t\). For every subset \(S\),
\[
\begin{aligned}
\Pr(S\subseteq Y_t)
&=\sum_{T\subseteq S}t^{|T|}(1-t)^{|S\setminus T|}
\det K_T\prod_{i\in S\setminus T}d_i\\
&=\det\big(tK_S+(1-t)D_S\big).
\tag{4}
\end{aligned}
\]
The last identity follows by multilinearity in columns: the diagonal columns selected from \(D_S\) force their matching rows, leaving the principal minor \(K_T\), with positive cofactor sign. The probabilities of all inclusion events determine a finite subset law by inclusion-exclusion. Hence
\[
\boxed{\operatorname{Law}(Y_t)=P_{D+t(K-D)}.}
\tag{5}
\]
This identity permits changing diagonal entries as well as changing correlations. It does not assume that \(K\) and \(D\) commute.

## 3. Convert relative entropy into Shannon entropy

Let \(p_t=P_{D+t(K-D)}\). Its one-site marginals are affine:
\[
m_i(t)=d_i+t(K_{ii}-d_i).
\]
Since \(\log\mu(x)=\sum_i[x_i\log d_i+(1-x_i)\log(1-d_i)]\), the cross-entropy
\[
-\sum_xp_t(x)\log\mu(x)
=-\sum_i[m_i(t)\log d_i+(1-m_i(t))\log(1-d_i)]
\tag{6}
\]
is affine in \(t\). Therefore
\[
H(p_t)=\text{the affine expression (6)}-F(t)
\]
is concave, and has strictly negative second derivative on \((0,1)\) unless \(P_K=P_D\).

The latter equality forces \(K=D\): one-site events give \(K_{ii}=d_i\); two-site events give
\(K_{ii}K_{jj}-|K_{ij}|^2=d_id_j\), hence \(K_{ij}=0\). Thus every chord from an interior diagonal kernel to a distinct arbitrary contraction is strictly concave.

For a full line \(D+sA\), the positive and negative feasible halves each have the preceding representation, using their respective outer endpoints. The entropy is analytic near \(s=0\), where the law has full support, so the two first derivatives agree. Two concave halves whose derivatives agree at the meeting point form a concave function on the whole interval. If \(A\ne0\), neither half contains a nontrivial affine interval, giving strict concavity throughout the full feasible interval. This proves the theorem.

A diagonal reference with entries equal to zero or one can be treated for a single chord by approximation \(D_\epsilon=(1-2\epsilon)D+\epsilon I_n\) and entropy continuity. Strictness at these degenerate references is not asserted by this approximation alone.

## 4. Quantitative curvature and the flat midpoint

The nonnegative pair terms in (1) also yield, on the chord parameterization,
\[
-H''(p_t)\ge\frac1{t^2}\sum_i\mathbb E_\mu\frac{(D_if_t)^2}{f_t}
\ge\sum_i\frac{(K_{ii}-d_i)^2}{m_i(t)(1-m_i(t))},\qquad 0<t<1.
\tag{7}
\]
For the second inequality, condition on coordinate \(i\) and apply Cauchy–Schwarz in the form \(\mathbb E(U^2/V)\ge(\mathbb EU)^2/\mathbb EV\). The conditional expectations of \(D_if_t\) are \(t(K_{ii}-d_i)/d_i\) at one and its negative counterpart \(-t(K_{ii}-d_i)/(1-d_i)\) at zero. The corresponding conditional densities are \(m_i(t)/d_i\) and \((1-m_i(t))/(1-d_i)\), giving exactly the last sum.

For a zero-diagonal direction, this marginal lower bound vanishes, while the full first inequality is strict away from the diagonal point. At the diagonal point itself the second derivative can vanish. The previously derived expansion from report023 still gives
\[
H(P_{D+sA})=\sum_i h(d_i)
-\frac{s^4}{2}\sum_{i<j}\frac{|A_{ij}|^4}{d_i(1-d_i)d_j(1-d_j)}+O(s^6)
\]
when \(A_{ii}=0\). Thus strict concavity on a full line is compatible with a flat second derivative at its central point.

## Dependencies, attribution and remaining checks

The proof uses only finite product averages, the elementary logarithm inequality, the determinantal inclusion formula and entropy continuity. Product resampling at fixed diagonals was already derived in report058. Report039 credits Gu's established thinning-relative-entropy argument for the scalar-ray case; that case is not new here. The binary resampling lemma above has been proved explicitly rather than imported as an unverified entropy-curvature assertion.

Primary context: [Lyons, *Determinantal Probability: Basic Properties and Conjectures*](https://arxiv.org/abs/1406.2707); [Gu, *Entropy of Determinantal Point Processes*](https://sevenkplus.com/data/dpp.pdf). These references identify the target and prior scalar-ray work; no complete historical-priority audit of this diagonal-endpoint extension has been performed.

An independent worker must audit every identity, the density-versus-law convention, complex-kernel resampling, both feasible halves, strictness, and the quantitative bound before integration. A search result about noise monotonicity by itself does not establish convexity in the retention parameter. General kernel lines whose endpoints are both nondiagonal remain outside this argument.
