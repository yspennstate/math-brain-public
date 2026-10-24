# P0195 low-temperature communication-barrier route

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-06`
Source: `P0195` — LPW ferromagnetic Ising spectral-gap edge-addition clause
Frozen metric: `n_edge^* >= 6`

## Idea before code

The previous six-vertex cutwidth census found 240 marked edge additions with strict cutwidth increase and 162 cutwidth ties. Cutwidth alone did not imply the desired spectral-gap ordering because the earlier argument supplied only a one-sided relaxation-time estimate.

Recast the finite-temperature chain as a weighted walk on the configuration hypercube. If `S` is the set of minus spins relative to all-plus, put

`h_G(S) = |delta_G(S)|`,

so the Ising weight, after removing the common ground-state factor, is `a_beta(S)=exp(-2 beta h_G(S))`. For adjacent configurations `S,T=S triangle {v}`, detailed balance gives the exact heat-bath conductance

`Q_beta(S,T) = [1/(n Z_beta)] * a_beta(S)a_beta(T)/(a_beta(S)+a_beta(T))`.

Hence `Q_beta(S,T)` is within a factor two of `(n Z_beta)^(-1) exp(-2 beta max(h_G(S),h_G(T)))`.

Define the communication barrier

`b(G) = min_{hypercube paths gamma: empty -> V} max_{S in gamma} h_G(S)`.

Two complementary bounds should then be enough:

1. A sublevel-component indicator gives `gap_G(beta) <= C_n exp(-2 beta b(G))`.
2. Canonical paths obtained by flipping disagreements in one optimal cutwidth ordering give `gap_G(beta) >= c_n exp(-2 beta cw(G))`.

The key deterministic inequality for the second step is: if `Z` is an intermediate configuration on the ordered path from `X` to `Y`, then

`h_G(Z) <= h_G(X) + h_G(Y) + cw(G)`.

Therefore, for a marked edge addition `H=G+e`, any strict separation

`b(H) > cw(G)`

forces `gap_H(beta)/gap_G(beta) -> 0` as `beta -> infinity`, and hence the LPW edge-addition inequality is eventually strict at low temperature.

The finite question worth checking is now exact and source-relevant: on all connected six-vertex graphs, is the hypercube communication barrier `b(G)` equal to graph cutwidth? If yes, every one of the 240 strict-cutwidth marked transitions from the existing census gets a rigorous low-temperature spectral-gap theorem. The 162 ties are then identified as the exact obstruction to this route rather than merely a heuristic failure.

Methods reused transparently because all thirty Section-B methods have already been used on P0195: #18 SAY IT IN ANOTHER LANGUAGE, #16 COMPUTE EVERY SMALL CASE, #20 FIND WHY THE ALGORITHM FAILS.
