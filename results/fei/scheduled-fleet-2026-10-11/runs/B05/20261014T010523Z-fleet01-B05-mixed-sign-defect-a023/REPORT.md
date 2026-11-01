# B05 / A023 — mixed-sign point-defect hierarchy

## Outcome

**AUTHOR-PROVED PROPER-CLASS EXTENSION; INDEPENDENT REVIEW PENDING.**

The previously separate positive and negative point-defect tower results now
combine without a sign-homogeneity assumption.  For arbitrary ranks
(r_k\ge2), arbitrary signs (\sigma_k\in\{-1,+1\}), fresh disjoint blocks,
and

\[
F_1=A(wP),\qquad F_k=A(\sigma_kQ_{r_k}F_{k-1}),
\]

the implication

\[
U(P)\le\frac83I(P)
\quad\Longrightarrow\quad
\boxed{U(F_d)\le\frac83I(F_d)}
\]

holds uniformly in every parameter.  Every finite adaptive/pruned physical
restriction tree with one common disjoint terminal Boolean core (h) obeys

\[
\boxed{U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le\frac83I(F_d).}
\]

Consequently (H(F_d)\le22I(F_d)/3).

## New mechanism and reserve

At level (k), let (t_k=\sigma_k\beta_{r_k}\mathbb E F_{k-1}).  The exact
recurrence is

\[
\begin{aligned}
U_k&=\tfrac12U_{k-1}+\tfrac12U(Q_{r_k})+R(t_k),\\
I_k&=\tfrac12I_{k-1}+\tfrac12I(Q_{r_k})+\tfrac12(1-t_k).
\end{aligned}
\]

Positive nodes use the reviewed
(R(t)\le\frac43(1-t)).  Negative nodes use (R(t)\le1), which at
(c=8/3) creates at least (1/3) of fresh slack.  Writing
(D_k=\frac83I(F_k)-U(F_k)),

\[
\boxed{
D_d\ge2^{-(d-1)}D_1+rac13
\sum_{k:\,2\le k\le d,\,\sigma_k=-1}2^{-(d-k)}.}
\]

This discounted reserve is retained through the complete endpoint/tree
ledger; it is not merely discarded to prove nonnegativity.

## Class extension

- Previous reviewed positive class: all (\sigma_k=+1), constant (8/3).
- Previous reviewed negative class: all (\sigma_k=-1), constant (16/9)
  (with a later (5/3) strengthening still awaiting a fresh review).
- New class: arbitrary alternation of positive and negative defects and
  arbitrary rank sequence, uniformly at constant (8/3).

This matters because a hierarchy may change the sign of the rare coherent
core from one level to the next; separate homogeneous theorems did not cover
that behavior.

## Verification

The independent checker passed:

- 200,002 scalar-side grid checks;
- 2,048 direct Boolean towers from all 256 three-bit bases;
- 1,024 genuinely mixed-sign direct towers;
- 157,353 arbitrary-rank recurrence steps, including 78,762 negative levels;
- 120 adaptive/pruned tree checks;
- 120 direct terminal-core tensor-cancellation checks.

The smallest observed negative scalar reserve was exactly (1/3).

## Exact remaining gap

This still is an endpoint telescope.  It does not assign first-revelation
ownership to the mismatch/KL rare logarithm, and it does not survive changing,
overlapping, shared-variable, or leaf-dependent terminal cores.  Those are
the unpaid A023 obligations.  Full FEI remains **OPEN**.

