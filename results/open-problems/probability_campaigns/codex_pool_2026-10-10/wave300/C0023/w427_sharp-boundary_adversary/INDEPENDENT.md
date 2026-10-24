# Independent boundary derivation

Saved before reading any paired prover proof. Target: C0023. This is an auxiliary boundary result, with independent review pending.

Let S_k be the nearest-neighbor graph on Z x {-k,...,k}. In independent bond percolation, the event that every one of the 2k+1 edges between columns j and j+1 is closed has probability q_k=(1-p)^(2k+1). Different column interfaces use disjoint edges, so these cut events are independent.

For integer R>=1, an open path from (0,0) to x=R must cross the R interfaces 0,...,R-1; to x=-R it must cross -R,...,-1. Consequently

    P_p((0,0) connects to |x|>=R) <= 2(1-q_k)^R.

For fixed finite k and p<1 this tends to zero. An infinite cluster in S_k must have unbounded x-coordinate, since every finite x-interval contains finitely many vertices. Thus the origin cluster is finite almost surely; applying the same argument at each of the countably many vertices rules out any infinite cluster. At p=1, S_k is connected and infinite. Therefore p_c(S_k)=1 exactly.

The rate is not uniform in k: q_k tends to zero for 0<p<1. Thus a proof attempting to pass absence of percolation from every finite-width graph to its union must supply an additional uniform estimate. The exact counterexample to such a bridge and comparison with the paired proof will be saved after the relevant primary sources are checked. No conclusion about critical percolation on Z^3,...,Z^10 follows from this result alone.

NEXT: Verify the primary statement, then construct the increasing-strip obstruction and inspect the paired proof's actual limit step.
