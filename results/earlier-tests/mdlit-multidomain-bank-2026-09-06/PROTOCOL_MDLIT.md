# PROTOCOL MDLIT: does the math brain help an agent find the one changed line in a literature proof outside probability? (pre-registered)

Written before any item of the sealed bank is served to a solver. The sha256 of this file at sealing goes into SEAL.json
and the improvement ledger; any change after the first serve is an amendment recorded below with its own sha and reason.
Written on 6 September 2026 as the sibling of the probability bank's protocol (PROTOCOL_PLIT); same item shape,
same runner, same scoring rule, so one harness grades both banks. This public copy differs from the sealed bytes
(SEAL.json) only in this paragraph and in local paths, which read <HOME> or <PRIVATE>.

## Question
Does a solver that receives notes from the math brain locate the one changed step of a research-level proof in analysis,
algebra, number theory, combinatorics, geometry, topology, logic or learning theory more often than the same solver without
notes; more often than the same solver with kind-and-bulk-matched notes about a different proof (the content contrast); and
does a solver handed the paper's OWN other statements (a brain that had read the paper) do better still?

## Population (the bank, mdlit_v1)
Theorem, lemma, proposition and corollary proofs extracted from the LaTeX sources of arXiv papers listed 2024-01-01 to
2026-09-06 in math.AP, math.FA, math.CA (analysis), math.AG, math.NT, math.CO (algebra_nt_co), math.DG, math.GT, math.AT,
math.LO (geom_top_log), stat.ML and cs.LG cross-listed with math.ST/stat.TH/math.OC/cs.IT (ml_theory), fetched round-robin
over the four groups, primary-category papers first, newest first (arxiv_harvest_md.py). Papers in the probability campaign's
listing are excluded so the two banks are disjoint. A proof enters when extraction is clean (extract_proofs_md.py acceptance,
unchanged from the probability lane: 3-25 sentence steps, 250-6,000 characters, statement 40-1,800 characters, at most two
references outside the pair, a third of steps carrying mathematics, no figure or environment residue, not a proof by reference,
no macro residue). Each proof contributes at most ONE item: FLAWED (exactly one step changed at exactly one place by one of the
eighteen operators of mutate_md.py, drawn from the eleven-class taxonomy: sign flip, inequality direction, quantifier swap,
dropped/weakened hypothesis, wrong constant or exponent, off-by-one index, wrong lemma or reference cited, limit order,
unjustified interchange, extremum swap, set-operator swap) or CLEAN (the proof as published), never both. A step whose token
overlap with the statement exceeds 0.55 Jaccard is never a site (the 2026-08-17 scar: a step that restates the theorem cannot
host a derivation fault). Bank size, operator, taxonomy, tier, difficulty and domain counts and the sha256 of the items and
keys files are in BUILD_REPORT.json; the Merkle root over the key records is in SEAL.json.

Keys live only in <HOME>/bank_multidomain_keys_quarantine/mdlit_keys.jsonl (NO_INGEST.md beside them); the solver,
the notes builder and the prompt never read them; the items file carries no paper id, no domain, no operator, no step marker
(BUILD_REPORT.items_leak_check).

Every item carries a certificate in its key: arXiv id, theorem label (environment, optional title, labels), proof_sha256 over the
statement and the clean steps, mutation_sha256 over the exact edit (operator, step, span, removed, inserted), and a difficulty
estimate (easy / medium / hard) from a fixed heuristic (operator class, proof length, whether the removed token recurs elsewhere
in the proof, site position). The estimate is a label, not a measurement; the none arm's rate per stratum is the measurement.

Operator tiers are a PRIOR on validity ("the changed proof is really invalid"), not a certificate: tier A - ineq_flip, word_flip,
quantifier_swap, quant_word, limit_target, index_shift, sum_bound_shift, limit_order, limop_swap, setop_swap; tier B - ineq_to_eq,
sign_flip, hypothesis_drop, hypothesis_swap, const_change, theorem_swap, ref_shift, interchange. A hand-read validity sample of
at least 200 flawed items, stratified over operators and domain groups, read by the author with the original step beside the
changed one and judged BEFORE any verdict is opened, is reported with a 95 percent Wilson interval per tier and per operator
(VALIDITY_REVIEW.json). Items judged cosmetic are regenerated from a fresh candidate or dropped before sealing, never shipped;
the false-mutation rate reported is the rate on the sample as first drawn, and the post-regeneration bank is re-sealed.

