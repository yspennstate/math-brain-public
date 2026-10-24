# Construction and audit log

This is a public-safe evidence ledger for the initial hardening campaign. It
records reproducible outcomes, not local file paths, source excerpts, machine
names, credentials, or private mathematical content. Machine-local manifests
and detailed findings remain under the gitignored `local/` tree.

## Campaign contract

- Started: 2026-07-13 11:08:11 UTC.
- Scheduled end: 2026-07-13 21:08:11 UTC.
- Scope: a mathematical-research memory and verification system only.
- Excluded: finance, trading, company, client, personal, credential, and
  unrelated-project material.
- Publication rule: an allowlisted local source is eligible for review, never
  automatically eligible for copying or publication.

The campaign remains open until the scheduled end. A completed component is not
evidence that the full timed contract is complete.

## Evidence ledger

### Privacy-isolated core

- Typed mathematical records and graph edges are implemented.
- Claim promotion is scoped to evidence kind; examples and numerical checks do
  not verify universal theorems.
- Retrieval, mistake triggers, citations, formal proof receipts, and
  consolidation are separate layers so agreement cannot be mistaken for
  independence merely because one component called another.
- The initial core and its tests were committed as `4c2cbf3`.

### Privacy and publication hardening

- Allowlist manifests now use a strict schema, exact run-local location, opaque
  source identifiers, explicit rights and content classes, and a mandatory
  local-only derivation policy.
- Approved reads use stable file descriptors with repeated containment,
  identity, link, and size checks; hardlinks, reparse points, home recursion,
  alternate streams, and check/open swaps fail closed.
- Local derivations are append-only. Public artifacts require a separate
  provenance sidecar, a reviewed redistributable license, source references,
  reviewer identity, a matching artifact digest, and a clean privacy scan.
- A combined-tree regression fixed a scanner ambiguity between UNC paths and
  LaTeX regular expressions while retaining a real UNC canary.
- The integrated hardening is commit `5b5d582`. At that checkpoint, 132 tests
  pass, 3 privilege-dependent link tests skip on this Windows host, all 53
  tracked files produce zero privacy findings, and the secret scan is clean.
- These gates are necessary, not sufficient: metadata is not a cryptographic
  attestation, and final human review remains mandatory.

### Guarded retrieval and mathematical consolidation

- Formula, symbol, lexical, and typed-graph signals have separate score traces.
- Retrieval explicitly abstains on empty, weak, or ambiguous matches and keeps
  negative edges visible as warnings rather than evidence for a claim.
- Evaluation retrieval rejects test-split, answer-role, active-item,
  active-pair, source-matched, denied, and quarantined records.
- Structured mistake records activate concrete reflexes with ordered actions,
  required evidence, and a stop condition.
- SWS-style replay and REM-style association emit deterministic quarantined
  proposals. The proposal type has no conversion path to verification evidence.
- The integrated component was committed as `ac13684`; the full suite at this
  checkpoint passes 86 tests.
- Red-team limitation: the evaluation guard trusts metadata assigned at
  ingestion. A malicious record falsely labeled as a training claim can pass
  the guard, so only provenance-validated records may enter an evaluation index.

### Paired evaluation protocol

- Ten matched brain-on/brain-off pairs are pre-registered in code.
- Assignment, strict solver-output parsing, macro scoring, deterministic paired
  bootstrap intervals, and benefit gates are tested.
- The protocol records model identity as unverified unless it is supported by a
  response-side receipt; request labels and solver self-reports are not treated
  as proof of the served model.
- The protocol was committed as `9894c2e`.

### Lean verification gate

- The project pins Lean 4.30.0 and now executes the installed `lean` binary
  directly; Lake and the Elan proxy are not runtime authority paths.
- Exact source bytes are rebuilt from a private snapshot in local-import order
  with trust level 0, one thread, fixed memory/time/output limits, process-tree
  containment, hidden/BelowNormal launch, and live compute-governor yielding.
