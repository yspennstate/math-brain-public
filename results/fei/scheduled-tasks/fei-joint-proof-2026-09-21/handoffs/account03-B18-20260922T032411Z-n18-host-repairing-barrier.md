# account03/B18 FEI handoff — exact n=18 host re-pairing barrier

**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_ADVERSARY_FAMILY_REFUTED`; full FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## Common target preserved

`LIMIT-PRIME-GATE-LIFT-v1` remains the single common target:

\[
C_*=6.5218512,
\qquad
\Gamma_*=\Gamma_{RO}+0.2682048\,p(1-p),
\]

and the unpaid universal implication remains `D_{Gamma_*}(P;p)>=0` for every finite composition-prime Boolean gate and every interior product bias.

## Peer artifact consumed

The completed account01/B12 exact 18-variable prime-gate artifact

`proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T011847Z-prime-n18-gate/REPORT.md`

was used substantively.  It gives `I=261/128`, a certified entropy interval around `6.7766053090059780825197902218918823`, and the exact nine-core/nine-host reconstruction with 18 exceptional core cells.

## New theorem

Keep those same 18 exceptional cells, but repartition them into nine two-cell host channels by an arbitrary perfect matching.  There are exactly `34,459,425` such matchings, and every one is a genuine balanced Boolean gate.

For a pair `{x,x'}`, its singleton-host Fourier block is nonzero on exactly 256 core characters, with squared mass `2^-16` on each.  Therefore every pair contributes exactly `1/16` spectral entropy, independent of pair geometry.  The whole gate entropy is consequently invariant under every re-pairing.

The influence contribution of a pair is `5/256` if `x,x'` have Hamming distance one and `11/512` otherwise, a quantized penalty `1/512` for each nonadjacent pair.  On the source 18-cell set the only nine Hamming-distance-one edges are exactly the published source pairs.  Hence the source pairing is the unique all-adjacent perfect matching.  If `k` is the number of nonadjacent pairs,

\[
I=\frac{261}{128}+\frac{k}{512},
\qquad
R=\frac{H}{I-1}=\frac{512H}{532+k}.
\]

Any non-source perfect matching has `k>=2`.  The published pairing therefore uniquely maximizes the balanced obstruction over the entire 34,459,425-member family, with

\[
R_{source}<6.521845710923046575658143972949<C_*,
\]

leaving stable-center gap at least `5.48907695342434e-6`; every non-source re-pairing has `R<6.497419322492624`.

Thus **re-pairing the same exceptional support cannot falsify the stable candidate**.  This is an analytic family closure, not a finite sweep.

## Remaining implication / recipients

The theorem covers the uniform balanced slice of the fixed-support two-cell-host family only.  It does not cover biased input vectors, replacing the exceptional support, unequal host-group sizes, or a different shared core.

The next useful adversarial move is therefore a changed exceptional support or heterogeneous host grouping, ideally tested against account02/B16's already-localized stable-candidate singleton/defect corridor rather than another re-pairing.  Builder-side workers can use the `1/512` penalty as a rigidity lemma for near-saturating fixed-core gates.

**Next recipients:** account02/B16 and account03/B17 for source-valid heterogeneous/corridor attacks; account01/B18 for the common candidate ledger.
