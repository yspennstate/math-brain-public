# Claude intake E for the 1,000 open probability problems campaign (2026-09-08)

Fourth disjoint intake ledger in the same campaign. The three earlier lists are
`probability_1000_intake_D_20260908/` (30 sources), `probability_1000_intake_claude_20260907/`
(35 sources) and the Codex worker's tree at `Downloads/Probability_1000_20h_20260906/`
(260 source rows, 251 distinct source ids across all three). Every candidate here was checked
against the union of those three source lists before it was fetched; nothing in this directory
re-mines a source that appears in any of them, and nothing was written into the Downloads
campaign tree.

Problem ids carry the prefix `E` so a merge into the campaign ledger can remap them without
colliding with the `C####`, `D####` and `P####` ranges.

## What is here

- `sources.jsonl` — 47 sources, all `validated_and_extracted`. Raw bytes and extracted text live
  under `Downloads/Probability_1000_intake_E_20260908/sources/<id>/`.
- `problems.jsonl` — 113 rows, `E0001`..`E0113`. `admitted = false` rows are literature
  exclusions and carry `resolved_by`.
- `attempts.jsonl` — 110 rows (`probability-attempt.v1`), one per admitted problem, written by
  this agent, no delegation.
- `raw/source_identity_check_20260908.json` — the first 220 characters of the extracted text of
  every one of the 47 PDFs, with the declared title beside it. All 47 were confirmed to be the
  intended document before any row was written. (The 09-07 run in this campaign cited three
  arXiv numbers guessed from memory that fetched entirely unrelated papers; that is why this
  file exists and why every source here was fetched from an arXiv API listing or a named author
  page rather than from recall.)
- `raw/grep4.py` — the numbered-statement finder used to locate problems with their PDF page;
  `raw/arxiv_search.py`, `raw/arxiv_recent.py` — the arXiv API queries used for discovery;
  `raw/batch_fetch.py`, `raw/cand*.jsonl` — the acquisition batches.
- `batches/b0*.json` — the exact row batches appended, in order; `add_batch.py` is the appender
  and enforces uniqueness of `problem_id` and of `(source_id, locator)`.
- `intake_tools.py` — `fetch` (source acquisition) and `snapshot` (regenerates `STATUS.json`).

## Counts (all computed by `python intake_tools.py snapshot`, never typed by hand)

    validated sources                47
    problem rows                    113
    admitted rows                   110
    admitted distinct problems      110
    attempts (substantive)          110
    literature exclusions             3
    rows flagged partial_result      10

Twenty-one of the forty-seven sources were mined. Rows per source:

    bandeira_42_problems_2015          16      polling_open_2014                   3
    chatterjee_lower_bounds_2017       13      favorite_sites_2016                 3
    qso_open_2009                      11      brw_boundary_infinity_2022          3
    durrett_coexistence_2009            9      sparse_graph_ips_2023               3
    hunts_hypothesis_survey_2019        7      map_processes_open_2019             2
    kesten_percolation_highlights_2002  6      brownian_polymers_poisson_2018      2
    simple_challenging_markov_2014      6      reflected_bm_ergodicity_2018        1
    pitman_tang_patterns_2014           6      sk_free_energy_survey_2025          1
    five_remarks_rw_groups_2014         5
    bootstrap_noise_sensitivity_2015    4
    diaconis_mcmc_learned_2013          4
    eigenvectors_survey_2016            4
    mobile_boolean_2014                 4

