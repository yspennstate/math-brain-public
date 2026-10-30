# Support-package supplement — fleet02/B01 auto11

Pinned mathematical source: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`, blob `19fb119877426b640b2c0dae19ec2f78a399fe11`, SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`.

This supplement does not change the immutable mathematical audit verdict.

## Support files

- `README.md`, `MANIFEST.json`, `proof_map.csv`: **PASS** for source identity, scope and label mapping.
- `AUDIT_NEW.md`: **UNCHECKED AS VALIDATION EVIDENCE**. It is an authoring-agent self-audit and was assigned zero weight in the independent reconstruction.
- `checks_new.json`: **PASS AS A RECORD OF THE REPORTED FINITE RUN ONLY**. Its 96 exact interpolation seeds, 8 exact aggregate overlap cases and exact rational constants are consistent with `verify_new.py`. Floating spectral comparisons are diagnostics, not proof.
- `verify_new.py`: **GAP (reproducibility/source binding only; no mathematical theorem impact)**. Unlike the historical baseline `verify.py`, it does not read/hash `paper.tex` or compare it with the pinned SHA-256 before running. Therefore the finite suite can report PASS after the source is changed. Repair: add a pinned-source SHA-256 check for `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`, or explicitly version the checker as diagnostics detached from source identity.

Downstream impact: none on the analytic proof, because the independent audit reconstructs the theorem from the pinned source and does not infer mathematical validity from the finite suite. Release-package impact: do not describe `verify_new.py` alone as a source-pinned reproducibility certificate until the binding is repaired.
