# September 23 architecture and delivery delta

## Scope and integration files

Compared `<private-repo>` at `bcff9346b68959f4cf330fdf9ca0e64a21c77d3e` with `9c754d786b3a0ea4943da0585d1490c13cd9ef99`. GitHub reports 11 intervening commits. This review covers the designated recall, dispatcher, owner-context and regression-gate changes. The benchmark agent owns T11/T12 numerical evidence and deployment receipts; their counts should be integrated separately.

Ready for manuscript integration:

- `proposal.tex`: approximately 535 words, source-grounded architecture subsection without repeated T11/T12 results or private billing details.
- `update_delivery_refs.bib`: five source references used by that subsection.
- `headless_gate_control.json` and `check_headless_gate.py`: portable isolated source-function evidence if useful; neither executes a live hook nor alters operational flags.

`fresh/`, `old/`, `source_manifest.json`, `delivery_refs.bib`, and `workflow_cost_inspection.json` are working evidence. In particular, the complete owner-memory and cost-guard source copies are not intended for inclusion in public-facing manuscript files or supplements. Use only the curated bibliography above for this subsection.

## 1. Normal entries can become explicit policy seeds

The loader already recognized `normal`, `parent_only`, and `disabled` modes, trigger groups, aliases, blocking phrases, and a separate structured intent gate. The update adds a loop in deliberate `recall()` for **normal** entries with trigger groups. If at least one group is wholly contained in the alias-enriched query-token set, and no configured blocking phrase occurs, the entry receives `policy_seeds[slug] = 3.0`, a lexical seed of at least `3.0`, and lexical eligibility. `BRAIN_RECALL_PINS=0` disables this new normal-entry promotion. A normal entry that does not trigger remains available through ordinary retrieval. This differs from parent-only gating, which removes the entry from ordinary seed channels unless its approved direct or intent condition succeeds. [Pinned brain source](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/brain.py).

The policy grew from three entries (one disabled, two parent-only) to five entries by adding two normal pins. The two additions have respectively 35 groups/54 alias keys and 15 groups/23 alias keys. The existing three entries were unchanged. This is deterministic lexical policy routing with explicit vocabulary. It is not learned semantic generalization, and its presence does not show that an agent acted on the selected memory. [Pinned recall policy](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/recall_policy.json).

The pin is introduced **before** graph propagation and seed-based semantic scoring. It can therefore affect graph/semantic tail candidates or their component scores. In the default BM25-first body, many existing BM25 ranks can remain unchanged, but removing the pin is not structurally guaranteed to recover the original full list. That must remain an empirical query-level statement. The ordinary display cap is `recall(query, n=8)`, so a pin consumes one of the same eight rows and can displace another candidate. The source memory explicitly recognizes the retrieval-versus-agent-action distinction; quantitative retrieval claims belong in the benchmark subsection. [Pinned brain source](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/brain.py).

## 2. Post-coverage precedence repair

The initial policy promotion uses an additive score `bm_peak + 2 + strength / policy_peak`. Name coverage and question-side coverage then multiply ordinary BM25 scores. A re-sort could consequently place an ordinary hit above the policy entry despite its initial promotion.

The new block resolves policy slugs through supersession, keeps their maximum policy strengths, finds the highest non-policy adjusted score in `order`, and replaces each policy score by:

`max_non_policy_score + 2 + policy_strength / policy_peak`.

It re-sorts by those replacement scores. This establishes precedence at that stage and orders policy entries by their policy strength. The fallback maximum is the original BM25 peak if no non-policy score remains. [Pinned brain source](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/brain.py).

Qualifications matter:

- The new lift lies inside the default BM25-first branch. `BRAIN_RECALL_BLEND=1` selects the legacy blend instead.
- Later query-semantic fusion and status ordering are separate stages; source-level precedence claims should identify the stage/configuration. In particular, `BRAIN_RECALL_STATUS_ORDER` defaults to `0`, but enabling it applies status weights and can re-sort after the lift.
- Display scores are normalized/rendered after ranking and are not calibrated relevance probabilities. A displayed score is not a guarantee of evidentiary truth.
- No new full-stack live runtime replay was performed in this review. Source, memory reports, benchmark records, emitted output, receiver evidence and subsequent action should remain distinct evidence classes.

## 3. Description rendering and context budgets

