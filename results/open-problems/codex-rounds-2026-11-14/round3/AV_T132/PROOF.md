# A conditional normalization exponent for the spanning-tree case

The conclusion here is an implication between assertions in OpenAI, *Metric-measure limits of subcritical FK and spanning-tree planar maps* (September 24, 2026). It does not verify the proofs of those assertions or establish the planar-map scaling limit independently.

Put gamma=sqrt(2), p=1/d_gamma, and let

\[
A_j=\|X_{[0,2^j]}\|_k,\qquad B_N=A_{\lfloor\log_2N\rfloor},
\]

where X is the internal endpoint distance in the bilateral spanning-tree encoding. These are the definitions in [tree-bootstrap.tex](sources/tree-bootstrap.tex). All norms and normalizations are deterministic.

## 1. The precise inputs

The following assertions are taken as hypotheses, rather than proved here.

1. Proposition `tree:prop:bootstrap` says that from every sequence j_r tending to infinity one can extract normalized joint data converging to a law in the rigid unit-internal-norm class R. The retained data include every fixed finite enlargement of the time window. Fixed-interval kth moments are uniformly integrable, as also stated in Theorem `tree:thm:bilateral_limit`. Consequently, for each fixed positive integer m, after extraction,

   \[
   \frac{A_{j_r+m}}{A_{j_r}}\longrightarrow q_{-m},\qquad q_0=1.
   \tag{1}
   \]

   Indeed the normalized internal endpoint distance on [0,2^m] is X_[0,2^(j_r+m)]/A_(j_r); its kth moment is exactly (A_(j_r+m)/A_(j_r))^k. Uniform integrability passes this moment to the retained endpoint variable. This uses internal endpoint coordinates, without identifying them with unrestricted tip distance.

2. Proposition `tree:prop:internal_norm_comparison` gives constants 0<alpha<=beta<infinity, independent of the rigid law and of the fixed integer i, such that

   \[
   \alpha C2^{-ip}\le q_i\le\beta C2^{-ip}.
   \tag{2}
   \]

   The proposition explicitly includes negative i and joint extractions of zooms. At i=0 and q_0=1 this yields

   \[
   \beta^{-1}\le C\le\alpha^{-1}.
   \tag{3}
   \]

3. Proposition `tree:prop:sphere_identification` in [sphere.tex](sources/sphere.tex) says every sequence n tending to infinity has a further subsequence on which

   \[
   (V(M_n),B_{2n}^{-1}d_n,\mu_n)
   \Rightarrow(S,\Lambda D_h,\mu_h)
   \tag{4}
   \]

   in GHP, with deterministic Lambda in a fixed compact subset of (0,infinity). Here mu_n(v)=deg(v)/(2n) and all primal edges enter d_n. The sphere is compact and has diameter H strictly between zero and infinity almost surely.

## 2. The dyadic logarithmic exponent

Let R_0=beta/alpha>=1. Equations (1)--(3), applied at i=-m, show that every sequence j_r tending to infinity has a further subsequence with

\[
\frac{A_{j_r+m}}{A_{j_r}}\longrightarrow L_m,
\qquad R_0^{-1}2^{mp}\le L_m\le R_0 2^{mp}.
\tag{5}
\]

Fix m. If there were infinitely many j with A_(j+m)/A_j>2R_0 2^(mp), extract that sequence using (5). Its limit cannot be at most R_0 2^(mp), a contradiction. The same argument for ratios below (2R_0)^(-1)2^(mp) gives a finite J_m such that, for every j>=J_m,

\[
(2R_0)^{-1}2^{mp}\le\frac{A_{j+m}}{A_j}
\le 2R_0 2^{mp}.
\tag{6}
\]

Write c=log_2(2R_0). Taking logarithms gives

\[
mp-c\le\log_2 A_{j+m}-\log_2 A_j\le mp+c.
\tag{7}
\]

For each residue r in {0,...,m-1}, iterate (7) starting at J_m+r. For every integer l>=0,

\[
\log_2 A_{J_m+r}+l(mp-c)
\le \log_2 A_{J_m+r+lm}
\le \log_2 A_{J_m+r}+l(mp+c).
\tag{8}
\]

Divide by J_m+r+lm and send l to infinity. There are only finitely many residues, so these inequalities imply

\[
p-\frac cm\le\liminf_{j\to\infty}\frac{\log_2 A_j}{j}
\le\limsup_{j\to\infty}\frac{\log_2 A_j}{j}
\le p+\frac cm.
\tag{9}
\]

