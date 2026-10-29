# A literature proof bank outside probability, 6 September 2026

A sealed fault-location bank built from published proofs in analysis, algebra, number theory, combinatorics,
geometry, topology, logic and learning theory. It is the sibling of the probability literature bank used in
`agents100-2026-09-07` and shares its item shape, runner and scoring rule. The bank was built, sealed and
checked for validity. Its powered comparison was never served, so it has no brain-against-control result.
The twenty proof audits in `papers/pseudo-cognitive-dynamics-2026-09-23` were drawn from it.

## Question (pre-registered)

Does a solver given notes from the math store find the one changed step of a research-level proof more often
than the same solver without notes, more often than with notes of matched kind and bulk about a different
proof, and less often than a solver given the paper's own other statements?

## The bank

4,208 theorem, lemma, proposition and corollary proofs were extracted from the LaTeX sources of 578 arXiv
papers. 55 were excluded because their paper also appeared in the probability bank's listing. 4,144 items
remain, one per distinct proof: 2,894 carry exactly one changed step and 1,250 are the proof as published.

| domain group | items |
|---|---|
| analysis (math.AP, math.FA, math.CA) | 1,018 |
| algebra, number theory, combinatorics | 1,306 |
| geometry, topology, logic | 1,363 |
| learning theory (stat.ML, cs.LG) | 457 |

Each change is one of eighteen mutation operators drawn from an eleven-class taxonomy (sign flip, inequality
direction, quantifier swap, a dropped or swapped hypothesis, an index or reference shift, an unjustified
interchange of limits or sums, an extremum swap, a set-operator swap and others). Operators carry a prior tier
on whether the changed proof is really invalid: tier A 1,513 items, tier B 1,381. A fixed heuristic rates
difficulty: 1,092 easy, 1,413 medium, 389 hard. The items file carries no paper id, domain, operator or step
marker, the notes builder never reads the keys, and the keys are sealed under a Merkle root over the
canonical key records. The items are not published.

## Validity

Before any verdict was opened, 201 flawed items stratified over operator and domain were read with the
original step beside the changed one. 178 changed proofs were judged really invalid: 88.6% (95% Wilson
interval 83.4 to 92.2). In most of the 23 rejects the changed sentence stays true: a word made redundant by
the context was dropped, two symmetric variables were relabelled, or an added term was zero. The rest are
broken notation or a changed label with no mathematical effect. That is why operator tier is treated as a
prior and not as a certificate. The protocol says items judged cosmetic are regenerated or dropped before
sealing. An audit of the sealed bank found that this had not happened: all 23 rejected items stayed in the
bank keyed as flawed, because the sampler did not read the validity review, and five of them fell in the
frozen stage-0 sample. A run on this bank has to exclude them first.

## Status

A stage-0 sample of 320 items (240 flawed, 80 clean, stratified over all eighteen operators and both tiers,
seed 20260916) was frozen and never served. The bank, its protocol, the seal and the grader (`grade_md.py`)
exist; the eligibility gate on the validity review is the one piece a run still needs.
