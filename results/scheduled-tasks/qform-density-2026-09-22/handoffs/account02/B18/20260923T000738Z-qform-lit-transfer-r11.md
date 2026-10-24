SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-23T00:07:38Z.
attacking: strict-N3 source-coordinate glue between cross-volume and hub regimes, with primary-source variational reduction and designated-partner transfer.

# account02/B18 handoff — strict-N3 cross-rank obstruction plus paid hub/diffuse branches

**Status:** supporting theorems proved; full QFORM and N3 remain **OPEN / NOT PROVED**. Execution remains `WITHOUT_VERIFIED_BRAIN`.

**Canonical math:** `yspennstate/math-open-problems@29b17fdbcd2dbd28074cf4593895e81e6ae441e5`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T000738Z-qform-lit-transfer-r11/REPORT.md`, blob `9ea17f6082d76ef299da1b599bbd2a95cdbc4a45`.

## First unpaid implication

`QFORM-N3-HUB-OR-CROSSVOLUME-GLUE-v1`: in strict N3, prove a universal quantitative dichotomy sending every matrix either to a payable D'/D5/account03-B18 physical cross-volume cut, or to a source-coordinate Theorem-H hub/light-block frame, or to an already-paid scalar-pivot/ridge/physical-pair branch. A rank-3 physical cross cut cannot simply be assumed.

## New strict-N3 obstruction and payment

For `m>=2`, put `S_m=[[0,m^(-1/2)1_m^T],[m^(-1/2)1_m,0]]` and `A_m=S_m direct_sum (J_m/m)`. Then `spec(A_m)={1,-1,1,0,...,0}`; every diagonal and every physical 2x2 principal determinant has modulus at most `1/m`; hence for fixed `tau in (0,1]`, `m>1/tau` puts `A_m` in strict N3. Yet every physical cut has cross rank at most two: the star and bank contribute ranks at most one each. Therefore `N3 => exists rank>=3 physical cross cut` is false.

This is not a QFORM counterexample. Applying pinned `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` Theorem H with the source hub and the diffuse rank-one bank gives

`|phi(t)| <= 4 pi^(3/2)|lambda|^(-1/2)||g||^(-1)|t|^(-3/2)`

and hence

`||p_Q||_infinity <= 3*2^(4/3)|lambda|^(-1/3)||g||^(-2/3) <= 7.559526299...`.

Thus the normalized star-plus-bank strict-N3 family is paid, continuously, for all independent cap-one laws.

## Primary-source variational transfer

Madiman–Melbourne–Xu, arXiv:1705.00642, Theorem 1.5 plus the non-atomic extreme-point description, applies to `Phi_J(mu_1,...,mu_n)=P(Q(X) in J)` for each open interval J: it is coordinate-affine and lower semicontinuous because `Q^{-1}(J)` is open. The interval supremum over all cap-one product laws therefore equals the supremum over compact measure-one indicator densities; regular approximation reduces further to finite unions of bounded intervals. This adds no moment or support-radius assumption and is interval-by-interval, not a universal extremizer statement.

## Designated partner applied

Completed account03/B18 r19, `math-open-problems@9415d0f2696d2e6ca05243c8e8f34b665bf5d42f`, proves for an original-coordinate physical cross block of rank `r>=3`

`||p_Q||_infinity <= [2r/(r-2)](prod sigma_l)^(-1/r)`

with arbitrary same-side measurable phases. Its LPP input was primary-source checked against arXiv:1507.07949v2: k-dimensional orthogonal marginals of cap-one product laws have density cap at most `2^(k/2)`, without moments, support, log-concavity or smoothness.

For three disjoint rank-one banks `lambda_l u_lu_l^T` with `u_l(i)^2<=delta<1/2`, a greedy half-mass physical cut gives `sigma_l>=|lambda_l|sqrt(1/4-delta^2)`, hence

`||p_Q||_infinity <= 12/sqrt(1-4delta^2)`.

For even uniform banks `(J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`, the bound is `12`, and this family lies in strict N3 once `m>1/tau`.

## Necessary geometry for any genuine counterexample sequence

Pinned D5 gives for every physical cut

`||p_Q||_infinity <= 5 sqrt(2e) e_5(A_IJ^T A_IJ)^(-1/10)`.

Hence any hypothetical sequence with density caps `M_k->infinity` must satisfy

`sup_{I|J} e_5((A_IJ)^T A_IJ) -> 0`.

On exact cross rank 3 or 4 the partner theorem further forces singular products to vanish at rates `(6/M)^3` and `(4/M)^4`. Thus a counterexample must concentrate remaining three-volume into a hub/high-marginal regime or higher-rank near-degeneracy; the simplest hub model above is already paid.

**Source/correction status:** OWNER CONTROL revision `2026-09-22.15`; pinned synthesis `e5f71d79eff325201dd0274053d20268ce65b837`; no post-rotation independence, arbitrary-joint coarea, hidden moments/support/log-concavity, or search-miss novelty. Full target remains open.