## Solver and serving
The inherited sterile runner (run_bank10k.py through run_md_wrapper.py): `claude -p --output-format json --model <M>
--setting-sources "" --tools ""`, prompt on stdin, no hooks, no tools, no project instructions; a served-model census that must
name the requested model AND a transcript receipt whose assistant turns all read that model with end_turn last and no tool use,
else the verdict is rejected and the item re-served; after any timeout the transport is re-proved before a timeout is recorded
(the 2026-09-05 outage rule). Primary solver: claude-sonnet-4-5. A second,
pre-registered solver: the Fable model as served by the CLI (verified from the transcript's message.model), on a subset of 60
items of the same sample; each solver's result is reported under its own name and never pooled. Concurrency 1-2, at most 3.

## Arms (one runner, same prompt, same items, same seed)
- none: the statement and the numbered steps, no notes.
- brain: the same plus REFERENCE NOTES = the top-3 BM25 nodes of the production math store
  (<HOME>/math-brain-build/local/population/brain.sqlite3 as it stands at sealing; node count recorded in
  brain_notes.json) for the query "statement + first three steps" - the B12/B13 builder's rule, unchanged.
- placebo: the brain arm's notes shifted by the builder's donor rule to a different item (kind and bulk matched, relevance
  broken; identical-notes collisions re-donated).
- lit: notes ranked by the same rule over the production store UNIONED with a statements-only store of the harvested
  literature (build_corpus_store_md.py: every extracted theorem/lemma/proposition/corollary STATEMENT of the multi-domain
  harvest, never any proof text; node count recorded in lit_notes.json). This is the arm a brain that had READ the paper's
  results would give; it is the only arm that can in principle catch a wrong-lemma-cited defect whose named lemma is local.

## Sampling (seeded, fingerprinted)
Stage 0: 320 items = 240 flawed + 80 clean; flawed items stratified over (domain group x taxonomy) cells (floor 2 per cell where
the bank has them, then proportional), clean items drawn proportionally over domain groups; seed 20260916; SAMPLE.json carries
the item ids, the bank fingerprint and the served-text hash the runner checks before serving. The none arm is served FIRST and
graded alone before any other arm is launched (the ceiling rule below decides the other arms' scope). Powered stage: sized from
stage 0 (below), seed 20260917, every served item excluded.

## Scoring (the B12/B13 rule, unchanged, plus the defect rule)
FOUND-THE-LINE (full credit, PRIMARY): the verdict is "flawed" AND the reported fault_step equals the key's step.
DETECTED: the verdict is "flawed" at any step (reported beside, never in place of, full credit).
FOUND-THE-DEFECT (SECONDARY, deterministic): found-the-line AND the verdict's "why" text, normalised (lower-case, backslashes
and spaces stripped), contains the key's removed text or its inserted text (normalised the same way), OR contains one of the
taxonomy's cue words fixed here: inequality_direction {inequal, direction, revers, flip, "<=", ">=", "\le", "\ge", "at most",
"at least"}; sign_flip {sign, minus, plus}; quantifier_swap {quantif, "for all", "for some", exists, every}; dropped_hypothesis
{hypothes, assum, requir, need, missing, without, dropp, weaker, does not follow, not enough, insufficient}; wrong_constant_or_
exponent {constant, exponent, power, factor, coefficient}; off_by_one_index {index, off by one, off-by-one, boundary, "n+1", "n-1",
"k=0", "k=1"}; wrong_lemma_cited {lemma, theorem, cite, refer, equation, "(eq", does not apply, wrong result}; limit_order
{order, interchang, swap, commut, limit}; unjustified_interchange {interchang, exchang, swap, justif, dominated, uniform,
commut, fubini, tonelli}; extremum_swap {sup, inf, max, min, extrem}; set_operator_swap {union, intersect, subset, superset,
contain}. A clean item is correct when the verdict reads valid/clean/correct/sound; clean items feed only the false-positive guard.

## Hypotheses and tests
H-primary: on flawed items, brain beats none on found-the-line. Paired by item, McNemar exact two-sided; report both rates with
95 percent Wilson intervals, the discordant counts, the paired difference with its 95 percent interval, and the room to fail
(1 - the none rate) beside it.
H-content: brain beats placebo, same test. H-lit: lit beats none, and lit beats brain, same test.
Guard: clean-item false-positive rate of any notes arm minus none, flagged above 10 points (arms_guard.require_placebo is
called on the run directory before any brain-vs-none number is written; MANIFEST.json declares the arms and results/placebo_raw.json
is written from the placebo verdicts).
Secondary (descriptive, no test): by domain group; by taxonomy; by tier; by difficulty stratum; by external-reference count; by
proof length; found-the-defect rates; detection-only rates; notes coverage (items with empty notes; items whose lit notes came
from the item's own paper; a hand read of six served note sets per arm).

## Ceiling rule and powered sizing
If the none arm's found-the-line rate on flawed items is above 85 percent (the 2026-09-05 rule), the bank is a ceiling for THAT
solver: the other arms are then served on the hard stratum only (the heuristic label, fixed before any verdict) so the paired
contrast has room to move, and the report says so; there is no powered stage for that solver. Otherwise the other arms are served
on the whole sample, and the powered stage serves n = ceil(784 * d) flawed pairs, clamped to [120, 400], plus clean items at one
quarter, where d is the brain-vs-none discordance rate of stage 0.

## Stopping and honesty rules
One stage 0 per solver, one powered stage per solver, no peeking-based additions. Every number in the report is re-derived from
the verdict files by a second script with its own data path (grade_md_check.py) before it leaves this directory; a non-empty
disagreement list blocks the report. The production store is not edited between sealing and the end of serving; lit is served
from a separate file. The hand-read validity sample is judged before any verdict is opened. Item generation counts, validated
counts and measured-benefit counts are reported as three separate numbers, never merged. Results are written under this
campaign directory only.

## Sealing record
(filled at sealing: bank counts, BUILD_REPORT sha256, items sha256, keys sha256, Merkle root, store node count, this file's sha256)
