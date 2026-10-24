# Central-level near-coloop receiver from a physical independent square component

Run UTC: 2026-09-23 20:37. Target: independent cap-one original coordinates, arbitrary real \(\beta,\epsilon\), near-coloop
\[
Q=2HL+\beta L^2+V^2+2\epsilon LP.
\]
Status: **proved scoped result, full QFORM conjecture open**. In this report \(H\) is a physical original-coordinate scalar independent of all leaves. Dependence between \(L\) and \(P\) is unrestricted. The additional hypothesis is an independent scalar component of \(V\) whose density is capped quantitatively.

## Lemma 1: bounded-density product band at bounded target

Suppose a real pair \((L,U)\) has a joint density \(g\le K\), and its two marginal densities satisfy \(p_L\le K\), \(p_U\le1\), with \(K\ge1\). For every \(|c|\le1\) and \(0<t\le1\),
\[
\boxed{\Pr\{c<2LU<c+t\}\le 2Kt+2t+2Kt\log(1/t).}\tag{1}
\]
The same bound holds with \(-2LU\) in place of \(2LU\).

**Proof.** Split by \(|L|\le t\), \(t<|L|\le t^{-1}\), and \(|L|>t^{-1}\). The first probability is at most \(2Kt\). For each fixed \(l\) in the middle region, the admissible \(u\) interval has length \(t/(2|l|)\); integrating the joint cap over both signs of \(l\) gives
\[
\frac{Kt}{2}\int_{t<|l|\le t^{-1}}\frac{dl}{|l|}
=2Kt\log(1/t).
\]
In the last region, \(|2lu|\le|c|+t\le1+t\) implies \(|u|\le(1+t)t/2\le t\). The \(U\)-marginal cap gives \(2t\). Signs and locations of supports play no role. Replacing \(u\) by \(-u\) proves the last claim. QED.

## Theorem 2: an independent square scalar pays every central target

Let \((L,U,W)\) be jointly distributed, let \(Z\) be independent of this triple with density \(p_Z\le B\), and suppose \(g_{L,U}\le K\), \(p_L\le K\), \(p_U\le1\), \(K\ge1\). Set
\[
Q_*=2LU+(W+Z)^2.
\]
Then \(Q_*\) has a density and
\[
\boxed{\sup_{|s|\le1}p_{Q_*}(s)\le B(6K+3)}\tag{2}
\]
for an almost-everywhere version of the density. This holds for arbitrary dependence of \(W\) on \((L,U)\) and arbitrary real translations.

**Proof.** Conditional on \((L,U,W)\), \(W+Z\) has a density at most \(B\), so the positive square \((W+Z)^2\) has a conditional density bounded by \(B y^{-1/2}\) for \(y>0\), uniformly in \(W\). Consequently, for each \(|s|\le1\),
\[
p_{Q_*}(s)\le B\,\mathbb E[(s-2LU)^{-1/2}\mathbf1_{\{s>2LU\}}].
\]
Put \(T=-2LU\) and \(a=-s\). Its expectation equals
\[
\frac12\int_0^\infty t^{-3/2}\Pr\{a<T<a+t\}\,dt.
\]
For \(0<t\le1\), (1) applies because \(|a|\le1\). The integral of \(t^{-3/2}[2Kt+2t+2Kt\log(1/t)]/2\) over \((0,1)\) is \(6K+2\), since \(\int_0^1t^{-1/2}dt=2\) and \(\int_0^1t^{-1/2}\log(1/t)dt=4\). The tail \(t\ge1\) contributes at most \(1\). All integrals are finite, and Tonelli plus the conditional square density establishes absolute continuity and (2). QED.

## Corollary 3: original-product near-coloop with a literal independent \(V\) component

Let all original \(X_i\) have independent densities at most one, with \(H\) a distinct original coordinate. Let \(L=\ell\cdot X\), \(P=p\cdot X\), \(V=v\cdot X\) be orthonormal linear forms on the leaves, with no restriction on overlapping support of \(L\) and \(P\). Suppose a subset \(T\) of the original leaves satisfies
\[
\ell_i=p_i=0\quad(i\in T),\qquad
\rho=\|v_T\|_2>0.
\]
Write \(V=W+Z\), \(W=v_{T^c}\cdot X_{T^c}\), \(Z=v_T\cdot X_T\). Then \(Z\) is independent of \((H,L,P,W)\). For all real \(\beta,\epsilon\), define
\[
U=H+\tfrac\beta2 L+\epsilon P.
\]
As \(H\) is independent with \(p_H\le1\), conditioning on \((L,P)\) gives
\[
g_{L,U}(l,u)
=\int f_H(u-\tfrac\beta2l-\epsilon p)\,d\mu_{L,P}(p\mid l)\,p_L(l)
\le p_L(l),\qquad p_U(u)\le1.
\]
The sharp one-dimensional marginal theorem for product densities gives \(p_L\le\sqrt2\) and \(p_Z\le\sqrt2/\rho\). Hence Theorem 2 proves
\[
\boxed{\sup_{-1\le s\le0}p_Q(s)
\le \frac{12+3\sqrt2}{\rho}.}\tag{3}
\]
In fact the same bound holds for every \(|s|\le1\). The reference for the one-dimensional \(\sqrt2\) product-marginal input is Livshyts, Paouris and Pivovarov, *On sharp bounds for marginal densities of product measures*, Theorem 1.1, [arXiv:1507.07949](https://arxiv.org/abs/1507.07949): every orthogonal \(k\)-dimensional marginal of a product of cap-one probability densities is bounded by \(2^{k/2}\). If \(Z\) is a single physical coordinate with coefficient \(\rho\), then \(p_Z\le1/\rho\) and (3) improves to \((6\sqrt2+3)/\rho\).

A fully separated \(V\) bank has \(\rho=1\), giving \(12+3\sqrt2<16.25\); nonzero overlap between \(V\) and the \((L,P)\) source bank is allowed if it retains a disjoint piece of norm \(\rho\).

## Exact remaining obligation

When **every** coordinate supporting \(V\) also contributes to \(L\) or \(P\), there need not be any \(\rho>0\). Conditioning on the physical sources then correlates the square variable with \((L,U)\); the square-density estimate in Theorem 2 cannot be used. An arbitrary capped three-dimensional projected law can concentrate on a curved surface, so replacing genuine product provenance by a bare joint-density cap is unjustified. This report supplies no dimension-uniform bound in that fully overlapping case and neither proves nor disproves the full theorem.
