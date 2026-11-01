# POS3 fleet02/B19 — newest named-partner uptake and the remaining global interface

**Outcome remains:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

A newer named-partner report arrived after the lead-r14 addendum and is incorporated here:

- fleet03/B10, `proofnet24/collective-POS3/fleet03/B10/20260922T051823Z-fleet03-B10-r11/REPORT.md`;
- report blob `8413593b751695eba06afe73a83ca2ad09e1c191`.

It proves, for the exact first-element deletion tilt `d mu/d nu=W/M` with `W=kappa+1`, that every deletion-balanced pair has actual-law minority `>4/27`; combining this with the OTHER-account rank-variance bound localizes every such pair to strong-majority distance at most `3786`. It also retains the earlier exact shallow/deep decomposition: all but `<1/81` of the tilt transfer is represented by at most `741` shallow first-hit states. Its first missing implication is the `BR3786-SH741` adaptive transfer lemma, not another tail estimate.

This sharpens the joint route with lead fleet04/B10 r14. The lead now supplies an actual cover gap `H={x<a<y}` of mass `>1/3` and at least two external relation distinguishers. The new B19 nine-element autonomous-prime width-three witness shows that exactly two such distinguishers can coexist with **no balanced pair anywhere in the full five-vertex cover/witness neighborhood**. Therefore the partner's deletion-balanced pair cannot be assumed to live inside that local neighborhood; a valid proof must link the heavy-cover `F*G` flux to an external bounded-span deletion pair or to a structural descent/decomposition.

There is a second exact obstruction to a tempting shortcut. In the same nine-element witness, let `p,z` be the two external relation distinguishers for the heavy cover `x lessdot y` relative to `a`. The two most direct witness-crossing events are

`E_p={x<p}`, `E_z={z<y}`.

Exact enumeration of all `499` uniform extensions gives

`Pr(H)=201/499`,
`Pr(E_p)=126/499`,
`Pr(E_z)=125/499`,

but

`Pr(H \ (E_p union E_z))=90/499>0`.

Hence the structural two-witness export theorem is **not** itself an event-cover of the target-scale heavy gap, and one cannot pigeonhole the `>1/3` gap mass directly onto the two witness-order events. The exact pattern counts `(H,E_p,E_z)` are

`000:180, 001:66, 010:52, 100:90, 101:37, 110:52, 111:22`.

The executable certificate is `verify_two_witness_gap_noncover.py`, execution SHA-256 `7b7e244b1b7c5e1a8a0de4c702a782bc2250a70277ec65b0473d8864d82b3362`; captured output SHA-256 `704a7ac9c3ce60c8e7c087fe04ae8d8be08e60bdc27af5e42b4184e8d720812b`, terminal marker `POS3_TWO_WITNESS_HEAVY_GAP_NONCOVER_PASS`.

The first essential missing implication after applying both latest lead and latest named partner is therefore:

> **HC2W–BR3786 global recycling/overlap lemma.** In a cardinality-minimal no-balanced width-three candidate, a lead-r14 heavy cover with `Pr(x<a<y)>1/3` and its at-least-two external relation witnesses must, through the actual three-chain `F*G` flow rather than a fictitious witness-event partition, force either (i) a deletion-balanced pair of strong-majority span at most `3786` whose exact `W`-tilt remains balanced after the `741`-state shallow/deep decomposition, or (ii) strict strong-majority span descent, a width-four antichain, a proper autonomous nonchain, or another already-isolated structural exit.

The B19 witness proves that any proof of this implication must use vertices/flow outside the immediate heavy-cover witness neighborhood. No claim of target-level closure is made.
