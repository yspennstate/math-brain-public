SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T09:37:09Z.
attacking: near-collinear zero-anchor arbitrary-background receiver: isolate genuinely transverse same-bank curvature and convert it to aggregate bordered cross-volume before reciprocal payment.

# Early substantive checkpoint

Consider the zero-anchor chamber
\[
A=\begin{pmatrix}0&0&a^T\\0&0&b^T\\a&b&C\end{pmatrix},\qquad b=\lambda a+\varepsilon,\quad \varepsilon\perp a.
\]
All coordinates are original independent coordinates; outside coordinates may be conditioned first, creating only affine terms.

## 1. Strong transverse-background budget
Let `u=a/||a||` (when `a!=0`) and `P=I-uu^T`. In the orthogonal decomposition of the Z-bank as `span{u} direct_sum u^perp`, construct H by replacing `b` by `lambda a` and replacing C by its central-row/central-column part
\[
C_0=C-PCP.
\]
Then H is an arrowhead supported by the single central coordinate u: in the block decomposition (all leaves, u) it has the form
\[
H=\begin{pmatrix}0&v\\v^T&c\end{pmatrix},
\]
so `rank(H)<=2`. Moreover
\[
A-H=\begin{pmatrix}0&0&0\\0&0&\varepsilon^T\\0&\varepsilon&PCP\end{pmatrix}.
\]
The symmetric epsilon-star has operator norm exactly `||epsilon||`, hence
\[
\|A-H\|_{op}\le \|\varepsilon\|+\|PCP\|_{op}.
\]
By Eckart--Young,
\[
\boxed{s_3(A)\le \|\varepsilon\|+\|P_{a^\perp} C P_{a^\perp}\|_{op}.}
\]
In particular, under the target normalization `s3(A)>=1`, either `||epsilon||>=1/2` or the genuinely transverse background curvature obeys `||P C P||op>=1/2`. This sharpens the partner fleet02/B06 budget `||epsilon||+||C||op>=1` by discarding the rank-two-payable central row/column of C.

## 2. Bordered cross third-volume identity
Split the Z coordinates physically as `S disjoint_union T`. Put `I={X} union S`, `J={Y} union T`. The original-coordinate cross block is
\[
M=\begin{pmatrix}0&a_T^T\\ b_S&C_{ST}\end{pmatrix}.
\]
Assume `a_T!=0,b_S!=0`, set `q=a_T/||a_T||`, `p=b_S/||b_S||`, and
\[
C_\perp=P_{p^\perp}C_{ST}P_{q^\perp}.
\]
Rotate only for the deterministic singular-value calculation on the row/column Euclidean spaces, sending p and q to their first coordinate. For every residual row r and residual column c, the 3x3 minor using the anchor row X, the p-row, the residual row r and the anchor column Y, q-column, residual column c equals
\[
-\|a_T\|\,\|b_S\|\,(C_\perp)_{rc}.
\]
Since the squared 3-volume
\[
E_3(M):=e_3(MM^T)=\sum_{|R|=|K|=3}\det(M_{R,K})^2
\]
is invariant under these row/column orthogonal changes, summing this explicit family of minors gives
\[
\boxed{E_3(M)\ge \|a_T\|^2\|b_S\|^2\|P_{b_S^\perp}C_{ST}P_{a_T^\perp}\|_F^2.}
\]
This spends a full aggregate of curved cross volume; it does not select or invert one physical minor.

## 3. Planned receiver splice
The partner fleet02/B06 theorem `QFORM-SHARED-COEFFICIENT-MAX-RECIPROCAL-v1` pays the large star-area branch because
\[
\Delta(a,b)=\sqrt{\|a\|^2\|b\|^2-(a\cdot b)^2}=\|a\|\,\|\varepsilon\|,
\]
and gives
\[
\|p_Q\|_\infty\le 2\sqrt{e/\Delta(a,b)}.
\]
For the complementary branch, the newest Claude volume-sampling theorem D/D' will be applied to the bordered cross block M using the displayed E3 lower bound. The remaining obstruction will be stated explicitly as a high-volume-marginal/heavy-row concentration or failure of every physical split to expose transverse C.

Status: checkpoint only; full target remains open.
