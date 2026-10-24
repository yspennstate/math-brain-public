C0044 statement for independent attack (2026-10-10)

Let d >= 3, E = {+e_1,-e_1,...,+e_d,-e_d}, and let P be a product law on nearest-neighbor transition probability vectors omega(x,.) at sites x in Z^d. Each vector has total mass one and omega(x,e)>0 for every e, P-almost surely (strict ellipticity). The environment is sampled once and retained on revisits. P_x^omega is the Markov path law with transition x -> x+e of probability omega(x,e); P_x = integral P_x^omega dP is the annealed law. For each fixed deterministic nonzero l in R^d, let A_l = {lim_n X_n dot l = +infinity}. The target is P_0(A_l) in {0,1}.

The uniformly elliptic specialization additionally assumes a deterministic kappa>0 with omega(x,e)>=kappa almost surely for all x,e. This is a stronger assumption, not a consequence of strict ellipticity.

Primary historical reference: Zerner and Merkl, Ann. Probab. 29 (2001), 1716-1732, introduction and Theorem 1, https://www.math.uni-tuebingen.de/~zerner/pub/zeroone.pdf. Their planar theorem has d=2 and does not imply the d>=3 statement.

Current-status caveat: https://raw.githubusercontent.com/openai/math/main/lean/docs/220.md now claims the full strictly elliptic d>=3 result and links a September 23, 2026 preprint. The claim is not independently verified here. Current openness stays UNKNOWN until primary theorem semantics, hypotheses, and proof are checked. No proof argument is included in this statement packet, so w586 can begin independently.
