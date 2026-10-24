SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T07:21:07Z.
attacking: spectral-threshold/footprint control of full nonseparable tails at the matrix level.

# Early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN; execution `WITHOUT_VERIFIED_BRAIN`.

Let `I,J` be disjoint original-coordinate sets and let `H=H^T` be an arbitrary symmetric spectral modification. With `P_I,P_J` the corresponding coordinate projections,

`eta(H;I,J)=||P_I H P_J||op`

obeys the exact deterministic bounds

`eta <= min{ ||P_I H^2 P_I||op^(1/2), ||P_J H^2 P_J||op^(1/2), [||P_I |H| P_I||op ||P_J |H| P_J||op]^(1/2) }.`

The first two follow from `||P_IHP_J||<=||P_IH||` and `||P_IH||^2=||P_IH^2P_I||`; the third follows from the polar factorization `H=|H|^(1/2) sgn(H) |H|^(1/2)` and submultiplicativity.

For a spectral threshold `h>=0`, split `S=sum tau_k u_k u_k^T` as `S=H_h+L_h` with `|tau_k|>h` in `H_h` and `|tau_k|<=h` in `L_h`. Then `||L_h||op<=h`, while the unbounded large modes satisfy the footprint estimate above. Therefore any baseline cross-certificate stable under a cross perturbation of size `eta` plus an operator-norm tail of size `delta` is preserved with effective budget

`epsilon_h = delta + h + chi_h`,

where `chi_h` is the minimum of the three displayed footprint bounds for `H_h`.

Next step in this run: insert this `epsilon_h` into the completed account02/B12 thresholded cross-footprint theorem and the current D5/fractional-volume exits, then give a literal multi-eigenvalue replacement family where arbitrarily many signed eigenvalue changes are unbounded but `epsilon_h` stays universal.
