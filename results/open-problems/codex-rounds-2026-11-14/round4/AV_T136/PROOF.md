# Exponential augmentation for finite Gaussian hierarchies

Fix \(m\ge1\), terminal mass \(a>0\), and masses
\(0<v_1\le\cdots\le v_L\le a\). Let \(z_0,\ldots,z_L\) be independent standard Gaussian vectors of finite dimensions. A block may have dimension zero. For spins \(\sigma\in\{-1,1\}^m\), let
\[
H_\sigma(z_0,\ldots,z_L)=\sum_{j=0}^L A_{j,\sigma}\cdot z_j.
\]
Assume that the spin gauge group acts orthogonally on each Gaussian block and satisfies
\[
H_\sigma(T_\eta z)=H_{\sigma\eta}(z)
\quad(\eta\in\{-1,1\}^m).
\tag{1}
\]
Completed Gaussian SK matrix increments and independent centered Gaussian spin-field increments satisfy this assumption. There is no deterministic external field.

Explicitly, a block with clock increments \(\Delta b_j,\Delta h_j\ge0\) contributes
\[
\sqrt{\frac{\Delta b_j}{2m}}\sum_{p,q=1}^m z_{j,pq}\sigma_p\sigma_q
+\sqrt{\Delta h_j}\sum_{p=1}^m w_{j,p}\sigma_p.
\]
Its covariance is \(m(\Delta b_j Q^2/2+\Delta h_j Q)\). The gauge sends \(z_{j,pq}\) to \(\eta_p\eta_q z_{j,pq}\) and \(w_{j,p}\) to \(\eta_p w_{j,p}\). These are orthogonal sign changes preserving the independent standard Gaussians. The diagonal matrix contribution is spin-constant and supplies the usual Gaussian completion.

Define
\[
F_L(z_0,\ldots,z_L)
=a^{-1}\log\left(2^{-m}\sum_\sigma e^{aH_\sigma(z)}\right),
\]
and recursively, for \(i=L,\ldots,1\),
\[
F_{i-1}(z_0,\ldots,z_{i-1})
=v_i^{-1}\log\int e^{v_iF_i(z_0,\ldots,z_i)}\,d\gamma_i(z_i).
\tag{2}
\]
Write \(G(z_0)=F_0(z_0)\). The law considered for \(G\) is its law under the original Gaussian \(\gamma_0\).

**Proposition.** If \(L\ge1\) and \(0<\rho\le v_1\), then \(G+E_\rho\) has a log-concave density, where \(E_\rho\) is independent exponential noise of rate \(\rho\). If \(L=0\), the same holds for \(0<\rho\le a\). Empty levels may be removed first. The assertion passes to every weak limit of such \(G\)'s with the same positive admissible rate.

Consequently, at each fixed system size, this proves augmentation for finite-step realizations of the physical clocks in Sections 2–4 of OpenAI, *The low-temperature Sherrington–Kirkpatrick free-energy limiting law* (September 24, 2026), and for their defining weak limits. The rate there is \(\rho=x/2\). The argument below also proves the stated uniform \(L^p\) bound on the stopped set. It does not establish the stopped pressure-increment proposition or the SK fluctuation theorem.

## 1. Convexity and integrability

