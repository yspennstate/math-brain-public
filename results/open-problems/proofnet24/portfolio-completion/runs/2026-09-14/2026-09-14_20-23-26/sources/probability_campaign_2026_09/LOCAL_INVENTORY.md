# Local inventory: Probability open-problems campaign (Sep 2026)

Catalogue only — no mathematical evaluation performed. Compiled 2026-09-14 by filesystem search.
All paths are on this machine (Windows, user `owner`). Dates below are the write-up's own dateline
(usually also its mtime); "campaign" = the multi-agent "Probability 1000" effort that ran
2026-09-06 through 2026-09-14 across a Codex 20h run and Claude intakes labelled C-I.

---

## A. Ledger / index files (CSV / JSON / MD), with row counts

| File | Rows (incl. header where CSV) | Notes |
|---|---|---|
| `~/Downloads/Probability_open_problems_list_2026-09-07.csv` | 624 | master candidate list, 7 Sep snapshot |
| `~/Downloads/Probability_open_problems_list_2026-09-07.md` | (139,990 bytes) | same, prose/markdown form |
| `~/Downloads/Probability_open_problems_ranked_2026-09-07.csv` | 559 | tiered/ranked version of the list |
| `~/Downloads/Probability_open_problems_ranked_2026-09-07.md` | (78,653 bytes) | annotated ranked list |
| `~/Downloads/Probability_1000_20h_20260906/problems.jsonl` | 611 | Codex campaign problems ledger (20h run) |
| `~/Downloads/Probability_1000_20h_20260906/attempts.jsonl` | 466 | Codex campaign attempts ledger |
| `~/Downloads/Probability_1000_20h_20260906/sources.jsonl` | 260 | Codex campaign sources ledger |
| `~/Downloads/Probability_1000_20h_20260906/STATUS.json` | - | campaign run-state snapshot, 7 Sep 09:32 UTC |
| `.../06_math_research/probability_1000_intake_claude_20260907/problems.jsonl` | 160 | Claude intake C |
| `.../06_math_research/probability_1000_intake_D_20260908/problems.jsonl` | 102 | Claude intake D (+ CORRECTIONS.md) |
| `.../06_math_research/probability_1000_intake_E_20260908/problems.jsonl` | 115 | Claude intake E (+ CORRECTIONS.md) |
| `.../06_math_research/probability_1000_intake_F_20260908/problems.jsonl` | 154 | Claude intake F |
| `.../06_math_research/probability_1000_intake_G_20260910/problems.jsonl` | 15 | Claude intake G |
| `.../06_math_research/probability_1000_intake_H_20260914/problems.jsonl` | 34 (+ intake_H_candidates.md, intake_H_verification.md) | Claude intake H |
| `.../06_math_research/probability_1000_intake_I_20260914/problems.jsonl` | 200 | Claude intake I (7th ledger) |
| `.../06_math_research/probability_1000_attempts_H_20260912/` (dir) | - | lane_Q1, g0013 scripts, BRAIN_USAGE*.jsonl |
| `.../06_math_research/probability_1000_attempts_I_20260914/` (dir) | ~75 files | check/search scripts for every I-series and late F/H/P problem, plus copies of write-ups |
| `.../06_math_research/prob1000_lean_20260908/` (dir) | - | Lean files + RANKED_LIST annotated, REPORT_*.md copies, NIGHT_REPORT_2026-09-08.md |

`06_math_research` full prefix: `~/<private-repo>/06_math_research/` (also mirrored under `~/math-open-problems-p300/`, apparently a git worktree/copy, as of 2026-09-14).

Full base dir of the Codex 20h run, with proofs/ (25 written arguments), sources/ (~90 fetched papers), qa/ page images, typeset_staging/:
`~/Downloads/Probability_1000_20h_20260906/`

---

## B. Report chapter file(s) - the "100-page" 13-14 Sep report

Primary consolidated report (17,394 lines / ~2.26 MB markdown, PDF companion 3.3 MB, most recently
built 2026-09-14 12:47):

- `~/Downloads/Probability_1000_report_2026-09-12/Probability_1000_open_problems_report_2026-09-12.md`
- `~/Downloads/Probability_1000_report_2026-09-12/Probability_1000_open_problems_report_2026-09-12.pdf`
- (top-level duplicate) `~/Downloads/Probability_1000_open_problems_report_2026-09-12.pdf`

Assembled from chapter fragments in `.../Probability_1000_report_2026-09-12/chapters/`:
- `00_front.md`, `01_campaign.md`, `02_what_is_solved.md`
- `10_attempts_H.md`
- **`12_results_I_13_14_september.md`** (119 KB) - the chapter of the 13-14 September results (Janson problems 18.9/18.30/18.39/18.40/18.41/18.42/20.1/20.2/20.3/20.4, Aldous-Fill 4.45/4.48/4.49/7.31, Hasebe-Ueda 3.3/3.11, Sylvester-Hadamard discrepancy, sign-matrix discrepancy, derivative-martingale correction, frog model, random drift, Neri-Pinto, layer distribution)
- `14_open_and_next.md`, `99_appendix.md`
- `catalog_01..04_codex_P0001_P0590.md`, `catalog_05_intake_C.md`, `catalog_06_intake_D_and_G.md`, `catalog_07_intake_E.md`, `catalog_08_intake_F.md`, `catalog_09_codex_R_series.md` - full raw catalogue of ~1,000 candidate problems (mostly still open; not itemised individually below)
- `results_A_codex_candidates.md`, `results_B_settled_and_audits.md`, `results_C_close_to_solved.md`

