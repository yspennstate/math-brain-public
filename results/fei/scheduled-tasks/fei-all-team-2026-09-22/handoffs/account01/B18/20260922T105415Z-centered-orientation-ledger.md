# account01/B18 handoff — centered orientation ledger

**Recipient:** account03/B19  
**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN_NOT_PROVED`.  
**Scientific source:** `yspennstate/math-open-problems`, commit `f37f278ea724a7810c3e167e05b3ccab719c42c4`, path `proofnet24/P03-fei/fleet-2026-09-22/account01/B18/20260922T105415Z-centered-orientation-ledger/REPORT.md`.

The direct centering of the hidden remainder is false. Since source-exactly
\[
\omega_{i\leftarrow j}=4r_{ij}-2c_{i\leftarrow j},
\]
one would get
\[
\omega_{i\leftarrow j}-4q_iq_j=4\delta_{ij}-2c_{i\leftarrow j},
\qquad \delta_{ij}=r_{ij}-q_iq_j.
\]
For any two-bit non-affine Boolean gate, `q_i=q_j=1/2`, `r_ij=1/4`, `c=1/2`, so this centered hidden remainder equals `-1`. Do not assume pointwise nonnegativity.

The exact nonnegative tensor-centered replacement is the pair I-projection cost
\[
I_{ij}=I(X_i;X_j)=D_{\rm KL,2}(P_{ij}\Vert P_i\otimes P_j)
=\Psi_{q_i,q_j}(\delta_{ij})\ge0,
\]
which vanishes on exact cross-factor tensor pairs. On a centered minimum-dimensional ratio-critical core of ratio `rho`, every physical block `A` obeys the new exact ledger
\[
\boxed{\operatorname{TC}(X_A)+\rho C_A+W_A
\le\sum_{i\in A}[h_2(q_i)-\rho q_i].}
\]
For every forest `T` on `A`, entropy chain rule gives `sum_{ij in T} I_ij <= TC(X_A)`, hence
\[
\boxed{
\sum_{ij\in E(T)}I(X_i;X_j)+\rho C_A+W_A
\le\sum_{i\in A}[h_2(q_i)-\rho q_i].
}
\]
This is a nonreusing, original-coordinate, tensor-compatible orientation payment using **true ratio-extremality**, not terminality alone. Pinsker yields `(8/ln2) sum_T delta_ij^2` as a corollary, but exact KL must remain primary.

Partner result actually applied: account02/B18 `LOG-WEIGHT-NECESSITY-v1`, corrected report commit `1d39bc35fbb7ce60be36242c3bee6ea6bec55445`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T101659Z-c-admission-failure-logweight-redirect/REPORT.md`. It rules out promoting a uniformly bounded quadratic compression to the universal logarithmic payment, so the exact `I_ij`/KL ledger is retained rather than collapsed to the Pinsker square.

**Next unpaid implication for B19/integration:** convert a genuinely obstructive signed complete-graph centered orientation contribution into a physical block/forest carrying a dimension-independent fraction of the needed exact mutual information, or book the residual cyclic dependence into another unspent block-information term. No free `|delta|`, `(delta)_+`, or raw `U_4=O(J)` step is available.
