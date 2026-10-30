# T109 A single phase transition for the hard-core model on Z^2

Lead: agent U. Dossier written 2026-10-14 23:5x by the lead
from worker AB's LITERATURE_REVIEW.md and the reviews of C1-C4 in worker AB/FEEDBACK.md.

## STATEMENT
Hard-core lattice gas on Z^2 (independent sets weighted lambda^|I|). Conjecture: a single critical activity
lambda_c (numerically 3.7962) with a unique Gibbs measure below it and two checkerboard (even/odd) measures above it.
The model is not known to be monotone in lambda, so a single transition point is part of the claim.

## FRONTIER
- Uniqueness side: Sinclair-Srivastava-Stefankovic-Yin, arXiv:1410.2595 (2017): strong spatial mixing for
  lambda < 2.538, via the connective constant of a pruned self-avoiding-walk tree (bound 2.429 at memory 30).
- Coexistence side: Blanca, Chen, Galvin, Randall, Tetali, "Phase coexistence for the hard-core model on Z^2"
  (CPC 2019): Theorem 2.3, "multiple Gibbs measures for all lambda > mu_taxi^4 - 1", with mu_taxi the growth rate of
  taxi walks; their finite-n count gives 5.3506.

## ARCHITECTURE (coexistence side)
Peierls argument with even boundary condition -> a defect produces a fault contour Gamma -> a shift map frees
|Gamma|/4 sites, so P(contour) <= (1+lambda)^(-|Gamma|/4) -> count contours of length n by taxi walks (Lemma 3.9 maps
a contour to a taxi walk; Lemma 3.4 counts positions) -> sum converges when (1+lambda) > mu^4 for the growth rate mu of
the counted class.

## FAILURE POINT
Two independent losses. (a) Counting: contours are counted by ALL taxi walks, so even the exact mu_taxi (about 1.574,
extrapolated from c_n to n = 60) caps the method at lambda about 5.13-5.14. (b) Weight: the shift frees only |Gamma|/4
sites; choosing the shift direction gains nothing (C2 review). Below about 5.1, the method needs a smaller counted
class than taxi walks or a heavier weight per contour. Neither side approaches 3.796; the uniqueness side is a separate
SAW-tree / connective-constant method with its own floor.

## SHAPE
Partly finite. Any counted class given by a finite automaton yields a certified bound by a Perron vector certificate
(exact rows, checked in integers). The gain past the taxi floor is real only if the forbidden words are proved never to
occur in a genuine contour (a local lemma per pattern), so each step is lemma + certificate.

## OBSTRUCTION
The counted class. Taxi walks are the method's own floor (about 5.14). Moving it means proving that contours avoid
patterns that taxi walks contain, so the contour class has strictly smaller growth rate (Kesten pattern theorem).
C3/C4 did exactly this: the cut-plus-extra forbidden words (C3, 45 prefix-minimal words through 16 edges, proved) give
a word language containing every contour with growth r <= 1.57997296, hence coexistence for lambda > 5.231586354
(C4 v1 PASS). That is below the taxi floor, so it is a move on the obstruction, not a sharper constant on the old
count.

## SETTLED
- mu_taxi <= 1.58706416 (C1 v2 PASS): coexistence for lambda > 5.3443; v3 (every polygon through length 44) PASS.
- C2 v1 PASS: for a finite W whose boundary edges all have an even interior endpoint, |F_s| = |Gamma|/4; the shift
  direction gains nothing.
- C3 v1 PASS: the 45 cut-plus-extra words never occur in a contour.
- C4 v1 PASS: coexistence for every lambda > 5.231586354 (r = 157997296/1e8, C = 2^50); exact v2 queued for audit.
- Realizable fraction of taxi polygons as contours: 0.67, 0.71, 0.66 at lengths 16, 20, 24 (no decay seen yet).
- Novelty: Chen-Shao-Shi cite 5.3506 as the frontier; the 15 journal citations of Blanca et al. still to be walked.

## TARGETS
1. More forbidden patterns: from the non-contour taxi polygons (length 16-28), extract SHORT cyclic subwords no contour
   can contain, prove each local lemma, add to the automaton, recertify. Say explicitly when a failure needs two far
   pieces of the walk (pattern route does not apply there).
2. A heavier contour weight: a map other than a single shift that frees more than |Gamma|/4 sites, or that has more
   entropy. This attacks loss (b), which no counting improvement touches.
3. Prune the 3,150,582 unreachable automaton states before the next certificate (one run; may lower r slightly).
NOT moves: a longer exact taxi count; a better certificate on the same forbidden set; tighter constant C.
