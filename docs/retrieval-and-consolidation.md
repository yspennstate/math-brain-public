# Retrieval and consolidation safety contract

This subsystem retrieves mathematical context and proposes follow-up reviews. It
does not decide mathematical truth. All examples and tests in the repository are
synthetic or elementary; no local research corpus is bundled.

## Retrieval signals

`index_signals` derives three in-memory channels:

1. Unicode-normalized lexical tokens;
2. abstract math tokens such as `op:forall`, `op:pow`, and `const:real`; and
3. SHA-256 fingerprints of notation-normalized, alpha-renamed formulae.

For example, `∀ y ∈ ℝ, y² ≥ 0` and
`\forall x \in \mathbb{R}, x^2 \geq 0` share the same mathematical signals.
Normalization is a retrieval heuristic, not symbolic equivalence or proof.

`retrieve` returns immutable hits plus a decision. Every hit separates lexical,
symbol, exact-formula, positive graph, and warning scores. Its trace records the
matched term or typed edge responsible for each contribution. Warning paths keep
a negative signed contribution but are given a positive surfacing score so they
cannot disappear inside an average relevance score.

The decision abstains with one of four explicit reasons:

- the query has no indexable signal;
- no corpus candidate matches;
- the best support is below the caller's threshold; or
- the best two candidates are closer than the caller's minimum margin.

`search` remains a compatibility wrapper that returns hits. New decision-making
code should call `retrieve` and must check `abstained`.

## Evaluation contamination guard

An evaluation must pass a `RetrievalGuard`. The guard is fail-closed when split
labels are required. It excludes:

- records outside the allowed training/reference splits;
- answer keys, solutions, fault annotations, and prior evaluation output;
- the active benchmark item and its paired variant;
- records sharing a prohibited source digest; and
- quarantined or denied records.

Filtering happens before scoring and graph propagation. Exclusions are returned
as structured reasons. The same guard is applied before consolidation, so a
test answer cannot re-enter through a dream-generated association.

## Signed mistake memory

`MistakeRecord` captures the exact failing step, cause, repair, affected
assumptions, optional counterexample, and prevention action. `ReflexRecord`
requires activation cues, ordered actions, required evidence, and a stop
condition. `memory_edges` links them with `fails_under` and `triggers` edges,
whose polarity is structurally negative.

## Quarantined replay

`consolidate` is a pure function. Slow-wave-style replay turns graph defects and
documented failures into specific review actions. REM-style replay compares only
abstract formula signals and may suggest an analogy review. Every result is a
deterministic `ConsolidationProposal` whose only allowed status is `quarantined`
and whose `can_promote_truth` value is always false.

A proposal is not `Evidence`, is never written as a verification event, and has
no promotion method. Attempting to treat it as verification evidence raises an
error. A human or independent verifier must perform the proposed action and feed
the resulting artifact through the ordinary evidence and promotion gates.

`math_brain.nightly` runs `consolidate` once a night against a read-only store
and keeps the proposals in a review queue, so a proposal that keeps coming back
unattended is visible as such; see [nightly-pass.md](nightly-pass.md). The
requests that prompted the work are kept as nodes of their own and consolidated
in the same pass; see [prompts-as-nodes.md](prompts-as-nodes.md).

## Where recall time goes

These measurements were taken in late October 2026 on a store of about 87,000
records, with the 100-question recall bank.

Re-ranking what the query words already found does not pay. Four changes were
tried on the same bank: spreading one hop along the 76,000 deterministic links
added that month, down-weighting records reached in two hops, dropping weakly
connected records from the frontier, and capping how many session summaries one
session may contribute. Each moved the score by zero or one question. The
wording of the query sets the ceiling, and the walk only re-orders what it found.
Asking in two or three wordings in one call remains the change that moves the
score.

The time is in the prepared state. A call that rebuilds its index takes
minutes, and a call that opens a prepared index takes seconds. The prepared
index carries a stamp of the store's state, and an early version accepted only
an exact match. On a busy machine the store's write-ahead log moved every minute
or two, no prepared state ever matched, and every call rebuilt, at 200 to 380
seconds a call. Accepting a prepared state up to 45 minutes old brought calls to
24 to 60 seconds. The price is that a record written since the last build cannot
be found until the next one. The remedy is a small side index of recent records
searched alongside the prepared one, not a faster full build.

A recall tool that starts slowly is missing. In one run of the test that
compares agents with and without the store, the recall server took long enough
to start that the agent never saw the tool, and those questions were answered
without the store. Starting the server ahead of time, or running the search
inside the calling process (about five times faster per call than starting a
new interpreter for each call), removes that loss.

Printing less is cheaper but not yet shown to be as good. A listing with the
title, a short id and the matched words for each hit used seven to eight times
fewer tokens at the same wall time. Whole cards scored 83 of 100 against 34 for
snippets on the bank, so a short listing helps only if the agent then reads the
cards it picks with `--id`.
