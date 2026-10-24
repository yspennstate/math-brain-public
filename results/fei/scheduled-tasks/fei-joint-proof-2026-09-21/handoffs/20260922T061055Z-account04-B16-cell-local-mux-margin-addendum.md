# account04/B16 margin addendum — owner-comparable c_G units

Scientific addendum commit: `e2a8d0c55ec680679e4f96549fb7a1d16bffac1a` at
`proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T061055Z-cell-local-mux-quadratic/MARGIN_ADDENDUM.md`.

For the balanced-address MUX, with `u=1-q0-q1`, `v=q1-q0`, the Poincare denominator is exactly
\[
Q_M=I(M)/4-p_{out}(1-p_{out})=(1-u^2-v^2)/8.
\]
Since `Gamma^dagger=Gamma0+a^dagger z(1-z)`, the owner's comparable base-potential margin is
\[
c_M=a^dagger-D_{Gamma^dagger}/Q_M.
\]
The new same-cell `rho<=3/20` theorem gives `D_{Gamma^dagger}>R_* p` with exact
`R_*=1114633887638025857/271020516100000000000` and `p=(1-u)/2`. Therefore
\[
\boxed{c_M<0.2599793983580645}
\]
uniformly on that theorem region. Relative to the lifted candidate itself the margin is `< -0.008225457641935514`.

This is the requested conversion from raw defect to comparable gate-margin units; it is analytic and does not change the theorem's remaining source-knot crossing obligation.
