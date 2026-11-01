# Probability open-problems campaign, September 2026: what was solved, refuted, reduced, or worked on

Archived 2026-09-14 from the machine the work ran on. This folder holds the material that was not yet in the
repository; the ledgers, Lean cores and the memos of 8 to 14 September that a peer session pushed earlier the
same day live beside it in `prob1000_lean_20260908/`, `probability_1000_intake_*/` and
`probability_1000_attempts_*/`. Nothing here is refereed. Every status word below is the record's own.

## Layout

| Folder | Content |
|---|---|
| `codex_20h_20260906/` | the Codex 20-hour campaign: `problems.jsonl` (611 rows), `attempts.jsonl` (466), `sources.jsonl` (260), `proofs/` (25 written arguments), the working and typeset reports, source checks. Fetched third-party papers and page images are not archived. |
| `report_2026-09-12/` | the consolidated report (markdown 2.3 MB, PDF 3.3 MB, rebuilt 2026-09-14 12:47) and its chapters; `chapters/12_results_I_13_14_september.md` is the 13-14 September results chapter. |
| `downloads_memos/` | every dated memo written for a settled problem (8 to 14 September), the 7 September lists, the 9 September handoff, and adjacent one-off manuscripts from the same pipeline. |
| `publishability_20260910/` | the 10 September paper packaging: the Cayley product-condition manuscript, the critical Allen-Cahn manuscript, their Lean components, the author declarations. |
| `hard_frontier_20260910/` | the retired Cayley line and the free-Brownian curvature line. |
| `benjamini_schramm_attempt_2026_06/` | the June attempt at p_c < p_{2->2} on nonamenable quasi-transitive graphs (unsolved; drafts and reductions). |
| `solved_register_2026_06/` | the June register of the earlier solved problems (Gaussian phase retrieval, Balan-Wang stability, submatrix singular values). |
| `RANKING.md` | the 14 September ranking of every settled problem by importance, with the reviewers' opinions and the vote. |

## The settled problems, one line each

Status: PROVED = full argument on the page; REFUTED = explicit counterexample; REDUCED / PARTIAL = a narrower or
equivalent statement; KNOWN = correct but already in the literature. "Lean" names a kernel-checked arithmetic core
(no sorry, axioms propext / Classical.choice / Quot.sound), never a full formalisation of the source theorem.

