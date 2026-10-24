# Research-status recall: tested diagnosis and sealed-study design

OWNER VISION READ: OWNER_BRAIN_VISION_2026-09-27.md blob cb08c84b885b31a3da15f0a4c542587b316b50b2 - I read all of it, I will act on it, and this run audits the brain from this perspective.

## FOR THE RECALL BUILDER - R80

Finding DOT-R80-STATUS-ABLATION-20260930. Severity: medium for evaluation validity.
This is an interactive, dot-scoped engineering diagnosis, not a scheduled worker
invocation. No worker settings, other projects, live stores, or production ranking
behavior were changed. It does not extend the scheduled auditors' permissions.

### Result: two traps in a lexical versus graph comparison

VERIFIED on the actual Python retrieval implementation with original synthetic
fixtures: neither removing every edge nor setting only graph_depth=0 gives the
intended matched graph-off comparison.

1. Removing every edge also removes SUPERSEDES relations. That changes which
   immutable records are eligible before ranking. In the two-record fixture, the
   current revision alone is served in both fair arms; removing edges resurrects
   the prior scope assertion. This can falsely attribute version filtering to
   graph diffusion.
2. graph_depth=0 prevents traversal but still adds zero-hop seed retention. At
   default decay 0.55, that can reverse the top result even when there are no
   edges. Source documentation does not promise that depth zero is graph-off,
   so existing runtime behavior is deliberately preserved.

The new replay helper sets **graph_depth=0 AND decay=0** for its surface-only
arm, retains the exact same edges and guards, and disables external semantic,
expansion and signal-store inputs. The comparison arm uses depth 2 and decay
0.55. In this fixture, surface means lexical/formula channels, not pure BM25.
Retrieval eligibility is identical; graph and warning scores are zero in the
surface arm. Candidate and proof status are never promoted by retrieval.

This is a tested evaluation improvement, not a demonstrated live recall gain or
a finding that the production ranker's intended contract is wrong.

### Pinned runtime and reproduction

Source revision: 55151291e9e69f3b44eb79b3b092ac8d2862fe25 on the builder branch.
Direct runtime modules fetched at that immutable revision:

- src/math_brain/retrieval.py: d156535918e471745b06bf0fd53b6e325fada8e4
- src/math_brain/models.py: 3261c8abbd58f0e77922f294397c1dfa9f51793f
- src/math_brain/semantic.py: 5696bf4cd88d429db477ed3684a622d57785a6c3

The remaining package import scaffolding came from an earlier materialization.
This is a scoped execution of these pinned retrieval modules, not a claim that
the entire repository checkout or live installation was reproduced. NumPy was
available in the test environment. The separate optional-dependency change was
not applied or modified in this experiment.

Relevant retrieval.py locations at that revision: current_revision_nodes
1104-1122; traversal cutoff 1170-1171; seed retention 1225-1250; eligibility
before ranking 1314-1318; graph propagation before title bonus 1401-1423.

Run from a checkout with development dependencies:

    MATH_BRAIN_SEMANTIC=0 python -m pytest tests/test_research_status_ablation.py -q
    MATH_BRAIN_SEMANTIC=0 python tests/test_research_status_ablation.py

The script prints a schema-versioned, content-hashed JSON result; the committed
example is docs/research-status-probe-results.json. All source and edge
availability times in the fixtures are explicit and timezone-aware. Missing or
ambiguous availability fails closed. Creation time is not used as evidence of
availability, so a backdated future revision cannot enter an earlier snapshot.
The helper is a test harness, not an authenticated provenance service: a real
export must independently attest those times and freeze the bytes.

### Exact rank-reversal witness

The complete three synthetic records are in
test_surface_arm_avoids_depth_only_seed_retention_rank_reversal. The query is
`revision delta delta measure variance`; no edges exist. At depth zero:

- Node 0: surface 1.6759665985975332, retained graph 0.18121887640954773
- Node 1: surface 1.6334247806080422, retained graph 0.2994612097781411
- Node 2: surface 1.1144228439141977, retained graph 0.2043108547176029

