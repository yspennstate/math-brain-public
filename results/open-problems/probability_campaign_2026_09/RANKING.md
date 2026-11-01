# Ranking of the settled open problems by importance (draft of 2026-09-14, first pass)

Scope: every problem that this machine's campaigns and the repository's ProofNet24 tracks claim to have
solved, refuted or reduced, September 2026, plus the June-July results already in the repository. The
ProofNet24 tracks (the hourly ChatGPT workers whose reports also arrive by email) claim no closed problem
as of the 14 September archive; their strongest items are listed at the end for completeness.

Two scores, each 1 to 5. Importance: how much the community would care that this particular question is
settled (prominence of the poser and venue, centrality of the question, whether a published claim is
overturned). Strength: how complete and how well checked the record is (a full argument on the page,
independent re-derivations, exact or machine-checked cores, prior-art search), and whether the result is
still unpublished. "Paper-ready" notes what a stand-alone paper would need.

## Tier 1: results a broad audience would notice

| Rank | Problem | Answer | Importance | Strength | Paper-ready |
|---|---|---|---|---|---|
| 1 | Kalai Conjecture 8 (ICM 2018) = Garban-Pete-Schramm 2010 open problem 1: Ent(f_R) = O(R^2 alpha_4(R)) for the percolation crossing event | PROVED (square crossing, Z^2 and triangular lattice) | 5 | 3 (author-checked, one independent read, no referee; novelty uncertified) | ALREADY PUBLIC: posted by the author on ResearchGate 2026-09-13. Not a candidate for a new paper. |
| 2 | Janson (Probability Surveys 2012) Problem 20.2 (b),(c), with the closing conjecture of Thevenin (EJP 2020) | NO in general: a law with two rare atoms straddling the condensate makes the outdegree count a two-point mixture; normal exactly at the mean of a finite-variance tilted law; 20.3 and 20.4 answered the same way | 4 | 3.5 (Theorem A subcritical: full proof; Theorem B critical infinite-variance: sketch; exact toy checks) | needs Theorem B written in full; a short paper |
| 3 | Hasebe-Ueda (ALEA 2018) Problem 3.3: the optimal C with mu boxplus S(0,t) unimodal for all t >= C D_mu^2 | C = 1, symmetric Bernoulli the unique extremal; the paper's printed lower bound 2 is a slip (their example gives 1) | 3.5 | 5 (two independent proofs, every inequality re-derived twice, symbolic check, 1.2e8-triple scan, an independent density computation, the classical companion D^2/4 the same day) | the two-atom inequalities are real-polynomial and formalisable; numerics natural; ready |
| 4 | Aldous-Janson (arXiv:2303.02529) Ansatz 20 inside Open Problem 8, and Open Problem 14 | Ansatz false in both parts (a(n,n) = 1); drawn length is Theta(n), not n log^4 n | 3.5 | 4.5 (elementary, Lean core for OP14, simulation) | ready; short note; the authors invoke the Ansatz |
| 5 | arXiv:2608.04303 (Stepanyants-Krapivsky-Hartle-Krioukov) Conjecture 1 and the layer half of Conjecture 2 | PROVED: the layer recursion is the Poisson-weighted infinite tree's minimum, so the front is Addario-Berry-Ford's k/e + (3/2e) log k with a genuine limit constant | 3.5 | 4 (full proof from two published theorems; recursion and Monte Carlo agree) | ready; the authors are physicists who called it open |
| 6 | Janson Conjecture 20.1: level widths uniformly integrable | PROVED for every real r >= 1 | 3 | 4 | short |
| 7 | Janson Problem 18.30 (ii),(iii); 18.41, 18.42; 18.40; 18.9; 18.4; 18.10; 18.39 | all answered (two NO, two NO, NO, iff w_1 > 0, PROVED, PROVED, reduced) | 3 (as a group) | 4 (exact witnesses and limit families, Lean core for 18.4) | one paper on condensation in random allocations |

## Tier 2: settled questions from well-known problem lists, narrower audience

