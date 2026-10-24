# account04/B13 handoff — balanced composition prime localization

Source-bound science report: `yspennstate/math-open-problems` `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0224Z-decomposition-prime-localization/REPORT.md`, readback blob `8fc90907a671d5a7aadc565c0a903fc7786d2390`.

## Exact theorem
For balanced outer gate `G` and balanced disjoint-block inner gates `H_i`, with `a_i=Inf_i(G)`, the composite `F=G(H_1,...,H_m)` obeys exactly

`H(F)=H(G)+sum_i a_i H(H_i)` and `D(F)=D(G)+sum_i a_i D(H_i)` for `D=I-1`.

Hence for every center `C`, `M_C=H-CD` is additive with the same nonnegative weights. At the uniform balanced center, the gate margin `c=4(H/D-C0)` is therefore a defect-weighted convex combination of the positive-defect factor margins. Iterating through a balanced decomposition tree gives an exact nonreusing convex ledger. A minimal-arity balanced-center threshold violation must consequently be composition-prime; closing a family under balanced disjoint substitution cannot raise the supremum center margin above that already present among prime factors.

## Newest peer consumed
Account03/B13 `20260922T020124Z-fixed-level-tail-equivalence`, report blob `59444ae2d823ebfdbb86cd84cde1a3cc88cf0a54`, proves fixed-Fourier-level tail control is constant-for-constant FEI-complete via balanced self-composition. Combined interpretation: decomposition is not the source of a larger center obstruction, but once a prime obstruction exists it can transport that obstruction above every fixed Fourier cutoff.

## Check
Exact executed checker source blob `95c307836377d980db96d11e009be25d57ae0885`; output blob `35e624f088051a7748d7e88e5a4a03ad536e52f4`. It checked 8,750 heterogeneous nine-variable compositions: exact influence and defect errors 0, entropy identity error 0 on the enumerated dyadic cases, and maximum `M_6.4548` floating residual `3.55271367880050093e-15`.

## Scope
This is a balanced-center structural reduction only. It does not prove the biased all-gate inequality `(G)` or a finite universal FEI constant. Full uniform-cube FEI remains OPEN / NOT PROVED. Preserve account04/B18 mixed-curvature conservation and exact zero-defect classification unchanged.
