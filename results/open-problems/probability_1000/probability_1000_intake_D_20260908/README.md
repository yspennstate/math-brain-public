# Claude intake D for the 1,000 open probability problems campaign (2026-09-08)

Third disjoint intake ledger in the same campaign. The two earlier ledgers are
`probability_1000_intake_claude_20260907/` (160 problem rows, 35 sources) and the Codex worker's
tree at `Downloads/Probability_1000_20h_20260906/` (260 source rows). Nothing in this directory
re-mines a source that appears in either of those two lists; the 30 sources here were checked
against both source lists before any of them was read.

Problem IDs carry the prefix `D` so a merge into the campaign ledger can remap them without
colliding with the `C####` and `P####` ranges.

## What is here

- `sources.jsonl` — 30 sources, all `validated_and_extracted`. Raw bytes and extracted text live
  under `Downloads/Probability_1000_intake_D_20260908/sources/<id>/`. These 30 were fetched by an
  earlier run of this task that died on a rate limit before writing any problem rows; this session
  read them and did the mining.
- `problems.jsonl` — 102 rows, `D0001`..`D0102`. `admitted = false` rows are literature exclusions
  and carry `resolved_by`. Two pairs of rows state the same mathematics from two different sources
  and share a `dedup_key`, so they count once in `admitted_distinct_problems`:
  `lqg_hausdorff_dimension_d_gamma` (D0049, D0052) and
  `planar_map_gromov_hausdorff_convergence_to_lqg_metric` (D0050, D0053).
- `attempts.jsonl` — 94 rows (`probability-attempt.v1`), one per admitted problem, written by this
  agent, no delegation. Six carry `result_status = partial_result` on the problem row; the rest are
  honest "here is the precise wall" attempts.
- `raw/source_identity_check_20260908.json` — the first 200 characters of the extracted text of
  every one of the 30 PDFs, recorded because the 09-07 run cited three arXiv numbers guessed from
  memory that fetched entirely unrelated papers. All 30 were confirmed to be the intended document
  before any row was written.
- `raw/dump.py`, `raw/grep_problems.py` — the extraction helpers (numbered-statement finder with the
  PDF page number).
- `batches/b0*.json` — the exact row batches appended, in order; `add_batch.py` is the appender and
  enforces uniqueness of `problem_id` and of `(source_id, locator)`.
- `intake_tools.py` — `fetch` (source acquisition) and `snapshot` (regenerates `STATUS.json`).

## Counts (all computed by `python intake_tools.py snapshot`, never typed by hand)

    validated sources                30
    problem rows                    102
    admitted rows                    94
    admitted distinct problems       92
    attempts (substantive)           94
    literature exclusions             8

Sixteen of the thirty sources were mined. The other fourteen carry no numbered open-problem list
(their open questions are stated inline in running prose, or the paper is a survey of results with
no problem section); they are left for a later pass rather than mined at low quality. The fourteen
are: copolymers_open_2010, chatterjee_ld_graphs_2016, parking_random_trees_survey_2025,
odometers_survey_2019, peled_spinka_loop_on_2017, legall_sphere_icm_2014, corwin_kpz_2012,
duminil_copin_ising_100_2022, lyons_random_complexes_2009, sheffield_random_surface_2022,
drsv_logcorrelated_2014, erdos_wigner_survey_2010, tsirelson_noise_2003, stability_open_2009
(the last has a broken text extraction — one character per line — and needs re-extraction before it
can be read).

## Status checking

Every admitted row carries a non-empty `status_search` recording what was actually done to check
the problem is still open: the query run, the papers the search returned, and what was and was not
read. Where a search produced a lead that I could not certify (an abstract read but not the paper,
a seminar listing rather than a publication, a result that is close to but not literally the stated
problem) the row stays admitted and the lead is written into `status_search` in those words.
Leads of that kind are recorded for D0012 (sums of standard uniforms), D0024 (disordered ZRP local
equilibrium), D0060/D0061 (percolation on nonamenable graphs — 2020-2026 preprints not exhaustively
searched), D0065 (log-correlated maximum in general dimension), D0078/D0084 (a Fall 2025 MIT seminar
listing for Holden-Yu on the spanning-tree map under circle packing) and D0097 (the small-lambda
half of the ARW statement).

## Merge rule for the campaign holder

1. Remap `D####` to the next free `P####`, keeping `dedup_key` and adding `origin_id: D####`.
2. Append the 30 `sources.jsonl` rows, copying the source folders into
   `Downloads/Probability_1000_20h_20260906/sources/` under the same ids.
3. Append problems and attempts; recompute the campaign `STATUS.json`.
4. The eight exclusions were identified from abstracts and search summaries, not from full texts.
   Treat them the way the campaign treats its own `resolved_in_literature` rows: as claims to
   verify, not certifications. D0096 in particular should have its hypotheses checked (dimension and
   jump distribution) before the exclusion is final.
5. Nothing here is a promoted original solution. The six `partial_result` rows are author-checked
   only, and two of them (D0035 and part of D0005) are best described as corrections to the way the
   source states its own question rather than progress on the mathematics.
