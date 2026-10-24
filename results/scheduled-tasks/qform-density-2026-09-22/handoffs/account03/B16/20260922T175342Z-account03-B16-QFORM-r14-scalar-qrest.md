SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T17:53:42Z.
attacking: after owner revision 2026-09-22.11 retired full-vector conditioning, test the replacement scalar-Q_rest worst-conditional-density target before using it.

# account03/B16 addendum — scalar Q_rest worst-condition bridge is also false

Fresh owner revision `2026-09-22.11` proposed `M=sup_b ||p_{Q3|Q_rest=b}||_infinity` as the next universal bridge. The identity `||p_Q||_infinity<=M` is valid, but a universal bound on `M` is false.

Canonical proof: `yspennstate/math-open-problems@850ab3e996732591f8bf32b3f905528079545870`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T175342Z-account03-B16-QFORM-r14/SCALAR_QREST_CORRECTION.md`.

Take independent cap-one laws `X_1,X_3,X_4 ~ Unif[0,1]`, while `X_2` has density equal to the indicator of `union_{k=0}^{m-1}[10k,10k+1/m]`. Put

`S=(X1+X2)/sqrt(2)`, `D=(X1-X2)/sqrt(2)`,
`Q3=D^2+X3^2-X4^2`, `Q_rest=S^2`.

Then the full form is exactly

`Q=Q3+Q_rest=X1^2+X2^2+X3^2-X4^2`,

so it is diagonal and its full density is already bounded by `pi`.

At `b_m=1/(2m^2)`, conditioning on `Q_rest=b_m` is the same as conditioning on `S=1/(sqrt(2)m)`, and exactly

`D | (Q_rest=b_m) ~ Unif[-1/(sqrt(2)m), 1/(sqrt(2)m)]`.

For `T=X3^2-X4^2`,

`p_T(t)=0.5 asinh(sqrt((1-t)/t))` for `0<t<1`, hence `p_T(d^2)=0.5 acosh(1/d)`. Therefore

`p_(Q3|Q_rest=b_m)(0)
 = (1/(2a_m)) integral_0^{a_m} acosh(1/d) dd
 >= 0.5 (log(sqrt(2)m)+1)`,

where `a_m=1/(sqrt(2)m)`. Thus

`sup_b ||p_(Q3|Q_rest=b)||_infinity -> infinity`.

The mechanism is exact: scalar conditioning squeezes the `D` core direction to width `O(1/m)`, leaving the opposite-sign rank-two logarithmic singularity smoothed only at scale `m^-2`. Averaging over `Q_rest` is essential; the worst-condition supremum discards that smoothing.

This is **not** a QFORM counterexample. It is a source-valid refutation of the revision-2026-09-22.11 scalar worst-conditional bridge. The replacement must control the shifted mixture directly, or aggregate original-coordinate product structure before taking a worst condition. Full QFORM remains OPEN; continuity remains unproved.
