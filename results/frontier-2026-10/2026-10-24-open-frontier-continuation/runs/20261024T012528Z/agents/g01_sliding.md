# Actual changing-weight endpoint: a strict two-input sliding lemma

**Status.** The deterministic lemma below applies to the exact simultaneous-GD endpoint recursion on a physical interval on which the second gate is positive and the two inward normal drifts have uniform strict margins. It allows a nonzero macroscopic first projection at the interval's start and the actual changing residual and output weight. It gives finite-time capture, an (O(h)) occupation primitive, and the limiting output action. It does **not** establish that a marked endpoint enters this sector or that the margins persist for the self-consistent network.

## Exact model and hypotheses

Fix (0<\rho<1), (G=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)), (a=m^{1/\alpha}), (L=(\log m)^{1/\alpha}), and a fixed (\gamma>0). Let (h=\gamma/L). For one actual row write (q_n=V_{i,n}/L=(x_n,y_n)), (z_n=W_{i,n}/a), (r_n=(r_{1,n},r_{2,n})). The simultaneous-GD equations, without freezing (z_n), are exactly

\[
q_{n+1}=q_n+h z_nG\operatorname{diag}(1_{x_n>0},1_{y_n>0})r_n,
\qquad
z_{n+1}=z_n+\frac{\gamma L}{a^2}\,r_n^T(q_n)_+ . \tag{1}
\]

Work on grid steps \(n_0\le n<n_1\), of physical duration at most \(T\). Assume \(y_n>0\) at every node \(n_0\le n\le n_1\), including the terminal node used in output increments, and define

\[
c_n=\rho z_n r_{2,n},\qquad d_n=-z_n(r_{1,n}+\rho r_{2,n}),\qquad A_n=c_n+d_n=-z_n r_{1,n}.
\]

Suppose, uniformly on these indices,

\[
0<c_*\le c_n\le c^*,\qquad 0<d_*\le d_n\le d^*,\qquad 0<z_-\le z_n\le Z,
\qquad \|r_n\|\le R. \tag{2}
\]

These are **strict attracting-cone assumptions**. In particular (r_{2,n}>0), (r_{1,n}<0), (A_n\ge A_*:=c_*+d_*>0), and (\theta_n:=c_n/A_n=-\rho r_{2,n}/r_{1,n}\in(0,1)). Put (M=\max(c^*,d^*)), (s_n=1_{x_n>0}), and (\eta_n=y_n-\rho x_n). The following identities hold at every step, including exact hits of (x=0), because the prescribed gate there is zero:

\[
x_{n+1}-x_n=h(c_n-A_ns_n)=-hA_n(s_n-\theta_n),
\qquad
\eta_{n+1}-\eta_n=h(1-\rho^2)z_n r_{2,n}. \tag{3}
\]

### Capture from a nonzero (q_1=x)

The closed strip (I_h=[-h d^*,h c^*]) is forward invariant while (2) and (y>0) hold. If (x_n\le0), the next point adds (hc_n); if (x_n>0), it subtracts (hd_n). Both possibilities remain in (I_h) from either half of that strip. If (x_{n_0}>h c^*), the first entry index (e) obeys

\[
e-n_0\le \left\lceil\frac{x_{n_0}-h c^*}{h d_*}\right\rceil,
\qquad x_e\in I_h. \tag{4+}
\]

If (x_{n_0}<-h d^*), the analogous bound is

\[
e-n_0\le \left\lceil\frac{-h d^*-x_{n_0}}{h c_*}\right\rceil,
\qquad x_e\in I_h. \tag{4-}
\]

For initial (x_{n_0}\in I_h), take (e=n_0). These entry claims require that the assumed second-gate and cone conditions hold through the displayed number of steps. The crossing step cannot jump across the opposite end of (I_h): just before a positive-side entry (x>h c^*\ge0), so (x-hd_n>-h d^*); the negative-side case is symmetric. In physical time, (4) is at most (x_{n_0}^+/d_*+O(h)) or ((-x_{n_0})^+/c_*+O(h)). After entry,

\[
|x_n|\le hM\quad(n\ge e),\qquad
\eta_n=\eta_e+h(1-\rho^2)\sum_{j=e}^{n-1}z_jr_{2,j}. \tag{5}
\]

### Occupation primitive with an evolving residual

For any grid interval ([k,\ell]\subset[e,n_1]) and any scalar sequence (\phi_j), summation by parts in the **actual** normal recurrence (3) gives

\[
h\sum_{j=k}^{\ell-1}\phi_j(s_j-\theta_j)
=-\sum_{j=k}^{\ell-1}\frac{\phi_j}{A_j}(x_{j+1}-x_j),
\]