The other twenty-six were fetched, identity-checked and left unmined in this pass. They fall
into three groups. (a) Sources whose open problems are stated inline in running prose with no
numbered list, so they cannot be mined at the quality this schema wants without a full read:
`stretched_polymers_2010`, `slade_saw_spin_rg_2018`, `legall_brownian_geometry_2018`,
`hyperbolic_spin_survey_2021`, `ising_correlations_survey_2019`, `large_n_spde_survey_2022`,
`potentials_recurrent_networks_2025`, `sle_large_deviations_2021`, `rg_method_intro_2019`,
`highdim_random_walk_2026`, `rbm_quadrant_survey_2026`, `pdmc_scaling_survey_2026`,
`classical_localization_survey_2025`, `cooling_random_env_2016`, `brw_random_env_survey_2020`,
`lace_bcc_survey_2017`, `ifs_survey_2022`, `hyperuniform_survey_2016`,
`rw_groups_basic_facts_2022`, `potts_cayley_survey_2021`. (b) Sources whose problems are
outside probability or too far from it to belong in this campaign:
`seven_applied_combinatorics_2023` (mostly graph algorithms and quantum computing),
`algebraic_statistics_open_2007`, `reliability_open_2024` (its open problems are
well-posedness questions for systems of transport equations rather than probability
statements). (c) Papers acquired as status references rather than as problem sources:
`nicd_erasures_2025` (it REFUTES the Simons-list question on majority optimality for the
noise operator with erasures, so it carries no open problem of its own),
`one_dependent_star_2018`, `discrete_interacting_updates_2025`.

## Status checking

Every admitted row carries a non-empty `status_search` recording what was done to check the
problem is still open: the query run, what came back, and what was and was not read. Where a
search produced a lead that could not be certified (an abstract read but not the paper, a
preprint claiming a proof, a nearby theorem with different quantifiers) the row stays admitted
and the lead is written into `status_search` in those words. The leads worth naming are:

- E0002 (supercritical cluster-size limit): the Wulff-construction literature (Alexander-
  Chayes-Chayes, Cerf, Cerf-Pisztora) may already give this for the local event; I checked the
  shape-LDP statements, not the papers.
- E0050 (matrix Spencer): a 2026 arXiv preprint titled "A Proof of the Matrix Spencer
  Conjecture" (2608.28816) exists and was NOT read. The row is admitted per the campaign's
  admit-when-in-doubt rule; check that preprint before treating the problem as closed.
- E0051 (random k-lifts): Bordenave-Collins (Ann. Math. 190, 2019) settles the fixed-base-graph,
  large-lift regime; the source asks for a bound uniform in both parameters.
- E0057 (multireference alignment): part (2) of the source's two-part question, the sample
  complexity, IS answered (Perry-Weed-Bandeira-Rigollet-Singer, sigma^6); part (1), consistency
  of the quasi-MLE, is what keeps the row admitted, and this is recorded in the row.
- E0048 (noncommutative Khintchine): Bandeira-Boedihardjo-van Handel reach (log d)^{3/4} on the
  reading of their abstract, not the conjectured (log d)^{1/2}; abstract read, paper not.
