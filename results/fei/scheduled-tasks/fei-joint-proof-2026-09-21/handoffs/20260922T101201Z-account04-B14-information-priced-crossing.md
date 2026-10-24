# FEI handoff — account04/B14 information-priced posterior crossing

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Scientific report: `yspennstate/math-open-problems`, commit `4a61a14227359dfbb512bdd6bb73b9627c37f50b`, path `proofnet24/P03-fei/fleet-2026-09-22/account04/B14/20260922T101201Z-information-priced-crossing/REPORT.md`.

Consumed exact account01/B18 curvature source: `account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`, with

`Delta_A F <= B_A - sum_{j notin A} j'(p_j)c_j(A)`

and exact folded drift

`D_A = J(parent)-E J(child) = I_A + C_A`.

Also consumed fresh account01/B18 shaped-safe-frontier report commit `a5f19f05fa03671fb5ffeb435081ed92e9827e6a`; its all-gate prime obligation remains open.

## New universal crossing price

For a survivor pivotality event `eta_j` of marginal `p_j<=1/2`, a physical block `A`, and posterior `U=P(eta_j=1|X_A)`, the exact identity

`E min(U,1-U)=p_j-c_j(A)`

plus binary-entropy concavity gives

`I(eta_j;X_A) >= h2(p_j)-h2(p_j-c_j(A))`.

Hence if `c_j(A)>=gamma p_j`, then

`I(eta_j;X_A) >= h2(p_j)-h2((1-gamma)p_j) >= gamma p_j log2((1-p_j)/p_j)`.

This prices crossing by information acquired by the whole physical block; it is not prescribed-coordinate payment.

## Realizable gross-Shannon stopping

Fix `K>0`, `0<gamma<=1`. At each reached centered physical restriction, reveal a deterministic-choice original-coordinate block `A` only when there is a survivor `j` with both

`c_j(A)>=gamma p_j`,  and  `B_A<=K D_A`.

Then recurse on the realized child and stop when no such pair remains. Exact drift telescoping gives

`sum_v pi_v B_{A_v} <= K sum_v pi_v D_{A_v} <= K J(root)`.

Thus the entire executed adaptive phase has literal/gross unpaid Shannon `O(J)`. At every executed node the selected crossing also carries the information certificate above.

Concrete clean choice: `K=4`, `gamma=1/2`, giving total gross Shannon at most `4J(root)` and per-crossing information at least `h2(p)-h2(p/2)`.

## Terminal class and B18 source-to-next-arrow

At every terminal leaf, every large crossing is gross-expensive:

`c_j(A)>=gamma p_j  =>  B_A>K D_A`

for every physical block/survivor pair.

For every executed block, B18 gives

`Delta_A F <= B_A-W_A <= K D_A-W_A`,
`W_A=sum j'(p_j)c_j(A)>=0`.

So the gross Shannon is already drift-paid and the curvature refund remains unspent; no refund is reused. On a ratio-rho critical core B18 gives `B_A>=rho D_A+W_A`.

**Next exact arrow:** on the terminal high-`B_A/D_A` class, combine the forced pivotality mutual-information price with the explicit B18 curvature credit `j'(p_j)c_j(A)` to rule out high-ratio cores, or exhibit an actual Boolean obstruction satisfying both constraints. Do not claim this comparison is already proved.

The known addressing obstruction is preserved throughout; no fixed target coordinate is asserted to pay its own erasure. Full FEI remains OPEN.
