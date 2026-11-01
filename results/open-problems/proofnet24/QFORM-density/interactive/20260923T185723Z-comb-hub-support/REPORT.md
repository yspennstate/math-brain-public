# Gap-independent bound for an interval-comb hub law

**Status:** proved sufficient theorem for the zero-diagonal one-hub normal form; the unrestricted three-eigenvalue theorem remains open. This note extends the interval-supported hub theorem in `manuscript/hubs.tex`, Theorem `thm:hub-interval`. It does not claim uniformity in the number of intervals.

Let \(X_0,X_1,\ldots,X_m\) be independent real variables with probability densities bounded by one. Set \(X'=(X_1,\ldots,X_m)\), \(L=\langle w,X'\rangle\), and \(V=\langle v,X'\rangle\), where \(w,v\) are orthonormal and \(w_i^2+v_i^2\le 1/2\) for every \(i\). Let \(\lambda\ne0\), and permit arbitrary real \(\beta,q,d_i,b_i,c_i\). Consider
\[
 Q=2X_0(L+\beta)+\lambda V^2+
       2L\langle q,X'\rangle+
       \sum_{i=1}^m(d_iX_i^2+b_iX_i+c_i).                 \tag{1}
\]

**Theorem.** Suppose the support of the density of \(X_0\), up to a null set, lies in a union of pairwise disjoint intervals \(J_j\) with lengths \(D_j>0\), and
\[
 S=\sum_j\sqrt{D_j}<\infty.
\]
The interval locations and the gaps between them are unrestricted. Then \(Q\) has a bounded density and
\[
 \boxed{\displaystyle
 \|p_Q\|_\infty\le
 \frac32\left(\frac{32\pi^4}{|\lambda|}\right)^{1/3}
 S^{2/3}.}                                                \tag{2}
\]
For \(N\) intervals with total supporting length \(D=\sum_{j=1}^N D_j\),
\[
 \|p_Q\|_\infty
 \le\frac32(32\pi^4 ND/|\lambda|)^{1/3}
 <22(ND/|\lambda|)^{1/3}.                                \tag{3}
\]
No condition on interval separation, input moments, \(q\), or the one-coordinate quadratic terms is imposed.

**Proof.** It suffices first to handle finitely many intervals. Fix an output level \(s\), window radius \(\delta>0\), and write \(t=\ell+\beta\). Freeze the \(L\)-dependent light polynomial at \(\ell_0\), as in `manuscript/hubs.tex`, Lemma `lem:hub-frozen` and Remark `rem:hub-freezing`. The resulting unnormalized slice \(\mu_{\ell_0,\ell}\) at \(L=\ell\) has total mass \(\rho_L(\ell)\), and, uniformly in the frozen parameter and almost every slice,
\[
 \mu_{\ell_0,\ell}(I)\le 2\pi^2\sqrt{|I|/|\lambda|}
                                                        \tag{4}
\]
for every interval \(I\).

Integrate out the hub. Its window kernel is
\[
 G(\ell,y)=\int f_0(x){\bf1}_{\{|2tx+y-s|\le\delta\}}\,dx
          =\sum_j G_j(\ell,y),\quad
 G_j=\int_{J_j}f_0(x){\bf1}_{\{|2tx+y-s|\le\delta\}}\,dx.
\]
For \(|t|\ge T>0\), use the *whole* hub kernel: \(f_0\le1\) implies \(G(\ell,y)\le\delta/|t|\). Integration over the slices and \(\int\rho_L=1\) gives a high-\(|t|\) window probability at most \(\delta/T\). This bound cannot be multiplied by the mass of an individual hub interval.

For \(|t|<T\), bound \(G_j\) by the kernel with density \({\bf1}_{J_j}\). Equation (4) and Fubini give the two simultaneous bounds
\[
 \int G_j(\ell,y)\,\mu_{\ell_0,\ell}(dy)
 \le {2\pi^2\delta\over|t|}
       \sqrt{(2|t|D_j+2\delta)/|\lambda|},\qquad
 \int G_j(\ell,y)\,\mu_{\ell_0,\ell}(dy)
 \le 2\pi^2D_j\sqrt{2\delta/|\lambda|}.                  \tag{5}
\]
The first follows because the \(y\)-support of the kernel is an interval of length \(2|t|D_j+2\delta\). The second integrates the interval small-ball bound of length \(2\delta\) over \(J_j\). For each fixed finite family, the freezing limit and the same dominated-convergence split used in the original interval theorem yield
\[
 \limsup_{\delta\downarrow0}
 \frac{\mathbb P(|Q-s|\le\delta)}{2\delta}
 \le {1\over2T}
    +4\sqrt2\,\pi^2\sqrt{T/|\lambda|}
            \sum_j\sqrt{D_j}.                            \tag{6}
\]
Specifically, the region \(|t|<\delta\) has vanishing contribution by the second bound in (5); on \(\delta\le|t|<T\), the first bound has an integrable \(|t|^{-1/2}\) majorant. Choosing
\[
 T=\left(\frac{\sqrt{|\lambda|}}
                  {4\sqrt2\,\pi^2 S}\right)^{2/3}
\]
proves (2). Its uniform interval estimates imply domination of the output law by the displayed constant times Lebesgue measure. Cauchy–Schwarz gives \(S^2\le ND\), hence (3).

For countably many intervals with \(S<\infty\), replace the hub probability density by its restriction to the first \(N\) intervals. These subprobability measures still obey \(f_0\le1\); the *global* high-\(|t|\) estimate \(\delta/T\) remains valid because the light slice mass integrates to one. Their output measures increase setwise to the full output law, while (2) gives a common density cap since \(S_N\le S\). Monotone convergence transfers this cap to the full law. \(\square\)

**Scope.** Formula (2) remains finite for some disconnected and unbounded hub supports. It does not solve arbitrary cap-one hub laws: unit-mass supports can have infinitely many tiny distant intervals with \(\sum_j\sqrt{D_j}=\infty\). For example, after normalizing, lengths proportional to \(j^{-2}\) have finite total length but divergent square-root sum. The positive leakage endpoint \(Q_\varepsilon=2X_0L+V^2+2\varepsilon LP\), uniformly over every cap-one product law as \(\varepsilon\to0\), therefore remains open.
