# Probability: 1,000-problem research campaign

This is a single-agent research campaign, not a claim that 1,000 open problems have been solved.

- Start: 2026-09-06T15:13:26Z.
- Deadline: 2026-09-07T11:13:26Z (14:13:26 Jerusalem).
- Mandate: find 1,000 genuine, distinct, sourced open problems in probability; check later literature; attempt each; preserve proofs, counterexamples, failed routes, and exact obstructions; produce a substantial PDF and build the probability math brain.
- One agent performs the work. No delegated solvers or reviewers. Author checking is never called independent review.

## Evidence model

`sources.jsonl` records source acquisition and exact locations. `problems.jsonl` records mathematical statements and status evidence. `attempts.jsonl` is append-only and records mathematical work, including unsuccessful work. `STATUS.json` reports actual counts. `RESUME.md` names the exact next work after an interruption.

A candidate URL is not an acquired source. A numbered exercise is not an open problem. A source's historical open label is not a verified present-day status. No finite experiment proves an unbounded claim. Splitting a parameterized question into many values does not create distinct corpus entries.

### Independent status axes

1. Source status: candidate, acquired, extracted, statement checked.
2. Historical status: source explicitly says open/conjectured, or not established.
3. Current status: unverified, no resolution found in documented search, resolved in later literature, disputed.
4. Attempt status: not started, partial attempt, proof candidate, counterexample candidate, obstruction documented.
5. Verification: unreviewed, author checked, independently reviewed, formally checked with separate statement-fidelity review.

The final PDF must report incomplete coverage directly. Known results belong to the literature-resolved appendix and do not count as original solutions.

## Research loop

For each admitted problem: state its assumptions and quantifiers; inspect later literature; attempt a construction or proof; challenge the key step with boundary cases and adversarial examples; identify the first unresolved obligation; record the result and dependencies. Revisit promising attempts after the first coverage pass.

## Math-brain intervention

Baseline: the new campaign has no source-checked corpus entries or retrieval receipts. Intervention: add typed, provenance-bound probability claims, dependencies, counterexamples, and failed routes through the existing math-brain interfaces. Prediction: realistic analogous queries retrieve the intended assumptions and obstruction without promoting conjectures to theorems. Stop promotion when statement fidelity, provenance, or a retrieval control fails. Rollback consists of retaining failed candidates in quarantine and withdrawing an unsupported promotion; evidence history remains intact.

No public release is authorized. Source PDFs are kept in the local Downloads research folder; the repository stores authored research, metadata, and reproducible tooling.
