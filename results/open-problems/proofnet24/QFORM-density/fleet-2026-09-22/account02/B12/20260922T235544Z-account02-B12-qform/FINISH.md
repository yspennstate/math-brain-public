# FINISH — account02/B12 QFORM localized-core stability

Run: `20260922T235544Z-account02-B12-qform`  
Observed finish snapshot: `2026-09-23T00:08:51Z`  
Elapsed execution through this snapshot: `787.342 s` (reasoning + generation + connector/network execution + verification + overhead; **not pure thinking time**).  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Full target status: **OPEN / NOT PROVED / NOT DISPROVED**.

Proved in this run:

- `QFORM-LOCALIZED-CORE-SPECTRAL-FOOTPRINT-STABILITY-v1`: a physical three-coordinate gap `kappa` survives an arbitrary-rank dense tail `||T||op<=delta` and arbitrary signed spectral additions `L=sum tau_r v_r v_r^T` whenever `delta+||L[S,S]||op<kappa`; the actual final quadratic form has `||p||inf<=6sqrt(pi)/(kappa-delta-||L[S,S]||op)`.
- Applied account03/B12 `QFORM-LOCAL-FOOTPRINT-HYBRID-STABILITY-v1` to obtain the corresponding weighted D' packet bound with cross-footprint `Delta_V` and constant `C(h)/(kappa-Delta_V)` for `h<3/4`.
- Exact target-class family `spec={2,2,-2,tau,0,...}`: after any dense symmetric tail of norm `<=1/4`, all `|tau|<=n/12` obey `s3>=7/4` and `||p||inf<=12sqrt(pi)`; choosing `tau=+-n/12` gives an unbounded fourth eigenvalue.
- `QFORM-NOPIVOT-DENSE-TAIL-STABILITY-v1`: explicit dimension-free threshold drift for the owner’s N3 class under arbitrary dense tails. In particular no-`1/16` with `s3>=65/64` plus `||E||op<=1/64` becomes a no-`1/8` target matrix.

Canonical report commit: `3afc8473206ce82f5f6b19b9e88f8c9fa32ff058`.

First unpaid implication: from bare `s3(A)>=1`, extract a protected physical triple or weighted three-volume packet, or prove N3 directly; in N3 aggregate exterior-cube/overlap-two mass before reciprocal local curvature. No small-quadratic-random-perturbation or post-rotation-independence shortcut was used.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: maximum actually supported. Configured reasoning effort: `UNKNOWN`. Provider reasoning tokens/time: `null` / not exposed.
