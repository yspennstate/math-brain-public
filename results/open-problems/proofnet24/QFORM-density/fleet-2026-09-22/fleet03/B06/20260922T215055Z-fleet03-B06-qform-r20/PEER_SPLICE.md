# r20 final-source peer splice

After `REPORT.md` was committed, a compatible completed fleet01/B08 result appeared at

`yspennstate/math-open-problems@0363353c145404642d80537955b58c3ce519dc09`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260922T215231Z-fleet01-B08-qform-r18/REPORT.md`.

Its theorem `QFORM-FRACTIONAL-RIDGE-L3-OUTER-SQUARE-v1` proves that if an actual physical cross block `H` has `s_2(H)>=sigma` and the full physical range projection has maximum coordinate leverage at most `1/2` on either side, then the current genuine outer-square branch satisfies

`||p_Q||_infinity <= 7.901945565491720 / sqrt(|a| sigma)`.

In the B08 r20 state `s_2(H)>gamma/sqrt(2)`, so this gives the actual inequality

`||p_Q||_infinity <9.397049888846953/sqrt(|a|gamma)`

whenever either physical range is half-leverage-diffuse, with the entire higher-rank tail retained.

This does not pay the current bicolooop survivor itself: for `Z=H(g^2I+H^TH)^(-1/2)`, `range(Z)=range(H)` and `ZZ^T <= P_range(H)`. Hence the surviving row energy `||z_j||^2>0.99` forces `(P_range(H))_jj>0.99`; the right-side near-coloop analog likewise forces a right range leverage above `0.99`. Thus the remaining state is genuinely **double-heavy physical range**, not an artifact of using the full-range sufficient condition.

The same fleet01/B08 report independently proves a stronger target-valid version of the small-tail characteristic-continuity obstruction in Section 6 of this run's `REPORT.md`: it embeds the perturbation in matrices already carrying three eigenvalues equal to one and makes the fixed-frequency characteristic discrepancy tend to two. Therefore this B06 run does not publish a duplicate correction event; the fleet01/B08 event `QFORM-SMALL-TAIL-CHAR-CONTINUITY-FALSE-v1` is the stronger canonical correction.

The remaining B06 implication after this peer splice is `QFORM-DOUBLE-HEAVY-SCHUR-FLAG-TAIL-v1`: keep the leading factorized incident-minor channel and the nonzero orthogonal tail inside one product-preserving estimate, or exploit the two >0.99 physical range coloops to force a separately paid physical-star/third-curvature branch. The `alpha=Z_jr=0` star-star subcase remains explicitly separate from the nonzero-alpha Schur flag.
