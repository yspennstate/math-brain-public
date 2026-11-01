# P26 ledger delta and immutable readback — 2026-09-18 07:00:32 run

Model actual: GPT-5.6 Sol. Reasoning actual: UNVERIFIED. GPT-6/maximum requested only; no authenticated applied-runtime receipt.

## Exact run report

- path: `proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_07-00-32__run-report.md`
- creation commit: `c055c616b3c670b728df590b2ca938b6fee9a989`
- exact-readback blob: `bd71dbce741ee1e3cef44fd48d973ee20c7cd0b7`
- first-line readback: PASS; records P26 `30 -> 31`, unchanged `1 -> 0`, methods `2,11,22`, actual model GPT-5.6 Sol / UNVERIFIED.
- tail readback: PASS; reaches literal `End of complete P26 run report.`

## Fixed metric delta

- metric before: `30`
- metric after: `31`
- supported unchanged count before: `1`
- supported unchanged count after: `0`
- new counted outside package: D0033 / Bradley Question 5, phi-mixing Markov chain => rho-star-mixing.

## D0033 audit evidence

- canonical claim: `operations/claims/D0033.md`; owner R7-01; CLOSABLE OUTSIDE.
- frozen owner package: `research7_2026-09-17/R7-01/paper_bradley_q5_phi_to_rhostar/`.
- owner handoff: `research7_2026-09-17/R7-01/handoffs/2026-09-18T011800Z__D0033_sixrun_handoff.md`.
- P26 audit: `P26-AUDIT-R7-01-D0033-BRADLEY-Q5-ENDTOEND-37 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_SCOPE_PASS / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_SEARCH_RECORDED / PUBLICATION_PRIORITY_UNVERIFIED`.
- distinct R01 audit: `R01-AUDIT-R7-01-D0033-BRADLEY-Q5-01 = PASS_MATHEMATICAL_SOURCE_SCOPE`.
- R01 audit report: `runs/R01/20260918T0310Z_pending_admission_d0033_audit_7c2f91b4.md`.
- R01 audit creation commit: `878d30b5293e516bffd2142a3609ada7a81d610b`.
- R01 audit blob: `0a4249cf496a36423878f5ea85fa9a526dadaedb`.
- reconciliation: `P26-RECONCILE-R7-01-D0033-2OF2-37 = PASS`.
- independent authors counted: P26 + R01 only. Owner R7-01 self-checks do not count. No prior P26 D0033 full-proof audit was found.
- metric disposition: `COUNT_ONE_NEW_OUTSIDE_PACKAGE`.

## Source / proof scope

Primary source: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Question 5, printed p.119 / source PDF p.13.

Literal source asks whether a given Markov chain that is phi-mixing must be rho-star-mixing. Section 3.1 and Theorem 3.3 explicitly allow not-necessarily-stationary Markov chains; the owner proof covers that broader literal scope, and hence also the narrower stationary canonical metadata.

Audited theorem:

`rho_star(n) <= min(1, 4*sqrt(2*phi(n)))`.

Core analytic interfaces independently checked by P26:

1. common full-measure transition-row TV bound and row diameter `<=2 phi(n)`;
2. robustness under arbitrary earlier-prefix conditioning;
3. exact zero subjective correlation for nonadjacent alternating blocks via a Markov separator;
4. adjacent-block subjective correlation `<=2 sqrt(2 phi(n))`;
5. Peyre Theorem 3.3.1 + Section 3.4(a) minimal-prefix tensorization;
6. alternating-path operator norm `<=2 kappa(n)`;
7. finite-to-countable sigma-field passage;
8. source normalization and one-lag closure through Bradley Theorem 3.3(6).

No essential finite computational core is used. R7-01's four-block Fraction checker is an owner self-check only and was not counted as an audit.

## NEW-METHODS diagnosis

- B2 ATTACK THE NEGATION: Bradley's 2001 rho-mixing/not-rho-star Markov example shows ordinary rho is insufficient; the new route succeeds because phi controls the essential TV diameter of all transition rows and keeps that control after prefix conditioning.
- B11 DUALIZE: the interlacing becomes a weighted path correlation operator. Its norm is `<=2 kappa`; for uniform weights the exact norm is `2 kappa cos(pi/(m+1))`, so path accumulation explains the factor 2 and why local pairwise bounds alone cannot be naively reused globally.
- B22 READ THE FAILURES: Bradley 1997 lower-psi positive results, Bradley 2001 ordinary-rho counterexample, later reversible/special-class literature, and Peyre 2010 identify the missing mechanism as uniform control over arbitrarily many interlaced blocks. Bounded fresh search found no explicit full-source resolution; publication priority remains UNVERIFIED.

## Shared-root observations and safe merge delta

Fresh observed blobs immediately before report creation:

- `RESULTS.md`: `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`
- `POSTED.md`: `4cba5265702ede8ecf9c11938a4e70d55f52549c`
- `QUEUE.md`: `2bb9fd1ac6ae45440cbddf25943e1afec6754693`

Safe `RESULTS.md` merge input when a conflict-preserving complete-file update surface is available:

- P26 target/metric: outside packages with two genuinely independent OTHER-track full-proof audits complete.
- before/after: `30 -> 31`.
- supported unchanged count: `1 -> 0`.
- new package: D0033 / Bradley Question 5.
- mathematical status: `PROVED` at source scope; audit authors P26 + R01; prior-art search recorded; publication priority `UNVERIFIED`.
- owner activity: `RETIRED / HANDOFF` after six ordinary no-movement runs; do not reassign.
- exact P26 report path/commit/blob: as above.
- R07/T28 remains pending second distinct full-proof audit.

No `POSTED.md` public-posting promotion is asserted. No `QUEUE.md` ownership change is warranted. The queue still lists sixty source candidates but does not certify sixty fully source/status/history/ownership-checked genuinely unassigned READY candidates; stronger reserve requirement remains `NOT_CERTIFIED`.

The large shared-root files were not destructively reconstructed from bounded connector renderings. No scheduler, email, Drive, public post, paid compute, access or peer-file mutation was performed.

## Model / scheduler interface

The exposed automation control schema still has title/prompt, schedule/start offset, enabled state and timing mode, but no binding model-family selector, reasoning-effort selector, guaranteed-duration control or authenticated completed-run applied-routing receipt. Enforcing GPT-6/maximum requires backend/product support for those fields plus per-run attestation.

The old P26 `You cannot modify this task` event is historical/context-specific; current root RESULTS records that a later P26 prompt update succeeded from an authorized context. If a task is denied in one context, the valid route is the owning/authorized account/workspace, ownership/admin repair/transfer, or platform support for that same task, not cloning or permission bypass.

END SIDECAR