# Independent review of the September 23 update

## Scope and current status

Reviewed the benchmark aggregate package, `update_evidence/benchmarks/update_benchmarks.tex`, the T12 retrieval audit, the integrated `paper/sections/05_update.tex`, the pinned analyzer, runner, and dispatcher source, and the final analyzer report/patch/existing validation output in `paper/supplement/update_20260923/analyzer/`. Numeric-only masked T11 grade cells were inspected in temporary scratch storage; no task text, answer keys, answer text, or masking map was added to the deliverables.

## T11: arithmetic and inferential scope

**All reported arithmetic independently reproduces.** Using the published shuffle recipe and seed with the numeric-only masked cells gives:

| Arm | Primary judge | Second judge |
|---|---:|---:|
| R | 18 | 15 |
| M0 | 24 | 21 |
| M1 | 25 | 22 |
| B | 35 | 33 |

The judges agree on 32 of 40 cells. Five cells differ by one point and three by two; in every disagreement the primary grade is higher. The absolute differences sum to 11, giving mean absolute difference `11/40 = 0.275`. The B-minus-M0 contrasts are 11 and 12; M0-minus-R is six for both judges; M1-minus-M0 is one for both. These satisfy the stated six-point and three-point thresholds and fail the stated two-point threshold, respectively. The task win/loss/tie counts also agree with the aggregate JSON. This was arithmetic reconstruction, not regrading or another solver trial.

The draft correctly calls these net rubric points rather than task accuracy, and correctly retains one solver session per arm, ten tasks per session, and two judging passes. Both judges assessed the same outputs; they are not independent replications of the intervention. The source-selected scoring keys favor the fully supplied block by construction, while the recall arms cannot open returned memories. The supported inference is that explicit delivery improved scored adherence in this selected operational task bundle, not a general improvement in mathematical inference or natural agent memory use.

The draft appropriately retains the missing frozen map, missing adjudicated merge, and incompatible grading-time metadata. Matching the preregistration file to its hash verifies textual identity, not when grading occurred. Approximate counters should remain undifferentiated token reports: `311k - 223k = 88k` and `311/223 = 1.3946188...`; they are not a new full monetary cost comparison.

One minor provenance ambiguity was reported to the benchmark agent: `t11_aggregates.json` originally paired the latest snapshot `source_ref` (19:52 UTC) with a `source_commit_time_utc` of 19:07 UTC, meaning the earlier evidence-landing commit. This has been corrected to `evidence_landing_commit_time_utc` with a distinct evidence-landing commit identifier. The manuscript's chronology already distinguishes trial timing from commit timing.

## T12: preserve the actual evidence boundary

The audit correctly classifies T12 as retrieval and engineering validation. The source reports top-five hub presence changing from 0/24 to 24/24 on source-designated held-out prompts and from 5/10 to 10/10 on reused tasks. Arithmetic combinations, if desired, are 5/34 to 34/34 and 33/34 remaining lists unchanged; these are descriptive combinations, not 34 fresh held-out solver trials. No agent-level pinned-hub versus hourly-block trial is established.

The following qualifications materially affect interpretation and should remain in the integrated prose:

1. **The 20 silent controls were selected conditional on not triggering.** The initial draft's phrase “Twenty non-film controls reportedly trigger nothing” omits that selection and can be read as independent specificity evidence. Recommended wording: “Twenty other-topic controls selected to have no pin trigger reportedly retained their result lists.” Their invariance should not estimate the rate of accidental triggers on unselected other-topic prompts.
2. **Historical raw query outcomes are unavailable.** The 62-query total, its 24/10/20 strata, and the remaining eight firing-other queries are reconstructed from reported counts and the harness structure. Eight is an inferred subgroup count, not eight observed committed rows. The comparison script retains ranks of a limited number of node identifiers, not complete stdout, so “byte-identical” remains the source's report rather than an independently established endpoint.
3. **The held-out label has limited scope.** The sources do not establish that the prompts remained unseen during trigger development. The draft correctly uses “source-designated” and explicitly avoids an untouched-holdout claim.
4. **The regression's negative endpoint needs a definition.** “31 negative controls quiet” means neither canonical policy node appeared in the top eight. It does not mean the retrieval system returned no content. The round-6 regression row log is unavailable; the inspected 35-row log is dated August 17 and cannot validate September 23 counts.
5. **Topic labels are not semantic truth.** `765/1213 = 63.0668%`, `65/6787 = 0.9577%`, and `765/830 = 92.1687%` are consistent with the report. The last fraction is the film-label share among triggers, not independently adjudicated precision. Misfiled prompts prevent computing a semantic false-positive rate from these aggregates.

