# The full hierarchy of projection-density caps does not control an indefinite quadratic pushforward

**Status:** proved obstruction to a projection-only lemma. The unrestricted product-input QFORM conjecture remains **OPEN**. This interactive report is not a scheduled-worker sign-in.

## The scoped theorem

Put \(q(u,v,w)=2uv+w^2\). Its symmetric matrix has eigenvalues \(1,-1,1\), so \(s_3=1\). For every sufficiently small \(0<\delta\le1/16\), there is a probability density \(g_\delta\) on \(\mathbb R^3\) such that

\[
\|g_\delta\|_\infty<1,\qquad
\sup_{\dim E=k}\|p_{\pi_E Y}\|_\infty\le2^{k/2}
\quad(k=1,2,3),\qquad Y\sim g_\delta,                 \tag{1}
\]

where \(\pi_E\) is orthogonal projection. Nevertheless,

\[
\mathbb P(|q(Y)+1|\le\delta)
 \ge\frac{\delta}{1024}\log(1/\delta),\qquad
\|p_{q(Y)}\|_\infty
 \ge\frac1{2048}\log(1/\delta).                         \tag{2}
\]

The caps in (1) are exactly the numerical bounds supplied by the Livshyts--Paouris--Pivovarov theorem for cap-one product laws. Satisfying the inequalities does **not** characterize projections of such product laws. The law constructed here has dependent three-dimensional coordinates and is **not exhibited as any projection of independent inputs**. Thus (2) refutes only a proposed proof step that discards product provenance; it is **not a counterexample to the full conjecture**.

This strengthens the earlier fleet01/B06 correction, which refutes use of the two-dimensional X-ray cap alone but uses a shell with a joint-density peak growing with \(\delta^{-1}\) or a fractional power thereof. Here the joint cap and the one-dimensional cap are preserved as well. The earlier result remains stronger in the size of its output-density blowup under its stated, weaker input information.

## Construction and normalization

Set \(R=\delta^{-1/2}\) and

\[
E_\delta=\{(u,v,w):1\le u\le R,\quad0\le w\le1,\quad
                     |2uv+w^2+1|\le\delta\}.
\]

At fixed \((u,w)\), the allowed \(v\)-interval has length \(\delta/u\), and \(v\in[-2,0]\). Hence

\[
|E_\delta|
 =\delta\int_1^R\frac{du}{u}
 =\delta\log R
 =\tfrac{\delta}{2}\log(1/\delta).                       \tag{3}
\]

Let \(c=1/512\), \(m=c|E_\delta|<1\), and
\(h(x)=(2\pi)^{-3/2}\exp(-|x|^2/2)\), the standard three-dimensional Gaussian probability density. Define

\[
g_\delta(x)=c\,\mathbf1_{E_\delta}(x)+(1-m)h(x).          \tag{4}
\]

Its integral is \(c|E_\delta|+(1-m)=1\), and its pointwise peak is at most
\(c+(2\pi)^{-3/2}<1\). Since the first term in (4) puts exactly mass \(m\) inside \([-1-\delta,-1+\delta]\) under \(q\), and the Gaussian term is nonnegative, (3) proves the first bound in (2). The output law is absolutely continuous: on \(E_\delta\), \(\partial_vq=2u\ge2\); the Gaussian component also has a density after a nonconstant quadratic pushforward. Dividing interval mass by length \(2\delta\) proves the second bound in (2).

## Bound on intersections with all affine lines

We deliberately use the comfortable numerical bound

\[
\sup_{\ell\ {\rm affine\ line}}\mathcal H^1(\ell\cap E_\delta)\le64. \tag{5}
\]

Let \(d=(d_u,d_v,d_w)\) be a unit line direction. When \(|d_u|\ge1/2\), use \(u\) as parameter:
\(v(u)=\gamma u+\zeta\), \(w(u)=\alpha u+\beta\). The polynomial

\[
P(u)=2u\,v(u)+w(u)^2+1
\]