and hence

\[
\left|h\sum_{j=k}^{\ell-1}\phi_j(s_j-\theta_j)\right|
\le hM\left(2\left\|\frac{\phi}{A}\right\|_\infty
+\operatorname{TV}_{[k,\ell)}\!\left(\frac{\phi}{A}\right)\right). \tag{6}
\]

In particular, with (\phi\equiv1),

\[
\sup_{e\le k<\ell\le n_1}\left|h\sum_{j=k}^{\ell-1}(s_j-\theta_j)\right|
\le hM\left(\frac{2}{A_*}+\frac{\operatorname{TV}(A)}{A_*^2}\right). \tag{7}
\]

The BV condition is concrete: (A_n=-z_n r_{1,n}), so

\[
\operatorname{TV}(A)\le \|r_1\|_\infty\operatorname{TV}(z)
+Z\operatorname{TV}(r_1). \tag{8}
\]

Thus a uniformly BV residual and the small actual-weight variation established below make the binary occupation primitive (O(h)), uniformly over *all* subintervals. For a BV test (\phi), (6) also gives weak temporal convergence (s_n\rightharpoonup^*\theta(t)), provided (r_n\to r(t)) and (z_n\to z>0) uniformly with strict margins. Indeed the same bound applies to (\phi/A), while the one partial cell between a grid endpoint and an arbitrary time contributes at most (h\|\phi\|_\infty). This is an occupation statement, not a pointwise or (L^1) gate limit.

### Finite-interval output action for the changing weight

The row's **actual** contribution to network output is (p_n=z_n((x_n)_+,y_n)), since (W_{i,n}(V_{i,n})_+/(aL)=z_n(q_n)_+). Define (E_n=z_n((x_n)_+,\rho x_n)). On the captured strip,

\[
p_n=(0,z_n\eta_n)+E_n,
\qquad \|E_n\|_2\le Z hM\sqrt{1+\rho^2}.
\]

The exact product rule (z_{j+1}\eta_{j+1}-z_j\eta_j=z_j(\eta_{j+1}-\eta_j)+(z_{j+1}-z_j)\eta_{j+1}) and (3) yield, for (e\le k<\ell\le n_1),

\[
p_\ell-p_k
=\begin{pmatrix}0\\ (1-\rho^2)h\sum_{j=k}^{\ell-1}z_j^2r_{2,j}\end{pmatrix}
+\begin{pmatrix}0\\\sum_{j=k}^{\ell-1}(z_{j+1}-z_j)\eta_{j+1}\end{pmatrix}
+E_\ell-E_k. \tag{9}
\]

Consequently, writing (Q_\eta=\sup_{e\le j\le n_1}|\eta_j|),

\[
\sup_{e\le k<\ell\le n_1}
\left\|p_\ell-p_k-
\begin{pmatrix}0\\(1-\rho^2)h\sum_{j=k}^{\ell-1}z_j^2r_{2,j}\end{pmatrix}\right\|_2
\le Q_\eta\operatorname{TV}(z)+2ZhM\sqrt{1+\rho^2}. \tag{10}
\]

This is the desired finite-interval Schur output action, with the **actual changing output weight** accounted for by an explicit product-rule remainder. It is stronger than asserting the frozen-(z) identity for (\eta). The matrix (z^2\operatorname{diag}(0,1-\rho^2)) represents the action on the residual along this strict sliding branch; (10) does not claim convergence of the pre-step tangent Gram to that matrix.

## Why the actual (z_n) variation vanishes

The weight equation in (1) proves this locally, without freezing it. If (\|q_{n_0}\|\le Q_0), (\|r_n\|\le R), (z_n\le Z), and the interval length is at most (T), then (\|q_n\|\le Q:=Q_0+(T+h)Z\|G\|R) and

\[
\operatorname{TV}_{[n_0,n_1]}(z)
\le \frac{\gamma L}{a^2}R\sum_{n=n_0}^{n_1-1}\|q_n\|
\le (T+h)RQ\frac{L^2}{a^2}=o(1). \tag{11}
\]

For a retained endpoint with (z_{n_0}\in[z_0^-,z_0^+]\subset(0,\infty)), the temporary bound (z_n\le2z_0^+) closes by a first-exit argument: compute (Q) using (Z=2z_0^+); for large (m), the last bound in (11) is smaller than both (z_0^-/2) and (z_0^+). Therefore (z_n\in[z_0^-/2,2z_0^+]) throughout any bounded physical interval on which the residual is bounded. This also proves (\sup_n|z_n-z_{n_0}|=o(1)). The MACRO_COMPACTNESS.md bootstrap supplies bounded (r_n) and physical-time Lipschitzness on localized network events; hence (\operatorname{TV}(r_1)=O(1)) there, and (7) is (O(h)). No smallness of (\gamma) is required.

