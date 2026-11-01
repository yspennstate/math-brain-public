SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T11:04:29Z.
attacking: numerical-rank cross-footprint stability for arbitrarily many signed eigenvalue replacements, with a full-rank dense tail paid only at matrix level.

# Early checkpoint: numerical-rank D5 stability

Full QFORM remains OPEN. This checkpoint records the first substantive implication before the final report.

Let I,J be disjoint ORIGINAL-coordinate banks, M0=A0[I,J], and A=A0+S+T with S symmetric completely arbitrary and ||T||op<=delta. For r>=0 put

eta_r := inf_{rank L<=r} ||S[I,J]-L||op = s_{r+1}(S[I,J])

(with eta_0=||S[I,J]||op), and rho=eta_r+delta. Choose a best rank-r approximation L and write S[I,J]=L+R, ||R||op=eta_r. Rank-r singular-value interlacing followed by Weyl gives, for j=1,...,5,

s_j(A[I,J]) >= s_{j+r}(M0)-rho.

Hence with a_j=(s_{r+j}(M0)-rho)_+, the pinned e5f71d79... D5 theorem gives, whenever a_5>0,

||p_Q||inf <= 5 sqrt(2e) (a_1 a_2 a_3 a_4 a_5)^(-1/5).

In particular, if s_{r+5}(M0)>=kappa>rho,

||p_Q||inf <= 5 sqrt(2e)/(kappa-rho).

This is matrix-level stability only: no assertion is made that X^T T X is small. S may have arbitrary global rank, signs, self blocks and norm; only the operator tail after removing r cross directions is charged.

For a spectral update S=sum_a tau_a v_a v_a^T, any group G whose I-side footprints span dimension <=r contributes a cross matrix of rank <=r and therefore costs no magnitude. The remaining group B is charged only by

eta_r <= sum_{a in B} |tau_a| ||(v_a)_I||_2 ||(v_a)_J||_2.

Next step in this run: build an exact target-class family with arbitrarily many independently arbitrary eigenvalue replacements whose physical cross footprint remains rank one, then combine the D5 certificate with the latest fleet03/B12 compression certificate under the same dense tail.
