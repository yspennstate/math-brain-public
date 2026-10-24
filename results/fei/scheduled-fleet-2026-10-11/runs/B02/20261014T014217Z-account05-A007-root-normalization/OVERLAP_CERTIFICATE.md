# Exact strict improvement on an overlapping prime table

Take B=(x0 AND x1) OR (x0 AND x2), g=2B-1, fresh one-bit positive core, p=1/2. The two clauses are all prime implicants. Fix lambda0=lambda1=1/2, beta=1, pi0=pi1=1/4, base orders (0,1) and (0,2), and activated core-first orders. Thus D=17/64 and D'=33/256. For selected data T={0,1} and core U={core}, the physical activated Fourier coefficient is 1/8, verified by integer FWHT; the event has squared spectral mass 1/64.

The old root-only lift has exactly two actual events and surrogate mass

    S_old=1/16+(1/32)(1/3)^(6/5).

The distributed lift has those same events and one additional event:

    S_dist=S_old+(1/32)(2/9)^(6/5).

The additional event assigns common data coordinate 0 to gate 1 and data coordinate 1 plus the core to gate 0. Gate 1 is the sole initial root, then draws gate 0 as a child attached at its selected data coordinate 0. The root does NOT own a core coordinate. Removing core edges (there are none in this c=1 example) recovers the old data tree, and deleting the core from gate 0's subset recovers its old selected subset. The augmented ownership graph is strongly connected; the designated root is valid.

For that event, selected sizes are one at gate 1 and two at gate 0. Their intersection sizes are respectively two and three. Thus the congestion base is (1/2)(2/3)^2=2/9. All selected-coordinate rank discrepancies are zero, because every physical predecessor in these fixed supports is selected. Its label/root prefactor is p lambda0 lambda1 pi1=1/32. This proves its positive surrogate mass exactly, with no logarithm approximation. All prescribed queue choices have positive probability, but this prefactor times congestion is NOT asserted to be the actual queue probability.

The complete conditioned selected residual strictly decreases by

    log2(S_dist/S_old)>0,

with the SAME log D'=Lambda'+log Z' retained on both sides. The strict improvement follows from an exact positive algebraic summand; this is not an asymptotic FEI or universal influence-payment certificate. out/EXACT_CHECK.json records the exact formal mass terms and chronological-event counts.
