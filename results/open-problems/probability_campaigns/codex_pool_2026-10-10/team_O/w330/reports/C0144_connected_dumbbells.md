# C0144: connected Folner geometry alone cannot ensure one internal giant

2026-10-10. Label: exact geometric lemma and conditional percolation consequence, awaiting w346 KEEP. Not a disproof of existence of a good Folner sequence.

In the nearest-neighbor square lattice, take two L by L vertex squares, [0,L-1]^2 and [2L,3L-1] x [0,L-1], and join their bottom corners by the one-vertex-wide corridor {(x,0): L<=x<2L}. The induced set F_L is connected, has volume 2L^2+L and edge boundary 10L-2. Hence its boundary/volume tends to zero: it is a connected Folner sequence.

Every path inside F_L from one square to the other must use all L+1 horizontal corridor edges. Under iid bond percolation with p<1, the probability of such a connection is at most p^(L+1), regardless of infinite-cluster uniqueness in the ambient lattice. It tends to zero, while the geometric boundary ratio does too.

The example can be nested and exhausting as well: use F_{2L} translated by (-L,-L), and L=8^n. Its first square is [-L,L-1]^2, its second is [3L,5L-1] x [-L,L-1], its corridor lies at y=-L, volume is 8L^2+2L, boundary 20L-2, and crossing needs 2L+1 open edges. At the next scale the first square already contains the entire previous set, since 5L<8L. These sets exhaust Z^2. Thus requiring a connected nested Folner exhaustion does not remove the geometric obstruction.

Conditional consequence: if each square's restricted infinite cluster has a giant of size (theta(p)+o(1))L^2, then with probability tending to one the two giants belong to different components inside F_L. The second largest is then macroscopic. With the usual stronger assumption that all other components in either square are o(L^2), their ratio tends to one and the largest density in F_L tends to theta(p)/2. This last claim explicitly depends on a finite-box giant theorem, rather than being derived solely from the corridor calculation.

Thus neither connectedness nor the Folner boundary condition alone supplies the coarse internal connectivity needed by the earlier route. The original question asks for existence of a suitable sequence, so a bad sequence on Z^2 does not answer it negatively. No unverified extension to exponential-growth amenable graphs is asserted.

Source warning: the ledger labels its locator 'Question 12.34, p.170'. The cached Pete notes instead have Exercise 12.34 on PDF page 140 about invariant finite-cluster percolation. A scan for the exact giant-component question did not locate it. This is a version/locator mismatch awaiting resolution, not a certificate that the stated question is absent from all versions or solved. The geometric lemma above is self-contained and independent of that attribution.
