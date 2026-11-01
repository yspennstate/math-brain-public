# FEI 100-agent plan: independent execution-design audit

## Verdict

The assignment arithmetic is correct, and the plan contains a serious, source-aware research portfolio. The initial version is a research menu rather than a fully specified execution protocol. It needs explicit packet interfaces, rolling review capacity, versioned claim propagation, bounded computation, and a deterministic mapping from the hypothetical 100 roles to the actual twenty scheduled workers.

This audit does not evaluate every mathematical theorem in the source manuscripts. It does not change schedules or final shared files. The schedule recurrence/count/deadline was already independently checked and was not rerun here.

## Audited source snapshots

- FEI_100_agent_research_plan.tex: SHA-256 e7cc3f21e59cf4c718e481c21caac18c042b0f716f0e15162a86e09d2e7fd692
- AGENT_ASSIGNMENTS.json: SHA-256 940483bc46fe5cdad8ec05d69983898fa9f4c873b8bc8358f3e20d37c6928ccf
- Both were read from /workspace/scratch/cd992ff12e5c/deliverables/fei-2026-10-11/.

Checks on this version:
- Exactly 100 JSON assignments.
- IDs are exactly A001 through A100, without gaps or duplicates.
- Exactly five assignments belong to each B01 through B20.
- The mapping B = floor((A-1)/5)+1 holds for every row.
- All 100 topic strings and assignment strings are distinct.
- Exactly 100 matching A-packet labels appear in the TeX.
- The portfolio table adds correctly: 30 + 25 + 25 + 20 = 100.
- The stated 24,000 worker-hour ceiling is explicitly hypothetical and arithmetically correct.

These checks establish bookkeeping consistency. They do not prove that all packet outputs are operationally distinct.

## Priority findings

| ID | Severity | Finding | Required improvement |
|---|---|---|---|
| E1 | High | The JSON contains only agent_id, stream, stream_name, topic, assignment. It does not specify dependencies, precise deliverables, acceptance tests, reviewers, next consumers, or bounded first steps. | Add an execution contract for every packet, with advisory upstream work separated from proof dependencies. |
| E2 | High | Several packets can independently attack the same unnamed global entropy debt. Distinct wording does not prevent duplicated proofs or inconsistent definitions. | Give shared interfaces one owner and assign downstream packets different named outputs. |
| E3 | High | Day 9 is the first explicit complete reconstruction checkpoint. Waiting until then risks an audit queue much larger than two squads can clear. | Begin rolling review on Day 1. Reserve Day 9 for integrated rechecks, not first review. |
| E4 | High | The plan says to propagate dependencies but has no versioned claim/attempt identity or invalidation rule. Renaming a failed potential can reset apparent progress. | Track exact statement versions, gap IDs, dependency versions, attempted methods, and supersession/refutation events. |
| E5 | High | B15/B17 describe exact certification, but the plan does not define a resource-gated search pipeline. A large fleet can duplicate expensive searches or exhaust time on uninformative precision. | Specify pilot, discovery, exact verification, independent reproduction, and finite-to-infinite stages with separate stopping conditions. |
| E6 | Medium | The actual twenty-worker execution policy does not say which of a stream's five packets to run next or how to resume it. 'Request available local assistance' can be misread as worker spawning. | Choose one ready packet per natural invocation, persist its identity, and request help from existing streams through handoffs. |
| E7 | Medium | Baseline and permanent research assignments are mixed. Several tasks can endlessly reprove standard identities or restate the gap map. | Mark baseline tasks as finite, retire their accepted artifact, and activate a new downstream obligation. |
| E8 | Medium | Pivot language is partly qualitative, while the configured prompts already use a three-run stagnation rule. | Make the threshold explicit and count substantive mathematical attempts on the same gap across renamed variants. |
| E9 | Medium | A universal good-coordinate or stopping-tree theorem appears under 'Major partial outcomes' even though it completes a route to full FEI. | Move that item to primary-completion criteria. |
| E10 | Medium | The initial obstruction table does not yet include the first live B05 output. | Add its narrow local-helper no-go with source and review status; do not promote it to a refutation of existential coordinate selection or full FEI. |

## 1. Minimum packet execution contract

Each A-row should contain, or resolve at dispatch:

