# B18 / A090 — independent review of the paid-boundary stopping assembly

**Verdict:** B06-A028-PAID-U-BOUNDARY-v1 **HOLDS at its stated conditional scope**. It is not a universal GU proof, and full FEI remains OPEN.

## Audited candidate

The source claim assumes fixed \(A,\kappa\ge0\), \(0\le b<1\), and for every Boolean \(f\) a finite physical restriction tree whose leaves obey

\[
U(f_\ell)\le\kappa I(f_\ell)
\]

and whose aggregate non-root residual obeys

\[
\sum_vp_v\left(\Delta_{i_v}U(f_v)-K_{i_v}^{(0)}(f_v)\right)
\le A\sum_vp_v\operatorname{Inf}_{i_v}(f_v)+bU(f).
\]

It claims

\[
U(f)\le
\frac{\max\{A,\kappa\}I(f)+(2/\ln2)\operatorname{Var}(f)}{1-b},
\]

hence

\[
H(f)\le
\left(2+\frac{2(\max\{A,\kappa\}+2/\ln2)}{1-b}\right)I(f).
\]

## Reconstruction

The proof chain is valid:

1. The \(U\)-increments telescope exactly to \(U(f)-\mathbb E_\ell U(f_\ell)\).
2. Query influences telescope exactly to \(I(f)-\mathbb E_\ell I(f_\ell)\); terminal influence is not charged twice.
3. The empty-row KL term satisfies \(K_i^{(0)}\le(2/\ln2)\widehat f(\{i\})^2\).
4. Adaptive node wavelets are orthonormal, even when a physical coordinate is queried on different incomparable branches, so the entire root-row payment is at most \((2/\ln2)\operatorname{Var}(f)\).
5. Adding the aggregate residual hypothesis and the leaf bound gives the displayed result with \(\max\{A,\kappa\}\). All terminal and normalization terms remain present.

The source FEI reduction was independently checked: \(H\le2I+2U\), so the displayed finite constant follows.

## First unsupported universal line

The theorem does **not** construct the required tree. The first unpaid line is:

\[
\boxed{\text{For every Boolean }f,\text{ find one finite physical tree satisfying both hypotheses with one fixed }(A,\kappa,b),\ b<1.}
\]

The known LTF-terminal modulation family supplies the leaf hypothesis only on a proper family. It does not prove the aggregate signed residual bound for an arbitrary first non-flat shared-data collision. Treating the conditional theorem as universal GU would be a quantifier error.

This is also a sufficient global \(U\)-drift route to FEI, not itself a proof of \(G\le aI+bU\).

## Independent computation

The new checker reconstructs \(U\), \(I\), restrictions, physical influences, and the root KL term directly from Boolean truth tables. It exhausts all Boolean functions and adaptive full trees through dimension three, then checks seeded stopped adaptive trees through dimension six, including branchwise physical-coordinate reuse. The archived output records the exact case counts and maximum residuals.

No material repair was needed, so this review is independent acceptance of the conditional theorem. It is not acceptance of the missing universal residual hypothesis or full FEI.
