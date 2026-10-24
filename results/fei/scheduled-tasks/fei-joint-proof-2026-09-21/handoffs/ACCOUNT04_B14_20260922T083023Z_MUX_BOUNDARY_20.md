# account04/B14 handoff — MUX deterministic-data boundary denominator 20

**Status:** ESSENTIAL_STEP_APPLIED; full FEI OPEN / NOT PROVED; WITHOUT_VERIFIED_BRAIN.

Scientific source: `yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260922T083023Z-mux-boundary-20/REPORT.md`, report blob `235317bb4035df1814d4ec04d973afc85685f01d`, readback commit `329e454a013a71a0d90a4cee68a3921134b327e2`.

Consumes newest account01/B18 `20260922T080302Z-mux-newborn-cancellation-121/REPORT.md` (blob `c08efa20ebf01b207ed3bb8ada31e8f258681084`) plus the h96 shape bounds recorded by account04/B18 and the earlier account01/B18 curvature-refunded restriction theorem.

For MUX selector/data biases `(p,x,y)`, put
`Q=p(1-p)x(1-x)`, `L=log2(16/Q)`.  The newest lead proved safety for `y<=Q/(121L)` and explicitly left `p Gamma^dagger(y)` unused.  B14 retains that term and applies the lead's own `|F_A'|<3` lemma also to the first moving old spectral atom.  The result is

`0 <= y <= Q/(20L)  =>  D_{Gamma^dagger}(MUX;p,x,y) >= 0`,

and by the same symmetries the analogous collar holds near all four deterministic data faces.  At `p=x=1/2` this enlarges the certified radius from `1/15488` to `1/2560`, factor `121/20=6.05`.

The scalar certificate is exact: after source bounds, the worst rate is at `L=8`; `2^73<160^10` gives `log2(160)>7.3`, and the remaining margin over the counterexample threshold is exactly positive, at least `1232701593/51200000000000` in the scalar rate.  Checker files are beside the report.

Preserve: no prescribed-coordinate payment; addressing obstruction remains; exact folded block drift remains `D_A=J-E J_child=I_A+C_A`; no crossing/refund is reused.

Next arrow for account01/B18: intersect the denominator-20 collars with the existing selector tube and account03/B14 terminal two-data-bit margin filter.  Attack only the resulting compact/interior MUX residual, or produce a source-valid negative point.  Even complete MUX closure does not close all composition-prime gates.
