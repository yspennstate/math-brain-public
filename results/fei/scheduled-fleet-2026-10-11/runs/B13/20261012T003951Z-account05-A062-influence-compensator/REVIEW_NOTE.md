# Scoped independent reconstruction of A064's minority-drift obstruction

Source: A064-TERMINAL-CORRECTED-GLOBAL-DEBT v1, only its physical-minority no-go clause, proved in POTENTIAL_OBSTRUCTION_TESTS.md. Reviewer: A062. Verdict: HOLDS AT THIS SCOPE. This is not independent acceptance of the entire bundled A064 claim.

For B05 let delta=2^{-k}, p=2^{-2k}, mu=p(1-sqrt(delta)+delta)/2, d=pdelta, and psi(u)=u log_2(1/u). The two child physical minorities equal mu +/- d/2. Since psi''(u)=-1/(u ln2), Taylor's integral formula gives

0<=psi(mu)-[psi(mu-d/2)+psi(mu+d/2)]/2<=d^2/[8 ln2 (mu-d/2)].

Divide by d and substitute mu-d/2=p(1-sqrt(delta))/2 to obtain an upper bound delta/[4 ln2(1-sqrt(delta))]->0. Meanwhile the explicit actual Boolean nonempty-data packets give D/d>=B/d>=(1-delta)(k-2)->infinity. Thus, for fixed finite c,C>=0, D<=Cd+cpsi(mu)-average cpsi(mu_children) fails at the selector root for large k. Each coefficient, branch probability and variable is retained; no entropy of the terminal core is discarded. This reconstructs the critical sign and asymptotic line by calculus rather than treating nonnegative parent/child slack as a drift theorem.

The present stage's pointwise result Q*<=4psi(mu) does not repair that false local potential assertion. It controls the actual Bellman reserve on one complete aligned tree by transporting odd-state reserve to a preceding data-pair query. No counterexample to FEI or to all physical rules follows from A064's local no-go.
