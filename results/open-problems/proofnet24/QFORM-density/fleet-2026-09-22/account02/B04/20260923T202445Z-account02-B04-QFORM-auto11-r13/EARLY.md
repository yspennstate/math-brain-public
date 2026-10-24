SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T20:24:45Z.
attacking: aggregate third-volume deletion to an actual original-coordinate singleton hub with surviving projected pair volume, then compare optimized volume and ridge certificates on the same physical family.

# Early substantive calculation

Let M have physical row vectors r_i and put

Z=e_3(M^T M)=sum_{|S|=3} det Gram(r_s:s in S)>0.

For one physical row i, let P_i be orthogonal projection in deterministic coefficient space onto r_i^perp and let N_i=M_{-i}P_i.  If

Z_i=sum_{S: |S|=3, i in S} det Gram(r_s:s in S),

then Gram-Schmidt gives the exact identity

Z_i = ||r_i||^2 e_2(N_i^T N_i).

Indeed each triple {i,j,k} has Gram determinant ||r_i||^2 times the 2x2 Gram determinant of P_i r_j,P_i r_k, and summing over {j,k} is Cauchy-Binet for e_2.

Under the canonical third-volume law nu(S)=det Gram(S)/Z, the row marginal is alpha_i=Z_i/Z.  If a physical set H has deletion mass

Z_out(H)=sum_{S: S cap H=emptyset}det Gram(S) <= delta Z,

then

sum_{i in H} alpha_i = E_nu |S cap H| >= P_nu(S cap H nonempty) >= 1-delta.

Hence some literal original-coordinate row i in H obeys

||r_i||^2 e_2(N_i^T N_i) >= ((1-delta)/|H|) Z.

This converts an aggregate third-volume deletion certificate into a singleton hub-times-projected-pair-volume currency without rotating random inputs or dividing by a local coefficient.

If the projected pair-volume law of N_i has row marginals <=1/2, the checked arbitrary-rank grouped projected-crossing theorem (one physical hub, ell=2) immediately yields

||p_Q||_infinity <= 3*2^(7/6)*exp(1/3) [((1-delta)/|H|) Z]^(-1/6).

The remaining subcase is therefore precise: the selected high-currency singleton leaves a projected E2 law with a heavy physical row.  The fresh account03/B04 r40 row-marginal-free critical E2 theorem is compatible with that residual packet and motivates promoting the secondary heavy row rather than paying a tiny local minor.

Pinned Claude/e5 sources consumed at e5f71d79eff325201dd0274053d20268ce65b837: RESULTS.md, FOURIER_ROUTE_REPORT.md, COUNTEREXAMPLE_SEARCH.md.  Full QFORM remains open.