| Rank | Problem | Answer | Importance | Strength |
|---|---|---|---|---|
| 8 | Aldous-Fill Open Problems 4.48 (a),(b), 4.45, 4.30, 7.27 | (a) FALSE, (b) TRUE; K = 1 fails; NO; REFUTED | 3 (Aldous-Fill is a standard reference, but these are unpublished-book questions) | 4.5 (exact rationals, Lean core for 7.27) |
| 9 | Agresti-Veraar (2025) Problems 4, 5, critical Allen-Cahn | REFUTED by a Bessel-4 construction | 3 | 4 (manuscript and partial Lean exist) |
| 10 | Salez (arXiv:2508.21055) Problem 2.4, cutoff iff product condition on abelian Cayley graphs | literal form REFUTED | 3 | 4, but superseded by the author's own later manuscript (retired 09-10) |
| 11 | Lyons-Peres Question 17.18 | NO | 2.5 | 4 |
| 12 | Burdzy-Scheutzow Problem 7.5 | YES | 2.5 | 4 (nearest relative: Last-Morters-Thorisson 2011) |
| 13 | Hasebe-Ueda-Wang Problem 4.7 (multiplicative free BM) | NO | 2.5 | 4.5 |
| 14 | Leskela Problems 1 (Ross's second conjecture) and 3 | 1 REFUTED, 3 YES | 2.5 | 4 |
| 15 | Neri-Pinto Remark 3.7 (urn contractivity) | NO | 2 | 4.5 (exact) |
| 16 | Rozikov Problems 3, 4, 10, 11 (quadratic stochastic operators) | YES / PROVED / PROVED / REFUTED | 2 | 4 (two Lean cores) |
| 17 | Khoshnevisan Open Problems 1 and 3 (d = 3, 5) | settled in those dimensions | 2.5 | 3.5 |
| 18 | Kumar-Duddala Conjecture 3.2 (UI clause inverted); Levy-drift compactness Remark 5.3(ii); frog-model Remark 3.6 | corrections to 2026 preprints | 2 | 4 |
| 19 | Pollett Section 2 Conjecture (ii); Bradley Question 7; Konstantopoulos mobile Boolean OP 2, 3 | NO; literal form NO; homogeneous case | 1.5 | 3.5 |

## Not candidates (already known, or partial only)

MMPP c^2 >= 1 (He 2021 Theorem 3.2); Bandeira 1.2 complex half (Hutnik 2026); Sylvester-Hadamard discrepancy (1983); Erdos-Sos Lean file (copy of the 3 September public proof). Partial or reduced: Hasebe-Ueda 3.11, Aldous-Fill 4.49 and 7.31, Vu 8.4/8.5, Lyons 2.6, Grimmett, Romik, sign-matrix discrepancy, and the rest of the PARTIAL rows in INDEX.md.

## ProofNet24 tracks (repository + hourly emails), for completeness

No closed problem. Strongest: P22 benign overfitting Target 2 (candidate complete, one audit short); P13/P12 fourth-moment least-singular-value law (candidate complete); P17-M1/M2 magnetic K-theory invariance; P15's disproof (a residual KRR stage can hurt); P25's disproof of Theorem 12.122 in the author's own K-theory manuscript. None is ready for a paper without the protocol's two independent audits.

## June-July results already in the repository

Exact Toeplitz/Hankel LSD moments (paper1), least singular value of the coordinate-optimised submatrix (sharp exponent 2H(a)/d_F), GinOE extreme gaps, Balan-Wang open problem 21, matrix Spencer lifts (paper12), law-of-robustness/adversarial submatrix (paper23). These were rated and published in their own sessions and are not re-ranked here.

## Where the first pass lands

Most important: Kalai Conjecture 8, already public. Among results still unpublished, the two that combine
importance and strength are Janson Problem 20.2 (importance) and Hasebe-Ueda Problem 3.3 (strength, and
the only one whose core is a set of real-polynomial inequalities that a proof assistant can certify in
full). The reviewers' task is to check these scores and say which unpublished result should be written up.


## Referee reviews and the vote (14 September 2026, later the same day)

Three independent Fable 5.1 referee sessions read the first pass and the memos and re-derived the top eight results;
their reports are archived beside this file as `REVIEW_A.md`, `REVIEW_B.md`, `REVIEW_C.md`. Where they moved the
scores:

- Kalai Conjecture 8: strength up to 4 (the coding argument re-derives CLEAN end to end); it stays excluded from the
  paper question because the author posted it on 13 September.
- Janson Problem 20.2: importance 3.5 rather than 4, and the status must read "(c) refuted; (b) sketch". Theorem A
  (subcritical) is complete; Theorem B (critical, infinite variance) is a sketch, and its stated growth condition
  n_r = n_{r-1}^r is insufficient (the bulk route beats the rare route unless log n_r >> (log n_{r-1})^2).
- Janson Problem 18.40: the memo's theorem is FALSE as stated. For w_k = k! on the full support the largest box has
  P(Y_(1) = m) -> e^{-1/lambda}, not 1 (exact rational computation, reproduced by the lead: 0.357 at m = n = 40, 0.607 at
  lambda = 2); the gap is the memo's inequality (3), which neglects the Theta(m) entropy of mixing small boxes with a
  giant. Problem 18.39's reduction inherits it. Both rows are back to unverified in INDEX.md.
- Aldous-Janson Ansatz 20: a correct but cheap refutation (a(n,n) = 1, an endpoint test function); the pair is carried
  by Open Problem 14. One reviewer asks that the sum's range (to i = n inclusive) be checked against the PDF before
  anything is published.
- Under-rated in the first pass: Agresti-Veraar Problems 4 and 5 (importance 3.5, strength 4.5), Lyons-Peres 17.18 and
  Leskela's pair (importance 3). Over-rated: Salez 2.4 (literal form, unbounded degree), Bradley Q7, Burdzy-Scheutzow.
- The classical companion of the unimodality result (D^2/4) is almost certainly known in the mixture literature and
  must be presented as such; the free constant C = 1 found nothing in the citation graph or on arXiv.

Every reviewer named the same paper candidate. The five-member vote (four Fable 5.1 voters with different briefs plus
the lead) was unanimous:

    WINNER    Hasebe-Ueda (ALEA 2018) Problem 3.3: the optimal constant is C = 1 (with the classical companion D^2/4)
    RUNNER-UP Agresti-Veraar (2025) Problems 4 and 5 (four voters); Janson Problem 20.2 (the lead)

Reasons given: two independent proofs, every inequality re-derived by all three referees, a sharp answer with the
extremal measure and a rigidity statement, a real-polynomial core that a proof assistant certifies in full, and the
lowest prior-art risk. The one risk every voter named, the exact wording of the source's Lemma 3.1, was settled by
reading the source text: the lemma is a sufficient condition (at most two solutions for every R implies unimodality),
which is the only direction the proof uses; D_mu is the diameter of the support, and the printed "2 <= C <= 4"
paragraph divides the Bernoulli threshold 4 by D_mu = 2 rather than by D_mu^2 = 4.
