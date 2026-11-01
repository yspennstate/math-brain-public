# C0029 independent statement packet

Let B_n be an n by n real random matrix whose n^2 entries are mutually independent, each uniform on {-1,+1}. Define s_min(B_n)=min_{||x||_2=1} ||B_n x||_2. The coefficient-one Spielman-Teng target is: there exists an absolute q in (0,1) such that, for every positive integer n and every epsilon >= 0,

P(s_min(B_n) <= epsilon/sqrt(n)) <= epsilon + q^n.

The allowed exponential term absorbs exact singularity. Entries are unnormalized Rademacher variables of variance one; this is neither a symmetric matrix model nor a {0,1} model. Epsilon may depend on n, including exponentially small values. The inequality for epsilon >= 1 is immediate.

Source: Sah, Sahasrabudhe, Sawhney, On the Spielman-Teng Conjecture, arXiv:2405.20308v2 (8 Jan 2025), introduction eq. (2), citing Spielman-Teng's ICM 2002 survey. Their Theorem 1.1 proves coefficient 1+O((log n)^(-1/16)), not coefficient one. URL: https://arxiv.org/html/2405.20308v2 . Original-source recovery and current-status check remain in progress. Current openness: UNKNOWN (no exhaustive current-literature or owner's-retirement clearance yet).

Independent adversary: w565. Referee: w566. Read this statement before ATTEMPT.md. Requested model settings are not served-model evidence; actual author/referee response-side served identity is not yet available.

Narrow lane claimed by w564: exact, untruncated Schur-complement equivalence for adding the final independent row/column, followed by the annealed Bernoulli slab estimate at that exact threshold. This packet includes no proposed proof so the adversary can start independently.
