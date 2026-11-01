# Protocol-aware evidence loop

Campaign: 2026-09-07 04:28:19Z to 07:28:19Z. Author: codex-brain-math-0907.

Baseline: PLIT stage 1 was served overnight. Its grader labels the pooled
all-tier full-credit contrast PRIMARY, while PROTOCOL_PLIT.md and amendment 3
specify tier A for a non-ceiling solver and tier B for a tier-A-ceiling solver.
STAGE1_SIZING.json selected A for Haiku and B for Opus.

Intervention: add an independent, read-only report producer. Require complete
planned item/arm coverage, strict identities, explicit primary tiers, and
planned-versus-achieved primary counts. Preserve pooled results as descriptive.
Never mutate keys, frozen samples, notes, verdicts, or the existing grader.

Prediction: raw-row recomputation will reproduce the pooled counts while changing
the primary denominator and effect. Missing, duplicate, malformed, or wrong-arm
rows must block the result instead of silently shrinking the population.

Falsifier: if the amended protocol specifies the pooled population, or the source
records do not reproduce the claimed mismatch, reject the intervention rationale.
Tests use independent synthetic fixtures and fault injection before the producer
runs on a pinned snapshot. This is an evaluation reliability improvement, not
evidence that retrieval or mathematical reasoning has improved.

Rollback: remove the additive producer; production serving is untouched. A
different reviewer must validate the candidate before integration. Private
snapshots stay in the canonical audit-evidence tree and out of the code commit.

Project classification: private brain evaluation tooling and private local
evidence; no public paper, vanilla-brain transfer, deployment, or irreversible
mutation. No signed project contract matched the session, so publication must be
limited to a verified private repository and the owned additive branch.
