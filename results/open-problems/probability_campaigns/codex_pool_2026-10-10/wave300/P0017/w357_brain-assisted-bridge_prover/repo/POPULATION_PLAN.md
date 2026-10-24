# Math-brain population - 10h build plan (owner goal 18:47 2026-08-02, clock to 04:47)

Owner's words: work for the next 10 hours on building the full math brain; all codex agents
work only on this; theorems, lemmas, definitions, everything in the whole math universe,
making text for everything, nodes, and then having that fire and get injected as agents
connected to the brain are thinking.

## Architecture decisions (locked ~19:05)

- Base: branch agent/mathbrain-population-10h-0802 (this worktree), forked from the codex
  overlay tip 1f8dfa6 - ingestion.py + overlay.py + hardened store. 14/14 ingestion tests
  pass here with PYTHONPATH=~\math-brain-build\src (installed package is main
  and lacks the overlay; do NOT touch the shared install).
- Division of labor: codex agents author DRAFT bundles (simple JSON, spec below); ONE
  integrator (mine, tools/integrate_drafts.py) performs all ceremony - digests, source
  manifests, store seal, release MAC - and ingests sequentially. Five agents never
  reimplement crypto.
- Dark is a refusal state (ingestion.py:950) - every ingested bundle carries an APPROVED
  manifest signed by the local population gate key (local/population_gate.key, gitignored).
  HONESTY LIVES IN TRUST CLASSES, not the MAC: all population nodes enter as
  GENERATED_UNVERIFIED (or SOURCE_VERIFIED where the integrator confirmed the excerpt
  digest against a fetched source); QA packet E upgrades later via supersession.
- Store: local\population\brain.sqlite3 + local\population\objects\ (content-addressed).
- Inbox: ~\math-brain-inbox\<agent-id>\bundle_*.json (drafts) - claimed.
- Firing/injection (the hardest piece, built EARLY not last): a math_sense recall lane that
  matches session prompts/context against the population store and injects top nodes as
  system-reminder context, modeled on the existing unconscious hooks; must abstain by
  default, fire only on mathematical content (two-anchor rule per the general brain's
  measured polysemy lesson), ASCII-only, parse-validated, fail-open silent.

## Phases and gates

- P0 done: mesh coordination (broadcast msg-bc05e9c4e0 fanout 5; acked requests to the two
  live codex; tasks 338-342), claims (inbox, worktree, branch), worktree, contract read,
  tests green.
- P1 (by ~20:00): BUNDLE_SPEC.md at inbox root; integrator tool; VERTICAL SLICE - one real
  6-entry bundle authored by me, integrated, ingested, and RECALLED via retrieval. Gate:
  a store query returns the right theorem for a test prompt.
- P2 (by ~21:30): injection hook prototype fires a node into a live test prompt; positive
  AND negative controls (fires on math prompt, silent on trading prompt).
- P3 (through the night): mass population - codex drafts + my own harvest lanes
  (Wikipedia/ProofWiki summaries, mathlib4 name index, owner-territory nodes from
  arXiv:2607.07778 / 2607.11010 / MOLS). Integrator loop ingests, dedupes, logs counts.
- P4 (03:30-04:47): verification (counts, dedupe rate, N-random spot-check vs sources,
  retrieval precision probes), hook hardening, memories, readmes, final report.

## Progress ledger (append-only; timestamps are Get-Date-measured)

- 18:53:30 tasks 338-342 posted; broadcast + 2 acked sends out.
- 19:0x claims clm-6577d31c33 (inbox), clm-c6f784cb8e (worktree), clm-209155a2b3 (branch);
  worktree at 1f8dfa6; ingestion tests 14/14 green.
- 19:02 P1 GATE PASSED: smoke bundle_001 (6 entries) ingested through the sealed pipeline
  after the locator/content-digest contract fixes (one source artifact per entry);
  retrieval returns Lagrange lex 2.71 + graph 1.85 via typed depends_on; off-topic probes
  ABSTAIN at min_support 0.5 / min_margin 0.1 (2 pos + 2 neg controls).
- 19:09 P2 CORE LIVE: math_sense.py (claim clm-9f7b67b3a9) fires the Lagrange block on a
  byte-exact driver test, silent on neutral off-topic/broken-stdin/missing-store; wired
  into settings.json UserPromptSubmit position 4 (claim clm-888a3b6f60, backup
  settings.json.bak_mathsense_20260802T190918, reparse ok). Earlier PS-pipe test silence
  was pipe encoding, not the hook. Live-brain prompt-contract advisories fired on these
  writes; proceeded under the owner's explicit session directive (this goal IS the
  injection wiring), everything claimed + reversible; noted for the hourly reconciler.
- NEXT: P3 mass population - integrator --watch running, codex GO message, my authoring
  lanes (owner-territory bundle first).
- 19:12:48 watch loop autonomously ingested bundle_002 (13 owner-territory entries: law of
  robustness chain with honest scope, Ising verification with the certified interval, MOLS
  + N(10)). Store 19 nodes. Live-fire: robustness prompt injects BLN conjecture (12.3) +
  Shmalo theorem (11.8) at 0.52s. GO broadcast fanout 5; targeted codex receipts PENDING
  (not yet delivered - they check in on their own cadence).