The terminal continuation is convex in its full Gaussian prefix. If \(F_i\) is convex, then for two prefixes \(r,r'\) and \(0<\theta<1\), pointwise convexity and Hölder give
\[
\begin{aligned}
\int e^{v_i F_i(\theta r+(1-\theta)r',z_i)}d\gamma_i
&\le \int e^{\theta v_iF_i(r,z_i)+(1-\theta)v_iF_i(r',z_i)}d\gamma_i\\
&\le
\left(\int e^{v_iF_i(r,z_i)}d\gamma_i\right)^\theta
\left(\int e^{v_iF_i(r',z_i)}d\gamma_i\right)^{1-\theta}.
\end{aligned}
\]
Taking logarithms proves convexity of \(F_{i-1}\).

For each block, put \(M_j=\max_\sigma|A_{j,\sigma}|\). The terminal continuation is \(M_j\)-Lipschitz in block \(j\). Each earlier log-Laplace operation preserves that Lipschitz bound in every surviving block: a uniform additive bound on its input gives the same additive bound on its output. In particular all integrals in (2) are finite, the continuations have at most linear growth in their surviving Gaussian variables, and \(G\) has finite moments of every order and finite exponential moments at every fixed real argument.

Induction in (2), changing Gaussian variables by \(T_\eta\) at each step, also gives gauge invariance of every continuation.

## 2. The positive law and the pin

Relative to the product Gaussian measure, the forward driver density is
\[
\prod_{i=1}^L \exp\{v_i(F_i-F_{i-1})\}.
\tag{3}
\]
For every fixed earlier prefix, each factor integrates to one in its new block by (2). Integrating future blocks in reverse order therefore gives one. Under (3), \(z_0\) has its original Gaussian marginal.

After the drivers, draw a terminal spin with conditional probability
\[
2^{-m}\exp\{aH_\sigma-aF_L\}.
\tag{4}
\]
This also integrates to one. Thus (3)–(4) define a probability law \(\mathbb P_*\), and the law of \(G\) under \(\mathbb P_*\) is its original law.

The map \((z,\sigma)\mapsto(T_\eta z,\sigma\eta)\) preserves this joint law. It preserves \(G\), and it acts transitively on the spins. Hence for every Borel set \(B\) the numbers
\(\mathbb P_*(G\in B,\sigma=\tau)\) are equal for all \(\tau\). Summing over the \(2^m\) spins gives
\[
\mathbb P_*(G\in B,\sigma=\tau)
=2^{-m}\mathbb P_*(G\in B).
\tag{5}
\]
In particular every spin has probability \(2^{-m}\), and conditioning on any fixed spin leaves the distribution of \(G\) unchanged.

Equation (5) asserts preservation of the distribution of \(G\). It does not assert preservation of the full initial-driver marginal after pinning.

## 3. Telescoping the pinned density

Fix the pinned spin \(\sigma^+=(1,\ldots,1)\). The factors \(2^{-m}\) in (4) and \(2^m\) from conditioning cancel. The driver density after pinning, relative to the product Gaussian measure, is
\[
\begin{aligned}
&\exp\left\{\sum_{i=1}^L v_i(F_i-F_{i-1})+aH_{\sigma^+}-aF_L\right\}\\
&=\exp\left\{aH_{\sigma^+}
-v_1G-\sum_{i=1}^{L-1}(v_{i+1}-v_i)F_i-(a-v_L)F_L\right\}.
\tag{6}
\end{aligned}
\]
For a second check, the coefficient of \(F_i\), \(1\le i<L\), is \(v_i-v_{i+1}\), that of \(F_0\) is \(-v_1\), and that of \(F_L\) is \(v_L-a\). Their negative coefficients sum to \(a\).

Adjoin independent \(E_\rho\) and set \(u=G+E_\rho\). Relative to Lebesgue measure on all standard drivers and \(u\), the joint density is
\[
\rho\prod_{j=0}^L\phi_j(z_j)
\exp\left\{aH_{\sigma^+}-(v_1-\rho)G
-\sum_{i=1}^{L-1}(v_{i+1}-v_i)F_i
-(a-v_L)F_L-\rho u\right\}
\mathbf1_{\{u\ge G\}}.
\tag{7}
\]
Integrating first in \(u\) recovers the pinned density (6), so (7) is normalized.

All the coefficients preceding the convex continuations in (7) are nonnegative. The log Gaussian density is concave, \(aH_{\sigma^+}-\rho u\) is affine, and \(\{u\ge G\}\) is a convex epigraph. Thus (7), extended by zero, is log-concave. Prékopa's marginal theorem gives a log-concave density for \(u\). By (5), its distribution is the original law of \(G+E_\rho\).

If \(L=0\), the same computation starts with the pinned density
\(\phi_0 e^{aH_{\sigma^+}-aG}\), and (7) has coefficient \(a-\rho\). This is the bare-system case, with arbitrary terminal mass \(a\).

## 4. Empty levels and the physical lower cut

If a Gaussian increment at level \(v_i\) is zero, (2) gives \(F_{i-1}=F_i\). The adjacent terms in (6) combine. Repeating removes every empty level. If the first nonzero future increment is at mass \(w\), the coefficient of \(G\) is \(w\); if there is no future increment it is \(a\).

Here is the lower-cut check directly from the physical clock formulas.

* In Section 3, \(G_{\mathrm{cut}}(v)\) in (P3) is zero on \([0,x]\). The other varying terms there have supports \(v/u\in[1/2,4]\), with \(u\ge16x\); they vanish below \(8x\). Therefore the matrix clock \(b(v)\) is constant for \(0<v<x\).
* The prescription just before (P6) sets the actual field clock \(h(v)\) to zero for \(v<x\). This concerns the actual clock, even though its auxiliary scalar reference \(K(v)\) varies there.
* Varying the strength or the two multipliers preserves these restrictions. Both direct and smoothed clocks use the same cutoffs.
* Direct paths have \(a=\ell\ge1\), smoothed paths have \(a=4\), and \(x=N^{-1/6}\le1\). The hard extension in the switching argument introduces its additional jump at mass \(\ell\ge x\).

Thus any finite-step approximation respecting the constant initial interval can put its first nonzero future increment at mass at least \(x\). Empty intermediate levels change no coefficient. With \(\rho=x/2\), the coefficient of \(G\) remaining in (7) is at least \(x/2\). This check does not require the estimates proving clock admissibility; it applies to each nonnegative nondecreasing clock satisfying the displayed cutoff.

Under terminal-mass normalization \(\widetilde v=v/a\), \(\widetilde F=aF\), the exponent \(vF\) becomes \(\widetilde v\widetilde F\). The augmented variable becomes \(a(G+E_\rho)\), whose independent exponential has rate \(\rho/a\), not \(\rho\). Hence the remaining normalized coefficient is
\[
\frac{v_1}{a}-\frac{\rho}{a}
=\frac{v_1-\rho}{a}\ge\frac{x}{2a}.
\tag{8}
\]
It stays positive for \(a=4\). Rescaling the continuation without also rescaling the exponential rate would give an incorrect sign.

## 5. Passage to fixed-site weak limits

Fix \(m,x>0\), and let \(G_k\Rightarrow G\) along finite-step hierarchies of this type. Keep \(\rho=x/2\) fixed. Independence and bounded-continuous test functions give
\(G_k+E_\rho\Rightarrow G+E_\rho\).

Every random variable \(X+E_\rho\), for arbitrary real \(X\), has density
\[
f(u)=\mathbb E\left[\rho e^{-\rho(u-X)}
\mathbf1_{\{X\le u\}}\right]\le\rho.
\tag{9}
\]
Fubini proves this density formula; it implies that the limiting law has no atoms.

For \(\delta>0\), put
\[
f_{k,\delta}(u)
=\frac{\mathbb P(G_k+E_\rho\in[u-\delta,u+\delta])}{2\delta}.
\]
It is log-concave by convolution of the log-concave density already proved with the uniform density on \([-\delta,\delta]\), using Prékopa's theorem. Weak convergence and the absence of atoms in (9) give convergence to \(f_\delta(u)\) for every \(u\). The defining log-concavity inequality passes to this pointwise limit. Lebesgue differentiation gives \(f_\delta\to f\) almost everywhere as \(\delta\downarrow0\); the limiting density has a log-concave representative. Equivalently, this is the weak closure of log-concave probability measures, with absolute continuity supplied separately by (9).

The conclusion concerns every such weak limit. The source defines its bounded monotone-clock laws through fixed-site step limits. Existence and identification of those limits are a separate input from its foundations; no limit in system size or quantitative approximation rate is used here.

For the physical clocks, the initial driver can always be realized in the same fixed \(m^2\)-dimensional ordered-matrix space. Its coefficient norm is \(M_{0,k}=\sqrt{m b_k(0+)/2}\), uniformly bounded for an approximation of one fixed clock. Hence \(G_k\) are uniformly Lipschitz functions of this one standard Gaussian vector. Their weakly convergent laws are tight. Tightness and the Lipschitz bound imply that \(G_k(0)\) is bounded: choose \(R\) with \(\mathbb P(|z_0|\le R)>3/4\) and a uniform tightness interval with probability greater than \(3/4\); their intersection has positive probability and bounds \(|G_k(0)|\) by the interval radius plus \(R\sup_k M_{0,k}\). Consequently \(|G_k(z_0)|\le C+M|z_0|\), uniformly in \(k\). Gaussian integrability and the lower-semicontinuous version of weak convergence imply finite moments and finite exponential moments of all fixed orders for \(G\). This supplies the integrability used next for these physical limits.

## 6. A uniform stopped \(L^p\) bound

The following estimates are independent of the number of hierarchy levels, the clocks and system size. For finite hierarchies the finite-moment hypotheses follow from Section 1; the same argument applies to any fixed-site limit with finite variance and the stated finite Laplace transform.

For a centered variable \(W\) with a log-concave density and variance \(d^2>0\), log-concavity of its survival functions and Chebyshev give
\[
\mathbb P(|W|\ge td)\le\tfrac12
\exp\{-A(t-2)\}\quad(t\ge2),\qquad A=\frac{\log3}{4}.
\tag{10}
\]
Indeed \(S(2d)\le1/4\), \(S(-2d)\ge3/4\), and concavity of \(\log S\) bounds its slope after \(2d\) by \(-(\log3)/(4d)\). Apply the same argument to \(-W\) and add. Integrating (10), with \(b=A/2\), yields
\[
\mathbb E e^{b|W|/d}\le K,\qquad
K=\tfrac32\,3^{1/4}.
\tag{11}
\]
The integral is
\(e^{2b}+(b/2)e^{2b}/(A-b)=K\).

For completeness, a uniform right-tail lower bound can also be derived from (11), rather than assumed. Put \(C=24K/b^4\). Since \(t^4\le24b^{-4}e^{bt}\) for \(t\ge0\), (11) gives \(\mathbb EW^4\le Cd^4\). Hölder gives
\[
d^2\le(\mathbb E|W|)^{2/3}(\mathbb EW^4)^{1/3},
\qquad
\mathbb E W_+=\tfrac12\mathbb E|W|\ge\frac{d}{2\sqrt C}.
\]
If \(\mu=\mathbb E W_+\), then
\[
\mu\le\mu/2+
\big(\mathbb E W_+^2\,\mathbb P(W_+\ge\mu/2)\big)^{1/2}
\]
by splitting at \(\mu/2\) and applying Cauchy–Schwarz. As
\(\mathbb E W_+^2\le d^2\), it follows that
\[
\mathbb P\left(W\ge\frac d{4\sqrt C}\right)\ge\frac1{16C}.
\]
Thus \(c=\min\{(4\sqrt C)^{-1},(16C)^{-1}\}>0\) satisfies
\[
\mathbb P(W\ge cd)\ge c.
\tag{12}
\]

Now take
\[
W=G+E_{x/2}-\mathbb E(G+E_{x/2}),\qquad
\mathcal K(s)=\log\mathbb E e^{s(G-\mathbb EG)},
\]
with \(s=q x^{1+\varepsilon}>0\), and assume
\(\mathcal K(s)\le3x^\varepsilon\). For sufficiently small \(x\),
\(t=2s/x=2q x^\varepsilon\le1/2\), and independence gives
\[
\delta:=\log\mathbb E e^{sW}
=\mathcal K(s)-\log(1-t)-t
\le3x^\varepsilon+t^2.
\tag{13}
\]
The last inequality follows from
\(\sum_{j\ge2}t^j/j\le t^2/[2(1-t)]\le t^2\).
Since \(e^u-1-u\ge0\) for all real \(u\), and at least \(u^2/2\) for \(u\ge0\), (12) implies
\[
\frac{c^3}{2}(sd)^2
\le\mathbb E(e^{sW}-1-sW)
=e^\delta-1.
\tag{14}
\]
For small \(x\), \(\delta\le1\), so
\(sd\le[2e(3+4q^2)/c^3]^{1/2}x^{\varepsilon/2}\).
This tends to zero uniformly over the stopped family.

For every fixed \(1\le p<\infty\), eventually \(psd\le b\), and (11) gives
\(\mathbb E e^{psW}\le K\). Conditional Jensen over the centered independent exponential transfers this estimate to \(G-\mathbb EG\). Since \(\mathcal K(s)\ge0\),
\[
\left\|\frac{e^{sG}}{\mathbb E e^{sG}}\right\|_p^p
=e^{-p\mathcal K(s)}
\mathbb E e^{ps(G-\mathbb EG)}
\le K.
\tag{15}
\]
The threshold may depend on \(p,q,\varepsilon\); the bound does not depend on the path or the number of levels. Orders below one are bounded as well by Jensen applied to the normalized density. This proves the stopped density-norm assertion under the stated fixed-site integrability conditions.

## 7. Boundary checks

The proof includes \(\rho=v_1\), repeated masses, \(v_L=a\), zero covariance increments, a degenerate initial driver, and a hierarchy with no future increments. It uses the original Gaussian law only for \(G\)'s initial driver; replacing it by a tilted root law changes the assertion. Random centered future spin fields preserve the gauge, whereas a deterministic external field generally does not.

The conditional statement about the stopped family supplies no bound showing that the stop holds along the comparison path. In particular (15) is not the pressure-increment estimate and does not establish variance asymptotics or a limiting law for SK.
