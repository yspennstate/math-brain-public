# Post-report peer update — safe-split envelope

After the B14 report and checker were read back, a newer compatible cross-account result landed:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T004033Z-prime-safe-split/REPORT.md`, commit `d96b3f494236cacf75f4ae0d4395f0f2dbb3008c`.

It independently proves the same Shannon/Poincare recursion used in the B14 report, then sharpens the induction interface. For a fixed base potential `Gamma`, write `P_G=I(G;p)/4-p_out(1-p_out)`, `S_c=D_Gamma+c P_G`, and on a Shannon split write `Q_i=t(1-t)[d-(p_1-p_0)^2]` and `c_{R,i}=-R_i/Q_i`. The exact recursion is

`S_c(G)=(1-t)S_c(G_0)+tS_c(G_1)+Q_i(c-c_{R,i})`.

The peer theorem proves that it is sufficient, after composition-prime reduction, to have **one** essential split with `c_{R,i}<=c` at every prime gate. It also proves the converse minimal-obstruction localization: if some gate has negative `S_c`, then a minimum-essential-input counterexample is composition-prime, all proper restrictions have nonnegative `S_c`, and **every** essential first split has `c_{R,i}>c`.

Applied at the exact decimal threshold `c=0.2681828`, the source-valid balanced n=18 obstruction yields a composition-prime gate of arity `2<=r<=18` at an interior bias vector with `c_{R,i}>0.2681828` for every essential coordinate. Thus a clever first-coordinate choice alone cannot repair the old read-once potential at the old AND-margin scale.

This is compatible with, and stronger than, the B14 report's replacement obligation. The current sharp target is now:

`sup over composition-prime gates and interior biases of min_i c_{R,i} < infinity`

for some replacement finite-cap base potential, or alternatively a quantitative child-slack stability theorem strong enough to rescue the cases where every local residual is negative. The old read-once base is already forced above `0.2681828` in this selector currency.

Full uniform-cube FEI remains OPEN / NOT PROVED. This update records peer integration only; it makes no novelty claim for the overlapping recursion identity.
