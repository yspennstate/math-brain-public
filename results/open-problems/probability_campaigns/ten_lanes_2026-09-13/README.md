# Five probability areas, 13 September 2026

Working notes from one day of attacks on open problems taken from the probability corpus, split
into five areas: percolation and discrete probability on graphs (P1), random matrices (P2),
continuous-time processes (P3), interacting particle systems and quadratic stochastic operators
(P4), and Markov chains (P5). Each note states the problem as printed in its source, what was
proved, what was only checked numerically, the strongest case against the result, and what is
left. The scripts and logs behind the exact and numerical checks sit in each area's `code/`
folder.

These are working reports, not papers. Nothing here has been refereed.

## What each note establishes

| id | problem | outcome |
|---|---|---|
| C0091 | negative correlation in the random-cluster model, q < 1 (Heydenreich-van der Hofstad, Open Problem 16.9) | an exact decomposition of the covariance and four elementary corollaries, proved and machine-checked; the conjecture itself open, no counterexample on graphs with at most 6 vertices |
| C0146 | monotone coupling of random-cluster measures in p for q < 1 (Pete, Question 13.2) | vector-parameter monotonicity refuted with exact rational witnesses on the triangle and C_4; equivalence with strict negative correlation proved; scalar monotonicity numerical only |
| P0001 | negative correlation of two edges in a uniform forest (Grimmett, Conjecture 4.2) | an exact covariance identity and corollaries proved; the conjecture not advanced |
| P0037 | BK-type inequality for the weighted uniform spanning tree (Lyons-Peres) | the principal-A case proved; first computer search of small graphs, no counterexample |
| F0008, F0009 | Vu's simplicity conjecture and the distinct-singular-values conjecture for random symmetric sign matrices | lower bounds of order n^4 4^(-n), from two disjoint support-two eigenvectors, proved (the n^4 prefactor in Conjecture 8.4 as a lower bound); two claims in the corpus record that these events are super-exponentially small refuted |
| P0016 | the worst-conditioned square subframe of a Gaussian frame at minimal redundancy | the 4^(-M) rate and a matching tail bound proved; the rate itself is in arXiv:2607.06249, which settles the problem; the exponential limit law is a conjecture with numerical support |
| E0025 | Kanda-Forst condition for pure-jump subordinators (Hu-Sun, Question 5) | an explicit subordinator with unbounded Kanda-Forst ratio, ratio 4m + O(1) along an explicit sequence; Question 5 itself untouched |
| F0065 | Janson's height conjecture for random trees | not open: proved by Addario-Berry and Donderwinkel (arXiv:2201.11773, 2022) |
| P0025 | synchronously coupled reflected Brownian motions outside a disk | an exact identity, a tangent-line criterion and a local martingale proved; the question open |
| P0177 | the mode of classical and free Brownian motion at large time | two-term asymptotic expansions of both modes proved, with the factor 6 between the free and classical displacements |
| E0065 | regularity thresholds alpha_m for quadratic stochastic operators | alpha_2 = (3 - sqrt 7)/4, a factor two below the published value; 1/12 <= alpha_3 <= 1/6 with an explicit extremal family |
| E0068 | quadratic stochastic operators with V^r = V | complete classification for m = 2 and unboundedness of the minimal exponent |
| P0245 | the extremal cover-time conjecture (Aldous-Fill, Open Problem 6.30) | proved for n = 3, with equality only for simple random walk on the triangle |
| P0253 | is the antivoter variance maximised by the complete graph? (Aldous-Fill, Chapter 14) | the complete graph is the maximum in an exhaustive check through n = 9; a natural relaxation shown too weak; a parity reformulation |

`P1_percolation/_ranked_candidates.md` is the ranked list the percolation problems were drawn
from, and `P2_rmt/LITERATURE_P2.md` the literature search for the random-matrix problems.

## Later work on the same problems

- P0001, C0146, P0025, P0037 and P0177 were taken up again in October; see
  `../codex_pool_2026-10-10/`.
- F0065 is closed in the literature (Addario-Berry and Donderwinkel, 2022).
- P0016 is closed by arXiv:2607.06249.
