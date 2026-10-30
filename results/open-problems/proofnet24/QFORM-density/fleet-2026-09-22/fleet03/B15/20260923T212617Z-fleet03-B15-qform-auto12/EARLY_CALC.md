SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T21:26:17Z.
attacking: endpoint L-infinity*L1 regularization and a product-preserving double-pivot branch that keeps the external coordinate jointly with the near-null curved coordinate.

# Early calculation

If `a` is a probability density in `L^1 cap L^infinity` and `b` is any probability density in `L^1`, then

`h=a*b`

has `||h||_infinity<=||a||_infinity` and a uniformly continuous representative. Indeed

`h(x+t)-h(x)=integral a(x-z)[b(z+t)-b(z)] dz`,

so

`sup_x |h(x+t)-h(x)| <= ||a||_infinity ||tau_t b-b||_1 ->0`.

Also `h in L^1`; a uniformly continuous `L^1` function vanishes at infinity. Hence `h in C_0`. This is the endpoint `(p,q)=(infinity,1)` companion to the completed fleet04/B15 finite-conjugate-exponent mixture theorem.

For three mutually uncoupled original coordinates after conditioning on the outside variables, two same-sign shifted square terms give a bounded density `<=pi/sqrt(|a_i a_j|)` by the beta integral, while the third nonzero shifted square contributes an arbitrary `L^1` density. The endpoint lemma therefore upgrades the conditional output to `C_0` without any extra height loss, and dominated convergence can then mix the outside conditioning.

For a genuinely joint near-null receiver, if two disjoint original-coordinate pairs each have a zero pivot and a nonzero cross coefficient, the fleet04/B15 pivot theorem at conjugate exponents gives a conditional convolution bound. This keeps the external coordinate jointly with the curved coordinate instead of conditioning it away.
