# Formal claim: adaptive quadratic-control tree payment

Let \(p_h(S)=\widehat h(S)^2\), \(\pi_h(S)=\sum_{A\supseteq S}p_h(A)\), and
\[
U(h)=\sum_Sp_h(S)\log_2\frac{\pi_h(S)}{p_h(S)}.
\]

## Theorem

Let \(q=(-1)^Q\) be a quadratic Boolean phase on a control set \(X\), let \(g\) be an arbitrary Boolean function on a disjoint set \(Y\), and let \(F=qg\). Let \(T\) be a finite binary decision tree which, at each internal node \(v\), queries a coordinate \(i_v\in X\) not previously queried on that root-to-node path. The query may depend on previous answers, and a physical coordinate may label distinct incomparable nodes. Write \(w_v=2^{-d(v)}\), and let \(F_v\) be the restriction at \(v\). Then
\[
U(F)-\sum_{\ell\in\partial T}w_\ell U(F_\ell)
=\sum_{v\in T^\circ}w_v\Delta_{i_v}U(F_v)
\le3I_T\le3I_X(F),
\]
where
\[
I_T=\sum_{v\in T^\circ}w_v\operatorname{Inf}_{i_v}(F_v).
\]

## Proof

The first equality is the martingale telescope of
\[
\Delta_iU(h)=U(h)-\frac{U(h|x_i=1)+U(h|x_i=-1)}2.
\]
All nonroot internal values cancel.

For disjoint products, \(p_{h_1h_2}=p_{h_1}\otimes p_{h_2}\) and \(\pi_{h_1h_2}=\pi_{h_1}\otimes\pi_{h_2}\), hence \(U(h_1h_2)=U(h_1)+U(h_2)\). Thus at every node
\[
\Delta_{i_v}U(F_v)=\Delta_{i_v}U(q_v),\qquad
\operatorname{Inf}_{i_v}(F_v)=\operatorname{Inf}_{i_v}(q_v).
\]
The restriction \(q_v\) is quadratic, so `B01_ALL_QUADRATIC_GU_v1` gives
\[
\Delta_{i_v}U(q_v)\le3\operatorname{Inf}_{i_v}(q_v).
\]
After multiplication by \(w_v\) and summation, this proves the first inequality.

For the second inequality, fix \(i\in X\). If \(V_i=\{v:i_v=i\}\), the reach cylinders \(E_v\), \(v\in V_i\), are pairwise disjoint because no path queries \(i\) twice. Since \(i\) is still free at \(v\), \(E_v\) is invariant under the \(i\)-flip, and therefore
\[
w_v\operatorname{Inf}_i(F_v)
=\Pr(E_v\cap\{z:F(z)\ne F(z^{\oplus i})\}).
\]
Disjointness gives
\[
\sum_{v\in V_i}w_v\operatorname{Inf}_i(F_v)
\le\operatorname{Inf}_i(F).
\]
Sum over \(i\in X\). Finally \(I_X(qg)=I(q)\), since multiplying by a disjoint Boolean factor does not change a control derivative. ∎

## Sharpness and boundary

The coefficient 3 cannot be lowered in this theorem using the same local inequality: take a one-node tree on one coordinate of the even clique quadratic, whose ratio is \(3-2^{2-|X|}\).

The theorem does not allow the queried coordinate to interact with arbitrary variables of \(g\). Disjointness is used exactly in the tensor identity. Shared-core coset stability remains open.
