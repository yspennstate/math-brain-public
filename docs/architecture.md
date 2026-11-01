# Architecture

The system is organized as a sequence of independently auditable layers.

```text
explicit allowlist
      |
      v
privacy + provenance gate -----> quarantine (default)
      |
      v
structured mathematical records
      |
      +--> typed association/dependency graph
      +--> immutable claim/evidence ledger
      +--> mistake patterns and review triggers
      |
      v
verification router
  | numeric | symbolic | proof | Lean | citation | statement fidelity |
      |
      v
status promotion with scoped evidence
      |
      v
replay/consolidation: contradictions, stale claims, graph orphans, new tests
```

## 1. Privacy and provenance gate

Ingestion is deny-by-default. A strict run-local TOML manifest grants individual
source roots, never the home tree. The reader rejects symlinks, junctions, and
hardlinks, opens a stable descriptor, compares identity before reading, and
revalidates containment afterward. All derivations remain under the manifest's
gitignored audit root.

Publication is a second gate. Every public data artifact has a provenance
sidecar recording its hash, rights, concrete license, public source identifiers,
and human review. A context-aware scanner rejects local paths, credential
patterns, and forbidden categories without echoing matched values.

## 2. Structured records

The core record types are claim, definition, theorem, proof attempt, example,
counterexample, source, citation, error pattern, verification result, and open
question. Records use stable identifiers, schema versions, timestamps, and a
canonical content hash.

The overlay represents one mathematical object with a stable logical identifier
and any number of immutable content-derived revision identifiers. Changes to a
statement, assumption, quantifier, scope, provenance, evidence set, or disposition
therefore create a new revision instead of rewriting history. Revisions may be
`unverified`, `provisional`, `conditional`, `verified`, `gap_found`, `refuted`, or
`retracted`; promotions still require the ordinary evidence gates. Every revision
also has a deterministic UTF-8 Markdown object under a SHA-256 path. Its graph node
stores that artifact path and digest, exact source revision, trust class, and
statement-fidelity flag. Trust class is provenance metadata, never evidence by
itself.

Bulk ingestion uses a typed, content-addressed `MathKnowledgeBundle`. A manifest
contains one immutable revision per logical object plus explicit endpoint-scoped
relations. Its digest is independent of entry order and ingestion time, but binds
the complete revision payload, provenance, relation rationale, weight, and metadata.
Bundles are bounded by entry, relation, and rendered-text limits. Every endpoint,
supersession target, logical identity, and new dependency/supersession cycle is
validated before any object is appended. Markdown objects are written first to the
idempotent SHA-256 store; all graph nodes, claims, and edges then enter SQLite in one
transaction. A failed database append can therefore leave only harmless immutable
objects, never a partial knowledge graph. Exact bundle replay fails explicitly under
the append-only contract.

The append path remains dark unless a cross-bound release manifest is approved. That
manifest binds an allowlisted, stable-read, acyclic transitive source closure; exact
statement and proof slice hashes plus locators for every entry; the allowlist,
builder, ProofSwarm parser, MathBrain package, toolchain, and normalization digests;
an independent review receipt; the exact database schema and pre-append state; and
explicit prior-release retirement pointers for every supersession. The transaction
rechecks the database seal under an immediate SQLite write lock. It persists the full
bundle/release manifest and member index beside the claims and edges, so a graph can
never outrun the source and executable configuration that produced it.
An `approved_by` string is not authority. Before any filesystem write, the trusted
runtime verifies an HMAC-SHA-256 receipt over the complete release payload using a
separately configured key; the key is never accepted from or persisted with the
bundle. A fabricated reviewer, receipt digest, component pin, or approval MAC leaves
the gate dark.
Bulk ingestion always creates `unverified` revisions. Source, parser, proof-text, and
review hashes establish origin and reproducibility; they do not establish mathematical
truth. Provisional, conditional, verified, refuted, or retracted status must come from
the separate authenticated evidence/derived-status path and cannot be supplied by a
bundle author.

## 3. Typed graph

Edges have mathematical meaning: `depends_on`, `defines`, `proves`, `refutes`,
`generalizes`, `specializes`, `analogous_to`, `cites`, `verified_by`,
`fails_under`, and `triggers`. Retrieval combines lexical matches with bounded,
typed graph spreading. Negative edges such as `refutes` and `fails_under` are
first-class so a nearby warning cannot be averaged away as mere similarity.
Every edge also carries a polarity consistent with its type. Retrieval propagates
positive support and negative warning paths in separate channels. A negative
path has a negative signed trace while receiving a positive surfacing score, so
it is visible without being mistaken for evidence supporting the recalled claim.

Retrieval indexes three deterministic signal families: Unicode-normalized words,
abstract mathematical tokens, and SHA-256 fingerprints of notation-normalized,
alpha-renamed formulae. Results expose per-term and per-edge contributions.
The decision API abstains when nothing is indexable, no candidate matches, support
is too weak, or the top match is too ambiguous. Evaluation callers use a
fail-closed split guard; records without an allowed split label are unavailable.

Discovery mode may diffuse through analogies, semantic associations, historical
revisions, and cross-brain bridges. Proof mode excludes those relations and follows
only directed exact edges. The exact dependency-closure API is stricter still: it
uses only directed `depends_on` edges and rejects reachable missing nodes or cycles.
This prevents embedding similarity or broad association scores from silently
becoming proof premises.

The math store remains independent of the main brain. A cross-brain link terminates
at a deterministic local `external_reference` proxy joined by `bridges_to`; writing
a reciprocal main-brain edge is a separate coordinated mutation. Association
events can aid discovery, but have no path back into evidence or truth promotion.
Bundle ingestion enforces that boundary structurally: an `external_reference` proxy
may only be the target of `bridges_to`. It cannot be used by `depends_on`, `proves`,
`defines`, or any other mathematical relation, so cross-brain diffusion cannot become
an unstated proof premise.

