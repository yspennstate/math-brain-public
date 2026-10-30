# B07 / A031 — adaptive single-use payment of root KL rows

**Status:** PROVED at the stated scope; independent review pending. Universal GU and full FEI remain OPEN.

## Frozen target

- Primary packet: **A031**.
- Stable gap: `G-GU-SIGNED-KL`.
- Claim: `B07-A031-ADAPTIVE-ROOT-NONREUSE-v1`.
- Prior bound: at any one Boolean function, the empty upper-set rows satisfy
  \(\sum_iK_i^{(0)}\le(2/\ln2)I\). It was not yet proved that this payment remains single-use through an adaptive physical restriction tree.

The candidate was: for every read-once adaptive restriction tree \(\mathcal T\),
\[
 \sum_{v\in\mathcal T^\circ}\Pr(E_v)K_{i_v}^{(0)}(f_v)
 \le {2\over\ln2}\operatorname{Var}(f).
\]

## Result

The candidate holds. At node \(v\), write
\[
d_v=\widehat {f_v}(\{i_v\})=\mathbb E[f x_{i_v}\mid E_v].
\]
The sharp Boolean root inequality gives
\[
K_{i_v}^{(0)}(f_v)\le {2\over\ln2}d_v^2.
\]
The node functions
\[
\psi_v={\mathbf1_{E_v}x_{i_v}\over\sqrt{\Pr(E_v)}}
\]
are orthonormal: incomparable nodes have disjoint support, while at a descendant the ancestor coordinate is fixed and the descendant query coordinate remains fair. Hence Bessel gives
\[
\boxed{
\sum_v\Pr(E_v)K_{i_v}^{(0)}(f_v)
\le {2\over\ln2}\sum_v\Pr(E_v)d_v^2
\le {2\over\ln2}\operatorname{Var}(f)
\le {2\over\ln2}I(f).}
\]
For a complete tree the middle inequality is equality. The result is uniform in dimension, depth, branch bias, overlap, address count, and the adaptive order.

## Exact GU implication and remaining line

At the root, the sharp aggregate bound still gives
\[
\sum_iK_i^{(0)}\le c_0I,\qquad c_0={2\over\ln2}.
\]
Thus for fixed \(a\ge c_0\), \(0\le b<1\), it remains sufficient on tensor-prime Boolean functions to prove
\[
\boxed{
\sum_iK_i^{(+)}
\le(a-c_0)I+bU+\sum_i(\Gamma_i-B_i).}
\]
This yields universal \(G\le aI+bU\), then the source-reviewed restriction induction gives \(U\le aI/(1-b)\), and Theorem G gives
\[
H\le\left(2+{2a\over1-b}\right)I.
\]

The new theorem removes repeated root payment from recursive/stopping proofs: selected-coordinate root rows over the whole tree cost only \(c_0\operatorname{Var}(f)\), not \(c_0I\) per level. The first unpaid line is a comparison transporting parent nonempty rows to descendant root rows, including its signed correlation and terminal-\(U\) remainder. Such a comparison is not assumed here.

## Verification

`verify_adaptive_root_nonreuse.py` independently evaluates conditional means, singleton coefficients and root KL terms directly from Boolean truth tables. It checked:

- every Boolean function and every adaptive full read-once tree through dimension three;
- every four-bit Boolean function under a complete physical order;
- all 24 fixed orders on a deterministic 4,096-function four-bit sample;
- 1,000 seeded adaptive trees in dimensions five and six.

It passed 167,948 tree/function cases and 2,526,204 internal-node checks. Complete-tree energy equality was exact in dyadic arithmetic represented by binary floats, and the maximum sharp-KL surplus was zero. The computation is diagnostic; the all-dimensional proof is the displayed orthogonality argument.

## Scope and next action

This is not a universal pair \((a,b)\) and is not a proof of FEI. It proves that the already-paid Boolean root component does not create hidden depth loss. The next action for A031/A035 is to derive, for the first singleton nonempty row, an exact parent-to-child root comparison and retain the signed remainder; any dimension or correlation-gap factor must remain visible.

No protected source, scheduler, deployment, graph, email or publication action was taken. Exact model and separate effort metadata were not exposed.

