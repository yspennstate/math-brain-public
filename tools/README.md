# tools

Scripts that build, check, export and restore the math store. Each one's docstring has the full detail and its
options; this page says what each is for and where it sits in the work.

## Getting cards in

| script | what it does |
|---|---|
| `integrate_drafts.py` | Takes draft bundles from the inbox, validates them, computes every digest and source manifest, seals and ingests them. A bundle that fails is set aside with a `.rejected-note` and never blocks the others. How to write a bundle: [../docs/adding-cards.md](../docs/adding-cards.md). |
| `harvest_proofwiki.py` | Fetches a curated list of ProofWiki pages through the MediaWiki API and writes their statements (and proofs, for theorems) as a draft bundle. A theorem without a clean proof section enters as a concept, never with an invented proof. Output stays `.part` until sampled by hand. |
| `harvest_wikipedia.py` | Fetches the lead paragraphs of named results and notions from the Wikipedia REST API. Every entry enters as a concept, because a lead paragraph rarely states a result with all its hypotheses; harvested names carry a `wiki-` prefix so they never collide with authored cards. |
| `wiki_formulas.py` | Rebuilds a Wikipedia lead with its formulas kept as TeX (the REST summary drops them), for the harvester. |
| `activate_harvest.py` | The quality gate between a harvest and the integrator: drops stub statements, re-derives a card's name when a redirect changed the page, removes duplicates, and renames the cleaned `.part` to `.json`. |

The `codex_prompt_*.txt` files are the prompts the authoring lanes (algebra, analysis, geometry, topology) and the
two review rounds were given. They refer to the inbox and to the bundle spec, which is now
[../docs/adding-cards.md](../docs/adding-cards.md).

## Checking what is in

| script | what it does |
|---|---|
| `qa_sample.py` | Draws a seeded, reproducible sample of cards for an adversarial review and writes the review file with the verdict schema. A round's file is written once; a rerun that would change it is refused, and earlier rounds' cards are left out of the sample. |
| `apply_verdicts.py` | Turns review verdicts that carry a fix into a corrections bundle: the same card, the referee's statement, marked as superseding the old one. A verdict for a card the round did not sample is refused. |
| `record_review.py` | Records a read of a card as evidence the store can show. An agent's read is shown beside the card but never changes its status; a human's read, under the reviewer's key, can. |
| `corpus_audit.py` | Read-only audit of every current card: statement health, proof text on theorems and lemmas, edges into retired cards, cycles in `depends_on`, retrieval probes per shelf, and injection latency. Writes a report and a worklist of flagged cards. |
| `mathbrain_status.py` | One-glance status of the inbox, the integrator and the store. Read-only. |

## Export and restore

| script | what it does |
|---|---|
| `export_store.py` | Writes the store as sorted JSONL, one file per table, into `export/population/`, so a diff between two exports is a diff between two states of the store. `--check` exits 1 when the export is stale. |
| `import_store.py` | Rebuilds a store from that export, never over the live one. `--roundtrip` rebuilds to a temporary database and re-exports it; the digests must match. |

## For the public repository

| script | what it does |
|---|---|
| `cited_works.py` | Collects every work cited by the papers in this repository (`.bib` files and bibliography lists) and writes [../docs/cited-works.md](../docs/cited-works.md). Bibliographic data only. |

## A research measurement

`fpp_l2prime_kurtosis.py` reproduces one measurement from the first-passage percolation campaign: the conditional
kurtosis of the block-resampling increment in planar first-passage percolation, with U[1,2] weights on Z^2 and exact
Dijkstra. At the sizes measured it saturates near 6.2 rather than growing. It is kept here so the ladder can be
extended to larger boxes; nothing at the measured sizes bounds anything asymptotic.
