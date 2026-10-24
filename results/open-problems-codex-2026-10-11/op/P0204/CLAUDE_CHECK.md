# P0204: third check (claude-322bc92e, 11 Oct 2026 23:0x)

Verdict: PASS. Settled for the walk Peres asked about. Chen and Peres, arXiv:2609.16515v2 (preprint, September 2026; abstract read from arXiv, which lists Yuval Peres as co-author), prove that the lazy walk on the cube censored to an increasing set A mixes in time at most K mu(A)^-3 n log(en). At density at least 1/2 this is O(n log n). The question is about the degree-weighted induced-subgraph walk, and the solver's section 4 transfer to it is correct. I checked each step:
- the average induced degree is at least N - sqrt(N) by the covariance bound, so pi <= 2 mu;
- both chains share the jump chain and the censored chain holds at least as long, so hitting times only drop;
- a hitting-time bound of 48 t0 for sets of mu-mass at least 1/8 (d(3 t0) <= 1/16);
- Peres-Sousi (JTP 2015, Theorem 1.1, alpha = 1/4 < 1/2) turns that back into mixing.
Record it as solved in the literature for the censored walk, plus a routine transfer. The source is a recent preprint, not yet refereed.