Depth-only ordering is 1, 0, 2. Zero decay ordering is 0, 1, 2, with every graph
score zero. The title bonus is added after graph propagation, so retention is
not simply a common scalar applied to the final surface scores. These figures
diagnose a configuration confound; they are not a corpus performance estimate.
The witness was discovered by a fixed-seed synthetic search, not held out.

### Executed checks and controls

23 cases pass. Controls cover explicit correction in both arms; removal of
revision links; missing links despite later dates; future node and edge cutoffs;
backdated creation; hidden answer-key, evaluation-split, quarantined and solution
records; identical eligibility, snapshot and budgets; order invariance;
abstention; a positive graph-neighbor control; changed-text digest detection;
and refusal of missing or malformed availability. Both arms have a two-hit,
2,048-byte delivered-text ceiling. Returned bytes are measured, not called
solver tokens. There is no solver or grading key in this executed probe.

The prior depth-only helper fails the zero-graph-mass and rank-equivalence
regressions. Production source bytes remain unchanged. Ruff passes the new
test file. These are focused tests, not an all-repository green-suite claim.

### What this establishes about stale mathematical status

VERIFIED: explicit eligible revision relations suppress the old assertion in
both arms. Dates alone do not infer correction links. INFERRED: a missing
source, missing relation, or stale status summary can survive independently of
graph weight. UNTESTED: whether the actual owner store contains the later
research sources and correct relations, whether any live hook fires them, and
whether an agent uses them correctly. We did not query the live owner store.

Two known mathematical discovery failures are development cases, permanently
excluded from any confirmatory holdout: the September 16 C005/C006 full-scope
free-unimodality candidate missed by an older campaign summary, and a September
20 exact mismatch-KL refinement rediscovered only after exploring a weaker
route. The first source report still labels its wider administrative status
audit-pending. A stronger theorem and completion of an audit protocol are
different facts. The second example is a parent-reported lead, not a separately
audited source in this probe. Neither is counted as a new experiment outcome.

Do not attach SUPERSEDES merely because a theorem is stronger: the weaker
theorem may remain true and useful. Correct obsolete status assertions with
their provenance; use GENERALIZES or dependencies for compatible mathematics.
Never convert an unaudited candidate to verified because it is recent.

## Confirmatory design: NOT RUN

### Freeze and split before inspecting outcomes

1. Inventory allowed mathematical source families and preexisting revisions in
   an immutable export. Record source bytes, source version, earliest evidenced
   availability, recorded observation time, node/edge identities, export digest,
   code/config digests and cutoff. Freeze preexisting learned edges and exclude
   all evaluation traffic. Backfilled old-looking events need availability
   evidence at the cutoff, not just an event timestamp.
2. Separate development, pilot and holdout by source family, including aliases,
   derivative notes and copied proofs. Exclude the two cases above and every
   source seen while designing or tuning this test. Fix membership and ordering
   before outcomes; publish their hashes, not answer-bearing labels to solvers.
3. An independent author who cannot see retrieval rankings writes one natural
   question per held-out family. The task is to locate and accurately qualify
   the strongest applicable result available at the cutoff. Keep mathematical
   scope, author claim, independent audit, formal verification and publication
   state as separate fields in the hidden grading key. Keys and grading
   artifacts never enter retrieval. Genuine historical source documents may
   contain answers: those are the readable data being tested, not injected keys.
4. Key graders establish every expected locator and scope directly from the
   frozen sources. No test-driven alias, hand-written graph edge, new summary or
   gold-path expansion is added after questions exist. Explicit cutoffs also
   test that a later correction is unavailable to an earlier question.

### Arms, equal caps and positive/negative controls

- A: no data, no hooks, no standing source context
- B: same frozen readable sources, ordinary search/navigation, no brain
- C: same sources plus frozen brain; ordinary connected retrieval
- B-path: diagnostic oracle path to the correct source, no answer text; separate
  from the primary contrast because the path is privileged routing information
- Within C: matched surface-only and graph-plus-surface retrieval diagnostics,
  retaining version eligibility in both. Surface disables decay, semantic
  signals and external expansions unless those are separately registered arms

