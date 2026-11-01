# P0297 independent obstruction, saved before reading w519

2026-10-10. Worker w520; referee w521. No paired proposed proof has been read at this checkpoint. Current openness is UNKNOWN pending dated primary-source and owner-work checks. No exact dimension formula is claimed.

The target is to compute the deterministic number d_gamma = dim_H(C,D_h) for the canonical subcritical gamma-LQG metric, 0 < gamma < 2, with h a normalized whole-plane GFF. The special value gamma = sqrt(8/3) has dimension 4. Multiplication of the metric by a deterministic positive normalization constant does not change dimension. A rigorous metric construction, rather than the formal tensor exp(gamma h)|dz|^2, is required.

Independent method: test whether field-shift covariance and multifractal identities identify a metric exponent, by constructing transformations that preserve those identities while changing dimension. This uses metric gauge/covering arguments rather than attempting a shortest-path recursion.

Lemma candidate (elementary, awaiting independent review). For any metric D on X and 0 < a < 1, D^a is a metric with the same topology and dim_H(X,D^a) = dim_H(X,D)/a. For any cover by sets U_i, diam_{D^a}(U_i) = diam_D(U_i)^a, hence H^s_{D^a,delta}(X) = H^{as}_{D,delta^{1/a}}(X). Passing to zero mesh proves the dimension identity, including zero and infinity. The triangle inequality follows from (u+v)^a <= u^a+v^a.

If a metric family satisfies D_{h+c} = exp(xi*c) D_h for constant c, then its snowflake satisfies (D_{h+c})^a = exp(a*xi*c) D_h^a. If xi*d = gamma, then (a*xi)*(d/a) = gamma too. Any exact coordinate-change identity for the unweighted distances is preserved upon raising both sides to a. Consequently these scalar identities and area scaling alone cannot choose xi or d.

Boundary of this obstruction: D^a is generally not a length metric and does not satisfy the full pathwise Weyl-scaling axiom of LQG. On an interval with D(s,t)=|s-t|, EVERY continuous path from 0 to 1 hits the levels k/n in their order (choose successive first hitting times). The corresponding partition has D^a-length at least n^(1-a), which diverges. Thus every such path has infinite length, while D^a(0,1)=1. This is a counterexample to deriving an exact dimension from reduced scaling hypotheses; it is not a second LQG metric or a counterexample to metric uniqueness.

Primary references recovered so far: Ding-Gwynne arXiv:1807.01072 (dimension exponent); Gwynne-Pfeffer arXiv:1905.11790 (metric KPZ and metric Hausdorff dimension); Ding-Dubedat-Gwynne arXiv:2109.01252 (LFPP construction and open problems). Exact numbered statements and local prior lanes still to be checked.

Single hardest piece: obtain an independently determined exact normalization exponent for LFPP crossings (or a comparable genuine geodesic estimate). The identity xi = gamma/d_gamma is a reparametrization, not an evaluation. Thick-point counts or the scalar field-shift identity alone leave that exponent free.

NEXT: Verify the numbered LFPP/KPZ statements and prior attempts, then audit w519's actual central implication against this independently saved obstruction.

Completion note (2026-10-10): Numbered primary statements and the original Rhodes-Vargas 2025 intake source are now verified in SOURCE_STATUS.json. The read-only canonical store already had an attempt explaining that scalar shifts give xi*d=gamma but do not calculate xi. This saved route adds a snowflake cover countermodel, while INDEPENDENT_DERIVATION.md adds the explicit thick-point completed-square deficit. w519's available original W519-L1 was independently checked and kept narrowly; no full candidate proof was present. The final next step is w521's check of claims .002 and .003.
