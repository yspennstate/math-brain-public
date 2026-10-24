SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T08:00:56Z.
attacking: QFORM-BL-R2-PLUS-DIFFUSE-THIRD-SOURCE-RETAINED-TAIL-ENDPOINT-v2: couple the BL-compatible rank-two carrier to the physically diffuse third spectral source without collapsing product provenance.

# Early substantive calculation

Let `M` be a literal physical cross block with `s_2(M)>0`, let `W` be an additional disjoint physical column bank, and let `B=[M W]`.  Put `K=MM^T` and let `P_2` be any orthogonal projector onto a top-two left singular subspace of `M`.

The contribution to `E_3(B)=e_3(BB^T)` from three-column minors using exactly two columns of `M` and one column `w` of `W` is

`e_3(K+ww^T)-e_3(K)=w^T T_2(K)w`,

where `T_2(K)=K^2-tr(K)K+e_2(K)I` is the second Newton transform.  In an eigenbasis of `K`, with eigenvalues `lambda_1>=lambda_2>=...>=0`, the eigenvalue of `T_2(K)` in direction `i` is `e_2(lambda without lambda_i)`.  Hence on `range(P_2)^perp` it is at least `lambda_1 lambda_2=s_1(M)^2 s_2(M)^2`.  Summing over all columns of `W` gives the exact lower bound

`E_3([M W]) >= s_1(M)^2 s_2(M)^2 ||(I-P_2)W||_F^2 >= s_2(M)^4 ||(I-P_2)W||_F^2`.

This is the arbitrary-anchor-block extension of the account04/B19 double-anchor Cauchy--Binet mechanism.  It retains the full rank and all tails of `M` and `W`.

For the live r51/r52 robust light-light crossing,

`sigma_* = 4089/458752 = 0.008913312639508928...`.

At the transverse aggregate gate `delta=1/64`,

`E_3([M W]) > sigma_*^4 delta^2 = 1.5409786145696073e-12`,

so the completed marginal-free physical-E3 receiver `||p_Q||_infinity <= 6^(4/3) E_3^(-1/6)` gives

`||p_Q||_infinity < 1014.46149 < 1015`,

with a continuous `C_0` density.  Therefore any unpaid r51/r52 state must have aggregate transverse outside coupling `<1/64` on each side once the theorem is applied to the entire outside coordinate bank.

This is an early checkpoint only; the complete proof, scope, partner application, correction refresh and proof-assembly consequences are recorded in `REPORT.md` later in this same run directory.
