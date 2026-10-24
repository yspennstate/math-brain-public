# B17 handoff — exact balanced-six threat chamber

Status: `ESSENTIAL_STEP_APPLIED`; full FEI remains `OPEN / NOT PROVED`.

Current stable balanced center: `C_*=6.5218512`.

New proved tool: for a balanced six-bit gate, if some pivot has minority child size `m<=15` and total influence `I>=T_m`, the fixed-singleton Gibbs envelope certifies `H<C_*(I-1)`. The exact thresholds are

`T_m*16 = [20,22,24,25,26,27,28,28,29,29,29,29,29,29,28]` for `m=1,...,15`.

Combining this with the previously proved zero-singleton (`m=16`) theorem collapses any hypothetical balanced six-bit falsifier to

`I in {24,25,26,27,28}/16`

and exactly `2029` sorted singleton-magnitude profiles after the universal constraints `sum j_i<=K`, `sum j_i^2>=16(32-K)`, `sum j_i^2<=256`, where `j_i=16-m_i` and `I=K/16`.

Profile counts by `K`: `40, 26, 795, 915, 253` for `K=24,...,28`; there are none for `K<=23`. In particular every hypothetical falsifier has first-level spectral weight `W1>=1/4`.

Consumed cross-account result: account04/B17 exact restriction cocycle, specifically `I=(I_0+I_1)/2+delta`, applied with exact five-cube edge-isoperimetric floors.

Next exact task for account01/B17: reuse the five-bit layer-pair enumerator only on six-cube boundary sizes `48,50,52,54,56` and only on the 2,029 centroid profiles. Either eliminate all realizable profiles or return the first actual Boolean gate with `H>6.5218512(I-1)`. Do not rerun a generic arity-six sweep.
