# account01/B17 handoff — periodic diffuse cube frames approach 3sqrt(2) from below

Programme `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.
Run `20260922T123638Z-account01-B17-qform-diffuse-edgeworth-v1`.
Classification `AUXILIARY_ONLY / SHARP_WITNESS_CONSTRAINT`; full conjecture remains OPEN.
Execution `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `yspennstate/math-open-problems@15e9504309108d37a6c5f8bcacebac07eb4fe1ff`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260922T123638Z-account01-B17-qform-diffuse-edgeworth-v1/REPORT.md`.
Exact coefficient checker: `yspennstate/math-open-problems@db8998c4f9445d8cd290795138c0a323b3d37fe3`, same run root `check_exact.py`; saved PASS output commit `1203b2522df2e15b8bd55f5261d8a89f89ef558b`.

Named partner actually applied: account02/B17 lower-bound theorem `yspennstate/math-open-problems@4a3d4af77778f20a95855c6dfbf69540dcfa5fe4`, proving `C>=3sqrt(2)` from diffuse uniform block averages.

New theorem. Fix a finite spanning row pattern `v_1,...,v_r in R^3` with `sum v_j v_j^T=I_3`. Repeat the pattern `m` times with rows `v_j/sqrt(m)` and use iid physical inputs `Uniform[-1/2,1/2]`. For `J=diag(1,1,-1)`, the resulting rank-three matrix has spectrum `(+1,+1,-1)`. Put `s_j=v_{j1}^2+v_{j2}^2`, `t_j=v_{j3}^2` and

`E_J(v_j)=57 s_j^2/32 + 15 s_j t_j/4 + 3 t_j^2/4`.

Then the zero-density has the Edgeworth expansion

`p_Q(0)=3sqrt(2)[1-(1/(20m)) sum_j E_J(v_j)+O(m^-2)]`.

Every coefficient is strictly positive, with `E_J(v)>=(3/4)||v||^4`. Hence `sum_j E_J(v_j)>=27/(4r)` and the first finite-size correction is always negative. In terms of `n=rm`, the relative first-order deficit is at least `27/(80n)`.

Canonical examples:
- disjoint three-block averages: `p_Q(0)=3sqrt(2)[1-69/(320m)+O(m^-2)]`;
- four-row Hadamard periodic frame: `p_Q(0)=3sqrt(2)[1-123/(640m)+O(m^-2)] = 3sqrt(2)[1-123/(160n)+O(n^-2)]`.

The exact cone calculation behind the sign is source-local: for the normalized Gaussian cone measure on `z1^2+z2^2-z3^2=0`,
`E H_{4,v}=57s^2/32+15st/4+3t^2/4`; standardized uniforms have fourth cumulant `-6/5`, giving the negative factor `-1/20`.

Consequence: no fixed-pattern periodic diffuse uniform-cube frame can beat `3sqrt(2)` by a small finite-size correction. Any witness above `3sqrt(2)` must use a genuinely mesoscopic/nonperiodic frame, non-uniform density-one supports, or another non-Edgeworth mechanism.

Fresh corrections consumed: `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. None conflicts with this witness-side theorem.

Unpaid target implication: arbitrary bounded-density product laws and arbitrary rotated matrices remain uncontrolled. Next B17 witness mechanism should leave the fixed-period diffuse uniform-cube regime rather than perturb it further.
