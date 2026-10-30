SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B12, 2026-09-23T14:47:37Z.
attacking: spectral-square row-energy spill: convert arbitrary extra spectrum into either a bounded physical core or cross smoothing directions without treating the spectral tail as random noise.

# Early substantive checkpoint

New deterministic mechanism (different from r32-r34 tail erosion): let A=A^T, H an ORIGINAL-coordinate set, C=A[H,H], B=A[H,H^c], and let 0<=G<=A^2 be any PSD spectral-energy certificate. If lambda_k(G[H,H])>=g^2 and c=s_{r+1}(C)<g, then

    s_{k-r}(B) >= sqrt(g^2-c^2).

Proof skeleton: (A^2)[H,H]=C^2+BB^T. Spectrally truncate C=C_r+E with rank(C_r)<=r, C_r E=0 and E^2<=c^2 I. Therefore

    BB^T+C_r^2=(A^2)[H,H]-E^2 >= G[H,H]-c^2 I,

so its kth eigenvalue is >=g^2-c^2. Since C_r^2 has rank <=r, Weyl/rank interlacing gives lambda_{k-r}(BB^T)>=lambda_k(BB^T+C_r^2), proving the claim.

For the final spectral window P=1_{|A|>=Lambda}, take G=Lambda^2 P. Every omitted eigenvalue, whether smaller or larger than a separately selected three-mode packet and of either sign, is retained in A and costs nothing in this lower bound; the argument uses the positive spectral square, not an independent quadratic remainder.

Planned analytic exits: if k-r>=5, apply the q=2 ridge theorem (no leverage gate). If k-r>=3 and the final cross-range projection has diagonal <=1/2, apply the newest fractional three-volume theorem at q=1. Partner fleet04/B12 complementary-Schur shield will be applied to an explicit physical branch inequality in the final report.

Full QFORM remains OPEN; this checkpoint is a supporting deterministic implication, not a completion claim.
