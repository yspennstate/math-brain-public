# C0120 statement-only packet

Recovered primary source: Sourav Chatterjee, arXiv:0810.4221v2 (16 December 2008), Sections 1, 8 and 12(3), printed pages 2, 37-38 and 59.

The source asks: "Improve the fluctuation exponent in directed polymers." Its proved logarithmic estimate concerns the Gaussian ground-state maximum M, not a finite-temperature log partition function.

Source model: g_v are independent N(0,1) variables on Z^2. P_n consists of every directed path p=(v_0,...,v_{n-1}), v_0=(0,0), with increments (1,0) or (0,1). The length counts n vertices, including the origin; the endpoint is free. Set M_n=max_{p in P_n} sum_{v in p} g_v. Theorem 8.1 proves Var(M_n) <= C n/log n.

Concrete objective for this lane: find epsilon>0 and C<infinity, independent of n, such that Var(M_n) <= C n^(1-epsilon) for every n>=2, or improve a precisely identified auxiliary step toward that objective. This inequality is the operational power-improvement formulation of Section 12(3), rather than a quoted formal quantifier in that section.

The source's chaos quantity is expected common-vertex overlap E|P_n(g) intersect P_n(g^s)|, where g^s=e^(-s)g+sqrt(1-e^(-2s))g' and g' is independent. A change of the maximizer alone does not assert small overlap.

Scope: the 2026-09-07 intake substitutes Var(log Z_n), general dimension and general disorder for the source's planar Gaussian ground-state setup. Those extensions need their own sources and assumptions. Current openness: UNKNOWN; the dated intake and a bounded literature search are not a current proof of openness. No parent-problem solution or novelty claim is made.

Adversary w499: first examine this statement and the overlap definition independently. The full proof packet will be sent afterward to referee w500.
