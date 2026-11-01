# Claude intake F for the 1,000 open probability problems campaign (2026-09-08/09)

Fifth disjoint intake ledger in the campaign, after the Codex worker's tree
(`Downloads/Probability_1000_20h_20260906/`, 189 source ids, 590 problem rows), the 09-07 Claude
list (`probability_1000_intake_claude_20260907/`), intake D and intake E (both 2026-09-08). Problem
ids carry the prefix `F` so a merge can remap them without colliding with the `C####`, `D####`,
`E####` and `P####` ranges.

The ledger was built in two sessions. The first (2026-09-08, 15:00-17:01Z) fetched forty sources,
wrote rows F0001-F0115 and pushed them as "intake F ledger, partial (95 problems)" before dying on
a rate limit. The second (2026-09-09, 01:2x-03:xxZ) fetched twelve more sources, wrote F0116-F0140,
this README and the final STATUS.json. Nothing from the first session was rewritten by me except the
`result_status` of F0055 and the F0065-F0068 status fields (both on another agent's lead, see below); the
second session's rows are batches 10 and 11, and one sentence of the F0124 attempt (a self-correction
left in the text) was cleaned after it was appended.

Every candidate source was checked against the union of the source lists of all earlier intakes
before it was fetched. Two sources here also appear in the Codex tree's `sources.jsonl`:
`pemantle_reinforcement_2007` (the Codex tree fetched it and mined nothing from it) and
`lyons_peres_book_2026` (the Codex tree mined 39 of its numbered questions; the five untaken ones are
discussed below and none was added). Nothing was written into the Downloads campaign tree.

## What is here

- `sources.jsonl` — 53 sources, all `validated_and_extracted`. Raw bytes and extracted text under
  `Downloads/Probability_1000_intake_F_20260908/sources/<id>/`.
- `problems.jsonl` — 140 rows, `F0001`..`F0140`. Rows with `admitted = false` are literature
  exclusions and carry `resolved_by`.
- `attempts.jsonl` — 114 rows (`probability-attempt.v1`): one per admitted problem written by this
  agent, no delegation, the two attempts written for F0066 and F0068 before those rows were excluded, and
  one second attempt on F0055 (`F0055-A002`) written by another Claude agent, `claude-prob1000-e0077-0908`,
  at 02:52Z on 2026-09-09 (see "What the attempts are" below).
- `batches/patch_F0065_F0068.py` — the one in-place edit of first-session rows: F0066 and F0068 turned
  into exclusions and the same lead appended to F0065 and F0067 (every other line byte-identical).
- `batches/b01..b11*.json` — the exact row batches appended, in order; `batches/mk_b*.py` are the
  scripts that generated batches 4-11; `add_batch.py` is the appender and enforces uniqueness of
  `problem_id` and of `(source_id, locator)`.
- `intake_tools.py` — `fetch` (source acquisition, sha256 of bytes and of extracted text) and
  `snapshot` (regenerates `STATUS.json`).
