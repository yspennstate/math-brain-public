# codex-20h-audit-2026-09-07: a twenty-hour audit of the proof hook and the store's proof notes

A Codex agent spent 7 and 8 September re-deriving two earlier results from their rows by a second code path, then read
every note the proof hook can serve. The two follow-up lanes of 8 September (retrieval and the proof gate) are folded in.

## The two results it reconstructed

| test | brain on | brain off | n | p |
|---|---|---|---|---|
| proof hook, flawed-proof pairs, all tiers | 63 | 53 | 74 | 0.006 |
| proof hook, hard tier only | 25 | 21 | 33 | 0.125 |
| agentic lookup (the solver may query the store) | 36 | 37 | 67 | - |

The pooled p comes mostly from the easier tiers; on the hard tier the difference is four items. The two runs used
different models, samples, tools and hook versions, so neither row says which part of the hook did the work. The
lookup row is the run archived in `../agents100-2026-09-07/`. Besides the roughly 95 queries that ran there, 20 more
died on a console encoding error, and the notes the agents read were mostly harvested statements rather than the
curated proof-audit notes, so that null says little about the curated layer.

A small component pilot (12 items, five arms, one model) gave 5 correct with no notes, 7 with the inventory alone, 5 with
retrieval alone, 7 with the hook as frozen and 9 with the corrected hook, which also raised no false alarm on a clean
proof where the frozen hook raised two. Twelve items is a pilot, not a measurement.

## What was wrong in the store

Twelve stored notes were mathematically wrong or stronger than the theorem. Each was shown wrong by a counterexample. Among them:

- Chernoff, lower tail: the signs were reversed (X = -1 gives P(X <= 0) = 1 > 1/2 against the stored bound).
- Dominated convergence was said not to give E|X| finite; it does, from the dominating function.
- Modes of convergence: a summable rate and an integrable dominator were stated as necessary; each is only sufficient.
- Portmanteau: uniform integrability was called necessary for convergence of means. X_n = +n^2 or -n^2 with probability
  1/(2n) each, else 0, converges in law to 0 and E X_n = 0 for every n by symmetry, while E|X_n| = n.
- A density was said to need an integrable characteristic function. The uniform law on [-1, 1] has a density and its
  characteristic function sin(t)/t is not integrable.
- Fubini and Tonelli: "no absolute integrability, so the swap is wrong" fails on the infinite array built from diagonal
  2 x 2 blocks with entries +1/n and -1/n: it is not absolutely summable, yet both iterated sums are 0.
- Holder: the note refused exponents 2 and 3. On a probability space 1/p + 1/q <= 1 is enough; on a space of mass M the
  bound carries a factor M^(1 - 1/p - 1/q).
- A limsup on the small side of an inequality was said to need the limit to exist; (-1)^n shows it does not.

`corrections.jsonl` holds each changed note before and after.

The hook's own wording had three faults of the same kind: it told the solver a flawed proof is wrong "in exactly one
step by one token" (a property of the test bank, not of mathematics), it treated a failed tactic as a counterexample (the
same true statement fails under a weak tactic and closes under `rfl`), and it cut each note at 560 characters, which
truncated 167 of the 197 notes it served. The inventory of steps was cut at 6,000 characters and only read one- and
two-digit step numbers.

The Lean checker reported a pass on a proof containing `sorry` (Lean only warns) and on a file that declared a false
axiom. It now refuses both and prints the axioms a target depends on, accepting only `propext`, `Classical.choice` and
`Quot.sound`; against the real compiler a true statement passes, a false one fails and a `sorry` fails.

## Files

`corrections.jsonl` the twelve corrected notes, before and after.
`lean_checker_gate_2235/` the checker's controls before and after the fix: each input, the generated check file and its
receipt.
`f002_recovered_20260908/` one row of the proof extractor recovered and re-checked. The row was accepted although its
statement covers dimensions four and five and the extracted proof finishes only one of them. The folder holds the two
recovered copies of the row, the frozen extractor that accepted it, and the scripts that recovered and sealed the
check. The source is arXiv 2608.23135v1; its text is not copied here.

The lookup run's per-item requests and verdicts are not included, for the reason given in the agents100 archive. Local
paths in the files are replaced by `<HOME>` and `<BRAIN>`. The tools named here (`lean_check`, `proof_receipt`,
`math_sense`) are in `framework/`.
