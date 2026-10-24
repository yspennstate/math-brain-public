# account01/B06 r14 — full fixed-multiplicity audit

Source pins: historical baseline `7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`; current standalone candidate `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, `improvements/interactive/20260924T145418Z-nine-400/paper.tex` blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`. Fresh controls: AGENTS blob `207b1dfce26c35dd8437cb469a807071aa5a0f08`; CURRENT_OBJECTIVE blob `194c09609c2ce750efaa9634a0849b5a27ff651c`.

I read all 790 historical lines, all 955 current lines, root README/AUDIT/proof_map/SOURCE_MANIFEST/verify/checks/DELIVERY_STATUS, and the nine-paper README/NINE_400_AND_OVERLAP/AUDIT_NEW/MANIFEST/proof_map/verify_new/checks_new.

## Verdict

Current source: **GAP AS WRITTEN at lines 598–600**. Baseline: identical **GAP at lines 472–474**. In the hyperbolic-pair proof the positive tail chooses an original coordinate (i) with (|u_i|ge|u|/sqrt2), then the negative tail is said to use (w) but the cutoff justification still uses the same (|u_i|). A coordinate large for (u) need not be large for (w). Repair: independently choose (i_+) with (|u_{i_+}|ge|u|/sqrt2) and (i_-) with (|w_{i_-}|ge|w|/sqrt2). Since (|u|=|w|), all displayed constants are unchanged. This is a local proof-writing gap, not a counterexample.

Current ledger: 1–597 PASS; 598–600 GAP; 601–955 PASS after the repair. More finely: 1–46 PASS; 47–75 PASS; 76–164 PASS; 165–214 PASS; 215–252 PASS; 253–297 PASS; 298–396 PASS; 397–527 PASS; 528–562 PASS; 563–597 PASS; 598–600 GAP; 601–610 PASS after repair; 611–662 PASS; 663–766 PASS; 767–860 PASS after repair; 861–955 PASS. **FALSE: none. UNCHECKED manuscript lines: none.** Fresh checker execution/PDF rebuild and priority claims were not rerun and are UNCHECKED production/novelty items, not proof lines.

The B06 determinant calculation independently closes:
[
a=2t,quad alpha=(2pi e)^2,quad H=alpha I+a^2M^TM,
]
with weights (c_j=alpha e_j^TH^{-1}e_j), (d_i=a^2m_i^TH^{-1}m_i). The substitution contributes (det H^{-1/2}); the (d_i)-powers cancel against the scalar Fourier-power bound; (prod c_j^{-c_j/2}le e^{	heta/2}); and ((2pi e/sqrtalpha)^	heta=1). The fourth root yields exactly
[
|phi_Z(t)|ledet(I+t^2M^TM/(pi^2e^2))^{-1/8}.
]
No Jacobian, factor-two, trace, exponent, or rotated-independence defect was found.

After the explicit hyperbola repair, the written (s_9) theorem is PASS mathematically. A complete (s_8) candidate and at least two distinct full PASS review artifacts are now present in the repository (account03/B08 and account01/B03); I do not assign an owner-level release flag. (s_7) remains open. The companion B06 improvement proves a new shared-anchor dyadic-L2 receiver and identifies the remaining obstruction as aggregate many-seed currency, not single-fiber integration.

Model: GPT-5.6 Sol. Reasoning counters: UNKNOWN/not exposed.
