Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; the scheduler exposes no model selector or reasoning-effort selector.

# P04 readback receipt — 2026-09-16 14:45:12 +03:00

Canonical run components:

1. Complete immutable report
   - path: `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_14-45-12__run-report.md`
   - creation commit: `e67dddbdfb3c6cc4c5f13502cc61d07980fe59f2`
   - verified blob: `762ba8d76c4d8adfc1e90de920f343b6234a999c`
   - exact-commit readback: reached `**End of complete run report.**`

2. One-line canonical transport correction
   - path: `proofnet24/P04-kernel-conjectures/runs/2026-09-16/2026-09-16_14-45-12__canonical-correction.md`
   - creation commit: `e0575ff32dbddc936b98922b88ec252c11857943`
   - verified blob: `61345322024f76ad4df07e11e769e2e5b35aa72b`
   - exact-commit readback: reached `**End of canonical correction.**`
   - correction only restores `1/(2N) = 1/(4n)`; no theorem/status/audit/metric change.

3. Frozen outside-audit packet
   - path: `proofnet24/P04-kernel-conjectures/artifacts/2026-09-16_14-45-12__target1_outside_audit_packet.md`
   - creation commit: `9050e7e5e9ea30a9bf1e621fbb9ad728b5bcf40b`
   - verified blob: `3e65882814b91132731435176ee6cd9e7500d7f0`
   - exact-commit readback completed.

Tracked metric after verified archival:

`required outside-audit obligations unresolved = 1`.

This is the recovered baseline from `UNMEASURED`, not an audit decrement. `P04-T1-OUTSIDE-AUDIT-P26` is satisfied by `P26-AUDIT-P04-T1-ENDTOEND-17 = PASS`; `P04-T1-OUTSIDE-AUDIT-P03` remains open.

Status: `COMPLETE_READBACK_VERIFIED_WITH_CANONICAL_CORRECTION`.

**End of readback receipt.**