# Multidisciplinary literature proof bank (mdlit_v1), 6 September 2026

This is the sibling of the probability bank (PLIT). The question is the same: given a research-level proof in which one step may have been changed, can a solver find the changed step, and does it find it more often when it is given notes from the math brain? The proofs here come from analysis, algebra, number theory, combinatorics, geometry, topology, logic and learning theory instead of probability.

## The bank

`arxiv_harvest_md.py` downloads LaTeX sources of arXiv papers in four groups: analysis (math.AP, math.FA, math.CA), algebra, number theory and combinatorics (math.AG, math.NT, math.CO), geometry, topology and logic (math.DG, math.GT, math.AT, math.LO), and learning theory (stat.ML, plus cs.LG cross-listed with math.ST, stat.TH, math.OC or cs.IT). It takes the groups in turn, primary-category papers first, newest first. Papers in the probability bank's listing are excluded, so the two banks are disjoint.

`extract_proofs_md.py` applies the probability lane's acceptance rules unchanged. A proof has 3 to 25 sentence steps and 250 to 6,000 characters, its statement has 40 to 1,800 characters, it cites at most two references outside the statement-proof pair, at least a third of its steps carry mathematics, and it has no figure, environment or macro residue and is not a proof by reference.

Each accepted proof gives at most one item, either clean (the proof as published) or flawed. A flawed item has exactly one step changed at one place by one of the eighteen operators in `mutate_md.py`, drawn from an eleven-class taxonomy: sign flip, inequality direction, quantifier swap, dropped or weakened hypothesis, wrong constant or exponent, off-by-one index, wrong lemma or reference cited, limit order, unjustified interchange, extremum swap and set-operator swap. A step whose token overlap with the statement exceeds 0.55 Jaccard is never changed, because a step that restates the theorem cannot carry a derivation fault. `build_bank_md.py` writes the items and a separate key file, and `seal_md.py` commits the key records to a Merkle root (RFC 6962) and hashes every artifact (`SEAL.json`; `python seal_md.py --verify` recomputes it).

From 4,208 accepted proofs in 578 papers (55 more were excluded as belonging to the probability listing, and 64 had no admissible change site), the build produced 4,144 items: 1,250 clean and 2,894 flawed. All the papers are from 2026. `BUILD_REPORT.json` gives the counts by operator, taxonomy class, tier, difficulty label, domain group, arXiv category, statement kind, number of external references and number of steps. The difficulty label (easy, medium, hard) comes from a fixed heuristic and is a label, not a measurement.

## Validity

A one-token change does not always make a proof wrong. The author read 201 flawed items, stratified over operators and domain groups, with the original step beside the changed one, before any solver verdict existed. 178 of the 201 were judged to be real defects (88.6 percent, Wilson 95 percent interval 83.4 to 92.3 percent). The 23 rejects fall into a few kinds: a garbled index or label with no mathematical change, a word dropped whose content the sentence already carries (a finite sequence of moves, a uniformly bounded family indexed by one parameter), an equivalent restatement, a relabelling of symmetric or existentially bound variables, a change to an added zero term, a citation numeral that cannot be checked from the text, and a LaTeX break.

The review was first only descriptive, and five rejected items were in the first 320-item sample. `validity_gate.py` closes that hole for every later sample: the sampler excludes each item reviewed `no` or `unsure`, binds the exact review bytes into the sample, and refuses to serve or grade when the review is missing, malformed or changed, or when a frozen sample holds a rejected id or changed question text. `VALIDITY_GATE_AMENDMENT.md` records the rule. The gate removes documented invalid items; it does not certify the items nobody has read.

## Pre-registered test

`PROTOCOL_MDLIT.md` was written before any item was served. It defines four arms on the same items and prompt: no notes; the top three BM25 notes from the math brain for the statement and first three steps; the same notes moved to a different item (a placebo matched in kind and bulk); and notes ranked over the math brain joined with a statements-only store of the harvested papers (`build_corpus_store_md.py`, never any proof text). Full credit requires the verdict "flawed" at the keyed step. Arms are compared on paired items with exact McNemar tests, a clean-item false-positive guard and a ceiling rule. `run_md_wrapper.py sample` draws a seeded, stratified sample and serves it, `md_notes_bm25.py` builds the notes, `grade_md.py` scores the verdicts, and `grade_md_check.py` re-derives every number by a separate path. `review_sample_md.py` prints the hand-read validity sample and summarizes the judgements.

This folder holds no solver results.

## Running it

    python -m unittest test_validity_gate

runs the 15 gate tests on synthetic fixtures. They pass on this copy. The serving wrapper `run_md_wrapper.py` and the notes builder import the sterile runner `run_bank10k.py` of the earlier 10,000-question bank, which is not in this folder. Local paths read `<HOME>` or `<PRIVATE>`. Because of that substitution, and because of the protocol's opening paragraph, the published files differ from the hashes in `SEAL.json`.

The items, keys, per-item review notes, hand-read logs, the harvested sources and the extracted proofs are private and are not included.
