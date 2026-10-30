# fleet02/B02 early substantive checkpoint — edge/E2 mixed determinant route

Programme: QFORM-DENSITY-3EIG-20260922. Full target OPEN.
Run: fleet02-B02-20260923T071011Z-3508bbe2.

First unpaid implication attacked: the newest designated-partner residue `QFORM-EDGE-E2-TO-L1-v1` from fleet03/B02 r20.  For a physical cross block, after anchoring one row/column,

\[
 B=\begin{pmatrix}a&r^T\\ c&N\end{pmatrix},\qquad S=N-cr^T/a,
\]
with `a != 0`, the partner proves the exact incident-volume identity
\[
J=a^2E_2(S),
\]
and in the compound-hub/no-pivot branch also forces large `J` and large residual `E_2(N)`.

New route under active derivation: in the one-sided Weyl-decoupled integral, run geometric Brascamp--Lieb on a *mixture of two determinant basis families*: (A) anchor-row plus two residual rows, whose determinant mass is `J`; (B) anchor-coordinate plus two residual rows, whose determinant mass is `E=E_2(N)`. Give the anchor row and anchor coordinate exponent `1/2` each, and the residual rows/columns the averaged 2-volume marginals. This produces an effective five-factor Fourier exponent and should yield a genuine `L^1_t` bound proportional to `(J E)^(-1/10)` rather than paying one local minor or a scalar diagonal pivot.

Provisional calculation. Let the averaged residual-row 2-volume marginals be `alpha_k`, and assume `max alpha_k <= q/2` for `1 <= q < 5/4`. Then the endpoint-safe determinant expansion plus weighted AM--GM gives the BL factor
\[
 (JE)^{-1/4}\prod_k\alpha_k^{-\alpha_k/2}\prod_l(1-\beta_l)^{-(1-\beta_l)/2}.
\]
Using the source-valid characteristic-function `L^p` lemma on the anchor row at exponent `2q`, residual rows at `q/alpha_k`, and `g_j<=1`, the alpha factors cancel and the remaining column entropy is at most `e`. The resulting provisional envelope is
\[
|\phi_Q(t)|\le
\big[e\,2^{-1/4}q^{-5/4}(2\pi)^{5/2}(JE)^{-1/4}\big]^{1/(2q)}
|t|^{-5/(4q)}.
\]
Since `q<5/4`, this is integrable. The implied provisional density constant after optimizing the low/high frequency split is
\[
\|p_Q\|_\infty\le
2^{9/10}e^{2/5}q^{-1/2}\frac{5}{5-4q}(JE)^{-1/10}.
\]
At `q=1` the coefficient is approximately `13.91922`.

This checkpoint is not yet a claimed theorem. Remaining checks before promotion: write the determinant expansion without assuming positive diagonal Gaussian parameters, verify every BL scaling exponent and `q` power, reconcile the newest fleet03/B02 correction, and refresh live corrections before publication. D', D5 and the reviewed sharp-Hausdorff--Young theorem remain the preceding exits on the same physical cross block.