Earlier / superseded whole-report snapshots (same lineage, earlier dates):
- `~/Downloads/Probability_1000_20h_20260906/Probability_Open_Problems_Working_Report.md` (+.pdf), 7 Sep 01:55
- `~/Downloads/Probability_1000_20h_20260906/Probability_Open_Problems_Typeset.md` (+.tex,.pdf), 7 Sep 11:33
- `~/Downloads/PDF deliverables 6-7 Sep 2026/8 - Probability open problems - working report (Codex 20h, 7 Sep).pdf`

---

## C. Consolidated "settled" summaries (closest things to a finished ledger)

- `~/Downloads/Probability_open_problems_thirteen_settled_2026-09-08.md` - the "thirteen settled" writeup (13 results narrated in full, 8 Sep), mirrored as `.../prob1000_lean_20260908/REPORT_thirteen_settled_2026-09-08.md`
- `~/Downloads/Probability_open_problems_night_report_2026-09-08.md` - "night of 8 September" roundup (E/D/P-series settled + attacked)
- `~/Downloads/Probability_five_problems_attacked_2026-09-08.md` - afternoon-session companion (Ross's 2nd conjecture closed, 4 others reduced), mirrored as `.../prob1000_lean_20260908/REPORT_five_attacked_2026-09-08.md`
- `chapters/02_what_is_solved.md`, `results_B_settled_and_audits.md`, `results_C_close_to_solved.md` - the report's own running "what was solved" / "what is close" sections (Summary table at report line ~2872 lists 12 candidate_full_solution P0xxx rows with verification/prior-art/gap columns)
- `chapters/12_results_I_13_14_september.md` - everything settled/refuted/reduced on 13-14 Sep (superset of the individual Downloads memos below)
- `~/probability-hard-problems-20260910/HARD_FRONTIER.md`, `ACTIVE_DIRECTION.md`, `CAYLEY_RETIRED_20260910.json` - bookkeeping for the retired Cayley/product-condition line and the free-Brownian-curvature line
- `~/Downloads/Probability_Publishability_20260910/AUTHOR_DECLARATIONS.md`, `README.md`, `PAPER_README.md`, `FORMALIZATION.md`, `CAYLEY_FORMALIZATION*.md` - publishability audit notes for the flagship results
- `~/Downloads/SESSION_HANDOFF_probability_2026-09-09.md` - 9 Sep handoff between agents

---

## D. Inventory of individual problems (one row per problem)

Status legend: PROVED = campaign claims full solution; REFUTED = counterexample to the stated
conjecture; REDUCED = restated as an equivalent, narrower, or explicit remaining question;
PARTIAL = a nontrivial special case or one direction settled, general case open; EVIDENCE =
computational/heuristic support only, no proof; KNOWN = campaign's argument correct but result
already in the literature (no credit claimed). All statuses are the campaign's own self-report.

| id | source | statement | status | write-up path(s) | code/Lean path(s) | date |
|---|---|---|---|---|---|---|
| P0208 | Aldous-Fill, OP 7.27 | arc-transitive graphs (excl n-cycles): tau*=O(n log n), tau2=O(n), tau*/2tau0->1? | REFUTED all 3 clauses | Downloads/Probability_open_problems_thirteen_settled_2026-09-08.md sec.1; report ~line 1281 | prob1000_lean_20260908/P0208.lean (9 thm); proofs/P0208_wreath_graph_counterexample_candidate.md | 2026-09-08 |
| P0340 | Aldous-Janson arXiv:2303.02529 OP14 | drawn length of DTCS(n) ~ n log^4 n ? | REFUTED, drawn length is Theta(n) | thirteen_settled...md sec.2 | prob1000_lean_20260908/P0340.lean (4 thm); proofs/P0340_beta_tree_drawn_length_counterexample_candidate.md | 2026-09-08 |
| P0193 | Hasebe Ueda Wang arXiv:2009.13848 Pb 4.7 | exists D: sigma_t boxtimes nu log-unimodal for t>=D on [a,b] 0<a<b ? | REFUTED, no such D | thirteen_settled...md sec.3 | proofs/P0193_compact_multiplicative_nonunimodality_candidate.md | 2026-09-08 |
| P0266 / P0267 | Agresti Veraar 2025 Problems 4,5 | E sup norm bound and continuity for critical Allen-Cahn gamma2=2 | REFUTED both | thirteen_settled...md sec.4 | proofs/P0266_P0267_critical_allen_cahn_counterexamples_candidate.md; Downloads/Critical_Allen_Cahn_paper_and_Lean.zip | 2026-09-08 |
| P0209 | Aldous-Fill OP 4.30 | universal psi bound on CLT deviation for additive functionals | REFUTED | thirteen_settled...md sec.5 | proofs/P0209_uniform_clt_counterexample_candidate.md | 2026-09-08 |
| Bradley Q7 / D0035 | Bradley arXiv:math/0511078 Q7 | every nonincreasing b_n in [0,1] realised as phi(n)? | REFUTED literal form | thirteen_settled...md sec.6 | - | 2026-09-08 |
| Pollett Sec2 Conj(ii) | Pollett Section 2 Conjecture ii | lambda-transient limit factors as A x_i m_j? | REFUTED, probably known | thirteen_settled...md sec.7 | - | 2026-09-08 |
| P0032 | Burdzy Scheutzow arXiv:1302.6958 Pb 7.5 | can a process equiv-in-law to BM be prefixed to become BM? | PROVED yes | thirteen_settled...md sec.8; report line 647 | proofs/P0032_brownian_prefix_candidate.md | 2026-09-08 |
| P0276 | Salez arXiv:2508.21055 Pb 2.4 | cutoff iff product condition on abelian Cayley graphs? | REFUTED literal statement | thirteen_settled...md sec.9; report line 1719 | Downloads/Shmalo_Cayley_Product_Condition.tex/.pdf, cayley_paper.tex/.pdf, CayleyAlgebra.lean, CayleyCore.lean, EndpointCore.lean; retired 09-10 (probability-hard-problems-20260910/CAYLEY_RETIRED_20260910.json) | 2026-09-08, retired 09-10 |
| P0033 | Lyons Peres Q17.18 | equivariant flow rule w/ stationary law equiv to GW implies ergodic? | REFUTED | thirteen_settled...md sec.10; report line 769 | proofs/P0033_stationary_flow_counterexample_candidate.md | 2026-09-08 |
| Hasebe-Ueda 3.3 (1st pass) | Hasebe Ueda ALEA 15 (2018) Pb 3.3 | optimal C with mu boxplus S(0,t) unimodal t>=C D^2 | PROVED C=1, notes fork vs printed C>=2 | thirteen_settled...md sec.11 | - | 2026-09-08 |
| P0341 | Aldous-Janson "Ansatz 20" inside OP8 | two convergence-transfer claims for descent chain | REFUTED both parts | thirteen_settled...md sec.12; report line 2315 | proofs/ | 2026-09-08 |
| P0189 | Brown-measure/strong-conv literature | strong convergence implies Brown-measure convergence of u+v? | PARTIAL, concrete half confirmed | thirteen_settled...md "Also P0189"; report line 1033,5291 | proofs/P0189_brown_measure_strong_convergence_counterexample_candidate.md | 2026-09-08 |
| E0077 | Asanjarani Nazarathy arXiv:1905.01736 Conj4.1 | irreducible MMPP: c^2>=1? | PROVED, later noted excluded by He 2021 prior art | Downloads/Probability_E0077_MMPP_scv_proved_2026-09-08.md; report line 3958 | prob1000_lean_20260908/E0077.lean (6 thm) | 2026-09-08 |
| E0078 | Asanjarani Nazarathy Conj4.2 | irreducible MMPP: T1pi >=_st T1alpha? | REFUTED | Downloads/Probability_E0078_MMPP_stochastic_order_refuted_2026-09-08.md; report line 4044 | - | 2026-09-08 |
| E0105 / E0104 | Konstantopoulos arXiv:1407.6834 OP2,3 | law of detection time of a ball before an enemy point/2nd ball | SETTLED homogeneous case | Downloads/Probability_E0105_inertial_Boolean_detection_before_a_point_2026-09-08.md; report line 6537 | prob1000_lean_20260908/e0105.py | 2026-09-08 |
| E0060 | Rozikov arXiv:0902.4207 Pb3 | exists transversal Volterra QSO w/ periodic itinerary? | ANSWERED YES | night_report...md sec Settled; report line 4212 | prob1000_lean_20260908/e0060.py | 2026-09-08 |
| E0061 | Rozikov Pb4 | same-sign nonzero a,b,c sufficient for Volterra ergodic thm on S^2? | PROVED sufficiency | Downloads/Probability_E0061_Volterra_ergodic_theorem_sufficiency_2026-09-08.md; report line 3739 | prob1000_lean_20260908/E0061.lean | 2026-09-08 |
| E0063 | Rozikov Pb10 | every xi-QSO converges to empty-body fixed point? | PROVED | Downloads/Probability_E0063_xi_QSO_converge_to_empty_body_2026-09-09.md | prob1000_lean_20260908/E0063.lean | 2026-09-09 |
| E0064 | Rozikov 2009 Pb11 | Thm6 unique non-attractive fixed point true for m>=4? | REFUTED m>=5 (2 fixed pts); m=4 separate | Downloads/Probability_E0064_strictly_nonVolterra_fixed_point_uniqueness_fails_for_five_types_2026-09-11.md; report line 3881,5492 | prob1000_lean_20260908/e0064_m5_exact.out, e0064_face_construction.py, .npy | 2026-09-11 |
| E0046 | Bandeira 2015 OP1.2 complex half | alpha_C(n) decreases in n? | PROVED indep., then found settled (Hutnik 2608.12151) - KNOWN | Downloads/Probability_E0046_complex_Ginibre_average_singular_value_decreasing_2026-09-08.md; report line 4150 | prob1000_lean_20260908/E0046.lean | 2026-09-08 |
| D0016 / D0018 | Khoshnevisan arXiv:math/0510518 OP1,3 | Brownian-sheet slice zero-sets finite/<=2 double pairs d=3/5? | SETTLED d=3,5; d=2,4 open | night_report...md sec Settled; report line 6226 | - | 2026-09-08 |
| F0055 | Janson 2012 Conj18.4 | for m/n->0, largest box Y1=o_p(log n)? | PROVED | Downloads/Probability_F0055_Janson_conjecture_18_4_largest_box_2026-09-09.md; report line 4294 | prob1000_lean_20260908/F0055.lean | 2026-09-09 |
| F0057 | Janson 2012 Pb18.10 | d_TV(Yj,xi_j)->0 for every j? | PARTIAL, pending source correction | Downloads/Probability_F0057_Janson_problem_18_10_total_variation_2026-09-09.md; report line 4385,5175 | - | 2026-09-09 |
| F0056 | Janson 2012 Pb18.9 | Thm18.7 extends to lambda=0<nu? | PROVED yes when w1>0 | Downloads/Probability_F0056_Janson_problem_18_9_complete_answer_2026-09-13.md | probability_1000_attempts_I_20260914/f0056_check.py, janson_cond_check.py | 2026-09-13 |
| F0090 | Kalai ICM2018 Conj8 = GPS OP1 | H(S(f))=O(I(f)), H(P(f))=O(I(f)) for percolation crossing? | PROVED (square); closed 09-13 by author publication | Downloads/Probability_F0090_Kalai_conjecture_8_entropy_influence_percolation_2026-09-10.md; report line 4499 | prob1000_lean_20260908/f0090_pivotal_scale_sum_mc.py, f0090_small_box_check.py | 2026-09-10, closed 09-13 |
| F0058 | Janson 2012 Pb18.30 | Thm18.7(ii)-(iii) hold at lambda=nu, sigma^2=inf? | REFUTED both parts | Downloads/Probability_F0058_Janson_problem_18_30_part_ii_fails_2026-09-14.md | probability_1000_attempts_I_20260914/toy_1830.py, toy_1830_iii.py | 2026-09-14 |
| F0059 | Janson 2012 Pb18.39 | Y1/n->_p 0 impossible when 0<nu<lambda? | REDUCED to a rate-function property | Downloads/Probability_F0059_Janson_problem_18_39_reduction_2026-09-14.md | - | 2026-09-14 |
| F0060 | Janson 2012 Pb18.40 | Y1/n->_p 0 possible when nu=0? | REFUTED, answered no | Downloads/Probability_F0060_Janson_problem_18_40_answered_no_2026-09-14.md | probability_1000_attempts_I_20260914/f0060_largest_box.py | 2026-09-14 |
| F0061 | Janson 2012 Pb18.41 | monotone weights force single-box condensation? | REFUTED | Downloads/Probability_F0061_F0062_Janson_problems_18_41_18_42_answered_no_2026-09-14.md | probability_1000_attempts_I_20260914/check_1841_np.py | 2026-09-14 |
| F0062 | Janson 2012 Pb18.42 | exploding ratios force single-box condensation? | REFUTED | same file as F0061 | same | 2026-09-14 |
| F0063 | Janson 2012 Conj20.1 | level widths l_k(T_n)^r unif. integrable for r>0,nu>0? | PROVED for real r>=1, one boundary case open | Downloads/Probability_F0063_Janson_conjecture_20_1_level_widths_uniformly_integrable_2026-09-14.md | - | 2026-09-14 |
| F0064 | Janson 2012 Pb20.2 | outdegree-count normality unconditional beyond reg. variation? | (a) already yes lit.; (b)(c) REFUTED in general | Downloads/Probability_F0064_Janson_problem_20_2_outdegree_counts_not_normal_in_general_2026-09-14.md | probability_1000_attempts_I_20260914/toy_202_bimodal.py | 2026-09-14 |
| I0020 (F0064b) | Janson 2012 Pb20.3 | N_d normality extends to general balls-in-boxes? | ANSWERED yes 2 regimes, no other 2 | Downloads/Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md | - | 2026-09-14 |
| I0021 (F0064b) | Janson 2012 Pb20.4 | fringe-subtree analogue of 20.3 | ANSWERED per memo title | same file | - | 2026-09-14 |
| I0022 (F0064b) | Janson 2012 Pb20.11 | third untracked problem | left unresolved | same file | - | 2026-09-14 |
| P0289 / H_P0289 | Leskela Queueing Systems 100 (2022) 213-215 Pb1 "Ross's 2nd conjecture" | faster modulation always lowers mean stationary workload of Cox queue? | REFUTED, counterexample completed | Downloads/Probability_five_problems_attacked_2026-09-08.md sec.1; Downloads/Probability_H_P0289_ross_second_conjecture_expansion_rederived_2026-09-12.md | prob1000_lean_20260908/p0289.py, p0289b.py; probability_1000_attempts_H_20260912/lane_Q1/ | 2026-09-08, re-derived 09-12 |
| P0291 | Leskela Pb3 (arXiv Pb2) | exists non-monotone stationary ergodic CTMC satisfying property (2)? | ANSWERED YES 3-state star chain | Downloads/Probability_P0291_Leskela_problem_3_nonmonotone_chain_with_supermodular_time_ordering_2026-09-10.md; report line 4595 | prob1000_lean_20260908/p0291_*.py | 2026-09-10 |
| H0010 (=G0014 conj) | Kumar Duddala arXiv:2608.21125 Prop3.1/Conj3.2 | is deriv. martingale dW_n unif. integrable iff dW_inf>0 a.s.? | REDUCED/CORRECTED, conditions shown incompatible, UI replaced by nondegenerate | Downloads/Probability_H0010_derivative_martingale_conjecture_is_inverted_2026-09-14.md | - | 2026-09-14 |
| H0013 / H0014 (H0012) | arXiv:2607.07410 Remark5.3(ii) | can random Levy drift break compactness of confining diffusion semigroup for delta>1/alpha? | ANSWERED yes for every delta | Downloads/Probability_H0013_H0014_random_drift_destroys_compactness_for_every_delta_2026-09-14.md | probability_1000_attempts_I_20260914/h0013_hardy.py, h0013_jumps.py | 2026-09-14 |
| H0019 | Stepanyants Krapivsky Hartle Krioukov arXiv:2608.04303 Conj1,2 | tail asymptotics of RRT layer distribution l_k; max layer ~e log n | REDUCED to branching random walk (Poisson-weighted infinite tree) | Downloads/Probability_H0019_layer_distribution_of_random_recursive_trees_2026-09-14.md | probability_1000_attempts_I_20260914/h0019_front.py, h0019_layer_identity.py, h0019_layers.py, h0019_mc.py | 2026-09-14 |
| H0020 | Neri Pinto arXiv:2607.07309 Remark3.7 | is lambda_max(...)<0 for p=d or d-1 for all tenable irreducible urns? | REFUTED both halves | Downloads/Probability_H0020_Neri_Pinto_urn_contractivity_fails_2026-09-14.md | probability_1000_attempts_I_20260914/h0020_search.py, h0020_search2.py, h0020_search3.py | 2026-09-14 |
| H0024 | Oshiro de Carvalho Machado Ramirez-Gonzalez arXiv:2607.27082 Thm3.1/Rmk3.6 | full phase diagram on critical line of interval-activation frog model? | PARTIAL/REDUCED, factor-4 gap explained, firework critical constant c=1 computed | Downloads/Probability_H0024_frog_model_critical_line_factor_four_2026-09-14.md | probability_1000_attempts_I_20260914/h0024_drift.py, h0024_exp.py, h0024_exp2.py, h0024_fast.py, h0024_firework.py, h0024_thresh.py | 2026-09-14 |
| P0242 | Aldous-Fill OP4.45 | is tau1(2) of lumped chain <= K*tau1(2) of original, K=1? | REFUTED for K=1 | Downloads/Probability_P0242_Aldous_Fill_open_problem_4_45_lumping_2026-09-14.md | probability_1000_attempts_I_20260914/verify_242.py | 2026-09-14 |
| P0243 | Aldous-Fill OP4.48 | (a) tau1<=tau0? (b) tau2<=tau1(2)? | (a) REFUTED; (b) PROVED yes | Downloads/Probability_P0243_Aldous_Fill_open_problem_4_48_2026-09-14.md | probability_1000_attempts_I_20260914/p0243_opt.py, p0243_search.py, p0243_verify.py | 2026-09-14 |
| I0026 | Aldous-Fill OP4.49 | (i) simple proof of Sinclair flow ineq? (ii) log n replaced by diameter? | (ii) EVIDENCE only, max ratio R(G)=2 on graphs to 16 vtx; (i) separate direct attempt | Downloads/Probability_I0026_Aldous_Fill_open_problem_4_49_evidence_2026-09-14.md; Downloads/Probability_I0026_aldous_fill_449_flow_cut_2026-09-14.md | probability_1000_attempts_I_20260914/af449_families.py, af449_flows.py | 2026-09-14 |
| I0031 | Aldous-Fill OP7.31 | distance-regular graphs (excl n-cycles): tau0=O(n)? | REDUCED to intersection-array identity + EVIDENCE, Biggs value reproduced as max over 13 cubic DRGs | Downloads/Probability_I0031_distance_regular_hitting_times_2026-09-14.md | probability_1000_attempts_I_20260914/drg_check.py, drg_families.py, drg_feasible.py, drg_hitting.py, drg_products.py, drg_sumu.py | 2026-09-14 |
| I0082 | Hasebe Ueda ALEA15(2018) Pb3.11 | exists non-delta freely strongly unimodal measure? | PARTIAL, Cauchy laws (and attraction domain) excluded | Downloads/Probability_I0082_free_strong_unimodality_cauchy_2026-09-14.md | probability_1000_attempts_I_20260914/cauchy_bad_nu.py, free_stable*.py, free_subord.py, free_sweep.py, free_uniform.py, free_unimod*.py, stable_unimodal.py | 2026-09-14 |
| I0086 | Hasebe Ueda ALEA15(2018) Pb3.3 | optimal C with mu boxplus S(0,t) unimodal t>=C D^2? | PROVED C=1 exactly (cleaner restatement of 09-08 result) | Downloads/Probability_I0086_free_brownian_unimodality_sharp_constant_2026-09-14.md | probability_1000_attempts_I_20260914/c1_endtoend.py | 2026-09-14 |
| (classical companion to I0086) | same paper, classical BM case | sharp constant for unimodality of classical BM w/ compact initial law | PROVED, constant is D^2/4 vs 36x larger bound in source | Downloads/Probability_classical_brownian_unimodality_sharp_constant_2026-09-14.md | probability_1000_attempts_I_20260914/classical_unimodal.py | 2026-09-14 |
| I0092 | Randomstrasse 2024 list Conj13 | disc(H_k)=sqrt2*sqrt(2^k) for odd k? | REFUTED, true only k in {1,3,5,7}, fails k>=9 (Reed-Muller covering radius, known since 1983) | Downloads/Probability_I0092_sylvester_hadamard_discrepancy_conjecture_false_2026-09-14.md | probability_1000_attempts_I_20260914/hadamard_disc.py, hadamard_disc2.py, paley_theta.py, pw15.py, pw15_search.py | 2026-09-14 |
| I0095 | Randomstrasse 2024 list OP11 | sup_n sup_A disc(A)/sqrt n = ? | PARTIAL/EVIDENCE, exact max disc(A) for n<=11, lower bound improved to 5/3 | Downloads/Probability_I0095_sign_matrix_discrepancy_exact_small_values_2026-09-14.md | probability_1000_attempts_I_20260914/disc_audit.py, disc_covering.py, disc_hunt.py, disc_lower2.py, disc_max.py, disc_n12.py, disc_small.py, disc_table24.py, disc_verify.py | 2026-09-14 |
| P0096 | Auffinger Damron Hanson / Grimmett Q12 (FPP) | four-edge-minimum bound for FPP time constant | KNOWN, already refuted in lit (Ahlberg arXiv:1911.09949) | report line 2697 | proofs/P0096_FPP_minimum_bound_counterexample_candidate.md | - |
| P0140 | van der Hofstad OP4.1 | identify limit law in thinned Levy random-drift exploration | KNOWN, already identified (Dhara-vdHofstad-vLeeuwaarden-Sen eq.2.22) | report line 2735 | proofs/P0140_thinned_levy_random_drift_candidate.md | - |
| P0248 | Aldous-Fill OP7.18 | diameter-squared relaxation bound on Cayley graphs | KNOWN, resolved by Pak SODA1999 Thm3.1 | report line 2787 | proofs/P0248_optimized_cayley_known_rederivation.md | - |
| P0249 | reversibilisation trace inequality | trace monotonicity under reversibilisation | KNOWN, implied by Huang-Mao arXiv:2012.13895 Thm4.3 | report line 2827 | proofs/P0249_reversibilization_trace_known_consequence.md | - |
| P0001 | Grimmett Conj4.2 (=Tang-Zhang Conj1.3 Mar2026) | negative correlation of edge indicators in uniform random forest | PARTIAL, cactus graphs only | report line 2237,5957 | proofs/ (P0001 file) | - |
| P0004 | Grimmett Q2.3 | convergence of c_n(v)^(1/n), quenched connective const on supercritical cluster | PARTIAL, root-independence of limsup proved (conclusion already in Lacoin arXiv:1203.6051) | report line 2281,5998 | proofs/P0004_quenched_limsup.md | - |
| P0342 | fringe-subtree CLT transfer | unrestricted fringe-CLT transfer for bounded continuous functional | PARTIAL, scope counterexample (degenerate-Gaussian case only) | report line 2357 | proofs/P0342_beta_tree_fringe_transfer_scope_counterexample.md | - |
| P0355 | discounted-tree nonendogeny conjecture (Conjecture 34) | nonendogeny of discounted random-tree recursion | PARTIAL, literal-scope counterexample | report line 2408 | proofs/P0355_discounted_RTP_degenerate_scope_counterexample.md | - |
| P0389 / P0390 | ARW mesoscopic hyperuniformity questions | hyperuniformity at fixed particle-number window | PARTIAL, window-quantifier correction | report line 2449 | proofs/ARW_fixed_mass_window_obstructions.md | - |
| P0411 | boundary-hole monotonicity, ideal Voronoi cells | hole-probability monotonicity + coefficient positivity | PARTIAL, proved all dims + odd-dim polynomial; negative 6th coeff found d=2 | report line 2493 | proofs/IPVT_boundary_hole_partial.md | - |
| P0429 | Wang et al. fork-join queueing | largest batch size compat. w/ asymptotic independence | PARTIAL, k=o((n/log n)^(1/3)) exponential-service regime | report line 2568 | proofs/Limited_forkjoin_stationary_exponential_partial.md | - |
| P0458 / P0459 | bilateral preference degree sequences | degree law + concentration for bilateral-preference graphs | PARTIAL, non-Gaussian limit k=o(n^(2/5)); concentration k/log n->inf | report line 2623 | proofs/Bilateral_degree_fluctuations_partial.md | - |
| P0288 | Pollett Sec2 assertion (ii) (dup of Pollett row above) | see Pollett row above | REFUTED | report line 1861 | proofs/P0288_pollett_rank_two_transition_counterexample_candidate.md | - |
| D0039 | Virag ICM2014 arXiv:1804.06953 Q1 | beta-Hermite vs GMC measures, same fractal spectrum at equal Hausdorff dim? | BOOKKEEPING, flagged as wrongly excluded, put back on open list | report line 5445 | - | - |
| E0024 | 2019 Hunt-hypothesis survey Q4/4' | does (H) transfer to X=(X1,X2) independent Levy? | PROVED on class strictly larger than survey's | report line 6393 | - | - |
| E0026 | same survey Q6 | does every 1D Levy w/ infinite jump variation satisfy (H)? | PARTIAL, reduction removing large jumps | report line 6424 | - | - |
| E0027 | same survey Q7 | is (H) stable under independent sums X+Y? | PARTIAL, same additivity argument as E0024 | report line 6445 | - | - |
| E0008 | Durrett 2009 coexistence notes Pb2 | general coexistence thm for long-range-interaction models | OPEN, row carried, no result found in report body | report line 6465 | - | - |
| E0058 | 2009 QSO survey Pb1 | another Lyapunov function for skew-symmetric Volterra operators? | PARTIAL, delimits known family exactly | report line 6494 | - | - |
| E0066 | same survey Pb13 | trajectories of bistochastic quadratic operators | PARTIAL, canonical Lyapunov fn identified (Shannon entropy) | report line 6517 | - | - |
| F0019 | Zygouras 2024 polymers review Q2 | is f'(beta)<0 throughout strong-disorder regime? | PARTIAL, exact identification of question, required a correction | report line 6593 | - | - |
| F0029 | Jarai 2014 sandpile survey Conj3.7 | toppling-probability exponent eta(d), Abelian sandpile 2<=d<=4 | OPEN, row carried | report line 6629 | - | - |
| F0036 | 2015 Brownian web/net survey Conj8.3 | local finiteness of first-meeting-point set M for Brownian net | OPEN, row carried | report line 6658 | - | - |
| C0033 | Lyons Determinantal probability Conj2.6/5.3 | concavity of entropy of determinantal measures in kernel | PARTIAL, original equivalence claim corrected | report line 5670 | prob1000_lean_20260908/c0033*.py | - |
| C0034 | Lyons Q2.8 | coupling of P_H1,P_H2 with union-marginal P_H | REDUCED to linear-feasibility (transportation-polytope) question | report line 5702 | prob1000_lean_20260908/c0034.py, c0034b.py | - |
| C0036 | Lyons Conj5.7 | Fuglede-Kadison domination bounds, equivariant determinantal processes | PARTIAL, proved w/ geometric mean replaced by harmonic mean | report line 5732 | - | - |
| C0062 | Romik Longest increasing subsequences sec1.18 | shape/uniqueness/asymptotics of max-dimension Young diagram | PARTIAL, uniqueness clause shown false via an identity | report line 5633 | prob1000_lean_20260908/c0062.py, c0062b.py, c0062c.py, c0062d.py, c0062_radius2_result.txt | - |
| G0001 | Cerf arXiv:2608.23661 Conj1.4 | stretched-exp finite-cluster tail at p_c implies theta(p_c)=0? | PARTIAL, recognised as theta(p_c)=0 "in disguise" | report line 5926 | - | - |
| G0004 | Flammant arXiv:2609.03492 Conj2.2 | universal boundary-connectivity function phi for increasing events | OPEN, row carried | report line 5888 | - | - |
| G0005 | Flammant / Kozma-Nitzan Conj3 restated | many-contacts connectivity conjecture (implies theta(p_c)=0, d>=2) | OPEN, row carried | report line 5854 | - | - |
| G0008 | Campos de Lima arXiv:2601.00291 | is n->P_p(0<->(0,n)) monotone non-increasing on Z^2 (and Z^d)? | OPEN, row carried | report line 5797 | - | - |
| G0013 | Catalano Lavenant (per report heading) | covered in report chapter 10 (10_attempts_H.md), not restated here | see chapter 10 | report line 5772 | prob1000_lean_20260908/g0013_local_search.py, g0013_permutation_search.py | - |
| G0014 | Kumar Duddala arXiv:2608.21125 Conj3.2 | Bramson-correction front CLT for threshold cascades | same conjecture as H0010 row above | report line 5558 | - | - |
| G0015 | Kumar Duddala arXiv:2608.21125 Conj7.2 | CRT scaling limit, critical clusters w/ continuous type space | OPEN, obstacle named (Miermont finite-type machinery doesn't cover Polish-space types) | report line 5599 | - | - |
| D0002 | 2014 complete-mixability survey OP2 | one generic proof unifying all known n-CM sufficient conditions? | OPEN, row carried | report line 6260 | - | - |
| D0005 | same survey OP5 | is uniform law on any convex body C n-completely mixable, n>=d+1? | PARTIAL, (d+1)-CM proved for simplices + one other family | report line 6290 | - | - |
| D0010 | same survey OP10 | extra conditions for n-CM of unimodal laws at mean-condition boundary | PARTIAL, quantitative necessary condition proved in tight case | report line 6318 | - | - |
| D0035 | Bradley Q7 (dup numbering) | same as Bradley/Pollett row above | REFUTED literal general form | report line 6367 | - | - |
| D0016 | Khoshnevisan OP1 (dup, fuller statement) | zero-set of Brownian-sheet slice finite outside null set, d in {2,3}? | SETTLED d=3 (see D0016/D0018 row above) | report line 6226 | - | - |
| F0133 | Guionnet 2004 lecture notes Conj7.1 (Voiculescu unification) | is microstates free entropy chi = non-microstates chi*? | OPEN, row carried | report line 6713 | - | - |
| F0059 (dup) | Janson 2012 Pb18.39 | see F0059 row above | REDUCED | report line 6687 | - | - |

---

## E. Additional context files (not per-problem, but part of the campaign's paper trail)

- `~/Downloads/Probability_Publishability_20260910/` - flagship-paper packaging: cayley_paper.tex/.pdf, Shmalo_Cayley_Product_Condition.tex/.pdf, paper.tex/.pdf (Allen-Cahn), Probability_flagship_papers_and_Lean.zip, plus Lean cores CayleyAlgebra.lean, CayleyCore.lean, EndpointCore.lean
- `~/Downloads/Critical_Allen_Cahn_paper_and_Lean.zip`, `Bernoulli_two_copy_manuscript_v2.tex/.pdf`, `Bernoulli_two_copy_entropy_refinement.tex/.pdf`, `Scalar_ReLU_*.tex/.pdf` - adjacent one-off papers from the same pipeline/date range in the same Downloads folder; not part of the probability-1000 ledgers, not itemised as "open problems" rows above
- `~/probability-hard-problems-20260910/` - HARD_FRONTIER.md, HARD_INTAKE.json, P0174_CURVATURE.md, P0276_subpolynomial_degree_extension.tex, check_free_curvature.py, free_brownian_sharp_mode_curvature_2026_09_10_body.md, probability_cayley_owner_generalization_retired_2026_09_10_body.md - the "hard frontier" follow-on push on P0174 (free-Brownian unimodality curvature) and the retirement of the P0276/Cayley line
- `~/arxiv_mathpr_sources/` - bulk arXiv math.PR harvesting infra behind the campaign: listing.jsonl (19MB), listing_more.jsonl (42MB), download_log.jsonl (3.3MB), harvest.log, harvest_more.py, harvest_more_years.log, plus src/, tex/ subdirs of fetched sources
- `~/math-open-problems-p300/` - a git-tracked mirror/worktree that as of 2026-09-14 13:12-13:35 picked up copies of prob1000_lean_20260908/, probability_1000_attempts_H_20260912/, probability_1000_attempts_I_20260914/, probability_1000_intake_claude_20260907/, probability_1000_intake_D_20260908/ alongside its own older, unrelated project content (doubling/jamming, Cayley/Toeplitz papers unrelated to probability)

---

## Summary (10 lines)

Output file: `~/AppData/Local/Temp/claude/<project>/88e175ec-e7cc-4bc7-a998-68bfafb7613f/scratchpad/LOCAL_INVENTORY.md`

1. The campaign lives in two trees: `Downloads/Probability_1000_20h_20260906/` (Codex 20h run: problems.jsonl 611 rows, attempts.jsonl 466, sources.jsonl 260, proofs/ 25 written arguments) and `06_math_research/probability_1000_intake_{claude,D,E,F,G,H,I}_*` (seven further Claude-agent ledgers: 160/102/115/154/15/34/200 rows).
2. The single consolidated document is `Downloads/Probability_1000_report_2026-09-12/Probability_1000_open_problems_report_2026-09-12.md` (17,394 lines), rebuilt through 2026-09-14 12:47 from `chapters/*.md`; its `12_results_I_13_14_september.md` chapter is the "13-14 September" report the task asked about.
3. Roughly 55-60 problems have a named, dated, individually-filed write-up in `Downloads/Probability_*.md` (2026-09-08 through 2026-09-14), each with a matching Python/Lean check script under `06_math_research/prob1000_lean_20260908/` or `.../probability_1000_attempts_{H,I}_*/`.
4. Seven problems carry Lean 4 formalisations (E0046, E0061, E0063, E0077, F0055, P0208, P0340), all reported "no sorry, standard axioms only."
5. The 8 September "thirteen settled" batch (Aldous-Fill 7.27/4.30, Aldous-Janson OP14/Ansatz20, Hasebe-Ueda-Wang 4.7, Agresti-Veraar 4/5, Bradley Q7, Pollett, Burdzy-Scheutzow 7.5, Salez 2.4, Lyons-Peres 17.18, Hasebe-Ueda 3.3) is the best-documented cluster, in `Probability_open_problems_thirteen_settled_2026-09-08.md`.
6. The 13-14 September burst mostly finished off S. Janson's Probability Surveys 9 (2012) problem list (18.9, 18.30, 18.39, 18.40, 18.41, 18.42, 20.1, 20.2, 20.3, 20.4) plus a cluster of Aldous-Fill open problems (4.45, 4.48, 4.49, 7.31) and two Hasebe-Ueda free-probability problems (3.3 sharp constant, 3.11 partial).
7. Refutations (REFUTED) outnumber proofs in the corpus; several "PROVED" results were later found already published (E0046/Hutnik 2026; F0090/Kalai closed by the author himself on 2026-09-13) and are marked KNOWN rather than credited.
8. A meaningful fraction of rows are explicitly PARTIAL or REDUCED (H0019, H0024, F0059, I0026, I0031, I0082, I0095, C0033/C0034/C0036, D0005/D0010, E0026/E0027/E0058/E0066) - reformulations or special cases, not full answers.
9. No independent, human-refereed certification exists anywhere in the corpus; the report itself states "the number of independently certified full solutions in this chapter is zero" and every memo repeats a standing caveat that only a bounded web/citation search was done for prior art.
10. Roughly 900-1,000 further candidate problems remain uncatalogued above (still open, no attempt beyond intake), living only in the raw catalog_0{1-9}_*.md chapter files and the seven problems.jsonl ledgers.

