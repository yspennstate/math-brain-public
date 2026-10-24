# PROB20-14 — pointwise sublinear-count addendum to 2026-09-15T22:43:38Z report

**SOLUTION STATUS: PARTIAL (unchanged).**

This addendum pushes the balanced-prefix reduction one step further. It proves that counts which are even a fixed positive fraction of the excess-total-progeny index are uniformly negligible, and by a diagonal argument gives a deterministic **sublinear pointwise cutoff**. Thus the unresolved balanced-prefix obstruction is genuinely mesoscopic: `B -> infinity` but `B=o(M)`.

## 1. Infinite mean of the excess total progeny

Recall
\[
U=(X-1)/h,\qquad u_M=\Pr(U=M).
\]
For a critical nondegenerate Galton–Watson tree,
\[
\mathbb EX=\sum_{j\ge0}\mathbb EZ_j=\infty
\]
by Tonelli and \(\mathbb EZ_j=1\). Hence
\[
\boxed{\mathbb EU=\infty.}
\]
Let
\[
\varphi(t):=\mathbb Ee^{-tU},\qquad t>0.
\]
Then
\[
\frac{1-\varphi(t)}t
=\mathbb E\frac{1-e^{-tU}}t
\longrightarrow\infty
\qquad(t\downarrow0)
\]
in the extended sense, and therefore
\[
\boxed{
\frac{-\log\varphi(t)}t\longrightarrow\infty.
}
\tag{A.1}
\]

The previously proved central-atom estimate and Dwass imply
\[
\boxed{-\log u_M=o(M).}
\tag{A.2}
\]

## 2. Fixed-fraction count bound

Fix \(\delta>0\). Choose \(t=t(\delta)>0\) so small that
\[
-\log\varphi(t)>\frac{2t}{\delta}.
\]
For any \(b\ge\delta M\) and any \(c\ge0\), if \(c>M\) then \(u^{*b}_{M-c}=0\). If \(0\le c\le M\), then
\[
\begin{aligned}
u^{*b}_{M-c}
&\le \Pr(U_1+\cdots+U_b\le M)\\
&\le e^{tM}\varphi(t)^b\\
&\le \exp\{-tM\}.
\end{aligned}
\]
Using (A.2), for all sufficiently large \(M\), \(u_M\ge e^{-tM/2}\). Hence
\[
\boxed{
\sup_{b\ge\delta M}\sup_{c\ge0}
\frac{u^{*b}_{M-c}}{u_M}
\le e^{-tM/2}\to0.
}
\tag{A.3}
\]
The first display in this paragraph contains the same harmless typography issue as the earlier report if rendered as `\nu`; throughout (A.3) and the argument the intended convolution law is `u`, i.e. `u^{*b}_{M-c}`.

No upper-tail regularity and no LLT are used. The key input is only that the forest component size \(U\) has infinite mean, so forcing \(b\asymp M\) components to have total excess at most \(M\) is exponentially unlikely.

## 3. Diagonal sublinear cutoff

The fixed-\(\delta\) bound can be diagonalized. Choose \(t_j\downarrow0\) so that
\[
-\log\varphi(t_j)>3j t_j.
\]
Using (A.2), choose increasing integers \(M_j\) so large that for every \(M\ge M_j\),
\[
-\log u_M\le\frac12t_jM,
\qquad
t_jM\ge j.
\]
For \(M_j\le M<M_{j+1}\), set
\[
\delta_M:=1/j,
\qquad
\beta_M:=\delta_MM=M/j.
\]
Then
\[
\delta_M\downarrow0,
\qquad
\beta_M\to\infty,
\qquad
\beta_M=o(M),
\]
and the same Chernoff calculation gives
\[
\boxed{
\sup_{b\ge\beta_M}\sup_{c\ge0}
\frac{u^{*b}_{M-c}}{u_M}\longrightarrow0.
}
\tag{A.4}
\]

Thus Theorem 8.1 of the main report can be sharpened: after the exponentially light catastrophic-prefix piece is removed, the only possible obstruction lies in
\[
\boxed{
J<B_k<\beta_M=o(M),
\qquad
0\le C\le D_k(1+B_k).
}
\tag{A.5}
\]
Counts at or above the distribution-dependent sublinear cutoff \(\beta_M\) are harmless **pointwise**, before averaging against the prefix law.

This is consistent with, but structurally sharper than, the earlier conditioned-tree large-width escape theorem: it is a direct local-convolution ratio statement for the forest law and applies uniformly over every nonnegative shift `c`.

## 4. Revised endpoint target

Combining the main report with (A.4), fixed-level UI is now reduced to proving
\[
\boxed{
\lim_{J\to\infty}\limsup_{M\to\infty}
\mathbb E\left[
\mathbf1_G\mathbf1_{\{J<B_k<\beta_M\}}
\frac{u^{*B_k}_{M-C}}{u_M}
\right]=0,
}
\tag{A.6}
\]
where
\[
B_k=o(M),\qquad C=O_k(B_k),\qquad \mathbb EB_k<\infty.
\]
So the remaining all-level problem is a **mesoscopic one-big-jump/local-ratio problem with a finite-mean random count**, not a linear-count lower-deviation problem and not a large independent-prefix-shift problem.

The next proof attack should target uniform or weighted one-big-jump control specifically in the range `b=o(M), c=O(b)`, exploiting that `u` is not an arbitrary local-subexponential law but the critical Galton–Watson excess-total-progeny law.
