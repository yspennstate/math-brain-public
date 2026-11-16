---
name: c0033_sharp_quartic_bound_all_n_proved_cramer_rao_stieltjes_2026_11_08
description: "[VERIFIED] C0033 Lyons entropy: at reducible Q=Q1+Q2, quartic coeff b <= -2/(k(n-k)) for all n,k, sharp at Q=I/2; Cramer-Rao on centred cross-pair statistic + Stieltjes inverse; public as Theorem 4.3, repo c2ef48ef, ledger bbe0e037"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:23:54+02:00
  status: verified
  evidence: "cr_chain_check.py n=3..6 R/C min ratio 1.004, equality exact at I/2; proof steps re-derived 8 Nov 09:0x"
---

# Sharp fourth-order bound at reducible kernels, all n and k (8 Nov 2026, 08:2x)

Setting. Q = Q1 (+) Q2 with 0 < Q < I, blocks of sizes k and m = n-k. D Hermitian, off-block, X = D[:k, k:],
||D||_F = 1, x_ij = |X_ij|^2, so sum_ij x_ij = 1/2. p_S(Q+tD) = P_S + t^2 R_S + t^4 T_S + ...;
sum T log P = 0 and sum R log P = 0 (v2), so Ent(Q+tD) = Ent(Q) - (t^4/2) S + O(t^6), S = sum_S R_S^2/P_S.

Theorem. S >= 16 sum_ij x_ij^2 >= 4/(k m). Hence the quartic coefficient b = -S/2 <= -2/(k(n-k)),
with equality at Q = I/2 and |X_ij| constant. (Matches the numerical infima 2, 1, 0.5 for (1,1), (1,2), (2,2).)

Proof.
1. Cramer-Rao. sum_S R_S = 0, so for any f: (sum R_S f(S))^2 = (sum R_S (f - E_P f))^2 <= S * Var_P(f) (Cauchy-Schwarz
   with weights P_S > 0; full support since 0 < Q < I).
2. Statistic. xi = 1_S on block 1, eta = 1_S on block 2, q = diag Q, f = sum_ij W_ij (xi_i - q_i)(eta_j - q_j).
   Under Q+tD: P(i in S) = q_i (D has zero diagonal), and for a cross pair P(i,j in S) = q_i q_j - t^2 x_ij exactly.
   So sum_S R_S f(S) = -sum W_ij x_ij. Under P the two blocks are independent DPPs, so
   Var_P f = vec(W)' (C1 (x) C2) vec(W), C_r = Q_r o (I - Q_r)^T the indicator covariance: (C_r)_aa = q_a(1-q_a) <= 1/4,
   (C_r)_ab = -|Q_ab|^2 <= 0 for a != b, and C_r > 0 (full support).
3. M-matrix. C1 is a symmetric positive definite Z-matrix (Stieltjes), so C1^{-1} >= 0 entrywise.
   Take W = C1^{-1} V with V = (x_ij) >= 0. Then sum W_ij x_ij = tr G, G = V' C1^{-1} V (m x m, entrywise >= 0, PSD),
   and Var_P f = tr(G C2) <= sum_j G_jj (C2)_jj <= tr(G)/4 (off-diagonal: G >= 0 times C2 <= 0).
   So S >= tr(G)^2 / tr(G C2) >= 4 tr G.
4. One block. tr G = sum_j v_j' C1^{-1} v_j (v_j = column j of V, v_j >= 0). Cauchy-Schwarz:
   v' C1^{-1} v >= |v|^4 / (v' C1 v) and v' C1 v <= sum_a v_a^2 q_a(1-q_a) <= |v|^2/4 (v >= 0, off-diagonal <= 0).
   So tr G >= 4 sum_ij x_ij^2 and S >= 16 sum x_ij^2 >= 16 (1/2)^2/(k m) = 4/(k m).
5. Equality: at Q = I/2, C1 = I/4, C2 = I/4 and every inequality is an equality when the x_ij are equal; the exact S at
   Q = I/2 equals 16 sum x^2 (cr_chain_check.py: 2, 1, 2/3, 4/9 for (n,k) = (3,1), (4,2), (5,2), (6,3)).

Remark. The cruder bound 16 x'(C1 (x) C2)x <= |x|^2 is FALSE for complex kernels (1.087 at k=m=2, kron_cr_test.py);
the M-matrix choice W = C1^{-1} V is what makes the argument go through. The k=1 case also has the factorisation
S = F_2(xx*)/(q(1-q)) with F the DPP Fisher information, and F(H) >= 4 sum H_jj^2 holds whenever diag(H) has one sign
(same Cramer-Rao with f = sum h_j 1_j); it fails for mixed signs (H = diag(1,-1) near a projection).

Checks (all on disk in this folder): cr_chain_check.py (S >= CR >= 16 sum x^2; min S/CR 1.000-1.015, min CR/(16 sum x^2)
1.02-1.08 over n = 3..6, real and complex; equality exact at I/2), kron_cr_test.py, fisher_rank1_test.py,
chi2_bound_test.py (S/(16 sum x^2) >= 1.003 on 300 random kernels per case).

