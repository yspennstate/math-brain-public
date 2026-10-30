# Publication-time source refresh

Run: `20260924T083540Z-fleet03-B01-qform-auto11-r48`.


The live correction ledger was refreshed. In particular this report respects:

- `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`: no use is made of `int |t|^(-1/2)||G_t||_2 dt`;
- fleet01/B02's fresh `QFORM-PIVOT-ABS-ACTUAL-MODULATION-L1-FALSE-v1`, canonical math source `0efcc1828226b25340cc3cefe7dfd6d16b46fb79`: no scalar-pivot proof is absoluteized before retaining its residual phase;
- the standing phase-aligned-density correction: no law-uniform scalar pointwise quadratic-phase power decay is used.

The designated fleet04/B01 dependency actually used is the `L^r` hyperbolic residual handoff whose canonical math commit is `f7e82d169badc671968036252d351b8533cdd425`; at `r=2` it supplies `||p_Z||_2<=sqrt(2)|c|^{-1/2}`, which is converted in REPORT.md to the explicit signed-Fejer inequality.

Full QFORM remains open; the new results are supporting averaged-frequency/phase-space theorems. Continuity is not claimed.
