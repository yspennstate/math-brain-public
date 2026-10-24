# FEI: keeping every worker's research memory current

## Latest manifest, assignment issue state, and active owner scope

The current FEI scientific checkpoint is `FEI-20260922T105045Z-assist-v2`. Always resolve the latest manifest and consume its complete required corrections plus the live inbox; this literal revision is an issue-time reference, never a permanent freshness ceiling. A compact assignment card's `state_revision=FEI-20260922T1000Z-v1` records when that assignment was issued. It does not make the old scientific state current and must not be copied into a new memory acknowledgment instead of the actual latest manifest revision. The same rule applies to task prompts carrying an earlier state revision.

The FEI programme's control revision `2026-09-22.3` is provenance for the issued scientific programme. Later owner controls retain priority. The latest observed revision is `2026-09-22.4`, which changes the active target; these FEI continuation notes do not override it. Continue or resume FEI assignments only when current owner scope authorizes FEI. Publishing a mathematical checkpoint does not reactivate a suspended programme or prove native task adoption.

This protocol applies to **account01–account04, B01–B20: all eighty mathematical workers**. When FEI is the authorized active target, every worker does FEI mathematics. Memory synchronization is a compact opening and closing step, not a separate job, waiting ritual, or replacement for proof work. Keep the existing hourly check-in and finish receipt; add the fields below to those records instead of creating duplicate reporting tasks. Keep task email and push notifications off. A later direct owner stop or access restriction still takes priority.

## 1. One current entry point; immutable evidence underneath

The FEI coordination root (called `BASE` below) is `scheduled_tasks/work/shared/fei-all-team-2026-09-22/` in `yspennstate/math-research-brain`. At the freshly resolved **main commit**, read `MANIFEST.json`, its named `CURRENT_RESEARCH.md`, `CLAIMS.json`, `DELTAS.json`, and your compact assignment card at `BASE/assignments/<account>/<slot>.json`. The complete `ASSIGNMENTS.json` is the fleet-wide projection; individual workers use their own card and named partner cards without rereading the whole matrix. Also read the live `CORRECTION_INBOX.json` at that fresh head; its pending critical events may postdate the last consolidated manifest. The manifest names the actual paths and revisions; never invent a path from a report's filename or assume that a mathematical report belongs in the brain repository. Full mathematics normally belongs in `yspennstate/math-open-problems`; the brain contains the current outline and compact source-bound handoffs.

Use these exact destination rules:

| Artifact | Destination |
|---|---|
| Full mathematics and own-run claim cards | The exact `deliverable.repository` and `deliverable.path` in your compact assignment card; replace `<actual-run-id>` with your actual unique run ID. |
| Peer handoff | The exact `deliverable.handoff` in that same assignment row: `BASE/handoffs/<account>/<slot>/<actual-run-id>.md`. |
| Immutable memory snapshot | `BASE/memory/<account>/<slot>/<actual-run-id>/MEMORY_SNAPSHOT.json`. |
| Mutable pointer to latest committed snapshot | `BASE/memory/<account>/<slot>/LATEST.json`; update with the current blob SHA and preserve the prior source pin. |
| Immutable mathematical correction event | `BASE/events/<account>/<slot>/<actual-run-id>/<event-id>.json`. |
| Initial owner rollout events | `BASE/events/owner/FEI-ALL-TEAM-20260922T095941Z/<event-id>.json`; these record source summaries, not new proofs. |

A mutable branch name is only a discovery pointer. Every mathematical citation retained in memory must identify **repository, full forty-character commit SHA, exact path, and relevant section**. Hash downloaded bytes when available; never fabricate a digest for a source you did not retrieve. A candidate has an immutable ID tied to its complete defining formula, normalization, parameters, and source. Changing its coefficient, correction shape, potential table, or normalization creates a **new candidate ID**, even when a worker calls it a minor repair.

`CLAIMS.json` is a compact current projection, not a new proof. Keep source reports, claim cards, and correction events immutable. The projection may be refreshed; the evidence and truth history must remain recoverable. Older work on FOREST, BT4, MOC4, POS3, and brain installation is preserved as suspended history and must not remain in an active assignment or current FEI proof premise.

## 2. Start each run from a fresh snapshot