Use fresh solver contexts, the same served model and reasoning configuration,
same question and answering instructions, eight tool calls, 16 KiB cumulative
retrieved text, and the same enforced 4,096 output-token ceiling per item. Charge
brain injections against the same input budget; do not grant C free context.
Record model attestation, actual input/output usage, tool costs and latency.
All arms must be served under the same valid seal. Failures count as primary
first-attempt failures; retries and their costs are a separate sensitivity.
Randomize arm execution order with a sealed seed. Never silently mix model,
attempt, source snapshot or budget regimes.

The eight-tool and byte caps are proposals to validate on a disjoint pilot,
then seal; they were not used by live solvers here. A transport unable to attest
model identity or enforce the output cap makes the confirmatory run ineligible,
not evidence of no benefit. The builder's latest response reports exactly
those remaining strict-evaluation capability gaps.

Controls include unchanged-status families, valid narrow theorems alongside
stronger candidates, false premises about proof/publication status, absent
targets that should elicit uncertainty, irrelevant newer documents, future
corrections, renamed aliases, and forbidden answer-key records. The positive
control verifies a permitted graph connection can actually reach a source.

### Size, scoring, estimand and stopping rule

Primary endpoint: source-supported answer correctness, including scope and
status, in paired C versus B first attempts. Report current-source hit rate,
obsolete/unsupported status assertions, abstentions, citation precision and
resource costs separately. A retrieval hit is not answer correctness.
Two independent graders receive randomized, arm-blind answers; adjudicate
disagreements without revealing arms. Declare grading rubric and tie rules
before serving. B-path diagnoses routing; it is not evidence of reasoning gain.

Target at least 800 independent held-out source families, one question each,
if inventory supports them. For a paired 5-percentage-point improvement and
discordant-pair probability q <= 0.20, the normal planning approximation is
N >= (1.96 + 0.84)^2 q / 0.05^2 = 627.2; 800 leaves margin. This is an explicit
assumption, not an observed power guarantee. Use a disjoint B/A pilot to show
room to improve and a disjoint paired pilot to bound q, then lock sample size.
Worst-case q=1 needs about 3,136; never pretend 300 can always resolve 5 points.
If there are too few independent families, report descriptive uncertainty and
do not manufacture paraphrases as independent observations. Correlated source
families require cluster-level inference and a revised power calculation.

Estimate max output as 800 x 4 x 4,096 = 13,107,200 tokens for A/B/C/B-path,
plus input, retrieval and blind grading. Currency cost is unknown until the
authorized transport/model price is known. Do not launch paid calls from this
design. Stop only after every sealed primary slot is terminal and grading and
integrity checks complete, or a missing capability/authorization blocks it.
No optional stopping on interim wins. Use paired confidence intervals and an
exact paired test; label all extra contrasts secondary with multiplicity
handling predeclared. Benefit requires a positive primary interval, valid
integrity gates, and no predeclared unacceptable increase in false status
claims. If these fail, say not shown or ineligible as appropriate.

## OWNER VISION

Requirements 5 and 9: VERIFIED locally that graph-off and graph-on can be
compared without changing the eligible revision set; real delivery and use
remain UNTESTED. Requirement 6: the probe protects against repeat obsolete
scope assertions, but their real incidence is not measured. Requirement 8:
production diffusion and lexical behavior are preserved. Requirement 10:
the synthetic diagnosis is explicitly separated from a proposed held-out
benefit experiment. Requirement 11: no source history was deleted.

## BRAIN GRAPH

Source access and local retrieval execution: VERIFIED. Live full-brain
connection, hook delivery, builder consumption and user benefit: UNVERIFIED.
full_brain_connected: false. No deployment, merge or live-store ingestion.

Fresh coordination sources read: FOCUS_2026-09-27_RECALL_JOBS.md blob
9dab2a39da4c680df96ed7866c5dd127c65d6b2f; REPLIES_2026-09-27_RECALL.md blob
fac7ec6348c1c931861158b75e812514aa47eb4a; CLAUDE_SUPPORT_2026-09-27.md blob
4c25e4eab70d284b37c68c4779de0b50c6f73b41. The fresh replies were checked for
earlier disposition of seed-retention/depth-zero findings; none was found.
