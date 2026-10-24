# GU research checkpoint and bounded recovery inventory

Prepared 14 October 2026, 04:01 UTC. Private research coordination checkpoint. This file records the owner's latest requested objective and verified source locations. It does not claim a new proof, a completed fleet migration, or complete recovery of missing work.

## Owner-requested objective

The owner asked on 14 October to have the existing scheduled research tasks work on the FEI inequality previously identified, save their results in the private `yspennstate/math-research-brain` repository, and recover missing results where permitted. The current canonical order identifies that inequality as **GU**, the global restriction inequality for the upward functional U. The older September gate-potential programme is historical context, not the current target.

Continue existing authorized work and ownership. Preserve schedule timing, enabled state, end dates, resource limits and all applicable source/access/write restrictions. A request to recover results does not authorize rerouting an operation that was actually denied. Do not reconstruct held material through another writer or destination.

## Exact mathematical target

For a Boolean function f on the uniform cube, let p(S) = fhat(S)^2, pi(S) = sum_{T containing S} p(T), and I(f) = sum_S |S| p(S). Define

    U(f) = sum_{S:p(S)>0} p(S) log2(pi(S)/p(S)).

The empty set is included. Constants have U = I = 0 and require no division. Let f_{i,+} and f_{i,-} be physical coordinate restrictions, and set

    Delta_i U(f) = U(f) - (U(f_{i,+}) + U(f_{i,-}))/2,
    G(f) = sum_i Delta_i U(f).

The requested sufficient inequality is

    (GU) G(f) <= K I(f)

for every dimension and every Boolean f, with one finite dimension-independent K. A weaker sufficient target is G <= a I + b U with b < 1. The reviewed restriction-induction reduction yields U <= [a/(1-b)] I and H <= [2 + 2a/(1-b)] I. The existential form, a relevant coordinate with Delta_i U <= K Inf_i for every nonconstant f, also suffices. Do not replace these quantifiers by a demand on every coordinate.

The reviewed bridge is stronger than the convenient H <= 2I + 2U:

    H(f) <= 2(I(f) - Var(f)) + 2U(f) - p(empty) log2(1/p(empty)).

The exact local decomposition is Delta_i U = B_i - Gamma_i + K_i, with B_i the conditional spectral-coordinate entropy, Gamma_i = sum_{S containing i} p(S) log2(pi(S minus i)/pi(S)), and K_i a nonnegative binary-KL mixture. This makes the aggregate KL contribution a concrete remaining obstacle. None of these reductions proves GU.

## Source-grounded corrections to carry forward

These are reported results from already-persisted source documents. No code or certificate was rerun for this checkpoint.

1. The canonical ORDER still quotes an observed GU ratio of 3.09. Its accompanying independent referee reports larger numerical examples: maj5(g5) gives 3.2157, and maj5 with an annealed six-bit inner function gives 3.2265. Thus 3.09 is not a valid summary of the maximum already observed in this package. These are numerical discoveries, not a universal bound or a new certificate from this audit.
2. The finite n <= 4 fit G <= 2.25 I + 0.5 U fails off that finite test set, including on maj3(g5). Do not assign it as an established global lemma. The surviving tested fit with b = 1 does not meet the strict b < 1 induction requirement.
3. The referee proves equality in the full bridge above for read-once AND/OR formulas, including allowed negations. The weaker expression without the empty-set correction had obscured this exact equality.
4. The growing local ratios through n = 9 are evidence against the universal-every-coordinate approach; those finite numbers alone do not prove unboundedness.
5. September's reported seven-input G7 witness defeats two particular stored read-once potentials. It does not refute FEI or the current GU target. Do not resume the old claim that the AND constraint remains binding at every fan-in for those potentials.

## Immutable sources checked

Brain snapshot: `94f617e7755c87cf427d067bab3141776cb312b6`.