1. Its owning B-stream and accountable packet identity. A role ID and an actual process/session ID are different.
2. Work type: baseline, proof, construction, targeted search, certificate, independent audit, or synthesis.
3. Exact target and the smallest useful output. A topic such as 'global potential' is not sufficient.
4. Source versions and normalization assumptions to be frozen before the attempt.
5. Advisory upstream packet IDs, and separately the actual theorem versions used as proof dependencies.
6. Expected artifact and a concrete acceptance or falsification test.
7. A bounded first work cycle and its stopping condition.
8. Intended downstream consumers.
9. Nominated independent reviewer, with conflict-of-contribution handling.
10. Current state, gap ID, attempt ID, and the next action after either success or failure.

Workflow dependencies may form feedback loops: a counterexample can send a proof packet back to a repaired conjecture. A claimed proof dependency graph must be acyclic. Do not encode an advisory research connection as an already established theorem.

Do not invent source pins for future artifacts. An initially unfilled input is a dispatch obligation, not evidence of a source read.

## 2. Resolve the main semantic overlaps

| Overlapping packets | Single-owner interface and distinct work |
|---|---|
| A023, A029, A037, A064 | A023 owns a rarity-payment theorem on an explicit model family. A029 owns the exact two-child deficit recurrence. A037 owns the posterior chain rule and proof that a credit is not reused. A064 owns a candidate global potential that consumes those interfaces. |
| A028, A059, A061, A062 | A061/A062 provide the common entropy and influence telescopes once. A028 proves a stopping/terminal-class theorem using them. A059 proves a composition/decomposition-depth statement with a distinct class and overhead parameter. |
| A018, A019, A058 | A018 owns the exact shared-data collision identity. A019 owns a quantified pairwise-correlation closure. A058 must name a broader overlapping-composition class not already covered by A019. |
| A032, A045, A078, A079 | A032 supplies uniform Fourier phase realizability; A045 handles product-biased normalization; A078 gives an actual coding/padding construction; A079 gives a correlated-auxiliary construction. Reuse a common realizability certificate instead of four separate Fourier engines. |
| A049, A073, A074, A082, A084 | A049 extracts a minimal actual witness. A073 certifies the logarithmic sign. A074 reproduces independently. A082 or A084 handles the separate finite-domain or continuum bridge only when that bridge is needed. |
| A001, A003, A004, A081, A096 | A001 fixes quantifiers; A003 records logical implications; A004 normalizes units; A081 validates a dependency representation; A096 maintains the live navigation index. They should not each create a competing authoritative ledger. |
| A021, A022, A053, A077 | Agree a common sparse-defect fixture format. A021 studies activation limits; A022 gives point-surgery spectra; A053 tests criticality/near-tensor structure; A077 builds multiscale towers. A fixture is shared input, not four separate claimed discoveries. |

This division preserves all 100 IDs. It changes the acceptance contract, not the allocation arithmetic.

## 3. Map 100 hypothetical roles to twenty actual tasks

State the capacity interpretation explicitly:

- The 100-role design includes proof writers, counterexample builders, auditors, certificate workers, and coordinators.
- B01–B20 are routing and ownership labels. They are not twenty additional workers on top of the 100.
- In the actual twenty-task configuration, each B-stream has a backlog of five A-packets. An invocation selects one packet and performs substantive work on it.
- Selecting one packet does not mean rotating mechanically through all five. Resume a productive unfinished packet, consume a new dependency, or choose the nearest ready blocked obligation.
- Preserve A-packet ID, gap ID, attempt number, last derivation, and next action in the run report.
- A ready packet can use an unreviewed claim conditionally, provided that dependency is explicit and the conclusion is not promoted to an accepted theorem.
- If the selected packet is blocked on an unavailable source or resource, choose an independent ready packet in the same FEI stream. Do not spend successive runs acknowledging the blocker.
- Assistance means source-bound requests to an existing peer stream. The plan should not imply permission for five child processes per scheduled task.

The current schedule prompt already prohibits new workers. Replace the loose 'request available local assistance' sentence with an explicit existing-peer handoff rule.

## 4. Baseline tasks should finish

A001, A004, A016, A046, A056, A061, A062 and A081 have useful baseline/intake components. They should not consume a recurring full research position forever.

For each, specify a finite initial artifact and a retirement event. Once an independent relevant check accepts the artifact, later runs consume it rather than rederive it. New source corrections may reopen the exact affected part. Otherwise the capacity moves to a downstream proof, falsifier, or overdue independent review.

The already recovered manuscripts and completed recovery audits count toward the Day 1 baseline. Do not start a new two-day reconstruction merely because a new plan file was published.

