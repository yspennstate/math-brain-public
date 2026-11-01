# Stronger uniform-all-level product-band receiver

This addendum improves the bounded-target estimate in the companion [REPORT.md](https://github.com/yspennstate/math-open-problems/blob/06480f5486450bc5b4230280ecbd5ae89a687d88/proofnet24/QFORM-density/interactive/20260923T203741Z-independent-v-square-product-band/REPORT.md). The earlier inequalities are true, but the actual physical-H convolution supplies a stronger *conditional* cap and removes the restriction \(|s|\le1\).

## Global band lemma

Let \(L,U\) have a joint density satisfying
\[
g_{L,U}(l,u)\le p_L(l),\qquad p_L(l)\le K\quad(K\ge1)
\]
almost everywhere. Thus the conditional law of \(U\) given \(L=l\) has density at most one. Then for every real \(c\) and \(0<t\le1\),
\[
\boxed{\Pr\{c<2LU<c+t\}
\le t\left(2K+K\log(1/t)+\tfrac12\right).}\tag{A1}
\]
The estimate also holds for \(-2LU\).

**Proof.** The region \(|L|\le t\) costs at most \(2Kt\). For \(t<|L|\le1\), each fixed \(l\) allows a \(u\)-interval of length \(t/(2|l|)\). Use \(g(l,u)\le p_L(l)\le K\) and integrate: \(Kt\log(1/t)\). For \(|L|>1\), the conditional cap gives probability at most \(t/(2|l|)\le t/2\), and \(p_L\) has total mass one. This yields (A1) with **no target-center dependence**.

## Global density theorem

Let \(Z\) be independent of \((L,U,W)\), with density at most \(B\), while the preceding conditional and marginal hypotheses hold. For
\[
Q=2LU+(W+Z)^2
\]
the conditional squared-variable density is at most \(B(s-2LU)^{-1/2}\mathbf 1_{\{s>2LU\}}\). Layer cake and (A1), now valid for center \(-s\) for **any \(s\in\mathbb R\)**, give
\[
\begin{aligned}
p_Q(s)
&\le \frac B2\int_0^\infty t^{-3/2}
\Pr\{-s<-2LU<-s+t\}\,dt\\
&\le B\left(
\frac12\int_0^1t^{-1/2}[2K+K\log(1/t)+\tfrac12]dt
+\frac12\int_1^\infty t^{-3/2}dt\right)\\
&=\boxed{B(4K+\tfrac32)}.\tag{A2}
\end{aligned}
\]
Here \(\int_0^1t^{-1/2}dt=2\), \(\int_0^1t^{-1/2}\log(1/t)dt=4\), and the tail integral is one. This is a uniform essential-supremum density bound at every target, without moments, bounded supports, signs, or special \(L,P\) dependence.

For the original near-coloop form \(Q=2HL+\beta L^2+V^2+2\epsilon LP\), take \(U=H+\beta L/2+\epsilon P\). Physical independent \(H\) with \(f_H\le1\) implies \(g_{L,U}(l,u)\le p_L(l)\), uniformly \(\beta,\epsilon\). If \(V=W+Z\) with \(Z\) an independent scalar contributed by original coordinates unused by both \(L\) and \(P\), \(\rho=\|v_T\|_2>0\), then the sharp cap-one product-marginal theorem yields \(K=\sqrt2\) and \(B=\sqrt2/\rho\). Therefore
\[
\boxed{\|p_Q\|_\infty\le\frac{8+\frac32\sqrt2}{\rho}
<\frac{10.13}{\rho}.}\tag{A3}
\]
If \(Z\) is exactly one original coordinate times \(\rho\), use \(B=1/\rho\) for \((4\sqrt2+3/2)/\rho\). All actual overlapping sources of \(L\) and \(P\) remain allowed. The all-overlap case \(\rho=0\) still requires a new argument; this addendum does not settle the full QFORM conjecture.
