# Early substantive checkpoint — diffuse teleporter rows

Run `20260923T125417Z-fleet02-B17-QFORM-auto11`, programme `QFORM-DENSITY-3EIG-20260922`.

The first unpaid sharp-witness mechanism attacked here is the one explicitly left open by fleet02/B17 `QFORM-VECTOR-INFINITESIMAL-SHARED-FRAME-NOESCAPE-v1`: deterministic row leverage tends to zero, but a fixed number of physical coordinates are scaled so that their *random row contributions remain order one with probability one*. Thus the row array is maximally non-infinitesimal in probability even though every spectral leverage vanishes.

Let `R_m` be any `n_m x 3` Parseval frame (`R_m^T R_m=I_3`) with maximum leverage `tau_m=max_i ||r_{mi}||^2 ->0`, and let `J=diag(1,1,-1)`. Choose exceptional rows `E_m` with aggregate Gram `D_m=sum_{i in E_m} r_{mi}r_{mi}^T ->0`. Put centered unit-interval inputs on every residual row and arbitrary independent cap-one inputs on the exceptional rows, and assume only that the exceptional latent aggregate `H_m=sum_{i in E_m}r_{mi}X_{mi}` converges in law to `H`. Then the residual latent aggregate has covariance `(I-D_m)/12` and satisfies Lindeberg automatically, hence converges to `G~N(0,I_3/12)`, independent of `H`. So the full latent vector tends to `G+H`.

The completed fleet03/B17 arbitrary-mean Gaussian theorem then gives, conditionally on `H=h`,

`||p_{(G+h)^T J(G+h)}||_inf <= 3 sqrt(2)`.

The genuinely new payment is the finite-row/local-spike gap. The pinned Claude Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies to the *actual physical form* `A_m=R_m J R_m^T` once `tau_m<=1/2` and gives

`|phi_m(t)| <= min(1,(4 pi)^(3/2)|t|^(-3/2))`.

This majorant is integrable. Since `Q_m => (G+H)^T J(G+H)`, dominated convergence gives `||phi_m-phi_inf||_1->0`; Fourier inversion therefore gives uniform convergence of the entire output density. Hence

`limsup_m ||p_{Q_m}||_inf <= 3 sqrt(2)`.

This closes a real branch not covered by the preceding probabilistically-infinitesimal theorem: a finite (or vanishing-total-Gram) set of diffuse-leverage rows may carry persistent arbitrary macroscopic randomness, yet it cannot create a hidden finite-stage density spike above the Gaussian obstruction when the complementary frame is the minimum-variance interval core.

Explicit source-valid stress instance: repeat the four tetrahedral rows `(±1,±1,±1)/(2 sqrt(L))`, giving a Parseval frame with leverage `3/(4L)` and exact nonzero spectrum `{1,1,-1}` for `R_L J R_L^T`. Mark one row of each tetrahedral type exceptional. Writing each such row as `s_L u_j`, `s_L=sqrt(3)/(2sqrt(L))`, choose any fixed bounded-density random variable `Z_j` and set physical `X_{Lj}=Z_j/s_L`; its density is `s_L g_j(s_L x)<=1` for all large `L`, while the row contribution is exactly `u_j Z_j`, order one. The other rows are centered unit intervals. Thus all physical inputs are independent and cap-one, supports may grow like `sqrt(L)` or be unbounded, every matrix has the exact target spectrum, and nevertheless the global output-density limsup is at most `3sqrt(2)`.

Full proof and checker follow in this run's immutable path. Full QFORM remains OPEN; this is a supporting witness exclusion, not a universal proof.
