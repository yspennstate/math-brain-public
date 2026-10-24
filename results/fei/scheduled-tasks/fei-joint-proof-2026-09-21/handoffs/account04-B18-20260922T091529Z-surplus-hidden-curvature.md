# account04/B18 handoff — surplus-weighted hidden-curvature reduction

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Canonical proof: `yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-22/account04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`, create commit `200e3fd37fe201f78d882ba8809414d201efb829`.

At a centered `F/J`-critical core of ratio `rho>4`, account01/B18's all-block curvature inequality makes the state all-block terminal at `K=4`. Let

`R_k=sum_{i!=k} c_k({i})`, `Omega_k=sum_{i!=k}[p_ki-2c_k({i})+4o_ki]`,

so account04/B18's exact mixed-curvature split gives

`4 d_k = 2 R_k + Omega_k`.

Write `sigma_k=h_2(q_k)-4q_k` and

`U_4=sum_k (4+j'(q_k)) Omega_k`.

The new scalar estimate is

`0 <= sigma_k <= lambda_4 (4+j'(q_k))`,

with

`lambda_4=(7/44) log_2(17/16)=0.0139145429261903...`.

It follows from the source-exact account01/B18 singleton constraint, `h_2(1/6)<2/3` (`6^6<16*5^5`), the exact derivative formula for `j'`, and `ln2<7/10`.

Combining this with account01/B18's global singleton crossing bank

`sum_k (rho+j'(q_k)) R_k <= P-DTC(X)`

gives the new weighted-depth reduction

`sum_k sigma_k d_k <= (lambda_4/2)(P-DTC) + (lambda_4/4) U_4`.

Fresh account04/B12 then yields, for relative-`1/16` near-subcube derivative rows,

`sum q_i^2(4+j'(q_i)) <= (128 lambda_4/105)(P-DTC) + (64 lambda_4/105) U_4`

and hence

`sum q_i^2(4+j'(q_i)) < 0.048944 J + 0.008482 U_4`.

For robust rows with `q_i>=tau`, their total influence is at most

`(0.012235851/tau) J + (0.002120312/tau) U_4`;

at `tau=1/16` this is `<0.195774 J + 0.033925 U_4`.

**Unpaid arrows:** (U1) a dimension-free payment/elimination for the hidden bank `U_4`, retaining the opposite-sign `4o` mode; (U2) small-influence and nonrobust positive-defect rows outside the inherited relative-`1/16` stability regime. The exact zero-depth branch remains classified as character-twisted one-point defects with `H<4J`. No raw `sum d_k=O(J)`, prescribed-coordinate payment, fixed-relative stability, fixed-`Gamma^dagger`, or decomposable-gate extremality claim is used.
