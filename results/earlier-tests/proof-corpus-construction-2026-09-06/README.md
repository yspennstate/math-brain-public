# Proof corpus construction, 6 September 2026

This continues the probability and multidisciplinary literature proof banks. It leaves the existing `plit` and sealed `mdlit_v1` artifacts unchanged.

## Starting point

On 6 September 2026 the probability bank held 4,901 candidate items and the multidisciplinary bank 4,144. Neither figure is an accepted count. The multidisciplinary manifest drew only on 2026 sources, its extractor predated the repair of probability proof headings, and both builders produced one form per proof rather than matched pairs.

## Method

Each reviewed source proof yields a clean form and a form with exactly one changed step. Both forms stay in the same split, and the number of forms is reported separately from the number of distinct source proofs. Exact source binaries, licensing evidence, proof locations, assumptions and proof identities are kept with every item.

Construction runs in seven stages:

1. Acquire and hash the primary source together with its access and licence evidence.
2. Read the full relevant source and write a faithful, explicit normalization of the proof. Keep the raw source bytes and record every normalization and every supplied premise.
3. Propose a single-step change, with a mathematical falsifier and a minimal repair.
4. Build both forms with `build_source_pairs.py` into a fresh private packet directory.
5. Read both assembled forms and record the author's review.
6. Obtain an independent source and mathematical review, then run the acceptance gate (`proof_bank_gate.py`, published separately).
7. Freeze only accepted forms for evaluation. One solver session never sees both twins, and keys, original proofs, reviewer reasoning and held-out controls are never indexed into solver-facing notes.

A candidate stops, with an explicit pending state, when source or licence evidence is missing, a proof is incomplete, an assumption is unresolved, the first erroneous step is ambiguous, a source family would leak across splits, or resource admission fails. No constructor writes a semantic acceptance record.

Reports keep apart candidate forms, distinct source proofs, distinct paper families, structurally eligible forms, author-reviewed forms, independently accepted forms, held-out-safe forms and evaluated forms.

## First accepted packet

Tropp's 2011 article on matrix martingales (arXiv 1101.3039, DOI 10.1214/ECP.v16-1624) supplies five localized proofs, giving five clean and five flawed forms. All ten passed separate hash-bound author and independent reviews, and recomputing the acceptance report from the unchanged inputs reproduced it exactly (SHA-256 `51027bacc62f4b6469906863fbdb9343a82906557bd96c2d6fd65f81f109c3f2`). These are ten calibration forms from five proofs and one source family. None has been evaluated, none is held-out-safe, and their difficulty is unmeasured, so the packet says nothing about whether the brain helps.

The institutional PDF matches its published checksum. Its bytes differ from the author-hosted PDF, but all nine pages have identical extracted text and identical 72 dpi renders, and a second parser agrees on every page. The article carries a CC BY 3.0 licence. Lemma 3.2 enters one question as a displayed premise; its proof lies outside the paper and is not counted as a proof the paper supplies.

## Source-context extraction

`extract_source_context.py` wraps a fixed copy of the repaired probability extractor (`upstream_extract_proofs.py`) and refuses to load it if its SHA-256 differs from the pinned value. It keeps full proof headings, distinguishable external references, raw statement and proof spans in a hash-bound expanded source, source-file hashes and the arXiv version recorded at download. Missing or cyclic include directives are kept and reported, and an ambiguous include or main file disqualifies the candidate. A clean parse is not a certificate of completeness, licensing or mathematical validity.

The command needs the archived source binary. It checks the download hash and compares every source file it reads with the matching archive member without extracting anything; filename collisions and changed bytes fail closed. The recorded version is an attribution from the download log, since some downloads used an unversioned URL. Repeated identical proofs share one proof-text identity, and occurrence counts are reported beside distinct proof-text counts.

Run one paper into a new private directory:

    python extract_source_context.py --tex-root ... --download-log ... --paper-id ... --source-archive ... --private-out-dir ...

It writes a no-ingest notice, context receipts, proof candidates, the expanded source and a file manifest. It creates no questions and no acceptance records.

Two archived arXiv sources (2609.04155 and 2609.04153) were run end to end: 23 and 44 candidate proofs, 3 and 16 passing the structural filter, archive bytes matching in both. Neither licence has been reviewed and neither added a bank question.

## Tests

    python -m unittest test_source_pairs test_source_context

The 20 tests (7 source-pair, 13 source-context) use synthetic fixtures only. The pair tests cover duplicate proofs, no-op changes, changed evidence, split leakage and overwrite protection. The context tests cover missing, escaping, cyclic, repeated and ambiguous includes, flattened archives, partial-proof headings, distinguishable references, source drift, exact byte origins, archive collisions and single-file compression.

In this copy the two path constants at the top of `upstream_extract_proofs.py` read `ARXIV_TEX_DIR` and `ARXIV_LISTING` from the environment, and the pin in `extract_source_context.py` was updated to match, so both files differ from the hashes recorded in `VALIDATION.json`. The 20 tests pass on this copy.

The items, keys, source binaries, reviews and split maps are private and are not included.
