# Full boundary versus exterior boundary — a proved obstruction

This deterministic proposition prevents a mistaken combination of two partial arguments. It is not a counterexample to G0001. The full boundary of a cluster includes sites within holes; the exterior boundary in the Peierls proof is the boundary after filling those holes.

**Proposition (dimension 3).** For every real `s<4` there is a fixed integer `L≥3` and connected finite sets `K_R` containing `0`, whose hole-filled hull is the whole cube `Q_R=[-R,R]^3∩ℤ³`, such that

`|∂K_R|/|K_R| → (12L-24)/(3L-2) > s`,

while their exterior boundary `B_R` has size exactly `6(2R+1)²` and `|B_R|/|K_R| → 0`. Here `∂K_R` is the full nearest-neighbour exterior vertex boundary, including sites within holes; `B_R` is the exterior boundary of the filled hull.

**Complete proof.** Let `W_L` be the infinite periodic wire mesh of points of `ℤ³` with at least two coordinates divisible by `L`. Set

`K_R = (Q_R \ Q_{R-1}) ∪ (W_L ∩ Q_R)` for integers `R≥1`.

Every mesh point lies on a complete coordinate line whose other two coordinates are divisible by `L`. The segment of that line inside `Q_R` reaches the cube shell. That shell is nearest-neighbour connected: keep one coordinate on a face while moving the others to the positive corner, then keep a second coordinate on its face while moving the first to the positive corner. Hence every mesh point connects to a common connected shell, and `K_R` is connected. It contains `0`, a mesh point.

The entire shell belongs to `K_R`. Every component of `Q_R \ K_R` is therefore a finite complementary component, and the complement outside `Q_R` is connected. Filling all finite complementary components gives exactly `Q_R`. Its exterior vertex boundary consists of six disjoint faces, with one coordinate `R+1` or `-R-1` and the other two coordinates in `[-R,R]`. Thus `|B_R|=6(2R+1)²`.

Count sites in the period cell `{0,…,L-1}³`. Mesh sites have at least two zero coordinates. There are `3(L-1)+1=3L-2`: choose the one nonzero coordinate and its nonzero value, or take all coordinates zero.

A site outside the mesh has at most one zero coordinate. If it has none, one lattice step can create at most one zero coordinate, so it has no mesh neighbour. If it has exactly one zero coordinate, it neighbours the mesh exactly when at least one of its other coordinates is `1` or `L-1`. For each of the three choices of its zero coordinate, the number of qualifying ordered pairs is

`(L-1)²-(L-3)²=4L-8`.

The full boundary of the infinite mesh consequently has `12L-24` sites per period cell.

For fixed `L`, any residue class has `(2R+1)³/L³+O_L(R²)` occurrences in `Q_R`. For each coordinate its residue count is `(2R+1)/L` plus an error of absolute value at most one; expanding the product proves this assertion. Adding the shell changes the mesh count by `O(R²)`. Away from a fixed-width layer at that shell, membership in the full boundary of `K_R` equals membership in the periodic full boundary of `W_L`. The layer has `O(R²)` vertices; so does the exterior cube boundary. Hence

`|K_R| = [(3L-2)/L³](2R+1)³ + O_L(R²)`,

`|∂K_R| = [(12L-24)/L³](2R+1)³ + O_L(R²)`.

The first leading constant is positive. Dividing proves the asserted full-boundary ratio. Since

`(12L-24)/(3L-2) = 4 - 16/(3L-2) → 4`,

choose a fixed sufficiently large `L` making that ratio exceed `s`. Finally cubic growth of `|K_R|` and the exact quadratic formula for `|B_R|` give `|B_R|/|K_R|→0`. This proves the proposition.

**Referee checks and scope.** Connectivity includes the root and is supplied by the actual shell; it is not inferred from positive density. The full-boundary count treats all possible numbers of zero coordinates and assumes `L≥3` so the residues `1` and `L-1` are distinct. Only a fixed-width shell layer is exceptional, and its order is quadratic. Hole filling is justified because every path from the interior to infinity crosses the full shell. This is a family of deterministic connected sets, not a percolation counterexample or a new probabilistic tail estimate. Exact-cluster events still have probability `p^{|K_R|}(1-p)^{|∂K_R|}`.

