# PROB10-04 idea before code — exact two-neighbor blocker occupancy

Model stays the classical iid proper random 3-SAT model from `operations/PROB10_2026-09-20.md`. Source metric remains the explicitly certified bracket `[3.52,4.4898]`, width `0.9698`; this note does **not** claim a source-level improvement.

## Why this is a genuine method change after run 3

The previous run proved that a global Hamming-weight maximum cannot contain a **clean rescue center**, but paid for absence of such centers with a McDiarmid bound of order `c0^2`, yielding only about `3.8e-9 n` in the example `alpha=4.4898, rho=0.46`. The bottleneck was not scarcity of candidate centers; it was the square-loss from concentrating their total count.

This run changes representation. Condition on a fixed assignment `sigma` satisfying all clauses. A clause is **critical at v** when its unique true literal is at `v`. Let `K_v` be the number of critical clauses at `v`. For a zero variable `x` with `K_x=1`, let `N_x` be the two false-variable positions in its unique blocker. For a one variable `y` with `K_y=0`, call `y` available. A raw rescue center is an available `y` lying in `N_x cap N_z` for two distinct zero leaves `x,z` with `K_x=K_z=1`.

The key observation is that, conditional on the critical-source count vector, the `N_x` for eligible leaves are independent uniform 2-subsets of `[n]\{x}`. Because leaves lie in the zero set and centers in the one set, every available center is admissible for every eligible leaf. Thus the dependence problem becomes an **exact occupancy problem in which every leaf throws two distinct balls into the center bins**.

## Exact finite no-collision count to derive

If there are `L` eligible zero leaves and `A` available one-centers, set `B=n-1-A`. The total number of target-pair choices is

`C(n-1,2)^L`.

For no available center to be selected by two different leaves, classify leaves into:

- `s` leaves choosing two available centers;
- `t` leaves choosing exactly one available center;
- `L-s-t` leaves choosing none.

Writing `h=2s+t`, injectivity of all available-center choices gives the exact count

`N0(n,L,A) = sum_{s,t: s+t<=L, 2s+t<=A} [L!/(s!t!(L-s-t)!)] (A)_h 2^{-s} B^t C(B,2)^{L-s-t}`.

Hence

`P0(n,L,A)=N0(n,L,A)/C(n-1,2)^L`.

This count retains both false neighbors of every blocker. It is strictly stronger than the one-neighbor thinning and the disjoint-triple occupancy bound from earlier runs.

## Asymptotic rate to prove

With `L/n -> ell`, `A/n -> a`, put `r=ell-u-v`, `h=2u+v`, `b=1-a`. Stirling gives

`Psi(ell,a)=max Phi(u,v;ell,a)`

over `u,v,r>=0`, `h<=a`, where

`Phi = ell H_3(u/ell,v/ell,r/ell)
       + a log a - (a-h)log(a-h) - h
       + (2r+v)log(1-a) + v log 2`.

The stationarity equations reduce to one scalar parameter. With

`q=(a-h)/(1-a)`, they imply

`u:r:v = q^2:1:2q`,

hence

`r=ell/(1+q)^2`, `v=2 ell q/(1+q)^2`, `u=ell q^2/(1+q)^2`, `h=2 ell q/(1+q)`

and `q` is the positive root of

`(1-a)q^2 + (1-2a+2ell)q - a = 0`.

Therefore the no-collision exponent is explicit: `kappa_2(ell,a)=-Psi(ell,a)>0` whenever `ell,a>0`.

For the conditioned random-3-SAT blocker process,

`lambda=3 alpha/7`,
`ell=rho lambda exp(-lambda)`,
`a=(1-rho) exp(-lambda)`.

At the run-3 comparison point `alpha=4.4898, rho=0.46`, preliminary hand arithmetic gives `ell≈0.12922`, `a≈0.07884`; the expected rate is around `2e-3`, many orders larger than the prior `3.8e-9` concentration penalty. This numerical size is only a target until the checker is run.

## Interference issue and planned proof repair

A raw collision alone is not enough: the previous run gave an exact counterexample mechanism via a clause with at least two initially true literals inside the flip triple. The repair here is to keep the interference explicitly.

If there are `R` raw centers, the bipartite leaf-center graph has leaf degree at most two and every raw center degree at least two. A greedy packing selects at least `R/3` raw centers with pairwise disjoint two-leaf stars. The corresponding 3-variable flip sets are disjoint. A noncritical clause can spoil at most one such disjoint star, and for any fixed star its conditioned interference probability is `O(n^-2)`. Thus if `R` is linear, making every packed star dirty requires linearly many distinct rare interference clauses, a superexponentially unlikely event. Consequently the exponential cost of having no **clean** center is governed by the occupancy rate, not by the old `c0^2` bounded-difference loss.

## Three attacks in this run

1. **Exact two-neighbor occupancy / blocker graph** — main route above; derive and verify the finite count and asymptotic saddle.
2. **Díaz near-maximizer insertion** — once the occupancy penalty is parameterized by blocker densities rather than a single `rho`, identify the exact extra coordinates needed to attach it to the Díaz configuration objective. This is the source-relevant route; no endpoint movement is claimed until the uniform insertion is proved.
3. **1RSB/interpolation baseline certification** — current 2026 literature says interpolation gives a rigorous variational upper bound matching the 1RSB prediction, but the displayed `d_sat(3)≈12.801` value is still presented as the physics prediction. Do not replace `4.4898` in the explicit-decimal fleet metric until the k=3 variational evaluation itself is reconstructed and interval-certified.

Negation test: the route must survive formulas with raw rescue collisions spoiled by higher-truth clauses. Therefore the report will not equate raw and clean centers; it will prove the disjoint-star interference payment separately.