The same c works for every fixed m because alpha and beta in (2) do not depend on i. Sending m to infinity proves

\[
\frac{\log_2 A_j}{j}\longrightarrow p.
\tag{10}
\]

Since floor(log_2 N)/log_2 N tends to one, (10) gives

\[
B_N=N^{p+o(1)},\qquad B_{2n}=n^{p+o(1)}.
\tag{11}
\]

This proves a logarithmic exponent, without asserting convergence of adjacent ratios or regular variation of A_j.

## 3. The final deterministic scale

Let H_n be the graph diameter of the finite map. The paper defines

\[
a_n=\exp\{m(\log H)-m(\log(H_n\vee1))\},
\tag{12}
\]

where m(Y) is the unique real number satisfying E arctan(Y-m(Y))=0. Lemma `measure:center` in [measured-convergence.tex](sources/measured-convergence.tex) states continuity under weak convergence and translation equivariance of m. They also follow directly: the expectation is a continuous strictly decreasing function of the proposed center with limits pi/2 and -pi/2; bounded continuity and the opposite signs on either side of its zero prove continuity of that zero.

Choose any sequence n tending to infinity and extract as in (4). Diameter is continuous for GH: a correspondence of distortion epsilon changes diameters by at most epsilon, while GHP convergence implies GH convergence. Therefore

\[
H_n/B_{2n}\Rightarrow\Lambda H.
\tag{13}
\]

By (11), B_(2n) tends to infinity. Since Lambda H>0 almost surely, truncation at one disappears after division by B_(2n), and logarithms yield

\[
\log(H_n\vee1)-\log B_{2n}
\Rightarrow\log\Lambda+\log H.
\tag{14}
\]

Continuity and translation equivariance of m now give, on this subsequence,

\[
\log(a_nB_{2n})\longrightarrow-\log\Lambda,
\qquad a_n B_{2n}\longrightarrow\Lambda^{-1}.
\tag{15}
\]

Because every original sequence has such a further subsequence, and the allowed Lambda belong to a fixed compact subset of (0,infinity), a_n B_(2n) is eventually bounded above and bounded away from zero. For example, a sequence escaping either bound would contradict (15) after extracting. Thus log(a_n B_(2n))=O(1), and (11) implies

\[
\frac{\log a_n}{\log n}\longrightarrow-p,
\qquad
\boxed{a_n=n^{-1/d_{\sqrt2}+o(1)}}.
\tag{16}
\]

Taken with the preprint's claimed spanning-tree GHP theorem, this supplies precisely the distance-exponent clause for q=0 with normalized degree measure. It supplies no new positive-q case, no uniform-vertex measure conclusion, and no independent verification of the claimed metric convergence.

## 4. An independent check of the deterministic step

There is a second way to see (10). Put t_j=log_2 A_j-pj. Equation (6) gives |t_(j+m)-t_j|<=c for j>=J_m. For any epsilon>0 choose a fixed integer m with c/m<epsilon. Write j=J_m+r+lm, 0<=r<m. Then |t_j|<=max_(0<=r<m)|t_(J_m+r)|+lc, and hence limsup |t_j|/j<=c/m<epsilon. This proves t_j/j tends to zero directly.

The final-scale step has a separate check using probabilities rather than the arctan center. The asserted limits (4) make H_n/B_(2n) tight and bounded away from zero in probability; the full claimed GHP theorem does the same for a_n H_n. If the deterministic ratios a_n B_(2n) tended to infinity along a subsequence, tightness of a_n H_n would fail because H_n/B_(2n) is bounded away from zero in probability. If they tended to zero, tightness of H_n/B_(2n) would force a_n H_n to tend to zero, contradicting its nonzero limiting diameter. Unbounded ratios have a subsequence tending to infinity, and ratios not bounded away from zero have one tending to zero. This recovers the two deterministic bounds used in (16).

The uniformity in m in (2) is essential. Bounds (5) with a different constant R_m growing exponentially in m would allow a different growth exponent. A single successful subsequence, or the coarse bound with s=p/2 alone, would also be insufficient. Adjacent ratios need not converge: the elementary sequence A_j=2^(pj)exp(a(-1)^j), a>0, has logarithmic exponent p and satisfies offset bounds of the form (5), while its adjacent ratios alternate. This example checks that the deduction does not silently assume regular variation.
