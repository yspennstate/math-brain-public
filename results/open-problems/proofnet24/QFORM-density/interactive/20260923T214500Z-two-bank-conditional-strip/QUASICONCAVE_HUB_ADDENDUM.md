# Quasiconcave and finite-component hub laws

This addendum extends the [two-bank conditional strip lemma](./REPORT.md). The light originals remain independent cap-one variables; \(P\) may overlap arbitrarily with \(L,V\) and may have unbounded moments. Assume the two independent light banks have planar \((L_j,V_j)\) density caps \(M_A,M_B\). Write
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP,
\]
where \(H\) is independent of both banks and has a cap-one probability density \(f_H\).

For almost every \(t\in(0,1)\), let the superlevel set \(E_t=\{h:f_H(h)>t\}\) be, up to null sets, a disjoint union of intervals \(I_{t,j}\), and suppose
\[
K(f_H):=\int_0^1\sum_j\sqrt{|I_{t,j}|}\,dt<\infty. \tag{1}
\]
Then
\[
\|p_Q\|_\infty\le C\sqrt{M_AM_B}\,K(f_H)+\frac12, \tag{2}
\]
uniformly in \(\beta,\varepsilon\), all affine translations of the target, and the heavy-tailed light laws.

Indeed \(f_H(h)=\int_0^1\mathbf1_{E_t}(h)dt\) almost everywhere. On a slice \(L=l\) with \(0<|l|<1\), membership of the hub argument in \(I_{t,j}\) requires the light phase \(W=\beta l^2+V^2+2\varepsilon lP\) to belong to an interval of length \(2|l||I_{t,j}|\). The pointwise slice estimate from the main report bounds its joint \(dl\)-mass by \(C\sqrt{M_AM_B}\sqrt{|l||I_{t,j}|}\,dl\). The hub Jacobian factor \((2|l|)^{-1}\), sum over \(j\), and integration over \(0<|l|<1\) yield the first term of (2). On \(|L|\ge1\), the direct hub cap gives \((2|L|)^{-1}f_H(\cdot)\le1/2\).

In particular, if \(f_H\) is **quasiconcave**, meaning almost every nonempty superlevel set \(E_t\) is one interval, then \(K(f_H)\le1\). To see this, set \(d_t=|E_t|\). Layer cake gives \(\int_0^1d_tdt=\int f_H=1\), and Cauchy-Schwarz gives \(\int_0^1\sqrt{d_t}dt\le1\). This covers all cap-one unimodal densities, with arbitrarily heavy tails and no bounded support condition.

More generally, if almost every \(E_t\) is a union of at most \(N\) disjoint intervals, then \(K(f_H)\le\sqrt N\). Indeed \(\sum_{j=1}^N\sqrt{|I_{t,j}|}\le\sqrt{N|E_t|}\), and integrate in \(t\). Every convex mixture of hub laws with a common bound in (2) inherits that bound by conditioning on the independent mixture label. An arbitrary fragmented cap-one hub need not have finite \(K(f_H)\); its case remains open.
