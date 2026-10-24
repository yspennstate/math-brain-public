# account04/B13 handoff — balanced six-bit dictator collar closed

Classification: `ESSENTIAL_STEP_APPLIED / BAL6_DICTATOR_COLLAR_CLOSED / FULL_FEI_OPEN`.

Source-bound scientific artifact:
`yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0729Z-six-bit-dictator-collar/REPORT.md`, creation commit `dd4629672944f3ddec40efff2079a38eeb777bf7`, readback blob `a4c8b0d8a9d90bc0437a546881582d04133ce93d`.

Newest compatible peer result consumed: account01/B13 `20260922T063239Z-six-bit-gibbs-shell`, scientific commit `4f330f0e645774b18bc2add4646c1b89a1c211bb`, report blob `12652ca949efdfe4eada1d64e23312fa142d15b4`.  That result forces any hypothetical live balanced six-bit falsifier to have `W1>=21/64`, all six singleton coefficients nonzero, and some singleton magnitude at least `1/4`.

New theorem: if a balanced six-bit Boolean gate has any singleton coefficient with magnitude at least `11/16`, then either it is a character or

`H(f) < 6 [ I(f)-1 ]`.

The proof uses the exact close-to-dictator mismatch representation.  If `a=|hat f({i})|`, balance forces `a=1-r/16` with the same `r` mismatch points in each five-bit half-cube.  For `r=1,...,5`, exact five-bit Walsh sums give the complete six-bit spectrum.  Translation/permutation orbit representatives for one mismatch half and all subsets for the other cover `28,122,488` ordered reduced cases.  Rational logarithm upper bounds and exact integer cross multiplication certify a global lower gap `6(I-1)-H >= 0.033082813`; no floating-point sign is used.

Owner-comparable consequence at the read-once base centre `C0=6.4548`: every nondegenerate gate in this collar has

`c_f = 4(H/(I-1)-C0) < -1.8192`.

Therefore the account01/B13 chamber is now compact.  Six-bit Walsh quantization gives every hypothetical live falsifier

`1/16 <= |hat f({i})| <= 5/8` for all i,
`sum_i hat f({i})^2 >= 21/64`,

and a strong pivot with `1/4 <= |hat f({i})| <= 5/8`.  Its two five-bit child output probabilities lie in the compact bands `[3/16,3/8]` and `[5/8,13/16]`.  The next exact target is to pay that compact strongly-unbalanced five-bit child pair with actual child slack plus the exact restriction cocycle, or construct a genuine Boolean counterexample in the chamber.

Account04/B18 mixed-curvature conservation and its exact zero-defect classification are preserved unchanged.  No `sum d_k=O(J)` step and no ambient-dimension continuity charge is introduced.  Full FEI remains OPEN.
