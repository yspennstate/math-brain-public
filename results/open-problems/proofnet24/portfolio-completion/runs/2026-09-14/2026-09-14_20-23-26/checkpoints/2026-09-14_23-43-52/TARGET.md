# Main target: Lyons determinantal entropy concavity

For every finite n, positive Hermitian contractions K0,K1 and t in [0,1], prove or refute H(P_((1-t)K0+tK1)) >= (1-t)H(P_K0)+t H(P_K1). P_K is the determinantal subset law with P(S subset X)=det K_S. Shannon entropy uses natural logs.

Primary statement: Russell Lyons, Determinantal Probability: Basic Properties and Conjectures (2014), Conjecture 2.6, https://arxiv.org/abs/1406.2707 . Originally conjectured in Determinantal probability measures (2003).

Existing source to inspect: Yuzhou Gu, Entropy of Determinantal Point Processes, https://sevenkplus.com/data/dpp.pdf . It gives rank-one direction concavity, a zero-endpoint inequality, and cardinality entropy concavity. Do not claim these known cases as new. A displayed intermediate inequality in its cardinality proof should not be copied without checking; the standard spectral majorization argument may repair it.

Exact atom formula: p_S(K)=det M_S(K), with column j of M equal to K e_j for j in S and (I-K)e_j otherwise. Interior 0<K<I gives p_S>0. In direction A=A*, let D_S have columns A e_j for j in S and -A e_j otherwise; R_S=M_S^{-1} D_S. Then p'_S=p_S tr R_S and p''_S=p_S[(tr R_S)^2-tr(R_S^2)]. Hence H''=-sum_S (p'_S)^2/p_S - sum_S p''_S log p_S. The first term is nonpositive; the second has no established general sign. These identities alone do not prove the conjecture.

Aim for a complete proof or exact certified counterexample. If an approach fails, save the exact obstruction and any fully proved restricted case. Small simulations and independent agreement are not universal proofs. Keep all hypotheses and distinguish established literature from session results. Each agent saves its own full report and computation files; parent integrates and pushes.
