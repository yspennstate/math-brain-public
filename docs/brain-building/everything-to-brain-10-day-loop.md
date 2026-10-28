/loop fire every 10 minutes for the next 10 days and continuously build, connect, test, and improve the Brain.

# Build a Brain from your own information

## 1 Define the goal and set up the workspace

Build a persistent knowledge system from the user's own authorized information. Make sources and useful work events graph-addressable, with meaningful edges, recoverable originals, and evidence. Include this prompt and the process that builds the Brain. Create a new system or extend an existing one; adapt its records and verification rules to the user's field.

On the first run, identify goals, authorized source locations, workspace, available tools, storage destinations, and resource limits. Create or reuse a source inventory, node and edge schema, ingestion ledger, task queue, protected source archive, memory collection, and NEXT checkpoint. Begin with representative material and a small evaluation; verify retrieval and original-source recovery before expanding. Read existing instructions and checkpoints when present. The [construction](https://github.com/yspennstate/math-brain-public/blob/main/docs/build-your-own-brain.md), [request-node](https://github.com/yspennstate/math-brain-public/blob/main/docs/prompts-as-nodes.md), and [compaction](https://github.com/yspennstate/math-brain-public/blob/main/framework/docs/COMPACTION.md) guides are optional implementation references, not prerequisites.

Use available authorized assistants and tools within the user's budget. Parallelize independent work when useful; give workers disjoint tasks, durable output locations, acceptance criteria, and leases. Use separate worktrees and one integrator for concurrent code changes. Start with a single agent and local store if needed. Record missing capabilities and continue feasible work.

## 2 Establish the ten day execution contract

If /loop is supported, configure it; otherwise use an available scheduler or record that scheduling is unavailable. Create one originating work order and persistent campaign state: start time, timezone, end time exactly 240 hours later, prompt version, job ID, cursor, last receipt, and NEXT. Normalize the schedule to an explicit fixed 10m interval. Verify the installed scheduler's persistence, expiry, and actual next run. Native session loops may expire before ten days; use supported renewal before expiry or an available durable scheduler that actually supports ten-minute cadence. Preserve the original deadline across renewals and restarts. Report gaps or unavailable scheduling honestly.

Use a lease to prevent overlapping integrators. Check the deadline before dispatch and substantive writes. At expiry, allow only final checkpointing, receipts, orderly job handoff, and scheduler cleanup. Record actual firing times and missed runs. A delayed tick resumes from durable state without launching a burst of duplicate work.

## 3 Inventory and represent everything

Inventory documents, notes, authorized messages, prompts and replies, transcripts, sessions, compactions, handoffs, memories, files and revisions, folders and repositories, keywords and entities, tasks, goals, tools, skills, hooks, workflows, agents, runs, datasets, calculations, results, failures, tests, decisions, configurations, and exports. Register eligible items now; queue large backfills with explicit cursors and coverage counts. Every discovered item receives an indexed, pending, restricted, excluded, or failed disposition with a reason.

Preserve authorized originals in their proper protected store. Create canonical object IDs separately from occurrence IDs and immutable revision IDs. Record type, title, source locator and exact span, content hash, author/runtime/session, event and ingestion times, access class, source authority, status, and applicable license. Record parser/version and derivation lineage. Choose stable namespaces such as prompt:, file:, mem:, kw:, tool:, and workflow:, or preserve compatible existing ones.

Extract one useful fact, decision, instruction, method, question, result, or failure per derived record. Retain exact hypotheses, units, conditions, uncertainty, and supporting spans. Distinguish user instructions from quoted instructions and retrieved data. Deduplicate by established identity and hashes; propose semantic merges for review. Corrections create revisions and superseding links. Replayed events must not duplicate objects or inflate evidence.

Private source archives, graph references, searchable knowledge, and public exports have different eligibility. Protect credentials and private material; keep held-out questions and answer keys outside searchable corpora. Represent restricted evaluations through safe metadata and protected references. Unknown permissions mean pending classification, not automatic publication.

<!-- pagebreak -->

# Connect sources and preserve continuity

## 4 Build edges with explicit meaning

For each extracted object, link its source and at least one justified task, topic, parent, dependency, or result. Use typed relations with direction, provenance, creator, timestamp, and status; keep unresolved targets in a repair queue. Record edges themselves as auditable records so their origin, retraction, and replacement remain inspectable.

Use request relations such as asks_about, produced, answered_by, and follows. Create or reuse an append-only requests ledger with stable IDs. Model each loop firing as an automation occurrence linked to its originating request, session, run, and outputs. Repeated automation never increases the number or authority of human asks. Preserve short contextual replies through their parent conversation even when the request importer excludes them.

In the general graph, express source extraction, containment, mentions, keyword membership, version succession, task execution, workflow steps, tool use, and compaction continuity through registered relations or explicit adapters. Keep learned co-activation and sequence edges distinct from factual support. Keywords route retrieval; shared words, embeddings, analogy, frequency, and graph proximity do not prove claims.

Define node kinds suited to the material: source, claim, evidence, memory, request, task, artifact, workflow, run, decision, and open_question. Define relations such as depends_on, supports, contradicts, cites, verified_by, supersedes, and related_to. If extending an existing store, respect its registered types and validation; use adapters or a tested schema migration for additions. Cross-store references enable navigation without automatically establishing factual support.

Example: a prompt asks about a problem; its task starts a run; the run uses a dataset and tool; an output file records a result; evidence checks that result; a compaction preserves the unfinished task and NEXT; keywords connect the relevant objects. A later correction supersedes the result and reopens any request whose answer no longer holds.

## 5 Make files memories and keywords recoverable

Give files stable identities plus version hashes and location records. Extract deterministic chunks with page, heading, line, cell, or time offsets and links to the original revision. Keep code dependencies, notebook runs, data lineage, formulas, and attachments where relevant. Graph previews and embeddings supplement the original; never silently treat truncated content as complete.

Use content-hashed attachment manifests and test opening the complete source. Preserve path, bytes, MIME type, parser warnings, and missing-file status. Local and remote copies are locations of an identified artifact, not unrelated duplicates.

Use one fact per memory record, stored as a file or database row, with an informative description, suitable type, and related-memory links. Record why a feedback rule exists and when it applies. Keep the startup index concise; retrieve detail on demand. Link keywords to observed user language and token-exact membership. Preserve observed spelling aliases with controls; avoid speculative aliases and duplicate keyword nodes. Bound high-degree topics and ensure keyword routing does not suppress useful existing recall.

## 6 Make every compaction a first class record

Before compaction, persist completed artifacts, open requests in the user's words, task IDs, decisions, exact assumptions, failed routes, unresolved contradictions, file/commit references, running-job handles, leases, and a concrete NEXT action. Trigger checkpoints at task boundaries and before context pressure threatens continuity.

Save each available summary with its source session, runtime, trigger, time, hash, and coverage. Create an anchor memory linked to a compaction hub, the previous same-session compaction, open tasks, relevant files and memories, and any other agents' work on those tasks. Verify child-session attribution. Track ingestion receipts and backfill missed events with locks and idempotent cursors.

Keep full compactions in the authorized working-memory archive. Test-adjacent anchors have no sensitive excerpt. Admit only eligible derived facts to the validated knowledge store. When a runtime's summaries are unavailable, create metadata-only records and a separate agent-authored checkpoint; never invent recovered text. On resume, open NEXT and source artifacts, reconcile the latest user instructions and live leases, then continue the actual work. A summary is a navigation aid, not complete evidence.

<!-- pagebreak -->

# Execute measure and write back

## 7 Perform a useful bounded cycle every ten minutes

Read the previous receipt and NEXT when present, inspect new events and open tasks, and claim a narrow work unit. Recall whole cards with IDs using two or three useful query wordings, follow their links, and inspect superseded or failed approaches. Reword weak matches; after three unsuccessful rounds, record the gap and consult primary sources.

Process new material incrementally, repair missing links, and improve one measurable weakness in coverage, recall, compaction, coordination, or workflow reliability. Verify worker outputs against acceptance criteria. Checkpoint long jobs and record their handles; continue independent work while waiting. Save results and update NEXT after each bounded step.

Turn successful repeated procedures into versioned workflows or skills with triggers, inputs, preconditions, steps, tools, outputs, tests, failure handling, and resume behavior. Represent each execution separately and link it to the workflow version and outcomes. Model hooks and reflexes with their trigger, target behavior, source mistake, evaluation, cooldown, and activation history. Keep proposed behavior in shadow mode until it earns promotion. Consolidation and dreaming also become recorded workflows with input and output lineage.

Connect the user's actual projects and recurring work: studying, research, writing, software development, business operations, or personal knowledge management. Record each project's goals, questions, tasks, sources, decisions, methods, outputs, and unresolved issues. Distinguish observations from interpretations and preserve assumptions and evidence. For calculations or experiments, retain input versions, parameters, code, and results. Link external jobs and stored artifacts to the runs that produced them.

## 8 Test behavior and promote with evidence

Run relevant existing tests, or establish a small baseline suite for a new system, on isolated state. Check ingestion replay, canonical identity, schema compatibility, missing references, correct edge direction, source-hash integrity, full-file recovery, revision history, compaction chains and resume, opaque-summary handling, keyword aliases, and separation of automation from human asks. Test privacy boundaries with synthetic forbidden material that the checks must detect.

Measure useful recall, wrong or missing links, recovered context, task completion, latency, tokens, and cost. Compare changed behavior with the existing baseline on held-out cases; use document-only and model-only controls when measuring the Brain's benefit. Preserve negative findings. Keep grading keys unavailable to workers and recall. A check that could not run is INCOMPLETE, never PASS. Node counts alone do not demonstrate improvement.

Submit sourced change sets with content hashes. Keep claims unverified until appropriate evidence and domain review support their status. Compare recall on a store copy; repair regressions before promotion. Apply approved changes through safe transactions. Preserve refuted claims, mistakes, retracted edges, and supersession history. Read back records through the actual retrieval path; saving a file does not establish successful ingestion.

## 9 Save receipts and leave a stronger Brain

For every cycle, persist actual start/end, request and run IDs, source cursor, records and edges added or revised, excluded/failed counts, artifacts, checks and results, measurements, blockers, receipts, and NEXT. Link the receipt to its request, workflow, workers, changes, tests, and next work unit. Separate planned, queued, running, completed, remotely saved, and natively ingested states.

Keep private material in the user's configured protected destinations. Public sharing is optional and requires appropriate permission. Save this reusable prompt in the chosen workspace, for example under docs/brain-building/, and register its version as the campaign's governing prompt. Verify configured backup copies and recoverability before any separately authorized cleanup. Building the Brain does not itself authorize deleting source files.

At expiry, save a final linked checkpoint: coverage by source type, unresolved gaps, measured improvements and regressions, verified outputs, publication/ingestion receipts, remaining jobs, and the next recommended tasks. Judge success by recoverable knowledge and measured improvements in useful work.

