# B17 fixed-multiplicity audit

Objective QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Baseline source: 7c0d6e60946b19423e6400a12d34b473cf0591e2 / blob 183ccd294763214e6a707e8d4749ff9a8cf7006d. Verdict: PASS except repairable local hyperbolic-tail issue at lines 472-475; lines 779-790 bibliographic metadata UNCHECKED. See BASELINE_VERDICT.md.

Current nine/400 source: eeb752c8943536541b34b42b8bf48e924f4d3d2f / blob 19fb119877426b640b2c0dae19ec2f78a399fe11. Verdict: PASS except the same repairable issue at lines 598-600; lines 944-955 bibliographic metadata UNCHECKED. The repair chooses the negative-tail maximizing coordinate independently and leaves constants unchanged.

FALSE: none found. Multiplicity seven remains open. New mathematics is in the matching improvement run directory.