Examples:
- A016's standard addressing identities are a calibration fixture; its successor is an iterated or shared-input family with a new cost comparison.
- A056's balanced composition identity is an imported interface; its successor is stability under the actual restricted children being used.
- A061/A062's finite telescopes are inputs to a new potential or stopping theorem, rather than two perpetual independent derivations.
- A046 should freeze a live potential only when one exists. It should not manufacture a candidate solely to keep its intake role occupied.

## 5. Rolling review and bottleneck control

The plan's two audit squads are valuable, but review must begin as soon as an important proof or counterexample is complete.

Recommended workflow:
- Author finishes a source-complete statement and proof, with its intended application and relevant falsifiers.
- A triage pass checks that the artifact is complete and materially advances an unpaid obligation.
- The relevant independent reviewer reconstructs the critical argument while later research continues conditionally.
- The two full-chain reviews are reserved for a complete full-FEI candidate or other major theorem selected for acceptance.
- Day 9 rechecks the integrated candidate and repaired dependencies; it is not the first day anyone reads the proofs.

Use a small work-in-progress cap, for example at most two complete unreviewed candidate claims per stream. If that queue is full, finish a proof, repair an objection, verify a decisive witness, or provide an independent review rather than introducing another broad conjecture.

Review capacity should be measured in completed substantive reviews and actual time, not in reviewer headcount. If 80 research roles each produce several candidates, ten nominal auditors can still be overwhelmed.

A reviewer who supplies a substantive repair becomes a contributor to that version. A089 and A095 should therefore not approve a theorem whose key missing step they supplied. Assign a different unaffiliated reviewer. Two agents reading the same summary or re-running the same code are not two independent proof reconstructions.

Do not require two complete independent audits before every exploratory inference. Preserve provisional/conditional status and review the critical dependencies promptly, or all proof workers can become idle waiting on the review queue.

## 6. Claim propagation and duplicate prevention

A compact versioned claim record should contain:
- claim ID and version;
- normalized exact statement and hypothesis list;
- statement hash and immutable proof source;
- author/contributors and review records;
- source theorem versions used as dependencies;
- applicable falsifiers and their versions;
- current status and the first unpaid line;
- explicit supersedes/refutes relationships;
- next consumers and the exact substitution where the result is intended to be used.

Keep the immutable full reports. Let A096/B20 own the concise live index rather than letting all 100 roles edit a common narrative.

When a claim version is refuted:
1. Record the exact false statement and actual counterexample.
2. Find downstream derivations using that version.
3. Mark the affected conclusions BLOCKED_DEPENDENCY or CONDITIONAL until an alternative proof is supplied.
4. Send the source-bound correction to the named consumers.
5. Require a consumer to state the corrected substitution in its next substantive report.

A receipt, a read acknowledgment, and successful use in a proof are separate facts. The propagation record should retain that distinction.

Use a stable gap ID for the same unpaid mathematical inequality even if a potential or notation changes. A new attempt should name the new method or hypothesis. Rephrasing an equivalent residual is not progress and should not reset stagnation.

No acknowledgment gate should prevent independent permitted mathematics. The light index exists to reduce repeated work, not to generate a new coordination-only workload.

## 7. Computation triage

A five-stage pipeline is preferable to undifferentiated 'run more tests':

### Stage 1: freeze the target and estimate feasibility

Write the exact helper version, actual Boolean search family, parameter domain, expected case count, symmetry reduction and its justification, arithmetic needs, memory estimate, and maximum allowed run.

Use a short pilot, for example at most 60 seconds, to measure actual throughput and numerical scale. The cap is a suggested starting policy, not a claim that any particular resource has been allocated.

All truth tables on n variables comprise 2^(2^n) Boolean functions: 65,536 at n=4, 4,294,967,296 at n=5, and 18,446,744,073,709,551,616 at n=6. Adding one variable can destroy feasibility. Do not enlarge n automatically after a search finds nothing.

### Stage 2: cheap targeted discovery

Use floating-point calculations to rank candidates and locate suspected failures. Prefer structured circuits, symbolic multiplicity classes, small parameter families, and analytic endpoint expansions. This stage can falsify a naive numerical expectation; it does not certify a sign near zero or prove a universal inequality.

### Stage 3: exact candidate verification

For a promising witness, compute an exact integer Walsh spectrum and exact influence, or an equally explicit analytic formula. Check Parseval and actual Boolean inverse realization. Certify entropy comparisons with rational interval logarithms or an exact integer-product comparison.