has degree at most two and \(P(0)=1+\beta^2\ge1\). Write
\(S=\{u\in[1,R]:|P(u)|\le\delta\}\), \(a=|S|\). If \(a>0\), choose three points \(u_1<u_2<u_3\) in \(S\) at measure quantiles approximately \(a/8,a/2,7a/8\). Since an interval of length \(b\) contains at most \(b\) measure of \(S\), each pairwise distance is at least \(a/4\) (limiting choices suffice). Lagrange interpolation of \(P\) at zero gives

\[
1\le|P(0)|
 \le\sum_{i=1}^3 |P(u_i)|
 \frac{|u_ju_k|}{|u_i-u_j||u_i-u_k|}
 \le\frac{48\delta R^2}{a^2}.
\]

Thus \(a\le\sqrt{48}R\sqrt\delta=\sqrt{48}<7\). Dividing by \(|d_u|\ge1/2\), the physical line length in the shell is below \(14\).

When \(|d_u|<1/2\) and \(|d_w|\ge1/2\), the \(w\)-range has length one, so the line intersection has length at most \(2\). In the remaining case \(|d_v|>1/\sqrt2\), and \(v\in[-2,0]\) gives length at most \(2\sqrt2\). This proves (5), with ample room in the constant \(64\).

## One-, two-, and three-dimensional caps

A two-dimensional orthogonal marginal is the integral of \(g_\delta\) over an affine line. By (5), the shell term contributes at most \(64c=1/8\). A two-dimensional marginal of \(h\) has peak \(1/(2\pi)\), so

\[
\sup_{\dim E=2}\|p_{\pi_E Y}\|_\infty
 \le\tfrac18+(2\pi)^{-1}<2.                              \tag{6}
\]

A one-dimensional marginal integrates over an affine plane \(H\). Choose a unit direction \(r\) in the direction plane of \(H\) with \(r_u=0\); such a direction exists by dimension counting. Because \(v\in[-2,0]\), \(w\in[0,1]\), the coordinate \(r\cdot(u,v,w)=r_vv+r_ww\) has range of length at most \(2|r_v|+|r_w|\le3\) on \(E_\delta\). Foliate \(H\) by lines perpendicular to \(r\) within \(H\); each line has shell intersection length at most \(64\). Fubini gives

\[
\sup_{H\ {\rm affine\ plane}}\mathcal H^2(H\cap E_\delta)\le3\cdot64=192.
\]

The standard one-dimensional Gaussian marginal has peak \((2\pi)^{-1/2}\). Hence

\[
\sup_{\dim E=1}\|p_{\pi_E Y}\|_\infty
 \le192c+(2\pi)^{-1/2}
 =\tfrac38+(2\pi)^{-1/2}<\sqrt2.                        \tag{7}
\]

For \(k=3\), the pointwise bound after (4) is less than one, hence less than \(2^{3/2}\). This completes (1).

## Meaning for the open problem

The previous fleet01/B06 source proved X-ray-only insufficiency:
math-open-problems commit cfb4137e221cd87aeb4f669389d14fa65e3251e7,
path proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260922T120617Z-a01-b06-qform-r11/REPORT.md. Its event is in the current math-research-brain CORRECTION_INBOX. The present calculation proves the stronger information-loss claim (1)--(2). It also shows why fleet01/B05's new Borel square-root slice estimate, which follows from a projected joint-density cap, cannot alone provide the missing two-base hub integration theorem: some genuinely product-preserving operation is still needed.

No admissible independent-coordinate counterexample was found. In particular, nothing here verifies that \(g_\delta\) has an original-coordinate product representation after projection. Further work must retain the product convolution/Pluecker structure through the curved trace and through additional spectral terms.

**Primary comparison source:** Livshyts, Paouris, Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, Theorem 1.1; the exact cap \(2^{k/2}\) is also quoted in the assembled manuscript at proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/hubs.tex.