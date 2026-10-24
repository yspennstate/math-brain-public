# Endpoint averaging still does not reverse current augmentation on bounded-degree trees

Author: w470, 2026-10-10. Status: author proof, independent referee w473 requested. This is a finite-tree counterexample to a graph-uniform shortcut; it does not decide C0052 or any estimate on the transitive lattice Z^3.

Let `T_{H,m}` consist of a rooted full binary tree of depth `H` with root `o`, plus a handle path `o=v_0,v_1,...,v_m=v`. Its maximum degree is three. Put the same positive Ising edge parameter `theta=log 3` on every edge, zero field, free boundary. Write `tau=tanh(theta)=4/5`, `s=sech(theta)=3/5`, and `rho=1-s=2/5`.

On a finite tree, spin two-point correlations satisfy `G(o,x)=tau^dist(o,x)`. Set `chi=sum_x G(o,x)` and sample a random endpoint `X` with probability `G(o,x)/chi`. Conditional on `X=x`, sample one random current with parity source set `o triangle x`. Define `k(v)=P(v in C_o(n))`, where the probability includes the endpoint draw.

In a tree current, an edge is odd precisely if it belongs to the unique source path. Conditional on the source pair, edge values factor independently. Every odd edge is present. An even edge is absent with probability `1/cosh(theta)=s`, so present with probability `rho`.

Write `S_H=sum_{h=0}^H (2 tau)^h` for the total two-point weight of the binary bush (including `o`) and `T_m=sum_{j=1}^m tau^j` for the handle. If `X` lies in the bush, all `m` handle edges are even, giving hit probability `rho^m`. If `X=v_j`, the first `j` handle edges are odd and the remaining `m-j` even, giving `rho^(m-j)`. Therefore the **exact endpoint-averaged identity** is

`k(v) = [S_H rho^m + sum_{j=1}^m tau^j rho^(m-j)] / [S_H + T_m]`.

For fixed `m`, `S_H -> infinity` because `2 tau=8/5>1`. Thus `k(v)/G(o,v) -> (rho/tau)^m=2^{-m}` as `H->infinity`. Taking `H=m^2` gives a single sequence of degree-three trees on which this ratio tends to zero: `sum_{j=1}^m tau^j rho^(m-j) <= sum_{j=1}^m tau^j <=4`, while `S_H >= (8/5)^H`, so

`k(v)/G(o,v) <= 2^{-m} + 4(5/8)^(m^2)(5/4)^m -> 0`.

By Aizenman's augmented-current hitting identity (5.9), averaging a source current plus an independent sourceless current against the same `G(o,x)/chi` endpoint law gives exactly `k_aug(v)=G(o,v)`. Hence even **after endpoint averaging**, no positive constant `c` can make `k(v)>=c k_aug(v)` hold for all finite connected ferromagnetic graphs of maximum degree three. The deterministic endpoint lower bound `k(v)>=G(o,v)/chi` remains true. This proof uses no claim about critical Z^3, where transitivity and a different geometry may allow a dimension-specific estimate.

NEXT: w473 checks parity factorization and the exact average; then integrate only as a scoped proof-shortcut obstruction.
