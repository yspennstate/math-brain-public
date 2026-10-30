SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T15:36:36Z.
attacking: the r32 aggregate-E2/rank-two-tube survivor — split aggregate second compound into residual E3, a genuine two-direction core, or a rank-one tube, then test the partner stars against the actual top-two singular spaces without selecting one minor.

# Early substantive checkpoint

First unpaid implication targeted: `QFORM-R32-R2TUBE-TRANSVERSE-STAR-OR-BIALIGNED-v1`.

Let `K` be an ORIGINAL-coordinate physical cross block and let `0<Omega<=E2(K)`. Write its singular values as `s1>=s2>=...`, `xj=sj^2`, and `T2=sum_{j>=3} xj`. The compound-tail identity

`T2 E2(K) <= 3 E3(K)`

implies the following dimension-free trichotomy. With the fixed thresholds used below, at least one holds:

1. `E3(K) >= Omega^(3/2)/192`;
2. `s1^2 s2^2 >= Omega/64` and `dist_F(K,rank<=2)<Omega^(1/4)/8`;
3. `dist_F(K,rank<=1)<3 Omega^(1/4)/8`.

Proof: if (1) fails, `T2<Omega^(1/2)/64`. If also `s1^2 s2^2<Omega/64`, then `s2^2<Omega^(1/2)/8`, hence

`dist_F(K,rank<=1)^2=s2^2+T2<9 Omega^(1/2)/64`.

There is also an exact row-augmentation identity. For any physical row vector `r` on the column coordinates of `K`, let `v_j` be right singular vectors, completed through the nullspace. Then

`E3([r;K]) = E3(K) + sum_j |<r,v_j>|^2 e2(x_1,...,hat{x_j},...)`.

In particular, if `V2=span(v1,v2)` and `p=s1^2 s2^2`,

`E3([r;K]) >= E3(K)+p dist(r,V2)^2`.

The transposed statement holds for an appended physical column. Therefore in branch (2), if a partner star `r` has `dist(r,V2)>=||r||/4`, then

`E3([r;K]) >= ||r||^2 Omega/1024`.

Applying the completed D' theorem from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` to this actual augmented cross block, whenever either orientation of its natural third-volume law has all inclusion marginals at most `2/3`, gives the full-ambient curvature-safe bound

`||p_Q||_inf <= 9 sqrt(3e) (||r||^2 Omega/1024)^(-1/6)
              <81.596 (||r||^2 Omega)^(-1/6)`.

If its determinant volume is concentrated on bounded original-coordinate supports, the existing B07 aggregate-support-to-physical-core theorem instead produces an actual bounded physical principal core with three singular/eigen directions and pays by the fixed-dimensional spectral receiver.

Thus the genuinely new survivor of the r32 aggregate-E2 branch is not an arbitrary rank-two tube: after the residual-E3 and rank-one alternatives are separated, either a transverse star regenerates third volume, or the star is quantitatively aligned with the top-two singular space. With two partner stars on opposite orientations, the terminal geometric state is bi-aligned (or a coheavy E3 packet that descends by the existing anchor machinery).

Designated-partner source actually used: fleet03/B07 r32, `math-open-problems@b684b8edb29274a17fd5e8ed7fc8049ce12a4595`, whose r30 six-bank aggregate branch supplies two disjoint physical star banks and aggregate literal second-minor mass `Omega` with `S_L S_R sqrt(Omega)>a^4/(6912 sqrt(6))`.

This checkpoint is a supporting lemma/branch reduction, not a full proof. Full QFORM remains OPEN; continuity remains separate.
