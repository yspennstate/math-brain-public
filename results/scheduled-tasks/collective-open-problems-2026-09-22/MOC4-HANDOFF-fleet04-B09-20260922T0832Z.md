# MOC4 handoff — fleet04/B09

Run `20260922T081236Z-b09-moc4-r37`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.

Source-bound report: `proofnet24/collective-MOC4/fleet04/B09/20260922T081236Z-b09-moc4-r37/REPORT.md`.

Consumed latest complete lead fleet03/B07 `20260922T060726Z-fleet03-B07-MOC4-r11` (`MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`) and assigned OTHER-account partner fleet01/B07 `20260922T070244Z-b07-moc4-r11` (`MOC4-EXTERNAL-SPINOR-HELLINGER-HOLE-v1`). Also retained fleet02/B09 `MOC4-SPIN4-SATURATION-EXCLUSION-v1`.

## New exact zero-face theorem

`MOC4-ZERO-FACE-BOGOLIUBOV-COFACTOR-RIGIDITY-v1`:

In an even-even gauge, write the genuine exterior-square orthogonal action as `z -> Mz + N conjugate(z)`. The inherited spinor identities give `det N=0` and `||N||_F^2=2(1-P_ij)`. If the corresponding original unitary entry is zero (`P_ij=0`), orthogonality makes `N` a contraction with Frobenius mass two. Hence its singular values are exactly `(1,1,0)`. If `u` and `v` are unit left/right kernel vectors, then

`M=e^{i phi} u v^T`, `adj(N)=e^{i psi} v u*`,

so

`|M_ab|^2=|cof_ab(N)|^2=(1-r_a)(1-c_b)`,

where `r_a=sum_b |N_ab|^2`, `c_b=sum_a |N_ab|^2`.

This is exact same-unitary geometry, singular/repeated-spectrum safe, and supplies a nonlinear equation absent from the Drury/Saxl outer relaxation.

## New finite outer-face reduction

`MOC4-ZERO-FACE-ALIGNED-EXTERNAL-REDUCTION-v1`:

At `P_ij=0`, nonnegativity of the singleton coordinate in any 72-vertex outer-hull decomposition kills every vertex with positive `P_ij`. Thus only 18 Weyl vertices with `sigma(i)!=j` and 12 external vertices with `tau(i)=j` can occur. A zero-face support violation therefore forces at least one of those 12 aligned external values above `M`.

The spectral-only shortcut `all aligned external values <= M` is false: relabel fleet01/B07's exact stress datum so its bad `tau` is identity. The endpoint set and exact excess remain unchanged, and the bad external vertex is then aligned with `(0,0)` while

`E_0-M=232716479/4000000000>0`.

So the next branch must use the cofactor rigidity, not spectra alone.

## Next exact obligation

`MOC4-ALIGNED-EXTERNAL-COFACTOR-PAYMENT-v1`: on the genuine zero face, combine the rank-two-partial-isometry/cofactor equations with the residual quaternion/Haar reserve, strict pair gaps and structured spectral coefficients to show every aligned external excess is paid back to at most `M`. The no-zero strict interior remains separate.

Exact rational consistency verifier and captured output are in the scientific run directory; no floating-point tolerance was used.
