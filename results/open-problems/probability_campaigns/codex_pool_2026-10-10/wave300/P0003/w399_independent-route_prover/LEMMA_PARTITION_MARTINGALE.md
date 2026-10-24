# Finite-SAW obstacle martingale, independently checked background

w401 returned KEEP for this finite-graph scope; RECEIVED_W401_VERDICTS.jsonl records it. This is rederived background, not a distinct new fleet result or a scaling-limit proof.

Let G be a finite undirected graph, a != b vertices joined by at least one path, and x>0. For an induced subgraph H containing u,b define Z_H(u,b) as the sum of x^(number of edges) over all vertex-simple paths u to b in H. Set Z_H(b,b)=1 (the empty tail). Give a-b paths in G probability x^length/Z_G(a,b).

Let A be a set of vertices excluding a,b. Let F_n reveal the path through v_n, stopping and padding the filtration once b is reached. Until that time let H_n=G minus {v_0,...,v_(n-1)}, keeping the current tip v_n. Define

M_n = 1{v_0,...,v_n avoid A} Z_(H_n minus A)(v_n,b)/Z_H_n(v_n,b).

The denominator is positive for every realized prefix. At the terminal time define M_n=1{the complete path avoids A}.

Proof: every compatible completion of the prefix has weight x^n times its tail weight. Cancelling x^n gives precisely the normalized tail SAW measure in H_n. Filtering its completions to avoid A gives the displayed ratio if the prefix has avoided A, and zero otherwise. Consequently M_n=E[1{omega avoids A}|F_n]. Thus 0<=M_n<=1, (M_n) is a martingale, and bounded optional stopping applies to every stopping time bounded by the finite maximum path length. At time zero,

P_G(omega avoids A)=Z_(G minus A)(a,b)/Z_G(a,b).

For a nonterminal tip u the exact recursion is Z_H(u,b)=x sum_(v neighbour u in H) Z_(H minus {u})(v,b). Therefore the conditional probability of next vertex v is x Z_(H minus {u})(v,b)/Z_H(u,b), with zero tails assigned zero probability. This supplies the filtration argument rather than an independence assumption.

Scope: established here for every finite graph and x>0. It supplies neither a conformal asymptotic for its initial value nor mesh-uniform geometric bounds. It is elementary and no literature novelty is claimed.
