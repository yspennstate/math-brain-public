SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-24T03:54:56Z.
attacking: the fully diffuse near-coloop two-sheet survivor; test whether the single-hub mixed slice norm can be controlled from product-projection provenance, and if not isolate the exact parabolic-trace replacement.

# Early calculation

Fresh owner control is QFORM-only, revision 2026-09-22.15. Full exact rank three and full QFORM remain open.

The first tested implication is the tempting bridge

`M(rho):=sup_y int_R sup_w rho(z,y,w) dz <= C`

for a three-dimensional orthogonal projection density `rho` of an independent cap-one product law, under a diffuse row-leverage hypothesis. This would feed the current single-hub receiver directly.

I found a source-valid counterexample to that bridge. Fix `m=64`. For three blocks of `m` independent coordinates define normalized block sums `A,B,Y`, and then `Z=(A+B)/sqrt(2)`, `W=(A-B)/sqrt(2)`. The three coefficient columns for `(Z,Y,W)` are orthonormal and every physical row leverage is exactly `1/m=1/64<1/61`.

For the first `2m` source coordinates, choose cap-one densities equal to indicators of `N` intervals of length `1/N` whose centers are separated in distinct base-`B` digit scales; use ordinary unit intervals in the `Y` block. Writing `h_m` for the density of a sum of `m` independent `U[0,1]` variables, choose a fixed central interval `J` on which `h_m>=a_m>0`. Each digit vector produces a disjoint core interval for `A` (and for `B`) of length `|J|/(N sqrt(m))` and density at least `a_m sqrt(m) N^(1-m)`. The `N^(2m)` pairwise core sums are disjoint. Hence

`int sup_w p_(Z,W)(z,w) dz >= c_m N`,

with `c_m>0` independent of `N`; multiplying by a fixed positive value of `p_Y` gives `M(rho_N)>=C_m N -> infinity`.

This is only an intermediate-interface obstruction, not a QFORM counterexample. The completed account02/B10 regression-clean reservoir theorem at commit `2181d0927de1374b092152c7e6fb51920e5ae40d` will be applied to a near-coloop target built from the same block geometry in the final report, while the mixed norm still diverges.
