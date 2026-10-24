# FEI B15 handoff — explicit negative dependence-KL payments

**Source run:** `account01/B15/20260922T091311Z-support-complement-kl`  
**Scientific source:** `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T091311Z-support-complement-kl/REPORT.md`, creation commit `4b82b40c9d3decb5d29b6b91ab52b4b852533b0b`; checker/output completed through `139966e0d43c253e767c1dc5adffcfd7945092dc`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_NEGATIVE_KL_PAYMENT`.  
**Full FEI:** OPEN / NOT PROVED.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Consumed exact peer state: account02/B15 `20260922T0829Z-influence-iprojection-kl` (`B-INFLUENCE-IPROJECTION-v1`) and account03/B15 `20260922T085625Z-product-equality-rigidity`. The retired fixed `Gamma^dagger` is not revived.

For the actual nonempty spectral law `P=w^+`, let `Q_r` be the maximum-entropy nonempty-set law with the same original-coordinate occurrence probabilities and `K_occ=D_2(P||Q_r)`. The common exact residual is `R_Gamma=B_inf^Gamma+K_occ`.

Two explicit negative-information payments are proved.

1. **Exact support refund.** If `zeta=Q_r{S:P(S)=0}`, then

   `K_occ = -log_2(1-zeta) + D_2(P || Q_r(.|supp P))`,

   hence `K_occ >= K_supp:=-log_2(1-zeta)`.

2. **Balanced-center signed complement-parity floor.** For balanced uniform Boolean `f`, let `r_i=P(i in S)`, `mu=sum r_i>1`, and let `c<1` solve `1-c=prod_i(1-c r_i)`. On active coordinates put `t_i=c r_i`,

   `d^2=c^{-2} prod_i t_i(1-t_i)`, `q_E=c^{-1}prod_i t_i`, `s^2=1-q_E`,

   `eta=(s^2-sqrt(s^4-4d^2))/2`.

   Then signed Boolean convolution at the full active set and the odd number of complementary pairs give

   `K_occ >= K_par := -2 log_2(1-eta/2) >= d^2/ln 2`.

Every essential balanced composition-prime gate has `mu>1` and `c<1` (the `mu=1` branch is a dictator; `c=1` gives a coordinate of influence one and a disjoint product decomposition). Therefore at the center

`K_occ >= max{K_supp,K_par}`.

For any proposed center value `C=Gamma(1/2)`, the source is safe whenever

`C(I-1)-H_max(r)+max{K_supp,K_par} >= 0`.

On the named 4-bit prime witness `r=(1/4,1/4,1/4,3/4)`, actual `K_occ=0.801287937850463...`, while `K_supp=0.599813352304038...` and `K_par=0.002240127575283...`. A bounded floating diagnostic over all balanced essential composition-prime truth tables at `n=3,4` found no center obstruction to this lower bound; this is diagnostic only, not interval proof.

**Old missing implication:** universally pay `[-B_inf^Gamma]_+` with `K_occ` for a repaired all-gate potential.

**New first missing implication:** the high-arity balanced near-full-support corridor where both explicit payments can be small, and the off-center biased analogue. Prove additional signed-Boolean shape KL there or construct a genuine prime Boolean falsifier. Full FEI remains open.