1. Resolve the actual current control branch head through the authorized GitHub connector. Read the existing five control files at that commit, including the natural-language owner message. Create the existing actual-hour check-in. If a login already exists, continue without overwriting it.
2. Read the current FEI manifest and its canonical research outline, claim statuses, and assignment. Read **every mandatory correction after your last consumed correction**, plus the current rejection list and all new pending critical events in the live correction inbox. On a first FEI run, load the compact full current state. Corrections published after this rollout remain mandatory. Record both consolidated correction IDs and the inbox event IDs consumed; a matching manifest revision alone does not establish freshness.
3. Read the latest compatible handoff of each named partner and the exact sources of every mathematical premise you will use. A handoff URL alone is not proof consumption. Record whether the source was retrieved and which result you actually used. Work asynchronously from available complete snapshots; missing partners do not require waiting.
4. Update your small repository snapshot with this run's actual control head, manifest revision, correction watermark, exact candidate IDs, source-pinned premises, unresolved implication, and next derivation. Record missing or inaccessible sources as such. Use independently justified premises for substantive work while resolving access gaps; do not substitute old disputed claims.

The startup record is not a promise that no newer correction will arrive. It states precisely which revision this invocation consumed. Never write "all workers are up to date" from one worker's acknowledgment.

## 3. Read mathematical statuses literally

| Status | What may be carried into memory |
|---|---|
| `PROVED_IN_SOURCE` | The source states a proof with its exact hypotheses and domain. Record proof-check provenance separately. The status is a mathematical assertion; a JSON validator or receipt does not establish it. |
| `CONDITIONAL_IN_SOURCE` | The implication and every unresolved assumption are explicit. Do not remember its conclusion as unconditional. |
| `FINITE_CHECK_IN_SOURCE` | The exact finite domain, grid, precision, and certificate/computation are recorded. A numerical pass is not a theorem about all gates, biases, or dimensions. |
| `CANDIDATE_UNPROVED` / `OPEN` | A proposal or missing implication; it must not enter a proved dependency silently. |
| `REFUTED` | The exact statement or candidate has source-bound contrary evidence. A fixed-potential gate obstruction does **not** refute uniform-cube FEI. |
| `NEEDS_REVALIDATION` | A required premise or its application changed. Do not use the result as established until the affected implication is repaired. |
| `EQUIVALENT_REFORMULATION` | The same global burden in a different formulation; this status is not an additional solved implication. |

Currency is separate from truth: `superseded` means that an older formulation or candidate is no longer the current route; it does not automatically make a correct theorem false. Preserve exact finite facts and conditional implications whose statements remain valid. A repaired candidate's success on a known witness is remembered as **witness repair only**, until its new universal inequality is proved.

Candidate-specific corrections remain candidate-specific. In particular, a refutation of a scalar lift such as a coefficient `0.337` or `0.34` applies to that fully defined potential; it does not transfer to a different shaped correction merely because the names resemble one another. The newest feed, not these illustrative coefficients, determines the current state.

## 4. Add discoveries once; connect their dependencies

For a substantive result, append an immutable claim card under your own run folder with: claim ID, exact statement and hypotheses, mathematical scope, candidate ID if applicable, status, source pins, verification provenance, and dependency IDs. Dependency modes distinguish **using a premise**, **assuming it conditionally**, **requiring a candidate to remain current**, and **mentioning it as context**. Mere citation is not a proof dependency.

For a correction, append an immutable correction event naming the precise claim/candidate, old assertion, corrected assertion, source evidence, and replacement claim if one exists. Publish its pointer in `CORRECTION_INBOX.json` with an atomic event-plus-inbox commit or a current-SHA merge. Existing account B20 workers, or another owner-authorized consolidator, fold it into the canonical bundle as described below. Until then its state is **published, pending consolidation**, not silently treated as an adopted theorem. A source-bound critical challenge is visible immediately; suspend use of its challenged premise while checking its mathematical scope. Do not edit another worker's source report or silently erase the old assertion.

A refuted premise blocks dependent attempts that require its truth and propagates along those dependency links. Superseding a candidate blocks attempts that specifically require that candidate as the current route. Neither operation invalidates unrelated FEI results. A proved implication with a false or unresolved hypothesis can remain a correct conditional theorem while ceasing to close FEI; preserve that distinction in the record. New hypotheses create a new claim ID, not an invisible amendment to the original theorem.

Use exact claims first; update prose summaries from them. A claim's author may propose a status, but must not label independent review as complete without actual separate reviewers and their source-bound reports. A full FEI candidate requires the entire arbitrary-dimension uniform-cube conclusion, one finite dimension-independent constant, all hypotheses/degenerate cases, and two independent end-to-end reviews before the team may mark it verified. No finite sweep, read-once result, or repaired example satisfies that gate by itself.

## 5. Refresh before publishing; merge without losing truth history

Before a significant mathematical write, re-read current controls and the current FEI manifest. If the relevant manifest revision, candidate status, or correction watermark changed, consume the new corrections and rebase the mathematical conclusion. Do not wait for the whole fleet. Preserve useful calculations even if their original candidate failed; label their actual scope.

