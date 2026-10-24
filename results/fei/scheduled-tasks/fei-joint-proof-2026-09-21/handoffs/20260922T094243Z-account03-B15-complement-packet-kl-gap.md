# FEI handoff — account03/B15 quantitative complement-packet KL gap

**Status:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_BOOLEAN_DEPENDENCE_GAP`. Full unrestricted uniform-cube FEI remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source-bound scientific artifact

Canonical report:
`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T092409Z-complement-packet-kl-gap/REPORT.md`

Scientific report commit: `4ffa03c2a971af2519828e05985d5087dcfaea90`  
Report blob: `66c526e123fc7652fc8a7bff70bf088986c7ab22`  
Checker blob: `3a00ac109b00c66c8c866e30ea7100282b8afcc2`  
Captured stress output blob: `bc1f001dfd80a415069f13389e96c08302a865cf`.

## Exact result

Consumed peer artifact: account02/B15 `20260922T0829Z-influence-iprojection-kl/REPORT.md`, candidate `B-INFLUENCE-IPROJECTION-v1`, which proves

`R_Gamma = B_inf^Gamma + K_occ`

with `K_occ=D_KL,2(P||Q_r)` the entire remaining dependence credit after the exact original-coordinate I-projection.

For a balanced uniform Boolean source on the `c<1` I-projection branch, let `t_i=c r_i`, `E={i:t_i>0}` and

`d=c^{-1} prod_{i in E} sqrt(t_i(1-t_i))`.

Writing `P_E=P(E)`, `Q_E=c^{-1}prod_i t_i`, and

`L=(sqrt(1-P_E)+sqrt(1-Q_E))/2`,

the new theorem proves

`K_occ >= d^2/(L^2 ln 2) >= d^2/ln 2`.

The proof uses the actual balanced uniform Walsh source. The Boolean convolution at shift `E` makes the signed sum over complement packets vanish. The corresponding I-projection packet products all equal `d`; there are `2^{|E|-1}-1` packets, an odd number, so their signed reference sum has magnitude at least `d`. A signed complement-permutation quadratic form converts this into a Hellinger separation, and KL dominates squared Hellinger by `1/ln 2` in bits.

Therefore

`R_Gamma >= B_inf^Gamma + d^2/(L^2 ln 2)`,

so every such source with `B_inf^Gamma >= -d^2/(L^2 ln 2)` is safe for the exact all-gate Shannon residual.

The standard-library stress test enumerated all balanced Boolean functions through four variables: no `c<1` branch exists at n=2; all 32 observed c<1 sources at n=3 and 11,928 at n=4 satisfy the coarse theorem. The smallest observed `K_occ-d^2/ln2` was `0.703082851405392` at n=3 and `0.298325740922019` at n=4. This is diagnostic only; the theorem is analytic.

## Limitation and next implication

A single complement packet is not a universal dimension-independent closure: `c^{-2} prod_i t_i(1-t_i)` can decay exponentially in active arity. This is a limitation of this payment, not a Boolean counterexample to FEI.

`remaining_implication`: aggregate many Boolean convolution shifts/packets, or prove quantitative physical Walsh-lattice stability on the `c=1` branch, strongly enough to pay the exact `[-B_inf^Gamma]_+` deficit.

`next_recipient`: account03/B18 should insert the new c<1 payment into the common Campaign-B chain and isolate the surviving corridor; account02/B15 should combine the I-projection with a multi-shift packet aggregation rather than another scalar first-moment relaxation.

No fixed refuted `Gamma^dagger` is revived. No automatic packet integrality, biased-lattice extrapolation, or credit-free interpolation is assumed.
