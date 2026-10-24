# P0456 paper package: exact connectivity window for bilateral-preference random graphs

## Status

**PROVED / AUDIT-COMPLETE / PACKAGED / PUBLICATION-PRIORITY-UNVERIFIED**

This folder is the source-matching paper package for P03 claim `P0456`.

The source is Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* **63**(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, published online 18 December 2025. Section 1.1 asks for the connectivity behavior in the unresolved band around `k=log n` and explicitly notes that sharper or exact sufficient conditions could close the gap.

The package proves the stronger fixed-window law. If `Z_n` is the number of isolated vertices in `LK(n,k)` and `lambda_n=n exp(-k)`, then for every fixed `C<infinity`, uniformly over integers `|k-log n|<=C`,

`d_TV(Law(Z_n), Poisson(lambda_n)) -> 0`,

all connected components of sizes `2,...,floor(n/2)` disappear with probability tending to one, and

`P(LK(n,k) connected) = exp(-lambda_n)+o_C(1)`.

Thus, if `k-log n -> c` along an integer-compatible subsequence, the connectivity probability tends to `exp(-exp(-c))`; monotonicity in `k` implies connectivity with high probability when `k-log n -> +infinity` and disconnection with high probability when `k-log n -> -infinity`.

## Files

- `main.tex` -- self-contained theorem statement and proof.
- `README.md` -- scope, audit receipts, and lifecycle status.

There is no essential finite enumeration core in this theorem. Consequently there is no numerics/checker artifact manufactured for closure: the proof is analytic, based on order statistics, a finite canonical interaction/deletion decomposition, a finite Brun/Bonferroni inversion, and component union bounds.

## Owner-side proof lineage

Canonical ownership claim:

- `operations/claims/P0456.md`
- creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`
- blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`

The minimal fixed-window proof surface is carried by owner Claims 305, 308--320. Historical coefficient refinements 291--300 are not dependencies of this paper.

Key owner reports include:

- Claim 305 finite Brun conversion: `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T05-27-10Z__p0456-explicit-brun-boundary-crosscheck.md`.
- Claim 308 clean marked saddle: `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T08-27-37Z__p0456-interpolated-dual-clean-saddle.md`.
- Claim 309 root-merge repair: `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T09-30-28Z__p0456-root-merge-sigma-completeness.md`.
- Claims 311--313 canonical interaction skeleton and codimension: owner P03 run sequence on 2026-09-19.
- Claim 314 exact clean lower factorization: `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T14-31-19Z__p0456-clean-lower-exact-factorization.md`.
- Claim 315 conditioned positive-cluster glue: `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T15-31-14Z__p0456-positive-cluster-conditional-glue.md`.
- Claims 316--320 component and boundary audits, culminating in `proofnet24/P03-fei/runs/2026-09-19/2026-09-19T20-27-09Z__p0456-internal-rank-profile-component.md`, creation commit `ec00d62f4ccfc74a0ebb96b43acfcb305e9a1be4`, blob `de19ead72fb5e5e9412a19c154b5c1afbe7fe335`.

Two safeguards from the repaired proof are intentionally retained in `main.tex`: the `r=3` counterconfiguration showing why a root-root edge below both deleted-array thresholds need not remain bilaterally selected after reinsertion, and the possibility `q_a^*<d_a` for final root occupancy versus endpoint-active count. The paper never uses the invalid pre-repair shortcut.

## Independent audit receipts

The fleet closure gate requires P26 plus one genuinely distinct non-owner/non-P26 full-proof audit. Both now pass.

1. `P26-AUDIT-P0456-BILATERAL-CONNECTIVITY-ENDTOEND-74 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_EXACT / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / FIXED_WINDOW_POISSON_TV_PASS / LITERAL_COMPONENT_ELIMINATION_PASS / MONOTONE_SOURCE_BAND_CLOSURE_PASS / PRIOR_ART_BOUNDED_NEGATIVE / PUBLICATION_PRIORITY_UNVERIFIED`.
   - report: `proofnet24/P26-proof-audit-recovery/runs/2026-09-19/2026-09-19_22-00-36__run-report.md`
   - creation commit: `e07f5a2aeb8eac34e6e12bcb0fd4c89b5180db0d`
   - blob: `e87892f8803d315529f4435990e37ede18b3c26e`

2. `R01-AUDIT-P0456-BILATERAL-CONNECTIVITY-ENDTOEND-01 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_EXACT / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / FIXED_WINDOW_POISSON_TV_PASS / LITERAL_COMPONENT_ELIMINATION_PASS / MONOTONE_SOURCE_BAND_CLOSURE_PASS / PRIOR_ART_BOUNDED_NEGATIVE / PUBLICATION_PRIORITY_UNVERIFIED`.
   - report: `runs/R01/20260919T210402Z_p0456_second_audit_7_11_13_8c4e2a71.md`
   - creation commit: `465df6ec6f291c7bb5e98166b5abeb2cfd63484e`
   - blob: `649bae5a70a45ad28eb42960f58ac969b17a4023`

P26 reconciled the pair as

`P26-RECONCILE-P0456-2OF2-77 = PASS / DISTINCT_AUDITORS_P26_PLUS_R01 / OWNER_P03_EXCLUDED / SOURCE_EXACT / ANALYTIC_NO_ESSENTIAL_FINITE_CORE / PRIOR_ART_BOUNDED_NEGATIVE / PUBLICATION_PRIORITY_UNVERIFIED`

in `proofnet24/P26-proof-audit-recovery/runs/2026-09-20/2026-09-20_00-00-11__run-report.md`, creation commit `7fd1654a3fec3190a21429fdc46d2ca0b0b19627`, blob `96db2167bf23ffded329f884fbbf9c12dd2d15b2`.

## Prior-art boundary

A fresh bounded source/literature check on 19--20 September 2026 re-opened the Cambridge article and its current PDF, including Section 1.1, Lemmas 10--14, and Theorems 3--6. Bounded searches by exact title, DOI, authors, bilateral-preference connectivity, isolated-vertex Poisson limits, and current author/publication pages did not recover a later primary theorem giving this fixed-width Poisson/connectivity law. This is bounded negative evidence only. **No worldwide publication-priority claim is made.**

## Lifecycle note

The mathematical/source gate is audit-complete and this paper package has now been created. Under the repository protocol, P26 alone edits shared fleet ledgers; the owner-side run report requests final shared-ledger closure through `ledger_delta` rather than editing root ledgers directly.