# C0120: source-faithful statement (2026-10-10)

Let (g_v) indexed by v in Z^2 be independent standard normal random variables. Let P_n be the finite set of n-vertex paths p=(v_0,...,v_{n-1}) with v_0=(0,0) and increments (1,0) or (0,1). The endpoint is free. Put M_n=max_{p in P_n} sum_{v in p} g_v; the minimum energy is -M_n. The source proves Var(M_n)<=C n/log n. A precise power-improvement target is: find epsilon>0 and C<infinity such that Var(M_n)<=C n^(1-epsilon) for every n>=2.

Primary source: Sourav Chatterjee, *Chaos, concentration, and multiple valleys*, arXiv:0810.4221v2 (2008), section 8, Theorem 8.1 (pp. 37-38); section 12, problem (3) (p. 59). Short source excerpt: "Improve the fluctuation exponent in directed polymers. The current proof via hypercontractivity gives only a log n correction."

Scope correction: the local C0120 row substitutes Var(log Z_n) and general dimension. Those extensions are not the model of source Theorem 8.1. The neighboring problem (2) asks separately about dimensions >=3. Positive temperature, arbitrary weights, and higher dimension require their own statements and sources.

Current openness: UNKNOWN as of this session. The dated ranking is not evidence of present openness; no novelty or solved-status claim is made.

Independent lemma boundary, stated before reading peer proofs: determine whether a small first Gaussian chaos, independent Gaussian vertex weights, fixed path length, a common root, and uniformly bounded outdegree imply a polynomial variance gain. Proposed obstruction family: a depth-r binary tree followed by 2^r disjoint chains of length 2^r. Adversary w496 receives this statement before the proof packet.