| Problem | Source | Answer | Record |
|---|---|---|---|
| Kalai Conjecture 8 = Garban-Pete-Schramm 2010 open problem 1, Ent(f_R) = O(R^2 alpha_4(R)) | Kalai ICM 2018 3.3.2; GPS arXiv:0803.3750 | PROVED for the square crossing on Z^2 and the triangular lattice (quadtree coding + GPS Lemma 3.2) | posted by the author on ResearchGate 2026-09-13 (publ. 414266816); `prob1000_lean_20260908/f0090_paper/` |
| Hasebe-Ueda Problem 3.3, optimal C with mu boxplus S(0,t) unimodal for t >= C D^2 | ALEA 15 (2018) | C = 1, symmetric Bernoulli extremal; two independent proofs (Cauchy-profile lemma 09-08, Choquet two-atom reduction 09-14); the printed "2 <= C" is a slip | `downloads_memos/Probability_I0086_*`, `Probability_open_problems_thirteen_settled_2026-09-08.md` sec. 11 |
| classical companion: unimodality of B_t started from a compactly supported law | same paper | sharp constant D^2/4 (the paper proves 9 D^2) | `downloads_memos/Probability_classical_brownian_unimodality_sharp_constant_2026-09-14.md` |
| Aldous-Janson Ansatz 20 (inside Open Problem 8) | arXiv:2303.02529 | FALSE in both parts (a(n,n) = 1) | `codex_20h_20260906/proofs/P0341_*`; thirteen_settled sec. 12 |
| Aldous-Janson Open Problem 14, drawn length ~ n log^4 n | arXiv:2303.02529 | FALSE: Theta(n) | Lean `P0340.lean`; thirteen_settled sec. 2 |
| Janson Problem 20.2 (b),(c) and Thevenin's closing conjecture (EJP 2020) | Probability Surveys 9 (2012) | NO in general: two rare atoms straddling the condensate give a two-point mixture | `downloads_memos/Probability_F0064_*` |
| Janson Problems 20.3, 20.4 | same | answered in two regimes each | `Probability_F0064b_*` |
| Janson Conjecture 20.1, level widths uniformly integrable | same | PROVED for every real r >= 1 | `Probability_F0063_*` |
| Janson Problem 18.30 (ii),(iii) | same | BOTH FAIL | `Probability_F0058_*` |
| Janson Problems 18.41, 18.42 | same | BOTH NO | `Probability_F0061_F0062_*` |
| Janson Problem 18.40 | same | OPEN again: the memo's theorem (P(Y_(1) = m) -> 1 along a subsequence for every rho = 0 sequence) is FALSE for w_k = k! on the full support, where P(Y_(1) = m) -> e^{-1/lambda} (exact rationals, 14 September review); the gap is its inequality (3) | `Probability_F0060_*`, flawed |
| Janson Problem 18.9 | same | Theorem 18.7 holds iff w_1 > 0 | `Probability_F0056_*` |
| Janson Conjecture 18.4 | same | PROVED | Lean `F0055.lean`; `Probability_F0055_*` |
| Janson Problem 18.10 | same | PROVED for every fixed j (pending a source correction) | `Probability_F0057_*` |
| Janson Problem 18.39 | same | reduction on file inherits the flawed rate comparison of the 18.40 memo; back to unverified | `Probability_F0059_*` |
| Aldous-Fill Open Problem 4.48 | Reversible Markov Chains, ch. 4 | (a) FALSE; (b) TRUE | `Probability_P0243_*` |
| Aldous-Fill Open Problem 4.45 | same | K = 1 fails (exact rational witness) | `Probability_P0242_*` |
| Aldous-Fill Open Problem 4.30 | same | NO | thirteen_settled sec. 5 |
| Aldous-Fill Open Problem 7.27 | same, ch. 7 | REFUTED (all three clauses) | Lean `P0208.lean`; thirteen_settled sec. 1 |
| Aldous-Fill Open Problem 4.49 (ii) | same | EVIDENCE: sharp constant 2 on all 992 connected graphs on 4-7 vertices | `Probability_I0026_*` |
| Aldous-Fill Open Problem 7.31 | same | REDUCED to an intersection-array identity | `Probability_I0031_*` |
| arXiv:2608.04303 Conjecture 1 (+ layer half of Conjecture 2), layers of random recursive trees | Stepanyants-Krapivsky-Hartle-Krioukov 2026 | PROVED: the recursion is the Poisson-weighted infinite tree's minimum; front from Addario-Berry-Ford and Aidekon with a genuine limit constant | `Probability_H0019_*` |
| arXiv:2607.07410 Remark 5.3(ii), compactness under a Levy drift | 2026 | NO for every confinement power | `Probability_H0013_H0014_*` |
| arXiv:2608.21125 Conjecture 3.2 | Kumar-Duddala 2026 | the UI clause is inverted | `Probability_H0010_*` |
| arXiv:2607.27082 Remark 3.6, frog model factor four | 2026 | artefact; growth is multiplicative | `Probability_H0024_*` |
| Neri-Pinto Remark 3.7, urn contractivity | arXiv:2607.07309 | NO (p = d always; p = d-1 five-colour witness) | `Probability_H0020_*` |
| MMPP conjectures 4.1 (c^2 >= 1) and 4.2 | Asanjarani-Nazarathy | 4.1 PROVED (KNOWN: He 2021 Thm 3.2); 4.2 REFUTED | Lean `E0077.lean`; `Probability_E0077_*`, `Probability_E0078_*` |
| Rozikov Problems 3, 4, 10, 11 (quadratic stochastic operators) | Rozikov's problem lists | 3 YES; 4 PROVED (sufficiency); 10 PROVED; 11 REFUTED for m >= 5 | Lean `E0061.lean`, `E0063.lean`; `Probability_E006x_*` |
| Burdzy-Scheutzow Problem 7.5 | arXiv:1302.6958 | YES (filling scheme) | thirteen_settled sec. 8 |
| Lyons-Peres Question 17.18 | Probability on Trees and Networks | NO | thirteen_settled sec. 10 |
| Salez Problem 2.4 (cutoff iff product condition on abelian Cayley graphs) | arXiv:2508.21055 | literal form REFUTED; retired 09-10 because the author's own later manuscript covers it | `publishability_20260910/Shmalo_Cayley_Product_Condition.pdf` |
| Agresti-Veraar Problems 4, 5 (critical Allen-Cahn) | 2025 | REFUTED by a Bessel-4 construction | `publishability_20260910/paper.pdf`, `EndpointCore.lean` |
| Hasebe-Ueda-Wang Problem 4.7 | arXiv:2009.13848 | NO (two atoms) | thirteen_settled sec. 3 |
| Hasebe-Ueda Problem 3.11 | ALEA 15 (2018) | PARTIAL: Cauchy laws and free stable laws of index down to about 0.7 excluded | `Probability_I0082_*` |
| Pollett Section 2 Conjecture (ii) | Pollett | NO (rank two) | thirteen_settled sec. 7 |
| Khoshnevisan Open Problems 1, 3 | arXiv:math/0510518 | settled for d = 3 and d = 5 | night report 09-08 |
| Leskela Problem 1 (Ross's second conjecture) and Problem 3 | Queueing Systems 100 (2022) | 1 REFUTED (one-directional cyclic environment); 3 YES (three-state star chain) | `Probability_five_problems_attacked_2026-09-08.md`, `Probability_P0291_*` |
| Bradley Question 7 | arXiv:math/0511078 | literal form REFUTED | thirteen_settled sec. 6 |
| Konstantopoulos mobile Boolean model, open problems 2, 3 | arXiv:1407.6834 | settled in the homogeneous case | `Probability_E0105_*` |
| Randomstrasse 2024 Conjecture 13, Sylvester-Hadamard discrepancy | Randomstrasse list | FALSE for k >= 9; a 1983 Reed-Muller covering-radius result | `Probability_I0092_*` |
| Randomstrasse 2024 open problem 11, sign-matrix discrepancy | same | exact values to n = 11; lower bound 5/3 | `Probability_I0095_*` |
| Bandeira Open Problem 1.2, complex half | Bandeira 2015 | proved, then found KNOWN (Hutnik 2026) | Lean `E0046.lean` |
| Vu Conjectures 8.4 / 8.5, Lyons Conjecture 2.6, Grimmett Conj 4.2 and Q 2.3, Romik 1.18, Lyons determinantal 2.6/2.8/5.7, ARW hyperuniformity, IPVT hole monotonicity, fork-join, bilateral degrees, complete mixability OP5/OP10, Hunt hypothesis Q4/Q6/Q7 | various | PARTIAL or REDUCED | report chapters 3-4 and `codex_20h_20260906/proofs/` |

The Erdos-problem Lean work of 7 September (Erdos 242 Mordell, Erdos 97 Danzer, and the Erdos-Sos file that turned out to be a copy of the 3 September public proof) is in the brain tree, not here.