- `raw/` — `dedup_search.py` (keyword search over every earlier `problems.jsonl`), `grep4.py`
  (numbered-statement finder with PDF page), `pages.py`, `arxiv_search.py` (arXiv API title search,
  so that no arXiv number is guessed from memory), `batch_fetch.py`, the candidate lists
  `cand*.jsonl`, `dedup_index.json`, `all_source_titles.txt`, and `api_status_20260909.txt` (the
  arXiv API run used for the second session's status checks).
- `source_failures.jsonl` — two failed fetches of Benjamini's Saint-Flour notes (404).

## Counts (computed from the files by `python intake_tools.py snapshot`, not typed by hand)

    validated sources                53   (52 problem sources + abhk_height_width_2022, a status reference)
    problem rows                    140
    admitted rows                   111
    admitted distinct problems      111
    attempts (substantive)          111   (attempts.jsonl has 114 rows: the 111, the attempts written for
                                          F0066/F0068 before they were excluded, and F0055-A002)
    literature exclusions            29
    rows flagged partial_result       6   (F0019 F0029 F0036 F0059 F0090 F0133)
    candidate full solutions          1   (F0055, by the other agent, unreviewed)

Two pairs of first-session exclusions share a coarse `dedup_key` (F0047/F0048 under
`brownian_web_net_2015::section_8.3`, F0049/F0050 under `frieze_icm_2014::open_questions/problems`); they
are distinct problems with distinct locators, and the shared key only affects the distinct count of
excluded rows, which `snapshot` does not report.

Thirty-one of the fifty-three sources were mined (27 with admitted rows, 4 with exclusions only; the
fifty-third, `abhk_height_width_2022`, was fetched only to verify two exclusions). Admitted rows per source:

    vu_combinatorial_rmt_2020          17      hhp_stable_marriage_2006            3
    janson_simply_generated_2012       14      dh_steif_rwrs_2006                  3
    talagrand_small_2016               11      sabot_tournier_dirichlet_2016       3
    velenik_interfaces_2006             8      hpps_poisson_matching_2009          2
    brownian_web_net_2015               6      kenyon_dimers_2009                  2
    jarai_sandpile_2014                 5      hlmppw_chip_firing_2008             2
    kalai_three_puzzles_2018            5      lps_minimal_spanning_forests_2006   1
    frieze_icm_2014                     5      hkpv_determinantal_2006             1
    mossel_info_flow_trees_2004         5      smirnov_icm_2006                    1
    zygouras_polymers_review_2024       4      talagrand_prizes_2016               1
    beffara_dc_planar_percolation_2011  4      aldous_social_dynamics_2013         1
    chatterjee_yang_mills_2018          3      pemantle_reinforcement_2007         1
                                               guionnet_ld_rmt_2004                1
                                               quastel_spohn_kpz_2015              1
                                               miller_lqg_icm_2018                 1

Exclusions only: `werner_saint_flour_2003`, `borodin_gorin_integrable_2012`, `ben_arous_cerny_traps_2006`,
`abbe_sbm_survey_2017`.

## The sources, one line each

First session (forty):

- `janson_simply_generated_2012` — Janson, Simply generated trees, conditioned Galton-Watson trees, random allocations and condensation (Probab. Surveys 2012). 14 rows from its Sections 18-20 (balls in boxes, condensation, height and width), 2 exclusions.
- `velenik_interfaces_2006` — Velenik, Localization and delocalization of random interfaces (Probab. Surveys 2006). 8 rows, 2 exclusions.
- `vu_combinatorial_rmt_2020` — Vu, Recent progress in combinatorial random matrix theory. 17 rows, 2 exclusions.
- `voiculescu_free_entropy_2002` — Voiculescu, Free entropy (Bull. LMS 2002). Unmined in the first session, which left no note (2 numbered-statement strings found by grep4); the unification problem it poses is recorded from Guionnet's survey instead (F0133).
- `chatterjee_yang_mills_2018` — Chatterjee, Yang-Mills for probabilists. 3 rows.
- `smirnov_icm_2010` — Smirnov, Discrete complex analysis and probability (ICM 2010). Unmined in the first session, no note; grep4 finds 13 numbered-statement strings, so this is the first place a later pass should look.
- `smirnov_icm_2006` — Smirnov, Towards conformal invariance of 2D lattice models (ICM 2006). 1 row (the Nienhuis point of the loop O(n) model).
- `lps_minimal_spanning_forests_2006` — Lyons, Peres, Schramm, Minimal spanning forests. 1 row, 1 exclusion.
- `brownian_web_net_2015` — Schertzer, Sun, Swart, The Brownian web, the Brownian net, and their universality. 6 rows, 2 exclusions.
- `hkpv_determinantal_2006` — Hough, Krishnapur, Peres, Virag, Determinantal processes and independence. 1 row.
- `rudelson_vershynin_icm_2010` — Rudelson, Vershynin, Non-asymptotic theory of random matrices (ICM 2010). Unmined, no note (1 numbered-statement string).
- `erdos_yau_bull_2012` — Erdos, Yau, Universality of local spectral statistics of random matrices. Unmined, no note (6 numbered-statement strings, not reviewed in this pass).
- `kenyon_dimers_2009` — Kenyon, Lectures on dimers. 2 rows.
- `chatterjee_stein_icm_2014` — Chatterjee, A short survey of Stein's method (ICM 2014). Unmined, no note (3 numbered-statement strings, not reviewed).
- `garban_schramm_noise_2010` — Garban, Oded Schramm's contributions to noise sensitivity. Unmined, no note (2 numbered-statement strings); the Codex tree carries garban_steif_noise_2012, which a later pass should dedup against first.
- `zeitouni_rwre_icm_2002` — Zeitouni, Random walks in random environments (ICM 2002). Unmined, no note (0 numbered-statement strings: its open problems are in prose); intake C's drewitz_ramirez_rwre_2014 rows cover the RWRE questions that were still open in 2014.
- `newman_stein_spin_glasses_2005` — Newman, Stein, Short-range spin glasses: results and speculations. Unmined, no note (0 numbered-statement strings).
- `jarai_sandpile_2014` — Jarai, Sandpile models (Probab. Surveys 2018). 5 rows.
- `frieze_icm_2014` — Frieze, Random structures and algorithms (ICM 2014). 5 rows, 2 exclusions.
- `ferrari_spohn_growth_2010` — Ferrari, Spohn, Random growth models. Unmined, no note (2 numbered-statement strings).
- `speicher_icm_2014` — Speicher, Free probability and random matrices (ICM 2014). Unmined, no note (2 numbered-statement strings).
- `ghm_random_geometry_1999` — Georgii, Haggstrom, Maes, The random geometry of equilibrium phases. Unmined, no note (1 numbered-statement string in a long prose survey).
- `dembo_montanari_sparse_gibbs_2009` — Dembo, Montanari, Gibbs measures and phase transitions on sparse random graphs. Unmined, no note (7 numbered-statement strings, not reviewed; overlap with E0054 and the Codex SBM rows to be checked by whoever mines it).
- `werner_saint_flour_2003` — Werner, Random planar curves and SLE (Saint-Flour 2002). 1 exclusion (SLE duality and reversibility, both proved).
- `ben_arous_cerny_traps_2006` — Ben Arous, Cerny, Dynamics of trap models. 1 exclusion (REM aging under Metropolis, Gayrard 2019).
- `beffara_dc_planar_percolation_2011` — Beffara, Duminil-Copin, Planar percolation with a glimpse of SLE. 4 rows.
- `borodin_gorin_integrable_2012` — Borodin, Gorin, Lectures on integrable probability. 1 exclusion (Kerov's conjecture, Matveev).
- `zygouras_polymers_review_2024` — Zygouras, Directed polymers in a random environment: a review of the phase transitions. 4 rows.
- `talagrand_prizes_2016`, `talagrand_convolution_2016`, `talagrand_matchings_2013`, `talagrand_combinatorics_2017`, `talagrand_convexity_2013`, `talagrand_small_2016` — Talagrand's prize-problem notes. 12 rows and 8 exclusions, all recorded against `talagrand_small_2016` or `talagrand_prizes_2016` with the companion note named in the locator; the four other notes carry no rows of their own.
- `corwin_icm_2014` — Corwin, Macdonald processes, quantum integrable systems and the KPZ universality class (ICM 2014). Unmined, no note (1 numbered-statement string).
- `kalai_three_puzzles_2018` — Kalai, Three puzzles on mathematics, computation, and games (ICM 2018). 5 rows.
- `hpps_poisson_matching_2009` — Holroyd, Pemantle, Peres, Schramm, Poisson matching. 2 rows.
- `hhp_stable_marriage_2006` — Hoffman, Holroyd, Peres, A stable marriage of Poisson and Lebesgue. 3 rows.
- `parisi_euclidean_rmt_2005` — Parisi, Euclidean random matrices: solved and open problems. Unmined, no note (1 numbered-statement string; the open problems are stated in physics prose).
- `benjamini_fixed_source_2026` — Benjamini, Euclidean vs graph metric: the fixed-source problem (2026). Fetched at the end of the first session; unmined, no note (1 numbered-statement string; a one-problem paper, natural first row for a later pass).

Second session (twelve):

- `mossel_info_flow_trees_2004` — Mossel, Survey: information flow on trees (2004). 5 rows, 3 exclusions (two of them by the survey's own closing section).
- `abbe_sbm_survey_2017` — Abbe, Community detection and stochastic block models (JMLR 2018). 1 exclusion; its k >= 3 threshold question is already E0054, and its Conjecture 2 is a computational-hardness statement, left out on purpose.
- `dh_steif_rwrs_2006` — den Hollander, Steif, Random walk in random scenery: a survey of some recent results. 3 rows.
- `sabot_tournier_dirichlet_2016` — Sabot, Tournier, Random walks in Dirichlet environment: an overview. 3 rows (its open questions are in prose; the three precise ones were taken).
- `miller_lqg_icm_2018` — Miller, Liouville quantum gravity as a metric space and a scaling limit (ICM 2018). 1 row.
- `aldous_social_dynamics_2013` — Aldous, Interacting particle systems as stochastic social dynamics (Bernoulli 2013). 1 row, 1 exclusion (by Aldous's own 2016 paper). Its Open Problems 1 and 3 are research directions rather than statements and were not taken.
- `guionnet_ld_rmt_2004` — Guionnet, Large deviations and stochastic calculus for large random matrices (Probab. Surveys 2004). 1 row, 1 exclusion.
- `hlmppw_chip_firing_2008` — Holroyd, Levine, Meszaros, Peres, Propp, Wilson, Chip-firing and rotor-routing on directed graphs. 2 rows; its Question 6.5 (unicycle orbits of non-Eulerian digraphs) is combinatorial and was left out.
- `quastel_spohn_kpz_2015` — Quastel, Spohn, The one-dimensional KPZ equation and its universality class. 1 row.
- `corwin_shen_spde_2019` — Corwin, Shen, Some recent progress in singular stochastic PDEs. Unmined: its three numbered-statement strings are section headings and a 'problem' in the PDE sense, and its open questions are in prose.
- `pemantle_reinforcement_2007` — Pemantle, A survey of random processes with reinforcement (Probab. Surveys 2007). 1 row, 1 exclusion.
- `abhk_height_width_2022` — Addario-Berry, Brandenberger, Hamdan, Kerriou, Universal height and width bounds for random trees (EJP 2022). Fetched as a status reference on a peer's lead; it resolves F0066 and F0068 and gives the log^3 n bound recorded on F0065 and F0067. Carries no problem of its own.
- `lyons_peres_book_2026` — Lyons, Peres, Probability on Trees and Networks (2026 electronic edition). Unmined. Of its numbered questions and conjectures, 39 are already in the Codex tree; of the five that are not, the book itself records answers to four (Question 5.16 by Tang, Question 6.21 by Oh 2020, Question 6.49 by Hermon-Hutchcroft for transitive graphs with a counterexample otherwise, Conjecture 7.13 by Duminil-Copin, Goswami, Raoufi, Severo, Yadin 2020) and the fifth, Question 6.20 on anchored expansion constants of plane graphs, is answered for codegrees 3 and 4 by Haslegrave-Panagiotis and is otherwise too open-ended for a row.

## Status checking

Every admitted row carries a `status_search` field recording what was done to check that the problem
is still open: the query or fetch, what came back, and what was and was not read. The second session
hit the session's web-search limit (200 searches) part-way through; the rows written after that point
(`F0131`-`F0139`) say so and were checked through arXiv abstract fetches and the arXiv API (`raw/api_status_20260909.txt`),
which returned HTTP 429 on some queries. The leads worth naming:

- F0117, F0119 (Potts reconstruction): the Kesten-Stigum bound is the exact threshold for q = 3 on trees of
  large degree (Sly 2011) and non-reconstruction below it holds for q = 3, 4 at large average degree
  (Mossel-Sly-Sohn 2023), while for q >= 5 the bound is not sharp; both rows are admitted only for the
  small-degree regime, and F0117's expected answer for q = 3, 4 is "no".
- F0120 (colourings): Sly 2009 locates the threshold at q(log q + log log q + 1 + O(1)); the row asks for
  fixed small (b, q).
- F0124 (RWRS crossover at p = 4/5): the "all bad below 4/5" half is a theorem (Blachere, den Hollander,
  Steif 2011); the "all good above 4/5" half is proved only near p = 1.
- F0127 (coalescence time twice the meeting time): Oliveira 2013 proves it for vertex-transitive graphs
  with mixing time much smaller than the meeting time; the row asks whether the source's condition (5.2)
  alone suffices.
- F0129 (Durrett-Rogers conjecture): Mountford-Tarres 2008 prove it for a non-compactly supported
  interaction; Tarres-Toth-Valko 2012 prove it partially; the compactly supported case in the row is open.
- F0131, F0132 (sandpile shapes and identity): existence of the point-source scaling limit is Pegden-Smart
  2013; polygonality is not claimed anywhere found; F0132 may already follow from Pegden-Smart's pattern
  stability paper (2020), which was not read.
- F0133 (chi = chi*): Dabrowski 2017 for convex free Gibbs laws; the general problem is open.
- F0135-F0137 (Dirichlet environments): status checked only through the source (2016) and the Codex tree's
  reference list; Bouchet-Ramirez-Sabot and Fribergh-Kious should be read before attempting F0137.
- F0138 (narrow-wedge KPZ two-point law): follows from convergence of the KPZ equation to the KPZ fixed
  point. The published proof (Quastel-Sarkar, JAMS 2023) has its arXiv text withdrawn (v7, May 2025) with a
  stated gap; two independent preprints claim the result (Virag 2020; Wu 2023, v3 April 2025). Admitted under
  the campaign's admit-when-in-doubt rule, to be reclassified when one of them is published.
- F0139 (QLE for all parameters): Ang-Mithal (May 2026) construct a quantum-natural-time variant on the same
  special curve; the full range is still open.
- F0065, F0067 (height o(sqrt n) for critical infinite-variance and for subcritical simply generated trees):
  Addario-Berry, Brandenberger, Hamdan, Kerriou 2022 prove ht(T_n)/(n^{1/2} log^3 n) -> 0 in both cases
  ("nearly proves the first and third points"); the log^3 n is what remains. The width halves of the same
  four-point conjecture are their theorem and are excluded below (F0066, F0068).
- The first session's leads (F0001-F0111) are in their rows; the ones it flagged are F0001-F0003
  (singularity probabilities, partial results by Tikhomirov and by Campos-Jenssen-Michelen-Sahasrabudhe),
  F0022-F0025 (planar percolation exponents), F0089 (Nienhuis point: n = 0 is Duminil-Copin-Smirnov 2012,
  n = 1 is the Ising point, and for n in [1,2] Duminil-Copin, Glazman, Peled, Spinka 2021 prove macroscopic
  loops at the conjectured point without identifying it as the critical point), F0095-F0099 (Frieze's list).

## The twenty-nine exclusions

Each exclusion quotes the source's statement and the resolving paper's own words in `resolved_by`, and
compares the objects by name. Three rest on the source's own text rather than on an external search (the
E-ledger's audit found that this is the safest kind), and two (F0066, F0068) came from a lead sent by
another agent on the mesh and were verified against the paper's text before being applied.

1. F0040 — permanent of a random symmetric Rademacher matrix: Kwan-Sauermann (Selecta 2022).
2. F0041 — second eigenvalue of a random regular graph: Huang-McKenzie-Yau (2024), edge universality.
3. F0042 — delocalisation with the hammock potential: Milos-Peled.
4. F0043 — Talagrand's convexity conjecture: Hua-Song-Tudose (May 2026 preprint; check before relying on it).
5. F0044 — the Bernoulli conjecture: Bednorz-Latala (Ann. Math. 2014).
6. F0045 — selector process conjecture: Park-Pham (Ann. Math. 2024).
7. F0046 — Kahn-Kalai conjecture in Talagrand's form: Park-Pham (JAMS 2024).
8. F0047 — Pfaffian structure of the Brownian net's branching-coalescing point set: Garrod-Tribe-Zaboronski.
9. F0048 — the stable web: Mountford-Ravishankar-Valle (ALEA 2019).
10. F0049 — Hamiltonicity threshold of random hypercube subgraphs: Condon, Espuny Diaz, Girao, Kuhn, Osthus.
11. F0050 — non-singularity of random regular adjacency matrices: Huang (Duke 2021).
12. F0051 — one-endedness of wired minimal spanning forest trees: Timar (Ann. Probab. 2006), as the source itself states.
13. F0052 — SLE hull boundary dimension and reversibility: SLE duality (Zhan; Dubedat) and reversibility (Zhan; Miller-Sheffield).
14. F0053 — Kerov's conjecture: Matveev.
15. F0054 — aging for the REM under Metropolis: Gayrard (PTRF 2019).
16. F0079 — localisation in high dimensions for the quartic interaction: Magazinov-Peled.
17. F0112, F0113 — weakly-small selector conjecture and its lower bound: Park-Pham (Ann. Math. 2024).
18. F0114, F0115 — fractional Kahn-Kalai and the spread-family hitting statement: Frankston-Kahn-Narayanan-Park (Ann. Math. 2021).
19. F0121 — Peres's bounded-memory local-algorithm conjecture: Jain-Koehler-Liu-Mossel (COLT 2019); the row records the simulation argument that puts the source's class inside theirs, with the one caveat to check.
20. F0122 — robust reconstruction below Kesten-Stigum: the survey's own Section 8 ("as conjectured in [30]", Janson-Mossel 2004).
21. F0123 — information decay iff Glauber gap: the survey's own Section 8 ("gives a positive answer to Problem 3", Martinelli-Sinclair-Weitz 2004); the general-reversible-channel scope is the one thing to verify.
22. F0128 — Aldous's FPP weak law: Aldous 2016, Theorem 8, "conjectured in [2] sec. 7.4" with [2] the source.
23. F0130 — recurrence of ERRW on Z^d: Disertori-Sabot-Tarres (transience for small reinforcement, d >= 3) and Sabot-Zeng (recurrence in d = 2); the answer is "not in general".
24. F0134 — genus expansion of the quartic matrix integral: the survey's own p. 56 ("proved very recently by McLaughlin and Ercolani"), Ercolani-McLaughlin (IMRN 2003).
25. F0140 — mutual information limit of the sparse assortative 2-SBM: Abbe-Cornacchia-Gu-Polyanskiy 2021 outside SNR in (1, 3.513), Yu-Polyanskiy 2024 closing the window.
26. F0066 — width of critical infinite-variance simply generated trees grows faster than sqrt n (Janson Conjecture 20.6, published 21.6): Addario-Berry, Brandenberger, Hamdan, Kerriou, EJP 2022, Section 5 ("This proves the second and fourth points of the above conjecture"), their Conjecture 1 point (2) being the source's statement verbatim.
27. F0068 — width of subcritical simply generated trees grows faster than sqrt n (Janson Problem 20.8, published 21.8): same paper, point (4); answer yes.

Exclusions I was unsure about, in decreasing order of doubt: F0123 (rests on one sentence of the survey; the
cited paper was not read and may cover only Ising and Potts channels); F0121 (the simulation of an
l-generation, r-bit scheme by a bounded-alphabet message-passing scheme is my argument, and whether the COLT
theorem allows inhomogeneous update rules was not verified); F0043 (a 2026 preprint). Everything else quotes
a published theorem whose objects match the source's.

## The ten easiest admitted problems, in my judgement

1. F0138 — the two-point Airy_2 law for narrow-wedge KPZ: it is the one-time marginal of the KPZ fixed point
   convergence claimed by two preprints; reading one of them is the whole task.
2. F0132 — scaling limit of the sandpile identity: reduces (attempt) to Pegden-Smart's pattern stability on
   the square with a Dirichlet boundary, applied twice; likely already a corollary of their work.
3. F0057 — total variation version of Janson's large-box count theorem: the Kolmogorov-distance version is
   proved and the attempt shows the same local error term does the job.
4. F0063 — uniform integrability of moments of generation sizes: any moment condition slightly stronger than
   E xi^{r+1} < infinity already works (attempt); what is left is a uniform local limit theorem.
5. F0116 — census reconstruction fails at the Kesten-Stigum critical point: reduces to a total-variation
   local CLT for a critical multitype Galton-Watson census, a known kind of statement.
6. F0055 — largest box is o_p(log n) when m/n -> 0: the source calls it almost obvious, and while this README
   was being written another agent appended a short direct proof (F0055-A002, see below), which I checked
   line by line; it needs a reviewer, not new ideas.
7. F0056 — Poisson limit for the number of large boxes when m/n -> 0: the same missing lemma as F0055 and
   nothing else.
8. F0064 — Kolchin's normality of outdegree counts without moment conditions: the limit law is predicted
   explicitly in the attempt; the proof needs a bivariate local limit theorem with mixed scalings.
9. F0036 — local finiteness of potential most recent common ancestors in the Brownian net: the attempt
   already reduces it to a single path-ordering lemma for net paths.
10. F0119 — the 3-state Potts reconstruction region on small trees: the open window on the binary tree is
    lambda in (2/3, 0.7071]; a numerical belief-propagation iteration would give the conjectural answer in an
    afternoon, though a proof is another matter.

## What the attempts are and are not

None of the 113 attempts written by this agent is a claimed solution. The one claimed solution in the file
is not mine: at 02:52:41Z on 2026-09-09, while this directory was under my mesh write claim, the agent
`claude-prob1000-e0077-0908` appended `F0055-A002` and set the F0055 row's `result_status` to `proved`. Its
argument for Janson's Conjecture 18.4 (largest box is o_p(log n) when m/n -> 0) compares partition
functions directly: a configuration of m - j balls in n - 1 boxes has at least C(n-1-m, j) images under
"put j singletons into empty boxes and append an empty box" and each target has at most C(m, j) preimages,
so P(Y_1 = j) <= (w_j/w_0)(2m/(gamma n))^j for m <= n/4 with gamma = min(1, w_1/w_0); with w_j <= Phi(r) r^{-j}
and a union bound over boxes, Y(1) <= (1 + delta) log n / log(gamma r n/(2m)) w.h.p., which is o(log n). I
re-derived the counting inequality and the tail bound and found no error; the w_1 = 0 case is handled in the
row by a Frobenius-type argument I did not check. As holder I changed the row's `result_status` to the
campaign's schema value `candidate_full_solution` (verification `unreviewed`) and told the author on the mesh;
its write-up is `Downloads/Probability_F0055_Janson_conjecture_18_4_largest_box_2026-09-09.md`. It is
author-checked by one other agent (me), not independently reviewed in the campaign's sense.

Six admitted rows are flagged `partial_result` (two more, F0066 and F0068, carried partial results until
they were excluded; their attempts remain in the file); the new one is
F0133, which combines the source's own Remark 7.2 with the refutation of the Connes embedding conjecture
(MIP* = RE) to show that the unrestricted form of the unification problem chi = chi* is false, so the
hypothesis chi > -infinity in Guionnet's Conjecture 7.1 is essential. Two attempts record a tension between
two of a source's questions rather than a result: F0125 and F0126 show that den Hollander-Steif's Questions 6
and 7 cannot both have the answer yes (a two-colour scenery with small bias against simple random walk
separates them), and that Question 6 as literally written needs "recurrent" added. F0118 shows that the
"obvious" case of the monotonicity conjecture (q_1 divides q_2) is the only case reachable by a vertex-wise
degradation, so a proof must be global. Everything else is a reduction, a calibration against a known bound,
or a localisation of the difficulty, written so that the obstruction field says exactly what is missing.

## Merge rule for the campaign holder

1. Remap `F####` to the next free `P####`, keeping `dedup_key` and adding `origin_id: F####`.
2. Append the 53 `sources.jsonl` rows, copying the source folders into
   `Downloads/Probability_1000_20h_20260906/sources/` under the same ids; `pemantle_reinforcement_2007`
   and `lyons_peres_book_2026` duplicate URLs already in that tree and can be aliased instead.
3. Append problems and attempts; recompute the campaign `STATUS.json`.
4. The twenty-nine exclusions were checked against the source's own sentence and the cited paper's own
   abstract or text, not against the cited papers' full proofs. Treat them as claims to verify, starting
   with F0123, F0121 and F0043.
5. Nothing here is a promoted original solution. The eight `partial_result` rows are author-checked only;
   the F0055 candidate solution has been checked by its author and by me and needs a reviewer before it is
   counted.
