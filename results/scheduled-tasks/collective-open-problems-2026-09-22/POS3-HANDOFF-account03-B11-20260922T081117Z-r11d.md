# POS3 handoff — account03/B11 — shared-support chain identity

Run `20260922T081117Z-account03-B11-pos3-r11d`; outcome `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**; execution context `WITHOUT_VERIFIED_BRAIN`.

## Sources consumed

- Immediate account03/B11 predecessor: `proofnet24/collective-POS3/account03/B11/20260922T074511Z-b11-pos3-r11c/REPORT.md`, blob `53d2dd83cc5691143f968fe40fac1bf962791673`.
- Named OTHER-account partner: account04/B19 run `B19-20260922T071535Z-r46`, report blob `26c2eab1c40a8da73357764efd0aab4160391e07`.
- New scientific report: `proofnet24/collective-POS3/account03/B11/20260922T081117Z-account03-B11-pos3-r11d/REPORT.md`, blob `56374ff9d4b1bf188929919d05e52b34c00868b6`.

## New exact implication

If an incomparable pair `p||q` has exactly two positive upper distinguishers forming a chain

`p<u<v`, `q||u,v`,

then full linear-extension multiplicities satisfy the exact identity

`N(q<u)=2N(q<p)`.

The proof is fiberwise: after deleting `p,q,u,v`, the remaining skeleton gives identical admissible gap intervals for `p,q`; the two legal words `q p u v` and `p q u v` have exactly equal lift multiplicity. The order-dual identity holds for two comparable positive lower distinguishers.

## Application to the current fully crossed residual

The predecessor reduced the live minimum-support branch to

`l<a<r`, `x<y`, `l<y`, `x<r`,
`l||x`, `a||x,y`, `r||y`,
`l prec_* x prec_* a prec_* y prec_* r`,

with exactly one additional positive support on each charged side.

If both charged sides reuse the same support `z`, positivity plus `x<y` forces

`l<z<r`, `z||x,y`.

- If `a<z`, apply the exact identity to `(l,x)` with distinguishers `a,z`: `N(x<a)=2N(x<l)`. Since `l prec_* x`, the right side is `<2E/3`, contradicting `x prec_* a`.
- If `z<a`, the dual identity on `(y,r)` gives `N(a<y)=2N(r<y)<2E/3`, contradicting `a prec_* y`.

Hence a shared support must satisfy `a||z`. Minimum support then forces

`l lessdot a,z lessdot r`.

Both `{a,z,x}` and `{a,z,y}` are three-antichains. None of `l,x,y,r` distinguishes `a,z`; therefore a no-balanced counterexample forces at least two **fresh external** distinguishers of the new central pair `a||z` (and exactly two must have coherent sign by the existing sign theorem). The shared-support branch is thus transferred into the controlled multi-distinguisher/double-fork branch.

## Remaining first implication

**DISJOINT DOUBLE-SUPPORT TRANSPORT:** assume the unique positive external support of `l||x` and the unique positive external support of `y||r` are distinct. Classify their lower/upper types and use exact multiplicities plus width three to force balance, strict strong-majority span descent, autonomous/ordinal reduction, or an already controlled charged corridor.

Regression: `811` exact gap fibers and all `5,230` naturally labelled posets through `n=6`; `1,326` ordered two-upper-chain cases satisfy the factor-two identity. Verifier terminates `POS3_SHARED_SUPPORT_CHAIN_CHECK_PASS`.