- Placeholders, new axioms, nonlocal imports, unsafe/native or compile-time-I/O
  escapes, and output-spoofing commands are rejected before invocation.
- Named declarations require one canonical `#print axioms` command and one
  no-axioms kernel report. A direct local smoke passed all three sample
  declarations; the signed evidence/attestation/receipt round trip independently
  verified with zero marginal API cost and no network use.
- Kernel acceptance and prose-to-formal-statement fidelity remain separate
  decisions.
- The initial gate and sample project were committed as `8f284ed`. A later
  direct-Lake attempt was blocked by Windows Application Control and correctly
  failed closed; replacing that path with direct Lean removed the blocked and
  unnecessary launcher without weakening the trust boundary.

### Exact-arithmetic benchmark baseline

- Commit `9bdcb82` generates exactly 10,000 deterministic MathIR records with
  unique coordinate-derived identifiers.
- Each record has a clean solution, a faulty solution, one recorded bad line,
  and a replayable one-line repair.
- The baseline spans five elementary or undergraduate exact-arithmetic
  families. It is a valid baseline, not yet the requested broad benchmark of
  qualifying-exam, hard, and research-status material.
- A parent-side referee evaluated the canonical JSON without calling either
  production validator. All 10,000 clean traces passed, all 10,000 faulty traces
  had exactly one false assertion at the recorded line, and all repairs exactly
  recovered the clean trace.
- Full-bank SHA-256, with one canonical JSON record plus newline per item:
  `a82199d658f95f18016f3c402923cb71afd7eef63ca8a2ed7df534dfcf404872`.
- Independent RFC 6962 Merkle root:
  `sha256:a62815f9597df3500e275b1a264776cef1cfcc80ac8b0b438be8f22c0c8b2505`.

An adversarial audit found that the baseline is mathematically correct but not
yet safe or broad enough for solver evaluation:

- for the pinned `public-10000-regression` seed, only 4,039 distinct problem
  bodies occur; 5,961 records repeat a problem;
- the current problem serialization exposes answer, witness, and parameter data;
- both validators ignore the prompt, stated answer, and solution conclusion;
- malformed JSON and manifests lack depth, size, and generation-count budgets;
- identifiers bind generation coordinates rather than record content;
- provenance is unstructured free text; and
- one declared fault class is never generated.

These findings supersede any reading of “10,000 records” as “10,000 distinct
problems.” A separate hardening task is repairing the solver boundary and input
budgets before the breadth expansion or paired evaluation.

### Benchmark trust-boundary hardening

Commits `779c48e` and `9762e58` close the stop-run security findings without
claiming that the five-family bank is already broad enough:

- solvers receive only an immutable, size-bounded prompt and numbered solution;
- prompt, answer, witness, conclusion, both variants, fault, and repair are
  bound into a content digest and deterministic coordinate replay;
- item identifiers have a fenced v2 namespace;
- exact-fraction evaluation has depth, node, integer, numerator, denominator,
  and power-preflight budgets;
- fault labels and descriptions, provenance, license, and generator-source hash
  must match trusted deterministic regeneration; and
- malformed Unicode is converted to a stable boundary error.

Independent replay rejected same-family coordinate transplantation, fault
relabeling, self-asserted provenance, a multi-million-bit power expression, and
unpaired Unicode. A 120,143-byte solver view round-tripped inside the aggregate
budget. The combined main-branch verification passed 155 tests with 3
platform-specific symlink skips; 53 tracked files produced zero privacy
findings and the secret scan was clean.

The remaining breadth defect is explicit: the current deterministic generator
still lacks the fourth declared fault mechanism and still repeats semantic
problems. A collision-free balanced generator is being built on top of this
accepted boundary before any confirmatory evaluation.

### Local mathematical audit

- Explicitly allowlisted roots: 5.
- Files discovered: 1,168.
- Eligible for local review under the strict policy: 636.
- Quarantined under the strict policy: 467.
- Unsupported: 64.
- Oversize: 1.
- Proof-gap markers requiring contextual review: 2.
- Parse failures: 0.