In particular high FULL boundary density does not imply large EXTERIOR boundary density, nor rule out a geometrically compact filled hull. The shape comparison in ATTEMPT.md section 8 cannot simply be joined to the Peierls count in section 2 to prove the critical upper bound. Describing all high-full-boundary clusters as geometrically ramified would be incorrect.

## Generalization and sharpness in every dimension

**Proposition.** For every integer `d≥2` and every real `s<2d-2`, the same phenomenon occurs for connected rooted sets in `ℤ^d`, with full-boundary ratio approaching a value greater than `s` and exterior-boundary ratio tending to zero. Moreover `2d-2` is the largest possible asymptotic full-boundary ratio for connected sets whose sizes tend to infinity.

**Complete proof.** Let `W_{L,d}` consist of points with at least `d-1` coordinates divisible by a fixed integer `L≥3`. Enclose its restriction to `Q_R=[-R,R]^d` in the full cube shell, exactly as above. Every mesh point lies on a coordinate line reaching that connected shell, so the finite set `K_R` is connected and rooted. The shell makes its filled hull exactly `Q_R`; its exterior vertex boundary has exactly `2d(2R+1)^{d-1}` points.

In a period cell there are

`a_{L,d}=d(L-1)+1=dL-d+1`

mesh points, because at most one coordinate is nonzero. A point outside the mesh can have a mesh neighbour only if exactly `d-2` coordinates are zero; one coordinate step can increase the number of zeros by at most one. With exactly `d-2` zero coordinates, it has a mesh neighbour precisely when at least one of its two nonzero residues is `1` or `L-1`. Choose those two nonzero coordinates in `binomial(d,2)` ways; their qualifying ordered residues number `(L-1)^2-(L-3)^2=4L-8`. Thus the full-boundary count per period is

`b_{L,d}=binomial(d,2)(4L-8)=2d(d-1)(L-2)`.

Expanding the product of the `d` one-coordinate residue counts gives a main term `(2R+1)^d/L^d` and error `O_{L,d}(R^{d-1})` for each fixed residue class. The shell and its fixed-width neighbourhood also have that error order. Consequently

`|K_R|=a_{L,d}(2R+1)^d/L^d+O_{L,d}(R^{d-1})`,

`|∂K_R|=b_{L,d}(2R+1)^d/L^d+O_{L,d}(R^{d-1})`.

For fixed `L`, the full-boundary ratio tends to

`b_{L,d}/a_{L,d} = 2d-2 - 2(d^2-1)/(dL-d+1)`.

As `L→∞` this tends to `2d-2`, so a fixed sufficiently large `L` makes it greater than the prescribed `s`. The exact exterior-boundary formula divided by the positive cubic-or-higher main volume term tends to zero (the same conclusion is quadratic versus linear-boundary in dimension two).

To prove the claimed maximality, let `K` be any finite nonempty connected set of `k` lattice vertices. Its induced graph has at least `k-1` internal edges because it contains a spanning tree. Summing the lattice degree `2d` over `K`, the number of edges from `K` to its complement is therefore at most `2dk-2(k-1)=(2d-2)k+2`. Every vertex of `∂K` is the outside endpoint of at least one such edge, and distinct vertices have distinct outside endpoints, so `|∂K|≤(2d-2)k+2`. For any sequence with `k→∞` its full-boundary ratio has limsup at most `2d-2`. The construction reaches ratios arbitrarily close to this value while keeping the filled hull cubic. This completes both claims.

**Relevance to the critical comparison threshold.** The standard path count gives `p_c≥1/(2d-1)` for site percolation: an open self-avoiding path with `m` edges requires its `m+1` distinct vertices open, and there are at most `2d(2d-1)^{m-1}` such paths from `0`. Hence the probability of an open path of length `m` is at most `2d(2d-1)^{m-1}p^{m+1}`, which tends to zero when `(2d-1)p<1`. An infinite cluster contains paths of every length, so its probability is zero in that range. Thus `(1-p_c)/p_c≤2d-2`. Every cutoff `s<(1-p_c)/p_c` used in the low-full-boundary comparison is consequently below `2d-2` and is exceeded by one of these compact-filled-hull constructions. This is a deterministic limitation of the proposed method; it makes no assertion about which shapes dominate the critical tail.