## 4. Verification router

Claims are decomposed into obligations. The router selects evidence appropriate
to each obligation and preserves the distinction between:

- arithmetic reproduction;
- symbolic identity checking under explicit domains;
- randomized or exhaustive finite testing;
- human proof review;
- formal proof checking;
- formalization-fidelity review;
- citation entailment and locator review; and
- independent reproduction.

No single verifier is universal. Promotion rules require coverage at the claim's
actual scope.

Evidence rows alone are never promotion authority. A trusted runtime verifies an
HMAC receipt that binds the exact evidence digest, immutable claim digest, kind,
nonce, artifact, source post-hash, verifier, toolchain, authority key, and fixed
authority role, together with the exact authority-attestation digest.
Receipt nonces are unique, and the evidence, attestation, and receipt are one atomic
append.
Human fidelity, automated checking, and independent reproduction use distinct fixed
roles; a key configured for one role cannot sign another role's evidence kind, and
two authority IDs cannot alias the same key material.
Every claim row, including a direct single-claim append, must enter as `unverified`.
Unauthenticated evidence is retained only as a discovery association; it cannot create
`verified_by` or `refutes` proof edges. Authenticated checks that fail likewise remain
associations rather than acquiring proof-edge semantics.

A receipt is not allowed to float above caller-authored runtime metadata. Every
receipt must bind a separately stored typed authority attestation. The attestation
binds the exact claim, evidence, artifact, request, result, verifier, toolchain,
source, and execution-environment digests plus the authority role and nonce. Its
mode is fixed by role: local automated run, local human review, or local independent
reproduction. Network use and nonzero marginal API cost are unrepresentable at this
boundary. Attestation, evidence, and receipt are one atomic append, and status replay
requires a complete matching triplet.

Lean authority is a concrete producer of that triplet, not a caller-authored label.
It stable-reads and snapshots a dependency-free local module graph, invokes only the
direct hash-pinned Lean executable from the exact installed toolchain, compiles every
module with trust level 0 under bounded hidden process-tree containment, and checks
fresh compute-governor state throughout. Authority additionally requires one
canonical source-side and output-side no-axioms report for every named declaration.
The execution result is sealed in process; the key-owning issuer signs only a fresh,
eligible seal and binds it to the immutable claim digest. Lake, Elan proxies, injected
process factories, unpinned executables, and unsigned serialized results cannot issue
`lean_kernel` evidence.

Formalization fidelity has a separate concrete human authority. Its review binds the
immutable claim and prose hashes to the sealed Lean result, source tree, ordered named
declarations, source-file hashes, one-based line locators, and exact statement-span
hashes. Issuance stable-reads the project again and recomputes every source binding;
source drift, claim substitution, declaration substitution, reviewer-key mismatch, or
any false checklist dimension produces no evidence. The human authority uses the fixed
local-human-review role and a distinct key from the automated Lean authority. Notes are
part of the signed artifact but cannot convert a failed checklist answer into a pass.

ProofSwarm tickets cross a separate strict parser with fixed byte, item, text, JSON
depth, and node budgets; duplicate keys, non-finite numbers, unknown schema fields,
unbound evidence hashes, nonzero cost, claim mismatch, or source-tree mismatch fail
closed. Even a ticket reporting `lean_verified` or `disproven` produces only a
dedicated `discovery_report` record. No authority key policy can authorize that
kind, even if a caller flips its result flag. It can never manufacture an authority
attestation or receipt; a trusted local verifier must rerun the exact artifact.

Direct verification-event insertion is disabled. The only status path acquires an
immediate write lock, reloads and re-authenticates evidence, deterministically applies
the scope-aware policy, requires distinct authorities for multi-evidence verified
routes, and writes an event plus real evidence foreign keys in one transaction.
Status reads replay every event and recompute its rationale, evidence set, transition,
and authority separation. A caller-authored or database-tampered persisted verdict is
therefore an error, not a status.

## 5. Mistake memory and triggers

An error record stores the minimal failing step, cause, counterexample or repair,
affected assumptions, and a reusable trigger. Triggers are specific review
actions (for example, “division: prove denominator nonzero”), not vague reminders.
Their precision and measured lift are tracked; noisy triggers are revised.
Structured mistake records preserve a minimal failing step, cause, affected
assumptions, counterexample, repair steps, and prevention action. Reflex records
pair explicit activation cues with ordered actions, required evidence, and a
stop/abstention condition. Their graph links are typed negative warning edges;
neither record changes claim status.

## 6. Mathematical consolidation

A consolidation cycle does not invent facts. It replays verified and failed
work to propose bounded tasks: contradiction checks, missing-edge checks,
counterexample searches, stale-citation reviews, proof compression attempts,
and benchmark mutations. New claims remain unverified until ordinary gates pass.
Slow-wave-style replay prioritizes contradictions, missing evidence, graph
orphans, hub audits, and concrete reflex rehearsal. REM-style association uses
only abstract formula structure to suggest bounded analogy reviews. Both phases
return deterministic `quarantined` proposal objects. The proposal type rejects
truth-promotion capability and deliberately raises if treated as evidence.

## 7. Evaluation

The benchmark runner pre-registers seeds, item strata, solver budgets, and
metrics. Brain-on and brain-off conditions are paired and blinded. Primary
metrics include fault localization, fault classification, corrected conclusion,
false-positive rate on clean solutions, calibrated confidence, latency, and cost.