- 19:1x launched 3 authoring subagents (analysis/algebra/topology lanes); commit went
  CRITICAL 90.7% with owner active -> shed per doctrine: stopped algebra + topology
  subagents (respawnable; integrator ignores .part files), kept analysis lane + watch.
  LESSON for the night: serialize authoring lanes when commit > ~88%; one subagent at a
  time from here unless headroom returns. bundle_003 (14 RMT/concentration/inequality
  entries) authored by me, in inbox awaiting the watch pass.
- 19:16:48 bundle_003 ingested (store 33). Wikipedia harvest batch 1: 59 fetched, gate
  dropped 3 (stub/duplicate/truncation), 56 activated 19:30. Harvester hardened: 429
  Retry-After backoff, resume-from-work-product, batch numbering offset (collision bug
  caught by the retry scar). ProofWiki 403s bots - respected, not spoofed; lane pivoted
  to Wikipedia REST which permits it.
- 19:2x commit critical again (91.4) with owner active: shed the LAST Claude subagent;
  switched codex enlistment from waiting-on-mailboxes to DIRECT delegation - worker 1
  (algebra lane, delegate_codex/gpt-5.6-sol) running. Owner asked whether all codex are
  helping: answered honestly (2 registered: trading-brain ACKED but correctly declined
  peer-relay reassignment - needs his direct word in its own thread; mathbrain-10d-root
  mail still pending delivery; 3 parked codex processes unreachable by mesh).
- 19:24 "packet 339 taken" message = my own analysis subagent's mesh registration seconds
  before I stopped it; lane is FREE - do not double-count. Acked all inbox, answered
  trading-brain respecting its boundary.
- 19:32:49 wikipedia bundle ingested (store 89). Hahn-Banach probe fires at 0.51s. Tooling committed to my branch (secrets-scanned staging). QA sample review_001.json (30 nodes) exported; worker prompts staged for qa/analysis/topology. OPEN: injection not yet observed on a REAL harness prompt - watch surfaced.tsv. Hour-1 memory filed.
- 19:48 worker 1 (algebra) ACCEPTED: served gpt-5.6-sol verified undowngraded, 45 entries 46 relations, 0 validation errors, 6/6 sampled statements correct (parent-checked before release). Harvest batch 2: 138 fetched, gate dropped 16, 122 activated. Commit eased to 86.3 - two workers permitted.
- 20:2x topology lane landed (48 entries, 57 relations, self-audited AoC fix). Supersession-aware xrel resolver shipped (superseded nodes excluded from the logical map). Contract lesson: relations must ORIGINATE at a bundle entry - existing->existing re-knit is forbidden by design; orphaned edges around corrected nodes self-heal as new bundles cite them (8 accepted as temporary). Azuma bundle in with 2 legal xrels. Quarantine renamed .rejected-note after a .rejected.json glob-match cascade. Codex retry due ~20:30.
- 21:03 coordinator claude-mathbrain-build-0802 died (usage limit) just after commit
  43f7466 landed; integrator watch + harvest lanes died with it; geometry Sonnet lane lost.
- 21:2x-21:49:00 TAKEOVER by claude-8c0397aa (owner: keep working, only math brain). Claims
  reacquired after lapse; ledger reconciliation: nothing unprocessed (016 ingested 20:55,
  qa3b 18-supersession wave 21:00). Retrieval: title-phrase channel applied POST graph
  spread (hub nodes were collecting propagated share of neighbors' bonuses) + linked-tie
  abstention exemption; probes 6/8 -> 8/8; suite 511 passed; commits 2626b5b, 665864e.
  math_sense: top-3 UNIQUE-title injection (near-dup harvest/authored pairs burned slots);
  pos/neg controls re-verified live. QA-4: 80-node referee sample -> pointer-only-lede
  defect class found by hand, mechanized in corpus_audit (theorem-titled body, no assertion
  marker) -> 74 harvest stubs corpus-wide + perron-frobenius; 3 Sonnet correction lanes
  drafting (qa4a/b/c), refereed on arrival. h01 thin-shelves (30: stats/info/numerical/
  games/category) + g01 geometry-dynamics-pde (36) authored, refereed entry-by-entry,
  ingested. Garble sweep: 1 hit (Liouville harvest, formula stripped mid-sentence),
  superseded via qa4d. Store 683 current / 42 superseded, retrieval 0.10-0.15s.
- 21:59:22 QA-4 CORRECTION WAVE COMPLETE: all 75 pointer-only/damaged harvest nodes
  superseded with real statements (qa4a 25 analysis/complex, qa4b 25 prob/dynamics/geometry,
  qa4c 24 algebra/NT/logic + perron, qa4d liouville garble, qa4e poincare-inequality orphan).
  Referee catches during the wave: little-Picard "infinitely often" over-claim (false for
  polynomials, fixed by hand); duplicate Galois target across lanes A/C (C's dropped);
  one worklist orphan from the lane split (authored inline); two more mechanical-pattern
  false-positive classes fixed (infix dot product, comma-ellipsis). Audit now: 683 current,
  117 superseded, flagged 0, dep cycles 0, probes 8/8, retrieval 0.10s. 142 entries ingested
  this shift total. Integrator --watch restarted for the night (hidden, this session).
  Open for QA-5: adversarially referee the correction wave itself; near-dup title families
  across harvest/authored namespaces (injection-level dedup only); codex lanes quiet since
  19:45, mesh tasks 338-342 open.
