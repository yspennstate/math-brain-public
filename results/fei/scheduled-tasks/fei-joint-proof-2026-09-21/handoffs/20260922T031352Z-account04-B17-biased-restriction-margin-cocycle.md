# account04/B17 handoff — exact biased restriction margin cocycle

**Run:** `20260922T031352Z-b17-fei-r17`  
**Status:** `WITHOUT_VERIFIED_BRAIN`; full FEI **OPEN / NOT PROVED**.  
**Canonical source:** `yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, creation commit `b6897a3675bb78bb3c262bc73f64ffb1e9c20301`; checker commit `9029b00e3825d8450f1718a6caa1a7a1c15b2a5f`; verification output commit `a35489848496d71886c353c8716e74ad14086959`.

For a Boolean gate `G`, product bias, pivot `j` with `t=p_j`, restrictions `G_0,G_1`, output biases `r_0,r_1`, disagreement `delta_j`, and exact information credit `C_j=H(B|S)+I(S;J)>=0`, the current all-gate defect satisfies

`D_G = (1-t) D_{G_0} + t D_{G_1} + R_j + C_j`,

where

`R_j=(1-t)Gamma(r_0)+t Gamma(r_1)-Gamma(r)+delta_j[Gamma(t)+h_2(V_t)]-h_2(t)-h_2(It_j)`

and `It_j=V_t delta_j`. For a quadratic lift `Gamma_c=Gamma_0+c p(1-p)`, the exact local currency is

`W_j=t(1-t)[delta_j-(r_1-r_0)^2]>=0`,

with `W_G=(1-t)W_{G_0}+tW_{G_1}+W_j`. Hence the global requested scalar margin `-D_{Gamma_0}(G)/W_G` is an exact nonnegative weighted average of positive-currency local restriction-gluing margins `-(R_j+C_j)/W_j` on any complete restriction tree.

The KL/branch credit is mandatory: for a biased literal, `R_j=-h_2(t)` while `C_j=+h_2(t)`, so any credit-free local condition fails exactly.

Fresh B0 handoff (`A={0,1,2,3,4,5,8,10} subset Q4`) at uniform bias splits into two pivot orbits. Pivots 2/3 have `It=1/2`, `C=1`, `W=1/16`, local base term `Gamma_0(1/4)-Gamma_0(1/2)/2-1`. Pivots 0/1 have `It=1/4`, `C=4-(15/8)log_2 3`, `W=3/64`, local base term `Gamma_0(3/8)-(3/4)Gamma_0(1/2)+1-(9/8)log_2 3`.

**Next exact obligation:** evaluate/certify these local margins for the live successor `Gamma` and then attack the general local two-restriction gluing inequality with the credits preserved. Any violation is an exact Boolean adversary; a universal nonnegative local inequality would imply the all-gate scalar-lift statement by the weighted-average theorem.