# Two-bank conditional strip lemma for the canonical light phase

**Status.** Rigorous conditional interval estimate. It proves a canonical density bound when the physical hub is uniform on a unit interval, even with arbitrary fragmented and heavy-tailed light originals. It does not prove the full conjecture for an arbitrary cap-one hub: the missing statement concerns a fragmented measurable target set, rather than one interval.

## Lemma: one linear sum and one mixed bilinear phase

Let \(A,B\) be independent random bank vectors. Suppose \((L_A,V_A)\) and \((L_B,V_B)\) have joint planar densities bounded by \(M_A,M_B\), respectively. Let \(F_A(A),F_B(B)\) be arbitrary real measurable functions of their respective banks, and put
\[
L=L_A+L_B,\qquad W=F_A(A)+F_B(B)+2V_AV_B.
\]
For every \(t\ne0\), the complex measure \(\mathbb E[e^{itW}\mathbf1_{\{L\in dl\}}]\) has a density \(g_t(l)\) satisfying
\[
\|g_t\|_\infty\le\sqrt{\frac{\pi M_A M_B}{|t|}}. \tag{1}
\]
Consequently, for every measurable \(D\subset\mathbb R\), measurable center \(z:D\to\mathbb R\), and \(u>0\),
\[
\Pr\{L\in D,\ |W-z(L)|\le u\}
 \le C\sqrt{M_A M_B}\,|D|\sqrt u. \tag{2}
\]
Here and below the right-hand side is interpreted as trivial if \(|D|=\infty\).

For (1), disintegrate each bank against its planar projection and define the complex functions
\[
f_{A,t}(a,v)=\int e^{itF_A}\,d\Pr_A(a,v,\mathrm{other}),\qquad
f_{B,t}(b,w)=\int e^{itF_B}\,d\Pr_B(b,w,\mathrm{other}).
\]
They obey \(|f_{A,t}|\le p_{(L_A,V_A)}\), hence \(\|f_{A,t}\|_2^2\le M_A\); similarly \(\|f_{B,t}\|_2^2\le M_B\). A convolution calculation gives
\[
g_t(l)=\int_{\mathbb R^3} f_{A,t}(a,v) f_{B,t}(l-a,w)e^{2itvw}\,da\,dv\,dw.
\]
For each \(a\), one-dimensional Plancherel bounds the \((v,w)\)-integral by
\(\sqrt{\pi/|t|}\,\|f_{A,t}(a,\cdot)\|_2\|f_{B,t}(l-a,\cdot)\|_2\).
Cauchy-Schwarz in \(a\) proves (1). Approximation by bounded compactly supported densities justifies the calculation in full generality.

For (2), use the nonnegative Fejér kernel at frequency \(T=1/u\). A fixed constant times \(u\) times that kernel majorizes \(\mathbf1_{[-u,u]}\). Its Fourier transform is supported on \([-T,T]\) and bounded by one. Integrating (1) over \(|t|\le T\) gives the pointwise in \(l\) conditional interval mass bound \(C\sqrt{M_AM_B}\sqrt u\), uniformly in the interval center; integration over \(D\) gives (2).

## Application with arbitrary overlapping P

Split the light originals into independent banks \(A,B\), and set
\(L=L_A+L_B\), \(V=V_A+V_B\), \(P=P_A+P_B\).
For a *fixed* value \(L=l\), write
\[
V^2+2\varepsilon lP+\beta l^2
=\underbrace{(V_A^2+2\varepsilon lP_A)}_{F_A}
 +\underbrace{(V_B^2+2\varepsilon lP_B)}_{F_B}
 +2V_AV_B+\beta l^2.
\]
The lemma permits the local phases to depend on the externally fixed \(l\). Thus, if the bank planar density caps are \(M_A,M_B\),
\[
\Pr\{L\in D,\ |V^2+2\varepsilon LP+\beta L^2-s|\le u\}
\le C\sqrt{M_AM_B}\,|D|\sqrt u \tag{3}
\]
uniformly in \(s,\beta,\varepsilon\), with no moment, support, independence-within-bank, or marginal P assumptions. In particular the dyadic shell \(D=\{r\le|l|\le2r\}\) gives \(C\sqrt{M_AM_B}\,r\sqrt u\).

If \(H\), independent of the light banks, has cap-one density supported on an interval \(I\) of length one, then \(Q=2HL+\beta L^2+V^2+2\varepsilon LP\) has a uniformly bounded density. Indeed,
\[
p_Q(s)=\mathbb E\frac1{2|L|}
 f_H\left(\frac{s-\beta L^2-V^2-2\varepsilon LP}{2L}\right).
\]
On \(|L|\ge1\), the integrand is at most \(1/2\). On a slice \(L=l\) with \(0<|l|<1\), the event that the argument lies in \(I\) says that \(V^2+2\varepsilon lP+\beta l^2\) lies in an interval of length \(2|l|\). The pointwise slice estimate from (2) bounds its joint \(dl\)-mass by \(C\sqrt{M_AM_B}\sqrt{|l|}\,dl\). Dividing by \(2|l|\) and integrating \(0<|l|<1\) is finite. The bound is uniform in \(s,\beta,\varepsilon\) and in the light laws.

For an orthonormal coefficient pair \(\ell,v\) on independent cap-one light originals with maximum physical row leverage \(\max_i(\ell_i^2+v_i^2)\le1/24\), a random physical cut has both two-column restricted Gram matrices between \(I_2/4\) and \(3I_2/4\): the expected squared Frobenius deviation of one bank from \(I_2/2\) is at most \((1/4)\sum_i(\ell_i^2+v_i^2)^2\le1/48<1/16\). The standard fixed-dimensional product-projection density bound then supplies absolute \(M_A,M_B\). The hub corollary therefore applies in the diffuse canonical product case with no P tails.

## Exact remaining gap

An arbitrary cap-one hub may be uniform on a highly fragmented measurable set of measure one. In that case the target window on each \(L=l\) slice is an equally fragmented set of measure \(2|l|\). Bound (2) only treats one interval, and summing it across infinitely many components incurs \(\sum_j\sqrt{|I_j|}\), which can diverge. A dimension-free arbitrary-target weak-\(L^2\) estimate, or a direct cap-one hub estimate using more product structure, remains necessary for the unrestricted canonical case.