The original 575/527 classification came from a legacy runner that reused path
category words as prose filters and recorded one racy read. The migrated runner
separates path and content policy, reads through the stable-descriptor gate, and
records every discovered file. It wrote an immutable 1,168-record local
manifest, then a second full pass verified all three output files byte-for-byte
instead of replacing them. The strict local manifest digest is
`05f34ed7ce3983b8482291ddd18104e465460d6d2fd052de30dbabf018cb332e`.

One existing mathematical release candidate contains an infrastructure-role
label in 457 verification records, 3,301 occurrences total, confined to two
runtime-host fields. The label belongs to an excluded operational domain. No
literal label or affected record was copied here. Those records are blocked
from publication until the field is removed or replaced with a neutral,
non-identifying execution-class label.

The strict scanner independently blocks that candidate: 459 files contain
absolute-local path material and 458 contain an excluded category marker. No
credential-shaped finding was emitted. These are aggregate local-only findings;
matched values and private paths remain outside the tracked repository.

The audit initially reported two Python syntax failures. Independent
reproduction showed that the parser, not the source, was wrong: it had not
handled an initial UTF-8 BOM as Python's normal file loader does. The auditor
was corrected and the full scan rerun before these counts were recorded.

### Proof-level audit results

Four independent proof audits deliberately separated verified reductions from
completion claims:

- The finite-group model's central local-order implication and algebraic
  obstruction survived; a uniform-buffer quantifier and one theorem citation
  need repair before the strongest wording is justified.
- The ReLU reduction remains conditional, but positive-sphere duality fails for
  all-negative vectors and a radial threshold was overstated as a global
  Lipschitz statement.
- The same-map work is a useful partial ledger, not a completed proof. An exact
  positive two-by-two matrix refutes the claimed monotonic envelope equivalence,
  and the fixed-depth and quenched limits must remain separate conjectures.
- The Ising/perceptron moment reduction, inball, localization, and near-one
  closure survived independent canaries. Its evidence bundle mixes two verifier
  generations, however, so it remains strong source-bound evidence pending one
  frozen release manifest and a fresh full numerical replay.

No local manuscript text or private path was copied into the tracked
repository. Detailed line-level findings remain under the ignored local audit
tree.

### Bound human formalization-fidelity authority

The local Lean checkpoint now has a separate human-review companion rather than
a caller-authored fidelity flag. The review artifact binds the immutable claim
and prose hashes to the sealed Lean result, exact source tree, ordered declaration
names, stable-read file hashes, and exact line-span hashes. Issuance reopens and
rechecks those bytes, requires every semantic checklist dimension, signs through
the fixed human-review role, and emits no evidence on claim, reviewer, source,
span, declaration, or checklist substitution.

The automated Lean and human fidelity authorities cannot share key material, and
neither network access nor marginal API cost is representable in either authority
attestation. The focused Lean/verification regression passed 71 tests. The full
serial suite passed 507 tests with 5 expected skips and only the explicitly
compute-gated 10,000-item benchmark deselected. A nonpersistent real-Lean 4.30
canary accepted `MathBrain.nat_add_zero`, issued the synthetic human-review bundle,
and verified its receipt with no network use or marginal API cost; its temporary
snapshot was removed. This is an implemented authority boundary, not evidence
that any private theorem has already received a human fidelity review; production
and ProofSwarm promotion gates remain closed.

## Open work at this checkpoint

- Complete the collision-free 10,000-item breadth expansion with all four
  structurally certified fault mechanisms.
- Replace the exploratory evaluation code with a sealed, exact-cardinality
  design whose repair and witness scores come only from replay receipts.
- Complete proof-level and citation-level reviews of the allowlisted local work.
- Run and score at least ten blinded matched solver pairs.
- Preserve a reviewed 10,000-record artifact and manifest under `data/public/`.
- Finish independent privacy, security, reproducibility, and mathematical
  red-team reviews before any public-release decision.
