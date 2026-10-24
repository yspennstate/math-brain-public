# Independent chain challenge: separated hierarchy payment

Target: `B05-A023-SEPARATED-HIERARCHY-PAYMENT-v1` at canonical commit
`72824efa4229ee109fc344f1a021840982509ee5`.

## Independently selected risks

1. **Fourier normalization.** Reconstruct every coefficient packet for a
   one-word selector rather than importing the author's formula.
2. **Upper-set caps.** Include child frequencies above the empty child
   frequency; this is where the scalar interaction term enters.
3. **Physical selector influence.** Count both endpoints of every active-word
   selector edge, yielding `2 p d theta`, not `p d theta`.
4. **Reach weighting.** Verify that every descendant selector coordinate is
   pivotal only on its unique ancestor event, with factor `w_v`.
5. **Terminal retention.** Confirm that the leaf `U` packets telescope with
   exactly their physical leaf probabilities and are never silently dropped.
6. **Singular regimes.** Check `theta=0`, `Delta=0`, balanced children,
   deterministic children, `d=1`, and rare `p`.
7. **Scope boundary.** Attempt no transfer to shared-variable siblings; their
   Fourier packets collide and invalidate the disjoint-support table.

## Result

All seven risks are discharged at the declared separated, fresh-variable
scope.  The exact coefficient/cap reconstruction appears in `REPORT.md`.
The independent checker exhausts all pairs of Boolean cores through two
variables for selector depths 1 through 5, plus every four-leaf one-bit
balanced tree and every four-leaf one-bit depth-three comb.

The claim is accepted at its stated scope.  It is not a universal FEI
payment and does not cover reused address bits, overlapping sibling spectra,
or arbitrary retained leaf packets.
