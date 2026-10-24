# Early calculation: cone-aligned remote cells are transverse, not resonant

For the dense Householder latent form

\[
B=I_3-2nn^T,\qquad n=(1,1,1)/\sqrt3,
\]
let the six physical variables be paired into banks
\(S_j=(X_{j,1}+X_{j,2})/\sqrt2\), so \(Q=S^TBS\).  The physical synthesis has two rows \(e_j/\sqrt2\) per bank, hence \(C^TC=I_3\) and \(A=CBC^T\) has exact nonzero spectrum \(\{1,1,-1\}\).

Take one fixed product fragment cell whose three bank centers are \(R d\), \(d\ne0\).  Since every physical fragment has length at most one, its bank deviation \(u\) obeys \(|u_j|\le1/\sqrt2\), hence \(\|u\|\le L:=\sqrt{3/2}\).  Because \(B\) is orthogonal, some coordinate k has

\[
|(Bd)_k|\ge \|d\|/\sqrt3.
\]

If \(R\|d\|\ge3\sqrt2\), then throughout the cell

\[
|R(Bd)_k+(Bu)_k|\ge {R\|d\|\over2\sqrt3},
\]
so

\[
|\partial_{u_k} Q(Rd+u)|\ge {R\|d\|\over\sqrt3}.
\]

The cell's bank-space subdensity is at most \((\sqrt2)^3=2\sqrt2\), and its projection onto the other two bank coordinates has area at most \((\sqrt2)^2=2\).  One-dimensional coarea in \(u_k\) therefore gives, at every output level s,

\[
\boxed{\ \|p_{\rm cell}\|_\infty\le {4\sqrt6\over R\|d\|}.\ }
\]

Crucially this estimate does not contain \(q(d)=d^TBd\).  It therefore applies unchanged when d is an irrational exact null-cone direction, \(q(d)=0\).  Null alignment removes the \(R^2q(d)\) displacement used in the partner's rational-separation argument, but it leaves a transverse gradient of order R and hence only an O(1/R) cell contribution.

For a fixed finite fragmentation plan, summing all nonzero-center cells gives

\[
\sup_s p_{\ne0,R}(s)\le {4\sqrt6\over R}\sum_{d\ne0}{1\over\|d\|}=O(R^{-1}).
\]

The remaining zero-center cells are the only possible O(1) contribution and will be compared pointwise with the connected triangular-bank source in the full report.
