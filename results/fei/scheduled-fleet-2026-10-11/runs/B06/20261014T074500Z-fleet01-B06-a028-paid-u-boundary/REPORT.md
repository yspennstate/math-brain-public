# B06 / A028 — paid-\(U\) stopping boundary with branchwise coordinate reuse

**Status:** PROVED at the stated conditional scope; independent review pending. The universal residual estimate, universal GU, and full FEI remain OPEN.

## Frozen target

- Primary packet: **A028**.
- Stable gap: `G-GU-STOPPING-RESIDUAL`.
- Claim: `B06-A028-PAID-U-BOUNDARY-v1`.
- Prior bound: A028 had a fully paid but proper modulation hierarchy with genuine LTF terminals and path constant below \(4\). It did not give a universal stopping theorem. The newer B07 input paid root KL rows once over an adaptive tree, but had not been assembled with terminal \(U\) and the exact influence decrement.

The candidate was to turn these ingredients into one rigorous dimension-independent stopping implication that permits reuse of a physical coordinate on incomparable branches and does not assume a GU estimate at every intermediate node.

## Result

For a finite physical restriction tree \(\mathcal T\), define

\[
\rho_i(g)=\Delta_iU(g)-K_i^{(0)}(g)
=B_i(g)-\Gamma_i(g)+K_i^{(+)}(g),
\]

\[
\Pi_I(\mathcal T)=\sum_{v\in\mathcal T^\circ}p_v\operatorname{Inf}_{i_v}(f_v).
\]

Suppose there are absolute \(A,\kappa\ge0\), \(0\le b<1\), such that every nonconstant Boolean \(f\) has such a tree with

\[
U(f_\ell)\le\kappa I(f_\ell)\quad\text{at every leaf},
\qquad
\sum_vp_v\rho_{i_v}(f_v)\le A\Pi_I(\mathcal T)+bU(f).
\]

Then, with \(c_0=2/\ln2\),

\[
\boxed{U(f)\le
\frac{\max\{A,\kappa\}I(f)+c_0\operatorname{Var}(f)}{1-b}}
\le\frac{\max\{A,\kappa\}+c_0}{1-b}I(f).
\]

Therefore the source reduction gives the explicit FEI constant

\[
\boxed{C=2+\frac{2(\max\{A,\kappa\}+2/\ln2)}{1-b}}.
\]

The proof uses the exact telescopes

\[
\sum_vp_v\Delta_{i_v}U(f_v)=U(f)-\sum_\ell p_\ell U(f_\ell),
\qquad
\Pi_I=I(f)-\sum_\ell p_\ell I(f_\ell),
\]

and the B07 cumulative root-row payment

\[
\sum_vp_vK_{i_v}^{(0)}(f_v)\le(2/\ln2)\operatorname{Var}(f).
\]

Thus the terminal \(U\), normalization, root KL, and queried influence are all retained. The same physical coordinate may be queried on different branches: the root-row proof uses orthogonal node wavelets and the two telescopes are purely local, so no congestion factor appears.

## Exact movement and remaining obligation

This replaces the vague demand for a “paid stopping tree” by one strictly smaller explicit unpaid inequality:

\[
\boxed{\sum_v p_v\bigl(B_{i_v}-\Gamma_{i_v}+K_{i_v}^{(+)}\bigr)
\le A\bigl(I(f)-\mathbb E_\ell I(f_\ell)\bigr)+bU(f).}
\]

It is an aggregate path estimate, not an every-node assumption. It must hold with one fixed \(A,b\) for a tree whose leaves have one fixed \(\kappa\). The prior LTF modulation family supplies the terminal condition only on that proper family; it does not supply this residual inequality for an arbitrary first non-flat data collision.

At one function, universal GU is \(G=\sum_i\Delta_iU\le aI+bU\). GU gives the source good-coordinate restriction induction. The theorem here is a different, explicitly sufficient global \(U\)-drift certificate and shows exactly what a stopping proof must establish if it does not prove GU at every child. It does **not** establish a universal pair \((a,b)\).

## Verification

`verify_paid_u_boundary.py` computes Fourier spectra, upper-set masses, \(U\), \(I\), influences, restrictions, and root KL directly from Boolean truth tables. It checks both exact telescopes and the cumulative root-row inequality on exhaustive small first-reuse trees and seeded adaptive stopped trees. The run output is archived in `CHECK.out`. This computation audits identities and endpoint handling; the all-dimensional theorem is the proof in `PAID_U_BOUNDARY.tex`.

## Scope and next action

The next A028 attempt should target the first non-flat shared-data residual and prove the boxed aggregate estimate from actual query influence plus any released terminal reserve. It must retain the signed \(-\Gamma_i\) contribution and may not replace the aggregate inequality by a separately charged local GU assumption.

No protected source, held payload, scheduler, publication, deployment, live-store, graph, email, or paid-compute action was taken. Model/effort metadata was not exposed and is recorded as `UNKNOWN`.