No historical retrieval tests were rerun. The difference between the detailed 23/24 remaining-list result and the unqualified landing-note wording is correctly retained.

## Diet-arm source mismatch and remaining scoring defects

Direct source inspection confirms the substantive interface mismatch. `ab30_run.py` removes an inherited `BRAIN_HEADLESS_DIET` value and sets it to `1` only for `ondiet`. The pinned `hook_dispatch.py` never reads that variable: `_headless_session` gates on the shared `HEADLESS_DIET_ON` switch file and a headless prompt/session marker. Both `on` and `ondiet` use the same home and headless prompt prefix. The committed dispatcher therefore cannot use the new runner's flag to distinguish these arms. A shared switch could suppress the hooks in both headless arms. This is a source-interface finding; it does not establish what an uncommitted local runtime did.

The current analyzer recognizes `ondiet` in run enumeration, token accounting, and grade-sheet production, but `score()` still constructs only on/off contrasts. It also retains `sorted({...}) | {"all"}`, which attempts a list/set union and raises a `TypeError` when the grouping loop is evaluated. Merely adding a third arm to enumeration therefore does not complete either the treatment implementation or its score analysis. The source independently establishes these defects; another live test is unnecessary.

The absence of committed run receipts, grade files, and aggregate results must remain an absence-of-verifiable-evidence statement. It does not establish zero local runs or zero completed local pairs. The 30 planned round-one pairs have a known denominator; a new `ondiet` code path does not supply a round-two enrollment denominator or completed outcome counts.

## Final analyzer report and repair review

The final report and exact patch have the correct scope. The grouping repair moves the set union inside `sorted()` without discarding current diet or alternate-directory support. The proposed runner supplies an explicit zero for `on` and one for `ondiet`; the proposed dispatcher checks that override before falling back to the existing shared-marker gate. Headless classification is still required. This fixes the described source interface while preserving the old marker behavior for unspecified or unrecognized values. It does not redesign the skip list, suppress startup documents, add diet score contrasts, or implement an unstated statistical protocol.

The existing validation record reports exit code zero with zero solver and hook processes. Its stdout distinguishes assertions that the repair passes from controls that reproduce other source limitations. I inspected that output and the patch; I did not rerun the controls. The report explicitly reserves native installed-code identity, environment propagation, runtime mark creation, actual delivery, and any benchmark effect for later evidence. It also keeps the repaired scorer's on/off-only contrasts, incomplete-pair handling, duplicate grades, contamination exclusions, retry policy, and round/provenance assumptions visible. No material overclaim was found in the report.

**One material wording correction was requested in the manuscript's existing AB30 discussion.** It said that token aggregates include “successful runs.” The pinned runner instead labels any nonempty result event `status="ok"` when no wall timeout occurs, without requiring `rc == 0` or `is_error == False`. Direct inspection confirms the analyzer report's mocked reproduction: an error result can enter the `ok` denominator and then be skipped as already done. Recommended manuscript wording is “records labeled `status=ok`,” with a note that this label does not itself establish successful completion. This is an existing implementation limitation, not a claim that a real AB30 record exhibited that condition.

## Integration disposition

**Integrated T11/T12 prose passes.** The reviewed `paper/sections/05_update.tex` now explicitly conditions the 20 control prompts on no trigger, defines the negative-regression endpoint as neither canonical policy node appearing in the top eight, and states that the round-six regression row log was not located. The other arithmetic and scope limitations above remain intact. No further material change is requested to that subsection.

**Analyzer report and proposed patch pass the source-scope review.** The remaining manuscript wording request is the `status=ok` qualification above; there is no further requested change to the analyzer proposal. No manuscript file was edited in this review. The review performed one independent calculation of T11's existing numeric grade cells and read existing evidence; it did not create a new solver or retrieval experiment or rerun the analyzer agent's controls.
