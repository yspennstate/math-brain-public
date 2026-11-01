# PROB10-09 idea before code — sharpen the uniqueness side with the all-genus surface spectral bound

Frozen parent: Benjamini–Schramm bond-percolation conjecture for every locally finite Cayley graph of a finitely generated nonamenable group. This iteration remains on R20's delimited standard surface-product quantitative/nonbacktracking lane and does not take NM13-11's free-core/complement or higher-rank-lattice claim.

Immediate predecessor metric on the frozen graph X_{3,4}: p_u-p_c > 2649449/100000000 = 0.02649449, with p_c(X_{3,4}) < 4540551/100000000 from the exact full-tree fibre fixed-point certificate and p_u(X_{3,4}) > 719/10000 from the previous spectral/nonbacktracking certificate.

Three genuinely different routes to test before code:

1. **All-genus surface spectral estimate (main attack).** The Bartholdi–Cantat–Ceccherini-Silberstein–de la Harpe surface-group estimate gives for the standard genus-g Markov operator M_g the rigorous upper bound
   ||M_g|| <= sqrt(4g-2)/(2g) + 1/(4g).
   Therefore the adjacency operator obeys ||A_g|| <= 2 sqrt(4g-2)+1. The predecessor used the much weaker Freiheitssatz bound 2+2 sqrt(13) for genus 4. Replace only that factor, retain the sharper Nagnibeda genus-3 bound, and push the D=28 nonbacktracking root comparison with exact rationals. Expected outcome: move the frozen p_u floor and hence the certified p_u-p_c gap.

2. **Use the same all-genus estimate on both factors (negation/stress test).** For genus 3 the BCCH bound is about 0.6104 for the Markov operator, substantially weaker than Nagnibeda's printed rigorous upper bound 0.552792. So replacing the genus-3 input as well should worsen the certificate. This route is kept only as a falsification/comparison and should not be coded unless the arithmetic contradicts the expectation.

3. **Further optimize the p_c full-tree fibre threshold (independent route).** The predecessor's p_c certificate 0.04540551 is already within about 3e-9 of the numerical root of the exact fibre activation equation for T_10 square T_14. Thus another p_c rational supersolution is unlikely to give a meaningful move. Treat this only as a numerical diagnostic, not as an exact theorem. The new theorem-sized work should instead be on the p_u side.

If Route 1 succeeds, also record the rigorous family-level mechanism: for every standard surface-product Cayley graph X_{g,h}, g,h>=2, degree D=4g+4h, the product adjacency norm is at most
R_{g,h}=2 sqrt(4g-2)+2 sqrt(4h-2)+2,
so the nonbacktracking transfer yields the explicit structural lower bound p_u(X_{g,h}) >= 1/beta_D(R_{g,h}) (with the usual sqrt(D-1) branch when R_{g,h}<=2sqrt(D-1)). This is a quantitative criterion, not a novelty claim for qualitative product nonuniqueness, which is already known in the literature.