Stop precision escalation when the required sign is rigorously determined. A near-zero unresolved margin should prompt analytic simplification or a more robust witness, not uncontrolled precision consumption.

### Stage 4: independent reproduction

Use a different representation or derivation for the decisive witness. A074/A092 should not merely call A072's function again. Compare exact data, normalizations, target version, and scope.

### Stage 5: bridge to the desired theorem

A084's continuum coverage needs boundary reductions plus certified region coverage. A finite table needs a theorem explaining why its finite domain is exhaustive. An all-dimensional result needs an analytic reduction; neither a dense grid nor a lack of small counterexamples is that reduction.

Each enlargement should name the proof bottleneck it could resolve and its bounded cost. Reuse one verified search/certificate engine across streams. No new account, paid resource or runtime guarantee follows from the hypothetical capacity table.

## 8. Explicit checkpoints and pivot rules

Translate elapsed days into fixed dates to avoid per-agent clock resets:

| Checkpoint | Jerusalem time | Required decision |
|---|---|---|
| End Day 2 | 13 October 2026, 22:15:57 | Source-complete baseline and exact live targets; baseline packets retired or their precise unresolved source issue retained. |
| End Day 4 | 15 October 2026, 22:15:57 | Identify quantitative new results, decisive falsifiers, and live dependencies; do not count broad reformulations as completed research. |
| End Day 5 | 16 October 2026, 22:15:57 | Reallocate within the existing capacity using actual mathematical advances and review backlog. |
| End Day 8 | 19 October 2026, 22:15:57 | Freeze serious proof candidates for integrated review while preserving independent alternative/falsifier work. |
| End Day 9 | 20 October 2026, 22:15:57 | Resolve audit objections or narrow claims; no accepted full-FEI claim with an unpaid dependency. |
| End Day 10 | 21 October 2026, 22:15:57 | Final accepted theorem/partial-result package and precise continuation frontier. |

Use the configured three-substantive-run stagnation threshold in the report:
- After three substantive attempts on the same gap with no bound, hypothesis, counterexample, or structural improvement, the next run must diagnose the exact obstruction and change mechanism or complete a narrower theorem.
- Access-blocked invocations and bookkeeping-only updates should not masquerade as mathematical attempts.
- Immediate falsification stops use of that helper version, not automatically the entire route. An all-coordinate counterexample does not refute an existential good-coordinate theorem.
- A genuinely new hypothesis or construction deserves a new attempt, but a renamed equivalent potential does not erase the history.
- Keep some independent alternative capacity until a complete candidate exists; avoid moving every proof worker onto one attractive but unchecked mechanism.

## 9. Incorporate the first actual FEI run without overclaiming

The live B05 output supplies an immediate test of the propagation design.

Canonical source:
yspennstate/math-open-problems at commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b,
reports/fei-2026-10-11/runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions/REPORT.md.

Brain full-text mirror:
commit 532e0b5ddb5b3b320b46beb155ee8b2be7e97761,
research_pushes/2026-10-11-full-fei-campaign/handoffs/fleet01/B05/20261011T193057Z-fleet01-B05-rare-restrictions/REPORT.md.

The report gives a genuine Boolean family with d=2^(-3k), delta=2^(-k), L >= (1-delta)(k-2)d, V <= 4 delta d, M=12kd^2, disproving every fixed-price one-node estimate L <= Kd+AV+BM. The complete report, checker, saved output, claims, and exact full-text mirror were read in the preceding followup. The checker reports 95 passing floating-point self-checks. This audit does not assert independent end-to-end acceptance of its theorem.

Add the result to the obstruction registry with its exact scope and review state. Route it to A022/A025/A029/A037/A064 and the relevant independent referee. This should retire the false local helper while keeping good-coordinate selection and nonlocal accounting active.

## 10. Acceptance recommendation

Accept the original arithmetic and portfolio structure. Before calling the plan operationally complete, integrate:
1. the enriched 100-row execution matrix;
2. the one-packet dispatch/resume rule for twenty actual tasks;
3. rolling reviews with contribution conflicts and capacity caps;
4. stable claim/gap versions and correction propagation;
5. bounded discovery-to-certificate computation;
6. explicit baseline retirement and three-attempt pivot rules;
7. corrected full-versus-partial outcome labels;
8. the source-scoped first B05 obstruction.

None of these changes can make a solution of FEI guaranteed. They make the proposed computation more likely to produce usable mathematics, and make failures visible soon enough to redirect effort.

