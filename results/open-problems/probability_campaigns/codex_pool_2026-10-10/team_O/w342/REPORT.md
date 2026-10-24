Prepared ten problem bundles with 41 typed nodes (16 lemmas, 5 theorems, 20 concepts) and 79 quoted edges. All thirteen result rows are saved in results.jsonl. w346 has kept 2 rows: S1.w342.001 (second-order coefficient sign criterion) and .002 (prior-source scope correction). The larger proofs and full bundles await review; no complete open problem is reported solved. Novelty is unverified. This is a proposal for brain enrichment: no live ingestion or recall-improvement measurement has occurred.

The main additions are the weighted theta-forest extension and the explicit phase-retrieval implicit-function argument. P0289 independently reconstructs the earlier candidate rather than claiming a new discovery. Every problem was checked against its earlier attempt and a bounded excerpt of its cached primary statement; later-ledger lookup is in later_status_scan.json. Literature status outside these cached sources remains unverified.

| Problem | Saved result | Run evidence |
|---|---|---|
| P0289 | Independent bounded-Cox remainder proof; cyclic workload-rise candidate | 715 configurations; 6,435 additions; 9 quadratures |
| C0035 | Equal pair laws miss triple phase by 16/15625 | 256 sublattice determinant checks |
| P0001 | Pairwise negative correlation for weighted theta blocks | 420 exact covariance formulas; 21 weighted cases |
| P0133 | Unimodular theta windings; explicit bouquet convention caveat | 11,664 trees; 9,072 theta cores; 4 comb witnesses |
| C0002 | Relative 1/log N correction to the bulk one-point Gaussian tail | 24 tails; scaled remainder maximum 9.696 |
| C0059 | Same quartic growth with opposite recurrence behavior | 12 generation checks; transient flow energy 7/6 |
| C0083 | Exact cycles and cubic susceptibility coefficient | 6 graphs; 19,825 edge-subset checks |
| C0128 | Sublinear adverse-cookie drift gives directional transience | 4,095 prefix checks; exact martingale mean zero |
| P0015 | Proof candidate for p_M<1 for all M>=2; p_2=p_3=0 | 7 exact Jacobians, M=2,...,8 |
| P0044 | Canonical invariant inclusion coupling on all tree networks | 54 wired trees; 48 joint-law symmetry checks |

Reproduce the mathematical checks with `python -X utf8 verify_p0289.py`, `python -X utf8 verify_structural.py`, `python -X utf8 verify_remaining.py`, and `python -X utf8 verify_torus_comb.py`. Receipts are the corresponding *_measurements.json files. These finite or numerical checks support the separate written proofs; they do not prove general asymptotic claims.

Before/after preparation: 0 matching new logical ids in the live store versus 41 in the prepared drafts; deployed store change is 0. `python -X utf8 validate_bundles.py` used the live parser read-only: 10/10 drafts accepted, 5/5 invalid controls rejected, 41 existing links resolved, and 158 exact endpoint quotations verified. `python -X utf8 verify_hooks.py` passed all three fire and three silent controls; no hook was activated.

Lean arithmetic was attempted with lean_check.py on lean/ross_margin.lean, named target ross_margin_bound and the reviewed source hash. It returned `SETUP_UNVERIFIED: Compute status is distressed or unknown`. No result is labeled Lean-checked; the rational margin passed exact Python checks.

Audit risks: P0015 needs the full implicit-function and rank-two witness proof checked for all M, beyond the seven finite Jacobians. P0133 needs Claude source-convention review: a comb-tree bouquet has four no-repeated-edge trail winding classes, whereas the cached primary text says precisely three paths. The theta statement is explicitly conditional. C0002 does not give level-set fluctuations; C0059 does not model the Boltzmann law; C0083 does not determine a critical-value coefficient.

Apply one kept bundle by running `python -X utf8 ~/brain_workers/w342/stage_reviewed.py --problem <ID> --verdict-file ~/brain_workers/w346/<verdict>.jsonl --apply`; it reconstructs the matching patches/NN_<id>_bundle.diff and requires w346 KEEP with proof_reviewed=true. Then the reviewer runs `python -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w342`. The three hook proposals are separately reviewable in patches/11_math_hooks.diff.

Audit and progress handoffs are local because this worker brief forbids external writes and mesh/chat sends. AUDIT_REQUEST_w346.md lists the proof checks; bundle_handoff.json maps every patch to its intended live path; progress_rows.jsonl is ready for the reviewer to post.

NEXT: w346 blind-check P0015 and P0289 first, claude-4a88bc43 reconcile the P0133 source convention, then land only fully kept bundles and measure live recall.
