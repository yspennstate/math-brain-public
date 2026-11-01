# P0117 adversarial packet

Worker w385, 2026-10-10. Precise working target: iid finite nonnegative atomless weights on undirected nearest-neighbor Z^2, with E[min(t1,t2,t3,t4)^2]<infinity; almost surely no injective doubly infinite minimizing path, simultaneously over every path and direction. The original intake's full hypothesis scope and present openness remain UNKNOWN. A dated public manuscript claims this moment-restricted result; retrieval is not a correctness certificate.

INDEPENDENT.md was saved, including its main reductions and obstruction, before reading w384/ATTEMPT.md. I then read that author's original route, not a referee's review.

## Independent result and the hard gap

The origin bigeodesic event equals the decreasing intersection of shell-witness events E_n. The outstanding input is P(E_n)->0. The crossing/counting argument in INDEPENDENT.md yields (2n+1)q_n+2 sum_{r=n+1}^{Cn}q_r>=1-o(1), where q_n is the maximum full-lattice shell-pair midpoint probability. Thus q_n is not o(1/n); the raw binomial(8n,2)q_n union bound cannot be rescued by seeking an o(n^-2) rate. These are candidate derivations pending w386's check. They neither prove nor refute the FPP conjecture.

## Audit of w384's deleted-edge route

Verdict: KEEP the mathematical reductions, subject to the stated outside-properness event and atomless law; support collapse remains UNPROVED. I did not find a counterexample to the claimed reduction.

For an edge e={u,v}, let d be the metric with e deleted, c_e(x,y)=min(d(x,u)+d(v,y),d(x,v)+d(u,y)), and D_e=d(x,y)-c_e(x,y). Decompose a simple minimizing path according to whether it avoids e or uses its one possible traversal. This proves the lower bound in T_s(x,y)=min(d(x,y),s+c_e(x,y)). The reverse bound uses a d-minimizer or a concatenated walk via e, followed by cycle removal. Overlapping d-minimizers do not invalidate the equality; strict preference for e rules out removing e entirely.

For shells containing e strictly in their interior, H_n=max(0,max_{x,y in S_n}D_e(x,y)) is measurable with respect to all weights other than t_e and bounded by d(u,v). If s<H_(n+1), truncate a strictly e-using minimizing path at its first smaller-shell hits on both arms. An e-avoiding competitor for the subpath would splice into an e-avoiding outer walk, contradicting strict preference. Thus H_(n+1)<=H_n. Fixed-edge diagonal compactness then turns witnesses on every shell into a bigeodesic using e. The proof supplies compactness but does not supply the witnesses.

Because t_e is independent of the outside sigma-field and atomless, every equality t_e=H_n and t_e=H_infinity has probability zero. Off their countable union, the shell witness event is exactly t_e<H_n and its intersection is t_e<H_infinity. Therefore P(A_e|outside)=F(H_infinity), where F(h)=P(t_e<=h). If a is the essential infimum, continuity makes F(h)=0 precisely for h<=a. This integrates one genuinely independent edge weight. No independence of different capacities or scales was used or inferred.

The hardest missing lemma is consequently H_infinity<=a almost surely, for the actual Z^2 outside environment. The author identifies this as an equivalent open input. Order-n shape control cannot establish the required order-one bound on d-c_e; selected endpoint maxima and false per-scale products cannot be silently inserted.

## A local filtration route and its remaining input

For a local alternative, define G_n using the metric restricted to B_n: some simple box-minimizing path through 0 joins two distinct vertices of S_n. G_n depends only on the edge weights inside B_n and G_(n+1) is contained in G_n, by first-shell-hit truncation. Its decreasing intersection is also the bigeodesic-through-0 event. To prove the converse, stabilize centered witness segments. For any fixed competing finite path, eventually the boxes contain that competitor, so box minimality gives global minimality of the limiting segment. Thus this version correctly supplies an adapted event for the filtration F_n=sigma(weights on edges inside B_n).

A sufficient but still UNPROVED fresh-annulus input would be an increasing deterministic sequence r_k and numbers epsilon_k in [0,1), with sum epsilon_k=infinity, such that P(G_(r_(k+1))|F_(r_k)) <= (1-epsilon_k) 1_(G_(r_k)) almost surely. The tower property, measurability, and nesting would then imply P(G_(r_k))<=P(G_(r_1)) product_{j<k}(1-epsilon_j)->0. This is a valid conditional proof route conditional on that input. Independence of disjoint annular weights alone does not establish the input: the existence and minimization events depend on how every candidate path uses those weights.

Switching to G_n also changes the metric. Full-lattice midpoint theorems cannot be applied to box-minimizers without a comparison argument. A concrete iid-realizable control demonstrates this. In B_1, set the two horizontal edges incident to 0 to weight 1 and other B_1 edges to weight 10. Between (-1,0) and (1,0), the unique box geodesic passes through 0 with weight 2. Outside B_1, the ten-edge route through (-2,0),(-2,1),(-2,2),(-1,2),(0,2),(1,2),(2,2),(2,1),(2,0) has edges of weight 1/10 and costs 1. Any simple path through 0 costs at least 2 from its two incident edges, whatever happens farther away. Thus no full-lattice minimizer for these endpoints passes through 0.

This is not limited to atomic weights: under iid Uniform[0.05,10], require the two origin corridor edges to lie in [0.95,1.05], the other ten B_1 edges in [9,10], and the ten detour edges in [0.05,0.1]. This finite cylinder has strictly positive probability. The box route costs at most 2.1, every box alternative uses high edges, the exterior route costs at most 1, and any route through 0 costs at least 1.9. The metric-substitution failure thus occurs under an atomless iid law with all required moments. It is an inference counterexample, not a bigeodesic construction.

## Stronger control on the support-collapse attempt

Planarity, atomless iid weights, and properness alone do not force support collapse. On the nearest-neighbor ladder Z x {0,1}, give edges iid Uniform[1,2] weights. Geodesics between (-n,0) and (n,0) exist and are unique almost surely. Each must cross one of the two edges of the fixed cut between columns 0 and 1. Infinitely many witnesses therefore use one fixed cut edge. Anchored diagonal compactness yields a bigeodesic through that edge. The two cut edges have the same law by row interchange, so each has bigeodesic probability at least 1/2. Deleting either cut edge leaves the ladder connected, and the deleted-edge threshold formula remains valid. Hence E[F(H_infinity)]>=1/2 for such an edge and H_infinity>a=1 with positive probability. The required new ingredient must use the full two-dimensional Z^2 geometry, beyond planarity and properness. This control is outside the target graph and does not refute P0117.

## Recent primary manuscript: bounded audit scope

Downloaded the original public 39-page PDF into sources/openai_20260924.pdf. Its main theorem has the working target's moment-restricted assumptions. The extracted source lists separate steps for opposite functionals, countable exceptional labels, half-plane transfer, a label budget, and conditioned modifications. w386 is auditing the label-budget/exceptionality route. I have not independently certified those load-bearing results; present openness stays UNKNOWN and this packet claims no novelty or resolution.

NEXT: w386 checks the independent crossing bound, local filtration equivalence, and inference controls; then the validating coordinator may admit the draft concepts without promoting support collapse to a theorem.
