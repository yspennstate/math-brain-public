# Printed lower-exponent convention versus a bounded law

Draft exact boundary-case derivation, w382, 2026-10-10. Independent referee w383 must check it. This does not compute an asymptotic exponent and does not settle P0110.

Let d>=2 and let every nearest-neighbor edge weight be in [a,b] with 0<a<=b<3a. In particular, iid Uniform[1,2] meets this condition. For any adjacent vertices x,y, the direct edge has passage time at most b. Every alternative path has at least three edges: the lattice is bipartite, and a path between neighbors has odd length. Positive weights remove any advantage from loops. Every alternative therefore has passage time at least 3a>b. The unique minimizing path is the direct edge for every environment in this support class.

Consequently D(0,e_1)=0, where D is the maximum distance from any minimizing path to the segment [0,e_1]. Thus for every real s,

inf_{v in Z^d except 0} E D(0,v)/|v|^s = 0.

As literally printed, Auffinger--Damron arXiv:1109.0523v2 equation (2.2), PDF page 4, requires that infimum to be strictly positive for each exponent below xi_b. No real xi_b can satisfy that printed all-nonzero-displacements convention for Uniform[1,2]. This is a failed hypothesis application, not a contradiction of their conditional theorem.

Chatterjee's published Theorem 1.1 instead requires its lower estimates only outside a sufficiently large ball. The finite adjacent-vertex obstruction does not contradict that asymptotic convention. Uniform[1,2] belongs to the nearly-gamma class named by that theorem, so it is possible to choose Chatterjee's exact sufficient route without silently weakening the printed Auffinger--Damron premise. Matching the asymptotic global exponent pairs is still unproved here.

Review implication: w381 L1--L5 remain valid for Uniform[1,2], but 'eligible law' should mean the weight-support assumptions only, not all the global-exponent assumptions of the printed Auffinger--Damron statement. A modified lower-bound convention needs explicit justification before invoking that theorem; using Chatterjee's stated large-distance convention keeps the theorem statement intact.

Primary references: https://arxiv.org/pdf/1109.0523 Eq. (2.2); https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf Theorem 1.1, (A4).
