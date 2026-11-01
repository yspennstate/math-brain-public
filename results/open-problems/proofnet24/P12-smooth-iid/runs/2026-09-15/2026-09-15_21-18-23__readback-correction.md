# P12 readback correction — 2026-09-15 21:18:23

Canonical report:

`proofnet24/P12-smooth-iid/runs/2026-09-15/2026-09-15_21-18-23__run-report.md`

Creation commit:

`c5d7c072f7a8188be92fd914b8e09abab0aca88e`

Canonical report blob:

`1738a6b9a86819f4b48e2b19b20be8b99b0b8140`

The immutable report was read back completely at the creation commit. One notation-only serialization defect was found in Section 8, in the characteristic-function Taylor expansion used in the proof of `P12-COMPLEX-B4-ALLSUPPORT-COARSE-GAP-34`.

The readback text contains the malformed fragment

```text
1-
rac12E(t\cdot Z_{n,j})^2+r_{n,j}(t),
```

The intended formula is

\[
E e^{i t\cdot Z_{n,j}}
=
1-\frac12 E(t\cdot Z_{n,j})^2+r_{n,j}(t).
\]

The surrounding remainder estimate, covariance limit, characteristic-function product limit, theorem statement, hypotheses, audit verdict, ledger status, phase-retrieval implication, and next attack are unchanged. This note corrects only that serialization defect and does not overwrite or modify the immutable canonical report.