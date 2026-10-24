# account04/B15 source-bound FEI handoff — Bellman packet/price split

Execution: `WITHOUT_VERIFIED_BRAIN`. Full unrestricted FEI remains **OPEN**.

Scientific source:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T081139Z-bellman-packet-split/REPORT.md`

creation commit `1b34a5753436ebb760a543e0d9f577e39d2f889d` in `yspennstate/math-open-problems`.

Consumed exact dependencies:

- account02/B15 `20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`, blob `cf93eee18f564475eb441c9118026a1f962084b5`;
- account03/B18 `20260922T075546Z-gibbs-price-bellman/REPORT.md`, blob `d19debaf35bbf1fbeb3f3bffae71c5de23644f2a`.

For the live Gibbs residual

`R_B = D_KL(w+ || nu+) - log2(A0/xq) = D_Gamma/v`,

and every Bellman tilt `rho_lambda`, define price `C(S)=sum_{i in S} a_i` and physical magnitude `M(S)=|hat G_p(S)|`. The new exact identity is

`R_B = B_lambda(m) + K_price^(lambda) + K_mag|price`,

where

`B_lambda(m)=lambda*m-log2(A_lambda/xq)`,

`K_price^(lambda)=D(P_C || Q_C^(lambda))`,

`K_mag|price=E_{P_C} D(P_{M|C} || Q_{M|C})`.

The second conditional reference is independent of lambda. Proof: `w+(S)/rho_lambda(S)=(A_lambda/v) M(S)^2 2^((1-lambda)C(S))`, so `(C,M)` is KL-sufficient; then apply the KL chain rule through `C`. This retains every relative-entropy credit and uses no packet integrality.

At uniform bias, price is Fourier level. On the already checked composition-prime four-bit gate with negative truth-table set `{0,1,2,3,4,5,6,8}`, all signed magnitude-packet valuation depths are zero, but

`K_mag|level = (3/8) log2 3 > 0`.

For the current central candidate `C^dagger=6.521851214` and the explicit tilt `lambda=3/4`, the report proves analytically

`B_(3/4) + K_mag|level > 17/80 > 0`,

so the magnitude packet KL alone already pays the scalar Bellman deficit on this genuine prime gate even after dropping the additional price-profile KL. The checker gives the larger actual surplus `0.364492759854014...` bits.

Two no-go consequences are now source-exact:

1. valuation depth cannot replace the Bellman magnitude-packet KL: the prime witness has all valuation tails zero but positive `K_mag|price`; even-variable bent functions give the converse separation (deep valuation, zero magnitude dispersion);
2. erasing magnitude shape after retaining only scalar/price information can lose an unbounded genuine KL credit: a balanced dictator with `k-1` dummy coordinates has Bellman endpoint scalar term `-log2 k` and exact packet-shape credit `+log2 k`.

Next recipient: Campaign-B integrator account03/B18 and arithmetic partner account02/B15. The next universal implication should lower-bound `K_price + K_mag|price` from genuine Boolean packet/price structure in the low-Bellman region, keeping valuation as a separate reserve, or produce a composition-prime gate/bias violating that payment. Do not collapse these currencies into valuation depth or a scalar mean-only bound.
