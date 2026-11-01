# Updated benchmark evidence: T11, T12 and AB30

**Pinned repository:** `<private-repo>`, commit `9c754d786b3a0ea4943da0585d1490c13cd9ef99`, committed **2026-09-23 19:52:16 UTC**. Compared with the paper's earlier `bcff9346b68959f4cf330fdf9ca0e64a21c77d3e` snapshot, this is an 11-commit update. All quantitative additions below retain their native evidence class. No held-out answer keys, private prompt text, solver answers, grader notes, original masking map, or per-item grade rows are exported in this package.

## Main finding

The update adds a four-arm, two-judge operational instruction-following study (T11), and a retrieval follow-up (T12). **It still supplies no completed AB30 mathematical scores or cost receipts.** The strongest new measured finding is that supplying the hourly film-instruction block yields 35 and 33 net rubric points, versus 24 and 21 with mechanical recall. This supports useful application of supplied project-specific instructions on those tasks. It does not add evidence of a general mathematical reasoning improvement. The earlier 45 reported contrasts should remain 45; T11 is one additional four-arm study, while T12 remains retrieval/engineering evidence. [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md) [T12 retrieval groundwork and remaining agent-level test](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md) [AB30 campaign directory at the update snapshot](https://github.com/<private-repo>/tree/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens)

## 1. T11: design, endpoints and independently recomputed totals

The task bundle comprises ten film-pipeline tasks and 35 available standing-order key points. One Opus 5.5 agent per arm answers all ten tasks, at most 120 words per answer. The model/version label is source-reported; no raw process identity or usage event was committed for independent verification. The scoring rule is one point per credited key and minus one per listed violation. Consequently a score such as 18/35 is a **net rubric score**, not 18 correct tasks and not necessarily 18 satisfied keys. All scoring keys were selected from the block itself and reportedly absent from the two baseline film READMEs. [T11 preregistration: film instructions and context delivery](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/PREREG.md) [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md)

| Arm | Supplied context | Primary judge, net points | Independent judge, net points | Source-rounded token counter |
|---|---|---:|---:|---:|
| R | Two film READMEs | 18 | 15 | approximately 197,000 |
| M0 | READMEs plus one mechanical top-five recall per task | 24 | 21 | approximately 223,000 |
| M1 | READMEs plus recall after the full-description snippet change | 25 | 22 | approximately 217,000 |
| B | READMEs plus the hourly film prompt block | 35 | 33 | approximately 311,000 |

Every one of the eight arm totals was independently reproduced from the committed numerical grade cells. The published masking procedure initializes Python `random.Random(20260923)`, starts from `[M0, B, R, M1]`, shuffles a fresh arm list for each sorted task, and maps A–D to the shuffled arms. Applying that declared algorithm to the ten observed task IDs reproduces the reported totals. The original frozen map is not committed, so this is a reconstruction from the published algorithm, rather than verification against the original map. Answers and keys are unavailable for independent regrading. [T11 primary masked grade cells](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/grades.json) [T11 independent masked grade cells](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/grades_judge2.json) [T11 deterministic masking procedure](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/make_blind.py)

The three prespecified score contrasts are:

| Prediction | Threshold | Primary difference | Independent difference | Threshold met? |
|---|---:|---:|---:|---|
| P1: block minus ordinary recall | at least 6 points | +11 | +12 | yes, both |
| P2: ordinary recall minus READMEs | at least 3 points | +6 | +6 | yes, both |
| P4: longer snippets minus ordinary recall | at least 2 points | +1 | +1 | no, both |

The source also reports that B committed no listed violations and no more than M0, satisfying P3. The exported numerical cells are net scores, so exact per-key credit and penalty counts cannot be independently separated. All contrast rows are facets of this one study; they are not new independent experiments. [T11 preregistration: film instructions and context delivery](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/PREREG.md) [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md)

### Masking and adjudication

The source describes both grading passes as blind to arm. The first report says the first grades were frozen before the map was opened; the second judge reportedly saw only the blind sheet. **No final adjudicated merge is present.** Keep the two judges separate; do not silently promote their average or the higher set to final adjudicated truth. The two graders agree exactly on **32/40 = 80%** of task-arm cells. Mean absolute cell difference is **0.275** points; five cells differ by one and three by two. The second judge is lower on all eight disagreements. These computations reproduce the source's rounded 0.28 statement. [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md) [T11 primary masked grade cells](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/grades.json) [T11 independent masked grade cells](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/grades_judge2.json)

A genuine metadata discrepancy remains: RESULT.md says the first grades were frozen at **19:41:23**, whereas grades.json says `graded_at: 2026-09-23 19:5x, blind ...`. Neither claim is independently time-certified. The preregistration text's SHA-256 **does** match the published stamp, `2e940a1a99658c6be291ed84587dd55a4e8f19b9f63d7b74a6d72e0df3a9c5e2`; this confirms content integrity relative to the stamp, not the claimed chronology or masking. The discrepancy should be reconciled by the study owner rather than silently repaired editorially. [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md) [T11 primary masked grade cells](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/grades.json) [T11 preregistration hashes and local time stamp](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/PREREG_STAMP.txt)

### Interpretation

There are four independent solver sessions, one per arm, not 40 independent solver processes or 35 independent replications. Task keys share an instruction source. M0 and M1 were not allowed to open the memory files suggested by recall; their performance is that of the supplied snippet policy, while an ordinary working agent may read the underlying files. The block contains all evaluated instructions by design and is substantially larger than the recall material. T11 therefore measures whether agents apply reachable instructions and how the tested context-selection policies expose them. It does not isolate the causal effect of durable memory, prove that all block content was useful, or determine a minimum context needed for the same score. [T11 preregistration: film instructions and context delivery](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/PREREG.md) [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md)

The snippet extension changes the displayed information and adds one point under each judge, below its prediction. This is a descriptive small difference in a single session per arm; the report's “not significant” wording should not be treated as a valid statistical conclusion without a suitable replication and variance model. The larger block difference is still meaningful descriptive evidence on this task bundle.

## 2. T11 tokens and full cost

The source gives approximate counters 197k, 223k, 217k and 311k. It does **not** provide a complete token meter broken into uncached input, cache reads, cache creation, output, or separate reasoning, nor a monetary receipt. Those fields are null in the exported aggregate files, not zero. Relative to M0, the block's counter is about **88,000 larger**, or **311/223 = 1.3946** times as large. Calling this “about 90k more tokens” is faithful to the rounded source. It is not a full inference cost ratio or a billing ratio, and it must not be added to the earlier category-complete receipt as if both use the same unit. [T11 four-arm instruction-following result](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t11/RESULT.md)

No new exact all-attempt or eligible-pair financial total is available. The older September 22 two-Opus receipt remains the located complete per-arm category accounting in the prior audit. T11 and T12 do not update construction-token attribution.

## 3. T12: retrieval groundwork, not a solver follow-up

T12 pins a hub of standing film instructions and separately repairs policy routes being displaced by multiplicative score boosts. The source explicitly says the **agent-level pinned-hub versus hourly-block test had not yet run**. It must not be counted as a new proof trial, a new instruction-compliance run, or demonstrated cost savings. [T12 retrieval groundwork and remaining agent-level test](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md)

| Reported endpoint | Comparator | New configuration | Interpretation |
|---|---:|---:|---|
| Hub top-five presence on source-designated held-out film prompts | 0/24 | 24/24 | retrieval availability |
| Hub top-five presence on reused T11 tasks | 5/10 | 10/10 | regression/reuse result |
| Remaining list unchanged, held-out film prompts | — | 23/24 | one returned-list remainder changed |
| Remaining list unchanged, T11 | — | 10/10 | selected fixture behavior |
| Non-film prompts selected conditional on no trigger | — | 20/20 byte-identical | absence of side effect when untriggered |
| Policy routes at rank one | three prior failures reported | 10/10 positives | routing regression |
| Policy negative controls quiet | — | 31/31 | target absent from top eight |
| GitHub-cost pin, positive/negative controls | — | 6/6 fires; 0/5 fires | trigger controls |

The stated total is 62 queries. The named strata account for 54: 24 + 10 + 20. The harness also appends up to eight firing prompts filed outside the film topic; eight extra probes are therefore inferred from the total and harness. No subgroup outcome summary is available for them. The non-firing sample is chosen conditional on the pin not firing, so its 0/20 trigger count is not an independently sampled false-positive estimate. [T12 retrieval groundwork and remaining agent-level test](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md) [T12 retrieval comparison harness](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/compare_arms.py)

The detailed RESULT says the remaining retrieved list is unchanged on **23/24**, while LANDED uses unqualified unchanged-list wording. Retain the precise 23/24 endpoint and note the discrepancy. Raw compare_arms.json rows and held-out prompt text are deliberately outside the repository. We recomputed arithmetic on source aggregates, but cannot independently reconstruct the reported per-query outcomes. The “held-out” set is loaded from the T11 scratch material and is not established as untouched after pin development. Both the pin and policy-top change are present in the measured staged configuration. [T12 retrieval groundwork and remaining agent-level test](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md) [T12 retrieval comparison harness](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/compare_arms.py) [Round-six implementation and measurement ledger](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/LANDED.md)

### Trigger audit over historical prompt labels

The reported counts are 765 fires among 1,213 film-labeled prompts and 65 among 6,787 other-labeled prompts:

| Computation | Exact fraction | Percent |
|---|---:|---:|
| Fire among film-labeled prompts | 765/1,213 | 63.0668% |
| Fire among other-labeled prompts | 65/6,787 | 0.9577% |
| Overall fire | 830/8,000 | 10.3750% |
| Film-labeled share of fires | 765/830 | 92.1687% |

These are label-based rates. The source claims nearly all of the 65 other-labeled fires are misfiled film prompts, but no adjudicated semantic labels are published. Therefore 92.17% is not established precision, and 0.958% is not established semantic false-positive rate. The GitHub-cost pin's separate 4.3% firing statement lacks an exact numerator and denominator and remains a rounded source report. [T12 retrieval groundwork and remaining agent-level test](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/tests/t12/RESULT.md)

Additional details and source-pinned configuration checks are in `t12_findings.md` and `t12_aggregates.json`. An available August 17 regression log cannot validate the new September 23 run. No current raw probe log was substituted with that stale file.

## 4. AB30: completed/missing pairs, rounds and new diet code

At the pinned head the AB30 directory contains DEVIATION.md, PREREG.md, two preregistration stamps, README.md, bank/, and tools/. There is no committed runs/ tree, result receipt, masked grade, adjudicated grade, TOKENS.json, RESULT.json or AUDIT.json. README's running-results section remains blank. Its references to local progress or first items are not sufficient to infer completed pairs. [AB30 campaign directory at the update snapshot](https://github.com/<private-repo>/tree/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens) [AB30 campaign status](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/README.md)

| Round / arm | Planned item runs | Committed result rows located | Planned rows without committed receipts | Actual local completions |
|---|---:|---:|---:|---|
| Round 1 / on | 30 | 0 | 30 | unknown |
| Round 1 / off | 30 | 0 | 30 | unknown |
| Round 2 / on, off, ondiet code paths | denominator not established | 0 for each path | unknown | unknown |

Thus **all 30 planned round-one paired outcomes lack committed evidence**; saying “zero pairs completed” would be false precision. Round two has no located separate protocol or denominator. The new scripts accept an ondiet arm and an alternate runs directory, but those capabilities are not evidence that a particular set of trials ran. The expected original strata remain 20 proof audits and ten house-mathematics questions; a bank or runner is not a result. [AB30 preregistered design](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md) [AB30 runner with round-two diet support](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py) [AB30 analyzer with diet accounting paths](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py)

The original intervention is the bundled home brain, with standing files, memory index and hooks, versus safe mode outside the home directory. Both arms retain shell and local-read tools and may read local notes; the control is therefore not demonstrably filesystem-isolated. The required contamination audit excludes both members of a pair when forbidden material is opened. No executed audit or eligible scored pair is available in the update. Existing deviations concerning the stopped web pilot, priority, hook changes and session-level modelUsage remain operative. Their claims that tokens or accuracy were unaffected by environmental changes are assertions requiring receipts, not assumptions this review adopts. [AB30 preregistered design](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md) [AB30 deviation record](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/DEVIATION.md)

### New integration finding: the diet label does not identify a distinct treatment

The runner's `child_env(arm)` clears inherited `BRAIN_HEADLESS_DIET` and sets it to 1 for ondiet. The pinned dispatcher does not read that environment variable; it checks only the shared `HEADLESS_DIET_ON` file before recognizing a headless session. Since on and ondiet otherwise share the same home cwd and headless prompt, the committed code does not establish arm separation: with the shared switch absent neither takes the diet; with it present both can. Two independent reviewers confirmed this source mismatch. This is an implementation finding, not an assertion that any actual trial had one particular switch state. The analyzer review provides functional controls and a proposed local repair. No remote file or live switch was changed. [AB30 runner with round-two diet support](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py) [Hook dispatcher at the update snapshot](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/hook_dispatch.py)

The grouping defect identified in the prior paper is also still present in the fresh analyzer: it unions a sorted list with a set. New token-reading support includes ondiet, but score() still compares only on/off. Any future diet accuracy analysis needs an explicit comparator and eligibility policy; code that prints diet token summaries is not a preregistered three-arm score analysis. [AB30 analyzer with diet accounting paths](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py)

### Full cost status

There is no new AB30 full cost total in the repository. Uncached input, cache-read input, cache-creation input, output, separate reasoning where actually reported, and list-valued cost remain unknown per arm. The calibration prompt must remain separate from the 30-item study. All-attempt cost must include pilots, failures, timeouts and retries; an eligible-pair analysis may report a separate subtotal after contamination exclusions. The current successful-run summary alone cannot establish all-attempt cost. The analyzer has the right direction of using cumulative modelUsage over final-call usage, but missing categories must not become measured zero.

## 5. Dates and publication scope

These are newly available artifacts relative to the earlier snapshot, not necessarily tests performed after 19:00 UTC. The update ledger gives T11's event as 19:55 at UTC+03:00 (16:55 UTC) and the recall-pin event as 21:39 at UTC+03:00 (18:39 UTC). The commit carrying them is `864155ed253428525f645eb855ca8d91d893a7ec`, 19:07:05 UTC. AB30 runner diet support arrives in `c8e021183253fc65201afbe4f891b91633c54f9c` at 19:31:36 UTC; analyzer support arrives in the pinned 19:52:16 UTC head. The manifest records exact commits, times and blob identities. [Round-six implementation and measurement ledger](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_round6/LANDED.md)

## 6. Deliverables and integration

- `update_benchmarks.tex`: ready-to-input manuscript addition with the four-arm table.
- `update_benchmarks_refs.bib`: new exact commit-pinned citations.
- `t11_aggregates.json` and `t11_arm_aggregates.csv`: aggregate results and qualified counters.
- `t12_aggregates.json` and `t12_findings.md`: retrieval audit and arithmetic.
- `ab30_status_aggregates.json/.csv`: missing committed receipts, unknown real completions, and round distinctions.
- `source_manifest.json`: sanitized provenance, directory inventory and commit chronology.
- `analyzer_independent_review.md/.json`: independent current-source controls and inspection of the proposed repair.

No manuscript or remote repository file was edited. The aggregate package contains no held-out keys or per-item grades. The raw numeric grade cells used for an independent arithmetic cross-check were supplied only as a temporary scratch reviewer input, outside this package.