The new `_full_description` reads a bounded prefix of the selected memory file, locates closed frontmatter and a one-line `description`, normalizes whitespace, and falls back on failure. It is used only for displayed rows, ahead of the index description. `BRAIN_RECALL_SNIPPET` defaults to `320`; longer descriptions are shortened and receive an ellipsis suffix. This replaces the old `d[:150]` display and can expose useful content hidden by short index lines, while increasing the allowed excerpt length. The 8,000 bound is the argument to a text-file `read`, so describe it as a bounded prefix rather than claiming a strict UTF-8 byte limit. [Pinned brain source](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/brain.py).

The dispatcher still has `INLINE_CAP = 9800`, in Python characters, under a documented `HARNESS_INLINE_MAX = 10000`. It preserves small hook messages, divides remaining capacity among larger messages and writes untrimmed overflow separately. This allocation code predated the inspected delta. Its documented harness interpretation is a source report, not an independently reproduced receiver measurement. [Pinned dispatcher](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/hook_dispatch.py).

Owner delivery has a separate `budget=9000` in **UTF-8 bytes**, including existing context and the history notice. It reserves available space, refits content and keeps leftovers in pending state. The receipt is saved after `writer.write` and `writer.flush`; it records hash, byte length and the explicit evidence stage `emitted_stdout_not_receiver_verified`. The single-line delta in this file expands picture-worker recognition from “a picture maker” to “a or the picture maker.” Existing subagent, headless, offline and safety-output checks were already in the baseline and must not be counted as new interventions. [Pinned owner delivery](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/owner_context_delivery.py).

## 4. Dispatcher controls and headless-arm mismatch

New dispatcher behavior includes a `HEADLESS_DIET_ON` marker beside the dispatcher, headless recognition from a launcher prefix or stored headless session state, and omission of ten named operational hooks when both gates succeed. It also omits a configured hook with an explicit `--enabled` argument when that flag file is absent. These are invocation controls; they are not source evidence that a live marker exists or that an end-to-end intervention ran. [Pinned dispatcher](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/hook_dispatch.py).

Independent source inspection confirms the analyzer agent's integration finding: this dispatcher never reads `BRAIN_HEADLESS_DIET`, although the new AB30 runner sets it to `1` only for `ondiet`. Both on and ondiet use a headless-prefixed prompt. For this source pair, absent marker means neither arm gets this diet; present marker means both recognized headless arms get it. The environment variable alone does not select the intervention. Sixteen isolated evaluations of the unmodified `_headless_session` function confirmed this truth table across marker states, environment unset/1, a headless prefix, the updated picture-worker prefix, an ordinary prompt and stored headless session state. Temporary fixture paths were used. This is reproducible source-function evidence, not a live runtime result.

The analyzer agent's proposed **paper-only** repair was independently inspected: explicitly set `on=0` and `ondiet=1`, make `0` a hard-off dispatcher override, let `1` enable the existing headless classification independently of the marker, and retain marker behavior when unset. No blocking logic issue was found in the reviewed proposal. Its aggregate and whole-dispatch tests are owned by that agent. No operational code, marker or settings were changed by this review.

## 5. Source-receipt gate now tolerates bounded growth

The gate previously failed any source-field mismatch. It now allows a mismatch when every differing field belongs to `{prompt_terms_sha256, prompt_term_count, corpus_search_sha256, corpus_vocab_sha256, memory_count}` and the artifact age lies between zero and `BRAIN_GATE_RECEIPT_WINDOW_S` (default `10800` seconds). Other drift, including reviewed-alias changes, still fails. A mismatching artifact older than the window fails; an exactly matching source can still pass irrespective of this drift-tolerance window. Therefore a PASS under the new rule can mean accepted live-input growth, not strict source identity. [Pinned regression gate](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/brain_regression_gate.py).

## 6. Read-only push-cost check for this authorized paper update

The operational principle is to inspect what a push starts, batch a completed piece of work, and preserve a skip-CI head message for a document-only update. No workflow, settings, hook installation, account budget or CI dispatch changes are part of this task.

Accessible, untruncated GitHub root trees showed no `.github` entry at either inspected destination snapshot:

| Repository | Inspected commit | Observation |
|---|---|---|
| `<private-repo>` | `9c754d786b3a0ea4943da0585d1490c13cd9ef99` | No repository-root workflow directory |
| `yspennstate/math-research-brain` | `37515b15222a23911b8953f4b0f70ceeebb7ed22` | No repository-root workflow directory |

The contents requests for `.github/workflows` returned 404, corroborated by those accessible root trees. This is a narrow source-existence check, not an account-billing guarantee. Before the actual update, reread the destination ref/tree, retain one batched publication per destination, verify only authorized paper/report/proposal paths change, and confirm the published commit. No CI override is needed on the inspected paper-only descendant trees. Detailed owner billing history is intentionally excluded from the manuscript fragment and curated bibliography.