## Conditional macroscopic path, including approach from (x\ne0)

Suppose on a sequence (m\to\infty), the hypotheses above hold on ([t_0,T]), (q_{n_0}\to(x_0,y_0)), (z_{n_0}\to z>0), and the polygonal residuals converge uniformly to a continuous (r(t)), with the strict margins persisting. Let (c(t)=\rho z r_2(t)), (d(t)=-z(r_1(t)+\rho r_2(t))). If (x_0>0), define

\[
\tau=\inf\left\{t\ge t_0:\int_{t_0}^t d(u)\,du\ge x_0\right\},\qquad
x(t)=\left[x_0-\int_{t_0}^t d(u)\,du\right]_+.
\]

If (x_0<0), use (\tau=\inf\{t:\int_{t_0}^t c(u)du\ge -x_0\}) and (x(t)=-[-x_0-\int_{t_0}^t c(u)du]_+). For (x_0=0), set (\tau=t_0,x\equiv0). Provided (\tau<T) and the sector assumptions hold through it, (4) and uniform convergence of (c_n,d_n) show the first strip-entry times converge to (\tau); before entry the normal recursion is exactly the corresponding one-sided Riemann sum, and afterwards (5) gives (x_n=O(h)). Thus the polygonal (q) paths converge uniformly to

\[
q(t)=\left(x(t),\;y_0+\rho[x(t)-x_0]+(1-\rho^2)z\int_{t_0}^t r_2(u)\,du\right). \tag{12}
\]

On (t>\tau), (x(t)=0); (9)--(11) give the limiting endpoint output law

\[
\frac{d}{dt}\bigl[z(q(t))_+\bigr]
=\begin{pmatrix}0\\z^2(1-\rho^2)r_2(t)\end{pmatrix}
\quad\text{for a.e. }t\in(\tau,T). \tag{13}
\]

Before capture, the output derivative is (z^2Gr) if (x>0,y>0), and ((0,z^2r_2)) if (x<0,y>0). Equation (13) begins only after the crossing/capture. The fixed-(m) microscopic (s_n) may chatter forever; its primitive follows (7), while its pre-step tangent Gram need not have the action (13).

## Precisely what remains conditional

The second gate's positivity cannot be inferred from (y_{n_0}>0) alone. On the captured strip, (5) and (z_nr_{2,n}>0) provide the sufficient forward condition

\[
\eta_e>\rho h d^*\quad\Longrightarrow\quad
y_n=\eta_n+\rho x_n>0\quad(n\ge e), \tag{14}
\]

as long as the cone margins persist. Before capture, (y) may hit zero: for (\rho=1/2,z=1,r=(-3,1)), the strict normal drifts are (c=1/2,d=5/2), but with (x_0=1,y_0=0.1) the both-active velocity is ((-2.5,-0.5)), so (y) reaches zero at physical time (0.2) while (x=0.5>0). At a finite grid step, a sufficiently small positive (y) can likewise cross zero before capture. A separate sector-validation argument or an explicit positive margin for (y) is needed.

The strict cone can also end when \(r_2\downarrow0\) (so \(c\downarrow0\)), when \(r_1+\rho r_2\uparrow0\) (so \(d\downarrow0\)), or at a second-gate event. Loss of \(c_*>0\) or \(d_*>0\) invalidates the uniform strict-capture estimate from a fixed off-face distance. A trapped strip can remain invariant with merely nonnegative drifts, but later exit needs a separate argument. It does **not** by itself force \(A=c+d\) to vanish; the occupation denominator becomes singular only if \(A\downarrow0\). A different one-sided or reflected argument may continue a trajectory through a margin loss. For a retained endpoint with \(z_0>0\), (11) rules out a weight-sign flip on a fixed physical interval under bounded residual, but does not prevent a residual-cone exit. At the original marked initialization \(q_0=XU_0/L\to0\), the limit \(x_0=0\) alone does not choose the initial sector/ray: the \(O(1)\) original mark \(U_0\) and early boundary grid still matter. This lemma supplies a rigorous *conditional local sliding segment* and its matching from a nonzero macroscopic approach; it does not solve mark-dependent entrance, global face transitions, or uniqueness of the MACRO_COMPACTNESS.md inclusion.
