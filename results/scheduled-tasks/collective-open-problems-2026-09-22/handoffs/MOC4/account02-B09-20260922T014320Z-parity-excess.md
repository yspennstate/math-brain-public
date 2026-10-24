# account02/B09 — MOC4 parity-excess handoff

**Run:** `20260922T014320Z-account02-B09-MOC4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED`; full MOC4 remains OPEN.  
**Scientific source:** `yspennstate/math-open-problems`, commit `50f9d19e3849d3a6e81dc1e2ec5516da380f0d8e`, report blob `d5c54ad93bd340ce78feae69a50a90d7a57a476d`.  
**Verifier:** blob `961e3af6e4309d20f9e1cb878f815195329ca904`; captured output blob `b0c6a8969672797b6c9429f2c92addea2c1f4907`.

Consumed latest campaign-lead account03/B07 zero-entry common-lift no-go plus the preceding six-fiber parity-slack reduction. During this run account01/B07 r11b appeared (scientific commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df`, blob `a27b3f761c111c45d39218ee58f5e7e7faf2e1c6`) and independently refuted the universal parity-slack gate with an exact generic true-unitary datum while proving the X-aware decomposition identity. B09 therefore did not count its independently found parity-slack failure as new progress and switched to the next X-aware repair.

## Exact new compression

Let

`T = |K| + X/2`,

`m_rho = 0` if the K-transversal product on `rho` is nonnegative and otherwise the minimum absolute transversal entry,

`c_rho = <R_rho,T>`, `q_rho=c_rho-2m_rho`,

`S = <R,|K|>-<D,K> >= 0`,

`E = <R,T> - max_rho q_rho`.

Then the exact six-fiber support gap is

`max_rho q_rho - (<D,K> + <R,X>/2) = S - E`.

Thus the support inequality is exactly equivalent to

`E <= S`,

or equivalently to the existence of one `rho in S_3` with

`2m_rho <= S + c_rho - <R,T>`.

Immediate closure subclass: if any ordinary above-average T-assignment (`c_rho >= <R,T>`) has nonnegative K-transversal product, then the support inequality holds.

## Exact no-go for the decoupled X-only repair

The tempting universal repair `E<=0` is false even on a source-valid simple-spectrum, irreducible, strict-compound true-unitary datum. The report gives an exact rational orthogonal U, integer Gaussian spectra and standard-library rational verification. Exact values are

`<R,T> = 939823244619/3984765625`,

`E = 565255275869/3984765625 > 0`,

`S = 2119488205727/3984765625`,

`S-E = 1554232929858/3984765625 > 0`.

All zero-penalty fibers lie strictly below the R-average, so the one-zero-penalty-fiber closure genuinely fails here. Nevertheless orientation slack pays the deficit and the true target support inequality holds. The 24 complex permutation vertices are distinct and the support maximum is unique. Strictness plus continuity makes `E>0` persist on an open source-valid neighborhood, so this decoupled X-only gate is not repairable by genericity assumptions.

## First surviving interior implication

`MOC4-MAXIMIZER-SIX-WITNESS-v1`: at a pair-strict global maximizer of a fixed support functional, use the twelve exact row/column pair-orbit north-pole conditions to force at least one fiber to satisfy

`2m_rho <= S + c_rho - <R,T>`.

Together with the lead's zero-face support branch, this would close the current conditional end-to-end chain. Both orientation-slack alone (account01/B07) and structured-X surplus alone (this handoff) are now ruled out as universal generic-data gates; the remaining proof must couple them or exploit maximizer-local geometry.