- E0015 (spatial Prisoner's Dilemma): Cox-Durrett-Perkins and Durrett's 2014 EJP paper settle
  spatial games with SMALL selection coefficients; the source's matrix has order-one entries.
- E0096, E0056, E0064, E0035: rows where I could not establish that a plausibly-relevant later
  result does or does not cover the exact statement; each says so in its own words.

## The three exclusions, each with both sentences quoted

The D-ledger audit found that one of its eight exclusions was wrong because it rested on a
search summary rather than on the source's own sentence. Each exclusion here quotes the
SOURCE's statement of the question and the cited paper's own statement of what it proves, and
compares the objects by name inside the `resolved_by` field.

1. **E0028** (Hunt's hypothesis, Question 3) — resolved inside the source itself: its
   Section 3.2.1 is headed "Counterexample for Question 3" and gives the explicit two-dimensional
   Gaussian counterexample. No external citation involved. Recorded rather than silently
   dropped so the check is on the record.
2. **E0043** (Bandeira Open Problem 0.2(a)) — the Recht-Re noncommutative arithmetic-geometric
   mean inequality, refuted by Lai and Lim (arXiv:2006.01510, ICML 2020), false as soon as
   n = 5. The source names it as Recht-Re with citation [RR12]; the paper names the same
   conjecture and the same objects.
3. **E0049** (Bandeira Open Problem 4.2, the Latala-Riemer-Schutt comparison) —
   settled by Latala, van Handel and Youssef (Invent. Math. 214, 2018) whose abstract, read
   verbatim, states the p = infinity case of exactly the comparison the source asks for, for
   exactly the source's class of matrices.

Note the deliberate near-miss: E0044 keeps the OTHER direction of Bandeira's Open Problem 0.2
(the one the source attributes to [Duc12], not to [RR12]) as an ADMITTED open problem, because
Lai and Lim's paper names only the Recht-Re direction. That is the beta-Hermite-versus-circular
distinction the D-ledger audit was about, applied prospectively.

## What the attempts are and are not

None of the 110 attempts is a claimed solution. Ten rows are flagged `partial_result` because
they contain a complete elementary derivation that adds something to the source's own text:

- E0008 — Jensen's inequality carries the fast-stirring Lyapunov inequality to the nonlocal
  (long-range) generator with no new hypothesis on phi.
- E0024, E0026, E0027 — Rao's sufficient condition for Hunt's hypothesis is closed under
  independent sums (up to replacing f by 2f), so Questions 4, 6 and 7 of that survey have a
  positive answer inside Rao's class. This extends the survey's own Proposition 3.10, which
  makes the same observation for the strictly smaller Kanda-Forst class.
- E0058 — the family of logarithmic Lyapunov functions for a Volterra QSO is exactly the
  nonnegative kernel of A-transpose, which delimits the search the source asks for.
- E0064 — a strictly non-Volterra QSO has zero diagonal, hence zero trace, in its derivative
  everywhere, while Euler's identity gives the radial eigenvalue 2 at any fixed point; the m-1
  tangential eigenvalues therefore sum to -2 and one has modulus at least 2/(m-1), which exceeds
  1 only for m <= 3 - a concrete reason to expect the source's Theorem 6 to fail for large m.
- E0066 — quadratic bistochastic operators are entropy-monotone, so every trajectory
  accumulates on the entropy-preserving set.
- E0077 — the MMPP squared-coefficient-of-variation conjecture holds whenever the modulating
  chain is reversible, leaving the non-reversible case as the whole content.
- E0104, E0105 — the Poisson void probability turns the mobile-Boolean detection comparison into
  an explicit integral, and for ballistic grains the point-detection time is asymptotically
  exponential with an explicit rate.

Everything else is an honest "here is the precise wall" attempt: a reduction, a calibration
against a trivial bound, or a localisation of the difficulty. Three specific cautions, all
written into the rows themselves rather than only here, following the D-ledger audit's finding
that its three overstatements were each contradicted by the row's own obstruction field:

- E0052 checks the conjectured 1 - 1/e bound against Markov's inequality explicitly and records
  that Markov gives only 1/(n+1), so the conjecture is not the trivial bound in disguise.
- E0044 states a candidate refutation of the reverse noncommutative AM-GM inequality and says in
  the same sentence that the normalisations were not checked and that it should be verified
  before being believed.
- E0110 records a tension rather than a result: a coupon-collector heuristic predicts a
  relaxation time of order d log d where the source's Conjecture 1.5 asserts order d, and the
  row says which of the two is right was not settled here.

## Merge rule for the campaign holder

1. Remap `E####` to the next free `P####`, keeping `dedup_key` and adding `origin_id: E####`.
2. Append the 47 `sources.jsonl` rows, copying the source folders into
   `Downloads/Probability_1000_20h_20260906/sources/` under the same ids.
3. Append problems and attempts; recompute the campaign `STATUS.json`.
4. The three exclusions were each checked against the source's own sentence and the cited
   paper's own abstract, but not against the cited papers' full texts. Treat them the way the
   campaign treats its own `resolved_in_literature` rows: as claims to verify.
5. Nothing here is a promoted original solution. The ten `partial_result` rows are
   author-checked only.