- [Canonical order and GU amendment](https://github.com/yspennstate/math-research-brain/blob/94f617e7755c87cf427d067bab3141776cb312b6/scheduled_tasks/work/shared/full-fei-only-2026-10-12/ORDER.md), blob `7c5e21945adef435e6b587909603dd96794a1ebe`.
- [U-universal notes, especially sections 5 and 7](https://github.com/yspennstate/math-research-brain/blob/94f617e7755c87cf427d067bab3141776cb312b6/scheduled_tasks/work/shared/full-fei-only-2026-10-12/gu/U-universal/NOTES.md), blob `3b0636c653c7818368eeb204011c3e1ff21c234e`.
- [Independent referee, especially sections 2.6 and 4.3–4.4](https://github.com/yspennstate/math-research-brain/blob/94f617e7755c87cf427d067bab3141776cb312b6/scheduled_tasks/work/shared/full-fei-only-2026-10-12/gu/U-universal/REFEREE.md), blob `87326516f71374bb2b37d593952be7ec581ee0f1`.
- [Historical September gate reformulation](https://github.com/yspennstate/math-open-problems/blob/73cc2c4a15c11a48483ee8971d90c9f7c303ac45/proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md), blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.
- [Historical G7 source report](https://github.com/yspennstate/math-open-problems/blob/73cc2c4a15c11a48483ee8971d90c9f7c303ac45/proofnet24/P03-fei/continuations/2026-09-22-opus-team/F3-small-arity/REPORT.md), blob `ffe2ebf3da040da16120bea05c8ccbf179967ed3`. It reports rigorous logarithm enclosures and negative defects for the two stored potentials; its checkers were not rerun here.

## Persistence audit: what is and is not established

- **Already persisted:** the canonical GU order, U notes, independent referee and route synthesis are readable in Brain at the pinned snapshot. This checkpoint cross-links their important corrections; it does not present them as newly recovered proofs.
- **Historical location discrepancy:** the September report's old Brain reference `06_math_research/fei_gate_reformulation_2026_09_22/` returned 404, and the current Brain root has no `06_math_research` directory. The accessible historical report remains in `math-open-problems`. The Brain `proofnet24` tree checked here has no FEI entry. These bounded checks do not prove that no equivalent copy exists elsewhere.
- **Not established:** a repository-wide absence/dedup audit, recovery of all unpublished results, completeness of any local working-machine files, or the current status of every worker. A root recursive-tree response was not available as parseable structured data in this audit.
- **Excluded from recovery:** peer results with unresolved or actual write/source restrictions, including the separately reported B09/B13 write-held work. No content from those results is reproduced or reconstructed here, and no alternate-writer path is proposed.
- **Scheduler blocker:** the coordinating session reports two unsuccessful native task-inventory attempts. No complete current native inventory or task-prompt update was established in this pass. Saving this file does not update schedules, prove adoption, or show that another worker read it.

## Next authorized work and saving requirements

Each existing worker should continue its own verified B/A stream and select one live GU gap from its actual assignment and latest checked results. Record the proposed inequality and quantifiers before testing. Grow a useful family or parameter; distinguish a finite computation, a certified witness, a conditional derivation, a proved class and an all-dimensional theorem. Review candidates against the stronger referee examples rather than only the old 3.09 example.

Use the canonical routes in the ORDER. Account01 run artifacts remain in `math-open-problems/reports/fei-2026-10-11/runs/Bnn/<unique-UTC-run>/`, with complete substantive Brain handoffs under `research_pushes/2026-10-11-full-fei-campaign/handoffs/account01/Bnn/<unique-UTC-run>/`. Other owners preserve their existing private namespaces and must not impersonate account01. A coordinator checkpoint is not a substitute for a substantive run.

For each permitted result, save the actual proof or partial derivation, exact statement, source pins, REPORT.md, CLAIMS.json, PROGRESS.json, compatible PACKET_DELTA.json, and the code, parameters, commands, outputs and certificates needed to reproduce any computation. State the unchanged obstruction and next step. Independently read back the committed artifacts and record their paths and commit/blob hashes before claiming that they were saved. Verify missingness and eligibility before a create-only recovery; do not overwrite peer results or recover a refused operation by rerouting it.

Full FEI and universal GU remain OPEN in the checked sources. A full candidate requires the canonical independent end-to-end review process; this source check is not one of those proof reviews.
