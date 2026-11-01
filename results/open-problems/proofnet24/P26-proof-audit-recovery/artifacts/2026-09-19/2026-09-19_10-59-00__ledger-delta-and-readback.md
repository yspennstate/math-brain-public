# P26 ledger delta and immutable readback — 2026-09-19 10:59 run

REPORT_PATH: `proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_10-59-00__run-report.md`
REPORT_CREATION_COMMIT: `06209d7c74fcf28437422732d2ff80b0fb47476f`
REPORT_BLOB: `47dfb4e91525059a6cf62e5458f9c41d06532880`

Exact-commit readback verified:

- required runtime/metric first line: GPT-5.6 Sol / reasoning UNVERIFIED; not verified GPT-6 maximum;
- fixed P26 metric: `51 -> 51`;
- supported unchanged count: `1 -> 2`;
- methods: `#3`, `#24`, `#25`;
- terminal marker: `End of complete P26 run report.`

## Audit state

- Target package: `R06-ROMERO-MAX2-ALLN`.
- Owner: `R06`.
- Mathematical status: `PROVED_CANDIDATE / SOURCE_PARTIAL_OPEN`.
- P26 audit: `P26-AUDIT-R06-ROMERO-MAX2-ALLN-65 = PASS_FULL_MATHEMATICAL_PROOF / CLAIM_SCOPED_UPPER_DIAGONAL / SOURCE_PARTIAL_OPEN / SATYANARAYANA_1992_DEPENDENCY_VERIFIED / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_EXACT_SPECIALIZATION_UNVERIFIED / PENDING_SECOND_DISTINCT_AUDIT`.
- Reconciliation: `P26-RECONCILE-R06-ROMERO-MAX2-ALLN-2OF2-65 = PENDING_SECOND_DISTINCT_AUDIT`.
- Directed request: `P26-REQUEST-R06-ROMERO-MAX2-ALLN-SECOND-AUDIT-65 = PENDING`.
- Second genuinely distinct non-R06/non-P26 full-proof audit: `MISSING` at this run's repository search.

The earlier finite `ROMERO-2025-SPLIT8` n=8 package remains separately at `1/2`; this R06 owner-side all-n strengthening is not a second independent auditor of that finite package.

## Exact scope and dependency

Audited theorem:

For every `n>=4`, if `M=binom(n,2)`, then `A_n=K_n-{st,su}` with terminals `s,t` is uniformly most split reliable in `T_{n,M-2}`; it strictly beats the other terminal-missing type `B_n=K_n-{st,uv}` for `0<p<1`.

Proof ingredients independently reconstructed in the report:

1. exact terminal-edge bridge `Rel(X+st)=Rel(X)+p SR_X`;
2. exact terminal-edge swap coupling `SR_{G-st+e}>=SR_G` in the dense application;
3. exhaustive two-type reduction after `st` is missing;
4. Satyanarayana--Schoppmann--Suffel (Networks 22 (1992), DOI 10.1002/net.3230220206), `r=2` independent-edge deletion all-terminal extremal theorem.

No essential finite core exists for this universal analytic theorem, so no redundant checker was manufactured.

## Shared-root merge intent

Fresh root blobs observed in the run:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`;
- `POSTED.md`: `d658f9ef00a98194a82b41713e83df1db0dee7d2`;
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`.

No shared-root rewrite was attempted because the connector exposes bounded renderings while the write primitive replaces the whole file. Conflict-safe future merge datum:

`P26 SUPPORT | metric 51 -> 51 | unchanged 1 -> 2 | R06-ROMERO-MAX2-ALLN | P26 audit PASS | second distinct audit MISSING | reconciliation PENDING_SECOND_DISTINCT_AUDIT | report 06209d7c74fcf28437422732d2ff80b0fb47476f / blob 47dfb4e91525059a6cf62e5458f9c41d06532880`.

`QUEUE.md` still has 60 listed source candidates but zero newly certified READY additions; no promotion is asserted. `POSTED.md` receives no new claim. Protected C31/Aldous--Fill audit accounting remains unchanged.

No peer files were edited. No scheduler changes were made.

END SIDECAR