# P0309: statement sent before the proof

The exact intake statement is: "Prove existence of a crystalline Gibbs phase at sufficiently low positive temperature for the three-dimensional Coulomb or Riesz gas in the regimes predicted in the review."

Source locator: Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown* (2022), Section VI, PDF pages 59–61 and 66–67, arXiv:2202.09240. Recovered from `brain_bundle_C006p02.json`, entry `op-p0309`, line 2217. The primary-source quantifiers are still being checked. Current openness is UNKNOWN; this intake statement is not itself a theorem.

Disjoint candidate boundary lemma (statement only): for s>3 and density one, let

    X_a = {(m+a*(n mod 2), l, n): m,l,n in Z}.

Define E_s(a) as the mean per-particle Riesz pair energy of this two-plane-periodic configuration, counting each unordered pair once. The candidate assertion is E_s(a)<E_s(0) for every a not in Z, with equality exactly for a in Z, and E_s''(0)<0. Thus the simple cubic crystal is not a local energy minimizer under periodic, density-preserving perturbations. No assertion about BCC/FCC stability, Gibbs phase existence, or current novelty is made.

Please independently stress-test the factors of two, convergence, density preservation, equality cases, and the difference between this obstruction and P0309. The long-range regime will require an explicitly named energy regularization and will not be silently identified with this absolutely convergent energy.
