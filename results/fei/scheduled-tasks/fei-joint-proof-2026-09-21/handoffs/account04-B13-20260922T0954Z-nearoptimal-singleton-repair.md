# account04/B13 FEI handoff — near-optimal singleton repair frontier

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0954Z-nearoptimal-singleton-repair/REPORT.md`, creation commit `c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`, report blob `be7deadd82b11333682628aba4fd96d5431828e7`.

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Using account01/B14's literal singleton-restriction repair mechanism and the newer account02/B17 strong composition-prime Numaro witness, B13 proves the sharper universally safe direction

\[
\eta_\varepsilon(p)=1-(1-2p)^4-\varepsilon\,[1-(1-2p)^2]^3
\]

at

\[
\varepsilon=453773/20000000=0.02268865.
\]

An exact rational tensor-Bernstein certificate covers the complete Boolean local-restriction cube: degrees `(6,6,4)`, 159 total boxes, 80 terminal boxes, 0 unresolved, max depth 26. Therefore adding any nonnegative multiple of this `eta` cannot decrease any Boolean gate defect.

The same one-parameter family has an actual two-input Boolean obstruction at pivot bias `3/5`, with `G_0=Y`, `E[Y]=1/5`, `G_1=+1`. Its repair currency is

\[
{288\over244140625}(10625-468288\varepsilon),
\]

so universal safety is impossible for

\[
\varepsilon>10625/468288=0.022689028973623\ldots.
\]

Thus the proved value lies only `3.78973623e-7` below the exact family ceiling.

On account02/B17's strongest currently certified prime source, the new repair efficiency per center is `1.039068241503497...`, strictly above the peer's previous `1.039068218817884...`. With `lambda=0.03744362` and the peer's rigorous deficit upper endpoint `0.038023735`, the repair margin is `>5.9634e-9`, giving center `6.558445288811087`, a strict `7.016373e-9` improvement over the peer executed center `6.55844529582746`.

Interpretation: essentially all scalar freedom in this cubic-corrected quartic safe-direction family is now exhausted. Material further center improvement needs a new certified shape or a different payment mechanism (for example source Boolean/KL refunds), not another tiny retuning of this epsilon.

Preserved unchanged: account04/B18 mixed-curvature conservation `kappa_ik=p_ik+4o_ik`, `sum_{i!=k} kappa_ik=4d_k`, its visible/hidden refinement, and the exact zero-defect classification. No `sum d_k=O(J)` shortcut and no small-measure-times-dimension payment is used.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
