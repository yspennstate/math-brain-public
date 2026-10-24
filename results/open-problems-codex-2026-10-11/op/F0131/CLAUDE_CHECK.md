# F0131: third check (claude-322bc92e, 11 Oct 2026 23:1x)

Verdict: PASS on correctness. Novelty is NOT verified; a proper literature search is required before calling it new.

Claim: for every H >= -1, the scaling limit of the sandpile aggregate S_{n,H} (n chips at the origin on constant background -H) cannot be a regular (4H+12)-gon. This answers Levine and Peres's Question 6.2 in the negative for H >= -1. The H = -2 square remains consistent.

Checked line by line:
- Lemma 3 (fully fired regions have height density at least 2) uses the last-firing order. An edge contributes the weight of its earlier endpoint, and the epsilon^2 passage to weak limits has an O(epsilon) edge error. Inside an assumed polygon limit this gives H+2 <= Delta U <= H+3, and Delta U = 0 outside it.
- Lemma 5 (corner inequality a <= b(1 - sin alpha) for a sector of opening alpha in (pi/2, pi)):
  - the projection of the Laplacian onto cos(2 theta) is F'' + F'/r - 4F/r^2 = G;
  - the central integral of cos(2 theta) over (-pi/4, pi/4) is 1, and the two side pieces of the sector total 1 - sin(alpha), so G >= a - b(1 - sin alpha) = kappa;
  - with f = F/r^2, (r^5 f')' = r^3 G (I verified the algebra);
  - C = 0 by boundedness, and kappa > 0 would force f >= (kappa/4) log(1/r), contradicting u = O(r^2), which comes from the subharmonic mean-value bound.
- Consequence. A regular 4k-gon (k = H+3) has corner angle pi - pi/(2k). The inequality (C) becomes k sin(pi/(2k)) <= 1. Since sin x > 2x/pi on (0, pi/2), this fails for every k >= 2 (k = 2: sqrt 2; k -> infinity: pi/2). At H = 0 it reads 2 <= 3/2.

Inputs taken on citation, not re-read by me: Pegden-Smart Theorem 4.2 (odometer convergence at H = 0, standard) and Bou-Rabee Theorem 9.2 (constant backgrounds up to 2) for H != 0. The H = 0 case already refutes the question's general proposal and rests only on Pegden-Smart.

The result is consistent with the source's own simulations ("a regular (4H+12)-gon with some rounding at the corners"): the argument says the corners cannot sharpen in the limit.

This is the most substantive claim of the run so far. Before any public statement: a full search (arXiv last 90 days, Levine, Pegden, Smart, Bou-Rabee, Fey-Levine-Peres follow-ups) and an outside reading.
