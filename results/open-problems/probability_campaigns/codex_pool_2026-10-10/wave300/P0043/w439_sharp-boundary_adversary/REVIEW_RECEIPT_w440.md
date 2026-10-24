# w440 independent review receipt for w439

Source: ~/brain_workers/w440/REVIEW_PACKET.md. Recorded 2026-10-10T05:38:25.291541+00:00. These sections record the referee's verdict; this is not a review of that review. Source correction 004 is not included in this receipt.

## w439-P0043-boundary-001 — KEEP (boundary calculation only)

The same independent calculation reproduces the exact p_c=1 and theta(1)=1 assertions. Its source caveat is accurate, and its status as a boundary counterexample is appropriate. It overlaps w438-C01; count it as a second derivation, not a second mathematical result. Remaining parent gap: all quasi-transitive graphs with p_c<1.

## w439-P0043-boundary-002 — KEEP (uniformity obstruction)

In the L-subdivision of the 3-regular tree, each replaced edge is open with probability p^L, independently across original edges. Thus p_c=2^(-1/L). For fixed n<=L, the three edge-disjoint initial arms each reach ambient distance n with probability p_c^n=2^(-n/L), giving a_L(n)=1-(1-2^(-n/L))^3. It tends to 1 as L grows with n fixed. The supremum is 1; this only excludes graph-independent one-arm bounds.

## w439-P0043-boundary-003 — KEEP (quantitative tree special case)

At p_c each coarse edge is open with probability 1/2. A forward branch reaches k levels with u_0=1 and u_(k+1)=1-(1-u_k/2)^2=u_k-u_k^2/4. The sequence decreases to 0, and 1/u_(k+1)-1/u_k=1/[4(1-u_k/4)] tends to 1/4; Cesaro averaging yields k u_k -> 4. The root has three arms, so q_k=1-(1-u_(k-1)/2)^3 and k q_k ->6; ambient radius is kL, giving (kL)q_k ->6L. There are 3*2^(k-1) original vertices on shell k, each linked to the root with probability 2^(-k), so each shell contributes 3/2 to susceptibility. This verifies the divergence and shows why infinite susceptibility does not imply critical percolation. Countability upgrades root extinction to almost-sure absence of any infinite cluster.

No full P0043 solution, novelty certification, served-account certification, or formal proof receipt is claimed.
