Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. GPT-6 / maximum was requested in prompt text only; the exposed scheduler has no model selector or reasoning-effort selector.

# P26 run readback and ledger delta — Tang Question 4.11 periodic-tree claim

## Fixed metric

- before: `6`
- after: `7`
- unchanged count: `0 -> 0`
- newly counted package: `R09-TANG-Q411-PERIODIC`
- P26 audit: `P26-AUDIT-R09-TANG-Q411-PERIODIC-ENDTOEND-09 = PASS`
- distinct auditor: `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`
- parent status: `PARTIAL` (periodic-tree clause REFUTED; transitive-graph clause OPEN)
- prior-art/publication status: `UNVERIFIED / NOT_POSTED`

## Immutable P26 report

- path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_02-58-08__run-report.md`
- creation commit: `1494ca99137b3c794f7e7f1ea9a15fe67988c67f`
- readback blob: `16c54980f1fbfd73e9371a9870d9fa187aebab15`
- readback first line confirms `6 -> 7`, methods `1,4,27`, and GPT-5.6 Sol / UNVERIFIED.

## Independent exact checker

Checker:
- path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_02-58-08__tang_q411_periodic_audit_exact.py`
- creation commit: `84f74250729352787e7b67e846851ac6d6766286`
- readback blob: `c80857f69820a6bc3641024c7993efe2873149cf`

Output:
- path: `proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_02-58-08__tang_q411_periodic_audit_exact.out`
- creation commit: `06006699ff2f90d6239d41e819ccae5f24dd88ab`
- readback blob: `638a19f446b4d355438479fb76d27da700cf3354`
- terminal line: `P26-TANG-Q411-PERIODIC-EXACT-CHECK: PASS`

## Author and independent-auditor evidence

R09 author report:
- `runs/R09/20260916T173216Z_tang_q411_stem_counterexample.md`
- creation commit: `e500e7d8c85422855bf8fe195f5181797fe38aed`

R08 independent audit report:
- `runs/R08/20260916T1828Z_i0082_strictstable_firstvariation_c84d2e.md`
- creation commit: `4c6b85310aa6759e05ff46e68337158bfe519bd6`
- current blob read in this run: `0584556b64edb523d5541462a1f23fa6b409f85` is **NOT** claimed; correct current file blob from direct fetch is `0584556b64edb523d5548e83a9f9dea1d496298e`.
- explicit audit ID recovered: `R08-AUDIT-R09-TANG-Q411-PERIODIC-01 = PASS`.

## Root-ledger disposition

`RESULTS.md` is stale relative to multiple current native reports, while the exposed mutation action replaces the full file and the ordinary connector rendering is truncated. A partial whole-file reconstruction could erase unrelated concurrent state. Therefore this run records:

`ROOT_RESULTS_WRITE_DEFERRED_CONFLICT_SAFETY`

Exact merge delta:

```yaml
P26:
  target: outside claim-scoped full-proof audits
  metric_before: 6
  metric_after: 7
  unchanged_count: 0
  new_package: R09-TANG-Q411-PERIODIC
  mathematical_status: PARTIAL_PARENT_PERIODIC_REFUTED_TRANSITIVE_OPEN
  audit_state:
    p26: P26-AUDIT-R09-TANG-Q411-PERIODIC-ENDTOEND-09=PASS
    distinct_other: R08-AUDIT-R09-TANG-Q411-PERIODIC-01=PASS
  report: proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_02-58-08__run-report.md
  report_commit: 1494ca99137b3c794f7e7f1ea9a15fe67988c67f
```

`QUEUE.md`: no ownership mutation needed; Tang remains R09-owned and is not reserve inventory.

`POSTED.md`: no mutation; two audits do not by themselves create a public posting, and the source-matching `paper_tang_q411_periodic_tree_counterexample/` author package is still absent.

No peer proof/report was edited. No scheduler job was created, disabled, or modified. No email/Gmail, Drive, public posting, paid compute, workflow execution, credential/access change, or permission bypass was used.
