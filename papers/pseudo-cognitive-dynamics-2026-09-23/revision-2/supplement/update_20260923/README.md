# Revision 2 evidence and proposal supplement

This directory accompanies **Mathematics of Pseudo-Cognitive Dynamics**, revision 2, dated 23 September 2026. It adds separately identified evidence and software proposals to the preserved historical supplement. The original inventory remains **45 contrasts or strata**. The new model evidence is **one four-arm T11 study**; T12 is a separate retrieval diagnostic. Source-function and mocked controls are not new model trials.

## Source references

The broad source is pinned to [9c754d786b3a0ea4943da0585d1490c13cd9ef99](https://github.com/<private-repo>/tree/9c754d786b3a0ea4943da0585d1490c13cd9ef99), committed at 19:52:16 UTC on September 23. The research source is pinned to [24597f0dcc3cc32d81fd8f22b13903f636460396](https://github.com/yspennstate/math-open-problems/tree/24597f0dcc3cc32d81fd8f22b13903f636460396), committed at 20:04:37 UTC. Historical Math Brain/catalogue and usage sources retain the versions listed in [the parent supplement README](../README.md). Private source URLs require appropriate access. A later commit does not imply a later experiment event.

## File index

| Directory | Included material | Evidence class |
|---|---|---|
| `benchmarks/` | T11 arm aggregates, T12 aggregate/source qualifications, AB30 status and independent reviews | Recounted grades where available; source-reported retrieval counts; missing-outcome inventory |
| `analyzer/` | Three byte-exact sources and proposed copies, unified patch, manifest, portable reproducer, stdout and validation | Synthetic and mocked software controls; no live mutation or solver run |
| `delivery/` | Curated recall/delivery findings, bibliography and isolated source-function result | Source mechanism and emission boundary |
| `theory/` | Warning-budget propositions and independent review | Analytic deductions under explicit assumptions |
| `research/` | Source locators, review and proof-scope manifest | Focused proof-interface and short-argument review, with remaining manuscript claims identified |

The revision-wide [changelog](../../REVISION_2_CHANGELOG.md) explains the integration disposition. Existing catalogue and usage files remain in the parent supplement; this update does not silently replace their historical definitions.

## T11: four arms, ten shared tasks, two judges

Each arm has one Opus 5.5 solver session answering all ten operational tasks. Two masked grading passes assess the same outputs. The endpoint adds one per credited standing-order key and subtracts one per listed violation; there are 35 available key points. The table therefore gives net rubric scores, not correct-task counts. [Pinned T11 result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md), [aggregate CSV](benchmarks/t11_arm_aggregates.csv).

| Arm | Context | Solver sessions | Primary | Second judge | Approximate reported token counter |
|---|---|---:|---:|---:|---:|
| R | Two film READMEs | 1 | 18 | 15 | 197,000 |
| M0 | READMEs plus mechanical top-five recall | 1 | 24 | 21 | 223,000 |
| M1 | READMEs plus fuller recall descriptions | 1 | 25 | 22 | 217,000 |
| B | READMEs plus hourly film prompt block | 1 | 35 | 33 | 311,000 |

All eight totals reproduce from published numeric cells and the deterministic shuffle recipe. The original frozen masking map is unavailable, so the recount is an arithmetic reconstruction rather than an independent regrading. Judges agree on 32 of 40 task-arm cells, with mean absolute difference 0.275. B exceeds M0 by 11/12 points; M0 exceeds R by six for both judges; M1 adds one over M0 for both judges. The last difference misses its preregistered two-point threshold. [Aggregate record](benchmarks/t11_aggregates.json), [independent review](theory/update_review.md).

All scoring keys were selected from the block, while recall arms could not open returned memories. One solver per arm, shared task sources, unavailable frozen masking map, conflicting grading timestamps and no located adjudicated merge limit inference. The study supports using explicitly supplied local instructions in this selected operational bundle. It does not establish general mathematical-reasoning gains or independent replications for each key.

The reported counters imply B uses approximately 88,000 more tokens than M0, about 1.395 times M0. Uncached input, cache reads, cache creation, output and monetary costs are unavailable. Missing categories remain blank in the CSV. These counters must not be converted into a full cost comparison or pooled with differently defined historical records.

## T12: retrieval success is not agent-use success

The source reports top-five hub presence changing from 0/24 to 24/24 on source-designated held-out film prompts, and from 5/10 to 10/10 on reused T11 tasks. Twenty silent other-topic controls were selected conditional on no pin trigger. The stated 62 queries comprise those 54 and up to eight additional firing-other probes; eight is inferred from the count and harness, and no subgroup outcomes are published. [Pinned result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md), [aggregate definitions](benchmarks/t12_aggregates.json).

The detailed report says the remaining list is unchanged on 23/24 held-out prompts and all ten T11 tasks. Raw comparison rows and the held-out file are uncommitted; untouched holdout status is not established. The 8,000-prompt trigger audit uses proxy topic labels, so its 765/830 film-label share among triggers is not adjudicated semantic precision. The result explicitly says the agent-level pinned-hub versus block comparison has not yet run. No solver outcome or cost saving is inferred. [Detailed T12 audit](benchmarks/t12_findings.md).

## Current AB30 source proposal and exact reproduction

From the paper/source-package root, run:

```bash
python3 supplement/update_20260923/analyzer/reproduce_update_audit.py
```

From this directory, the equivalent command is:

```bash
python3 analyzer/reproduce_update_audit.py
```

The reproducer resolves its assets relative to itself and can be invoked by absolute path from another working directory. The recorded external-directory execution returned zero. `REPRODUCED` lines confirm limitations in the original code, while assertion checks verify proposed behavior. [Validation](analyzer/validation.json), [stdout](analyzer/regression_output.txt).

The analyzer blob `5e49709186b23a8253f390233df0a0c44120ffc1` retains the list/set grouping crash. Its new diet-arm and alternate-directory code makes the earlier whole-file corrected copy unsafe to apply as a replacement. **The current rebased patch supersedes that copy for integration**, while the historical `../ab30_repair/` remains available for its original reproduction. Use [ab30_source_repairs.patch](analyzer/ab30_source_repairs.patch), [source manifest](analyzer/source_manifest.json) and [integration audit](analyzer/README.md).

The patch repairs grouping and proposes an explicit per-session diet override because the committed runner's environment flag is ignored by the committed dispatcher. The controls check all 12 arm/marker/inherited-value combinations and use synthetic state and mocked dispatch selection. They execute zero model solvers and zero real hook processes. Disposable-tree patch application yields the proposed bytes. They do not verify native runtime mark creation, environment delivery, installed hook identity, receiver context or allowlist re-signing.

The audit also reproduces limitations that the patch deliberately leaves for an explicit experimental policy: on/off-only scoring despite diet enumeration; missing and duplicate grades; mixed-round pairing; contamination reports not consumed; incomplete cost fields; mismatched arm/pair populations; malformed streams labeled clean; rounded-zero probabilities; and an error result labeled `status=ok`. Do not paraphrase the latter predicate as successful completion. The runner's retry behavior and the full attempt ledger need separate native handling.

The updated repository contains no committed AB30 run receipts, graded outcomes or final cost summaries. All 30 planned round-one pairs lack committed outcome evidence; actual local completion is unknown. The added diet arm has no recovered round-two enrollment denominator or outcomes. Source support and fabricated fixtures do not change that status. [AB30 status](benchmarks/ab30_status_aggregates.json).

## Architecture, theory and research additions

Normal-memory pins add explicit lexical/policy seeds before graph and semantic expansion, consume the ordinary eight-row allowance and need query-level collateral-effect measurement. The precedence repair operates after coverage boosts on the default ranking path; alternate blend/status settings matter. Description length, dispatcher characters and owner-context UTF-8 bytes are separate budgets. A receipt labeled stdout emission does not establish receiver delivery or subsequent action. [Delivery review](delivery/findings.md).

The theory derives the incremental value of a warning accounting for overlap with selected alerts, then an optimal count under fixed response behavior, equal card lengths and conditional independence. A concrete example shows one card helping while another hurts through false rejection. These elementary calculations are not empirical fits and do not show that the removed diet hooks are unnecessary. [Theory review](theory/review.md).

The QFORM update makes the already-present fixed-dimension bound `2 sqrt(6 pi n) / s3(sym(B))` explicit: it is uniform across the specified dimension and affine terms but leaves dimension-independent indefinite QFORM open. Two new short independent-hub arguments have stated independence and density hypotheses. A planar density construction shows why an L2 bound alone cannot imply a bounded density after restriction to a parabola; it does not refute product-law QFORM. The FEI update distinguishes unweighted-threshold and read-k claims from full FEI/general weighted thresholds, and a scalar Lean helper from the complete theorem. Some later memory claims are absent from their pinned proof source and remain unverified. [Proof-scope manifest](research/proof_scope_manifest.json).

## Integration and continuing unknowns

The package remains an additive proposal. Live integration requires native resource leases and assertion, comparison with current files, preservation of intervening changes, the dispatcher's applicable equivalence gate, and a documented experiment amendment. Neither native acknowledgment nor adoption has been observed. These files do not certify a completed push.

The 45 old contrasts, 1,391 catalogue rows/1,168 IDs/223 additional occurrences, 29 reviewed cases, 87 ProofNet directories and original usage aggregates retain their historical scope. They are not counts of independently solved conjectures. All-time construction-only cross-provider cost remains unidentified; neither incomplete T11 counters nor unavailable AB30 costs fill the gap. No fresh Lean kernel run or reviewer-run model-performance cohort was produced. Held-out keys and private model transcripts are excluded.
