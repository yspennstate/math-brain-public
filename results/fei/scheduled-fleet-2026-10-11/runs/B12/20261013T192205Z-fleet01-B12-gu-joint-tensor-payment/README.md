# B12 A056 joint tensor payment

- `REPORT.md`: complete result, proof, diagnostics, limitations, and next step.
- `JOINT_TENSOR_PAYMENT.tex`: standalone mathematical proof.
- `check_joint_tensor_payment.py`: deterministic exact/numerical verifier.
- `check_joint_tensor_payment.out`: archived verifier output.
- `CLAIMS.json`, `PROGRESS.json`, `PACKET_DELTA.json`: evidence state.
- `SOURCE_PINS.md`: immutable dependencies and newer review evidence.
- `HANDOFF.md`: concise consumer handoff.

Run the checker with:

```bash
python3 check_joint_tensor_payment.py
```

The all-depth theorem is analytic. Direct tensor depths 1 through 4 are
diagnostics. No randomness is used.
