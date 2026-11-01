SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-23T13:37:27Z.
attacking: the heavy third-volume / dominant-pivot transport-failure collar by compiling it to a fixed double-anchor packet before any reciprocal-minor payment.

# Early checkpoint: heavy-star strip concentration forces a double anchor

Full QFORM remains OPEN.  This checkpoint records the first substantive implication of this run.

Let `B=A[I,J]` be an ORIGINAL-coordinate physical cross block and `Z=E3(B)>0`.  Apply the completed fleet03/B02 r30 theorem at `q=4/3`.  Unless the sharp-Hausdorff--Young D' exit already gives

`||p_Q||inf <= (9 sqrt(3)e/2) Z^(-1/6)`,

there are a physical row anchor `i` and column anchor `j` with joint incident third-volume

`J_ij > Z/3`.

Normalize the determinants counted by `J_ij` to a probability law on residual row pairs `R` and residual column pairs `T`.  Let `H` and `K` be fixed two-element physical row/column sets, disjoint from `i,j`.  Suppose the earlier incident-(3+2) transport exit against the fixed `H x K` pivot fails on both banks:

`P(R cap H = empty)<1/4`,  `P(T cap K = empty)<1/4`.

Then with probability `>1/2` both `R cap H` and `T cap K` are nonempty.  Summing over the four pairs `(h,k) in H x K`, every determinant in that event is counted at least once.  Hence for some `h in H`, `k in K`,

`G_{ih;jk}:=sum_{p,q} det B[{i,h,p},{j,k,q}]^2 > J_ij/8 > Z/24`.

This is a fixed double-anchor packet, not a single-minor claim.  If `P0=B[{i,h},{j,k}]` were zero, every 3x3 determinant containing these two rows and columns would vanish (the first two rows of the corresponding 3x3 block would be supported on one remaining column), contradicting `G_{ih;jk}>0`.  Thus `rank(P0)>=1`.

If `P0` is invertible and `S0` is its algebraic cross-Schur residual, Cauchy--Binet/block determinant expansion gives the exact identity

`G_{ih;jk}=|det P0|^2 ||S0||_F^2 > Z/24`.

If `rank(P0)=1`, choose a nonzero scalar entry `p` of `P0` and take the corresponding scalar cross-Schur residual `S1`; the determinants in `G_{ih;jk}` form a subset of the scalar-pivot 2-minor family, so

`p^2 E2(S1) >= G_{ih;jk} > Z/24`.

Therefore the transport-failure collar has been reduced to an invertible double-anchor Frobenius-Schur packet or a singular-rank-one scalar-pivot E2 packet.  No post-shear independence, fixed-good-minor inference, or small-tail deletion is used.
