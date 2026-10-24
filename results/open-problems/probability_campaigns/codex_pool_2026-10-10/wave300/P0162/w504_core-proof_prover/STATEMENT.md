# P0162 statement sent before the proof packet

For every integer n >= 1 and every Boolean function f:{-1,1}^n -> {-1,1}, use the uniform measure and characters chi_S(x)=product_{j in S} x_j. Write a_S=E[f chi_S], p_S=a_S^2, H(f)=sum_S p_S log_2(1/p_S), and I(f)=sum_S |S|p_S. Zero summands are zero. The FEI target is the existence of one finite constant C, independent of n and f, such that H(f)<=C I(f). Parseval gives sum_S p_S=1. Constants have both H and I zero. No balance, monotonicity, independence, or circuit-size assumption is part of the target.

Primary source checked: Gonzalez, MacManus, Pereyra, Further evidence towards the Fourier Entropy-Influence conjecture, arXiv:2606.00246v1 (29 May 2026), introduction, equations defining H and I and FEI Conjecture: https://arxiv.org/html/2606.00246v1 . Origin attributed there to Friedgut and Kalai (1996); origin paper retrieval is pending. Wan, Wright, Wu, arXiv:1312.3003, independently states the same target.

Restriction route to test independently: for coordinate i put f_i^+=f|_{x_i=1}, f_i^-=f|_{x_i=-1}, and Delta_i(f)=H(f)-[H(f_i^+)+H(f_i^-)]/2. The sufficient missing lemma is: some finite universal C has, for every nonconstant Boolean f, at least one coordinate i with Delta_i(f)<=C Inf_i(f). The quantifier is EXISTS i. The stronger statement FOR EVERY i is a separate possible claim and is not assumed.

This file intentionally contains no construction or proof result. Independent adversary: w505; referee: w506. Current openness remains UNKNOWN until source and owner-work checks finish. No novelty claim.
