# HARD7-03 correction to the 16:23Z idea note before theorem-level use

The immutable idea note `20260919T1623Z__idea-center-extreme-branch-kernel.md` contains one labeling error in the second symmetry event. Its numerical correction formula remains valid, but the second disjoint first-layer event for **one fixed left-centre adjacent pair** is not `A_1` being the maximum.

For the left-centre pair

`R=max(Y_{-1},Y_0)`, `X=Y_{-2}`, `Z=Y_1`,

there are two disjoint useful extreme events:

1. `E_L={A_{-1}>=A_0,A_1}`. Then `X,Y_{-1},Y_0` all have first-layer shift `A_{-1}`, so the left unique branch `X` gives the one-sided gap transform.
2. `E_M={A_0>=A_{-1},A_1}`. Then `Y_{-1},Y_0,Z` all have first-layer shift `A_0`, so the right unique branch `Z` gives the identical one-sided gap transform.

These events are disjoint almost surely and have the same exact expectation by iid symmetry. Therefore the per-centre-pair lower correction is still

`delta_ctr = 2 delta_left = 8 theta/(q a^4 b^2)`.

The reflected right-centre adjacent pair has the analogous two events `A_0` maximal and `A_1` maximal. Hence the total multiplicity across the two centre pairs and their two appearances in fourth-step windows is still four, and

`DeltaC_ctr = 4 delta_ctr = 32 theta/(q a^4 b^2)`

remains correct.

The checker uses only this corrected formula. No theorem-level report will repeat the incorrect event label from the exploratory idea note.