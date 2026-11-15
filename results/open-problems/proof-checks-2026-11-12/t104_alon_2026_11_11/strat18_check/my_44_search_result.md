# My 4+4 float search (an agent, 13 Nov 2026) - NUMERICAL, corroboration only

Script my_44_search.py (written from STRAT17 RESULT.md formula, not Codex code); output mine_44_search.out.
No negative T found anywhere.

Isolates only: k=6 0.0494 (K4+K4), k=7 ~0 (two equal edges, the known equality), k=8 0.146, k=10 0.204,
k=20 ~0 (two edges), k=1e6 0.444 (K4+K4).
With lowers, s in [0,k-7]: k=7 0.104 (optimizer missed the two-edge zero; s forced 0), k=8 ~0 (two edges, s=0),
k=10 0.0553 at s=3 (max), k=20 0.0146 at s=13 (max), k=1e6 7e-12 at s=k-7 (K4+K4).
Reading: with lowers the tight spot is K4+K4 at maximal lower trace, T decaying like the 1/M^2 normalisation
(T* at k=1e6 is about 1.7 > 0). Consistent with STRAT18's claim: strict T>0 for positive lower trace at each N,
no uniform margin as N->infinity. Same pattern as STRAT17 (K5 top at max lower trace).