Use a unique immutable own-run path. For a shared projection or your `LATEST.json`, read the current blob and update with its actual SHA; for an atomic tree commit use the observed branch head as the parent and move the branch **without force**. A conflict means re-fetch, preserve both histories, and recompute the merged projection. Never force-push, overwrite a peer's event, or reuse a stale expected blob SHA. An unrelated new commit need not invalidate the mathematics, but it does require a fresh merge before a shared write.

At finish, write the existing receipt plus a compact memory snapshot: starting and final observed heads, consumed manifest revision and corrections, consumed inbox event IDs and unresolved challenges, claim/candidate statuses actually used, partner run IDs actually read, immutable output source, next mathematical step, and successful write/readback receipts. Mark write success only after the connector returns a successful receipt and the committed contents are read back. The reference validator checks provenance shape, correction scope, dependency effects, snapshot consistency, and optimistic-concurrency parents; it does not certify mathematics or contact GitHub.

### Atomic canonical-state consolidation

During authorized FEI work, the existing B20 workers retain FEI mathematics as their primary duty. As a compact secondary action, an account B20 or another owner-authorized consolidator can integrate a ready source-bound event; there is no designated reporting-only worker and no requirement to wait for all eighty workers.

1. Resolve a fresh branch head and read the current canonical bundle and inbox. Inspect the actual result and its affected dependencies; metadata alone cannot promote truth.
2. Preserve existing immutable events and claims. Add the new source and claim IDs, revise the current status projection at the exact affected scope, and propagate only genuine proof/application dependencies. Update `CURRENT_RESEARCH.md` to match the surviving argument and precise remaining obligation.
3. Prepare **`CLAIMS.json`, `DELTAS.json`, `CURRENT_RESEARCH.md`, and `MANIFEST.json` in one atomic commit**. Advance `state_revision` consistently, recalculate SHA-256 over the exact final bytes of each manifest-listed artifact, and list every required correction ID. The manifest never hashes or embeds its own final commit SHA. If an assignment changes, include its projection and digest in that same coherent update.
4. The live `CORRECTION_INBOX.json` is intentionally outside the manifest's hashed canonical file set so a critical event can arrive between consolidations. Remove only inbox entries actually incorporated by this commit, preserving concurrent or unresolved entries. Record the consumed IDs in `DELTAS.json` before removing their inbox pointers. Keep the immutable event files.
5. Run the validator on the prepared bundle, publish with the freshly observed head as parent and a nonforced ref update, then read back the new manifest and changed files. On conflict, re-fetch and preserve both event histories before retrying. A failed update leaves the new event pending; report that exact state and continue compatible FEI mathematics.

Workers who encounter a pending source-bound challenge should retain the canonical status plus its `pending_challenges` reference, and avoid using that claim as a positive premise. They need not wait for consolidation to perform an independent derivation or to inspect the challenge. A pending report is never sufficient to mark full FEI solved.

## 6. Repository memory and native memory are different

This rollout updates GitHub coordination state, research summaries, assignments, and source-bound worker snapshots. GitHub is durable file exchange. It does not by itself establish native ingestion, an authenticated memory query, or memory restored in another scheduled invocation.

Use `repository_memory: loaded` only after reading the specified bytes in this invocation. Use `native_memory: unavailable`, `not_attempted`, or `unverified` unless an actual permitted API/runtime operation supplies a receipt. A claimed native load records the API, source version/hash, actual returned receipt, receiver run, and an observed use of the retrieved content. `full_brain_connected` remains false unless the existing complete readiness requirements are actually met. A local simulation or a second process is not cross-run restoration.

No new native production ingestion, held-out-data import, account connection, paid API, or permission bypass is authorized by this memory protocol. Work on FEI continues without native memory. Do not spend an assigned mathematical invocation rebuilding the old brain installation or collecting unavailable telemetry.

## 7. Adoption is measured by later reads

Distinguish **published order**, **updated native task prompt**, **worker read acknowledgment**, and **substantive use of the corrected premises**. The first two are deployment facts; the latter two need later run evidence. Account caretakers add a compact freshness column to their existing summary and continue their own FEI task. They do not create a reporting-only slot or another acknowledgment loop. Missing, stale, or blocked adoption remains visible without being mislabeled as a stopped scheduler.

The adjacent `MEMORY_BUNDLE.schema.json`, `validate_memory.py`, and regression tests define a compact interchange format for these checks. Existing live state files can retain additional fields. Export the named fields into a validation bundle; do not invent proof-check or native-memory receipts merely to make a validator pass.
